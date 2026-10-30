# -*- coding: utf-8 -*-
"""
Public copy for the Diverse Autoworks site, English + Spanish.
Source: MASTER - Diverse_Autoworks_Website, Part I (public drafts) only.
Nothing from Part II (internal notes, review archive, competitor research) is used here.

Every text is a dict {"en": ..., "es": ...}. build.py fails if either side is missing.
"""


def t(en, es):
    return {"en": en, "es": es}


# ---------------------------------------------------------------- business
BUSINESS = {
    "name": "Diverse Autoworks, Inc.",
    "short": "Diverse Autoworks",
    "street": "1415 Pawlings Road",
    "city": "Phoenixville",
    "state": "PA",
    "zip": "19460",
    "phone_display": "610-650-0316",
    "phone_tel": "+16106500316",
    "email": "Diverseautoworks@verizon.net",
    "maps_query": "1415 Pawlings Road, Phoenixville, PA 19460",
}

# ---------------------------------------------------------------- services
# id, icon, title, home-card title, card line, description
SERVICES = [
    {
        "id": "inspections", "icon": "inspection",
        "title": t("State inspections & emissions testing", "Inspecciones estatales y pruebas de emisiones"),
        "card": t("State Inspections & Emissions", "Inspecciones estatales y emisiones"),
        "line": t("State inspections and emissions testing for cars, trucks, trailers, and motorcycles.",
                  "Inspecciones estatales y pruebas de emisiones para autos, camiones, remolques y motocicletas."),
        "desc": t("We offer state inspection and emissions services. Our inspection services include cars, trucks, trailers, and motorcycles. Call and we'll tell you which inspection your vehicle needs and set up a visit.",
                  "Ofrecemos inspección estatal y servicios de emisiones. Nuestros servicios de inspección incluyen autos, camiones, remolques y motocicletas. Llame y le diremos qué inspección necesita su vehículo y coordinaremos su visita."),
        "faq": "inspections", "page": "inspections", "group": "inspect",
    },
    {
        "id": "maintenance", "icon": "oil",
        "title": t("Oil changes & routine maintenance", "Cambios de aceite y mantenimiento de rutina"),
        "card": t("Oil Changes & Maintenance", "Aceite y mantenimiento"),
        "line": t("Oil changes, cabin and fuel filters, fan and accessory belts, wiper blades.",
                  "Cambios de aceite, filtros de cabina y de combustible, bandas del ventilador y de accesorios, plumillas."),
        "desc": t("Stay on top of vehicle maintenance with oil changes, cabin air filters, fuel filters, fan and accessory belts, and wiper blade replacement. Fuel filters are listed here. Fuel pumps, fuel lines, and fuel injectors are part of our engine repair work (see Engine analysis, repair & tune-ups), and gas tank service is listed under More services. Contact us to discuss the maintenance appropriate for your vehicle.",
                  "Mantenga al día el mantenimiento de su vehículo con cambios de aceite, filtros de aire de cabina, filtros de combustible, bandas del ventilador y de accesorios, y reemplazo de plumillas limpiaparabrisas. Los filtros de combustible figuran aquí. Las bombas, las líneas y los inyectores de combustible forman parte de nuestro trabajo de reparación del motor (vea Análisis, reparación y afinación del motor), y el servicio de tanque de combustible figura en Más servicios. Comuníquese con nosotros para hablar del mantenimiento adecuado para su vehículo."),
        "faq": "maintenance", "group": "maint",
    },
    {
        "id": "engine", "icon": "engine",
        "title": t("Engine analysis, repair & tune-ups", "Análisis, reparación y afinación del motor"),
        "card": t("Diagnostics & Engine Maintenance", "Diagnóstico y mantenimiento del motor"),
        "line": t("Engine analysis, tune-ups, fuel-injector cleaning, and engine repair.",
                  "Análisis del motor, afinaciones, limpieza de inyectores y reparación del motor."),
        "desc": t("We diagnose and repair engine problems, and we offer engine analysis, tune-ups, and fuel-injector cleaning. Our engine work covers ignition and fuel systems, sensors and electronics, cooling, oil leaks and lubrication, timing and valvetrain, belts and accessories, internal engine repair, and engine rebuild or replacement. Call 610-650-0316 with your vehicle's year, make, model, and symptoms.",
                  "Diagnosticamos y reparamos problemas del motor, y ofrecemos análisis del motor, afinaciones y limpieza de inyectores. Nuestro trabajo en el motor incluye los sistemas de encendido y combustible, sensores y electrónica, enfriamiento, fugas de aceite y lubricación, distribución y tren de válvulas, correas y accesorios, reparación interna del motor, y reconstrucción o reemplazo del motor. Llame al 610-650-0316 con el año, la marca, el modelo y los síntomas de su vehículo."),
        "faq": "engine", "group": "maint",
    },
    {
        "id": "brakes", "icon": "brakes",
        "title": t("Brakes & rotors", "Frenos y rotores"),
        "card": t("Brakes & Rotors", "Frenos y rotores"),
        "line": t("Brake and rotor service.", "Servicio de frenos y rotores."),
        "desc": t("We provide brake and rotor services. If you have concerns about braking performance or notice unusual noises, contact the shop to discuss an inspection and repair options.",
                  "Ofrecemos servicio de frenos y rotores. Si le preocupa el desempeño de los frenos o nota ruidos inusuales, comuníquese con el taller para hablar de una inspección y de las opciones de reparación."),
        "faq": "brakes", "group": "ride",
    },
    {
        "id": "tires", "icon": "tire",
        "title": t("Tires & wheel alignments", "Llantas y alineación de ruedas"),
        "card": t("Tires & Alignments", "Llantas y alineación"),
        "line": t("Tires, tire repairs, and wheel alignments.", "Llantas, reparación de llantas y alineación."),
        "desc": t("We offer tires, tire repairs, and wheel alignments. We also handle wheel (rim) repair and replacement, tire retreads, and tire rotation and balancing; see More services. Contact us for help with tire concerns or to discuss alignment service.",
                  "Ofrecemos llantas, reparación de llantas y alineación de ruedas. También hacemos reparación y reemplazo de ruedas (rines), llantas renovadas y rotación y balanceo de llantas; vea Más servicios. Comuníquese con nosotros para recibir ayuda con problemas de llantas o para hablar del servicio de alineación."),
        "faq": "tires", "group": "ride",
    },
    {
        "id": "suspension", "icon": "spring",
        "title": t("Steering & suspension", "Dirección y suspensión"),
        "card": t("Steering & Suspension", "Dirección y suspensión"),
        "line": t("Steering parts, suspension parts, shocks, and struts.",
                  "Piezas de dirección y suspensión, amortiguadores y puntales."),
        "desc": t("Our service range includes steering and suspension components, shock absorbers, and struts. We also service ball joints; see Ball joints under More services. Contact us if you have concerns about your vehicle's handling or ride.",
                  "Nuestra gama de servicios incluye componentes de dirección y suspensión, amortiguadores y puntales. También damos servicio a las rótulas; vea Rótulas en Más servicios. Comuníquese con nosotros si le preocupa el manejo o la comodidad de marcha de su vehículo."),
        "faq": "suspension", "group": "ride",
    },
    {
        "id": "ac", "icon": "snow",
        "title": t("Air conditioning & cooling systems", "Aire acondicionado y sistemas de enfriamiento"),
        "card": t("A/C & Cooling", "A/C y enfriamiento"),
        "line": t("Automotive A/C, coolant systems, and cooling-system service.", "Servicio de A/C automotriz, sistemas de refrigerante y del sistema de enfriamiento."),
        "desc": t("We offer automotive A/C service, coolant systems, and cooling-system service. We also service and repair heaters; see Heater service & repair under More services. Call to discuss cabin cooling problems or concerns about your vehicle's cooling system.",
                  "Ofrecemos servicio de aire acondicionado automotriz, sistemas de refrigerante y servicio del sistema de enfriamiento. También damos servicio y reparamos la calefacción; vea Servicio y reparación de la calefacción en Más servicios. Llame para hablar de problemas de enfriamiento en la cabina o de inquietudes sobre el sistema de enfriamiento de su vehículo."),
        "faq": "ac", "group": "climate",
    },
    {
        "id": "battery", "icon": "battery",
        "title": t("Batteries", "Baterías"),
        "card": t("Batteries", "Baterías"),
        "line": t("Battery testing, replacement, and starting and charging system diagnosis.", "Pruebas y reemplazo de baterías, y diagnóstico del sistema de arranque y carga."),
        "desc": t("We test and replace batteries, and we diagnose starting and charging system problems. Call to discuss your vehicle's battery needs.",
                  "Probamos y reemplazamos baterías, y diagnosticamos problemas del sistema de arranque y carga. Llame para hablar de las necesidades de batería de su vehículo."),
        "faq": "battery", "group": "maint",
    },
    {
        "id": "drivetrain", "icon": "gear",
        "title": t("Drivetrain maintenance", "Mantenimiento del tren motriz"),
        "card": t("Drivetrain Maintenance", "Tren motriz"),
        "line": t("Transmission maintenance and rear-axle bearing and seal service.",
                  "Mantenimiento de transmisión y servicio de cojinetes y sellos del eje trasero."),
        "desc": t("We offer transmission maintenance and service for rear-axle bearings and seals. We also repair differentials; see Differential repair under More services. Contact us to discuss the work appropriate for your vehicle.",
                  "Ofrecemos mantenimiento de transmisión y servicio de cojinetes y sellos del eje trasero. También reparamos diferenciales; vea Reparación del diferencial en Más servicios. Comuníquese con nosotros para hablar del trabajo adecuado para su vehículo."),
        "faq": "drivetrain", "group": "maint",
    },
    {
        "id": "fleet", "icon": "van",
        "title": t("Fleet repairs", "Reparaciones para flotas"),
        "card": t("Fleet Repairs", "Reparaciones para flotas"),
        "line": t("Repairs for business vehicles.", "Reparaciones para vehículos de negocios."),
        "desc": t("Keep your business vehicles on your maintenance radar. Diverse Autoworks offers fleet repairs; call to discuss your vehicles, repair needs, and scheduling.",
                  "Mantenga los vehículos de su negocio en su radar de mantenimiento. Diverse Autoworks ofrece reparaciones para flotas; llame para hablar de sus vehículos, sus necesidades de reparación y la programación."),
        "faq": "fleet", "page": "fleet-repairs", "group": "biz",
    },
    {
        "id": "notary", "icon": "seal",
        "title": t("Notary services", "Servicios de notario público"),
        "card": t("Notary Services", "Notario público"),
        "line": t("Notary services, Monday through Friday.", "Servicios de notario público, de lunes a viernes."),
        "desc": t("Diverse Autoworks also offers notary services Monday through Friday, 8 a.m.–3 p.m. Contact the shop before your visit to confirm availability and requirements.",
                  "Diverse Autoworks también ofrece servicios de notario público de lunes a viernes, de 8 a. m. a 3 p. m. Comuníquese con el taller antes de su visita para confirmar la disponibilidad y los requisitos."),
        "faq": "notary", "page": "contact", "anchor": "notary", "group": "biz",
    },
]

