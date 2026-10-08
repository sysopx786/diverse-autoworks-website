# -*- coding: utf-8 -*-
"""
Static site generator for Diverse Autoworks (English at /, Spanish at /es/).

Usage:
    python3 tools/build.py                      # builds into ./docs
    SITE_URL=https://example.com python3 tools/build.py
    FORM_ENDPOINT=https://formspree.io/f/xxxx python3 tools/build.py

SITE_URL      Final public address (no trailing slash, include repo path for GitHub Pages
              project sites). When empty, canonical/hreflang/sitemap/og:url are NOT written
              (they must never point at the wrong domain).
FORM_ENDPOINT Approved form-handling endpoint (e.g. Formspree). When empty, the request form
              prepares an email to the shop's address instead of posting anywhere.
"""
import html
import json
import os
import posixpath
import sys

sys.path.insert(0, os.path.dirname(__file__))
from content import *  # noqa
from notary import NOTARY  # noqa
import graphics as G
import reviews_es as RES

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs"))
SITE_URL = os.environ.get("SITE_URL", "").rstrip("/")
FORM_ENDPOINT = os.environ.get("FORM_ENDPOINT", "").strip()
FORM_PROVIDER = os.environ.get("FORM_PROVIDER", "Formspree")
LANGS = ("en", "es")

B = BUSINESS
PHONE = B["phone_display"]
TEL = "tel:" + B["phone_tel"]
MAIL = "mailto:" + B["email"]
ADDR_ONE = f'{B["street"]}, {B["city"]}, {B["state"]} {B["zip"]}'
MAPS_Q = B["maps_query"].replace(" ", "+")

# ------------------------------------------------------------------ SHOP HOURS (header open/closed status)
# THE one place to edit hours. The header strip reads this, in the shop's own time zone (never the visitor's clock).
#   hours: 24-hour "HH:MM"; several ranges per day allowed, e.g. [["08:00","12:00"],["13:00","17:00"]]; [] = closed all day.
#          Ranges must end the same day (no overnight ranges).
#   closedDates: whole days closed, "YYYY-MM-DD" (holidays, vacation).
#   sample: True while the hours below are PLACEHOLDERS. The strip then shows a "Sample" tag. Set False once the hours are real.
SHOP = {
    "timeZone": "America/New_York",
    "closingSoonMinutes": 60,
    "sample": False,
    "hours": {
        "mon": [["08:00", "17:00"]], "tue": [["08:00", "17:00"]], "wed": [["08:00", "17:00"]],
        "thu": [["08:00", "17:00"]], "fri": [["08:00", "17:00"]], "sat": [], "sun": [],
    },
    "closedDates": [],
}
DIRECTIONS = "https://www.google.com/maps/search/?api=1&query=" + MAPS_Q.replace(",", "%2C")
MAP_EMBED = "https://www.google.com/maps?q=" + MAPS_Q + "&output=embed"

SLUGS = {  # slug -> directory path (English)
    "home": "", "services": "services", "inspections": "inspections", "fleet": "fleet-repairs",
    "about": "about", "reviews": "reviews", "faq": "faq", "contact": "contact", "privacy": "privacy",
}
# the content.py key "fleet" for page copy; map slug key -> PAGES key
PAGEKEY = {k: k for k in SLUGS}

UI = {
    "en": {
        "skip": "Skip to content", "menu": "Menu", "back_top": "Back to top",
        "search": "Search", "search_label": "Search the site", "search_ph": "Search services, inspections, notary…", "search_close": "Close",
        "search_none": f'No match. Call <a href="{TEL}">{PHONE}</a> and we will point you to the right service.',
        "status": {"open": "Open now · closes {time}", "soon": "Closing soon · closes {time}", "closed": "Closed · opens {when} {time}",
                   "never": "Closed · call for hours", "today": "today", "tomorrow": "tomorrow", "am": "AM", "pm": "PM", "sample": "Sample",
                   "days": ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]},
        "nav": {"services": "Services", "inspections": "Inspections", "fleet": "Fleet Repairs", "about": "About",
                "reviews": "Reviews", "faq": "FAQs", "contact": "Contact"},
        "call": f"Call {PHONE}", "call_short": "Call", "request": "Request an Appointment", "directions": "Get Directions",
        "home_label": "Diverse Autoworks home", "lang_label": "Language", "main_nav": "Main navigation",
        "hours_shop": "Shop open Monday–Friday. Call for current hours.", "hours_notary": "Notary: Monday–Friday, 8 a.m.–3 p.m.",
        "hero_types_lead": "State inspections for", "types": ["Cars", "Trucks", "Trailers", "Motorcycles"],
        "gauge_aria": "Decorative engine gauge. Press and hold to rev the needle.", "gauge_hint": "Press and hold the gauge",
        "gauge_top": "Diverse Autoworks", "gauge_sub": "Phoenixville, PA",
        "pick_h": "What's your vehicle doing?", "pick_p": "Pick what you notice and we will point you to the right service.",
        "pick_group": "Vehicle symptoms and needs", "pick_empty_h": "Pick an option", "pick_empty_p": "The matching service shows up here, with a one-tap way to send a request.",
        "pick_request": "Request this service", "pick_learn": "See details", "pick_call": f"Call {PHONE}",
        "all_services": "See all services", "more_reviews": "Read more reviews", "full_reviews": "Read the full reviews on",
        "notary_nav": "Notary Services", "source": "Source", "fleet_btn": "Fleet repairs", "notary_btn": "Notary hours and details", "email_us": "Email the shop",
        "close_hours": "Hours", "close_addr": "Address", "close_mail": "Email", "close_notary": "Notary services",
        "moto_init": "Tap a numbered point to see which items PennDOT lists.", "moto_sel": "Selected:",
        "moto_listed": "listed by PennDOT among the items covered in a motorcycle safety inspection.",
        "moto_aria": "Motorcycle diagram with the PennDOT-listed inspection items marked",
        "moto_caveat": "An inspection evaluates the required safety components; it is not the same as a complete engine-service appointment.",
        "faq_search": "Search the questions", "faq_search_ph": "Search, for example brakes or notary", "faq_all": "All", "faq_count": "{n} questions",
        "faq_none_h": "No question matches that.", "faq_none_p": f"Call {PHONE} and we will answer it.",
        "faq_related": "Related questions", "faq_more": "More questions and answers", "faq_cats": "Question categories",
        "svc_index": "On this page", "svc_details": "Details", "svc_request": "Request this service",
        "contact_phone": "Phone", "contact_email": "Email", "contact_addr": "Address", "contact_hours": "Hours",
        "contact_hours_p": "Shop open Monday–Friday. Call for current hours.",
        "map_t": "Directions to the shop", "map_small": "The map loads from Google only after you choose to load it.",
        "map_load": "Load the map", "map_open": "Open in Google Maps", "map_title": "Map showing Diverse Autoworks at 1415 Pawlings Road, Phoenixville",
        "about_range": ["Everyday maintenance", "Brakes", "Tires and alignments", "Engine analysis", "Steering and suspension",
                        "A/C and cooling-system service", "Fleet repairs", "Motorcycle state inspections", "Weekday notary services"],
        "foot_pages": "Pages", "foot_visit": "Visit", "foot_contact": "Contact", "foot_privacy": "Privacy notice",
        "foot_copy": "Diverse Autoworks, Inc. All rights reserved.", "back_top": "Back to top",
        "form": {
            "name": "Name", "phone": "Phone", "email": "Email", "contact": "Best way to reach you", "p_phone": "Phone", "p_email": "Email",
            "vehicle": "Vehicle (year, make, model)", "service": "Service", "svc_pick": "Choose a service", "svc_other": "Something else", "svc_unsure": "I'm not sure",
            "msg": "What is going on?", "msg_help": "What you noticed, when it happens, and whether a warning light is on.",
            "date": "Preferred date", "fleet": "Number of business vehicles", "optional": "optional",
            "notice": "Your request is not a confirmed appointment. The shop will contact you to confirm availability.",
            "safe": "Please do not include payment card details or the contents of personal documents.",
            "submit_mail": "Prepare email request", "submit_post": "Send request",
            "mail_note": "This opens your email app with the details filled in. Nothing is sent until you press Send there.",
            "privacy": "How we handle your information",
        },
        "js": {
            "name": "Enter your name.", "either": "Enter a phone number or an email so the shop can reach you.",
            "email": "Enter a valid email address.", "phone": "Enter a phone number with area code.",
            "l_name": "Name", "l_phone": "Phone", "l_email": "Email", "l_pref": "Preferred contact", "p_phone": "Phone", "p_email": "Email",
            "l_vehicle": "Vehicle", "l_service": "Service", "l_date": "Preferred date", "l_fleet": "Business vehicles", "l_desc": "Details",
            "sent": "Request sent.", "notconf": "This is not a confirmed appointment. The shop will contact you to confirm availability.",
            "fail": f"We could not send your request. Please call {PHONE} or email {B['email']}.",
            "opened": "Your email app should open with your request.", "again": "Open the email again",
            "subject": "Appointment request", "fleet": "Fleet inquiry",
        },
        "pick_ui": {"request": "Request this service", "learn": "See details", "call": f"Call {PHONE}"},
        "faq_online": "online",
    },
    "es": {
        "skip": "Saltar al contenido", "menu": "Menú", "back_top": "Volver arriba",
        "search": "Buscar", "search_label": "Buscar en el sitio", "search_ph": "Buscar servicios, inspecciones, notario…", "search_close": "Cerrar",
        "search_none": f'Sin resultados. Llame al <a href="{TEL}">{PHONE}</a> y le indicaremos el servicio adecuado.',
        "status": {"open": "Abierto ahora · cierra a las {time}", "soon": "Cierra pronto · cierra a las {time}", "closed": "Cerrado · abre {when} a las {time}",
                   "never": "Cerrado · llame para conocer el horario", "today": "hoy", "tomorrow": "mañana", "am": "a. m.", "pm": "p. m.", "sample": "Ejemplo",
                   "days": ["el domingo", "el lunes", "el martes", "el miércoles", "el jueves", "el viernes", "el sábado"]},
        "nav": {"services": "Servicios", "inspections": "Inspecciones", "fleet": "Flotas", "about": "Nosotros",
                "reviews": "Reseñas", "faq": "Preguntas", "contact": "Contacto"},
        "call": f"Llamar al {PHONE}", "call_short": "Llamar", "request": "Solicitar una cita", "directions": "Cómo llegar",
        "home_label": "Inicio de Diverse Autoworks", "lang_label": "Idioma", "main_nav": "Navegación principal",
        "hours_shop": "Taller abierto de lunes a viernes. Llame para conocer el horario actual.", "hours_notary": "Notario: de lunes a viernes, de 8 a. m. a 3 p. m.",
        "hero_types_lead": "Inspecciones estatales para", "types": ["Autos", "Camiones", "Remolques", "Motocicletas"],
        "gauge_aria": "Medidor de motor decorativo. Mantenga presionado para acelerar la aguja.", "gauge_hint": "Mantenga presionado el medidor",
        "gauge_top": "Diverse Autoworks", "gauge_sub": "Phoenixville, PA",
        "pick_h": "¿Qué le pasa a su vehículo?", "pick_p": "Elija lo que nota y le indicaremos el servicio adecuado.",
        "pick_group": "Síntomas y necesidades del vehículo", "pick_empty_h": "Elija una opción", "pick_empty_p": "El servicio correspondiente aparece aquí, con una forma rápida de enviar su solicitud.",
        "pick_request": "Solicitar este servicio", "pick_learn": "Ver detalles", "pick_call": f"Llamar al {PHONE}",
        "all_services": "Ver todos los servicios", "more_reviews": "Leer más reseñas", "full_reviews": "Lea las reseñas completas en",
        "notary_nav": "Notario público", "source": "Fuente", "fleet_btn": "Reparaciones para flotas", "notary_btn": "Horario y detalles del notario", "email_us": "Escribir al taller",
        "close_hours": "Horario", "close_addr": "Dirección", "close_mail": "Correo", "close_notary": "Notario público",
        "moto_init": "Toque un punto numerado para ver los elementos que enumera PennDOT.", "moto_sel": "Seleccionado:",
        "moto_listed": "PennDOT lo enumera entre los elementos que cubre una inspección de seguridad de motocicletas.",
        "moto_aria": "Diagrama de una motocicleta con los elementos de inspección enumerados por PennDOT",
        "moto_caveat": "Una inspección evalúa los componentes de seguridad requeridos; no es lo mismo que una cita completa de servicio del motor.",
        "faq_search": "Buscar entre las preguntas", "faq_search_ph": "Busque, por ejemplo, frenos o notario", "faq_all": "Todas", "faq_count": "{n} preguntas",
        "faq_none_h": "Ninguna pregunta coincide.", "faq_none_p": f"Llame al {PHONE} y se la responderemos.",
        "faq_related": "Preguntas relacionadas", "faq_more": "Más preguntas y respuestas", "faq_cats": "Categorías de preguntas",
        "svc_index": "En esta página", "svc_details": "Detalles", "svc_request": "Solicitar este servicio",
        "contact_phone": "Teléfono", "contact_email": "Correo electrónico", "contact_addr": "Dirección", "contact_hours": "Horario",
        "contact_hours_p": "Taller abierto de lunes a viernes. Llame para conocer el horario actual.",
        "map_t": "Cómo llegar al taller", "map_small": "El mapa se carga desde Google solo cuando usted decide cargarlo.",
        "map_load": "Cargar el mapa", "map_open": "Abrir en Google Maps", "map_title": "Mapa con la ubicación de Diverse Autoworks en 1415 Pawlings Road, Phoenixville",
        "about_range": ["Mantenimiento diario", "Frenos", "Llantas y alineaciones", "Análisis del motor", "Dirección y suspensión",
                        "Servicio de A/C y del sistema de enfriamiento", "Reparaciones para flotas", "Inspecciones estatales de motocicletas", "Servicios de notario público entre semana"],
        "foot_pages": "Páginas", "foot_visit": "Visítenos", "foot_contact": "Contacto", "foot_privacy": "Aviso de privacidad",
        "foot_copy": "Diverse Autoworks, Inc. Todos los derechos reservados.", "back_top": "Volver arriba",
        "form": {
            "name": "Nombre", "phone": "Teléfono", "email": "Correo electrónico", "contact": "Mejor forma de comunicarnos con usted", "p_phone": "Teléfono", "p_email": "Correo",
            "vehicle": "Vehículo (año, marca, modelo)", "service": "Servicio", "svc_pick": "Elija un servicio", "svc_other": "Otro", "svc_unsure": "No estoy seguro",
            "msg": "¿Qué está pasando?", "msg_help": "Lo que ha notado, cuándo ocurre y si hay una luz de advertencia encendida.",
            "date": "Fecha preferida", "fleet": "Cantidad de vehículos de negocio", "optional": "opcional",
            "notice": "Su solicitud no es una cita confirmada. El taller se comunicará con usted para confirmar la disponibilidad.",
            "safe": "Por favor, no incluya datos de tarjetas de pago ni el contenido de documentos personales.",
            "submit_mail": "Preparar solicitud por correo", "submit_post": "Enviar solicitud",
            "mail_note": "Esto abre su aplicación de correo con los datos ya escritos. No se envía nada hasta que usted presione Enviar allí.",
            "privacy": "Cómo manejamos su información",
        },
        "js": {
            "name": "Escriba su nombre.", "either": "Escriba un teléfono o un correo para que el taller pueda comunicarse con usted.",
            "email": "Escriba un correo electrónico válido.", "phone": "Escriba un teléfono con código de área.",
            "l_name": "Nombre", "l_phone": "Teléfono", "l_email": "Correo", "l_pref": "Contacto preferido", "p_phone": "Teléfono", "p_email": "Correo",
            "l_vehicle": "Vehículo", "l_service": "Servicio", "l_date": "Fecha preferida", "l_fleet": "Vehículos de negocio", "l_desc": "Detalles",
            "sent": "Solicitud enviada.", "notconf": "Esto no es una cita confirmada. El taller se comunicará con usted para confirmar la disponibilidad.",
            "fail": f"No pudimos enviar su solicitud. Llame al {PHONE} o escriba a {B['email']}.",
            "opened": "Su aplicación de correo debería abrirse con su solicitud.", "again": "Abrir el correo de nuevo",
            "subject": "Solicitud de cita", "fleet": "Consulta de flota",
        },
        "pick_ui": {"request": "Solicitar este servicio", "learn": "Ver detalles", "call": f"Llamar al {PHONE}"},
    },
}

