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

    # -------------------------------------------------- cylinder head & block
    _svc("headblock", "engine",
         t("Cylinder head & block repair", "Reparación de culata y bloque del motor"),
         t("Cylinder Head & Block", "Culata y bloque"),
         t("Ask about cylinder head and block repair.", "Pregunte por reparación de culata y bloque."),
         t("Engine work beyond analysis and tune-ups, such as cylinder head and engine block repair, is not listed on this site. Call with your vehicle details to ask whether the shop can take it on." + _DISCLAIM_EN,
           "El trabajo del motor más allá del análisis y las afinaciones, como la reparación de la culata y del bloque del motor, no figura en este sitio. Llame con los datos de su vehículo para preguntar si el taller puede realizarlo." + _DISCLAIM_ES),
         t("Cylinder head & block repair", "Reparación de culata y bloque del motor"),
         "cylinder head and block repair", "la reparación de la culata y el bloque del motor", "de la reparación de la culata y el bloque del motor",
         (t("What problems are linked to cylinder head or block damage?", "¿Qué problemas se relacionan con daños en la culata o el bloque?"),
          t("Overheating, coolant loss, white exhaust smoke, or oil and coolant mixing can be reported. Other problems cause similar signs, so a diagnosis is needed before assuming head or block damage.",
            "Se pueden reportar sobrecalentamiento, pérdida de refrigerante, humo blanco en el escape o mezcla de aceite y refrigerante. Otros problemas causan señales parecidas, por lo que se necesita un diagnóstico antes de suponer daño en la culata o el bloque.")),
         (t("Is this the same as engine analysis or a tune-up?", "¿Es lo mismo que un análisis del motor o una afinación?"),
          t("No. Engine analysis and tune-ups are listed services. Head and block work is a separate, larger repair. Ask the shop whether it is available for your vehicle.",
            "No. El análisis del motor y las afinaciones son servicios anunciados. El trabajo de culata y bloque es una reparación aparte y de mayor alcance. Pregunte al taller si está disponible para su vehículo."))),

    # ---------------------------------------------------- fuel system & tanks
    _svc("fuelsys", "engine",
         t("Fuel system & gas tank service", "Servicio del sistema de combustible y tanque"),
         t("Fuel System & Gas Tanks", "Combustible y tanque"),
         t("Ask about fuel system and gas tank service.", "Pregunte por el sistema de combustible y el tanque."),
         t("Fuel filters and fuel-injector cleaning are listed on this site. For other fuel-system service or repair, including gas tanks, call to ask what the shop can handle for your vehicle." + _DISCLAIM_EN,
           "Los filtros de combustible y la limpieza de inyectores figuran en este sitio. Para otro servicio o reparación del sistema de combustible, incluido el tanque, llame para preguntar qué puede realizar el taller en su vehículo." + _DISCLAIM_ES),
         t("Fuel system & gas tank service", "Servicio del sistema de combustible y tanque"),
         "fuel system and gas tank service", "el servicio del sistema de combustible y del tanque", "del servicio del sistema de combustible y del tanque",
         (t("What signs point to a fuel-system problem?", "¿Qué señales apuntan a un problema del sistema de combustible?"),
          t("Hard starting, stalling, rough running, or lower mileage can be reported. Several systems cause similar signs, so the cause needs to be assessed. A strong fuel smell or a visible leak is a safety concern: do not drive the vehicle, and call for help.",
            "Se pueden reportar dificultad para arrancar, apagones del motor, funcionamiento irregular o menor rendimiento. Varios sistemas causan señales parecidas, por lo que hay que evaluar la causa. Un olor fuerte a combustible o una fuga visible es un riesgo de seguridad: no maneje el vehículo y pida ayuda.")),
         (t("Which fuel services are listed on this site today?", "¿Qué servicios de combustible figuran hoy en este sitio?"),
          t("Fuel filters and fuel-injector cleaning. Fuel pumps, fuel lines, and gas tanks are not listed, so call to ask.",
            "Los filtros de combustible y la limpieza de inyectores. Las bombas de combustible, las líneas de combustible y los tanques no figuran, así que llame para preguntar."))),

    # ------------------------------------------------------------ spark plugs
    _svc("sparkplugs", "engine",
         t("Spark plugs", "Bujías"),
         t("Spark Plugs", "Bujías"),
         t("Ask about spark plug service.", "Pregunte por el servicio de bujías."),
         t("Spark plug replacement is not itemized on this site. Call to ask whether the shop can service spark plugs on its own or as part of a tune-up for your vehicle." + _DISCLAIM_EN,
           "El cambio de bujías no está detallado en este sitio. Llame para preguntar si el taller puede dar servicio a las bujías por separado o como parte de una afinación para su vehículo." + _DISCLAIM_ES),
         t("Spark plugs", "Bujías"),
         "spark plug service", "el servicio de bujías", "del servicio de bujías",
         (t("How do I know whether spark plugs need attention?", "¿Cómo sé si las bujías necesitan atención?"),
          t("Misfires, rough idle, hard starting, or lower mileage can be linked to spark plugs, but other causes exist. Follow your manufacturer's recommended replacement interval.",
            "Los fallos de encendido, el ralentí irregular, la dificultad para arrancar o el menor rendimiento pueden relacionarse con las bujías, pero existen otras causas. Siga el intervalo de cambio recomendado por el fabricante.")),
         (t("Are spark plugs part of a tune-up?", "¿Las bujías forman parte de una afinación?"),
          t("Engine tune-ups are a listed service, but the work included is not itemized on this site. Ask the shop whether spark plugs are part of the tune-up your vehicle needs.",
            "Las afinaciones del motor son un servicio anunciado, pero el trabajo incluido no está detallado en este sitio. Pregunte al taller si las bujías forman parte de la afinación que necesita su vehículo."))),

    # ---------------------------------------------------- onboard computer
    _svc("computer", "gear",
         t("Onboard computer diagnostics", "Diagnóstico de la computadora del vehículo"),
         t("Onboard Computer", "Computadora del vehículo"),
         t("Ask about onboard computer diagnostics.", "Pregunte por el diagnóstico de la computadora."),
         t("If a check-engine or other warning light is on, call to ask whether the shop can read and diagnose your vehicle's onboard computer. This is not a specialist or manufacturer-certified claim." + _DISCLAIM_EN,
           "Si hay una luz de motor u otra luz de advertencia encendida, llame para preguntar si el taller puede leer y diagnosticar la computadora de su vehículo. No es una afirmación de especialidad ni de certificación del fabricante." + _DISCLAIM_ES),
         t("Onboard computer diagnostics", "Diagnóstico de la computadora del vehículo"),
         "onboard computer diagnostics", "el diagnóstico de la computadora del vehículo", "del diagnóstico de la computadora del vehículo",
         (t("What does a check-engine light mean?", "¿Qué significa la luz de motor (check engine)?"),
          t("The onboard computer stored a fault. The cause can be minor or serious. Reading the code is a starting point; it does not by itself identify the failed part.",
            "La computadora del vehículo registró una falla. La causa puede ser menor o grave. Leer el código es un punto de partida; por sí solo no identifica la pieza averiada.")),
         (t("Do you reprogram or replace vehicle computer modules?", "¿Reprograman o reemplazan módulos de la computadora del vehículo?"),
          t("Module reprogramming and replacement are not listed on this site. Call with your vehicle details to ask whether that work is available.",
            "La reprogramación y el reemplazo de módulos no figuran en este sitio. Llame con los datos de su vehículo para preguntar si ese trabajo está disponible."))),

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

    # --------------------------------------------------- emission control
    _svc("emissioncontrol", "inspection",
         t("Emission control repair", "Reparación del control de emisiones"),
         t("Emission Control Repair", "Control de emisiones"),
         t("Ask about emission control repair.", "Pregunte por reparación del control de emisiones."),
         t("Emissions testing is a listed service. Repair of emission-control parts, for example after a failed test, is not listed. Call with your inspection report to ask what the shop can do." + _DISCLAIM_EN,
           "Las pruebas de emisiones son un servicio anunciado. La reparación de piezas del control de emisiones, por ejemplo después de una prueba reprobada, no figura. Llame con su informe de inspección para preguntar qué puede hacer el taller." + _DISCLAIM_ES),
         t("Emission control repair", "Reparación del control de emisiones"),
         "emission control repair", "la reparación del control de emisiones", "de la reparación del control de emisiones",
         (t("My vehicle failed an emissions test. Can you fix it?", "Mi vehículo reprobó la prueba de emisiones. ¿Pueden repararlo?"),
          t("Call and have your inspection report ready. The shop will confirm whether it can diagnose and repair the cause for your vehicle.",
            "Llame y tenga a mano su informe de inspección. El taller confirmará si puede diagnosticar y reparar la causa en su vehículo.")),
         (t("Is emissions testing the same as emission control repair?", "¿Las pruebas de emisiones son lo mismo que la reparación del control de emisiones?"),
          t("No. Testing checks whether your vehicle meets the requirement. Repair addresses the parts behind a failure. Testing is listed; repair is call-to-confirm.",
            "No. La prueba verifica si su vehículo cumple el requisito. La reparación atiende las piezas que causan una falla. La prueba figura entre los servicios; la reparación se confirma por teléfono."))),

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
         t("Tire retreads", "Llantas renovadas (retread)"),
         t("Tire Retreads", "Llantas renovadas"),
         t("Ask about tire retreads.", "Pregunte por llantas renovadas."),
         t("A retread puts new tread on a worn tire's casing. Call to ask whether the shop offers or can arrange retreads for your vehicle." + _DISCLAIM_EN,
           "Una llanta renovada (retread) lleva banda de rodadura nueva sobre la carcasa de una llanta desgastada. Llame para preguntar si el taller ofrece o puede coordinar llantas renovadas para su vehículo." + _DISCLAIM_ES),
         t("Tire retreads", "Llantas renovadas (retread)"),
         "tire retreads", "las llantas renovadas", "de las llantas renovadas",
         (t("What is a retread tire?", "¿Qué es una llanta renovada (retread)?"),
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