# the 8 cards the brief lists for the home page
HOME_CARDS = ["inspections", "maintenance", "battery", "drivetrain", "brakes", "tires", "suspension", "ac", "fleet"]

GROUPS = [
    ("inspect", t("Inspections & testing", "Inspecciones y pruebas")),
    ("maint", t("Maintenance & engine", "Mantenimiento y motor")),
    ("exhaust", t("Exhaust & emissions", "Escape y emisiones")),
    ("ride", t("Brakes, tires & ride", "Frenos, llantas y manejo")),
    ("climate", t("Climate & cooling", "Clima y enfriamiento")),
    ("biz", t("Business & paperwork", "Negocios y trámites")),
]

# service picker: what is the vehicle doing -> service id
PICKER = [
    {"chip": t("Inspection is due", "Me toca la inspección"), "svc": "inspections", "icon": "inspection"},
    {"chip": t("Oil change or upkeep", "Cambio de aceite o mantenimiento"), "svc": "maintenance", "icon": "oil"},
    {"chip": t("Brakes feel or sound off", "Los frenos suenan o se sienten raros"), "svc": "brakes", "icon": "brakes"},
    {"chip": t("Pulling to one side or uneven tire wear", "Se va hacia un lado o las llantas se desgastan parejo"), "svc": "tires", "icon": "tire",
     "note": t("Other tire or suspension issues can cause similar symptoms, so the cause needs to be assessed rather than assumed.",
               "Otros problemas de llantas o suspensión pueden causar síntomas parecidos, por lo que hay que evaluar la causa en lugar de suponerla.")},
    {"chip": t("Rough ride or loose handling", "Marcha brusca o manejo flojo"), "svc": "suspension", "icon": "spring"},
    {"chip": t("A/C isn't cooling", "El A/C no enfría"), "svc": "ac", "icon": "snow"},
    {"chip": t("Engine isn't running right", "El motor no funciona bien"), "svc": "engine", "icon": "engine"},
    {"chip": t("Won't start", "No arranca"), "svc": "battery", "icon": "battery",
     "note": t("We diagnose no-start problems. Call and describe what happens when you try to start it.",
               "Diagnosticamos fallas de arranque. Llame y describa qué pasa cuando intenta arrancarlo.")},
    {"chip": t("Motorcycle inspection", "Inspección de motocicleta"), "svc": "motorcycle", "icon": "moto"},
    {"chip": t("Business vehicles", "Vehículos de negocio"), "svc": "fleet", "icon": "van"},
    {"chip": t("Notary", "Notario público"), "svc": "notary", "icon": "seal"},
]

MOTORCYCLE_SERVICE = {
    "id": "motorcycle",
    "title": t("Motorcycle state inspections", "Inspecciones estatales de motocicletas"),
    "desc": t("Diverse Autoworks offers state inspections for motorcycles, along with cars, trucks, and trailers. Call to arrange an inspection and confirm availability.",
              "Diverse Autoworks ofrece inspecciones estatales para motocicletas, además de autos, camiones y remolques. Llame para coordinar una inspección y confirmar la disponibilidad."),
    "page": "inspections", "anchor": "motorcycle",
}

# PennDOT-listed motorcycle inspection items (from the brief's FAQ answer)
MOTO_PARTS = [
    ("brakes", t("Brakes", "Frenos")),
    ("steering", t("Steering", "Dirección")),
    ("suspension", t("Suspension", "Suspensión")),
    ("tires", t("Tires and wheels", "Llantas y ruedas")),
    ("lights", t("Lights and electrical systems", "Luces y sistema eléctrico")),
    ("mirrors", t("Mirrors", "Espejos")),
    ("fuel", t("Fuel and exhaust systems", "Sistemas de combustible y escape")),
    ("horn", t("Horn", "Bocina")),
    ("body", t("Body and chassis", "Carrocería y chasis")),
]

# ---------------------------------------------------------------- reviews
# Exact excerpts from the owner brief's candidate list. Attribution as supplied.
YELP_URL = "https://www.yelp.com/biz/diverse-autoworks-phoenixville-2"
CARFAX_URL = "https://www.carfax.com/Reviews-Diverse-Auto-Works-Phoenixville-PA_IDY2JBSOYI"

REVIEWS = [
    {"src": "CARFAX", "url": CARFAX_URL, "lead": True,
     "who": t("Joseph N.", "Joseph N."), "date": t("August 20, 2026", "20 de agosto de 2026"),
     "q": "They also give honest assessments of vehicle status and make reasonable recommendations for repairs and/or replacements."},
    {"src": "Yelp", "url": YELP_URL,
     "who": t("Judith S.", "Judith S."), "date": t("August 31, 2026", "31 de agosto de 2026"),
     "q": "Great experience with motorcycle inspection. Great availability for appointment. Fast service!"},
    {"src": "CARFAX", "url": CARFAX_URL,
     "who": t("2023 Mazda CX-9 owner", "Propietario de un Mazda CX-9 2023"), "date": t("June 11, 2026", "11 de junio de 2026"),
     "q": "always friendly service, competitive pricing, and they may recommend additional services, but always as a recommendation, no pressure"},
    {"src": "CARFAX", "url": CARFAX_URL,
     "who": t("2014 Volvo XC90 owner", "Propietario de un Volvo XC90 2014"), "date": t("September 26, 2026", "26 de septiembre de 2026"),
     "q": "They listened to me and helped me diagnose the problem."},
    {"src": "CARFAX", "url": CARFAX_URL,
     "who": t("2023 Toyota Tacoma owner", "Propietario de una Toyota Tacoma 2023"), "date": t("September 17, 2026", "17 de septiembre de 2026"),
     "q": "Communication was also very good. Would recommend them to anyone."},
    {"src": "CARFAX", "url": CARFAX_URL,
     "who": t("2013 Honda Civic owner", "Propietario de un Honda Civic 2013"), "date": t("November 22, 2024", "22 de noviembre de 2024"),
     "q": "They are great communicators and make things much easier."},
    {"src": "Yelp", "url": YELP_URL,
     "who": t("D. C.", "D. C."), "date": t("January 12, 2022", "12 de enero de 2022"),
     "q": "I have been bringing my cars to Diverse Autoworks for many years. Joe and his team are awesome, upfront and honest. The facility and waiting areas are very clean and accommodating."},
    {"src": "Yelp", "url": YELP_URL,
     "who": t("Michael A.", "Michael A."), "date": t("January 21, 2019", "21 de enero de 2019"),
     "q": "Reliable and hardworking. We bring all our cars there for everything from inspections, tires, etc."},
]

# Rating summaries, read from owner-supplied screenshots on Oct 6, 2026. Plain text only: no platform logos or look-alike widgets.
RATINGS_ASOF = t("October 6, 2026", "6 de octubre de 2026")
RATINGS = [
    {"name": "Google", "url": "", "avg": "4.9", "count": 34,
     "line": t("34 Google reviews", "34 reseñas en Google"), "bars": None},
    {"name": "Yelp", "url": YELP_URL, "avg": None, "count": 10,
     "line": t("10 Yelp reviews: 9 five-star, 1 one-star (2018)", "10 reseñas en Yelp: 9 de cinco estrellas, 1 de una estrella (2018)"),
     "bars": [(5, 90), (4, 0), (3, 0), (2, 0), (1, 10)]},
    {"name": "CARFAX", "url": CARFAX_URL, "avg": "5.0", "count": 61,
     "line": t("61 verified CARFAX reviews", "61 reseñas verificadas en CARFAX"),
     "bars": [(5, 98), (4, 2), (3, 0), (2, 0), (1, 0)]},
]

THEMES = [
    t("Clear explanations", "Explicaciones claras"),
    t("Friendly service", "Trato amable"),
    t("Fair pricing", "Precios justos"),
    t("Practical recommendations", "Recomendaciones prácticas"),
]