# ------------------------------------------------------------------ helpers
esc = html.escape


def L(d, lang):
    return d[lang]


def path_of(lang, key):
    p = SLUGS[key]
    return ("es/" + p).rstrip("/") if lang == "es" else p


def depth(lang, key):
    p = path_of(lang, key)
    return 0 if not p else p.count("/") + 1


def href(cur_lang, cur_key, lang, key, anchor="", query=""):
    cur = path_of(cur_lang, cur_key) or "."
    tgt = path_of(lang, key) or "."
    r = posixpath.relpath(tgt, cur)
    r = "./" if r == "." else r + "/"
    return r + (("?" + query) if query else "") + (("#" + anchor) if anchor else "")


def asset(cur_lang, cur_key, name):
    return "../" * depth(cur_lang, cur_key) + "assets/" + name


def img(lang, key, name, cls="", eager=False, alt=None):
    d = IMAGES[name]
    a = esc(L(d["alt"], lang), quote=True) if alt is None else alt
    c = f' class="{cls}"' if cls else ""
    return (f'<img{c} src="{asset(lang, key, "img/" + d["file"])}" width="{d["w"]}" height="{d["h"]}" '
            f'alt="{a}" loading="{"eager" if eager else "lazy"}" decoding="async">')


def abs_url(lang, key):
    p = path_of(lang, key)
    return SITE_URL + "/" + (p + "/" if p else "")


def svc_by_id(sid):
    for s in SERVICES:
        if s["id"] == sid:
            return s
    return None


def request_href(lang, cur_key, sid):
    if sid == "fleet":
        return href(lang, cur_key, lang, "fleet", anchor="request")
    return href(lang, cur_key, lang, "contact", anchor="request", query="service=" + sid)


def learn_href(lang, cur_key, sid):
    if sid == "motorcycle":
        return href(lang, cur_key, lang, "inspections", anchor="motorcycle")
    s = svc_by_id(sid)
    if s.get("page") == "inspections":
        return href(lang, cur_key, lang, "inspections")
    if s.get("page") == "fleet-repairs":
        return href(lang, cur_key, lang, "fleet")
    if s.get("page") == "contact":
        return href(lang, cur_key, lang, "contact", anchor=s.get("anchor", ""))
    return href(lang, cur_key, lang, "services", anchor=sid)


def check_parity():
    """Every user-facing dict must have both languages with non-empty text (except flagged blanks)."""
    problems = []

    def walk(o, path=""):
        if isinstance(o, dict):
            if set(o.keys()) == {"en", "es"}:
                for k in ("en", "es"):
                    if not isinstance(o[k], str):
                        problems.append(path + "/" + k)
                if o["es"] == "" and path.endswith("orig"):
                    return
                if not o["en"].strip() and not path.endswith("orig_es") and not path.endswith("orig"):
                    problems.append(path + "/en empty")
                if not o["es"].strip() and not path.endswith("orig_es") and not path.endswith("orig"):
                    problems.append(path + "/es empty")
            else:
                for k, v in o.items():
                    walk(v, path + "/" + str(k))
        elif isinstance(o, (list, tuple)):
            for i, v in enumerate(o):
                walk(v, path + f"[{i}]")

    for name in ("SERVICES", "GROUPS", "PICKER", "MOTO_PARTS", "REVIEWS", "THEMES", "FAQ_CATS", "FAQ_GENERAL", "PAGES", "NOT_FOUND", "MOTORCYCLE_SERVICE", "ASK_FAQ_CATS", "NOTARY"):
        walk(globals()[name], name)
    for k in ("en", "es"):
        pass
    if set(UI["en"].keys()) - {"faq_online"} != set(UI["es"].keys()):
        problems.append("UI keys differ: " + str(set(UI["en"].keys()) ^ set(UI["es"].keys())))
    if set(UI["en"]["form"]) != set(UI["es"]["form"]) or set(UI["en"]["js"]) != set(UI["es"]["js"]):
        problems.append("UI form/js keys differ")
    n = sum(len(c["items"]) for c in FAQ_CATS)
    if n != 36:
        problems.append(f"expected 36 service FAQs, found {n}")
    if problems:
        raise SystemExit("PARITY CHECK FAILED:\n  " + "\n  ".join(problems))


# ------------------------------------------------------------------ layout
BRAND_MARK = ('<svg class="brand-mark" viewBox="0 0 44 44" aria-hidden="true" focusable="false"><circle cx="22" cy="22" r="20.500" fill="#26282C" stroke="#E4372F" stroke-width="2"/>'
              '<path d="M8.500 29A15 15 0 0 1 35.500 29" fill="none" stroke="#D5D7DA" stroke-width="2.600" stroke-linecap="round" stroke-dasharray="1 4.300"/>'
              '<path d="M22 25L30 12" stroke="#E4372F" stroke-width="3" stroke-linecap="round"/><circle cx="22" cy="25" r="3.600" fill="#E4372F"/></svg>')


