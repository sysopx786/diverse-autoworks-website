# -*- coding: utf-8 -*-
"""
Additional "ask us about" services (Oct 8, 2026), from the owner checklist, Part B.

The owner confirmed all of these on Oct 30, 2026. They stay in the "More services"
group on /services/ and are worded as confirmed offerings.

Deduplicated against what the site already has:
  - tire rotation & balancing, alternators & starters -> already in ASK_SERVICES (content.py)
  - gas tank + fuel system repair                     -> one card (fuelsys)
  - differential + axles                              -> one card (diff); axle bearings/seals stay under Drivetrain
Each service gets its own FAQ category with 5 questions.
"""


def t(en, es):
    return {"en": en, "es": es}


# Three questions are shared in shape; the rest are written per service.
def _q_offer(en_ref, es_ref):
    return (t(f"Do you offer {en_ref}?", f"¿Ofrecen {es_ref}?"),
            t(f"Yes. We offer {en_ref}. Call with your vehicle's year, make, and model to schedule.",
              f"Sí. Ofrecemos {es_ref}. Llame con el año, la marca y el modelo de su vehículo para programar su cita."))


def _q_tell(en_ref, es_ref):
    return (t(f"What should I tell the shop when I ask about {en_ref}?", f"¿Qué debo decirle al taller cuando pregunte por {es_ref}?"),
            t("Give your vehicle's year, make, and model, what you have noticed, when it happens, and whether a warning light is on. This helps the shop answer your question; it does not replace an assessment of the vehicle.",
              "Indique el año, la marca y el modelo de su vehículo, lo que ha notado, cuándo ocurre y si hay una luz de advertencia encendida. Esto ayuda al taller a responder su pregunta; no reemplaza la evaluación del vehículo."))


def _q_price(en_ref, es_de):
    return (t(f"What is the price and timing for {en_ref}?", f"¿Cuál es el precio y el tiempo {es_de}?"),
            t("Please call for current pricing and timing for your vehicle. We do not publish fixed prices or completion-time guarantees for this work.",
              "Llame para conocer el precio y el tiempo actuales para su vehículo. No publicamos precios fijos ni garantías de tiempo de entrega para este trabajo."))


def _svc(sid, icon, title, card, line, desc, faq_title, en_ref, es_ref, es_de, q2, q5):
    svc = {"id": sid, "icon": icon, "title": title, "card": card, "line": line, "desc": desc,
           "faq": sid, "group": "ask"}
    faq = {"id": sid, "title": faq_title, "items": [
        _q_offer(en_ref, es_ref), q2, _q_tell(en_ref, es_ref), _q_price(en_ref, es_de), q5]}
    return svc, faq