# ---------------------------------------------------------------- FAQs
# category id, title, items. 36 service FAQs (12 x 3) + general.
FAQ_CATS = [
    {"id": "inspections", "title": t("State inspections & emissions testing", "Inspecciones estatales y pruebas de emisiones"), "items": [
        (t("Do you offer state inspections and emissions testing?", "¿Ofrecen inspecciones estatales y pruebas de emisiones?"),
         t("Yes. Diverse Autoworks offers state inspection and emissions services. Call 610-650-0316 to arrange a visit and confirm which inspection applies to your vehicle.",
           "Sí. Diverse Autoworks ofrece servicios de inspección estatal y de emisiones. Llame al 610-650-0316 para coordinar su visita y confirmar qué inspección corresponde a su vehículo.")),
        (t("What types of vehicles do you inspect?", "¿Qué tipos de vehículos inspeccionan?"),
         t("Our advertised inspection services include cars, trucks, trailers, and motorcycles. Contact us with your vehicle details to confirm availability. Not every vehicle type requires the same testing.",
           "Nuestros servicios de inspección anunciados incluyen autos, camiones, remolques y motocicletas. Comuníquese con nosotros con los datos de su vehículo para confirmar la disponibilidad. No todos los tipos de vehículo requieren las mismas pruebas.")),
        (t("How much does an inspection cost, and how long does it take?", "¿Cuánto cuesta una inspección y cuánto tarda?"),
         t("Please call for current pricing and appointment availability. Timing depends on your vehicle and the inspection required; we do not publish a fixed completion-time guarantee.",
           "Llame para conocer los precios actuales y la disponibilidad de citas. El tiempo depende de su vehículo y de la inspección requerida; no publicamos una garantía de tiempo de entrega fijo.")),
    ]},
    {"id": "motorcycle", "title": t("Motorcycle inspections", "Inspecciones de motocicletas"), "items": [
        (t("Do you perform motorcycle state inspections?", "¿Realizan inspecciones estatales de motocicletas?"),
         t("Yes. Motorcycle state inspections are included in our inspection services. Call the shop to arrange your visit.",
           "Sí. Las inspecciones estatales de motocicletas forman parte de nuestros servicios de inspección. Llame al taller para coordinar su visita.")),
        (t("What does a Pennsylvania motorcycle safety inspection cover?", "¿Qué cubre la inspección de seguridad de motocicletas en Pensilvania?"),
         t("PennDOT lists items including brakes, steering, suspension, tires and wheels, lights and electrical systems, mirrors, fuel and exhaust systems, the horn, and the body and chassis. An inspection evaluates the required safety components; it is not the same as a complete engine-service appointment.",
           "PennDOT enumera elementos como los frenos, la dirección, la suspensión, las llantas y ruedas, las luces y el sistema eléctrico, los espejos, los sistemas de combustible y escape, la bocina, y la carrocería y el chasis. Una inspección evalúa los componentes de seguridad requeridos; no es lo mismo que una cita completa de servicio del motor.")),
        (t("Do you offer motorcycle repairs as well as inspections?", "¿Ofrecen reparación de motocicletas además de inspecciones?"),
         t("Our published motorcycle offering is state inspection. Please call with your motorcycle's year, make, model, and repair needs to confirm whether we can help with anything beyond the inspection.",
           "Nuestro servicio publicado para motocicletas es la inspección estatal. Llame con el año, la marca, el modelo y las necesidades de reparación de su motocicleta para confirmar si podemos ayudarle con algo más que la inspección.")),
    ]},
    {"id": "maintenance", "title": t("Oil changes & routine maintenance", "Cambios de aceite y mantenimiento de rutina"), "items": [
        (t("What routine maintenance services do you offer?", "¿Qué servicios de mantenimiento de rutina ofrecen?"),
         t("Our service list includes oil changes, cabin air filters, fuel filters, fan and accessory belts, and wiper blade replacement. Call to discuss the maintenance needed for your vehicle.",
           "Nuestra lista de servicios incluye cambios de aceite, filtros de aire de cabina, filtros de combustible, bandas del ventilador y de accesorios, y reemplazo de plumillas limpiaparabrisas. Llame para hablar del mantenimiento que necesita su vehículo.")),
        (t("How often should I change my oil?", "¿Cada cuánto debo cambiar el aceite?"),
         t("Follow the maintenance schedule and oil specifications for your vehicle. Intervals vary by model, oil requirements, and driving conditions; one fixed interval is not appropriate for every vehicle.",
           "Siga el programa de mantenimiento y las especificaciones de aceite de su vehículo. Los intervalos varían según el modelo, el tipo de aceite requerido y las condiciones de manejo; un solo intervalo fijo no es adecuado para todos los vehículos.")),
        (t("Can I combine an oil change with another service?", "¿Puedo combinar un cambio de aceite con otro servicio?"),
         t("When you call, let us know all the work you would like performed. The shop can confirm whether the requested services can be scheduled together.",
           "Cuando llame, cuéntenos todo el trabajo que desea realizar. El taller puede confirmar si los servicios solicitados se pueden programar juntos.")),
    ]},
    {"id": "engine", "title": t("Engine analysis, tune-ups & fuel systems", "Análisis del motor, afinaciones y sistemas de combustible"), "items": [
        (t("Do you offer engine diagnostics and tune-ups?", "¿Ofrecen diagnóstico del motor y afinaciones?"),
         t("Yes. We offer engine analysis, engine tune-ups, fuel-injector cleaning, and engine repair. Call 610-650-0316 and describe the problem so we can book the right appointment.",
           "Sí. Ofrecemos análisis del motor, afinaciones, limpieza de inyectores y reparación del motor. Llame al 610-650-0316 y describa el problema para programar la cita adecuada.")),
        (t("What should I tell you when requesting engine analysis?", "¿Qué debo decirles al solicitar un análisis del motor?"),
         t("Tell us your vehicle's year, make, and model, what you have noticed, when it happens, and whether a warning light is showing. Mention any recent work as well. This information helps explain your request; it does not replace an assessment of the vehicle.",
           "Indíquenos el año, la marca y el modelo de su vehículo, lo que ha notado, cuándo ocurre y si hay una luz de advertencia encendida. Mencione también cualquier trabajo reciente. Esta información ayuda a explicar su solicitud; no reemplaza la evaluación del vehículo.")),
        (t("What engine problems do you repair?", "¿Qué problemas del motor reparan?"),
         t("Ignition and fuel: spark plugs, ignition coils, fuel injectors, fuel pump, fuel filter, fuel lines, fuel pressure regulator, throttle body, and mass airflow sensor. Air and emissions: air filter, vacuum leaks, PCV valve, intake manifold gasket, oxygen sensors, catalytic converter, EGR valve, and EVAP leaks. Sensors and electronics: engine control module, coolant temperature, manifold pressure, throttle position, and knock sensors, and check-engine diagnosis. Cooling: water pump, thermostat, radiator, hoses, cooling fan, coolant leaks, coolant flush, and head gasket. Oil and seals: oil pump, oil pressure sensor, valve cover, oil pan, rear main and front crankshaft seals, and oil consumption. Timing and valves: timing belt or chain, tensioner, guides, valve adjustment, valve seals, rocker arms, lifters, and camshaft and crankshaft seals. Belts and accessories: serpentine and accessory belts, tensioners, idler pulleys, alternator, and A/C compressor. Internal: compression loss, piston rings, cylinder head cracks, cylinder head and block repair, rod and main bearing knock, and engine rebuild or replacement. Mounts: motor mounts.",
            "Ignición y combustible: bujías, bobinas de encendido, inyectores de combustible, bomba de combustible, filtro de combustible, líneas de combustible, regulador de presión de combustible, cuerpo de aceleración y sensor de flujo de aire. Aire y emisiones: filtro de aire, fugas de vacío, válvula PCV, junta del múltiple de admisión, sensores de oxígeno, convertidor catalítico, válvula EGR y fugas EVAP. Sensores y electrónica: módulo de control del motor, sensores de temperatura del refrigerante, presión del múltiple, posición del acelerador y detonación, y diagnóstico de la luz de revisión del motor. Enfriamiento: bomba de agua, termostato, radiador, mangueras, ventilador de enfriamiento, fugas de refrigerante, cambio del sistema de refrigerante y junta de culata. Aceite y sellos: bomba de aceite, sensor de presión de aceite, tapa de válvulas, cárter, sellos del cigüeñal trasero y delantero, y consumo de aceite. Distribución y válvulas: correa o cadena de distribución, tensor, guías, ajuste de válvulas, sellos de válvulas, balancines, levantadores, y sellos del árbol de levas y del cigüeñal. Correas y accesorios: correas de accesorios, tensores, poleas locas, alternador y compresor de A/C. Internos: pérdida de compresión, anillos de pistón, grietas en la culata, reparación de culata y bloque, golpeteo de cojinetes de biela y de bancada, y reconstrucción o reemplazo del motor. Soportes: soportes del motor."),
         ),
        (t("What symptoms should I call about?", "¿Qué síntomas debo reportar?"),
         t("Misfires, rough idle, stalling, hesitation, loss of power, poor fuel economy, knocking or pinging, overheating, blue, white, or black exhaust smoke, ticking, knocking, whining, or tapping noises, and a check-engine light. Several causes can produce the same symptom, so the shop needs to diagnose it.",
            "Fallos de encendido, ralentí irregular, apagones, vacilación, pérdida de potencia, bajo rendimiento de combustible, golpeteo o detonación, sobrecalentamiento, humo de escape azul, blanco o negro, ruidos de tictac, golpeteo, silbido o chasquido, y la luz de revisión del motor. Varias causas pueden producir el mismo síntoma, por lo que el taller debe diagnosticarlo."),
        ),
        (t("Do you rebuild or replace engines?", "¿Reconstruyen o reemplazan motores?"),
         t("Yes. Engine rebuild and replacement are part of our engine repair work. Call 610-650-0316 to discuss the work your vehicle needs.",
           "Sí. La reconstrucción y el reemplazo del motor forman parte de nuestro trabajo de reparación del motor. Llame al 610-650-0316 para hablar del trabajo que necesita su vehículo.")),
    ]},
    {"id": "brakes", "title": t("Brakes & rotors", "Frenos y rotores"), "items": [
        (t("Do you service brakes and rotors?", "¿Dan servicio a frenos y rotores?"),
         t("Yes. Brake and rotor services are part of our advertised repair offerings. Call to discuss your vehicle and your braking concerns.",
           "Sí. Los servicios de frenos y rotores forman parte de nuestras reparaciones anunciadas. Llame para hablar de su vehículo y de sus inquietudes sobre los frenos.")),
        (t("What signs mean I should have my brakes checked?", "¿Qué señales indican que debo revisar los frenos?"),
         t("Changes in braking response, a soft or spongy pedal, and grinding or scraping sounds warrant prompt attention. Do not wait for a routine maintenance appointment to raise a braking concern.",
           "Los cambios en la respuesta de los frenos, un pedal blando o esponjoso y los sonidos de rechinido o raspado requieren atención pronta. No espere a una cita de mantenimiento de rutina para plantear un problema de frenos.")),
        (t("Do you offer free brake inspections or publish fixed brake prices?", "¿Ofrecen inspecciones de frenos gratis o publican precios fijos de frenos?"),
         t("Call for current brake-assessment fees and service pricing for your vehicle.",
           "Llame para conocer las tarifas actuales de evaluación de frenos y los precios del servicio para su vehículo.")),
    ]},
    {"id": "tires", "title": t("Tires, tire repairs & wheel alignments", "Llantas, reparación de llantas y alineación"), "items": [
        (t("What tire services do you offer?", "¿Qué servicios de llantas ofrecen?"),
         t("Our published services include tires, tire repairs, and wheel alignments. Contact the shop to discuss the work your vehicle needs.",
           "Nuestros servicios publicados incluyen llantas, reparación de llantas y alineación de ruedas. Comuníquese con el taller para hablar del trabajo que necesita su vehículo.")),
        (t("How can I tell whether I might need an alignment?", "¿Cómo sé si podría necesitar una alineación?"),
         t("Pulling to one side, an off-center steering wheel, or uneven tire wear can indicate an alignment concern. Other tire or suspension issues can cause similar symptoms, so the cause needs to be assessed rather than assumed.",
           "Que el vehículo se vaya hacia un lado, que el volante quede descentrado o que las llantas se desgasten de forma despareja puede indicar un problema de alineación. Otros problemas de llantas o suspensión pueden causar síntomas parecidos, por lo que hay que evaluar la causa en lugar de suponerla.")),
        (t("Do you offer tire rotations and balancing?", "¿Ofrecen rotación y balanceo de llantas?"),
         t("Yes. We rotate and balance tires. Call for current pricing and to schedule.",
           "Sí. Rotamos y balanceamos llantas. Llame para conocer el precio actual y programar su cita.")),
    ]},
    {"id": "suspension", "title": t("Steering & suspension", "Dirección y suspensión"), "items": [
        (t("What steering and suspension work do you offer?", "¿Qué trabajos de dirección y suspensión ofrecen?"),
         t("Our advertised service range includes steering parts, suspension parts, shock absorbers, and struts. Call with your vehicle details to discuss the work needed.",
           "Nuestra gama de servicios anunciada incluye piezas de dirección, piezas de suspensión, amortiguadores y puntales. Llame con los datos de su vehículo para hablar del trabajo necesario.")),
        (t("Is a wheel alignment the same as suspension repair?", "¿Una alineación de ruedas es lo mismo que reparar la suspensión?"),
         t("No. Alignment adjusts suspension angles to the vehicle's specifications. Repairing worn or damaged suspension parts is a separate task. The work needed depends on the condition of your vehicle.",
           "No. La alineación ajusta los ángulos de la suspensión según las especificaciones del vehículo. Reparar piezas de suspensión desgastadas o dañadas es un trabajo aparte. El trabajo necesario depende del estado de su vehículo.")),
        (t("Can pulling or vibration have more than one cause?", "¿Puede haber más de una causa cuando el vehículo se va hacia un lado o vibra?"),
         t("Yes. Tire pressure, tire condition, wheel balance, alignment, and suspension problems can produce overlapping symptoms. Describe when the problem occurs when you contact the shop.",
           "Sí. La presión y el estado de las llantas, el balanceo de las ruedas, la alineación y los problemas de suspensión pueden producir síntomas que se superponen. Al comunicarse con el taller, describa cuándo ocurre el problema.")),
    ]},
    {"id": "ac", "title": t("Air conditioning & cooling systems", "Aire acondicionado y sistemas de enfriamiento"), "items": [
        (t("Do you service automotive air conditioning?", "¿Dan servicio al aire acondicionado automotriz?"),
         t("Yes. A/C service is listed among our services. Call with your vehicle details and describe the problem so we can confirm the appropriate service.",
           "Sí. El servicio de A/C figura entre nuestros servicios. Llame con los datos de su vehículo y describa el problema para que podamos confirmar el servicio adecuado.")),
        (t("Do you also work on the engine cooling system?", "¿También trabajan en el sistema de enfriamiento del motor?"),
         t("Yes. Cooling-system service is included in our published service range. Contact us about the particular issue or component you need assessed.",
           "Sí. El servicio del sistema de enfriamiento está incluido en nuestra gama de servicios publicada. Comuníquese con nosotros sobre el problema o el componente específico que necesita evaluar.")),
        (t("Can you service every refrigerant type or replace any cooling-system component?", "¿Pueden dar servicio a todos los tipos de refrigerante o reemplazar cualquier componente del sistema de enfriamiento?"),
         t("Please call with your vehicle details to confirm the refrigerant type, A/C service, or cooling-system component work we can handle.",
           "Llame con los datos de su vehículo para confirmar el tipo de refrigerante, el servicio de A/C o el trabajo en componentes del sistema de enfriamiento que podemos realizar.")),
    ]},
    {"id": "battery", "title": t("Batteries", "Baterías"), "items": [
        (t("Do you offer battery service?", "¿Ofrecen servicio de baterías?"),
         t("Yes. We test and replace batteries, and we diagnose starting and charging system problems. Call to discuss your vehicle and its battery needs.",
           "Sí. Probamos y reemplazamos baterías, y diagnosticamos problemas del sistema de arranque y carga. Llame para hablar de su vehículo y de lo que necesita su batería.")),
        (t("Can you help if my vehicle will not start?", "¿Pueden ayudarme si mi vehículo no arranca?"),
         t("Yes. We diagnose no-start problems, including battery, starter, and charging-system faults. Call and describe the symptoms.",
           "Sí. Diagnosticamos fallas de arranque, incluidas fallas de la batería, del motor de arranque y del sistema de carga. Llame y describa los síntomas.")),
        (t("What signs suggest my battery may need replacing?", "¿Qué señales indican que mi batería podría necesitar reemplazo?"),
         t("A slow crank, dim lights, a battery warning light, or a battery that is several years old can all be reported. A charging-system fault can cause similar signs, so the cause needs to be assessed. For alternator or starter work, see Alternators & starters.",
           "Un arranque lento, luces tenues, una luz de advertencia de la batería o una batería con varios años de uso son señales que se pueden reportar. Una falla del sistema de carga puede causar señales parecidas, por lo que hay que evaluar la causa. Para trabajos de alternador o motor de arranque, vea Alternadores y motores de arranque.")),
    ]},
    {"id": "drivetrain", "title": t("Transmission maintenance & rear-axle service", "Mantenimiento de transmisión y servicio del eje trasero"), "items": [
        (t("Do you offer transmission maintenance?", "¿Ofrecen mantenimiento de transmisión?"),
         t("Yes. Transmission maintenance is included in our service list. Contact us with your vehicle details to discuss the appropriate service.",
           "Sí. El mantenimiento de transmisión está incluido en nuestra lista de servicios. Comuníquese con nosotros con los datos de su vehículo para hablar del servicio adecuado.")),
        (t("How often should transmission maintenance be performed?", "¿Cada cuánto se debe dar mantenimiento a la transmisión?"),
         t("Use the manufacturer's maintenance schedule for your vehicle and driving conditions. Transmission types and fluid requirements differ, so a single interval should not be applied to every vehicle.",
           "Use el programa de mantenimiento del fabricante para su vehículo y sus condiciones de manejo. Los tipos de transmisión y los requisitos de líquido difieren, por lo que no se debe aplicar un solo intervalo a todos los vehículos.")),
        (t("Do you rebuild transmissions or service rear-axle bearings and seals?", "¿Reconstruyen transmisiones o dan servicio a los cojinetes y sellos del eje trasero?"),
         t("Yes. We service rear-axle bearings and seals, and we rebuild and replace transmissions. Call with your vehicle details to discuss the work.",
           "Sí. Damos servicio a los cojinetes y sellos del eje trasero, y reconstruimos y reemplazamos transmisiones. Llame con los datos de su vehículo para hablar del trabajo.")),
    ]},
    {"id": "fleet", "title": t("Fleet repairs", "Reparaciones para flotas"), "items": [
        (t("Do you work with business fleets?", "¿Trabajan con flotas de empresas?"),
         t("Yes. Diverse Autoworks advertises fleet repairs. Call to discuss your business vehicles and repair needs.",
           "Sí. Diverse Autoworks anuncia reparaciones para flotas. Llame para hablar de los vehículos de su empresa y de sus necesidades de reparación.")),
        (t("What information should I provide for a fleet inquiry?", "¿Qué información debo dar al consultar por una flota?"),
         t("Tell us the number of vehicles, their years/makes/models, the work needed, and your preferred scheduling arrangements. Include a contact person for your business.",
           "Indíquenos la cantidad de vehículos, el año, la marca y el modelo de cada uno, el trabajo necesario y sus preferencias de programación. Incluya una persona de contacto de su empresa.")),
        (t("Do fleet customers receive special rates, account billing, or priority appointments?", "¿Los clientes con flotas reciben tarifas especiales, facturación por cuenta o citas prioritarias?"),
         t("Those arrangements are not specified in our published information. Discuss pricing, billing, and scheduling directly with the shop before relying on a particular fleet arrangement.",
           "Esos arreglos no se especifican en nuestra información publicada. Hable directamente con el taller sobre precios, facturación y programación antes de contar con un arreglo en particular.")),
    ]},
    {"id": "notary", "title": t("Notary services", "Servicios de notario público"), "items": [
        (t("Do you offer notary services?", "¿Ofrecen servicios de notario público?"),
         t("Yes. Diverse Autoworks advertises notary services in addition to automotive services.",
           "Sí. Diverse Autoworks anuncia servicios de notario público además de los servicios automotrices.")),
        (t("What are your notary hours?", "¿Cuál es su horario de notario?"),
         t("Our listed notary hours are Monday–Friday, 8 a.m.–3 p.m. These differ from repair-shop hours. Call ahead to confirm availability.",
           "Nuestro horario de notario publicado es de lunes a viernes, de 8 a. m. a 3 p. m. Es distinto del horario del taller de reparación. Llame con anticipación para confirmar la disponibilidad.")),
        (t("Do you handle vehicle titles and tags, and what should I bring?", "¿Tramitan títulos y placas de vehículos, y qué debo llevar?"),
         t("Yes. We handle vehicle title and tag transactions. Call before your visit and we'll tell you which identification, documents, fees, and signers you need.",
           "Sí. Tramitamos títulos y placas de vehículos. Llame antes de su visita y le diremos qué identificación, documentos, tarifas y firmantes necesita.")),
    ]},
]