def head_tags(lang, key, title, desc, extra_ld=""):
    u = UI[lang]
    out = [
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        f"<title>{esc(title)}</title>",
        f'<meta name="description" content="{esc(desc, quote=True)}">',
        '<meta name="theme-color" content="#0F1012">',
        f'<link rel="icon" href="{asset(lang, key, "img/favicon.svg")}" type="image/svg+xml">',
        f'<link rel="preload" href="{asset(lang, key, "fonts/barlow-condensed-latin-800-normal.woff2")}" as="font" type="font/woff2" crossorigin>',
        f'<link rel="preload" href="{asset(lang, key, "fonts/barlow-latin-400-normal.woff2")}" as="font" type="font/woff2" crossorigin>',
        f'<link rel="stylesheet" href="{asset(lang, key, "css/main.css")}">',
        f'<meta property="og:title" content="{esc(title, quote=True)}">',
        f'<meta property="og:description" content="{esc(desc, quote=True)}">',
        '<meta property="og:type" content="website">',
        f'<meta property="og:site_name" content="{B["short"]}">',
        f'<meta property="og:locale" content="{"es_US" if lang == "es" else "en_US"}">',
        '<meta name="twitter:card" content="summary">',
    ]
    if SITE_URL:
        out.append(f'<link rel="canonical" href="{abs_url(lang, key)}">')
        out.append(f'<meta property="og:url" content="{abs_url(lang, key)}">')
        out.append(f'<link rel="alternate" hreflang="en" href="{abs_url("en", key)}">')
        out.append(f'<link rel="alternate" hreflang="es" href="{abs_url("es", key)}">')
        out.append(f'<link rel="alternate" hreflang="x-default" href="{abs_url("en", key)}">')
    if key == "home":
        ld = {"@context": "https://schema.org", "@type": "AutoRepair", "name": B["name"], "telephone": B["phone_tel"], "email": B["email"],
              "address": {"@type": "PostalAddress", "streetAddress": B["street"], "addressLocality": B["city"], "addressRegion": B["state"], "postalCode": B["zip"], "addressCountry": "US"},
              "inLanguage": ["en", "es"]}
        if SITE_URL:
            ld["url"] = SITE_URL + "/"
        out.append('<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>")
    if extra_ld:
        out.append(extra_ld)
    return "\n".join(out)


def flag_svg(code):
    """Round-button flag art: US flag for English, Spain flag for Spanish. Decorative (the link carries the label)."""
    if code == "es":
        art = '<rect width="44" height="44" fill="#c60b1e"/><rect y="11" width="44" height="22" fill="#ffc400"/>'
    else:
        h = 44 / 13
        stripes = "".join(f'<rect y="{i * h:.2f}" width="44" height="{h:.2f}" fill="#b22234"/>' for i in range(0, 13, 2))
        stars = "".join(f'<circle cx="{4 + c * 5.2:.1f}" cy="{4 + r * 5.6:.1f}" r="1" fill="#fff"/>' for r in range(4) for c in range(5))
        art = f'<rect width="44" height="44" fill="#fff"/>{stripes}<rect width="26" height="{7 * h:.2f}" fill="#3c3b6e"/>{stars}'
    return f'<svg class="lang-flag" viewBox="0 0 44 44" width="44" height="44" aria-hidden="true" focusable="false">{art}</svg>'


# (page key, anchor, EN title, ES title, EN keywords, ES keywords) for the header search
SEARCH_ROWS = [
    ("services", "", "Services", "Servicios", "repair maintenance all services", "reparación mantenimiento todos los servicios"),
    ("services", "maintenance", "Oil changes & maintenance", "Cambios de aceite y mantenimiento", "oil change filters cabin fuel belts wiper blades upkeep", "aceite filtros cabina combustible correas limpiaparabrisas mantenimiento"),
    ("services", "brakes", "Brakes & rotors", "Frenos y rotores", "brake rotor noise squeal grinding stopping", "frenos rotor ruido chirrido parar"),
    ("services", "tires", "Tires & alignments", "Llantas y alineación", "tire repair alignment wheel pulling uneven wear", "llantas neumáticos reparación alineación jalar desgaste"),
    ("services", "engine", "Diagnostics & engine", "Diagnóstico y motor", "engine analysis tune-up fuel injector check engine running rough diagnostics", "motor análisis afinación inyectores diagnóstico falla"),
    ("services", "suspension", "Steering & suspension", "Dirección y suspensión", "steering shocks struts ride handling loose rough", "dirección amortiguadores suspensión manejo"),
    ("services", "ac", "A/C & cooling", "A/C y enfriamiento", "air conditioning ac cooling radiator not cold", "aire acondicionado enfriamiento radiador no enfría"),
    ("services", "battery", "Batteries", "Baterías", "battery won't start no start dead", "batería no arranca no enciende"),
    ("inspections", "", "State inspections & emissions", "Inspecciones estatales y emisiones", "state inspection emissions sticker car truck trailer", "inspección estatal emisiones calcomanía auto camión remolque"),
    ("inspections", "motorcycle", "Motorcycle inspections", "Inspecciones de motocicletas", "motorcycle bike inspection", "motocicleta moto inspección"),
    ("fleet", "", "Fleet repairs", "Reparaciones de flotas", "fleet business vehicles commercial vans trucks", "flota negocio vehículos comerciales camionetas"),
    ("contact", "notary", "Notary services", "Servicios de notario", "notary notarize documents signing", "notario notarizar documentos firma"),
    ("contact", "request", "Request an appointment", "Solicitar una cita", "appointment book schedule quote request", "cita agendar presupuesto solicitud"),
    ("contact", "", "Contact, phone & hours", "Contacto, teléfono y horario", "contact phone email address hours location", "contacto teléfono correo dirección horario ubicación"),
    ("reviews", "", "Reviews", "Reseñas", "reviews ratings customers carfax yelp google", "reseñas opiniones clientes calificaciones"),
    ("faq", "", "FAQs", "Preguntas frecuentes", "faq questions answers help", "preguntas respuestas ayuda"),
    ("about", "", "About", "Nosotros", "about us shop team", "nosotros taller equipo acerca"),
    ("privacy", "", "Privacy notice", "Aviso de privacidad", "privacy", "privacidad"),
]


def search_index(lang, key):
    rows = []
    for pk, anchor, ten, tes, ken, kes in SEARCH_ROWS:
        rows.append([ten if lang == "en" else tes, href(lang, key, lang, pk, anchor=anchor), ken if lang == "en" else kes])
    rows.append([UI[lang]["directions"], DIRECTIONS, "directions map address pawlings road cómo llegar mapa dirección"])
    return rows


def header(lang, key):
    u = UI[lang]
    other = "es" if lang == "en" else "en"
    items = []
    for k in ("services", "inspections", "fleet", "about", "reviews", "faq", "contact"):
        cur = ' aria-current="page"' if k == key else ""
        items.append(f'<li><a href="{href(lang, key, lang, k)}"{cur}>{u["nav"][k]}</a></li>')
    items.append(f'<li class="nav-mob"><a href="{href(lang, key, lang, "contact", anchor="notary")}">{u["notary_nav"]}</a></li>')
    names = {"en": "English", "es": "Español"}
    sw = (f'<a class="lang" href="{href(lang, key, other, key)}" lang="{other}" hreflang="{other}" '
          f'aria-label="{u["lang_label"]}: {names[other]}" title="{names[other]}">{flag_svg(other)}<span class="lang-code" aria-hidden="true">{other.upper()}</span></a>')
    data = json.dumps({"shop": SHOP, "ui": u["status"], "search": search_index(lang, key)}, ensure_ascii=False).replace("</", "<\\/")
    search_svg = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>'
    return f'''<header class="hdr no-tr" id="hdr"><div class="wrap hdr-in">
<a class="brand" href="{href(lang, key, lang, "home")}"><img class="brand-logo" src="{asset(lang, key, "img/diverse-autoworks-logo.png")}" width="114" height="60" alt="Diverse Auto Works"></a>
<nav class="nav" id="site-nav" aria-label="{u["main_nav"]}"><ul>{"".join(items)}</ul></nav>
<div class="hdr-end">{sw}<a class="btn btn-sign btn-call" href="{TEL}" aria-label="{u["call"]}">{G.icon("phone", 22)}<span>{PHONE}</span></a>
<button class="hbtn search-btn" type="button" aria-expanded="false" aria-controls="site-search" aria-label="{u["search"]}">{search_svg}</button>
<button class="hbtn menu-btn" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="{u["menu"]}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path class="ic-bars" d="M4 7h16M4 12h16M4 17h16"/><path class="ic-x" d="M6 6l12 12M18 6L6 18"/></svg></button></div>
</div>
<div class="hdr-strip"><div class="wrap"><div class="status" id="shop-status" role="status" aria-live="polite" data-state="unknown"><i class="dot" aria-hidden="true"></i><span class="status-text">{u["hours_shop"]}</span></div></div></div>
<div class="srch" id="site-search" role="search" aria-label="{u["search_label"]}"><div class="srch-in">
<div class="srch-row"><input id="site-search-input" type="search" inputmode="search" enterkeyhint="search" autocomplete="off" placeholder="{u["search_ph"]}" aria-label="{u["search_label"]}" aria-controls="site-search-res"><button class="srch-close" type="button">{u["search_close"]}</button></div>
<ul class="srch-res" id="site-search-res"></ul>
<p class="srch-empty" id="site-search-empty" hidden>{u["search_none"]}</p>
</div></div>
<script type="application/json" id="shop-data">{data}</script>
</header>
<div class="hdr-spacer" aria-hidden="true"></div>'''


def footer(lang, key):
    u = UI[lang]
    pages = "".join(f'<li><a href="{href(lang, key, lang, k)}">{u["nav"][k]}</a></li>' for k in ("services", "inspections", "fleet", "about", "reviews", "faq", "contact"))
    return f'''<footer class="foot on-dark"><div class="wrap">
<div class="foot-grid">
<div><a class="brand" href="{href(lang, key, lang, "home")}"><img class="brand-logo foot-logo" src="{asset(lang, key, "img/diverse-autoworks-logo.png")}" width="168" height="88" alt="Diverse Auto Works" loading="lazy"></a>
<address>{B["name"]}<br>{B["street"]}<br>{B["city"]}, {B["state"]} {B["zip"]}</address></div>
<div><h2>{u["foot_pages"]}</h2><ul>{pages}</ul></div>
<div><h2>{u["foot_contact"]}</h2><ul><li><a href="{TEL}">{PHONE}</a></li><li><a href="{MAIL}">{B["email"]}</a></li><li><a href="{DIRECTIONS}" rel="noopener" target="_blank">{u["directions"]}</a></li></ul></div>
<div><h2>{u["close_hours"]}</h2><ul><li>{u["hours_shop"]}</li><li>{u["hours_notary"]}</li></ul></div>
</div>
<div class="foot-bot"><span>© <span data-year>2026</span> {u["foot_copy"]}</span><span class="foot-links"><a href="#top">{u["back_top"]}</a><a href="{href(lang, key, lang, "privacy")}">{u["foot_privacy"]}</a></span></div>
</div></footer>'''


def layout(lang, key, title, desc, body, extra_ld="", page_class=""):
    u = UI[lang]
    return f'''<!doctype html>
<html lang="{lang}">
<head>
{head_tags(lang, key, title, desc, extra_ld)}
</head>
<body class="{page_class}" id="top">
<a class="skip" href="#main">{u["skip"]}</a>
{header(lang, key)}
<main id="main">
{body}
</main>
{footer(lang, key)}
<button class="to-top" type="button" aria-label="{u["back_top"]}" hidden><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg></button>
<script src="{asset(lang, key, "js/main.js")}" defer></script>
</body>
</html>
'''


def phead(lang, key, h1, lead, crumb=True):
    u = UI[lang]
    cr = (f'<p class="crumbs"><a href="{href(lang, key, lang, "home")}">{"Home" if lang == "en" else "Inicio"}</a> / {u["nav"].get(key, h1)}</p>' if crumb else "")
    return f'<section class="phead on-dark"><div class="wrap">{cr}<h1>{esc(h1)}</h1><p>{esc(lead)}</p></div></section>'


# ------------------------------------------------------------------ components
def motorcycle_block(lang, key):
    u = UI[lang]
    names = {"sel": u["moto_sel"], "listed": u["moto_listed"], "parts": {pid: L(lab, lang) for pid, lab in MOTO_PARTS}}
    parts = [(pid, L(lab, lang)) for pid, lab in MOTO_PARTS]
    lis = "".join(f'<li><button type="button" data-part="{pid}" aria-pressed="false"><b>{i}</b>{esc(lab)}</button></li>' for i, (pid, lab) in enumerate(parts, start=1))
    return f'''<div class="moto" id="moto">
<div class="moto-stage">{G.moto(parts, esc(u["moto_aria"], quote=True))}</div>
<div><ol class="parts" aria-label="PennDOT">{lis}</ol>
<p class="moto-note" id="moto-note" aria-live="polite">{u["moto_init"]}</p></div>
<script type="application/json" id="moto-data">{json.dumps(names, ensure_ascii=False)}</script>
</div>'''


def review_html(lang, r, big=False, key="reviews"):
    u = UI[lang]
    who = L(r["who"], lang)
    date = L(r["date"], lang)
    orig = f'<span class="rev-orig">{PAGES["reviews"]["orig_es"]["es"]}</span>' if lang == "es" else ""
    ic = {"CARFAX": '<img class="src-ic src-cx" src="' + asset(lang, key, "img/carfax.png") + '" width="64" height="14" alt="CARFAX">',
          "Yelp": '<span class="src-ic src-yelp">Yelp</span>'}.get(r["src"], "")
    cite = (f'<div class="who"><b>{esc(who)}</b>{esc(date)}<br><span class="src-row">{ic}<a href="{r["url"]}" rel="noopener" target="_blank">{u["source"]}: {r["src"]}</a></span>{("<br>" + orig) if orig else ""}</div>')
    q = f'<blockquote lang="es">“{esc(RES.FEATURED[REVIEWS.index(r)])}”</blockquote>' if lang == "es" else f'<blockquote lang="en">“{esc(r["q"])}”</blockquote>'
    return q, cite


def form_html(lang, key, fleet=False):
    u = UI[lang]
    f = u["form"]
    opts = [f'<option value="">{f["svc_pick"]}</option>']
    for s in SERVICES:
        if s["id"] == "inspections":
            opts.append(f'<option value="inspections">{esc(L(s["title"], lang))}</option>')
            opts.append(f'<option value="motorcycle">{esc(L(MOTORCYCLE_SERVICE["title"], lang))}</option>')
        else:
            opts.append(f'<option value="{s["id"]}">{esc(L(s["title"], lang))}</option>')
    opts.append(f'<option value="unsure">{f["svc_unsure"]}</option>')
    opts.append(f'<option value="other">{f["svc_other"]}</option>')
    sel_default = "fleet" if fleet else ""
    options = "".join(opts).replace(f'<option value="{sel_default}">', f'<option value="{sel_default}" selected>') if sel_default else "".join(opts)
    submit = f["submit_post"] if FORM_ENDPOINT else f["submit_mail"]
    mail_note = "" if FORM_ENDPOINT else f'<small>{f["mail_note"]}</small>'
    fleet_attr = ' data-fleet="1"' if fleet else ""
    return f'''<form class="form" id="request" data-request data-endpoint="{esc(FORM_ENDPOINT, quote=True)}" data-email="{B["email"]}"{fleet_attr} novalidate>
<p class="form-note">{f["notice"]}</p>
<div class="hp" aria-hidden="true"><label>Website<input type="text" name="company_site" tabindex="-1" autocomplete="off"></label></div>
<div class="grid2">
<div class="fld"><label for="f-name">{f["name"]}</label><input id="f-name" name="name" type="text" autocomplete="name" required aria-describedby="e-name"><span class="err" id="e-name" data-err="name" role="alert"></span></div>
<div class="fld"><label for="f-phone">{f["phone"]}</label><input id="f-phone" name="phone" type="tel" autocomplete="tel" inputmode="tel" aria-describedby="e-phone"><span class="err" id="e-phone" data-err="phone" role="alert"></span></div>
</div>
<div class="grid2">
<div class="fld"><label for="f-email">{f["email"]}</label><input id="f-email" name="email" type="email" autocomplete="email" aria-describedby="e-email"><span class="err" id="e-email" data-err="email" role="alert"></span></div>
<fieldset class="fld" style="border:0;padding:0;margin:0"><legend>{f["contact"]}</legend><div class="radios">
<label><input type="radio" name="contact" value="phone" checked>{f["p_phone"]}</label><label><input type="radio" name="contact" value="email">{f["p_email"]}</label></div></fieldset>
</div>
<div class="grid2">
<div class="fld"><label for="f-vehicle">{f["vehicle"]}</label><input id="f-vehicle" name="vehicle" type="text" autocomplete="off"></div>
<div class="fld"><label for="f-service">{f["service"]}</label><select id="f-service" name="service">{options}</select></div>
</div>
<div class="fld"><label for="f-message">{f["msg"]}</label><textarea id="f-message" name="message" aria-describedby="h-msg"></textarea><small id="h-msg">{f["msg_help"]}</small></div>
<div class="grid2">
<div class="fld"><label for="f-date">{f["date"]} <span class="opt">({f["optional"]})</span></label><input id="f-date" name="date" type="date"></div>
<div class="fld"><label for="f-fleet">{f["fleet"]} <span class="opt">({f["optional"]})</span></label><input id="f-fleet" name="fleet" type="number" min="1" inputmode="numeric"></div>
</div>
<small>{f["safe"]} <a href="{href(lang, key, lang, "privacy")}">{f["privacy"]}</a></small>
<div><button class="btn btn-navy" type="submit">{submit}</button></div>
{mail_note}
<div class="form-status" role="status" aria-live="polite"></div>
</form>
<script type="application/json" id="form-i18n">{json.dumps(u["js"], ensure_ascii=False)}</script>'''


def faq_list(lang, cat, with_id=False):
    out = []
    for q, a in cat["items"]:
        out.append(f'<details class="q"><summary>{esc(L(q, lang))}</summary><div class="a"><p>{esc(L(a, lang))}</p></div></details>')
    return "".join(out)


def faq_cats_all():
    cats = list(FAQ_CATS) + list(ASK_FAQ_CATS)
    gen = dict(FAQ_GENERAL)
    items = list(gen["items"])
    if FORM_ENDPOINT:
        items.insert(1, gen["online"])
    cats.append({"id": "general", "title": gen["title"], "items": items})
    return cats


def faq_cat_by_id(cid):
    for c in list(FAQ_CATS) + list(ASK_FAQ_CATS):
        if c["id"] == cid:
            return c


# ------------------------------------------------------------------ pages
def page_home(lang):
    key = "home"
    P = PAGES["home"]
    u = UI[lang]
    # hero
    types = "".join(f"<span>{t_}</span>" for t_ in u["types"])
    gauge_svg = G.gauge(esc(u["gauge_top"]), esc(u["gauge_sub"]), "").replace(' role="img" aria-label=""', ' aria-hidden="true"')
    hero = f'''<section class="hero on-dark"><div class="wrap hero-in">
<div class="hero-copy">
<h1 class="rise d1">{esc(L(P["h1"], lang))}</h1>
<p class="lead rise d2">{esc(L(P["lead"], lang))}</p>
<div class="hero-cta rise d3"><a class="btn btn-sign" href="{TEL}">{G.icon("phone", 22)}{u["call"]}</a>
<a class="btn btn-line" href="{href(lang, key, lang, "contact", anchor="request")}">{u["request"]}</a>
<a class="dir" href="{DIRECTIONS}" rel="noopener" target="_blank">{u["directions"]}</a></div>
<p class="hero-types rise d4"><b>{u["hero_types_lead"]}</b>{types}</p>
</div>
<div class="gauge rise d2">{gauge_svg}<button class="gauge-btn" id="gauge-btn" type="button" aria-label="{esc(u["gauge_aria"], quote=True)}"></button><span class="gauge-hint" aria-hidden="true">{u["gauge_hint"]}</span></div>
</div></section>'''

    # picker
    pdata = {"tel": TEL, "ui": u["pick_ui"], "items": {}}
    chips = []
    for it in PICKER:
        sid = it["svc"]
        if sid == "motorcycle":
            svc = MOTORCYCLE_SERVICE
        else:
            svc = svc_by_id(sid)
        pdata["items"][sid] = {
            "title": esc(L(svc["title"], lang)), "desc": esc(L(svc["desc"], lang)),
            "note": esc(L(it["note"], lang)) if it.get("note") else "",
            "icon": G.icon(it["icon"], 56, "res-ic"),
            "request": request_href(lang, key, sid), "learn": learn_href(lang, key, sid),
        }
        chips.append(f'<button type="button" class="chip" data-svc="{sid}" aria-pressed="false">{G.icon(it["icon"], 26)}<span>{esc(L(it["chip"], lang))}</span></button>')
    picker = f'''<section class="sec sec-concrete" id="picker"><div class="wrap">
<div class="sec-head"><h2>{u["pick_h"]}</h2><p>{u["pick_p"]}</p></div>
<div class="picker"><div class="chips" role="group" aria-label="{u["pick_group"]}">{"".join(chips)}</div>
<div class="result" id="picker-result" aria-live="polite"><div class="result-empty"><strong>{u["pick_empty_h"]}</strong>{u["pick_empty_p"]}</div></div></div>
<script type="application/json" id="picker-data">{json.dumps(pdata, ensure_ascii=False)}</script>
</div></section>'''

    # board
    tiles = []
    for sid in HOME_CARDS:
        s = svc_by_id(sid)
        tiles.append(f'<a class="tile" href="{learn_href(lang, key, sid)}">{img(lang, key, SVC_IMG[sid], "tile-img")}<h3>{esc(L(s["card"], lang))}</h3><p>{esc(L(s["line"], lang))}</p></a>')
    board = f'''<section class="sec sec-white" id="services"><div class="wrap">
<div class="sec-head"><h2>{esc(L(P["svc_h"], lang))}</h2><p>{esc(L(P["svc_p"], lang))}</p></div>
<div class="board">{"".join(tiles)}</div>
<p class="board-foot"><a class="link-arrow" href="{href(lang, key, lang, "services")}">{u["all_services"]}</a></p>
{img(lang, key, "about-mechanic", "fig-img fig-wide fig-band")}
</div></section>'''

    # motorcycle
    moto = f'''<section class="sec sec-ink on-dark" id="motorcycle"><div class="wrap">
<div class="sec-head"><h2>{esc(L(P["moto_h"], lang))}</h2><p>{esc(L(P["moto_p"], lang))}</p>
<p class="moto-cta"><a class="btn btn-sign" href="{TEL}">{G.icon("phone", 22)}{esc(L(P["moto_btn"], lang))}</a></p></div>
{img(lang, key, "moto", "fig-img fig-wide")}
{motorcycle_block(lang, key)}
</div></section>'''

    # reviews (lead + three)
    rev = REVIEWS
    lq, lc = review_html(lang, rev[0], key=key)
    others = []
    for r in rev[1:4]:
        q, c = review_html(lang, r, key=key)
        others.append(f"<li>{q}{c}</li>")
    themes = "".join(f"<li>{esc(L(t_, lang))}</li>" for t_ in THEMES)
    reviews = f'''<section class="sec sec-paper" id="reviews"><div class="wrap">
<div class="rev-top"><div><div class="sec-head"><h2>{esc(L(P["rev_h"], lang))}</h2><p>{esc(L(P["rev_p"], lang))}</p></div>
<ul class="themes">{themes}</ul></div>{img(lang, key, "about-hands", "fig-img rev-img")}</div>
<div class="revs"><figure class="lead-quote">{lq}<figcaption>{lc}</figcaption></figure><ul class="qlist">{"".join(others)}</ul></div>
<div class="rev-more"><a class="btn btn-navy" href="{href(lang, key, lang, "reviews")}">{u["more_reviews"]}</a></div>
</div></section>'''

    # duo
    duo = f'''<section class="duo" aria-label="{u["nav"]["fleet"]} / {L(svc_by_id("notary")["title"], lang)}">
<div class="panel panel-fleet on-dark">{G.icon("van", 64)}<h2>{esc(L(svc_by_id("fleet")["title"], lang))}</h2><p>{esc(L(P["fleet_p"], lang))}</p>
<a class="btn btn-sign" href="{href(lang, key, lang, "fleet")}">{u["fleet_btn"]}</a></div>
<div class="panel panel-notary">{G.icon("seal", 64)}<h2>{esc(L(svc_by_id("notary")["title"], lang))}</h2><p>{esc(L(P["notary_p"], lang))}</p>
<img class="panel-photo" src="{asset(lang, key, "img/notary-signing.webp")}" width="1168" height="880" alt="{esc(L(NOTARY["photo_alt"], lang), quote=True)}" loading="lazy" decoding="async">
<a class="btn btn-navy" href="{href(lang, key, lang, "contact", anchor="notary")}">{u["notary_btn"]}</a></div></section>'''

    # close
    close = f'''<section class="sec sec-ink on-dark" id="visit"><div class="wrap close">
<div><h2>{esc(L(P["close_h"], lang))}</h2><p>{esc(L(P["close_p"], lang))}</p>
<a class="bigphone" href="{TEL}">{PHONE}</a>
<div class="hero-cta"><a class="btn btn-sign" href="{href(lang, key, lang, "contact", anchor="request")}">{u["request"]}</a>
<a class="btn btn-line" href="{DIRECTIONS}" rel="noopener" target="_blank">{u["directions"]}</a></div></div>
<ul class="facts">
<li>{G.icon("pin", 30)}<div><b>{u["close_addr"]}</b><span>{B["street"]}<br>{B["city"]}, {B["state"]} {B["zip"]}</span></div></li>
<li>{G.icon("gear", 30)}<div><b>{u["close_hours"]}</b><span>{u["hours_shop"]}</span></div></li>
<li>{G.icon("seal", 30)}<div><b>{u["close_notary"]}</b><span>{u["hours_notary"]}</span></div></li>
<li>{G.icon("mail", 30)}<div><b>{u["close_mail"]}</b><a href="{MAIL}">{B["email"]}</a></div></li>
</ul>
{img(lang, key, "home-storefront", "fig-img close-photo")}</div></section>'''
    return layout(lang, key, L(P["title"], lang), L(P["desc"], lang), hero + picker + board + moto + reviews + duo + close)


def page_services(lang):
    key = "services"
    P = PAGES["services"]
    u = UI[lang]
    idx, groups = [], []
    for gid, gtitle in GROUPS:
        svcs = [s for s in SERVICES if s["group"] == gid]
        idx.append(f'<li><a href="#g-{gid}">{esc(L(gtitle, lang))}</a></li>')
        blocks = []
        for s in svcs:
            acts = [f'<a class="btn btn-navy" style="min-height:44px;font-size:1.15rem" href="{request_href(lang, key, s["id"])}">{u["svc_request"]}</a>']
            if s.get("page"):
                acts.append(f'<a href="{learn_href(lang, key, s["id"])}">{u["svc_details"]}</a>')
            acts.append(f'<a href="{href(lang, key, lang, "faq", anchor=s["faq"])}">{u["faq_related"]}</a>')
            blocks.append(f'<article class="svc" id="{s["id"]}">{G.icon(s["icon"], 56)}<h3>{esc(L(s["title"], lang))}</h3><div>{img(lang, key, SVC_IMG[s["id"]], "svc-img") if s["id"] in SVC_IMG else ""}<p>{esc(L(s["desc"], lang))}</p><div class="svc-acts">{"".join(acts)}</div></div></article>')
        groups.append(f'<section class="svc-group" id="g-{gid}"><h2>{esc(L(gtitle, lang))}</h2>{"".join(blocks)}</section>')
    body = phead(lang, key, L(P["h1"], lang), L(P["lead"], lang)) + f'''<section class="sec sec-paper"><div class="wrap svc-layout">
<nav aria-label="{u["svc_index"]}"><ul class="svc-index">{"".join(idx)}</ul></nav><div>{"".join(groups)}</div></div></section>'''
    return layout(lang, key, L(P["title"], lang), L(P["desc"], lang), body)


def page_inspections(lang):
    key = "inspections"
    P = PAGES["inspections"]
    u = UI[lang]
    types = "".join(f"<li>{esc(L(t_, lang))}</li>" for t_ in P["types"])
    ins = faq_cat_by_id("inspections")
    mot = faq_cat_by_id("motorcycle")
    body = phead(lang, key, L(P["h1"], lang), L(P["lead"], lang)) + f'''
<section class="sec sec-paper"><div class="wrap">
<div class="sec-head"><h2>{esc(L(P["two_h"], lang))}</h2><p>{esc(L(P["two_p"], lang))}</p></div>
<div class="split"><div><h3>{esc(L(P["safety_h"], lang))}</h3><p>{esc(L(P["safety_p"], lang))}</p></div><div><h3>{esc(L(P["emis_h"], lang))}</h3><p>{esc(L(P["emis_p"], lang))}</p></div></div>
</div></section>
<section class="sec sec-white"><div class="wrap two-col">
<div><h2>{esc(L(P["types_h"], lang))}</h2>{img(lang, key, "svc-inspections", "fig-img")}<ul class="vtypes">{types}</ul>
<div class="callout"><h3>{esc(L(P["price_h"], lang))}</h3><p>{esc(L(P["price_p"], lang))}</p></div>
<p style="margin-top:22px"><a class="btn btn-sign" href="{TEL}">{G.icon("phone", 22)}{u["call"]}</a></p></div>
<div><h2>{esc(L(ins["title"], lang))}</h2>{faq_list(lang, ins)}</div></div></section>
<section class="sec sec-ink on-dark" id="motorcycle"><div class="wrap">
<div class="sec-head"><h2>{esc(L(P["moto_h"], lang))}</h2><p>{esc(L(P["moto_p"], lang))}</p></div>
{img(lang, key, "moto", "fig-img fig-wide")}
{motorcycle_block(lang, key)}
<p class="moto-note" style="max-width:68ch;margin-top:22px">{u["moto_caveat"]}</p>
<p class="moto-cta"><a class="btn btn-sign" href="{TEL}">{G.icon("phone", 22)}{esc(L(PAGES["home"]["moto_btn"], lang))}</a></p>
</div></section>
<section class="sec sec-paper"><div class="wrap two-col"><div><h2>{esc(L(mot["title"], lang))}</h2>{faq_list(lang, mot)}</div>
<div class="callout"><h3>{esc(L(PAGES["faq"]["h1"], lang))}</h3><p style="margin-bottom:14px">{esc(L(PAGES["faq"]["lead"], lang))}</p><a class="btn btn-navy" href="{href(lang, key, lang, "faq")}">{u["faq_more"]}</a></div></div></section>'''
    return layout(lang, key, L(P["title"], lang), L(P["desc"], lang), body)


def page_fleet(lang):
    key = "fleet"
    P = PAGES["fleet"]
    u = UI[lang]
    tell = "".join(f"<li>{esc(L(t_, lang))}</li>" for t_ in P["tell"])
    fc = faq_cat_by_id("fleet")
    body = phead(lang, key, L(P["h1"], lang), L(P["lead"], lang)) + f'''
<section class="sec sec-paper"><div class="wrap two-col">
<div>{img(lang, key, "svc-fleet", "fig-img")}<h2>{esc(L(P["tell_h"], lang))}</h2><ul class="checklist">{tell}</ul>
<div class="callout" style="margin-top:28px"><h3>{esc(L(P["terms_h"], lang))}</h3><p>{esc(L(P["terms_p"], lang))}</p></div>
<p style="margin-top:22px"><a class="btn btn-sign" href="{TEL}">{G.icon("phone", 22)}{u["call"]}</a></p></div>
<div><h2 style="margin-bottom:.5em">{esc(L(P["form_h"], lang))}</h2>{form_html(lang, key, fleet=True)}</div></div></section>
<section class="sec sec-white"><div class="wrap"><div class="sec-head"><h2>{esc(L(fc["title"], lang))}</h2></div><div style="max-width:820px">{faq_list(lang, fc)}</div></div></section>'''
    return layout(lang, key, L(P["title"], lang), L(P["desc"], lang), body)


def page_about(lang):
    key = "about"
    P = PAGES["about"]
    u = UI[lang]
    rng = "".join(f"<li>{esc(x)}</li>" for x in u["about_range"])
    themes = "".join(f"<li>{esc(L(t_, lang))}</li>" for t_ in THEMES)
    body = phead(lang, key, L(P["h1"], lang), L(P["p2"], lang)) + f'''
<section class="sec sec-paper"><div class="wrap two-col">
<div><p style="font-size:1.2rem">{esc(L(P["p1"], lang))}</p>
<p style="margin-top:26px"><a class="btn btn-sign" href="{TEL}">{G.icon("phone", 22)}{u["call"]}</a> <a class="btn btn-line" href="{href(lang, key, lang, "services")}" style="margin-left:6px">{u["all_services"]}</a></p><img class="logo-card" style="margin-top:28px" src="{asset(lang, key, "img/diverse-autoworks-logo.png")}" width="320" height="168" alt="Diverse Auto Works logo" loading="lazy"></div>
<div><h2>{esc(L(P["range_h"], lang))}</h2><ul class="checklist">{rng}</ul></div></div></section>
<section class="sec sec-ink on-dark"><div class="wrap"><ul class="gallery">{"".join(f'<li>{img(lang, key, n, "fig-img")}</li>' for n in ("about-storefront", "about-interior", "about-mechanic", "about-hands"))}</ul></div></section>
<section class="sec sec-white"><div class="wrap"><div class="sec-head"><h2>{esc(L(P["themes_h"], lang))}</h2><p>{esc(L(P["themes_p"], lang))}</p></div>
<ul class="themes">{themes}</ul><a class="btn btn-navy" href="{href(lang, key, lang, "reviews")}">{u["more_reviews"]}</a></div></section>'''
    return layout(lang, key, L(P["title"], lang), L(P["desc"], lang), body)


def ratings_html(lang):
    cards = []
    for r in RATINGS:
        avg = f'<div class="rt-avg">{r["avg"]}<span> / 5</span></div>' if r["avg"] else ""
        bars = ""
        if r["bars"]:
            bars = "<ul class=\"rt-bars\" aria-hidden=\"true\">" + "".join(
                f'<li><span>{n}</span><i><b style="width:{pc}%"></b></i></li>' for n, pc in r["bars"]) + "</ul>"
        link = (f'<a href="{r["url"]}" rel="noopener" target="_blank">{UI[lang]["source"]}: {r["name"]}</a>' if r["url"] else "")
        g_logo = ('<img class="g-logo" src="' + asset(lang, "reviews", "img/google-g.png") + '" width="36" height="36" alt="Google">') if r["name"] == "Google" else ""
        if r["name"] == "Google":
            avg = avg + '<div class="g-stars" role="img" aria-label="4.9 out of 5 stars">★★★★★</div>'
        if r["name"] == "CARFAX":
            g_logo = '<img class="rt-cx" src="' + asset(lang, "reviews", "img/carfax.png") + '" width="116" height="25" alt="">'
        elif r["name"] == "Yelp":
            g_logo = '<span class="src-ic src-yelp" aria-hidden="true">Yelp</span>'
        cards.append(f'<li class="rt-card"><h2>{g_logo}{r["name"]}</h2>{avg}<p>{esc(L(r["line"], lang))}</p>{bars}{link}</li>')
    asof = L({"en": "Ratings as shown on each site on", "es": "Calificaciones tal como se mostraban en cada sitio el"}, lang) if False else (
        "Ratings as shown on each site on " if lang == "en" else "Calificaciones tal como se mostraban en cada sitio el ")
    return f'<ul class="rt-grid">{"".join(cards)}</ul><p class="rt-note">{asof}{esc(L(RATINGS_ASOF, lang))}. ' + (
        "They change over time; the linked pages show current figures." if lang == "en" else "Cambian con el tiempo; las páginas enlazadas muestran las cifras actuales.") + "</p>"


def google_html(lang):
    import json as _j, os as _o
    data = _j.load(open(_o.path.join(_o.path.dirname(__file__), "google_reviews.json"), encoding="utf-8"))
    shown = [r for r in data if r["text"] and not r["hold"]]
    blank = sum(1 for r in data if not r["text"])
    assert len(shown) == len(RES.GOOGLE), "google_reviews.json changed: update reviews_es.GOOGLE"
    es = lang == "es"
    items = "".join(
        f'<li><blockquote lang="{lang}">“{esc(RES.GOOGLE[i] if es else r["text"])}”</blockquote><div class="who"><b>{esc(r["who"])}</b>{esc(RES.age_es(r["age"]) if es else r["age"])}<br><span class="src-row"><img class="src-ic src-g" src="{asset(lang, "reviews", "img/google-g.png")}" width="22" height="22" alt="Google">Google</span></div><div class="g-rate" role="img" aria-label="{r["stars"]} {"de 5 estrellas" if es else "of 5 stars"}"><span class="g-stars" style="--p:{r["stars"]*20}%">★★★★★</span></div></li>' for i, r in enumerate(shown))
    if lang == "en":
        h, p = "Reviews from Google", f"Written Google reviews, newest first, as captured on {L(RATINGS_ASOF, lang)}. {blank} more customers left a star rating with no text. Ages such as “2 months ago” are as of that date."
    else:
        h, p = "Reseñas de Google", f"Reseñas escritas de Google, de la más nueva a la más antigua, según se capturaron el {L(RATINGS_ASOF, lang)}. {blank} clientes más dejaron solo una calificación con estrellas. Las antigüedades como “hace 2 meses” corresponden a esa fecha. Las reseñas se tradujeron del inglés; los textos originales están en Google."
    return f'<div class="sec-head" style="margin-top:44px"><h2 class="g-h"><img class="g-logo" src="{asset(lang, "reviews", "img/google-g.png")}" width="44" height="44" alt="">{h}</h2><p>{esc(p)}</p></div><ul class="qlist g-list" style="max-width:860px">{items}</ul>'


_MON = {"en": "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(), "es": "ene feb mar abr may jun jul ago sep oct nov dic".split()}


def _jload(name):
    import json as _j, os as _o
    return _j.load(open(_o.path.join(_o.path.dirname(__file__), name), encoding="utf-8"))


def _car_who(w, lang="en"):
    parts = []
    for tok in w.split():
        if tok.upper() == "OWNER":
            parts.append("owner"); continue
        keep = any(c.isdigit() for c in tok) or "/" in tok or all(len(x) <= 3 for x in tok.split("-"))
        parts.append("Fe" if tok == "FE" else (tok if keep else tok.title()))
    if lang == "es" and parts and parts[-1] == "owner":
        return "Propietario del vehículo: " + " ".join(parts[:-1])
    return " ".join(parts)


def _car_date(lang, d):
    mm, dd, yy = d.split("/")
    m = _MON[lang][int(mm) - 1]
    return f"{m} {int(dd)}, {yy}" if lang == "en" else f"{int(dd)} {m} {yy}"


def _yelp_date(lang, d):
    m, rest = d.split(" ", 1)
    dd, yy = rest.replace(",", "").split()
    mi = _MON["en"].index(m)
    return d if lang == "en" else f"{int(dd)} {_MON['es'][mi]} {yy}"


def carfax_html(lang):
    data = _jload("carfax_reviews.json")
    ic = f'<img class="src-ic src-cx" src="{asset(lang, "reviews", "img/carfax.png")}" width="64" height="14" alt="CARFAX">'
    assert len(data) == len(RES.CARFAX), "carfax_reviews.json changed: update reviews_es.CARFAX"
    items = "".join(
        f'<li><blockquote lang="{lang}">“{esc(RES.CARFAX[i] if lang == "es" else r["text"])}”</blockquote><div class="who"><b>{esc(_car_who(r["who"], lang))}</b>{esc(_car_date(lang, r["date"]))}<br><span class="src-row">{ic}<span class="vs">{"Verified Service" if lang == "en" else "Servicio verificado"}</span></span></div></li>'
        for i, r in enumerate(data))
    if lang == "en":
        h, p = "All CARFAX reviews", f"All {len(data)} written CARFAX reviews as supplied, newest-first order as on the CARFAX page. CARFAX shows an overall 5.0 from 61 verified reviews; it did not give a star count for each review, so none is shown here."
    else:
        h, p = "Todas las reseñas de CARFAX", f"Las {len(data)} reseñas escritas de CARFAX, tal como se recibieron, en el orden de la página de CARFAX. CARFAX muestra 5.0 en total con 61 reseñas verificadas; no indicó las estrellas de cada reseña, así que aquí no se muestra ninguna. Las reseñas se tradujeron del inglés; los textos originales están en CARFAX."
    return f'<div class="sec-head" style="margin-top:44px"><h2>{h}</h2><p>{esc(p)}</p></div><ul class="qlist g-list" style="max-width:860px">{items}</ul>'


def yelp_html(lang):
    data = _jload("yelp_reviews.json")
    ic = '<span class="src-ic src-yelp">Yelp</span>'
    assert len(data) == len(RES.YELP), "yelp_reviews.json changed: update reviews_es.YELP"
    out = []
    for i, r in enumerate(data):
        rep = ""
        if r.get("reply"):
            q = r["reply"]
            lab = "Business owner reply" if lang == "en" else "Respuesta del propietario"
            rep = f'<div class="owner-reply"><b>{lab}: {esc(q["who"])}, {esc(_yelp_date(lang, q["date"]))}</b><p lang="{lang}">{esc(RES.YELP_REPLY[i] if lang == "es" else q["text"])}</p></div>'
        out.append(f'<li><blockquote lang="{lang}">“{esc(RES.YELP[i] if lang == "es" else r["text"])}”</blockquote><div class="who"><b>{esc(r["who"])}</b>{esc(r["loc"])} · {esc(_yelp_date(lang, r["date"]))}<br><span class="src-row">{ic}</span></div>{rep}</li>')
    if lang == "en":
        h, p = "All Yelp reviews", f"Yelp shows 10 reviews. The supplied copy has {len(data)} with text, shown here as supplied; Yelp did not give a reliable overall score or a star count per review, so none is shown."
    else:
        h, p = "Todas las reseñas de Yelp", f"Yelp muestra 10 reseñas. El texto recibido tiene {len(data)} con comentario, que se muestran tal cual; Yelp no dio una calificación general confiable ni las estrellas de cada reseña, así que no se muestra ninguna. Las reseñas se tradujeron del inglés; los textos originales están en Yelp."
    return f'<div class="sec-head" style="margin-top:44px"><h2>{h}</h2><p>{esc(p)}</p></div><ul class="qlist g-list" style="max-width:860px">{"".join(out)}</ul>'


def page_reviews(lang):
    key = "reviews"
    P = PAGES["reviews"]
    u = UI[lang]
    items = []
    for i, r in enumerate(REVIEWS):
        q, c = review_html(lang, r)
        items.append(f"<li>{q}{c}</li>")
    themes = "".join(f"<li>{esc(L(t_, lang))}</li>" for t_ in THEMES)
    body = phead(lang, key, L(P["h1"], lang), L(P["lead"], lang)) + f'''
<section class="sec sec-paper"><div class="wrap">
{ratings_html(lang)}
<ul class="themes">{themes}</ul>
<ul class="qlist" style="max-width:860px">{"".join(items)}</ul>
{google_html(lang)}
{carfax_html(lang)}
{yelp_html(lang)}
<div class="rev-more"><span>{u["full_reviews"]}</span><a class="btn btn-navy" href="{CARFAX_URL}" rel="noopener" target="_blank">CARFAX</a><a class="btn btn-navy" href="{YELP_URL}" rel="noopener" target="_blank">Yelp</a></div>
</div></section>'''
    return layout(lang, key, L(P["title"], lang), L(P["desc"], lang), body)


def page_faq(lang):
    key = "faq"
    P = PAGES["faq"]
    u = UI[lang]
    cats = faq_cats_all()
    chips = [f'<button type="button" data-cat="all" aria-pressed="true">{u["faq_all"]}</button>'] + [
        f'<button type="button" data-cat="{c["id"]}" aria-pressed="false">{esc(L(c["title"], lang))}</button>' for c in cats]
    sections = "".join(f'<section class="faq-cat" id="{c["id"]}" data-cat="{c["id"]}"><h2>{esc(L(c["title"], lang))}</h2>{faq_list(lang, c)}</section>' for c in cats)
    ld_items = []
    for c in cats:
        for q, a in c["items"]:
            ld_items.append({"@type": "Question", "name": L(q, lang), "acceptedAnswer": {"@type": "Answer", "text": L(a, lang)}})
    ld = '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": lang, "mainEntity": ld_items}, ensure_ascii=False) + "</script>"
    body = phead(lang, key, L(P["h1"], lang), L(P["lead"], lang)) + f'''
<section class="sec sec-paper"><div class="wrap" id="faq-root">
<div class="faq-tools"><div><label class="vh" for="faq-search">{u["faq_search"]}</label><input class="faq-search" id="faq-search" type="search" placeholder="{esc(u["faq_search_ph"], quote=True)}" autocomplete="off"></div>
<div class="faq-chips" role="group" aria-label="{u["faq_cats"]}">{"".join(chips)}</div>
<div class="faq-count" id="faq-count" data-tpl="{u["faq_count"]}" aria-live="polite"></div></div>
{sections}
<div class="faq-empty" id="faq-empty"><p><strong>{u["faq_none_h"]}</strong></p><p>{u["faq_none_p"]}</p></div>
</div></section>'''
    return layout(lang, key, L(P["title"], lang), L(P["desc"], lang), body, extra_ld=ld)


def notary_sections(lang):
    """Redesigned notary block on the Contact page (anchor #notary). Copy lives in tools/notary.py."""
    N = NOTARY
    u = UI[lang]

    def e(d):
        return esc(L(d, lang))

    call = f"Llame al {PHONE}" if lang == "es" else f"Call {PHONE}"
    chips = "".join(f"<li>{e(c)}</li>" for c in N["chips"])
    cards = "".join(f'<div class="nt-card">{G.icon(ic, 34)}<h4>{e(h)}</h4><p>{e(p)}</p></div>' for ic, h, p in N["cards"])
    steps = "".join(f'<li class="nt-step"><span class="nt-n" aria-hidden="true">{i:02d}</span><h4>{e(h)}</h4><p>{e(p)}</p></li>'
                    for i, (h, p) in enumerate(N["steps"], 1))
    rules = "".join(
        f'<div class="nt-rule"><dt>{e(dt)}<small>{e(sm)}</small></dt><dd>{"".join(f"<p>{e(x)}</p>" for x in ps)}</dd></div>'
        for dt, sm, ps in N["rules"])
    note = e(N["note"])
    for i, (url, label) in enumerate(N["note_links"], 1):
        note = note.replace(f"[[{i}]]", f'<a href="{url}" rel="noopener" target="_blank">{e(label)}</a>')
    bring = "".join(f"<li>{e(x)}</li>" for x in N["bring"])
    avoid = "".join(f"<li>{e(x)}</li>" for x in N["avoid"])
    faq = "".join(
        f'<details class="q"><summary>{e(q)}</summary><div class="a">{"".join(f"<p>{e(x)}</p>" for x in ans)}</div></details>'
        for q, ans in N["faq"])
    doc = f"""<svg class="nt-doc" viewBox="0 0 520 440" role="img" aria-label="{esc(L(N["doc_aria"], lang), quote=True)}">
<rect x="40" y="14" width="440" height="412" fill="#fff" stroke="#CDCED0"/><rect x="40" y="14" width="440" height="44" fill="#26282C"/>
<text x="62" y="42" font-size="12" letter-spacing="2" fill="#fff">{e(N["doc_top"])}</text>
<g fill="#E6E6E7"><rect x="62" y="80" width="190" height="8"/><rect x="62" y="100" width="260" height="8"/><rect x="62" y="120" width="150" height="8"/><rect x="330" y="80" width="130" height="8"/><rect x="330" y="100" width="100" height="8"/></g>
<text x="62" y="170" font-size="11" letter-spacing="2" fill="#5B5F66">{e(N["doc_assign"])}</text>
<rect x="62" y="182" width="396" height="86" fill="#FDECEA" stroke="#B3201B" stroke-width="1.5"/>
<text x="76" y="204" font-size="11" letter-spacing="1.2" fill="#B3201B">{e(N["doc_seller"])}</text>
<path d="M78 246 q16 -26 30 -4 t28 -2 t26 2 t26 -4" fill="none" stroke="#26282C" stroke-width="1.6" stroke-linecap="round" stroke-dasharray="3 4" opacity=".55"/>
<line x1="76" y1="254" x2="440" y2="254" stroke="#B3201B" stroke-width="1"/>
<rect x="62" y="284" width="190" height="52" fill="#fff" stroke="#CDCED0"/><text x="74" y="304" font-size="10.5" letter-spacing="1.2" fill="#5B5F66">{e(N["doc_odo"])}</text>
<rect x="268" y="284" width="190" height="52" fill="#fff" stroke="#CDCED0"/><text x="280" y="304" font-size="10.5" letter-spacing="1.2" fill="#5B5F66">{e(N["doc_buyer"])}</text>
<g fill="#E6E6E7"><rect x="62" y="356" width="396" height="8"/><rect x="62" y="376" width="300" height="8"/></g>
<circle cx="430" cy="390" r="30" fill="none" stroke="#26282C" stroke-width="1.5" opacity=".6"/><circle cx="430" cy="390" r="23" fill="none" stroke="#26282C" stroke-width="1" stroke-dasharray="1 3" opacity=".6"/>
<text x="430" y="394" text-anchor="middle" font-size="8.5" letter-spacing="1" fill="#26282C" opacity=".75">{e(N["doc_notary"])}</text></svg>"""
    return f"""<section class="sec sec-white nt" id="notary" aria-labelledby="nt-h"><div class="wrap">
<div class="nt-intro"><div class="nt-intro-txt"><p class="nt-eyebrow">{e(N["eyebrow"])}</p><h2 id="nt-h">{e(N["h2"])}</h2><p class="nt-lede">{e(N["lede"])}</p>
<div class="nt-cta"><a class="btn btn-navy" href="{TEL}">{call}</a><a class="btn btn-line" href="#notary-process">{e(N["cta_how"])}</a><a class="btn btn-line" href="{MAIL}">{u["email_us"]}</a></div>
<ul class="nt-chips">{chips}</ul></div>
<figure class="nt-photo"><img src="{asset(lang, "contact", "img/notary-signing.webp")}" width="1168" height="880" alt="{esc(L(N["photo_alt"], lang), quote=True)}" loading="lazy" decoding="async"></figure></div>
<h3 class="nt-sh"><span class="nt-sec">§ 01</span>{e(N["s1_h"])}</h3><p class="nt-sp">{e(N["s1_p"])}</p>
<div class="nt-cards">{cards}</div></div></section>
<section class="sec sec-paper nt" id="notary-process" aria-labelledby="nt-h2"><div class="wrap">
<h3 class="nt-sh" id="nt-h2"><span class="nt-sec">§ 02</span>{e(N["s2_h"])}</h3><p class="nt-sp">{e(N["s2_p"])}</p>
<ol class="nt-steps">{steps}</ol></div></section>
<section class="sec sec-white nt" id="notary-rules" aria-labelledby="nt-h3"><div class="wrap">
<h3 class="nt-sh" id="nt-h3"><span class="nt-sec">§ 03</span>{e(N["s3_h"])}</h3><p class="nt-sp">{e(N["s3_p"])}</p>
<dl class="nt-rules">{rules}</dl><p class="nt-note">{note}</p></div></section>
<section class="sec sec-paper nt" aria-labelledby="nt-h4"><div class="wrap two-col nt-split">
<div>{doc}</div>
<div><p class="nt-eyebrow">{e(N["s4_eyebrow"])}</p><h3 class="nt-sh" id="nt-h4">{e(N["s4_h"])}</h3><p class="nt-sp">{e(N["s4_p"])}</p>
<h4 class="nt-sub">{e(N["bring_h"])}</h4><ul class="nt-list">{bring}</ul>
<h4 class="nt-sub">{e(N["avoid_h"])}</h4><ul class="nt-list nt-no">{avoid}</ul></div></div></section>
<section class="sec sec-white nt" aria-labelledby="nt-h5"><div class="wrap">
<div class="nt-faq"><h3 class="nt-sh" id="nt-h5"><span class="nt-sec">§ 04</span>{e(N["faq_h"])}</h3>{faq}</div>
<div class="nt-shop"><div><p class="nt-eyebrow">{e(N["shop_eyebrow"])}</p><h3>{e(N["shop_h"])}</h3><p>{e(N["shop_p"])}</p></div>
<div class="nt-cta"><a class="btn btn-navy" href="{href(lang, "contact", lang, "inspections")}">{u["nav"]["inspections"]}</a><a class="btn btn-line" href="{href(lang, "contact", lang, "services")}">{u["nav"]["services"]}</a></div></div></div></section>"""


def notary_ld(lang):
    items = [{"@type": "Question", "name": L(q, lang),
              "acceptedAnswer": {"@type": "Answer", "text": " ".join(L(x, lang) for x in ans)}} for q, ans in NOTARY["faq"]]
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "inLanguage": lang, "mainEntity": items}, ensure_ascii=False) + "</script>"


