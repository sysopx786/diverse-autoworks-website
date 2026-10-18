# -*- coding: utf-8 -*-
"""
Additional "ask us about" services (Oct 8, 2026), from the owner checklist, Part B.

These are NOT confirmed offerings. Every card and FAQ is worded "call to confirm",
the same way tags/title, EV/hybrid, tire rotation and alternators already are.
When the owner marks a service Yes, move it out of this file into SERVICES with
confirmed wording.

Deduplicated against what the site already has:
  - tire rotation & balancing, alternators & starters -> already in ASK_SERVICES (content.py)
  - gas tank + fuel system repair                     -> one card (fuelsys)
  - differential + axles                              -> one card (diff); axle bearings/seals stay under Drivetrain
  - body work                                         -> one card (bodywork); replaces the old FAQ_GENERAL bodywork item
Each service gets its own FAQ category with 5 questions.
"""


def t(en, es):
    return {"en": en, "es": es}


# Three questions are shared in shape; the rest are written per service.
def _q_offer(en_ref, es_ref):
    return (t(f"Do you offer {en_ref}?", f"¿Ofrecen {es_ref}?"),
            t(f"Call to ask whether the shop can help with {en_ref} for your vehicle. It is not listed as a confirmed service on this site, and availability is confirmed vehicle by vehicle.",
              f"Llame para preguntar si el taller puede ayudarle con {es_ref} para su vehículo. No figura como servicio confirmado en este sitio, y la disponibilidad se confirma vehículo por vehículo."))


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


_DISCLAIM_EN = " We do not list this as a confirmed service on this site."
_DISCLAIM_ES = " No lo anunciamos como servicio confirmado en este sitio."