# extra visitor FAQs; "online-request" is only shown when a working form endpoint is configured
FAQ_GENERAL = {
    "id": "general", "title": t("General", "General"), "items": [
        (t("Where are you located?", "¿Dónde están ubicados?"),
         t("1415 Pawlings Road, Phoenixville, PA 19460.", "1415 Pawlings Road, Phoenixville, PA 19460.")),
    ],
    "online": (t("Can I request an appointment online?", "¿Puedo solicitar una cita en línea?"),
               t("Use the request form or call the shop. Your requested date is not confirmed until the team contacts you.",
                 "Use el formulario de solicitud o llame al taller. La fecha que solicite no queda confirmada hasta que el equipo se comunique con usted.")),
}

# ---------------------------------------------------------------- page copy
PAGES = {
    "home": {
        "title": t("Auto Repair Shop in Phoenixville, PA | Diverse Autoworks",
                   "Reparación de autos en Phoenixville, PA | Diverse Autoworks"),
        "desc": t("Auto repair and maintenance in Phoenixville, PA: brakes, tires, oil changes, PA state inspections, fleet repairs and notary. Call 610-650-0316.",
                  "Reparación y mantenimiento de autos en Phoenixville, PA: frenos, llantas, inspecciones estatales de PA y flotas. Llame al 610-650-0316."),
        "h1": t("Auto Repair & State Inspections in Phoenixville, PA",
                "Reparación de autos e inspecciones estatales en Phoenixville, PA"),
        "lead": t("Keep your vehicle moving with mechanical repairs, routine maintenance, and inspection services from Diverse Autoworks. From oil changes and brakes to diagnostics and fleet repairs, our team is here to help you care for your vehicle.",
                  "Mantenga su vehículo en marcha con reparaciones mecánicas, mantenimiento de rutina y servicios de inspección de Diverse Autoworks. Desde cambios de aceite y frenos hasta diagnósticos y reparaciones para flotas, nuestro equipo está aquí para ayudarle a cuidar su vehículo."),
        "svc_h": t("Care for Your Vehicle, All in One Place", "Cuide su vehículo, todo en un solo lugar"),
        "svc_p": t("Explore our inspection, maintenance, and repair services. Call us to discuss your vehicle and the work you need.",
                   "Conozca nuestros servicios de inspección, mantenimiento y reparación. Llámenos para hablar de su vehículo y del trabajo que necesita."),
        "moto_h": t("Motorcycle State Inspections", "Inspecciones estatales de motocicletas"),
        "moto_p": t("Diverse Autoworks offers state inspections for motorcycles, along with cars, trucks, and trailers. Call to arrange an inspection and confirm availability.",
                    "Diverse Autoworks ofrece inspecciones estatales para motocicletas, además de autos, camiones y remolques. Llame para coordinar una inspección y confirmar la disponibilidad."),
        "moto_btn": t("Call About a Motorcycle Inspection", "Llame por una inspección de motocicleta"),
        "rev_h": t("What Customers Appreciate", "Lo que valoran nuestros clientes"),
        "rev_p": t("Customers frequently mention clear explanations, friendly service, fair pricing, and practical repair recommendations.",
                   "Los clientes mencionan con frecuencia las explicaciones claras, el trato amable, los precios justos y las recomendaciones de reparación prácticas."),
        "fleet_p": t("Need repair support for business vehicles? Diverse Autoworks offers fleet repairs. Contact the shop to discuss your vehicles and service needs.",
                     "¿Necesita apoyo de reparación para vehículos de negocio? Diverse Autoworks ofrece reparaciones para flotas. Comuníquese con el taller para hablar de sus vehículos y sus necesidades de servicio."),
        "notary_p": t("Notary services are available Monday through Friday, 8 a.m.–3 p.m. Call ahead to confirm availability and any requirements for your documents.",
                      "Los servicios de notario público están disponibles de lunes a viernes, de 8 a. m. a 3 p. m. Llame con anticipación para confirmar la disponibilidad y los requisitos para sus documentos."),
        "close_h": t("Call or Visit Diverse Autoworks", "Llame o visite Diverse Autoworks"),
        "close_p": t("Find us at 1415 Pawlings Road in Phoenixville. Call 610-650-0316 to discuss a repair, request an inspection, or ask about fleet and notary services.",
                     "Nos encuentra en 1415 Pawlings Road, en Phoenixville. Llame al 610-650-0316 para hablar de una reparación, solicitar una inspección o preguntar por los servicios para flotas y de notario público."),
    },
    "services": {
        "title": t("Brakes, Tires, Engine & A/C Repair in Phoenixville, PA",
                   "Frenos, llantas, motor y A/C en Phoenixville, PA"),
        "desc": t("Oil changes, brakes, tires and alignments, engine repair, suspension, A/C, batteries, fleet repairs and notary in Phoenixville, PA.",
                  "Cambios de aceite, frenos, llantas, alineación, motor, suspensión, A/C, baterías, flotas y notario público en Phoenixville, PA."),
        "h1": t("Auto Repair Services in Phoenixville, PA", "Servicios de reparación de autos en Phoenixville, PA"),
        "lead": t("Inspection, maintenance, and repair services for your vehicle, minor or major. Call 610-650-0316 with your vehicle's year, make, and model to schedule.",
                  "Servicios de inspección, mantenimiento y reparación para su vehículo, menores o mayores. Llame al 610-650-0316 con el año, la marca y el modelo de su vehículo para programar su cita."),
    },
    "inspections": {
        "title": t("PA State Inspection & Emissions in Phoenixville, PA",
                   "Inspección estatal y de emisiones de PA en Phoenixville"),
        "desc": t("PA safety inspections and emissions testing for cars, trucks, trailers and motorcycles at 1415 Pawlings Rd, Phoenixville. Call 610-650-0316.",
                  "Inspección de seguridad y de emisiones de PA para autos, camiones, remolques y motocicletas en Phoenixville. Llame al 610-650-0316."),
        "h1": t("PA State Inspections & Emissions Testing in Phoenixville", "Inspecciones estatales y de emisiones de PA en Phoenixville"),
        "lead": t("Diverse Autoworks offers state inspection and emissions services for cars, trucks, trailers, and motorcycles. Call 610-650-0316 and we'll tell you which inspection your vehicle needs and set up a visit.",
                  "Diverse Autoworks ofrece servicios de inspección estatal y de emisiones para autos, camiones, remolques y motocicletas. Llame al 610-650-0316 y le diremos qué inspección necesita su vehículo y coordinaremos su visita."),
        "two_h": t("Safety inspection and emissions testing are separate", "La inspección de seguridad y la prueba de emisiones son distintas"),
        "two_p": t("Not every vehicle type requires the same testing. Call with your vehicle's details and we will confirm what applies.",
                   "No todos los tipos de vehículo requieren las mismas pruebas. Llame con los datos de su vehículo y le confirmaremos qué corresponde."),
        "safety_h": t("State safety inspection", "Inspección estatal de seguridad"),
        "safety_p": t("Offered for cars, trucks, trailers, and motorcycles.", "Disponible para autos, camiones, remolques y motocicletas."),
        "emis_h": t("Emissions testing", "Pruebas de emisiones"),
        "emis_p": t("Offered as part of our state inspection and emissions services. Call and we'll tell you whether your vehicle needs it.",
                    "Disponible como parte de nuestros servicios de inspección estatal y de emisiones. Llame y le diremos si su vehículo la necesita."),
        "types_h": t("Vehicles we inspect", "Vehículos que inspeccionamos"),
        "types": [t("Cars", "Autos"), t("Trucks", "Camiones"), t("Trailers", "Remolques"), t("Motorcycles", "Motocicletas")],
        "price_h": t("Pricing and timing", "Precios y tiempos"),
        "price_p": t("PennDOT says inspection fees are posted at official inspection stations and do not include repairs to correct defects. Call 610-650-0316 for our current fee and appointment availability. Timing depends on your vehicle and the inspection required; we do not publish a fixed completion-time guarantee.",
                     "PennDOT indica que las tarifas de inspección se publican en las estaciones de inspección oficiales y no incluyen las reparaciones para corregir defectos. Llame al 610-650-0316 para conocer nuestra tarifa actual y la disponibilidad de citas. El tiempo depende de su vehículo y de la inspección requerida; no publicamos una garantía de tiempo de finalización fija."),
        "facts_h": t("What to expect at a PA inspection", "Qué esperar en una inspección de PA"),
        "facts": [
            (t("What the safety inspection checks", "Qué revisa la inspección de seguridad"),
             t("PennDOT lists these items for passenger cars and light-duty trucks: suspension components, steering, braking systems, tires and wheels, lighting and electrical systems, glass, mirrors, windshield washer, defroster, wipers, fuel systems, the speedometer, the odometer, exhaust systems, horns and warning devices, the body and the chassis.",
               "PennDOT enumera estos elementos para autos de pasajeros y camionetas ligeras: componentes de la suspensión, dirección, sistemas de frenos, llantas y ruedas, sistemas de iluminación y eléctricos, cristales, espejos, lavaparabrisas, desempañador, limpiaparabrisas, sistemas de combustible, velocímetro, odómetro, sistemas de escape, bocina y dispositivos de advertencia, la carrocería y el chasis.")),
            (t("Your inspection sticker", "Su calcomanía de inspección"),
             t("After a pass, most passenger cars and light trucks get a sticker valid for one year from the month of inspection or one year from the expiration of the current sticker, according to PennDOT.",
               "Después de aprobar, la mayoría de los autos de pasajeros y camionetas ligeras reciben una calcomanía válida por un año a partir del mes de la inspección o por un año a partir del vencimiento de la calcomanía actual, según PennDOT.")),
            (t("Emissions testing in Chester County", "Pruebas de emisiones en el condado de Chester"),
             t("Chester County is part of Pennsylvania's Philadelphia-area emissions region, along with Bucks, Delaware, Montgomery and Philadelphia counties, according to Drive Clean PA. Which emissions test applies depends on your vehicle, so call us with its year and type.",
               "El condado de Chester forma parte de la región de emisiones del área de Filadelfia de Pensilvania, junto con los condados de Bucks, Delaware, Montgomery y Filadelfia, según Drive Clean PA. La prueba de emisiones que corresponde depende de su vehículo; llámenos con el año y el tipo.")),
        ],
        "src_lead": t("Sources:", "Fuentes:"),
        "src": [
            (t("PennDOT safety inspection FAQs for consumers", "Preguntas frecuentes de PennDOT sobre la inspección de seguridad"),
             "https://www.pa.gov/agencies/dmv/faqs/motor-vehicle-faqs/safety-inspection-consumers-faqs"),
            (t("PennDOT station owner and mechanic page", "Página de PennDOT para estaciones y mecánicos"),
             "https://www.pa.gov/agencies/dmv/vehicle-services/inspection-and-safety-requirements/station-owner-and-mechanic"),
            (t("Drive Clean PA: Philadelphia area", "Drive Clean PA: área de Filadelfia"),
             "http://www.drivecleanpa.state.pa.us/info_se.htm"),
        ],
        "moto_h": t("Motorcycle state inspections", "Inspecciones estatales de motocicletas"),
        "moto_p": t("Motorcycle state inspections are part of our inspection services, and Pennsylvania motorcycles can now be inspected year-round. Call the shop to arrange your visit, or read the guide to see what PennDOT covers.",
                    "Las inspecciones estatales de motocicletas forman parte de nuestros servicios de inspección, y las motocicletas de Pensilvania ahora se pueden inspeccionar todo el año. Llame al taller para coordinar su visita, o lea la guía para ver qué cubre PennDOT."),
    },
    "moto": {
        "title": t("Motorcycle Inspection in Phoenixville, PA | Year-Round",
                   "Inspección de motocicletas en Phoenixville, PA | Todo el año"),
        "desc": t("PA motorcycle safety inspections are now year-round. Diverse Autoworks inspects motorcycles in Phoenixville, PA. Call 610-650-0316.",
                  "Las inspecciones de motocicletas en Pensilvania ahora son todo el año. Diverse Autoworks, Phoenixville, PA. Llame al 610-650-0316."),
        "h1": t("Motorcycle state inspection in Phoenixville, PA (now year-round)",
                "Inspección estatal de motocicletas en Phoenixville, PA (ahora todo el año)"),
        "lead": t("Pennsylvania motorcycles can now be inspected in any month of the year. Call 610-650-0316 to arrange your motorcycle inspection at Diverse Autoworks.",
                  "Las motocicletas de Pensilvania ahora se pueden inspeccionar en cualquier mes del año. Llame al 610-650-0316 para coordinar la inspección de su motocicleta en Diverse Autoworks."),
        "crumb": t("Motorcycle", "Motocicletas"),
        "short_h": t("Can motorcycles be inspected year-round in PA?", "¿Se pueden inspeccionar las motocicletas todo el año en PA?"),
        "list_lead": t("PennDOT lists these items for a motorcycle safety inspection:", "PennDOT enumera estos elementos para una inspección de seguridad de motocicletas:"),
        "call_h": t("Year-round motorcycle inspections", "Inspecciones de motocicletas todo el año"),
        "call_p": t("Under Pennsylvania Act 149 of 2024, which took effect on January 17, 2025, motorcycle safety inspections are no longer limited to March through October. PennDOT says a motorcycle that passes receives a sticker valid for one year from the expiration of the sticker being replaced, and a sticker may not be issued for more than 15 months from the month of inspection.",
                    "Según la Ley 149 de 2024 de Pensilvania, vigente desde el 17 de enero de 2025, las inspecciones de seguridad de motocicletas ya no se limitan de marzo a octubre. PennDOT indica que una motocicleta que aprueba recibe una calcomanía válida por un año a partir del vencimiento de la calcomanía que se reemplaza, y que la calcomanía no puede emitirse por más de 15 meses a partir del mes de la inspección."),
        "src_t": t("Source: PennDOT announcement", "Fuente: anuncio de PennDOT"),
        "src_url": "https://www.pa.gov/agencies/penndot/news-and-media/newsroom/statewide/2025/shapiro-administration-improves-motorcycle-owner-s-experience",
        "faq_h": t("Motorcycle inspection questions", "Preguntas sobre la inspección de motocicletas"),
        "faqs": [
            (t("Can I get my motorcycle inspected in winter?", "¿Puedo inspeccionar mi motocicleta en invierno?"),
             t("Yes. Since Act 149 of 2024 took effect on January 17, 2025, Pennsylvania motorcycle inspections can be done year-round instead of only March through October. Call 610-650-0316 to arrange your visit.",
               "Sí. Desde que la Ley 149 de 2024 entró en vigor el 17 de enero de 2025, las inspecciones de motocicletas en Pensilvania pueden hacerse todo el año y no solo de marzo a octubre. Llame al 610-650-0316 para coordinar su visita.")),
            (t("When does my new inspection sticker expire?", "¿Cuándo vence mi nueva calcomanía de inspección?"),
             t("PennDOT says the new sticker is valid for one year from the expiration of the sticker being replaced, and a motorcycle sticker may not be issued for more than 15 months from the month of inspection. If you are unsure, call us with your current sticker month.",
               "PennDOT indica que la nueva calcomanía es válida por un año a partir del vencimiento de la calcomanía que se reemplaza, y que la calcomanía de una motocicleta no puede emitirse por más de 15 meses a partir del mes de la inspección. Si tiene dudas, llámenos con el mes de su calcomanía actual.")),
            (t("Do you also inspect cars, trucks and trailers?", "¿También inspeccionan autos, camiones y remolques?"),
             t("Yes. We offer state inspection and emissions services for cars, trucks, trailers, and motorcycles. Call and we'll tell you which inspection your vehicle needs.",
               "Sí. Ofrecemos servicios de inspección estatal y de emisiones para autos, camiones, remolques y motocicletas. Llame y le diremos qué inspección necesita su vehículo.")),
        ],
        "covers_h": t("What a PA motorcycle inspection covers", "Qué cubre una inspección de motocicletas en PA"),
        "covers_p": t("Tap a part below to see which items PennDOT lists. Call the shop to arrange your visit.",
                      "Toque una parte para ver los elementos que enumera PennDOT. Llame al taller para coordinar su visita."),
        "visit_h": t("Visit Diverse Autoworks", "Visite Diverse Autoworks"),
        "visit_p": t("1415 Pawlings Road, Phoenixville, PA 19460. Call 610-650-0316 to arrange your inspection and confirm availability.",
                     "1415 Pawlings Road, Phoenixville, PA 19460. Llame al 610-650-0316 para coordinar su inspección y confirmar la disponibilidad."),
        "cars_btn": t("Cars, trucks and trailers: state inspections", "Autos, camiones y remolques: inspecciones estatales"),
        "more_btn": t("Year-round motorcycle inspection guide", "Guía de inspección de motocicletas todo el año"),
    },
    "fleet": {
        "title": t("Fleet Repairs in Phoenixville, PA | Diverse Autoworks",
                   "Reparaciones para flotas | Diverse Autoworks, Phoenixville"),
        "desc": t("Diverse Autoworks offers fleet repairs for business vehicles in Phoenixville, PA. Contact the shop to discuss your vehicles, repair needs, and scheduling.",
                  "Reparaciones para flotas de vehículos de negocio en Phoenixville, PA. Hable con el taller sobre sus vehículos y la programación."),
        "h1": t("Fleet Repairs in Phoenixville, PA", "Reparaciones para flotas en Phoenixville, PA"),
        "lead": t("Keep your business vehicles on your maintenance radar. Diverse Autoworks offers fleet repairs; call to discuss your vehicles, repair needs, and scheduling.",
                  "Mantenga los vehículos de su negocio en su radar de mantenimiento. Diverse Autoworks ofrece reparaciones para flotas; llame para hablar de sus vehículos, sus necesidades de reparación y la programación."),
        "tell_h": t("What to tell us", "Qué debe indicarnos"),
        "tell": [t("The number of vehicles", "La cantidad de vehículos"),
                 t("Year, make, and model of each", "Año, marca y modelo de cada uno"),
                 t("The work needed", "El trabajo necesario"),
                 t("Your preferred scheduling arrangements", "Sus preferencias de programación"),
                 t("A contact person for your business", "Una persona de contacto de su empresa")],
        "terms_h": t("Rates, billing, and scheduling", "Tarifas, facturación y programación"),
        "terms_p": t("Those arrangements are not specified in our published information. Discuss pricing, billing, and scheduling directly with the shop before relying on a particular fleet arrangement.",
                     "Esos arreglos no se especifican en nuestra información publicada. Hable directamente con el taller sobre precios, facturación y programación antes de contar con un arreglo en particular."),
        "form_h": t("Send a fleet inquiry", "Envíe una consulta para su flota"),
    },
    "about": {
        "title": t("About Diverse Autoworks | Auto Repair in Phoenixville, PA",
                   "Sobre Diverse Autoworks | Taller en Phoenixville, PA"),
        "desc": t("Diverse Autoworks, Inc. provides mechanical repair, maintenance, and inspection services at 1415 Pawlings Road in Phoenixville, PA.",
                  "Diverse Autoworks, Inc. ofrece reparación mecánica, mantenimiento y servicios de inspección en 1415 Pawlings Road, Phoenixville, PA."),
        "h1": t("Your Local Auto Repair Shop in Phoenixville", "Su taller mecánico local en Phoenixville"),
        "p1": t("Diverse Autoworks, Inc. provides mechanical repair, maintenance, and inspection services at 1415 Pawlings Road in Phoenixville. Our service range includes everyday maintenance, brakes, tires, alignments, engine analysis, steering and suspension work, A/C and cooling-system service, and fleet repairs. We also offer motorcycle state inspections and weekday notary services.",
                "Diverse Autoworks, Inc. ofrece servicios de reparación mecánica, mantenimiento e inspección en 1415 Pawlings Road, en Phoenixville. Nuestra gama de servicios incluye mantenimiento diario, frenos, llantas, alineaciones, análisis del motor, trabajos de dirección y suspensión, servicio de A/C y del sistema de enfriamiento, y reparaciones para flotas. También ofrecemos inspecciones estatales de motocicletas y servicios de notario público entre semana."),
        "p2": t("We focus on continued technician training and helping customers return to the road safely.",
                "Nos enfocamos en la capacitación continua de los técnicos y en ayudar a nuestros clientes a volver a la carretera de forma segura."),
        "hist_h": t("History", "Historia"),
        "hist_p1": t("Established in 2007.", "Fundado en 2007."),
        "hist_p2": t("Diverse Autoworks Inc. is a family run business in which our goal and main priority is to deliver complete satisfaction for every customer through honest and thorough workmanship, while still offering knowledgeable and friendly service at affordable rates. We are an auto repair shop specializing in both domestic and foreign vehicles. We offer State Inspection and Emissions services as well as tags and notary services. We stand behind our work, including A/C service, alignments, batteries, brakes and rotors, engine analysis and tune-ups, rear axle bearings and seals, shock absorbers and struts, transmission maintenance, and much more.",
                     "Diverse Autoworks Inc. es un negocio familiar cuyo objetivo y prioridad principal es brindar la plena satisfacción de cada cliente mediante un trabajo honesto y minucioso, y al mismo tiempo ofrecer un servicio cordial y con conocimiento a precios accesibles. Somos un taller mecánico especializado en vehículos nacionales y extranjeros. Ofrecemos inspecciones estatales y servicios de emisiones, así como trámites de placas y servicios de notario público. Respaldamos nuestro trabajo, incluidos el servicio de A/C, alineaciones, baterías, frenos y discos, análisis del motor y afinaciones, cojinetes y sellos del eje trasero, amortiguadores y puntales, mantenimiento de transmisión, y mucho más."),
        "range_h": t("What we work on", "En qué trabajamos"),
        "themes_h": t("What customers say they notice", "Lo que los clientes dicen que notan"),
        "themes_p": t("Customers frequently mention clear explanations, friendly service, fair pricing, and practical repair recommendations.",
                      "Los clientes mencionan con frecuencia las explicaciones claras, el trato amable, los precios justos y las recomendaciones de reparación prácticas."),
    },
    "reviews": {
        "title": t("Customer Reviews | Diverse Autoworks, Phoenixville PA",
                   "Reseñas de clientes | Diverse Autoworks, Phoenixville PA"),
        "desc": t("Selected customer review excerpts for Diverse Autoworks in Phoenixville, PA, with links to the full reviews on CARFAX and Yelp.",
                  "Extractos seleccionados de reseñas de clientes de Diverse Autoworks en Phoenixville, PA, con enlaces a las reseñas completas en CARFAX y Yelp."),
        "h1": t("What customers appreciate", "Lo que valoran nuestros clientes"),
        "lead": t("A few excerpts from public reviews. They are a selection, not the full record. Read the complete reviews on each platform.",
                  "Algunos extractos de reseñas públicas. Son una selección, no el registro completo. Lea las reseñas completas en cada plataforma."),
        "orig": t("Excerpt from the original review", "Extracto de la reseña original"),
        "orig_es": t("", "Traducido del inglés"),
        "more": t("Read the full reviews", "Lea las reseñas completas"),
    },
    "faq": {
        "title": t("Auto Repair & Inspection FAQs | Diverse Autoworks",
                   "Preguntas frecuentes | Diverse Autoworks, Phoenixville"),
        "desc": t("Answers about state and motorcycle inspections, oil changes, brakes, tires, A/C, batteries, fleet repairs and notary services at Diverse Autoworks.",
                  "Respuestas sobre inspecciones estatales y de motocicletas, aceite, frenos, llantas, A/C, baterías, flotas y notario en Diverse Autoworks."),
        "h1": t("Frequently asked questions", "Preguntas frecuentes"),
        "lead": t("Answers about our services. When something depends on your vehicle, call and we will confirm.",
                  "Respuestas sobre nuestros servicios. Cuando algo depende de su vehículo, llame y se lo confirmaremos."),
    },
    "contact": {
        "title": t("Contact & Directions | Diverse Autoworks, Phoenixville",
                   "Contacto y cómo llegar | Diverse Autoworks, Phoenixville PA"),
        "desc": t("Call 610-650-0316 or visit Diverse Autoworks at 1415 Pawlings Road, Phoenixville, PA 19460. Request an appointment, ask about fleet repairs, or notary services.",
                  "Llame al 610-650-0316 o visite Diverse Autoworks, 1415 Pawlings Road, Phoenixville, PA 19460. Cita, flotas y notario público."),
        "h1": t("Call or Visit Diverse Autoworks", "Llame o visite Diverse Autoworks"),
        "lead": t("Call 610-650-0316 to discuss a repair, request an inspection, or ask about fleet and notary services. Find us at 1415 Pawlings Road, Phoenixville, PA 19460.",
                  "Llame al 610-650-0316 para hablar de una reparación, solicitar una inspección o preguntar por los servicios para flotas y de notario público. Nos encuentra en 1415 Pawlings Road, Phoenixville, PA 19460."),
        "notary_h": t("Notary services", "Servicios de notario público"),
        "notary_p": t("Notary hours: Monday–Friday, 8 a.m.–3 p.m. Call ahead to confirm availability and requirements.",
                      "Horario de notario: de lunes a viernes, de 8 a. m. a 3 p. m. Llame con anticipación para confirmar la disponibilidad y los requisitos."),
        "form_h": t("Request an appointment", "Solicite una cita"),
    },
    "brands": {
        "title": t("Brands We Work On | Diverse Autoworks, Phoenixville PA",
                   "Marcas con las que trabajamos | Diverse Autoworks"),
        "desc": t("Diverse Autoworks works on domestic and foreign cars in Phoenixville, PA. See the brands we work on and call about your vehicle.",
                  "Diverse Autoworks trabaja con autos nacionales y extranjeros en Phoenixville, PA. Vea las marcas con las que trabajamos y llámenos por su vehículo."),
        "h1": t("Domestic and Foreign Brands We Work On", "Marcas nacionales y extranjeras con las que trabajamos"),
        "lead": t("We work on domestic and foreign cars. Find your brand below, then call 610-650-0316 with your year, make, and model to schedule.",
                  "Trabajamos con autos nacionales y extranjeros. Busque su marca abajo y llame al 610-650-0316 con el año, la marca y el modelo para programar su cita."),
        "note": t("Don't see your make? Call us to ask. Hybrid and electric vehicles: we service these too, except repairs on Tesla, Rivian, Lucid, Karma, and Polestar, which need factory software and high-voltage training. We don't service Rolls-Royce, McLaren, Bentley, Aston Martin, or Lotus, which need specialized tools.",
                  "¿No ve su marca? Llámenos para preguntar. Vehículos híbridos y eléctricos: también les damos servicio, excepto reparaciones de Tesla, Rivian, Lucid, Karma y Polestar, que requieren software de fábrica y capacitación en alto voltaje. No damos servicio a Rolls-Royce, McLaren, Bentley, Aston Martin ni Lotus, que requieren herramientas especializadas."),
    },
    "privacy": {
        "title": t("Privacy Notice | Diverse Autoworks", "Aviso de privacidad | Diverse Autoworks"),
        "desc": t("How the Diverse Autoworks website handles your information.", "Cómo el sitio web de Diverse Autoworks maneja su información."),
        "h1": t("Privacy notice", "Aviso de privacidad"),
    },
}