def page_contact(lang):
    key = "contact"
    P = PAGES["contact"]
    u = UI[lang]
    cards = f'''<div class="cards">
<div class="cardrow">{G.icon("phone", 34)}<div><b>{u["contact_phone"]}</b><a href="{TEL}">{PHONE}</a></div></div>
<div class="cardrow">{G.icon("pin", 34)}<div><b>{u["contact_addr"]}</b><p>{B["street"]}<br>{B["city"]}, {B["state"]} {B["zip"]}</p><a href="{DIRECTIONS}" rel="noopener" target="_blank">{u["directions"]}</a></div></div>
<div class="cardrow">{G.icon("mail", 34)}<div><b>{u["contact_email"]}</b><a href="{MAIL}">{B["email"]}</a></div></div>
<div class="cardrow">{G.icon("gear", 34)}<div><b>{u["contact_hours"]}</b><p>{u["contact_hours_p"]}</p></div></div></div>'''
    mapbox = f'''<div class="mapbox" id="mapbox"><div class="map-face">{G.icon("pin", 54)}<div class="t">{u["map_t"]}</div><small>{u["map_small"]}</small>
<div class="row"><button class="btn btn-navy" type="button" id="map-load" data-src="{MAP_EMBED}" data-title="{esc(u["map_title"], quote=True)}">{u["map_load"]}</button>
<a class="btn btn-line" href="{DIRECTIONS}" rel="noopener" target="_blank">{u["map_open"]}</a></div></div></div>'''
    body = phead(lang, key, L(P["h1"], lang), L(P["lead"], lang)) + f'''
<section class="sec sec-paper"><div class="wrap contact-grid"><div>{cards}</div>
<div><h2 style="margin-bottom:.5em">{esc(L(P["form_h"], lang))}</h2>{form_html(lang, key)}</div></div></section>
{notary_sections(lang)}
<section class="sec sec-concrete"><div class="wrap">{mapbox}</div></section>'''
    return layout(lang, key, L(P["title"], lang), L(P["desc"], lang), body, extra_ld=notary_ld(lang))