_ITEMS = [
    # ---------------------------------------------------------------- towing
    _svc("towing", "van",
         t("Towing", "Servicio de remolque"),
         t("Towing", "Remolque"),
         t("Ask about towing.", "Pregunte por el servicio de remolque."),
         t("If your vehicle cannot be driven, call to ask whether the shop can arrange or accept a tow for your visit." + _DISCLAIM_EN,
           "Si su vehículo no se puede manejar, llame para preguntar si el taller puede coordinar o recibir un remolque para su visita." + _DISCLAIM_ES),
         t("Towing", "Servicio de remolque"),
         "towing", "el servicio de remolque", "del servicio de remolque",
         (t("What should I do if my vehicle cannot be driven?", "¿Qué debo hacer si mi vehículo no se puede manejar?"),
          t("If it is unsafe to move, get to a safe place and call for roadside help first. Then call the shop to ask whether it can arrange or accept a tow and what it can look at on arrival.",
            "Si no es seguro moverlo, póngase en un lugar seguro y pida ayuda en carretera primero. Luego llame al taller para preguntar si puede coordinar o recibir un remolque y qué puede revisar a su llegada.")),
         (t("Is towing the same as roadside assistance?", "¿El remolque es lo mismo que la asistencia en carretera?"),
          t("No. Roadside assistance, such as jump starts or lockouts, is a separate service, and this site does not list it. Ask the shop what it can arrange.",
            "No. La asistencia en carretera, como el paso de corriente o la apertura de puertas, es un servicio aparte y este sitio no lo anuncia. Pregunte al taller qué puede coordinar."))),

    # ------------------------------------------------- pre-purchase inspection
    _svc("prepurchase", "inspection",
         t("Pre-purchase inspections", "Inspecciones previas a la compra"),
         t("Pre-Purchase Inspections", "Inspección previa a la compra"),
         t("Ask about pre-purchase inspections.", "Pregunte por inspecciones previas a la compra."),
         t("Thinking about buying a used vehicle? Call to ask whether the shop can inspect it before you buy, and what the inspection would cover." + _DISCLAIM_EN,
           "¿Piensa comprar un vehículo usado? Llame para preguntar si el taller puede inspeccionarlo antes de comprarlo y qué cubriría la inspección." + _DISCLAIM_ES),
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
         t("Ask about gas tank service.", "Pregunte por el servicio de tanque de combustible."),
         t("Gas tank repair is not listed on this site. Call to ask what the shop can handle for your vehicle." + _DISCLAIM_EN,
           "La reparación del tanque de combustible no figura en este sitio. Llame para preguntar qué puede realizar el taller en su vehículo." + _DISCLAIM_ES),
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
         t("Ask about differential repair.", "Pregunte por la reparación del diferencial."),
         t("Differential repair is not listed on this site. Call with your vehicle details to ask whether the shop can service differentials and related axle work." + _DISCLAIM_EN,
           "La reparación del diferencial no figura en este sitio. Llame con los datos de su vehículo para preguntar si el taller puede dar servicio a diferenciales y trabajos relacionados con los ejes." + _DISCLAIM_ES),
         t("Differential repair", "Reparación del diferencial"),
         "differential repair", "la reparación del diferencial", "de la reparación del diferencial",
         (t("What signs are linked to differential problems?", "¿Qué señales se relacionan con problemas del diferencial?"),
          t("Whining or howling that changes with speed, clunking in turns, or fluid leaks near the axle can be reported. Other drivetrain parts cause similar signs, so the cause needs to be assessed.",
            "Se pueden reportar zumbidos o aullidos que cambian con la velocidad, golpeteos en las curvas o fugas de líquido cerca del eje. Otras piezas del tren motriz causan señales parecidas, por lo que hay que evaluar la causa.")),
         (t("How is this different from drivetrain maintenance?", "¿En qué se diferencia del mantenimiento del tren motriz?"),
          t("Listed drivetrain work is transmission maintenance and rear-axle bearing and seal service. Differential repair is not listed; call to confirm.",
            "El trabajo del tren motriz anunciado es el mantenimiento de transmisión y el servicio de cojinetes y sellos del eje trasero. La reparación del diferencial no figura; llame para confirmar."))),

    # -------------------------------------------------------------- heater
    _svc("heater", "engine",
         t("Heater service & repair", "Servicio y reparación de la calefacción"),
         t("Heater Service", "Calefacción"),
         t("Ask about heater service and repair.", "Pregunte por servicio y reparación de la calefacción."),
         t("A/C and cooling-system service are listed on this site. Heater service and repair are not. Call to ask whether the shop can help if your vehicle is not producing heat." + _DISCLAIM_EN,
           "El servicio de A/C y del sistema de enfriamiento figuran en este sitio. El servicio y la reparación de la calefacción no. Llame para preguntar si el taller puede ayudarle si su vehículo no calienta." + _DISCLAIM_ES),
         t("Heater service & repair", "Servicio y reparación de la calefacción"),
         "heater service and repair", "el servicio y la reparación de la calefacción", "del servicio y la reparación de la calefacción",
         (t("What signs point to a heater problem?", "¿Qué señales apuntan a un problema de la calefacción?"),
          t("No heat, weak airflow, a sweet smell, or fogging windows can be reported. A low coolant level or a cooling-system fault can also cause no heat, so the system needs to be assessed.",
            "Se pueden reportar falta de calor, poco flujo de aire, un olor dulce o vidrios empañados. Un nivel bajo de refrigerante o una falla del sistema de enfriamiento también pueden causar falta de calor, por lo que hay que evaluar el sistema.")),
         (t("Is heater service the same as A/C service?", "¿El servicio de calefacción es lo mismo que el de A/C?"),
          t("They share parts of the climate system but are different services. A/C and cooling-system service are listed; heater repair is not, so call to confirm.",
            "Comparten partes del sistema de climatización, pero son servicios distintos. El servicio de A/C y del sistema de enfriamiento figuran; la reparación de la calefacción no, así que llame para confirmar."))),

    # ------------------------------------------------------------ corrosion
    _svc("corrosion", "gear",
         t("Corrosion & rust control", "Control de corrosión y óxido"),
         t("Corrosion Control", "Control de corrosión"),
         t("Ask about corrosion and rust control.", "Pregunte por el control de corrosión y óxido."),
         t("Road salt and winter weather can cause rust on a vehicle's underside and parts. Call to ask whether the shop can assess or treat corrosion on your vehicle." + _DISCLAIM_EN,
           "La sal de las carreteras y el clima invernal pueden causar óxido en la parte inferior y en las piezas del vehículo. Llame para preguntar si el taller puede evaluar o tratar la corrosión en su vehículo." + _DISCLAIM_ES),
         t("Corrosion & rust control", "Control de corrosión y óxido"),
         "corrosion and rust control", "el control de corrosión y óxido", "del control de corrosión y óxido",
         (t("Which parts of a vehicle can be affected by rust?", "¿Qué partes de un vehículo pueden afectarse por el óxido?"),
          t("Brake lines, the frame, the exhaust, suspension parts, and body panels are common areas. Ask the shop which of these it can assess on your vehicle.",
            "Las líneas de frenos, el chasis, el escape, las piezas de suspensión y los paneles de la carrocería son zonas comunes. Pregunte al taller cuáles de ellas puede evaluar en su vehículo.")),
         (t("Can rust affect a state inspection?", "¿Puede el óxido afectar una inspección estatal?"),
          t("Rust or corrosion on safety-related parts can affect an inspection result. Call the shop to ask how it applies to your vehicle.",
            "El óxido o la corrosión en piezas relacionadas con la seguridad pueden afectar el resultado de una inspección. Llame al taller para preguntar cómo aplica a su vehículo."))),

    # ---------------------------------------------------------------- wheels
    _svc("wheels", "tire",
         t("Wheels & wheel replacement", "Ruedas y reemplazo de ruedas"),
         t("Wheels & Replacement", "Ruedas y reemplazo"),
         t("Ask about wheel repair and replacement.", "Pregunte por reparación y reemplazo de ruedas."),
         t("Tires, tire repairs, and wheel alignments are listed. Wheel (rim) repair and replacement are not. Call to ask whether the shop can help with a damaged or worn wheel." + _DISCLAIM_EN,
           "Las llantas, su reparación y la alineación de ruedas figuran en el sitio. La reparación y el reemplazo de ruedas (rines) no. Llame para preguntar si el taller puede ayudarle con una rueda dañada o desgastada." + _DISCLAIM_ES),
         t("Wheels & wheel replacement", "Ruedas y reemplazo de ruedas"),
         "wheel repair and replacement", "la reparación y el reemplazo de ruedas", "de la reparación y el reemplazo de ruedas",
         (t("What signs point to a damaged wheel?", "¿Qué señales apuntan a una rueda dañada?"),
          t("Vibration, a bent or cracked rim, or a slow air leak can be reported. Tire and balance problems cause similar signs, so the cause needs to be assessed.",
            "Se pueden reportar vibración, un rin doblado o agrietado o una fuga lenta de aire. Los problemas de llantas y de balanceo causan señales parecidas, por lo que hay que evaluar la causa.")),
         (t("Is wheel replacement the same as tire replacement?", "¿El reemplazo de ruedas es lo mismo que el de llantas?"),
          t("No. Tires and tire repairs are listed services. Replacing the wheel (rim) itself is not listed; call to confirm.",
            "No. Las llantas y su reparación son servicios anunciados. El reemplazo de la rueda (rin) como tal no figura; llame para confirmar."))),

    # --------------------------------------------------------------- retreads
    _svc("retreads", "tire",
         t("Tire retreads", "Llantas renovadas (reencauchadas)"),
         t("Tire Retreads", "Llantas renovadas"),
         t("Ask about tire retreads.", "Pregunte por llantas renovadas."),
         t("A retread puts new tread on a worn tire's casing. Call to ask whether the shop offers or can arrange retreads for your vehicle." + _DISCLAIM_EN,
           "Una llanta renovada, también llamada reencauchada, lleva banda de rodadura nueva sobre la carcasa de una llanta desgastada. Llame para preguntar si el taller ofrece o puede coordinar llantas renovadas para su vehículo." + _DISCLAIM_ES),
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
         t("Ask about ball joint replacement.", "Pregunte por el reemplazo de rótulas."),
         t("Steering parts, suspension parts, shocks, and struts are listed. Ball joints are not named separately. Call to ask whether the shop can inspect or replace ball joints on your vehicle." + _DISCLAIM_EN,
           "Las piezas de dirección y suspensión, los amortiguadores y los puntales figuran en el sitio. Las rótulas no se nombran por separado. Llame para preguntar si el taller puede revisar o reemplazar las rótulas de su vehículo." + _DISCLAIM_ES),
         t("Ball joints", "Rótulas"),
         "ball joint service", "el servicio de rótulas", "del servicio de rótulas",
         (t("What signs point to worn ball joints?", "¿Qué señales apuntan a rótulas desgastadas?"),
          t("Clunking over bumps, loose or wandering steering, or uneven tire wear can be reported. Other suspension parts cause similar signs, so the cause needs to be assessed.",
            "Se pueden reportar golpeteos en los baches, dirección floja o que se desvía, o desgaste desigual de las llantas. Otras piezas de la suspensión causan señales parecidas, por lo que hay que evaluar la causa.")),
         (t("Are ball joints part of steering and suspension service?", "¿Las rótulas forman parte del servicio de dirección y suspensión?"),
          t("Steering parts, suspension parts, shocks, and struts are listed. Ball joints are not named separately, so call to confirm.",
            "Las piezas de dirección y suspensión, los amortiguadores y los puntales figuran. Las rótulas no se nombran por separado, así que llame para confirmar."))),

    # ---------------------------------------------------------------- body work
    _svc("bodywork", "van",
         t("Body work", "Carrocería"),
         t("Body Work", "Carrocería"),
         t("Ask about body work.", "Pregunte por trabajos de carrocería."),
         t("Our published services focus on mechanical repair and maintenance. Call to ask about dents, panels, paint, or collision-related work." + _DISCLAIM_EN,
           "Nuestros servicios publicados se centran en la reparación mecánica y el mantenimiento. Llame para preguntar por abolladuras, paneles, pintura o trabajos relacionados con colisiones." + _DISCLAIM_ES),
         t("Body work", "Carrocería"),
         "body work", "los trabajos de carrocería", "de los trabajos de carrocería",
         (t("Do you do dent repair, painting, or collision repair?", "¿Hacen reparación de abolladuras, pintura o reparación por colisión?"),
          t("Not listed. Our published services focus on mechanical repair and maintenance. Contact the shop about any bodywork or collision-related request.",
            "No figura. Nuestros servicios publicados se centran en la reparación mecánica y el mantenimiento. Comuníquese con el taller si tiene alguna solicitud de carrocería o relacionada con colisiones.")),
         (t("Do you work with insurance claims?", "¿Trabajan con reclamos de seguro?"),
          t("Insurance-claim work is not specified in our published information. Ask the shop before assuming a claim can be handled.",
            "El trabajo con reclamos de seguro no está especificado en nuestra información publicada. Pregunte al taller antes de dar por hecho que se puede atender un reclamo."))),
]

NEW_ASK_SERVICES = [s for s, _ in _ITEMS]
NEW_ASK_FAQ_CATS = [f for _, f in _ITEMS]

# Reuse existing illustrations where one fits (others show no image, like tags/EV/pickup).
NEW_SVC_IMG = {"prepurchase": "svc-inspections", "emissioncontrol": "svc-inspections",
               "headblock": "svc-engine", "fuelsys": "svc-engine", "sparkplugs": "svc-engine",
               "computer": "svc-engine", "differential": "svc-drivetrain", "heater": "svc-ac",
               "wheels": "svc-tires", "retreads": "svc-tires", "balljoints": "svc-suspension"}