# Brand list for the Brands page. Origin is the company's headquarters country (None = no origin label).
_JP = t("Japan", "Japón"); _KR = t("South Korea", "Corea del Sur"); _DE = t("Germany", "Alemania")
_SE = t("Sweden", "Suecia"); _GB = t("UK", "Reino Unido"); _US = t("US", "EE. UU.")
BRAND_GROUPS = [
    (t("Brands with hybrid models", "Marcas con modelos híbridos"), [
        ("Toyota", _JP), ("Honda", _JP), ("Ford", _US), ("Jeep", None), ("Volkswagen", _DE),
        ("Mercedes-Benz", _DE), ("Audi", _DE)]),
    (t("US-headquartered brands", "Marcas con sede en EE. UU."), [
        ("Ford", _US), ("Lincoln", _US), ("Chevrolet", _US), ("GMC", _US), ("Buick", _US),
        ("Cadillac", _US)]),
    (t("Stellantis brands, built mainly in the US", "Marcas de Stellantis, fabricadas principalmente en EE. UU."), [
        ("Chrysler", None), ("Dodge", None), ("Jeep", None), ("Ram", None)]),
    (t("Mainstream foreign brands", "Marcas extranjeras populares"), [
        ("Toyota", _JP), ("Honda", _JP), ("Nissan", _JP), ("Mazda", _JP), ("Subaru", _JP),
        ("Mitsubishi", _JP), ("Hyundai", _KR), ("Kia", _KR), ("Volkswagen", _DE), ("BMW", _DE),
        ("Mercedes-Benz", _DE), ("Volvo", _SE), ("Audi", _DE)]),
    (t("Luxury and specialty brands", "Marcas de lujo y especializadas"), [
        ("Lexus", _JP), ("Acura", _JP), ("Infiniti", _JP), ("Genesis", _KR), ("Porsche", _DE),
        ("MINI", t("UK, BMW", "Reino Unido, BMW")), ("Jaguar", _GB), ("Land Rover", _GB)]),
    (t("Italian brands", "Marcas italianas"), [
        ("Fiat", t("Italy, Stellantis", "Italia, Stellantis")), ("Alfa Romeo", t("Italy, Stellantis", "Italia, Stellantis")),
        ("Maserati", t("Italy", "Italia"))]),
]