def page_privacy(lang):
    key = "privacy"
    P = PAGES["privacy"]
    u = UI[lang]
    if lang == "en":
        form_txt = (f"When you use a request form, the details you enter are sent to the shop's inbox through {FORM_PROVIDER}, a form-handling service."
                    if FORM_ENDPOINT else
                    "When you use a request form, your browser opens your email app with the details you entered. Nothing is sent until you press Send in your email app.")
        sections = [
            ("What this website does", "<p>This website does not use analytics, advertising trackers, or cookies. Its fonts and scripts are hosted on this site.</p>"),
            ("Request forms", f"<p>{form_txt}</p><p>Please do not include payment card details or the contents of personal documents. We use what you send only to respond to your request.</p>"),
            ("Maps and links", f"<p>The map on the Contact page loads from Google only after you choose to load it. Review links lead to CARFAX and Yelp, which have their own privacy practices.</p>"),
            ("Questions", f'<p>Call <a href="{TEL}">{PHONE}</a> or email <a href="{MAIL}">{B["email"]}</a>.</p>'),
        ]
    else:
        form_txt = (f"Cuando usa un formulario de solicitud, los datos que escribe se envían a la bandeja de entrada del taller mediante {FORM_PROVIDER}, un servicio de manejo de formularios."
                    if FORM_ENDPOINT else
                    "Cuando usa un formulario de solicitud, su navegador abre su aplicación de correo con los datos que escribió. No se envía nada hasta que usted presione Enviar en su aplicación de correo.")
        sections = [
            ("Qué hace este sitio web", "<p>Este sitio web no usa analítica, rastreadores publicitarios ni cookies. Sus fuentes y scripts se alojan en este mismo sitio.</p>"),
            ("Formularios de solicitud", f"<p>{form_txt}</p><p>Por favor, no incluya datos de tarjetas de pago ni el contenido de documentos personales. Usamos lo que usted envía solo para responder a su solicitud.</p>"),
            ("Mapas y enlaces", "<p>El mapa de la página de Contacto se carga desde Google solo cuando usted decide cargarlo. Los enlaces de reseñas llevan a CARFAX y Yelp, que tienen sus propias prácticas de privacidad.</p>"),
            ("Preguntas", f'<p>Llame al <a href="{TEL}">{PHONE}</a> o escriba a <a href="{MAIL}">{B["email"]}</a>.</p>'),
        ]
    prose = "".join(f"<h2>{h}</h2>{b}" for h, b in sections)
    body = phead(lang, key, L(P["h1"], lang), L(P["desc"], lang), crumb=False) + f'<section class="sec sec-paper"><div class="wrap"><div class="prose">{prose}</div></div></section>'
    return layout(lang, key, L(P["title"], lang), L(P["desc"], lang), body)


