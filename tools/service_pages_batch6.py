# -*- coding: utf-8 -*-
"""Service pages batch 1: svc_engine, svc_battery, svc_transmission, svc_steering. Written by ChatGPT, 2026-11-01. Needs fact check before publishing."""


def t(en, es):
    return {"en": en, "es": es}


SERVICE_PAGES = [
    {
        "key": "svc_engine",
        "slug": "engine-repair",
        "covers": ["engine"],
        "primary_kw": "engine repair Phoenixville PA",
        "secondary_kws": [
            "check engine light", "engine diagnostics", "engine tune-up", "fuel injector cleaning", "engine misfire",
            "spark plugs", "timing components", "engine rebuild", "engine replacement", "fuel pumps", "oil leaks"
        ],
        "page": {
            "title": t("Engine Repair Phoenixville, PA | Diverse Autoworks", "Reparación de motor en Phoenixville, PA | Diverse Autoworks"),
            "desc": t(
                "Engine repair in Phoenixville, PA: diagnosis, tune-ups, fuel injectors, timing, internal repairs and engine replacement at Diverse Autoworks.",
                "Reparación de motor en Phoenixville, PA: diagnóstico, afinación, inyectores, distribución y reparación interna en Diverse Autoworks."
            ),
            "h1": t("Engine Repair in Phoenixville, PA", "Reparación de motor en Phoenixville, PA"),
            "lead": t(
                "For engine repair in Phoenixville, PA, Diverse Autoworks diagnoses performance problems and handles everything from tune-ups to internal engine work. Our ASE-certified technicians work with domestic and foreign gas and diesel vehicles. A warning light, hard start or unfamiliar engine noise deserves an explanation before anyone decides which repair makes sense.",
                "Para reparación de motor en Phoenixville, PA, Diverse Autoworks diagnostica fallas de funcionamiento y realiza desde afinaciones hasta trabajos internos del motor. Nuestros técnicos certificados por ASE atienden vehículos nacionales e importados de gasolina y diésel. Si aparece una luz de advertencia, cuesta arrancar o escucha un ruido nuevo, conviene identificar la causa antes de decidir qué reparar."
            ),
            "crumb": t("Engine repair", "Reparación de motor"),
        },
        "service_type": t("Engine diagnosis and repair", "Diagnóstico y reparación del motor"),
        "blocks": [
            ("h2", t("Engine repair in Phoenixville, PA: start with the cause", "Reparación de motor en Phoenixville, PA: primero la causa")),
            ("p", t(
                "Your engine depends on fuel, air, ignition or compression, cooling, lubrication and computer controls working together. A problem in one area can look like trouble somewhere else. Rough idling, for example, may involve ignition, fuel delivery or a sensor rather than an internal engine failure. Engine diagnostics help separate those possibilities, especially when the vehicle still runs but feels different from normal.",
                "El motor necesita que la alimentación de combustible, el aire, el encendido o la compresión, el enfriamiento, la lubricación y los controles electrónicos funcionen en conjunto. Una falla puede parecer que viene de otra parte. Por ejemplo, un ralentí irregular puede relacionarse con el encendido, el combustible o un sensor, sin que necesariamente exista daño interno. El diagnóstico permite diferenciar estas posibilidades."
            )),
            ("p", t(
                "The check engine light reports that the vehicle's onboard system detected a fault; it does not name the failed part. A diagnostic code is a starting point, not a parts order. Describe when the light appeared, what the car was doing and whether the symptoms change when the engine is cold, warm or under load. Those details can distinguish an occasional engine misfire from a problem that happens on every drive.",
                "La luz de revisión del motor indica que el sistema de diagnóstico del vehículo detectó una falla, pero no identifica por sí sola la pieza dañada. Un código es el punto de partida, no una orden de cambiar componentes. Explique cuándo apareció la luz, qué hacía el vehículo y si el problema cambia con el motor frío, caliente o al acelerar. Esos detalles ayudan a interpretar la falla."
            )),
            ("h2", t("Signs you may need engine repair", "Señales de que el motor necesita atención")),
            ("ul", [
                t("The check engine light stays on or begins flashing.", "La luz de revisión del motor permanece encendida o parpadea."),
                t("The engine shakes, hesitates, misfires or idles unevenly.", "El motor vibra, titubea, presenta fallas de combustión o tiene un ralentí irregular."),
                t("Starting becomes difficult or the engine stalls unexpectedly.", "Cuesta arrancar o el motor se apaga de manera inesperada."),
                t("Acceleration feels weaker, or fuel use changes without an obvious reason.", "Nota menos respuesta al acelerar o un cambio en el consumo de combustible sin causa evidente."),
                t("An unfamiliar ticking, knocking or other engine sound appears.", "Aparece un golpeteo, tic-tac u otro ruido nuevo del motor."),
                t("The temperature warning rises, or oil-related warning signs appear.", "Sube la advertencia de temperatura o aparece una alerta relacionada con el aceite."),
            ]),
            ("p", t(
                "These signs do not all mean a major engine repair is needed. The underlying cause should be diagnosed before parts are replaced. If the check engine light is flashing, or an oil-pressure or overheating warning appears, stop in a safe place and consult the owner's manual rather than continuing a trip that could worsen the problem.",
                "Estas señales no significan necesariamente que el motor necesite una reparación mayor. Primero hay que diagnosticar la causa antes de reemplazar piezas. Si la luz de revisión del motor parpadea o aparece una alerta de presión de aceite o sobrecalentamiento, deténgase en un lugar seguro y consulte el manual antes de continuar."
            )),
            ("h2", t("Engine repair work we do", "Trabajos de motor que realizamos")),
            ("ul", [
                t("Engine analysis, onboard computer diagnostics and engine repair.", "Análisis del motor, diagnóstico de la computadora del vehículo y reparación del motor."),
                t("Tune-ups, spark plugs, ignition systems, sensors and engine electronics.", "Afinaciones, bujías, sistemas de encendido, sensores y electrónica del motor."),
                t("Fuel-injector cleaning and service involving fuel pumps, fuel lines and injectors.", "Limpieza de inyectores y trabajos en bombas de combustible, líneas e inyectores."),
                t("Cooling, lubrication, oil-leak, belt and engine-accessory work.", "Trabajos de enfriamiento, lubricación, fugas de aceite, correas y accesorios del motor."),
                t("Timing components, valvetrain, cylinder heads and engine blocks.", "Componentes de distribución, tren de válvulas, culatas y bloques del motor."),
                t("Internal engine repair, engine rebuild and engine replacement.", "Reparación interna, reconstrucción y reemplazo de motores."),
            ]),
            ("h3", t("Tune-ups, ignition and fuel delivery", "Afinación, encendido y suministro de combustible")),
            ("p", t(
                "An engine tune-up is not the same fixed package for every car. The relevant items depend on the engine and the maintenance record. Spark plugs, ignition faults, sensor information and fuel delivery can all affect starting and running quality. We handle tune-ups and fuel injector cleaning, along with the confirmed fuel-system and electronic work listed above. A rough-running engine may need diagnosis rather than a routine tune-up.",
                "Una afinación no es un paquete idéntico para todos los autos. Depende del motor y de su historial de mantenimiento. Las bujías, el encendido, las lecturas de los sensores y el suministro de combustible pueden afectar el arranque y el funcionamiento. Realizamos afinaciones, limpieza de inyectores y los trabajos de combustible y electrónica indicados arriba. Un motor inestable puede necesitar diagnóstico antes que una afinación rutinaria."
            )),
            ("h3", t("Timing, oil leaks and cooling", "Distribución, fugas de aceite y enfriamiento")),
            ("p", t(
                "Engine trouble is not limited to combustion. A lubrication problem can affect internal moving parts; cooling problems can allow temperatures to rise; and worn timing components can affect how the engine operates. Those concerns are related but should not be treated as interchangeable diagnoses. We also have separate information about [timing belts and chains](svc_timing), [oil leaks and gaskets](svc_oilleak) and the [cooling system](svc_cooling).",
                "Las fallas del motor no se limitan a la combustión. Una dificultad de lubricación puede afectar piezas internas; un problema de enfriamiento puede elevar la temperatura; y el desgaste de la distribución puede alterar el funcionamiento. Son asuntos relacionados, pero no equivalentes. Puede consultar nuestras páginas de [correas y cadenas de distribución](svc_timing), [fugas de aceite y juntas](svc_oilleak) y [sistema de enfriamiento](svc_cooling)."
            )),
            ("h3", t("Internal repair, rebuilding or replacement", "Reparación interna, reconstrucción o reemplazo")),
            ("p", t(
                "Some problems involve the cylinder head, block, valvetrain or other internal components rather than external maintenance items. Diverse Autoworks performs internal engine repair and can rebuild or replace an engine. Which approach is appropriate depends on the condition of the existing engine and the diagnosis, not on a single symptom. Ask about the findings and the proposed scope before deciding how to proceed.",
                "Algunas fallas afectan la culata, el bloque, el tren de válvulas u otras piezas internas, y no solamente elementos de mantenimiento externo. Diverse Autoworks realiza reparaciones internas y puede reconstruir o reemplazar motores. La opción adecuada depende del estado del motor y del diagnóstico, no de un solo síntoma. Solicite una explicación de los hallazgos y del trabajo propuesto antes de decidir."
            )),
            ("h2", t("When does your engine need maintenance?", "¿Cuándo necesita mantenimiento el motor?")),
            ("p", t(
                "Your owner's manual lists the maintenance interval for your particular engine, including the applicable spark plug, belt and fluid requirements. Driving conditions and previous service also matter when discussing what should be checked. A tune-up is not a substitute for investigating an active warning light, and a warning light does not automatically mean a replacement engine is needed. Bring the maintenance history if you have it; it provides useful context for the discussion.",
                "El manual del propietario indica los intervalos correspondientes a su motor, incluidas las recomendaciones para bujías, correas y líquidos. Las condiciones de manejo y el servicio anterior también ayudan a decidir qué revisar. Una afinación no sustituye el diagnóstico de una luz de advertencia, y esa luz tampoco significa automáticamente que haga falta otro motor. Si conserva el historial de mantenimiento, tráigalo como referencia."
            )),
            ("h2", t("Engine problems and Pennsylvania inspections", "El motor y las inspecciones de Pensilvania")),
            ("p", t(
                "The engine and its emissions controls interact, but an engine warning light is not itself a complete emissions diagnosis. Chester County vehicles subject to emissions testing follow Pennsylvania's applicable rules, and safety inspections cover other systems as well. If a problem involves exhaust or emissions controls, see our [emissions-related repairs](svc_emissions) page and the [state inspections](inspections) page. The applicable test depends on the vehicle.",
                "El motor y los controles de emisiones están relacionados, pero una luz de advertencia no constituye por sí sola un diagnóstico de emisiones. Los vehículos de Chester County sujetos a estas pruebas siguen las reglas correspondientes de Pensilvania; la inspección de seguridad también revisa otros sistemas. Si el problema se relaciona con el escape o las emisiones, vea [reparaciones de emisiones](svc_emissions) e [inspecciones estatales](inspections). La prueba aplicable depende del vehículo."
            )),
            ("p", t(
                "When discussing an engine problem, separate what you have observed from what you suspect caused it. A warning light that appeared after a cold start, a noise noticed only under acceleration and a loss of power while climbing a hill are different descriptions. An accurate history does not replace engine analysis, but it helps explain why one inspection or repair approach may fit better than another. Ask which findings support the recommendation.",
                "Al explicar una falla del motor, distinga lo que observó de lo que cree que la causó. Una luz que aparece con el motor frío, un ruido que solo se oye al acelerar y una pérdida de fuerza en una pendiente son situaciones distintas. Un historial preciso no reemplaza el análisis del motor, pero ayuda a entender las recomendaciones. Pregunte qué hallazgos respaldan el trabajo propuesto."
            )),
            ("p", t(
                "Our shop is at 1415 Pawlings Road in Phoenixville, Chester County, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge. If it can't be driven, we can arrange or accept a tow, and we offer drop-off and after-hours arrangements.",
                "Estamos en 1415 Pawlings Road, Phoenixville, Chester County, a poca distancia en auto de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge. Si no puede conducir el vehículo, podemos coordinar o recibir una grúa, así como organizar la entrega del auto fuera del horario habitual."
            )),
        ],
        "faq": [
            (t("Does a check engine light always mean the engine is failing?", "¿La luz de revisión del motor significa que el motor está fallando?"), t("No. It reports a detected fault and can relate to ignition, fuel delivery, sensors or other systems. A diagnosis is needed to identify the cause.", "No. Indica una falla detectada y puede estar relacionada con el encendido, el combustible, los sensores u otros sistemas. Hace falta un diagnóstico para encontrar la causa.")),
            (t("What causes an engine to misfire?", "¿Por qué falla el encendido de un motor?"), t("Ignition, fuel delivery and mechanical problems can cause misfires. The pattern and diagnostic results help narrow down what is happening.", "Las fallas de encendido pueden deberse al sistema de encendido, al combustible o a problemas mecánicos. Los síntomas y el diagnóstico ayudan a identificar el origen.")),
            (t("Do you clean fuel injectors?", "¿Realizan limpieza de inyectores de combustible?"), t("Yes. Fuel-injector cleaning is among the engine services Diverse Autoworks provides. A technician can discuss whether it is relevant to your vehicle's symptoms.", "Sí. Diverse Autoworks realiza limpieza de inyectores. Un técnico puede explicar si ese servicio corresponde a los síntomas de su vehículo.")),
            (t("Can you rebuild or replace an engine?", "¿Pueden reconstruir o reemplazar un motor?"), t("Yes. The shop performs internal engine repairs, engine rebuilds and replacements. The recommended work depends on the condition of the engine.", "Sí. El taller realiza reparaciones internas, reconstrucciones y reemplazos de motor. El trabajo recomendado depende de su condición.")),
            (t("Should I keep driving with a flashing check engine light?", "¿Debo seguir manejando si parpadea la luz del motor?"), t("A flashing light calls for prompt attention. Stop somewhere safe and follow the warning guidance in your owner's manual rather than continuing to drive with serious symptoms.", "Una luz que parpadea requiere atención pronta. Deténgase en un lugar seguro y siga las indicaciones del manual en vez de continuar conduciendo con síntomas graves.")),
            (t("Do engine tune-ups include spark plugs?", "¿Una afinación incluye las bujías?"), t("Spark plugs are within our confirmed engine service scope, but the work appropriate for a tune-up depends on the specific vehicle and its maintenance needs.", "Las bujías forman parte de los trabajos que realizamos, pero el contenido de una afinación depende del vehículo y de sus necesidades de mantenimiento.")),
        ],
        "cta": [
            ("h2", t("Schedule engine repair near Phoenixville, PA", "Programe reparación de motor cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule engine repair with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Comuníquese con Diverse Autoworks para programar la reparación del motor con uno de nuestros técnicos certificados por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": (
            "engine repair check engine light engine diagnostics misfire rough idle tune up tune-up spark plugs ignition coil injector cleaning fuel pump fuel line timing valve train cylinder head engine block rebuild replacement oil pressure overheating mechanic motor repair moter engin chek engin Phoenixville Chester County",
            "reparación de motor diagnóstico del motor luz de revisión del motor luz check engine falla de encendido ralentí irregular afinación bujías bobina inyectores limpieza de inyectores bomba de gasolina línea de combustible correa de distribución cadena de distribución culata bloque reconstrucción cambio de motor temperatura presión de aceite mecánico Fénixvil Chester County"
        ),
        "sources": [
            ("AAA: Onboard Diagnostics and Check Engine Light", "https://www.aaa.com/autorepair/codetranslator"),
            ("AAA: Car Tune-Up Warning Signs", "https://mwg.aaa.com/automotive/auto-repair/articles/car-tune-up-warning-signs-checklist"),
            ("AAA: How Engine Oil Protects the Engine", "https://ww2.aaa.com/autorepair/articles/car-fluids-how-to-check-and-maintain-them-for-peak-performance"),
            ("PennDOT: Safety Inspection Program for Consumers", "https://www.pa.gov/agencies/dmv/faqs/motor-vehicle-faqs/safety-inspection-consumers-faqs"),
            ("PennDOT: Emissions Inspection Program", "https://www.pa.gov/agencies/dmv/vehicle-services/inspection-and-safety-requirements/emission-inspections-program"),
        ],
        "verify": [],
    },
    {
        "key": "svc_battery",
        "slug": "battery-replacement",
        "covers": ["battery"],
        "primary_kw": "car battery replacement Phoenixville",
        "secondary_kws": [
            "slow engine crank", "car won't start", "dead car battery", "battery warning light", "starting system diagnosis",
            "repeated jump starts", "dim headlights", "alternator", "battery condition", "charging system diagnosis"
        ],
        "page": {
            "title": t("Car Battery Replacement Phoenixville | Diverse Autoworks", "Cambio de batería en Phoenixville, PA | Diverse Autoworks"),
            "desc": t(
                "Car battery replacement in Phoenixville, PA. Diverse Autoworks tests batteries and diagnoses starting and charging problems before replacement.",
                "Cambio de batería en Phoenixville, PA. Diverse Autoworks prueba baterías y diagnostica fallas de arranque y carga antes del reemplazo."
            ),
            "h1": t("Car Battery Replacement in Phoenixville, PA", "Cambio de batería de auto en Phoenixville, PA"),
            "lead": t(
                "For car battery replacement in Phoenixville, Diverse Autoworks checks the battery and diagnoses starting or charging concerns. Our ASE-certified technicians help you tell the difference between a weak battery and another problem that keeps the car from starting. We work on domestic and foreign gas and diesel vehicles at our Phoenixville, PA shop.",
                "Si necesita un cambio de batería de auto en Phoenixville, Diverse Autoworks realiza pruebas de batería y diagnostica problemas de arranque o carga. Nuestros técnicos certificados por ASE ayudan a distinguir una batería débil de otras fallas que impiden arrancar. Atendemos vehículos nacionales e importados de gasolina y diésel en Phoenixville, PA."
            ),
            "crumb": t("Battery replacement", "Cambio de batería"),
        },
        "service_type": t("Battery testing and replacement", "Prueba y reemplazo de batería"),
        "blocks": [
            ("h2", t("Car battery replacement in Phoenixville: what gets checked", "Cambio de batería en Phoenixville: qué se revisa")),
            ("p", t(
                "The battery supplies the electrical power needed to start a conventional gas or diesel vehicle and supports its electrical systems. Once the engine is running, the charging system helps restore the battery's charge. The starter, charging system and battery therefore produce some overlapping symptoms. A car that will not start does not automatically need a new battery, and a new battery may not solve a charging fault.",
                "La batería proporciona la energía eléctrica necesaria para arrancar un vehículo convencional de gasolina o diésel y alimentar sus sistemas eléctricos. Cuando el motor funciona, el sistema de carga ayuda a reponer esa energía. Por eso, una falla de batería puede parecerse a un problema del motor de arranque o del sistema de carga. Si el auto no arranca, no siempre necesita una batería nueva; reemplazarla tampoco corrige una falla de carga."
            )),
            ("p", t(
                "Battery testing is useful because it addresses the question directly: is the battery able to do its job? Starting and charging system diagnosis looks beyond the battery itself. If the engine cranks slowly, that information matters. If you turn the key and hear clicking without cranking, that is a different clue. Tell the technician what happens at the moment you try to start the car, rather than describing every starting problem as a dead car battery.",
                "La prueba de batería ayuda a saber si todavía puede cumplir su función. El diagnóstico del sistema de arranque y carga examina posibles causas fuera de la batería. Que el motor gire lentamente es un dato útil; escuchar clics sin que gire es una pista distinta. Explique exactamente qué ocurre al intentar arrancar en lugar de llamar batería descargada a cualquier problema de encendido."
            )),
            ("h2", t("Signs you may need battery testing or replacement", "Señales de que la batería necesita una revisión")),
            ("ul", [
                t("The engine turns over more slowly than it used to.", "El motor gira más lentamente de lo habitual al arrancar."),
                t("You hear a click when starting, or the car won't start.", "Escucha un clic al intentar arrancar o el auto no enciende."),
                t("Headlights are dim, or interior electronics behave unpredictably.", "Los faros se ven tenues o los dispositivos interiores funcionan de forma irregular."),
                t("The battery warning light or charging indicator appears.", "Se enciende el testigo de batería o del sistema de carga."),
                t("The vehicle needs repeated jump starts to get going.", "El vehículo necesita recibir corriente repetidamente para arrancar."),
                t("Starting changes noticeably after the vehicle has been parked.", "El arranque cambia notablemente después de dejar el vehículo estacionado."),
            ]),
            ("p", t(
                "Dim headlights and repeated jump starts are warning signs, not proof of a failed battery. A charging problem, electrical fault or starting-system issue may be involved. The cause should be diagnosed before parts are replaced. If the vehicle has stalled or will not restart, do not assume that getting it running once means the underlying problem has gone away.",
                "Los faros tenues y la necesidad frecuente de recibir corriente son señales, no pruebas de que la batería esté dañada. También puede existir una falla eléctrica, de carga o de arranque. Hay que diagnosticar la causa antes de reemplazar piezas. Si el vehículo se apagó o no vuelve a arrancar, no suponga que la falla desapareció porque logró encenderlo una vez."
            )),
            ("h2", t("Battery and charging work we do", "Servicios de batería y carga que realizamos")),
            ("ul", [
                t("Car battery testing to evaluate battery condition.", "Pruebas de batería para evaluar su estado."),
                t("Car battery replacement when a replacement is appropriate.", "Reemplazo de batería cuando corresponde cambiarla."),
                t("Starting system diagnosis for cranking and no-start symptoms.", "Diagnóstico del sistema de arranque cuando el motor gira con dificultad o no arranca."),
                t("Charging system diagnosis for battery and charging warnings.", "Diagnóstico del sistema de carga ante alertas de batería o de carga."),
            ]),
            ("h3", t("Battery condition versus charging problems", "Estado de la batería frente a fallas de carga")),
            ("p", t(
                "A battery can be weak even though the charging system is working. The reverse is also possible: a usable battery may lose charge when the vehicle is not replenishing it properly. That is why we distinguish battery testing from charging system diagnosis. A battery warning light while driving should not be interpreted as an instruction to purchase a battery; it may indicate that the vehicle is not charging as expected.",
                "Una batería puede estar débil aunque el sistema de carga funcione bien. También puede ocurrir lo contrario: una batería en buen estado pierde carga porque el vehículo no la repone correctamente. Por eso distinguimos la prueba de batería del diagnóstico del sistema de carga. Una luz de batería encendida mientras conduce no significa automáticamente que deba comprar otra; puede indicar un problema de carga."
            )),
            ("h3", t("Why starting symptoms need context", "Por qué importa describir el arranque")),
            ("p", t(
                "A slow engine crank, a single click, silence when turning the key and normal cranking without the engine firing are different complaints. They can guide where a starting-system diagnosis begins. Mention any recent battery replacement, changes in dashboard lights and occasions when the car started normally. That history may help separate an intermittent condition from a problem that occurs every time you attempt to start.",
                "Que el motor gire despacio, se escuche un solo clic, no haya reacción al girar la llave o el motor gire sin encender son situaciones diferentes. Describirlas ayuda a orientar el diagnóstico. Indique si cambiaron la batería recientemente, si aparecieron luces de advertencia o si a veces arranca con normalidad. El historial ayuda a distinguir una falla intermitente de una constante."
            )),
            ("h2", t("When should a car battery be checked?", "¿Cuándo conviene revisar la batería?")),
            ("p", t(
                "The right time to test a battery depends on its condition, the vehicle's behavior and your maintenance history. Heat, cold and long periods without driving can expose a weakness that was not obvious during daily use. If you notice slower cranking, ask about battery testing rather than waiting for a complete no-start. For vehicle-specific maintenance guidance, follow your owner's manual; there is no single replacement date that fits every battery.",
                "El momento adecuado para probar una batería depende de su estado, del comportamiento del vehículo y de su historial. El calor, el frío y los periodos largos sin conducir pueden revelar una debilidad antes poco evidente. Si nota que el motor gira más despacio, pregunte por una prueba de batería en vez de esperar a que deje de arrancar. Siga el manual del propietario: no existe una fecha de reemplazo aplicable a todas las baterías."
            )),
            ("p", t(
                "Before choosing a replacement, it also helps to distinguish a starting complaint from an engine-running problem. If the engine cranks normally but fails to fire, diagnosis may need to consider other systems. Read about our [engine diagnostics and repair](svc_engine) for running concerns, or [electrical repair](svc_electrical) for other electrical complaints. Those pages cover different services; a battery test is not a substitute for diagnosing unrelated symptoms.",
                "Antes de elegir una batería nueva, conviene distinguir una falla de arranque de un problema de funcionamiento del motor. Si gira normalmente pero no enciende, puede ser necesario revisar otros sistemas. Vea [diagnóstico y reparación del motor](svc_engine) para fallas de funcionamiento, o [reparación eléctrica](svc_electrical) para otros problemas eléctricos. Una prueba de batería no sustituye el diagnóstico de síntomas distintos."
            )),
            ("h2", t("What to do if the vehicle will not start", "Qué hacer si el vehículo no arranca")),
            ("p", t(
                "Pay attention to the dash warning lamps, the sound when you try to start and any recent changes in how the car behaves. Avoid repeated attempts if there is smoke, a strong unusual smell or another sign of an electrical problem. If you are unsure about jump-starting safely, use appropriate roadside help rather than improvising around battery terminals. A successful jump start tells you the car started; it does not identify why it lost power.",
                "Observe las luces del tablero, el sonido al intentar arrancar y los cambios recientes en el vehículo. Evite insistir si nota humo, un olor inusual fuerte u otra señal de falla eléctrica. Si no sabe cómo pasar corriente de forma segura, solicite ayuda de carretera en vez de improvisar con las terminales. Que el auto arranque después de recibir corriente no explica por qué se quedó sin energía."
            )),
            ("p", t(
                "If you are planning a visit, note how long the vehicle was parked before the problem started and if dashboard lights or interior accessories still worked. Tell the shop if the starting difficulty happened once or has been recurring. Do not assume a recently installed battery rules out a separate charging-system issue; describing the events in order gives a more useful picture than guessing which part to replace. Battery testing can then address the condition of the battery itself.",
                "Antes de visitar el taller, recuerde cuánto tiempo estuvo estacionado el auto antes de fallar y si las luces del tablero u otros accesorios funcionaban. Indique si el problema ocurrió una sola vez o se repite. Una batería instalada recientemente no descarta una falla de carga. Relatar los hechos en orden es más útil que adivinar qué pieza cambiar; la prueba de batería permite evaluar su estado."
            )),
            ("p", t(
                "Diverse Autoworks is located at 1415 Pawlings Road in Phoenixville, Chester County, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge. If it can't be driven, we can arrange or accept a tow, and we offer drop-off and after-hours arrangements.",
                "Diverse Autoworks está en 1415 Pawlings Road, Phoenixville, Chester County, a poca distancia en auto de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge. Si no puede conducir el vehículo, podemos coordinar o recibir una grúa, así como organizar la entrega del auto fuera del horario habitual."
            )),
        ],
        "faq": [
            (t("How do I know if my car battery needs replacing?", "¿Cómo sé si debo cambiar la batería de mi auto?"), t("Slow cranking, repeated jump starts and dim lights are reasons to test it. Battery testing helps determine its condition before replacement.", "Un arranque lento, la necesidad frecuente de recibir corriente y las luces tenues son motivos para probarla. La prueba ayuda a conocer su estado antes de cambiarla.")),
            (t("Can a bad alternator look like a dead battery?", "¿Una falla del alternador puede parecer una batería descargada?"), t("Yes. A charging problem can leave the battery low on power. Charging system diagnosis helps distinguish that situation from a battery that is no longer working properly.", "Sí. Una falla de carga puede dejar la batería sin suficiente energía. El diagnóstico del sistema de carga ayuda a distinguirla de una batería deteriorada.")),
            (t("Why does my car click but not start?", "¿Por qué mi auto hace clic pero no arranca?"), t("A click may be related to the battery, its connections or the starting system. The sound alone is not enough to select a replacement part.", "El clic puede relacionarse con la batería, sus conexiones o el sistema de arranque. El sonido por sí solo no permite decidir qué pieza cambiar.")),
            (t("Do you test a battery before replacing it?", "¿Prueban la batería antes de reemplazarla?"), t("Battery testing and replacement are confirmed services at Diverse Autoworks. Describe your symptoms so the shop can discuss the appropriate evaluation.", "Diverse Autoworks ofrece pruebas y reemplazo de baterías. Explique los síntomas para que el taller le indique la evaluación adecuada.")),
            (t("Does a battery warning light mean I need a new battery?", "¿La luz de batería significa que necesito una nueva?"), t("Not necessarily. The warning can indicate a charging-system problem, so the system should be diagnosed instead of assuming the battery is at fault.", "No necesariamente. La alerta puede indicar una falla del sistema de carga, por lo que conviene diagnosticarlo antes de culpar a la batería.")),
            (t("Can I drive after jump-starting a dead battery?", "¿Puedo conducir después de pasarle corriente a la batería?"), t("A jump start does not confirm that the charging system is functioning properly. If the car loses power again or a charging warning stays on, seek an evaluation and avoid relying on it for a long trip.", "Pasar corriente no confirma que el sistema de carga funcione bien. Si vuelve a perder energía o sigue la advertencia de carga, solicite una revisión y no dependa del auto para un viaje largo.")),
        ],
        "cta": [
            ("h2", t("Schedule car battery replacement near Phoenixville, PA", "Programe cambio de batería cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule battery testing or replacement with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Comuníquese con Diverse Autoworks para programar una prueba o cambio de batería con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": (
            "car battery replacement battery change battery testing battery light charging system alternator test starter diagnosis no start not starting wont start won't start dead battery slow crank clicking dim headlights jump start jumpstart car battrey batery battary Phoenixville Chester County",
            "cambio de batería batería de carro batería de auto prueba de batería test de batería sistema de carga alternador motor de arranque no arranca no enciende arranque lento clic faros tenues pasar corriente batería descargada bateria remplazo de bateria Phoenixville Chester County"
        ),
        "sources": [
            ("AAA: Signs Your Battery Needs Replacing", "https://mwg.aaa.com/automotive/roadside/articles/10-signs-your-battery-needs-replacing"),
            ("AAA: How Long Do Car Batteries Last", "https://www.aaa.com/autorepair/articles/how-long-do-car-batteries-last"),
            ("AAA: Common Reasons a Car Won't Start", "https://www.aaa.com/autorepair/articles/14-reasons-why-your-car-wont-start"),
        ],
        "verify": [],
    },
    {
        "key": "svc_transmission",
        "slug": "transmission-repair",
        "covers": ["drivetrain", "mounts"],
        "primary_kw": "transmission repair Phoenixville PA",
        "secondary_kws": [
            "transmission fluid", "transmission rebuild", "transmission replacement", "motor mount replacement", "transmission mount replacement",
            "rear-axle bearing and seal service", "shifting feel", "gear-change complaint", "engine speed rises"
        ],
        "page": {
            "title": t("Transmission Repair Phoenixville, PA | Diverse Autoworks", "Reparación de transmisión en Phoenixville, PA"),
            "desc": t(
                "Transmission repair in Phoenixville, PA, including maintenance, rebuilds, replacement, mounts and rear-axle bearing and seal service.",
                "Reparación de transmisión en Phoenixville, PA: mantenimiento, reconstrucción, reemplazo, soportes y servicio de baleros y sellos del eje trasero."
            ),
            "h1": t("Transmission Repair in Phoenixville, PA", "Reparación de transmisión en Phoenixville, PA"),
            "lead": t(
                "For transmission repair in Phoenixville, PA, Diverse Autoworks provides transmission maintenance, rebuilds and replacements, as well as motor and transmission mount replacement. Our ASE-certified technicians also service rear-axle bearings and seals. If a vehicle hesitates between gears or develops a new vibration, we start by looking at what the symptom actually tells us rather than assuming it needs a complete transmission.",
                "Para reparación de transmisión en Phoenixville, PA, Diverse Autoworks ofrece mantenimiento, reconstrucción y reemplazo de transmisiones, además de cambio de soportes de motor y de transmisión. Nuestros técnicos certificados por ASE también atienden baleros y sellos del eje trasero. Si el vehículo tarda en cambiar de marcha o aparece una vibración, primero hay que entender el síntoma, sin suponer que necesita una transmisión completa."
            ),
            "crumb": t("Transmission repair", "Reparación de transmisión"),
        },
        "service_type": t("Transmission and mount service", "Servicio de transmisión y soportes"),
        "blocks": [
            ("h2", t("Transmission repair in Phoenixville, PA: understanding the drivetrain", "Reparación de transmisión en Phoenixville, PA: cómo funciona")),
            ("p", t(
                "The transmission helps transfer engine power to the wheels through the vehicle's drivetrain. In an automatic vehicle, gear changes happen without the driver selecting each gear; in a manual vehicle, the driver operates the clutch and gear selector. Both arrangements depend on components working together. A change in shifting feel can be a transmission concern, while a clunk during a change in load may come from a mount or another drivetrain component.",
                "La transmisión lleva la potencia del motor hacia las ruedas por medio del tren motriz. En un vehículo automático, los cambios se realizan sin elegir cada marcha manualmente; en uno manual, el conductor usa el embrague y la palanca. Los sistemas funcionan de manera diferente, pero dependen de varias piezas. Un cambio brusco puede apuntar a la transmisión; un golpe al acelerar o soltar el acelerador también puede relacionarse con un soporte u otro componente."
            )),
            ("p", t(
                "Descriptions such as 'slipping' and 'not shifting right' can mean different things to different drivers. Try to note if the issue happens from a stop, during acceleration, while reversing or after driving for a while. Also note whether the engine speed rises without a matching increase in road speed. That information provides context when discussing transmission maintenance, rebuilding or replacement; it does not, on its own, decide the repair.",
                "Expresiones como 'patina' o 'no cambia bien' pueden describir situaciones distintas. Observe si ocurre al salir, acelerar, poner reversa o después de conducir cierto tiempo. También indique si las revoluciones suben sin que aumente la velocidad de la misma manera. Esa información ayuda a hablar de mantenimiento, reconstrucción o reemplazo, pero no determina por sí sola qué reparación corresponde."
            )),
            ("h2", t("Signs you may need transmission or mount service", "Señales de problemas de transmisión o soportes")),
            ("ul", [
                t("Shifts become harsh, delayed or unusually soft.", "Los cambios se sienten bruscos, tardados o demasiado suaves."),
                t("Engine speed increases without the expected increase in vehicle speed.", "Las revoluciones del motor suben sin el aumento esperado de velocidad."),
                t("There is hesitation when selecting drive or reverse.", "Hay una demora al seleccionar avance o reversa."),
                t("New whining, grinding or clunking sounds appear during driving or shifting.", "Aparecen zumbidos, rechinidos o golpes al conducir o cambiar de marcha."),
                t("A new vibration or thump is noticeable when accelerating or changing load.", "Se percibe una vibración o golpe nuevo al acelerar o cambiar la carga del motor."),
                t("Fluid appears beneath the vehicle, or a related dashboard warning turns on.", "Aparece líquido debajo del vehículo o se enciende una advertencia del tablero."),
            ]),
            ("p", t(
                "Any of these symptoms may have more than one cause. A vibration does not prove that the transmission needs rebuilding, and a gear-change complaint does not automatically indicate a worn mount. The underlying cause should be diagnosed before parts are replaced. If the vehicle loses drive, makes a severe mechanical noise or cannot be controlled normally, stop driving safely and arrange transport rather than forcing it to continue.",
                "Cada síntoma puede tener distintas causas. Una vibración no demuestra que haya que reconstruir la transmisión, ni un cambio brusco confirma un soporte dañado. Se debe diagnosticar la causa antes de reemplazar piezas. Si pierde tracción, produce un ruido mecánico fuerte o deja de responder normalmente, deténgase en un lugar seguro y coordine el traslado en vez de forzarlo a continuar."
            )),
            ("h2", t("Transmission and drivetrain work we do", "Trabajos de transmisión y tren motriz que realizamos")),
            ("ul", [
                t("Transmission maintenance appropriate to the vehicle.", "Mantenimiento de transmisión adecuado para el vehículo."),
                t("Transmission rebuilding and complete transmission replacement.", "Reconstrucción y reemplazo completo de transmisiones."),
                t("Motor mount replacement.", "Reemplazo de soportes de motor."),
                t("Transmission mount replacement.", "Reemplazo de soportes de transmisión."),
                t("Rear-axle bearing and seal service.", "Servicio de baleros y sellos del eje trasero."),
            ]),
            ("h3", t("Transmission maintenance, rebuilds and replacement", "Mantenimiento, reconstrucción y reemplazo de transmisión")),
            ("p", t(
                "Transmission maintenance and major internal work are different decisions. Maintenance follows the requirements of the particular transmission and its service history. Rebuilding involves work on the existing transmission; replacement involves installing another unit. Diverse Autoworks offers all three categories of work. The appropriate path depends on what is wrong, the condition of the assembly and the options discussed for that vehicle, not a generic rule that applies to every shifting complaint.",
                "El mantenimiento y una reparación interna mayor de transmisión son decisiones distintas. El mantenimiento responde a las necesidades de cada vehículo y su historial. Reconstruir significa trabajar en la transmisión existente; reemplazar significa instalar otra unidad. Diverse Autoworks ofrece las tres opciones. La indicada depende de la falla, del estado del conjunto y de lo que se determine para ese vehículo, no de una regla general para cualquier cambio irregular."
            )),
            ("h3", t("Motor and transmission mounts", "Soportes de motor y de transmisión")),
            ("p", t(
                "Mounts hold the engine and transmission in position while allowing for movement and vibration during normal operation. If a mount wears or breaks, a driver may notice extra movement, vibration or a knock as the vehicle takes up load. Those signs can overlap with other mechanical issues. We replace motor and transmission mounts, but the symptom still needs to be traced before deciding that a particular mount is responsible.",
                "Los soportes mantienen el motor y la transmisión en su posición, a la vez que permiten cierto movimiento y absorben vibraciones. Si se desgastan o rompen, pueden aparecer movimientos excesivos, vibraciones o golpes al acelerar. Esas señales también pueden tener otras causas. Reemplazamos soportes de motor y de transmisión, pero primero hay que identificar la pieza que realmente ocasiona el problema."
            )),
            ("h3", t("Rear-axle bearings and seals", "Baleros y sellos del eje trasero")),
            ("p", t(
                "Rear-axle bearings support rotating components, and seals help contain lubricant where required by the axle design. Noise from the rear or lubricant around an axle area may justify closer attention, but the location and source of a sound are not always obvious from the driver's seat. Our confirmed drivetrain scope includes rear-axle bearing and seal service. For different work involving [CV axles and differentials](svc_axle), see the existing dedicated page.",
                "Los baleros del eje trasero soportan piezas giratorias y los sellos ayudan a retener el lubricante según el diseño. Un ruido posterior o señales de líquido cerca del eje merecen atención, aunque desde el asiento puede ser difícil ubicar su origen. Nuestro servicio confirmado incluye baleros y sellos del eje trasero. Para otros trabajos de [ejes CV y diferenciales](svc_axle), consulte la página correspondiente."
            )),
            ("h2", t("Transmission fluid and service intervals", "Líquido de transmisión e intervalos de servicio")),
            ("p", t(
                "Transmission maintenance is vehicle-specific. The correct fluid requirements, inspection procedure and service interval are found in your owner's manual. Some transmissions make fluid condition difficult for an owner to check directly, so guessing by color alone is not a dependable maintenance plan. Ask about your vehicle's recommended service if you are unsure what has been done before. Keep a record of past maintenance and describe any shifting change separately from routine service.",
                "El mantenimiento de transmisión depende de cada vehículo. El manual del propietario indica el líquido adecuado, el procedimiento y los intervalos de servicio. En algunas transmisiones es difícil revisar el líquido sin equipo o procedimiento específico, por lo que su color no basta para decidir. Si desconoce el mantenimiento anterior, pregunte por lo recomendado para su modelo. Conserve el historial y describa cualquier cambio anormal por separado."
            )),
            ("h2", t("When another drivetrain component is involved", "Cuando el problema está en otra parte del tren motriz")),
            ("p", t(
                "A complaint that feels like transmission trouble may involve connected components. Manual-transmission drivers may also want to read about [clutch repair](svc_clutch). A humming noise near a wheel may call for information about [wheel bearings and hubs](svc_bearing), while axle or joint concerns have their own [CV axle and differential](svc_axle) page. These are links to existing services, not a reason to assume all of those parts need repair together.",
                "Una falla que parece venir de la transmisión puede relacionarse con piezas conectadas. Quienes conducen vehículos manuales pueden consultar [reparación del embrague](svc_clutch). Un zumbido cerca de una rueda puede relacionarse con [baleros y mazas de rueda](svc_bearing), mientras que los ejes y juntas tienen su propia página de [ejes CV y diferencial](svc_axle). Son servicios distintos; no significa que todas esas piezas necesiten reparación."
            )),
            ("p", t(
                "For a shifting complaint, record the conditions in which it first appears and what happens immediately afterward. Does the transmission react differently in reverse, or does the sound occur only when the vehicle begins moving? Are you noticing a change from its previous behavior, or have you just purchased the car and have no baseline? These details help keep a routine maintenance discussion separate from an active mechanical complaint. The owner's manual remains the reference for scheduled work.",
                "Ante un problema de cambios, recuerde cuándo aparece y qué ocurre después. ¿La transmisión responde distinto en reversa o el ruido comienza al iniciar el movimiento? ¿Es un cambio reciente o acaba de adquirir el vehículo y desconoce cómo funcionaba antes? Esos detalles permiten separar el mantenimiento programado de una falla mecánica activa. El manual del propietario sigue siendo la referencia para los servicios periódicos."
            )),
            ("p", t(
                "You can find Diverse Autoworks at 1415 Pawlings Road in Phoenixville, Chester County, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge. If it can't be driven, we can arrange or accept a tow, and we offer drop-off and after-hours arrangements.",
                "Diverse Autoworks se encuentra en 1415 Pawlings Road, Phoenixville, Chester County, a poca distancia en auto de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge. Si no puede conducir el vehículo, podemos coordinar o recibir una grúa, así como organizar la entrega del auto fuera del horario habitual."
            )),
        ],
        "faq": [
            (t("Does rough shifting mean I need a new transmission?", "¿Los cambios bruscos significan que necesito otra transmisión?"), t("Not automatically. Rough shifting can have different causes, so the symptoms and condition of the transmission need evaluation before a rebuild or replacement is discussed.", "No necesariamente. Los cambios bruscos pueden tener distintas causas, así que primero hay que evaluar los síntomas y el estado de la transmisión antes de decidir una reconstrucción o reemplazo.")),
            (t("Do you rebuild transmissions?", "¿Reconstruyen transmisiones?"), t("Yes. Diverse Autoworks provides transmission maintenance, rebuilding and replacement. The choice depends on the vehicle's condition and the work needed.", "Sí. Diverse Autoworks ofrece mantenimiento, reconstrucción y reemplazo de transmisiones. La decisión depende del estado del vehículo y del trabajo requerido.")),
            (t("What are symptoms of a worn transmission mount?", "¿Qué síntomas produce un soporte de transmisión desgastado?"), t("New vibrations, movement or clunks when engine load changes may point to a mount. Other components can cause similar sensations, so a diagnosis matters.", "Una vibración nueva, movimientos o golpes al cambiar la carga del motor pueden apuntar a un soporte. Otras piezas producen síntomas parecidos, por lo que es importante diagnosticar.")),
            (t("Can you replace motor mounts?", "¿Pueden cambiar los soportes del motor?"), t("Yes. Motor and transmission mount replacement are both within the shop's confirmed services.", "Sí. El taller realiza reemplazo de soportes de motor y de transmisión.")),
            (t("Do you service rear-axle bearings and seals?", "¿Revisan baleros y sellos del eje trasero?"), t("Yes. Rear-axle bearing and seal service are included in our drivetrain work. The specific concern should be described when arranging a visit.", "Sí. El servicio de baleros y sellos del eje trasero forma parte de nuestros trabajos del tren motriz. Describa el problema al solicitar atención.")),
            (t("How often should transmission fluid be serviced?", "¿Cada cuánto se debe cambiar el líquido de transmisión?"), t("Follow the interval and fluid specifications in your owner's manual. Requirements vary by vehicle and transmission type.", "Siga el intervalo y las especificaciones del manual del propietario. Las recomendaciones varían según el vehículo y el tipo de transmisión.")),
        ],
        "cta": [
            ("h2", t("Schedule transmission repair near Phoenixville, PA", "Programe reparación de transmisión cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule transmission service with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Comuníquese con Diverse Autoworks para programar un servicio de transmisión con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": (
            "transmission repair transmission rebuild rebuilt transmission replace transmission service maintenance fluid automatic manual shifting slip slipping hard shift gear delayed engagement drivetrain transsmision transmsission motor mount transmission mount engine mounts rear axle bearings seal axle seal Phoenixville Chester County",
            "reparación de transmisión caja de velocidades transmisión automática manual reconstrucción cambio de transmisión mantenimiento aceite líquido de transmisión patina resbala cambio brusco tarda en entrar marcha soportes de motor soportes de transmisión balero eje trasero sello retén eje Phoenixville Chester County"
        ),
        "sources": [
            ("AAA: How to Recognize Common Mechanical Problems", "https://ace.aaa.com/automotive/advocacy/recognize-symptoms-most-common-car-mechanical-problems.html"),
            ("AAA: How to Check and Maintain Transmission Fluid", "https://www.acg.aaa.com/connect/blogs/5c/auto/how-to-check-and-maintain-your-transmission-fluid"),
            ("AAA: Car Maintenance Guide, Fluids", "https://autoclubsouth.aaa.com/Automotive/auto_maintenance_text.aspx?section=Fluids"),
        ],
        "verify": [],
    },
    {
        "key": "svc_steering",
        "slug": "steering-components",
        "covers": ["powersteer", "control", "balljoints"],
        "primary_kw": "power steering repair Phoenixville",
        "secondary_kws": [
            "heavy steering", "power steering service", "control arms", "tie rods", "sway bar links",
            "ball joint inspection", "ball joint replacement", "uneven tire wear", "steering vibration", "steering warning"
        ],
        "page": {
            "title": t("Power Steering Repair Phoenixville | Diverse Autoworks", "Reparación de dirección asistida en Phoenixville, PA"),
            "desc": t(
                "Power steering repair in Phoenixville, PA. Diverse Autoworks services steering systems, control arms, tie rods, sway bar links and ball joints.",
                "Dirección asistida en Phoenixville, PA: servicio y reparación, brazos de control, terminales, bieletas e inspección y cambio de rótulas."
            ),
            "h1": t("Power Steering Repair in Phoenixville, PA", "Reparación de dirección asistida en Phoenixville, PA"),
            "lead": t(
                "For power steering repair in Phoenixville, Diverse Autoworks handles steering service and repair along with control arms, tie rods, sway bar links and ball joints. Our ASE-certified technicians serve domestic and foreign gas and diesel vehicles from our Phoenixville, PA shop. If the wheel feels unusually heavy, loose or noisy, the important question is which steering or suspension component is responsible.",
                "Para reparación de dirección asistida en Phoenixville, Diverse Autoworks realiza servicio de dirección y trabajos en brazos de control, terminales de dirección, bieletas y rótulas. Nuestros técnicos certificados por ASE atienden vehículos nacionales e importados de gasolina y diésel desde Phoenixville, PA. Si el volante está pesado, tiene juego o hace ruido, lo importante es encontrar el componente responsable."
            ),
            "crumb": t("Steering components", "Componentes de dirección"),
        },
        "service_type": t("Power steering and steering components", "Dirección asistida y componentes de dirección"),
        "blocks": [
            ("h2", t("Power steering repair in Phoenixville: how steering parts work together", "Reparación de dirección asistida en Phoenixville: cómo funciona")),
            ("p", t(
                "Turning the steering wheel sets several connected parts in motion. Tie rods help transmit steering movement toward the wheels. Ball joints allow certain steering and suspension parts to move as the wheels turn and travel over the road. Control arms locate suspension components, while sway bar links connect parts of the stabilizer system. Power steering reduces the effort needed to turn the wheel. Trouble in one area can change how the whole vehicle feels to the driver.",
                "Al girar el volante, trabajan varias piezas conectadas. Las terminales de dirección transmiten el movimiento hacia las ruedas. Las rótulas permiten que determinadas piezas de suspensión y dirección se muevan al girar y pasar por irregularidades. Los brazos de control ayudan a ubicar componentes de suspensión, y las bieletas conectan partes de la barra estabilizadora. La dirección asistida reduce el esfuerzo para girar. Una falla puede alterar la sensación de manejo."
            )),
            ("p", t(
                "Steering complaints are especially important to describe precisely. Does the wheel resist turning while the vehicle is parked, or does the car wander at road speed? Is there a knock over bumps, or play at the center of the steering wheel? Those are different clues. A steering vibration can also be mistaken for a tire or wheel problem. The symptom helps direct attention to the right system instead of making assumptions based on the sound alone.",
                "Es importante describir con precisión los problemas de dirección. ¿Cuesta girar el volante al estacionar o el auto se desvía al avanzar? ¿Escucha golpes sobre baches o siente juego en el centro del volante? Son pistas distintas. Una vibración también puede confundirse con una falla de llantas o ruedas. Explicar cuándo ocurre ayuda a evaluar el sistema correcto, sin decidir por el ruido solamente."
            )),
            ("h2", t("Signs you may need steering or ball joint service", "Señales de problemas de dirección o rótulas")),
            ("ul", [
                t("The steering wheel feels unusually hard to turn or has excessive play.", "El volante cuesta mucho trabajo para girar o tiene juego excesivo."),
                t("There is a clunk or knock when turning or driving over bumps.", "Se escucha un golpe al girar o pasar sobre baches."),
                t("The vehicle wanders or requires frequent steering corrections.", "El vehículo se desvía o necesita correcciones frecuentes del volante."),
                t("Tires show uneven wear that is difficult to explain.", "Las llantas muestran desgaste desigual sin una causa clara."),
                t("A vibration or change in steering feel appears at certain speeds.", "Aparece una vibración o cambia la sensación de dirección a ciertas velocidades."),
                t("A steering warning appears, or the level of steering effort suddenly changes.", "Aparece una alerta de dirección o cambia de repente el esfuerzo para girar."),
            ]),
            ("p", t(
                "None of these signs identifies a single failed part. Loose tie rods, worn ball joints, suspension problems and power steering faults may produce overlapping complaints. The cause should be diagnosed before parts are replaced. If steering suddenly becomes difficult to control or the vehicle cannot hold its direction normally, stop in a safe place and arrange appropriate transport rather than continuing to drive.",
                "Ninguna de estas señales identifica por sí sola una pieza dañada. Terminales flojas, rótulas gastadas, fallas de suspensión y problemas de dirección asistida pueden producir síntomas parecidos. Se debe diagnosticar la causa antes de reemplazar piezas. Si pierde el control normal de la dirección, deténgase en un lugar seguro y solicite un traslado adecuado."
            )),
            ("h2", t("Steering and suspension component work we do", "Trabajos de dirección y suspensión que realizamos")),
            ("ul", [
                t("Power steering service and repair.", "Servicio y reparación de dirección asistida."),
                t("Control arms.", "Trabajos en brazos de control."),
                t("Tie rods.", "Trabajos en terminales de dirección."),
                t("Sway bar links.", "Trabajos en bieletas de la barra estabilizadora."),
                t("Ball joint inspection and replacement.", "Inspección y reemplazo de rótulas."),
            ]),
            ("h3", t("Power steering service and repair", "Servicio y reparación de dirección asistida")),
            ("p", t(
                "Power steering may provide assistance through different vehicle designs, so a complaint about heavy steering needs context. An intermittent loss of assistance is not the same as a mechanical knock from a worn linkage part. We perform power steering service and repair within the shop's confirmed scope. Tell us if the problem changes while parking, turning at low speed or moving along the road, and mention any dashboard warnings you have seen.",
                "La dirección asistida funciona de distintas maneras según el diseño del vehículo. Por eso es importante describir cuándo el volante se pone pesado. Una pérdida intermitente de asistencia no es lo mismo que un golpe mecánico de una pieza floja. Realizamos servicio y reparación de dirección asistida dentro de los trabajos confirmados del taller. Indique si la falla cambia al estacionar, girar lentamente o avanzar, y mencione las alertas del tablero."
            )),
            ("h3", t("Control arms, tie rods and sway bar links", "Brazos de control, terminales y bieletas")),
            ("p", t(
                "These pieces play related but separate roles. Tie rods connect steering motion to wheel direction. Control arms help keep the suspension located as the wheels move. Sway bar links are part of the stabilizer arrangement. An unusual noise or imprecise steering may call attention to one of them, but it takes an inspection of the actual condition to decide what needs work. Diverse Autoworks services these named components; a symptom does not justify replacing them as a set.",
                "Estas piezas trabajan juntas, pero tienen funciones distintas. Las terminales transmiten el movimiento de dirección hacia las ruedas. Los brazos de control mantienen la posición de componentes de suspensión, y las bieletas forman parte del sistema estabilizador. Un ruido o una dirección imprecisa puede relacionarse con cualquiera de ellas, pero hay que revisar su estado. Diverse Autoworks trabaja en estos componentes; un síntoma no justifica cambiarlos todos."
            )),
            ("h3", t("Ball joint inspection and replacement", "Inspección y reemplazo de rótulas")),
            ("p", t(
                "Ball joints are pivot points that accommodate wheel movement in the designs that use them. Wear can allow excess movement and affect steering or suspension behavior. Because different vehicles use different arrangements, the relevant check depends on the vehicle. Ball joint inspection and replacement are confirmed services here. A technician can explain the observed condition without turning every tire-wear or knocking complaint into an automatic ball joint replacement.",
                "Las rótulas son puntos de articulación que permiten el movimiento de las ruedas en los vehículos que las utilizan. El desgaste puede generar juego y afectar la dirección o suspensión. Como los diseños varían, también cambia la forma de revisarlas. La inspección y el reemplazo de rótulas son servicios confirmados. Un técnico puede explicar su estado sin atribuirles automáticamente cada ruido o desgaste de llantas."
            )),
            ("h2", t("Maintenance and alignment after steering concerns", "Mantenimiento y alineación ante problemas de dirección")),
            ("p", t(
                "Your owner's manual sets vehicle-specific inspection and maintenance guidance. Do not wait for a calendar interval if steering effort, directional control or noises have changed. Uneven tire wear can result from several conditions, and an alignment does not correct a worn or loose component. After addressing a steering or suspension concern, the appropriate alignment requirements depend on the vehicle and work performed. Read more about [tires and alignment](svc_tires) and [suspension repair](svc_suspension).",
                "El manual del propietario indica las revisiones y el mantenimiento propios del vehículo. No espere al siguiente servicio programado si cambian el esfuerzo del volante, el control de la dirección o los ruidos. El desgaste desigual de llantas puede tener varias causas, y una alineación no corrige una pieza gastada o floja. La necesidad de alinear después de un trabajo depende del vehículo y de la reparación. Consulte [llantas y alineación](svc_tires) y [reparación de suspensión](svc_suspension)."
            )),
            ("h2", t("Steering components and Pennsylvania safety inspections", "Dirección e inspecciones de seguridad de Pensilvania")),
            ("p", t(
                "Pennsylvania safety inspections include steering and suspension components. The state's passenger-vehicle inspection rules address steering condition, linkage security and ball joint movement, among other checks. A passing inspection and a diagnosis for a new steering symptom are not the same thing: a recent inspection does not explain a problem that appears afterward. For details on our station's service, visit [state inspections](inspections).",
                "Las inspecciones de seguridad de Pensilvania incluyen componentes de dirección y suspensión. Las reglas estatales para vehículos de pasajeros contemplan el estado de la dirección, la sujeción de las conexiones y el juego de las rótulas, entre otras revisiones. Aprobar una inspección no explica un síntoma nuevo que aparezca después. Consulte nuestra página de [inspecciones estatales](inspections) para conocer ese servicio."
            )),
            ("p", t(
                "A steering concern can change with speed, road surface and turning direction. Tell the shop if the noise occurs only over bumps, if the steering wheel stays off-center or if a warning appears at the same time. These details help separate power assistance from loose mechanical connections. A driver may feel several of those effects together, but that does not mean every linked steering component needs replacement. The individual condition of each relevant part matters.",
                "Una falla de dirección puede cambiar con la velocidad, la superficie y el sentido del giro. Indique si el ruido solo aparece sobre baches, si el volante queda descentrado o si se enciende una alerta al mismo tiempo. Eso ayuda a diferenciar un problema de asistencia de una conexión mecánica floja. Pueden presentarse varias señales juntas, pero no significa que todas las piezas de dirección deban reemplazarse. Importa el estado de cada componente."
            )),
            ("p", t(
                "For related wheel noise, see [wheel bearings and hubs](svc_bearing). Diverse Autoworks is at 1415 Pawlings Road in Phoenixville, Chester County, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge. Call the shop if you need to discuss a drop-off or after-hours arrangement.",
                "Si escucha ruidos cerca de una rueda, consulte [baleros y mazas de rueda](svc_bearing). Diverse Autoworks está en 1415 Pawlings Road, Phoenixville, Chester County, a poca distancia en auto de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge. Comuníquese con el taller para consultar arreglos de entrega fuera del horario habitual."
            )),
        ],
        "faq": [
            (t("Why is my steering wheel suddenly hard to turn?", "¿Por qué el volante se puso duro de repente?"), t("Power steering faults and other steering problems can affect effort. If you cannot control the vehicle normally, stop safely and arrange an evaluation instead of forcing the wheel.", "Una falla de dirección asistida u otro problema de dirección puede aumentar el esfuerzo. Si no controla el vehículo normalmente, deténgase en un lugar seguro y solicite una revisión.")),
            (t("Can worn tie rods cause loose steering?", "¿Las terminales de dirección desgastadas causan juego?"), t("They can contribute to unwanted movement or imprecise steering. Other steering parts can cause similar symptoms, so the condition needs to be checked.", "Sí, pueden provocar juego o una dirección imprecisa. Otras piezas causan síntomas parecidos, por lo que hay que revisarlas.")),
            (t("What does a bad ball joint sound like?", "¿Qué ruido hace una rótula desgastada?"), t("A worn ball joint can be associated with clunks or knocks over bumps, but sound alone cannot identify it. Ball joint inspection helps evaluate its condition.", "Una rótula desgastada puede producir golpes al pasar por baches, pero el sonido por sí solo no la identifica. La inspección permite evaluar su estado.")),
            (t("Do you replace control arms and sway bar links?", "¿Cambian brazos de control y bieletas?"), t("Work on control arms and sway bar links is within the shop's confirmed service scope. The appropriate work depends on the condition of the individual components.", "El taller realiza trabajos en brazos de control y bieletas de la barra estabilizadora. Lo necesario depende del estado de cada pieza.")),
            (t("Will a wheel alignment fix steering play?", "¿Una alineación elimina el juego del volante?"), t("Alignment adjusts wheel angles; it does not repair a loose steering component. A steering concern should be evaluated before assuming alignment is the solution.", "La alineación ajusta los ángulos de las ruedas; no repara una pieza de dirección floja. Primero hay que evaluar el problema.")),
            (t("Are ball joints checked during a Pennsylvania inspection?", "¿Revisan las rótulas durante la inspección de Pensilvania?"), t("Pennsylvania's passenger-vehicle safety rules include suspension and ball joint condition among the inspection criteria. The state rules determine the applicable rejection standards.", "Sí. Las reglas estatales de inspección de seguridad incluyen el estado de la suspensión y de las rótulas. La normativa determina los criterios aplicables.")),
            (t("Should I keep driving with a loose steering wheel?", "¿Puedo seguir conduciendo con juego en la dirección?"), t("Unusual steering play deserves attention, especially if the vehicle wanders or becomes difficult to control. Stop safely if you cannot steer normally.", "El juego anormal de dirección requiere atención, sobre todo si el vehículo se desvía o cuesta controlarlo. Deténgase en un lugar seguro si no puede dirigirlo normalmente.")),
        ],
        "cta": [
            ("h2", t("Schedule power steering repair near Phoenixville, PA", "Programe servicio de dirección cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule power steering repair with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Comuníquese con Diverse Autoworks para programar la reparación de dirección asistida con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": (
            "power steering repair steering service heavy hard steering power assist steering wheel play loose steering control arms tie rod tie rods sway bar links stabilizer bar ball joint inspection replacement bad ball joint steering clunk vibration tire wear alignment steerng powr stering Phoenixville Chester County",
            "dirección asistida reparación de dirección volante duro volante flojo juego de dirección brazos de control terminales de dirección bieletas barra estabilizadora rótulas revisión de rótulas cambio de rótulas golpes dirección vibración llantas desgaste desigual alineación dirrecion asistida Phoenixville Chester County"
        ),
        "sources": [
            ("PennDOT: Safety Inspection Program for Consumers", "https://www.pa.gov/agencies/dmv/faqs/motor-vehicle-faqs/safety-inspection-consumers-faqs"),
            ("Pennsylvania Code: 67 Pa. Code Section 175.80", "https://www.pacodeandbulletin.gov/secure/pacode/data/067/chapter175/s175.80.html"),
            ("Pennsylvania Code: Chapter 175, Subchapter E", "https://pacodeandbulletin.gov/secure/pacode/data/067/chapter175/chap175toc.html"),
            ("AAA: How Car Steering Works", "https://www.acg.aaa.com/connect/blogs/5c/auto/how-car-steering-works"),
            ("AAA: Potholes and Steering Components", "https://cluballiance.aaa.com/the-extra-mile/advice/car/avoid-pothole-damage-to-your-vehicle"),
        ],
        "verify": [],
    },
]