NOT_FOUND = {
    "h": t("That page isn't here", "Esa página no existe"),
    "p": t("The link may be old or mistyped. Try the home page, or call the shop at 610-650-0316.",
           "Es posible que el enlace sea antiguo o tenga un error. Pruebe la página de inicio o llame al taller al 610-650-0316."),
}


# ------------------------------------------------- "ask us about" services
# Owner confirmed all of these on Oct 30, 2026. They stay in their own
# "More services" group on /services/; wording is confirmed (no "call to confirm").
ASK_SERVICES = [
    {"id": "tags", "icon": "seal",
     "title": t("Tags & title work", "Placas y trámites de título"),
     "card": t("Tags & Title Work", "Placas y títulos"),
     "line": t("Ask about vehicle tag and title paperwork.", "Pregunte por los trámites de placas y título."),
     "desc": t("Diverse Autoworks handles vehicle tag and title paperwork, and you can take care of it alongside a notary visit. Call before you come to find out what to bring.",
               "Diverse Autoworks realiza trámites de placas y título de vehículos, y puede hacerlos junto con su visita al notario. Llame antes de venir para saber qué debe llevar."),
     "faq": "tags", "group": "ask"},
    {"id": "ev", "icon": "gear",
     "title": t("Electric and hybrid vehicles", "Vehículos eléctricos e híbridos"),
     "card": t("Electric & Hybrid", "Eléctricos e híbridos"),
     "line": t("Ask about electric and hybrid vehicles.", "Pregunte por vehículos eléctricos e híbridos."),
     "desc": t("We service electric and hybrid vehicles, except repairs on Tesla, Rivian, Lucid, Karma, and Polestar, which need factory software and high-voltage training. Call with the year, make, and model to discuss the work you need. This is not a manufacturer certification or a brand-specialist claim.",
               "Damos servicio a vehículos eléctricos e híbridos, excepto reparaciones de Tesla, Rivian, Lucid, Karma y Polestar, que requieren software de fábrica y capacitación en alto voltaje. Llame con el año, la marca y el modelo para hablar del trabajo que necesita. No es una certificación del fabricante ni una afirmación de especialidad en una marca."),
     "faq": "ev", "group": "ask"},
    {"id": "rotation", "icon": "tire",
     "title": t("Tire rotation & balancing", "Rotación y balanceo de llantas"),
     "card": t("Tire Rotation & Balancing", "Rotación y balanceo"),
     "line": t("Ask about tire rotation and balancing.", "Pregunte por la rotación y el balanceo de llantas."),
     "desc": t("We rotate and balance tires. Call for current pricing before you schedule, and tell us about any vibration or uneven wear you have noticed.",
               "Rotamos y balanceamos llantas. Llame para conocer los precios actuales antes de programar, y cuéntenos si ha notado vibración o desgaste desigual."),
     "faq": "rotation", "group": "ask"},
    {"id": "electrical", "icon": "battery",
     "title": t("Alternators & starters", "Alternadores y motores de arranque"),
     "card": t("Alternators & Starters", "Alternadores y arranques"),
     "line": t("Ask about alternator and starter repair.", "Pregunte por la reparación de alternadores y arranques."),
     "desc": t("We repair and replace alternators and starters. If your vehicle is slow to start, will not start, or the battery light is on, call and describe what happens.",
               "Reparamos y reemplazamos alternadores y motores de arranque. Si su vehículo tarda en arrancar, no arranca o la luz de la batería está encendida, llame y describa lo que ocurre."),
     "faq": "electrical", "group": "ask"},
    {"id": "pickup", "icon": "pin",
     "title": t("Pickup, drop-off & after-hours", "Recogida, entrega y fuera de horario"),
     "card": t("Pickup & Drop-off", "Recogida y entrega"),
     "line": t("Ask about drop-off, pickup, and after-hours arrangements.", "Pregunte por entrega, recogida y arreglos fuera de horario."),
     "desc": t("If you cannot bring your vehicle in during the day, we offer drop-off, pickup, and after-hours arrangements. Call to set them up for your visit.",
               "Si no puede traer su vehículo durante el día, ofrecemos entrega, recogida y arreglos fuera de horario. Llame para coordinarlos para su visita."),
     "faq": "pickup", "group": "ask"},
]