BUILDERS = {"home": page_home, "services": page_services, "inspections": page_inspections, "fleet": page_fleet,
            "about": page_about, "reviews": page_reviews, "faq": page_faq, "contact": page_contact, "privacy": page_privacy}


def linkify(html_text):
    """Make every plain-text phone number and street address a link (tel: / Google Maps)."""
    import re as _re
    skip = {"a", "script", "style", "svg", "button", "title", "textarea", "option", "select", "head", "noscript"}
    ph = B["phone_display"]
    tel = f'<a href="{TEL}">{ph}</a>'
    addr_pat = _re.compile(r"1415 Pawlings Road(?:,? ?(?:<br\s*/?>\s*)?Phoenixville,? PA 19460)?|Phoenixville, PA 19460")
    def fix(txt):
        txt = txt.replace(ph, "\x00")
        txt = addr_pat.sub(lambda m: f'<a href="{DIRECTIONS}" rel="noopener" target="_blank">{m.group(0)}</a>', txt)
        return txt.replace("\x00", tel)
    out, depth, i = [], {}, 0
    for tok in _re.split(r"(<!--.*?-->|<[^>]+>)", html_text, flags=_re.S):
        if tok.startswith("<") and not tok.startswith("<!--"):
            m = _re.match(r"<(/?)([a-zA-Z0-9]+)", tok)
            if m:
                name = m.group(2).lower()
                if name in skip:
                    if m.group(1): depth[name] = max(0, depth.get(name, 0) - 1)
                    elif not tok.rstrip().endswith("/>"): depth[name] = depth.get(name, 0) + 1
            out.append(tok)
        elif tok.startswith("<!--") or any(depth.values()):
            out.append(tok)
        else:
            out.append(fix(tok))
    return "".join(out)