_ITEMS = [
    # ---------------------------------------------------------------- towing
    _svc("towing", "van",
         t("Towing", "Servicio de remolque"),
         t("Towing", "Remolque"),
         t("Towing for vehicles that can't be driven.", "Remolque para vehículos que no se pueden manejar."),
         t("If your vehicle cannot be driven, we can arrange or accept a tow for your visit. Call to set it up.",
           "Si su vehículo no se puede manejar, podemos coordinar o recibir un remolque para su visita. Llame para organizarlo."),
         t("Towing", "Servicio de remolque"),
         "towing", "el servicio de remolque", "del servicio de remolque",
         (t("What should I do if my vehicle cannot be driven?", "¿Qué debo hacer si mi vehículo no se puede manejar?"),
          t("If it is unsafe to move, get to a safe place and call for roadside help first. Then call the shop to arrange a tow.",
            "Si no es seguro moverlo, póngase en un lugar seguro y pida ayuda en carretera primero. Luego llame al taller para coordinar el remolque.")),
         (t("Is towing the same as roadside assistance?", "¿El remolque es lo mismo que la asistencia en carretera?"),
          t("No. Roadside assistance, such as jump starts or lockouts, is a separate service, and this site does not list it. Ask the shop what it can arrange.",
            "No. La asistencia en carretera, como el paso de corriente o la apertura de puertas, es un servicio aparte y este sitio no lo anuncia. Pregunte al taller qué puede coordinar."))),

    # ------------------------------------------------- pre-purchase inspection
    _svc("prepurchase", "inspection",
         t("Pre-purchase inspections", "Inspecciones previas a la compra"),
         t("Pre-Purchase Inspections", "Inspección previa a la compra"),
         t("Inspections before you buy a used vehicle.", "Inspecciones antes de comprar un vehículo usado."),
         t("Thinking about buying a used vehicle? We inspect it before you buy. Call to ask what the inspection covers.",
           "¿Piensa comprar un vehículo usado? Lo inspeccionamos antes de que lo compre. Llame para preguntar qué cubre la inspección."),
         t("Pre-purchase inspections", "Inspecciones previas a la compra"),
         "pre-purchase inspections", "las inspecciones previas a la compra", "de las inspecciones previas a la compra",
         (t("What does a pre-purchase inspection look at?", "¿Qué revisa una inspección previa a la compra?"),
          t("The scope is set by the shop for each vehicle. Before you book, ask what the inspection covers and whether it includes a road test.",
            "El alcance lo define el taller para cada vehículo. Antes de reservar, pregunte qué cubre la inspección y si incluye una prueba de manejo.")),
         (t("Is a pre-purchase inspection the same as a state inspection?", "¿Una inspección previa a la compra es lo mismo que una inspección estatal?"),
          t("No. A Pennsylvania state inspection checks required safety and emissions items. A pre-purchase inspection is a buyer's check of a used vehicle's condition. Call to ask which one you need.",
            "No. La inspección estatal de Pensilvania revisa los elementos de seguridad y emisiones requeridos. Una inspección previa a la compra es una revisión del estado de un vehículo usado para el comprador. Llame para preguntar cuál necesita."))),

    # ------------------------------------------------------------ gas tanks
    _svc("fuelsys", "engine",
         t("Gas tank service", "Servicio de tanque de combustible"),
         t("Gas Tanks", "Tanques de combustible"),
         t("Gas tank service and repair.", "Servicio y reparación de tanques de combustible."),
         t("We service and repair gas tanks. Call with your vehicle details to schedule.",
           "Damos servicio y reparamos tanques de combustible. Llame con los datos de su vehículo para programar su cita."),
         t("Gas tank service", "Servicio de tanque de combustible"),
         "gas tank service", "el servicio de tanque de combustible", "del servicio de tanque de combustible",
         (t("What signs point to a gas tank problem?", "¿Qué señales indican un problema del tanque de combustible?"),
          t("A strong fuel smell, a visible leak, or a damaged fuel cap can be reported. A strong fuel smell or a visible leak is a safety concern: do not drive the vehicle, and call for help.",
            "Un olor fuerte a combustible, una fuga visible o un tapón dañado pueden reportarse. Un olor fuerte a combustible o una fuga visible es un riesgo de seguridad: no maneje el vehículo y llame para pedir ayuda.")),
         (t("Do fuel pumps and fuel lines belong here?", "¿Las bombas y las líneas de combustible van aquí?"),
          t("No. Fuel pumps, fuel lines, and fuel injectors are part of our engine repair work. See Engine analysis, repair & tune-ups.",
            "No. Las bombas, las líneas y los inyectores de combustible forman parte de nuestro trabajo de reparación del motor. Vea Análisis, reparación y afinación del motor."))),

    # ------------------------------------------------------------ differential
    _svc("differential", "gear",
         t("Differential repair", "Reparación del diferencial"),
         t("Differential Repair", "Diferencial"),
         t("Differential and related axle repair.", "Reparación del diferencial y de los ejes."),
         t("We repair differentials and do related axle work. Call with your vehicle details to schedule.",
           "Reparamos diferenciales y hacemos trabajos relacionados con los ejes. Llame con los datos de su vehículo para programar su cita."),
         t("Differential repair", "Reparación del diferencial"),
         "differential repair", "la reparación del diferencial", "de la reparación del diferencial",
         (t("What signs are linked to differential problems?", "¿Qué señales se relacionan con problemas del diferencial?"),
          t("Whining or howling that changes with speed, clunking in turns, or fluid leaks near the axle can be reported. Other drivetrain parts cause similar signs, so the cause needs to be assessed.",
            "Se pueden reportar zumbidos o aullidos que cambian con la velocidad, golpeteos en las curvas o fugas de líquido cerca del eje. Otras piezas del tren motriz causan señales parecidas, por lo que hay que evaluar la causa.")),
         (t("How is this different from drivetrain maintenance?", "¿En qué se diferencia del mantenimiento del tren motriz?"),
          t("Drivetrain maintenance covers transmission maintenance and rear-axle bearing and seal service. Differential repair is a separate repair, and we do it too.",
            "El mantenimiento del tren motriz incluye el mantenimiento de transmisión y el servicio de cojinetes y sellos del eje trasero. La reparación del diferencial es un trabajo aparte, y también lo hacemos."))),

    # -------------------------------------------------------------- heater
    _svc("heater", "engine",
         t("Heater service & repair", "Servicio y reparación de la calefacción"),
         t("Heater Service", "Calefacción"),
         t("Heater service and repair.", "Servicio y reparación de la calefacción."),
         t("We service and repair vehicle heaters. Call if your vehicle is not producing heat.",
           "Damos servicio y reparamos la calefacción del vehículo. Llame si su vehículo no calienta."),
         t("Heater service & repair", "Servicio y reparación de la calefacción"),
         "heater service and repair", "el servicio y la reparación de la calefacción", "del servicio y la reparación de la calefacción",
         (t("What signs point to a heater problem?", "¿Qué señales apuntan a un problema de la calefacción?"),
          t("No heat, weak airflow, a sweet smell, or fogging windows can be reported. A low coolant level or a cooling-system fault can also cause no heat, so the system needs to be assessed.",
            "Se pueden reportar falta de calor, poco flujo de aire, un olor dulce o vidrios empañados. Un nivel bajo de refrigerante o una falla del sistema de enfriamiento también pueden causar falta de calor, por lo que hay que evaluar el sistema.")),
         (t("Is heater service the same as A/C service?", "¿El servicio de calefacción es lo mismo que el de A/C?"),
          t("They share parts of the climate system but are different services. We do both, along with cooling-system service.",
            "Comparten partes del sistema de climatización, pero son servicios distintos. Hacemos ambos, además del servicio del sistema de enfriamiento."))),

    # ------------------------------------------------------------ corrosion
    _svc("corrosion", "gear",
         t("Corrosion & rust control", "Control de corrosión y óxido"),
         t("Corrosion Control", "Control de corrosión"),
         t("Rust assessment and corrosion treatment.", "Evaluación del óxido y tratamiento de la corrosión."),
         t("Road salt and winter weather can cause rust on a vehicle's underside and parts. We assess and treat corrosion. Call to schedule.",
           "La sal de las carreteras y el clima invernal pueden causar óxido en la parte inferior y en las piezas del vehículo. Evaluamos y tratamos la corrosión. Llame para programar su cita."),
         t("Corrosion & rust control", "Control de corrosión y óxido"),
         "corrosion and rust control", "el control de corrosión y óxido", "del control de corrosión y óxido",
         (t("Which parts of a vehicle can be affected by rust?", "¿Qué partes de un vehículo pueden afectarse por el óxido?"),
          t("Brake lines, the frame, the exhaust, suspension parts, and body panels are common areas. We can assess these areas on your vehicle.",
            "Las líneas de frenos, el chasis, el escape, las piezas de suspensión y los paneles de la carrocería son zonas comunes. Podemos evaluar estas zonas en su vehículo.")),
         (t("Can rust affect a state inspection?", "¿Puede el óxido afectar una inspección estatal?"),
          t("Rust or corrosion on safety-related parts can affect an inspection result. Call the shop to ask how it applies to your vehicle.",
            "El óxido o la corrosión en piezas relacionadas con la seguridad pueden afectar el resultado de una inspección. Llame al taller para preguntar cómo aplica a su vehículo."))),

    # ---------------------------------------------------------------- wheels
    _svc("wheels", "tire",
         t("Wheels & wheel replacement", "Ruedas y reemplazo de ruedas"),
         t("Wheels & Replacement", "Ruedas y reemplazo"),
         t("Wheel (rim) repair and replacement.", "Reparación y reemplazo de ruedas (rines)."),
         t("We repair and replace damaged or worn wheels (rims), along with tires, tire repairs, and wheel alignments.",
           "Reparamos y reemplazamos ruedas (rines) dañadas o desgastadas, además de llantas, reparación de llantas y alineación de ruedas."),
         t("Wheels & wheel replacement", "Ruedas y reemplazo de ruedas"),
         "wheel repair and replacement", "la reparación y el reemplazo de ruedas", "de la reparación y el reemplazo de ruedas",
         (t("What signs point to a damaged wheel?", "¿Qué señales apuntan a una rueda dañada?"),
          t("Vibration, a bent or cracked rim, or a slow air leak can be reported. Tire and balance problems cause similar signs, so the cause needs to be assessed.",
            "Se pueden reportar vibración, un rin doblado o agrietado o una fuga lenta de aire. Los problemas de llantas y de balanceo causan señales parecidas, por lo que hay que evaluar la causa.")),
         (t("Is wheel replacement the same as tire replacement?", "¿El reemplazo de ruedas es lo mismo que el de llantas?"),
          t("No. Tire replacement swaps the tire. Wheel replacement swaps the wheel (rim) itself. We do both.",
            "No. El reemplazo de llantas cambia la llanta. El reemplazo de ruedas cambia la rueda (rin) como tal. Hacemos ambos."))),

    # --------------------------------------------------------------- retreads
    _svc("retreads", "tire",
         t("Tire retreads", "Llantas renovadas (reencauchadas)"),
         t("Tire Retreads", "Llantas renovadas"),
         t("Retreaded tires.", "Llantas renovadas."),
         t("A retread puts new tread on a worn tire's casing. We offer retreads. Call with your vehicle details.",
           "Una llanta renovada, también llamada reencauchada, lleva banda de rodadura nueva sobre la carcasa de una llanta desgastada. Ofrecemos llantas renovadas. Llame con los datos de su vehículo."),
         t("Tire retreads", "Llantas renovadas (reencauchadas)"),
         "tire retreads", "las llantas renovadas", "de las llantas renovadas",
         (t("What is a retread tire?", "¿Qué es una llanta renovada o reencauchada?"),
          t("A retread reuses the casing of a worn tire and adds new tread. Whether a tire can be retreaded depends on its condition and type, so ask the shop.",
            "Una llanta renovada reutiliza la carcasa de una llanta desgastada y le agrega banda de rodadura nueva. Que una llanta pueda renovarse depende de su estado y tipo, así que pregunte al taller.")),
         (t("Are retreads right for every vehicle?", "¿Las llantas renovadas son adecuadas para todos los vehículos?"),
          t("Not necessarily. Ask the shop and check your vehicle manufacturer's guidance before choosing a retread.",
            "No necesariamente. Pregunte al taller y consulte la guía del fabricante de su vehículo antes de elegir una llanta renovada."))),

    # ------------------------------------------------------------ ball joints
    _svc("balljoints", "spring",
         t("Ball joints", "Rótulas"),
         t("Ball Joints", "Rótulas"),
         t("Ball joint inspection and replacement.", "Revisión y reemplazo de rótulas."),
         t("We inspect and replace ball joints, along with other steering and suspension parts, shocks, and struts.",
           "Revisamos y reemplazamos rótulas, además de otras piezas de dirección y suspensión, amortiguadores y puntales."),
         t("Ball joints", "Rótulas"),
         "ball joint service", "el servicio de rótulas", "del servicio de rótulas",
         (t("What signs point to worn ball joints?", "¿Qué señales apuntan a rótulas desgastadas?"),
          t("Clunking over bumps, loose or wandering steering, or uneven tire wear can be reported. Other suspension parts cause similar signs, so the cause needs to be assessed.",
            "Se pueden reportar golpeteos en los baches, dirección floja o que se desvía, o desgaste desigual de las llantas. Otras piezas de la suspensión causan señales parecidas, por lo que hay que evaluar la causa.")),
         (t("Are ball joints part of steering and suspension service?", "¿Las rótulas forman parte del servicio de dirección y suspensión?"),
          t("Yes. Ball joints are part of our steering and suspension work, along with shocks and struts.",
            "Sí. Las rótulas forman parte de nuestro trabajo de dirección y suspensión, junto con los amortiguadores y los puntales."))),
]

NEW_ASK_SERVICES = [s for s, _ in _ITEMS]
NEW_ASK_FAQ_CATS = [f for _, f in _ITEMS]

# Reuse existing illustrations where one fits (others show no image, like tags/EV/pickup).
NEW_SVC_IMG = {"prepurchase": "svc-inspections", "emissioncontrol": "svc-inspections",
               "headblock": "svc-engine", "fuelsys": "svc-engine", "sparkplugs": "svc-engine",
               "computer": "svc-engine", "differential": "svc-drivetrain", "heater": "svc-ac",
               "wheels": "svc-tires", "retreads": "svc-tires", "balljoints": "svc-suspension"}