ASK_GROUP = ("ask", t("More services", "Más servicios"))

ASK_FAQ_CATS = [
    {"id": "tags", "title": t("Tags & title work", "Placas y trámites de título"), "items": [
        (t("Do you handle vehicle tags and titles?", "¿Realizan trámites de placas y título de vehículos?"),
         t("Yes. We handle vehicle tag and title transactions at the shop. Call before your visit to find out what to bring.",
           "Sí. Tramitamos placas y títulos de vehículos en el taller. Llame antes de su visita para saber qué debe llevar.")),
        (t("What should I bring for a tag or title transaction?", "¿Qué debo llevar para un trámite de placas o título?"),
         t("Requirements depend on the transaction. When you call, ask which identification, documents, fees, and signer attendance apply.",
           "Los requisitos dependen del trámite. Cuando llame, pregunte qué identificación, documentos, tarifas y asistencia de firmantes aplican.")),
        (t("Is this the same as your notary service?", "¿Es lo mismo que su servicio de notario público?"),
         t("No. Notary service is a separate offering with its own hours, Monday–Friday, 8 a.m.–3 p.m. Tag and title work is a separate service, and you can ask for both when you call.",
           "No. El servicio de notario público es una oferta aparte con su propio horario, de lunes a viernes, de 8 a. m. a 3 p. m. Los trámites de placas y título son un servicio aparte, y puede pedir ambos cuando llame.")),
    ]},
    {"id": "ev", "title": t("Electric and hybrid vehicles", "Vehículos eléctricos e híbridos"), "items": [
        (t("Do you service electric and hybrid vehicles?", "¿Dan servicio a vehículos eléctricos e híbridos?"),
         t("Yes, except repairs on Tesla, Rivian, Lucid, Karma, and Polestar, which need factory software and high-voltage training. Call with your vehicle's year, make, and model to discuss the work you need.",
           "Sí, excepto reparaciones de Tesla, Rivian, Lucid, Karma y Polestar, que requieren software de fábrica y capacitación en alto voltaje. Llame con el año, la marca y el modelo de su vehículo para hablar del trabajo que necesita.")),
        (t("Are you certified for a particular electric vehicle brand?", "¿Están certificados para alguna marca de vehículos eléctricos?"),
         t("We do not claim manufacturer certification or brand-specialist status. Call to discuss the work your vehicle needs.",
           "No afirmamos tener certificación del fabricante ni especialidad en una marca. Llame para hablar del trabajo que necesita su vehículo.")),
        (t("Can my electric or hybrid vehicle have a state inspection?", "¿Puede mi vehículo eléctrico o híbrido pasar la inspección estatal?"),
         t("Inspection requirements differ by vehicle type. Call with your vehicle details and we'll tell you which inspection applies and set up a visit.",
           "Los requisitos de inspección difieren según el tipo de vehículo. Llame con los datos de su vehículo y le diremos qué inspección aplica y coordinaremos su visita.")),
    ]},
    {"id": "rotation", "title": t("Tire rotation & balancing", "Rotación y balanceo de llantas"), "items": [
        (t("Do you offer tire rotation and balancing?", "¿Ofrecen rotación y balanceo de llantas?"),
         t("Yes. We rotate and balance tires. Call for current pricing before you schedule.",
           "Sí. Rotamos y balanceamos llantas. Llame para conocer los precios actuales antes de programar.")),
        (t("How often should tires be rotated?", "¿Cada cuánto deben rotarse las llantas?"),
         t("Follow your vehicle manufacturer's recommendation. Intervals vary by vehicle, tire type, and driving conditions, so one fixed number does not fit every vehicle.",
           "Siga la recomendación del fabricante de su vehículo. Los intervalos varían según el vehículo, el tipo de llanta y las condiciones de manejo, por lo que un solo número fijo no sirve para todos.")),
        (t("Does balancing fix a vibration?", "¿El balanceo corrige una vibración?"),
         t("It can, but tire condition, alignment, and suspension problems can cause similar symptoms. Describe when the vibration happens so the cause can be assessed rather than assumed.",
           "Puede hacerlo, pero la condición de las llantas, la alineación y los problemas de suspensión pueden causar síntomas parecidos. Describa cuándo ocurre la vibración para que se evalúe la causa en lugar de suponerla.")),
    ]},
    {"id": "electrical", "title": t("Alternators & starters", "Alternadores y motores de arranque"), "items": [
        (t("Do you repair alternators and starters?", "¿Reparan alternadores y motores de arranque?"),
         t("Yes. We repair and replace alternators and starters. Call with your vehicle details to schedule.",
           "Sí. Reparamos y reemplazamos alternadores y motores de arranque. Llame con los datos de su vehículo para programar su cita.")),
        (t("What signs point to an alternator or starter problem?", "¿Qué señales apuntan a un problema del alternador o del arranque?"),
         t("A battery warning light, dim lights, a slow crank, or a click without the engine turning over can all be reported. A weak battery can cause similar signs, so the cause needs to be assessed.",
           "Una luz de advertencia de la batería, luces tenues, un arranque lento o un clic sin que gire el motor son señales que se pueden reportar. Una batería débil puede causar señales parecidas, por lo que hay que evaluar la causa.")),
        (t("My vehicle will not start. Can you help?", "Mi vehículo no arranca. ¿Pueden ayudarme?"),
         t("Yes. Call and describe what happens. We diagnose no-start problems, including battery, starter, alternator, and charging-system faults.",
           "Sí. Llame y describa lo que ocurre. Diagnosticamos fallas de arranque, incluidas fallas de la batería, del motor de arranque, del alternador y del sistema de carga.")),
    ]},
    {"id": "pickup", "title": t("Pickup, drop-off & after-hours", "Recogida, entrega y fuera de horario"), "items": [
        (t("Can I drop off my vehicle outside shop hours?", "¿Puedo dejar mi vehículo fuera del horario del taller?"),
         t("Yes. Call to arrange after-hours drop-off for your visit.",
           "Sí. Llame para coordinar la entrega fuera de horario para su visita.")),
        (t("Do you offer pickup or a ride nearby?", "¿Ofrecen recogida o transporte cercano?"),
         t("We offer pickup and drop-off. Call to arrange it for your visit.",
           "Ofrecemos recogida y entrega. Llame para coordinarlo para su visita.")),
        (t("How will I know when my vehicle is ready?", "¿Cómo sabré cuándo está listo mi vehículo?"),
         t("Tell the shop how you prefer to be contacted when you book. We do not publish a fixed completion time or a guaranteed notification method.",
           "Dígale al taller cómo prefiere que lo contacten cuando haga su cita. No publicamos un tiempo de entrega fijo ni un método de aviso garantizado.")),
    ]},
]