def write(rel, text):
    if rel.endswith(".html"):
        text = linkify(text)
    full = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(text)


def build():
    check_parity()
    count = 0
    for lang in LANGS:
        for key, fn in BUILDERS.items():
            p = path_of(lang, key)
            write((p + "/" if p else "") + "index.html", fn(lang))
            count += 1
    # 404 (self-contained: no external assets, so it works at any depth)
    nf = NOT_FOUND
    write("404.html", f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Page not found | Diverse Autoworks</title>
<style>body{{margin:0;font-family:system-ui,Arial,sans-serif;background:#0F1012;color:#fff;display:grid;min-height:100vh;place-items:center;padding:24px;text-align:center}}
h1{{font-size:clamp(2.2rem,6vw,3.6rem);margin:0 0 .3em}}p{{color:#DADCDF;max-width:46ch;margin:0 auto 1em;line-height:1.5}}a{{color:#E4372F;font-weight:700}}</style></head>
<body><main><h1>{nf["h"]["en"]} / {nf["h"]["es"]}</h1><p>{nf["p"]["en"]}</p><p>{nf["p"]["es"]}</p>
<p><a href="tel:{B["phone_tel"]}">{PHONE}</a></p></main></body></html>''')
    write("assets/img/favicon.svg", '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44 44"><circle cx="22" cy="22" r="21" fill="#26282C"/><circle cx="22" cy="22" r="20" fill="none" stroke="#E4372F" stroke-width="2"/><path d="M8.5 29A15 15 0 0 1 35.5 29" fill="none" stroke="#D5D7DA" stroke-width="2.6" stroke-linecap="round" stroke-dasharray="1 4.3"/><path d="M22 25L30 12" stroke="#E4372F" stroke-width="3" stroke-linecap="round"/><circle cx="22" cy="25" r="3.6" fill="#E4372F"/></svg>')
    write(".nojekyll", "")
    write("robots.txt", "User-agent: *\nAllow: /\n" + (f"Sitemap: {SITE_URL}/sitemap.xml\n" if SITE_URL else ""))
    if SITE_URL:
        urls = []
        for key in SLUGS:
            en, es = abs_url("en", key), abs_url("es", key)
            for loc in (en, es):
                urls.append(f'<url><loc>{loc}</loc><xhtml:link rel="alternate" hreflang="en" href="{en}"/><xhtml:link rel="alternate" hreflang="es" href="{es}"/>'
                            f'<xhtml:link rel="alternate" hreflang="x-default" href="{en}"/></url>')
        write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n' + "\n".join(urls) + "\n</urlset>\n")
    elif os.path.exists(os.path.join(ROOT, "sitemap.xml")):
        os.remove(os.path.join(ROOT, "sitemap.xml"))
    print(f"built {count} pages + 404 | SITE_URL={SITE_URL or '(unset: canonical/hreflang/sitemap skipped)'} | form={'endpoint' if FORM_ENDPOINT else 'mailto fallback'}")


if __name__ == "__main__":
    build()
