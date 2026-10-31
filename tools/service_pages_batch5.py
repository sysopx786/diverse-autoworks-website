# -*- coding: utf-8 -*-
"""Service pages batch 5: svc_electrical, svc_lights, svc_windowlock, svc_fleet. Written by Grok, 2026-10-31. Needs fact check before publishing."""


def t(en, es):
    return {"en": en, "es": es}


SERVICE_PAGES = [
    {
        "key": "svc_electrical",
        "slug": "electrical-repair",
        "covers": ["electrical", "starter"],
        "primary_kw": "electrical repair Phoenixville",
        "secondary_kws": [
            "starter replacement", "no start", "electrical diagnosis",
            "wiring", "alternator", "check engine light", "electrical short",
            "starter near me", "electrical service Phoenixville"
        ],
        "page": {
            "title": t("Electrical Repair in Phoenixville, PA | Diverse Autoworks", "Reparación eléctrica en Phoenixville, PA"),
            "desc": t("Electrical diagnosis and starter replacement by ASE-certified technicians in Phoenixville, PA.", "Diagnóstico eléctrico y reemplazo de motor de arranque por técnicos certificados por ASE en Phoenixville, PA."),
            "h1": t("Electrical Repair in Phoenixville, PA", "Reparación eléctrica en Phoenixville, PA"),
            "lead": t("Diverse Autoworks diagnoses electrical problems and replaces starters on domestic and foreign vehicles in Phoenixville. ASE-certified technicians find the failed circuit or component before any parts are replaced.", "Diverse Autoworks diagnostica problemas eléctricos y reemplaza motores de arranque en vehículos nacionales y extranjeros en Phoenixville. Los técnicos certificados por ASE encuentran el circuito o componente fallido antes de reemplazar cualquier pieza."),
            "crumb": t("Electrical repair", "Eléctrico"),
        },
        "service_type": t("Electrical diagnosis and starter replacement", "Diagnóstico eléctrico y reemplazo de motor de arranque"),
        "blocks": [
            ("h2", t("Electrical repair in Phoenixville, PA", "Reparación eléctrica en Phoenixville, PA")),
            ("p", t("A vehicle’s electrical system powers the starter, charging system, lights, computers and accessories. The starter motor turns the engine over when the key or start button is pressed. A failed starter, a weak battery, a bad connection or a wiring problem can leave the engine unable to crank. Other electrical problems can affect lights, sensors or accessories and can set a check-engine light. Diagnosis uses testing of circuits, voltage and components before any part is replaced. In Phoenixville, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge, we diagnose electrical systems and replace starters on gas and diesel vehicles.", "El sistema eléctrico de un vehículo alimenta el motor de arranque, el sistema de carga, las luces, las computadoras y los accesorios. El motor de arranque hace girar el motor cuando se presiona la llave o el botón de arranque. Un motor de arranque fallido, una batería débil, una mala conexión o un problema de cableado pueden dejar el motor sin poder girar. Otros problemas eléctricos pueden afectar las luces, los sensores o los accesorios y pueden encender una luz de revisión del motor. El diagnóstico usa pruebas de circuitos, voltaje y componentes antes de reemplazar cualquier pieza. En Phoenixville, a un corto viaje de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge, diagnosticamos sistemas eléctricos y reemplazamos motores de arranque en vehículos de gasolina y diésel.")),
            ("h2", t("Signs you need electrical or starter service", "Señales de que necesita servicio eléctrico o de arranque")),
            ("ul", [
                t("Engine does not crank when the key is turned or the start button is pressed", "El motor no gira cuando se gira la llave o se presiona el botón de arranque"),
                t("Clicking sound when trying to start", "Sonido de clic al intentar arrancar"),
                t("Intermittent no-start or electrical problems", "Problemas de no arranque o eléctricos intermitentes"),
                t("Check-engine light or other warning lights", "Luz de revisión del motor u otras luces de advertencia"),
                t("Accessories that work only some of the time", "Accesorios que funcionan solo algunas veces"),
            ]),
            ("p", t("The cause is diagnosed before parts are replaced. A no-crank condition can be the starter, the battery, a relay or a wiring problem. Testing identifies the failed component.", "Se diagnostica la causa antes de reemplazar piezas. Una condición de no giro puede ser el motor de arranque, la batería, un relé o un problema de cableado. Las pruebas identifican el componente fallido.")),
            ("h2", t("Electrical work we do", "Trabajo eléctrico que realizamos")),
            ("h3", t("Electrical diagnosis and repair", "Diagnóstico y reparación eléctrica")),
            ("p", t("We diagnose and repair electrical problems, including wiring, connections and related components.", "Diagnosticamos y reparamos problemas eléctricos, incluyendo cableado, conexiones y componentes relacionados.")),
            ("h3", t("Starter", "Motor de arranque")),
            ("p", t("We replace starters when diagnosis shows the starter is the cause of a no-crank condition.", "Reemplazamos motores de arranque cuando el diagnóstico muestra que el motor de arranque es la causa de una condición de no giro.")),
            ("ul", [
                t("Electrical diagnosis and repair", "Diagnóstico y reparación eléctrica"),
                t("Starter replacement", "Reemplazo de motor de arranque"),
            ]),
            ("p", t("If the vehicle will not start, we can arrange or accept a tow, and we offer drop-off and after-hours arrangements.", "Si el vehículo no arranca, podemos organizar o aceptar un remolque, y ofrecemos arreglos de entrega y después de horas.")),
            ("p", t("Related services include [battery service](services) and [engine repair](services). We also perform [state inspections](inspections).", "Los servicios relacionados incluyen [servicio de batería](services) y [reparación de motor](services). También realizamos [inspecciones estatales](inspections).")),
        ],
        "faq": [
            (t("What causes a no-crank condition?", "¿Qué causa una condición de no giro?"), t("A no-crank can be a failed starter, a weak battery, a bad connection, a relay or a wiring problem. Diagnosis tests the circuit so the correct component is replaced.", "Un no giro puede ser un motor de arranque fallido, una batería débil, una mala conexión, un relé o un problema de cableado. El diagnóstico prueba el circuito para que se reemplace el componente correcto.")),
            (t("Do you replace starters?", "¿Reemplazan motores de arranque?"), t("Yes. Starter replacement is part of the electrical service we perform when diagnosis confirms the starter is the cause.", "Sí. El reemplazo del motor de arranque es parte del servicio eléctrico que realizamos cuando el diagnóstico confirma que el motor de arranque es la causa.")),
            (t("Can a wiring problem cause a check-engine light?", "¿Un problema de cableado puede causar una luz de revisión del motor?"), t("Yes. Poor connections or wiring faults can set codes and turn on the check-engine light. Diagnosis tests the related circuits before any repair.", "Sí. Las malas conexiones o las fallas de cableado pueden establecer códigos y encender la luz de revisión del motor. El diagnóstico prueba los circuitos relacionados antes de cualquier reparación.")),
            (t("Is a clicking sound always a bad starter?", "¿Un sonido de clic siempre es un motor de arranque malo?"), t("Not always. A clicking sound can be a weak battery, a poor connection or a starter. Testing distinguishes among these causes.", "No siempre. Un sonido de clic puede ser una batería débil, una mala conexión o un motor de arranque. Las pruebas distinguen entre estas causas.")),
            (t("Do you diagnose intermittent electrical problems?", "¿Diagnostican problemas eléctricos intermitentes?"), t("Yes. We diagnose intermittent electrical problems by testing circuits and components under the conditions that produce the fault.", "Sí. Diagnosticamos problemas eléctricos intermitentes probando circuitos y componentes bajo las condiciones que producen la falla.")),
        ],
        "cta": [
            ("h2", t("Schedule electrical repair near Phoenixville, PA", "Programe la reparación eléctrica cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule electrical repair with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Contacte a Diverse Autoworks para programar la reparación eléctrica con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": ("electrical repair starter replacement no start no crank electrical diagnosis wiring alternator check engine light", "reparación eléctrica motor de arranque no arranque no giro diagnóstico eléctrico cableado"),
        "sources": [],
        "verify": [
            "Electrical and starter scope matches confirmed services",
            "No unconfirmed claims",
        ],
    },
    {
        "key": "svc_lights",
        "slug": "lights",
        "covers": ["lights"],
        "primary_kw": "headlight and bulb replacement Phoenixville",
        "secondary_kws": [
            "headlight repair", "bulb replacement", "taillight", "turn signal",
            "brake light", "light not working", "headlight near me",
            "bulb service Phoenixville"
        ],
        "page": {
            "title": t("Lights & Bulb Replacement in Phoenixville, PA", "Luces y bombillas en Phoenixville, PA"),
            "desc": t("Headlight, taillight and bulb replacement by ASE-certified technicians in Phoenixville, PA.", "Reemplazo de faros, luces traseras y bombillas por técnicos certificados por ASE en Phoenixville, PA."),
            "h1": t("Lights and Bulb Replacement in Phoenixville, PA", "Reemplazo de luces y bombillas en Phoenixville, PA"),
            "lead": t("Diverse Autoworks replaces headlights, taillights and other bulbs on domestic and foreign vehicles in Phoenixville. ASE-certified technicians diagnose a non-working light before any bulb or assembly is replaced.", "Diverse Autoworks reemplaza faros, luces traseras y otras bombillas en vehículos nacionales y extranjeros en Phoenixville. Los técnicos certificados por ASE diagnostican una luz que no funciona antes de reemplazar cualquier bombilla o conjunto."),
            "crumb": t("Lights", "Luces"),
        },
        "service_type": t("Light and bulb replacement", "Reemplazo de luces y bombillas"),
        "blocks": [
            ("h2", t("Lights and bulb replacement in Phoenixville, PA", "Reemplazo de luces y bombillas en Phoenixville, PA")),
            ("p", t("Vehicle lights include headlights, taillights, brake lights, turn signals and other lamps. A burned-out bulb, a failed socket, a wiring problem or a control module can leave a light dark. Pennsylvania’s safety inspection checks that required lights work and are aimed properly. A non-working headlight, brake light or turn signal can cause a vehicle to fail inspection. In Phoenixville, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge, we diagnose and replace lights and bulbs on gas and diesel vehicles.", "Las luces del vehículo incluyen faros, luces traseras, luces de freno, señales de giro y otras lámparas. Una bombilla quemada, un socket fallido, un problema de cableado o un módulo de control pueden dejar una luz apagada. La inspección de seguridad de Pensilvania verifica que las luces requeridas funcionen y estén orientadas correctamente. Un faro, una luz de freno o una señal de giro que no funciona puede hacer que un vehículo falle la inspección. En Phoenixville, a un corto viaje de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge, diagnosticamos y reemplazamos luces y bombillas en vehículos de gasolina y diésel.")),
            ("h2", t("Signs you need light service", "Señales de que necesita servicio de luces")),
            ("ul", [
                t("A headlight, taillight, brake light or turn signal does not light", "Un faro, luz trasera, luz de freno o señal de giro no se enciende"),
                t("Light is dim or flickers", "La luz está tenue o parpadea"),
                t("Moisture inside a light assembly", "Humedad dentro de un conjunto de luz"),
                t("Vehicle failed inspection for a light", "El vehículo falló la inspección por una luz"),
            ]),
            ("p", t("The cause is diagnosed before parts are replaced. A dark light can be a bulb, a socket, a fuse or a wiring problem. Testing identifies the failed part.", "Se diagnostica la causa antes de reemplazar piezas. Una luz apagada puede ser una bombilla, un socket, un fusible o un problema de cableado. Las pruebas identifican la pieza fallida.")),
            ("h2", t("Light work we do", "Trabajo de luces que realizamos")),
            ("ul", [
                t("Headlight, taillight and other bulb replacement", "Reemplazo de faros, luces traseras y otras bombillas"),
                t("Light assembly diagnosis and repair", "Diagnóstico y reparación de conjuntos de luz"),
            ]),
            ("h2", t("Lights and the Pennsylvania inspection", "Las luces y la inspección de Pensilvania")),
            ("p", t("Pennsylvania’s safety inspection checks that required lights operate and are properly aimed. See [state inspections](inspections).", "La inspección de seguridad de Pensilvania verifica que las luces requeridas funcionen y estén orientadas correctamente. Vea [inspecciones estatales](inspections).")),
            ("p", t("Related services include [electrical repair](svc_electrical) and [battery service](services). We also perform [state inspections](inspections).", "Los servicios relacionados incluyen [reparación eléctrica](svc_electrical) y [servicio de batería](services). También realizamos [inspecciones estatales](inspections).")),
        ],
        "faq": [
            (t("Why is my headlight not working?", "¿Por qué no funciona mi faro?"), t("A non-working headlight can be a burned-out bulb, a failed socket, a fuse or a wiring problem. Diagnosis tests the circuit before the bulb or assembly is replaced.", "Un faro que no funciona puede ser una bombilla quemada, un socket fallido, un fusible o un problema de cableado. El diagnóstico prueba el circuito antes de reemplazar la bombilla o el conjunto.")),
            (t("Do you replace both headlights at the same time?", "¿Reemplazan ambos faros al mismo tiempo?"), t("We replace the failed bulb or assembly after diagnosis. If both sides show similar wear, both can be replaced at the same time.", "Reemplazamos la bombilla o el conjunto fallido después del diagnóstico. Si ambos lados muestran un desgaste similar, ambos pueden reemplazarse al mismo tiempo.")),
            (t("Will a non-working light fail a Pennsylvania inspection?", "¿Una luz que no funciona fallará una inspección de Pensilvania?"), t("Yes. Pennsylvania’s safety inspection checks that required lights work. We diagnose and replace the light so the vehicle can pass. See [state inspections](inspections).", "Sí. La inspección de seguridad de Pensilvania verifica que las luces requeridas funcionen. Diagnosticamos y reemplazamos la luz para que el vehículo pueda pasar. Vea [inspecciones estatales](inspections).")),
            (t("Can moisture inside a light assembly be fixed?", "¿Se puede arreglar la humedad dentro de un conjunto de luz?"), t("Moisture can indicate a seal problem. Diagnosis checks the assembly; the bulb or the assembly is replaced when testing shows it is needed.", "La humedad puede indicar un problema de sello. El diagnóstico verifica el conjunto; la bombilla o el conjunto se reemplaza cuando las pruebas muestran que se necesita.")),
            (t("Do you service LED and halogen lights?", "¿Atienden luces LED y halógenas?"), t("Yes. We diagnose and replace lights on vehicles that use halogen, LED or other bulb types after confirming the correct part for the vehicle.", "Sí. Diagnosticamos y reemplazamos luces en vehículos que usan halógenas, LED u otros tipos de bombillas después de confirmar la pieza correcta para el vehículo.")),
        ],
        "cta": [
            ("h2", t("Schedule light service near Phoenixville, PA", "Programe el servicio de luces cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule light service with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Contacte a Diverse Autoworks para programar el servicio de luces con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": ("headlight repair bulb replacement taillight turn signal brake light light not working", "reparación de faro reemplazo de bombilla luz trasera señal de giro luz de freno luz que no funciona"),
        "sources": [],
        "verify": [
            "Lights scope matches confirmed service",
            "No unconfirmed claims",
        ],
    },
    {
        "key": "svc_windowlock",
        "slug": "power-windows-locks",
        "covers": ["window", "lock"],
        "primary_kw": "power window repair Phoenixville",
        "secondary_kws": [
            "power lock", "window regulator", "door lock", "window not working",
            "lock actuator", "power window near me", "door lock repair Phoenixville"
        ],
        "page": {
            "title": t("Power Windows & Locks in Phoenixville, PA", "Ventanas y cerraduras eléctricas en Phoenixville, PA"),
            "desc": t("Power window and power lock repair by ASE-certified technicians in Phoenixville, PA.", "Reparación de ventanas y cerraduras eléctricas por técnicos certificados por ASE en Phoenixville, PA."),
            "h1": t("Power Windows and Locks in Phoenixville, PA", "Ventanas y cerraduras eléctricas en Phoenixville, PA"),
            "lead": t("Diverse Autoworks diagnoses and repairs power windows and power locks on domestic and foreign vehicles in Phoenixville. ASE-certified technicians find the failed regulator, motor or actuator before any parts are replaced.", "Diverse Autoworks diagnostica y repara ventanas y cerraduras eléctricas en vehículos nacionales y extranjeros en Phoenixville. Los técnicos certificados por ASE encuentran el regulador, motor o actuador fallido antes de reemplazar cualquier pieza."),
            "crumb": t("Power windows & locks", "Ventanas y cerraduras"),
        },
        "service_type": t("Power window and lock repair", "Reparación de ventanas y cerraduras eléctricas"),
        "blocks": [
            ("h2", t("Power window and lock repair in Phoenixville, PA", "Reparación de ventanas y cerraduras eléctricas en Phoenixville, PA")),
            ("p", t("Power windows use a motor and regulator to raise and lower the glass. Power locks use an actuator to lock and unlock the doors. When a regulator breaks, a motor fails or an actuator stops working, the window or lock may not operate. Diagnosis tests the switch, the motor or actuator, and the wiring before any part is replaced. In Phoenixville, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge, we repair power windows and power locks on gas and diesel vehicles.", "Las ventanas eléctricas usan un motor y un regulador para subir y bajar el vidrio. Las cerraduras eléctricas usan un actuador para bloquear y desbloquear las puertas. Cuando un regulador se rompe, un motor falla o un actuador deja de funcionar, la ventana o la cerradura puede no operar. El diagnóstico prueba el interruptor, el motor o actuador y el cableado antes de reemplazar cualquier pieza. En Phoenixville, a un corto viaje de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge, reparamos ventanas y cerraduras eléctricas en vehículos de gasolina y diésel.")),
            ("h2", t("Signs you need window or lock repair", "Señales de que necesita reparación de ventana o cerradura")),
            ("ul", [
                t("Window does not go up or down", "La ventana no sube ni baja"),
                t("Window moves slowly or only part way", "La ventana se mueve lentamente o solo parcialmente"),
                t("Door lock does not lock or unlock", "La cerradura de la puerta no bloquea ni desbloquea"),
                t("Clicking or grinding from the door when the switch is pressed", "Clic o rechinido de la puerta cuando se presiona el interruptor"),
            ]),
            ("p", t("The cause is diagnosed before parts are replaced. A non-working window can be the switch, the motor, the regulator or the wiring. Testing identifies the failed component.", "Se diagnostica la causa antes de reemplazar piezas. Una ventana que no funciona puede ser el interruptor, el motor, el regulador o el cableado. Las pruebas identifican el componente fallido.")),
            ("h2", t("Window and lock work we do", "Trabajo de ventanas y cerraduras que realizamos")),
            ("ul", [
                t("Power window repair", "Reparación de ventanas eléctricas"),
                t("Power lock repair", "Reparación de cerraduras eléctricas"),
            ]),
            ("p", t("We replace the failed regulator, motor or actuator after diagnosis confirms it is the source of the problem.", "Reemplazamos el regulador, motor o actuador fallido después de que el diagnóstico confirma que es la fuente del problema.")),
            ("p", t("Related services include [electrical repair](svc_electrical). We also perform [state inspections](inspections).", "Los servicios relacionados incluyen [reparación eléctrica](svc_electrical). También realizamos [inspecciones estatales](inspections).")),
        ],
        "faq": [
            (t("Why won’t my power window go up?", "¿Por qué no sube mi ventana eléctrica?"), t("A non-working power window can be a failed motor, a broken regulator, a bad switch or a wiring problem. Diagnosis tests these components before any part is replaced.", "Una ventana eléctrica que no funciona puede ser un motor fallido, un regulador roto, un interruptor malo o un problema de cableado. El diagnóstico prueba estos componentes antes de reemplazar cualquier pieza.")),
            (t("Do you repair power locks?", "¿Reparan cerraduras eléctricas?"), t("Yes. Power lock repair, including actuator replacement when diagnosis confirms it is needed, is part of the service we offer.", "Sí. La reparación de cerraduras eléctricas, incluyendo el reemplazo del actuador cuando el diagnóstico confirma que se necesita, es parte del servicio que ofrecemos.")),
            (t("Can a window regulator be replaced without replacing the motor?", "¿Se puede reemplazar un regulador de ventana sin reemplazar el motor?"), t("It depends on the vehicle and the condition of the parts. Diagnosis determines which components need replacement.", "Depende del vehículo y la condición de las piezas. El diagnóstico determina qué componentes necesitan reemplazo.")),
            (t("Is a slow window a sign of a failing regulator?", "¿Una ventana lenta es una señal de un regulador fallando?"), t("A slow window can be a worn regulator, a weak motor or a binding track. Diagnosis identifies the cause before parts are replaced.", "Una ventana lenta puede ser un regulador desgastado, un motor débil o una guía que se atasca. El diagnóstico identifica la causa antes de reemplazar piezas.")),
            (t("Do you work on both front and rear windows?", "¿Trabajan en ventanas delanteras y traseras?"), t("Yes. We diagnose and repair power windows on all doors after confirming the failed component.", "Sí. Diagnosticamos y reparamos ventanas eléctricas en todas las puertas después de confirmar el componente fallido.")),
        ],
        "cta": [
            ("h2", t("Schedule power window or lock repair near Phoenixville, PA", "Programe la reparación de ventana o cerradura eléctrica cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule power window or lock repair with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Contacte a Diverse Autoworks para programar la reparación de ventana o cerradura eléctrica con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": ("power window repair power lock window regulator door lock actuator window not working", "reparación de ventana eléctrica cerradura eléctrica regulador de ventana actuador de cerradura ventana que no funciona"),
        "sources": [],
        "verify": [
            "Power window and lock scope matches confirmed services",
            "No unconfirmed claims",
        ],
    },
    {
        "key": "svc_fleet",
        "slug": "fleet-and-fleet-wash",
        "covers": ["fleet", "fleetwash"],
        "primary_kw": "fleet repair Phoenixville PA",
        "secondary_kws": [
            "fleet service", "fleet wash", "commercial vehicles",
            "fleet maintenance", "fleet near me", "fleet service Phoenixville"
        ],
        "page": {
            "title": t("Fleet Repair & Wash in Phoenixville, PA", "Flota y lavado de flota en Phoenixville, PA"),
            "desc": t("Fleet repair and fleet wash for commercial vehicles by ASE-certified technicians in Phoenixville, PA.", "Reparación de flota y lavado de flota para vehículos comerciales por técnicos certificados por ASE en Phoenixville, PA."),
            "h1": t("Fleet Repair and Wash in Phoenixville, PA", "Reparación y lavado de flota en Phoenixville, PA"),
            "lead": t("Diverse Autoworks provides fleet repair and fleet wash for commercial vehicles in Phoenixville. ASE-certified technicians perform the mechanical work; fleet wash is available as a separate service.", "Diverse Autoworks proporciona reparación de flota y lavado de flota para vehículos comerciales en Phoenixville. Los técnicos certificados por ASE realizan el trabajo mecánico; el lavado de flota está disponible como un servicio separado."),
            "crumb": t("Fleet repair", "Flota"),
        },
        "service_type": t("Fleet repair and fleet wash", "Reparación de flota y lavado de flota"),
        "blocks": [
            ("h2", t("Fleet repair and wash in Phoenixville, PA", "Reparación y lavado de flota en Phoenixville, PA")),
            ("p", t("Fleet vehicles need regular mechanical service to stay on the road. Diverse Autoworks performs fleet repair on commercial vehicles, covering the mechanical services listed on this site. Fleet wash is a separate service that cleans the exterior of fleet vehicles. In Phoenixville, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge, we work with businesses that need ongoing vehicle service.", "Los vehículos de flota necesitan servicio mecánico regular para permanecer en la carretera. Diverse Autoworks realiza reparación de flota en vehículos comerciales, cubriendo los servicios mecánicos listados en este sitio. El lavado de flota es un servicio separado que limpia el exterior de los vehículos de flota. En Phoenixville, a un corto viaje de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge, trabajamos con negocios que necesitan servicio de vehículos continuo.")),
            ("h2", t("Fleet services we offer", "Servicios de flota que ofrecemos")),
            ("ul", [
                t("Fleet repair for commercial vehicles", "Reparación de flota para vehículos comerciales"),
                t("Fleet wash", "Lavado de flota"),
            ]),
            ("p", t("Fleet repair includes the mechanical services available on this site. Contact us to discuss the vehicles and the work needed.", "La reparación de flota incluye los servicios mecánicos disponibles en este sitio. Contáctenos para discutir los vehículos y el trabajo necesario.")),
            ("p", t("Related services include the individual repair pages on this site. We also perform [state inspections](inspections).", "Los servicios relacionados incluyen las páginas de reparación individuales en este sitio. También realizamos [inspecciones estatales](inspections).")),
        ],
        "faq": [
            (t("Do you service commercial fleets?", "¿Atienden flotas comerciales?"), t("Yes. Fleet repair for commercial vehicles is part of the service we offer. Contact us to discuss your vehicles.", "Sí. La reparación de flota para vehículos comerciales es parte del servicio que ofrecemos. Contáctenos para discutir sus vehículos.")),
            (t("Is fleet wash included with repair?", "¿El lavado de flota está incluido con la reparación?"), t("Fleet wash is a separate service. It can be scheduled with repair or on its own.", "El lavado de flota es un servicio separado. Puede programarse con la reparación o por sí solo.")),
            (t("What mechanical work is available for fleets?", "¿Qué trabajo mecánico está disponible para flotas?"), t("Fleet repair covers the mechanical services listed on this site. Contact us with the vehicle details and the work needed.", "La reparación de flota cubre los servicios mecánicos listados en este sitio. Contáctenos con los detalles del vehículo y el trabajo necesario.")),
            (t("Do you work with local businesses?", "¿Trabajan con negocios locales?"), t("Yes. We work with businesses in Phoenixville and the surrounding area that need fleet service.", "Sí. Trabajamos con negocios en Phoenixville y el área circundante que necesitan servicio de flota.")),
            (t("How do I schedule fleet service?", "¿Cómo programo el servicio de flota?"), t("Contact Diverse Autoworks to discuss your vehicles and schedule. Send us a message or [request an appointment](contact#request) online.", "Contacte a Diverse Autoworks para discutir sus vehículos y programar. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "cta": [
            ("h2", t("Schedule fleet service near Phoenixville, PA", "Programe el servicio de flota cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule fleet repair or fleet wash. Send us a message or [request an appointment](contact#request) online.", "Contacte a Diverse Autoworks para programar la reparación de flota o el lavado de flota. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": ("fleet repair fleet wash commercial vehicles fleet maintenance fleet service Phoenixville", "reparación de flota lavado de flota vehículos comerciales mantenimiento de flota"),
        "sources": [],
        "verify": [
            "Fleet and fleet-wash scope matches confirmed services",
            "No unconfirmed claims",
        ],
    },
]