from more_services import NEW_ASK_SERVICES, NEW_ASK_FAQ_CATS, NEW_SVC_IMG  # noqa: E402
ASK_SERVICES.extend(NEW_ASK_SERVICES)
ASK_FAQ_CATS.extend(NEW_ASK_FAQ_CATS)

from confirmed_services import NEW_MAIN_SERVICES, NEW_MAIN_FAQ_CATS  # noqa: E402
SERVICES.extend(NEW_MAIN_SERVICES)
FAQ_CATS.extend(NEW_MAIN_FAQ_CATS)

SERVICES.extend(ASK_SERVICES)
GROUPS.append(ASK_GROUP)


# ---------------------------------------------------------------------------
# Illustrative images (AI-generated; alt text says so). file, width, height.
# ---------------------------------------------------------------------------
def _im(file, w, h, en, es):
    return {"file": file, "w": w, "h": h,
            "alt": t(en[0].upper() + en[1:], es[0].upper() + es[1:])}

IMAGES = {
    "svc-inspections": _im("svc-inspections.webp", 800, 603, "blueprint-style drawing of a vehicle inspection", "dibujo tipo plano de una inspección vehicular"),
    "svc-oil": _im("svc-oil.webp", 800, 603, "oil filter", "filtro de aceite"),
    "svc-brakes": _im("svc-brakes.webp", 800, 603, "brake rotor", "disco de freno"),
    "svc-tires": _im("svc-tires.webp", 800, 603, "tire", "neumático"),
    "svc-engine": _im("svc-engine.webp", 800, 603, "blueprint-style drawing of an engine", "dibujo tipo plano de un motor"),
    "svc-suspension": _im("svc-suspension.webp", 800, 603, "suspension strut", "amortiguador de la suspensión"),
    "svc-ac": _im("svc-ac.webp", 800, 603, "A/C compressor", "compresor del aire acondicionado"),
    "svc-fleet": _im("svc-fleet.webp", 800, 603, "white work van", "camioneta de trabajo blanca"),
    "svc-battery": _im("svc-battery.webp", 800, 603, "battery and alternator", "batería y alternador"),
    "svc-drivetrain": _im("svc-drivetrain.webp", 800, 603, "transmission and axle", "transmisión y eje"),
    "svc-tags": _im("svc-tags.webp", 800, 603, "blueprint-style drawing of a license plate, vehicle title, registration sticker and key", "dibujo tipo plano de una placa, un título de vehículo, una calcomanía de registro y una llave"),
    "svc-notary": _im("svc-notary.webp", 800, 603, "blueprint-style drawing of a notary embosser, pen, stamp and documents", "dibujo tipo plano de un sello notarial en relieve, una pluma, un sello y documentos"),
    "svc-ev": _im("svc-ev.webp", 800, 603, "blueprint-style drawing of an electric vehicle battery, motor and charge port", "dibujo tipo plano de la batería, el motor y el puerto de carga de un vehículo eléctrico"),
    "svc-prepurchase": _im("svc-prepurchase.webp", 800, 603, "blueprint-style drawing of a used car with its hood open, a flashlight and a checklist", "dibujo tipo plano de un auto usado con el capó abierto, una linterna y una lista de verificación"),
    "svc-bodywork": _im("svc-bodywork.webp", 800, 603, "blueprint-style drawing of a car door with dent repair tools and a spray gun", "dibujo tipo plano de la puerta de un auto con herramientas para reparar abolladuras y una pistola de pintura"),
    "svc-corrosion": _im("svc-corrosion.webp", 800, 603, "blueprint-style drawing of a car underbody with rust, rust-proofing spray and coating layers", "dibujo tipo plano de los bajos de un auto con óxido, rociado antióxido y capas de recubrimiento"),
    "svc-computer": _im("svc-computer.webp", 800, 603, "blueprint-style drawing of a car with a scan tool, engine computer and diagnostic port", "dibujo tipo plano de un auto con un escáner, la computadora del motor y el puerto de diagnóstico"),
    "svc-towing": _im("svc-towing.webp", 800, 603, "blueprint-style drawing of a flatbed tow truck carrying a car", "dibujo tipo plano de una grúa de plataforma que transporta un auto"),
    "svc-sparkplugs": _im("svc-sparkplugs.webp", 800, 603, "blueprint-style drawing of an engine with spark plugs and ignition coils", "dibujo tipo plano de un motor con bujías y bobinas de encendido"),
    "svc-emissioncontrol": _im("svc-emissioncontrol.webp", 800, 603, "blueprint-style drawing of an exhaust system with a catalytic converter and oxygen sensor", "dibujo tipo plano de un sistema de escape con convertidor catalítico y sensor de oxígeno"),
    "svc-fuelsys": _im("svc-fuelsys.webp", 800, 603, "blueprint-style drawing of a fuel tank, fuel pump, filter and injector", "dibujo tipo plano de un tanque de combustible, bomba, filtro e inyector"),
    "svc-heater": _im("svc-heater.webp", 800, 603, "blueprint-style drawing of a car heater core, blower motor and hoses", "dibujo tipo plano del núcleo del calefactor, el motor del ventilador y las mangueras de un auto"),
    "moto": _im("moto.webp", 1200, 671, "motorcycle", "motocicleta"),
    "about-storefront": _im("about-storefront.webp", 1000, 753, "Diverse Autoworks shop front at sunset, with state inspection and emission station signs", "fachada de Diverse Autoworks al atardecer, con letreros de estación de inspección y de emisiones del estado"),
    "home-storefront": _im("home-storefront.webp", 1376, 768, "Diverse Autoworks shop front at sunset, with state inspection and emission station signs", "fachada de Diverse Autoworks al atardecer, con letreros de estación de inspección y de emisiones del estado"),
    "about-interior": _im("about-interior.webp", 1200, 671, "repair shop interior", "interior de un taller"),
    "about-mechanic": _im("about-mechanic.webp", 1200, 671, "mechanic working on an SUV", "mecánico trabajando en una camioneta SUV"),
    "about-hands": _im("about-hands.webp", 800, 603, "hands using a torque wrench", "manos usando una llave de torque"),
}
# Services that reuse another service's image on /services/
SVC_IMG = {"inspections": "svc-inspections", "maintenance": "svc-oil", "engine": "svc-engine",
           "battery": "svc-battery", "drivetrain": "svc-drivetrain", "brakes": "svc-brakes",
           "tires": "svc-tires", "rotation": "svc-tires", "suspension": "svc-suspension",
           "ac": "svc-ac", "fleet": "svc-fleet", "electrical": "svc-battery"}
SVC_IMG.update(NEW_SVC_IMG)
SVC_IMG.update({"tags": "svc-tags", "notary": "svc-notary", "ev": "svc-ev", "prepurchase": "svc-prepurchase", "corrosion": "svc-corrosion", "computer": "svc-computer", "towing": "svc-towing", "sparkplugs": "svc-sparkplugs", "emissioncontrol": "svc-emissioncontrol", "fuelsys": "svc-fuelsys", "heater": "svc-heater"})
