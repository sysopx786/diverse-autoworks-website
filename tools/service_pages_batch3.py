# -*- coding: utf-8 -*-
"""Service pages batch 3: svc_exhaust, svc_emissions, svc_brakes, svc_tires. Written by Grok, 2026-10-31. Needs fact check before publishing."""


def t(en, es):
    return {"en": en, "es": es}


SERVICE_PAGES = [
    {
        "key": "svc_exhaust",
        "slug": "exhaust-muffler-repair",
        "covers": ["exhaust"],
        "primary_kw": "muffler and exhaust repair Phoenixville",
        "secondary_kws": [
            "exhaust leak", "muffler replacement", "catalytic converter",
            "exhaust noise", "loud exhaust", "exhaust pipe", "exhaust repair near me",
            "catalytic converter replacement Phoenixville"
        ],
        "page": {
            "title": t("Exhaust & Muffler Repair in Phoenixville, PA", "Escape y silenciador en Phoenixville, PA"),
            "desc": t("Exhaust inspection, muffler and catalytic converter replacement by ASE-certified technicians in Phoenixville, PA.", "Inspección de escape, reemplazo de silenciador y convertidor catalítico por técnicos certificados por ASE en Phoenixville, PA."),
            "h1": t("Exhaust and Muffler Repair in Phoenixville, PA", "Reparación de escape y silenciador en Phoenixville, PA"),
            "lead": t("Diverse Autoworks inspects and repairs exhaust systems and replaces mufflers and catalytic converters on domestic and foreign vehicles in Phoenixville. ASE-certified technicians diagnose leaks and noise before parts are replaced.", "Diverse Autoworks inspecciona y repara sistemas de escape y reemplaza silenciadores y convertidores catalíticos en vehículos nacionales y extranjeros en Phoenixville. Los técnicos certificados por ASE diagnostican fugas y ruido antes de reemplazar piezas."),
            "crumb": t("Exhaust repair", "Escape"),
        },
        "service_type": t("Exhaust inspection and muffler replacement", "Inspección de escape y reemplazo de silenciador"),
        "blocks": [
            ("h2", t("Exhaust and muffler repair in Phoenixville, PA", "Reparación de escape y silenciador en Phoenixville, PA")),
            ("p", t("The exhaust system carries combustion gases from the engine to the rear of the vehicle. It includes the manifold, pipes, catalytic converter, muffler and hangers. A leak can let exhaust gases enter the passenger area and can cause a loud noise. The catalytic converter reduces harmful emissions. The muffler quiets the exhaust. Pennsylvania's safety inspection checks the exhaust system for leaks, holes, loose joints, a missing or externally repaired muffler, and proper discharge past the body. In Phoenixville, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge, we diagnose and repair these systems.", "El sistema de escape lleva los gases de combustión del motor a la parte trasera del vehículo. Incluye el múltiple, las tuberías, el convertidor catalítico, el silenciador y los soportes. Una fuga puede dejar que los gases de escape entren en el área de pasajeros y puede causar un ruido fuerte. El convertidor catalítico reduce las emisiones dañinas. El silenciador silencia el escape. La inspección de seguridad de Pensilvania verifica el sistema de escape en busca de fugas, agujeros, uniones sueltas, un silenciador faltante o reparado externamente, y una descarga adecuada más allá de la carrocería. En Phoenixville, a un corto viaje de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge, diagnosticamos y reparamos estos sistemas.")),
            ("h2", t("Signs you need exhaust repair", "Señales de que necesita reparación de escape")),
            ("ul", [
                t("Loud rumbling or hissing from under the vehicle", "Retumbo fuerte o siseo desde debajo del vehículo"),
                t("Exhaust smell inside the cabin", "Olor a escape dentro de la cabina"),
                t("Rattling or hanging exhaust components", "Componentes de escape que cascabelean o cuelgan"),
                t("Check-engine light related to the catalytic converter or oxygen sensors", "Luz de revisión del motor relacionada con el convertidor catalítico o los sensores de oxígeno"),
                t("Visible rust holes or broken hangers", "Agujeros de óxido visibles o soportes rotos"),
            ]),
            ("p", t("The cause is diagnosed before parts are replaced. A noise or smell is traced to the leaking joint, the muffler, or the catalytic converter before any part is ordered.", "Se diagnostica la causa antes de reemplazar piezas. Un ruido o un olor se rastrea hasta la unión que fuga, el silenciador o el convertidor catalítico antes de ordenar cualquier pieza.")),
            ("h2", t("Exhaust work we do", "Trabajo de escape que realizamos")),
            ("ul", [
                t("Exhaust inspection and diagnosis", "Inspección y diagnóstico de escape"),
                t("Exhaust parts, mufflers and catalytic converter replacement", "Piezas de escape, silenciadores y reemplazo de convertidor catalítico"),
            ]),
            ("h2", t("Exhaust and the Pennsylvania inspection", "El escape y la inspección de Pensilvania")),
            ("p", t("Pennsylvania's safety inspection includes the exhaust system. Under 67 Pa. Code, the system must be free of leaks, holes and loose joints; the muffler must be present and free of external repair; and exhaust must not enter the passenger area. See [state inspections](inspections).", "La inspección de seguridad de Pensilvania incluye el sistema de escape. Bajo el Código de Pensilvania 67, el sistema debe estar libre de fugas, agujeros y uniones sueltas; el silenciador debe estar presente y libre de reparación externa; y el escape no debe entrar en el área de pasajeros. Vea [inspecciones estatales](inspections).")),
            ("p", t("Related services include [emissions repair](svc_emissions) and [engine repair](services). We also perform [state inspections](inspections).", "Los servicios relacionados incluyen [reparación de emisiones](svc_emissions) y [reparación de motor](services). También realizamos [inspecciones estatales](inspections).")),
        ],
        "faq": [
            (t("What causes a loud exhaust?", "¿Qué causa un escape ruidoso?"), t("A hole in the muffler or pipe, a broken hanger, or a leaking joint can make the exhaust louder. Diagnosis finds the failed part before it is replaced.", "Un agujero en el silenciador o la tubería, un soporte roto o una unión que fuga pueden hacer que el escape sea más ruidoso. El diagnóstico encuentra la pieza fallida antes de reemplazarla.")),
            (t("Do you replace catalytic converters?", "¿Reemplazan convertidores catalíticos?"), t("Yes. Catalytic converter replacement is part of the exhaust work we perform after diagnosis confirms it is needed.", "Sí. El reemplazo del convertidor catalítico es parte del trabajo de escape que realizamos después de que el diagnóstico confirma que se necesita.")),
            (t("Will an exhaust leak fail a Pennsylvania inspection?", "¿Una fuga de escape fallará una inspección de Pensilvania?"), t("Yes. Pennsylvania's safety inspection checks for exhaust leaks, holes, loose joints and a properly functioning muffler. We diagnose and repair the system so the vehicle can pass. See [state inspections](inspections).", "Sí. La inspección de seguridad de Pensilvania verifica fugas de escape, agujeros, uniones sueltas y un silenciador que funcione correctamente. Diagnosticamos y reparamos el sistema para que el vehículo pueda pasar. Vea [inspecciones estatales](inspections).")),
            (t("Can a catalytic converter cause a check-engine light?", "¿Un convertidor catalítico puede causar una luz de revisión del motor?"), t("Yes. A failing catalytic converter or related oxygen sensors can set a check-engine light. Diagnosis reads the codes and tests the system before parts are replaced.", "Sí. Un convertidor catalítico fallando o sensores de oxígeno relacionados pueden encender una luz de revisión del motor. El diagnóstico lee los códigos y prueba el sistema antes de reemplazar piezas.")),
            (t("Is exhaust noise always a muffler problem?", "¿El ruido del escape siempre es un problema del silenciador?"), t("Not always. A leak at a joint, a hole in a pipe, or a broken hanger can also cause noise. Diagnosis identifies the source.", "No siempre. Una fuga en una unión, un agujero en una tubería o un soporte roto también pueden causar ruido. El diagnóstico identifica la fuente.")),
        ],
        "cta": [
            ("h2", t("Schedule exhaust repair near Phoenixville, PA", "Programe la reparación de escape cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule exhaust repair with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Contacte a Diverse Autoworks para programar la reparación de escape con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": ("exhaust repair muffler catalytic converter exhaust leak loud exhaust exhaust pipe exhaust noise", "reparación de escape silenciador convertidor catalítico fuga de escape escape ruidoso"),
        "sources": [
            ("67 Pa. Code § 175.75 – Exhaust systems", "https://parules.elaws.us/pacode/title67_parti_subparta_articlevii_chapter175_subchaptere_section175.75"),
        ],
        "verify": [
            "Exhaust scope matches confirmed service",
            "PA inspection statement matches 67 Pa. Code",
        ],
    },
    {
        "key": "svc_emissions",
        "slug": "emissions-repair",
        "covers": ["emissioncontrol", "o2sensor"],
        "primary_kw": "failed emissions test repair Chester County PA",
        "secondary_kws": [
            "oxygen sensor", "check engine light", "emissions repair",
            "catalytic converter", "OBD", "Drive Clean PA", "emissions test Phoenixville",
            "failed emissions Chester County"
        ],
        "page": {
            "title": t("Emissions Repair in Phoenixville, PA | Diverse Autoworks", "Reparación de emisiones en Phoenixville, PA"),
            "desc": t("Emission-control repairs and oxygen sensor diagnosis after a failed emissions test by ASE-certified technicians in Phoenixville, PA.", "Reparaciones de emisiones y sensores de oxígeno por técnicos ASE en Phoenixville, PA."),
            "h1": t("Emissions Repair in Phoenixville, PA", "Reparación de emisiones en Phoenixville, PA"),
            "lead": t("Diverse Autoworks diagnoses and repairs emission-control systems and oxygen sensors on domestic and foreign vehicles in Phoenixville. ASE-certified technicians work on vehicles that have failed the Chester County emissions test.", "Diverse Autoworks diagnostica y repara sistemas de control de emisiones y sensores de oxígeno en vehículos nacionales y extranjeros en Phoenixville. Los técnicos certificados por ASE trabajan en vehículos que han fallado la prueba de emisiones del condado de Chester."),
            "crumb": t("Emissions repair", "Emisiones"),
        },
        "service_type": t("Emission-control and oxygen sensor repair", "Reparación de control de emisiones y sensor de oxígeno"),
        "blocks": [
            ("h2", t("Emissions repair in Phoenixville, PA", "Reparación de emisiones en Phoenixville, PA")),
            ("p", t("Emission-control systems reduce the pollutants that leave the tailpipe. Oxygen sensors measure the oxygen in the exhaust and help the computer adjust the fuel mixture. A failed sensor or other emission-control component can set a check-engine light and cause a vehicle to fail the emissions test. Chester and Montgomery counties are in Pennsylvania's Philadelphia-area emissions region. Gas and hybrid vehicles of 9,000 lb GVWR or less need the emissions test; diesels, heavier gas vehicles and fully electric vehicles do not. In Phoenixville, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge, we diagnose and repair these systems after a failed test.", "Los sistemas de control de emisiones reducen los contaminantes que salen del tubo de escape. Los sensores de oxígeno miden el oxígeno en el escape y ayudan a la computadora a ajustar la mezcla de combustible. Un sensor fallido u otro componente de control de emisiones puede encender una luz de revisión del motor y hacer que un vehículo falle la prueba de emisiones. Los condados de Chester y Montgomery están en la región de emisiones del área de Filadelfia de Pensilvania. Los vehículos de gasolina e híbridos de 9,000 lb de GVWR o menos necesitan la prueba de emisiones; los diésel, los vehículos de gasolina más pesados y los vehículos completamente eléctricos no. En Phoenixville, a un corto viaje de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge, diagnosticamos y reparamos estos sistemas después de una prueba fallida.")),
            ("h2", t("Signs you need emissions repair", "Señales de que necesita reparación de emisiones")),
            ("ul", [
                t("Check-engine light is on", "La luz de revisión del motor está encendida"),
                t("Vehicle failed the emissions test", "El vehículo falló la prueba de emisiones"),
                t("Rough idle or poor fuel economy", "Ralentí irregular o mala economía de combustible"),
                t("Oxygen sensor codes or catalytic converter codes", "Códigos de sensor de oxígeno o códigos de convertidor catalítico"),
            ]),
            ("p", t("The cause is diagnosed before parts are replaced. Codes are read and the related sensors and systems are tested so that only the failed component is replaced.", "Se diagnostica la causa antes de reemplazar piezas. Se leen los códigos y se prueban los sensores y sistemas relacionados para que solo se reemplace el componente fallido.")),
            ("h2", t("Emissions work we do", "Trabajo de emisiones que realizamos")),
            ("h3", t("Emission-control repairs", "Reparaciones de control de emisiones")),
            ("p", t("We repair emission-control systems, including work after a failed emissions test.", "Reparamos sistemas de control de emisiones, incluyendo trabajo después de una prueba de emisiones fallida.")),
            ("h3", t("Oxygen sensors", "Sensores de oxígeno")),
            ("p", t("We diagnose and replace oxygen sensors when testing shows they have failed.", "Diagnosticamos y reemplazamos sensores de oxígeno cuando las pruebas muestran que han fallado.")),
            ("ul", [
                t("Emission-control repairs, including after a failed emissions test", "Reparaciones de control de emisiones, incluyendo después de una prueba de emisiones fallida"),
                t("Oxygen sensor diagnosis and replacement", "Diagnóstico y reemplazo de sensor de oxígeno"),
            ]),
            ("p", t("Related services include [exhaust repair](svc_exhaust) and [engine repair](services). We also perform [state inspections](inspections).", "Los servicios relacionados incluyen [reparación de escape](svc_exhaust) y [reparación de motor](services). También realizamos [inspecciones estatales](inspections).")),
        ],
        "faq": [
            (t("What happens if my car fails the emissions test?", "¿Qué pasa si mi auto falla la prueba de emisiones?"), t("The test report lists the codes or reasons for the failure. We diagnose the emission-control system and oxygen sensors and repair the failed components so the vehicle can be retested.", "El informe de la prueba lista los códigos o las razones de la falla. Diagnosticamos el sistema de control de emisiones y los sensores de oxígeno y reparamos los componentes fallidos para que el vehículo pueda ser reprobado.")),
            (t("Do Chester County vehicles need an emissions test?", "¿Los vehículos del condado de Chester necesitan una prueba de emisiones?"), t("Yes. Chester and Montgomery counties are in the Philadelphia-area emissions region. Gas and hybrid vehicles of 9,000 lb GVWR or less need the test. Diesels, heavier gas vehicles and fully electric vehicles do not.", "Sí. Los condados de Chester y Montgomery están en la región de emisiones del área de Filadelfia. Los vehículos de gasolina e híbridos de 9,000 lb de GVWR o menos necesitan la prueba. Los diésel, los vehículos de gasolina más pesados y los vehículos completamente eléctricos no.")),
            (t("Can an oxygen sensor cause a check-engine light?", "¿Un sensor de oxígeno puede causar una luz de revisión del motor?"), t("Yes. A failed oxygen sensor is a common cause of a check-engine light and can contribute to an emissions failure. Diagnosis confirms the sensor before it is replaced.", "Sí. Un sensor de oxígeno fallido es una causa común de una luz de revisión del motor y puede contribuir a una falla de emisiones. El diagnóstico confirma el sensor antes de reemplazarlo.")),
            (t("Do you repair vehicles after a failed emissions test?", "¿Reparan vehículos después de una prueba de emisiones fallida?"), t("Yes. Emission-control repairs after a failed test, including oxygen sensor work, are part of the service we offer.", "Sí. Las reparaciones de control de emisiones después de una prueba fallida, incluyendo trabajo de sensor de oxígeno, son parte del servicio que ofrecemos.")),
            (t("Is a check-engine light always an emissions problem?", "¿Una luz de revisión del motor siempre es un problema de emisiones?"), t("Not always. The light can come on for many reasons. Diagnosis reads the codes and tests the related systems to find the actual cause.", "No siempre. La luz puede encenderse por muchas razones. El diagnóstico lee los códigos y prueba los sistemas relacionados para encontrar la causa real.")),
        ],
        "cta": [
            ("h2", t("Schedule emissions repair near Phoenixville, PA", "Programe la reparación de emisiones cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule emissions repair with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Contacte a Diverse Autoworks para programar la reparación de emisiones con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": ("emissions repair failed emissions test oxygen sensor check engine light Drive Clean PA Chester County OBD catalytic converter", "reparación de emisiones prueba de emisiones fallida sensor de oxígeno luz de revisión del motor"),
        "sources": [
            ("Drive Clean PA – official site", "http://www.drivecleanpa.state.pa.us/"),
        ],
        "verify": [
            "Emissions region and vehicle rules match section 1 facts",
            "Oxygen sensor and emission-control scope matches confirmed services",
        ],
    },
    {
        "key": "svc_brakes",
        "slug": "brake-repair",
        "covers": ["brakes", "brakefluid"],
        "primary_kw": "brake repair Phoenixville PA",
        "secondary_kws": [
            "brake pads", "rotors", "grinding brakes", "squeaking brakes",
            "brake fluid flush", "brake pedal soft", "brake repair near me",
            "brake service Phoenixville"
        ],
        "page": {
            "title": t("Brake Repair in Phoenixville, PA | Diverse Autoworks", "Reparación de frenos en Phoenixville, PA"),
            "desc": t("Brake and rotor service plus brake fluid flush by ASE-certified technicians in Phoenixville, PA.", "Servicio de frenos y rotores más cambio de líquido de frenos por técnicos certificados por ASE en Phoenixville, PA."),
            "h1": t("Brake Repair in Phoenixville, PA", "Reparación de frenos en Phoenixville, PA"),
            "lead": t("Diverse Autoworks performs brake and rotor service and brake fluid flushes on domestic and foreign vehicles in Phoenixville. ASE-certified technicians diagnose noise, vibration and soft pedal before parts are replaced.", "Diverse Autoworks realiza servicio de frenos y rotores y cambios de líquido de frenos en vehículos nacionales y extranjeros en Phoenixville. Los técnicos certificados por ASE diagnostican ruido, vibración y pedal suave antes de reemplazar piezas."),
            "crumb": t("Brake repair", "Frenos"),
        },
        "service_type": t("Brake and rotor service", "Servicio de frenos y rotores"),
        "blocks": [
            ("h2", t("Brake repair in Phoenixville, PA", "Reparación de frenos en Phoenixville, PA")),
            ("p", t("The brake system slows and stops the vehicle. Pads (or shoes) press against rotors (or drums) to create friction. Brake fluid transmits the force from the pedal to the calipers or wheel cylinders. When pads wear thin they can grind. Warped rotors can cause a pulsating pedal. Brake fluid absorbs moisture over time, which can lower its boiling point and contribute to a soft pedal. Pennsylvania's safety inspection checks brake lining thickness, rotors, lines and pedal operation. In Phoenixville, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge, we service brakes on gas and diesel vehicles.", "El sistema de frenos desacelera y detiene el vehículo. Las pastillas (o zapatas) presionan contra los rotores (o tambores) para crear fricción. El líquido de frenos transmite la fuerza del pedal a las pinzas o los cilindros de rueda. Cuando las pastillas se desgastan pueden rechinar. Los rotores deformados pueden causar un pedal pulsante. El líquido de frenos absorbe humedad con el tiempo, lo que puede bajar su punto de ebullición y contribuir a un pedal suave. La inspección de seguridad de Pensilvania verifica el grosor del revestimiento de frenos, los rotores, las líneas y la operación del pedal. En Phoenixville, a un corto viaje de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge, atendemos frenos en vehículos de gasolina y diésel.")),
            ("h2", t("Signs you need brake repair", "Señales de que necesita reparación de frenos")),
            ("ul", [
                t("Grinding or squealing when braking", "Rechinido o chirrido al frenar"),
                t("Pulsating or vibrating brake pedal", "Pedal de freno pulsante o vibrante"),
                t("Soft or spongy pedal", "Pedal suave o esponjoso"),
                t("Vehicle pulls to one side when braking", "El vehículo se jala hacia un lado al frenar"),
                t("Brake warning light on", "Luz de advertencia de frenos encendida"),
            ]),
            ("p", t("The cause is diagnosed before parts are replaced. Grinding can be worn pads; pulsation can be rotors; a soft pedal can be fluid or air in the system. Testing identifies the failed component.", "Se diagnostica la causa antes de reemplazar piezas. El rechinido puede ser pastillas desgastadas; la pulsación puede ser rotores; un pedal suave puede ser fluido o aire en el sistema. Las pruebas identifican el componente fallido.")),
            ("h2", t("Brake work we do", "Trabajo de frenos que realizamos")),
            ("h3", t("Brakes and rotors", "Frenos y rotores")),
            ("p", t("We perform brake and rotor service, replacing pads and resurfacing or replacing rotors as diagnosis requires.", "Realizamos servicio de frenos y rotores, reemplazando pastillas y rectificando o reemplazando rotores según requiera el diagnóstico.")),
            ("h3", t("Brake fluid", "Líquido de frenos")),
            ("p", t("We flush and replace brake fluid. Your owner's manual lists any recommended interval; many manufacturers call for periodic replacement because the fluid absorbs moisture.", "Cambiamos y reemplazamos el líquido de frenos. Su manual del propietario indica cualquier intervalo recomendado; muchos fabricantes piden reemplazo periódico porque el fluido absorbe humedad.")),
            ("ul", [
                t("Brake and rotor service", "Servicio de frenos y rotores"),
                t("Brake fluid flush and replacement", "Cambio y reemplazo de líquido de frenos"),
            ]),
            ("h2", t("Brakes and the Pennsylvania inspection", "Los frenos y la inspección de Pensilvania")),
            ("p", t("Pennsylvania's safety inspection checks brake lining thickness, rotor condition, lines, hoses and pedal operation. See [state inspections](inspections).", "La inspección de seguridad de Pensilvania verifica el grosor del revestimiento de frenos, la condición de los rotores, las líneas, las mangueras y la operación del pedal. Vea [inspecciones estatales](inspections).")),
            ("p", t("If the brakes cannot be driven safely, we can arrange or accept a tow, and we offer drop-off and after-hours arrangements.", "Si los frenos no pueden conducirse de forma segura, podemos organizar o aceptar un remolque, y ofrecemos arreglos de entrega y después de horas.")),
            ("p", t("Related services include [suspension repair](svc_suspension) and [wheel bearing replacement](svc_bearing). We also perform [state inspections](inspections).", "Los servicios relacionados incluyen [reparación de suspensión](svc_suspension) y [reemplazo de balero de rueda](svc_bearing). También realizamos [inspecciones estatales](inspections).")),
        ],
        "faq": [
            (t("What causes grinding brakes?", "¿Qué causa el rechinido de frenos?"), t("Grinding is often worn brake pads that have worn through to the metal. Diagnosis confirms the pad and rotor condition before parts are replaced.", "El rechinido a menudo son pastillas de freno desgastadas que se han desgastado hasta el metal. El diagnóstico confirma la condición de la pastilla y el rotor antes de reemplazar piezas.")),
            (t("How often should brake fluid be changed?", "¿Con qué frecuencia se debe cambiar el líquido de frenos?"), t("Follow the interval in your owner's manual. Brake fluid absorbs moisture over time, which can lower its boiling point. We flush and replace the fluid when it is due or when diagnosis shows it is needed.", "Siga el intervalo de su manual del propietario. El líquido de frenos absorbe humedad con el tiempo, lo que puede bajar su punto de ebullición. Cambiamos y reemplazamos el fluido cuando corresponde o cuando el diagnóstico muestra que se necesita.")),
            (t("Do you resurface rotors?", "¿Rectifican rotores?"), t("We perform brake and rotor service. Rotors are resurfaced or replaced according to their condition after diagnosis.", "Realizamos servicio de frenos y rotores. Los rotores se rectifican o se reemplazan según su condición después del diagnóstico.")),
            (t("Will worn brakes fail a Pennsylvania inspection?", "¿Los frenos desgastados fallarán una inspección de Pensilvania?"), t("Yes. Pennsylvania's safety inspection checks brake lining thickness and other brake components. We diagnose and repair the system so the vehicle can pass. See [state inspections](inspections).", "Sí. La inspección de seguridad de Pensilvania verifica el grosor del revestimiento de frenos y otros componentes de frenos. Diagnosticamos y reparamos el sistema para que el vehículo pueda pasar. Vea [inspecciones estatales](inspections).")),
            (t("What does a soft brake pedal mean?", "¿Qué significa un pedal de freno suave?"), t("A soft or spongy pedal can be caused by air in the system, moisture-contaminated fluid, or a leak. Diagnosis identifies the cause before fluid is flushed or parts are replaced.", "Un pedal suave o esponjoso puede ser causado por aire en el sistema, fluido contaminado con humedad o una fuga. El diagnóstico identifica la causa antes de que se cambie el fluido o se reemplacen piezas.")),
        ],
        "cta": [
            ("h2", t("Schedule brake repair near Phoenixville, PA", "Programe la reparación de frenos cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule brake repair with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Contacte a Diverse Autoworks para programar la reparación de frenos con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": ("brake repair brake pads rotors grinding brakes squeaking brakes brake fluid flush soft pedal", "reparación de frenos pastillas de freno rotores frenos que rechinan chirrido de frenos cambio de líquido de frenos"),
        "sources": [],
        "verify": [
            "Brake and brake-fluid scope matches confirmed services",
            "No unconfirmed interval claims; owner’s manual is the reference",
        ],
    },
    {
        "key": "svc_tires",
        "slug": "tires-alignment",
        "covers": ["tires", "rotation", "wheels", "retreads"],
        "primary_kw": "tires and wheel alignment Phoenixville",
        "secondary_kws": [
            "tire rotation", "wheel balancing", "tire repair", "wheel repair",
            "retreads", "uneven tire wear", "alignment near me", "tire service Phoenixville",
            "tire pressure"
        ],
        "page": {
            "title": t("Tires & Wheel Alignment in Phoenixville, PA", "Llantas y alineación en Phoenixville, PA"),
            "desc": t("Tires, tire repairs, wheel alignments, rotation, balancing, wheel repair and retreads by ASE-certified technicians in Phoenixville, PA.", "Llantas, reparaciones de llantas, alineaciones, rotación, balanceo, reparación de ruedas y recauchutados por técnicos certificados por ASE en Phoenixville, PA."),
            "h1": t("Tires and Wheel Alignment in Phoenixville, PA", "Llantas y alineación en Phoenixville, PA"),
            "lead": t("Diverse Autoworks mounts and repairs tires, performs wheel alignments, rotates and balances tires, and repairs or replaces wheels on domestic and foreign vehicles in Phoenixville. ASE-certified technicians also service retreads.", "Diverse Autoworks monta y repara llantas, realiza alineaciones de ruedas, rota y balancea llantas, y repara o reemplaza ruedas en vehículos nacionales y extranjeros en Phoenixville. Los técnicos certificados por ASE también atienden recauchutados."),
            "crumb": t("Tires & alignment", "Llantas y alineación"),
        },
        "service_type": t("Tires, alignment and wheel service", "Llantas, alineación y servicio de ruedas"),
        "blocks": [
            ("h2", t("Tires and wheel alignment in Phoenixville, PA", "Llantas y alineación en Phoenixville, PA")),
            ("p", t("Tires are the only contact between the vehicle and the road. Proper inflation, tread depth and alignment affect stopping distance, handling and tire life. Wheel alignment sets the angles of the wheels so the tires wear evenly and the vehicle tracks straight. Rotation moves tires to different positions so they wear more evenly. Balancing reduces vibration. Wheels (rims) can be repaired or replaced when they are bent or damaged. Retreads are tires that have had new tread applied. Pennsylvania's safety inspection checks tread depth (minimum 2/32 inch) and tire condition. In Phoenixville, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge, we service tires and wheels on gas and diesel vehicles.", "Las llantas son el único contacto entre el vehículo y la carretera. La inflación adecuada, la profundidad de la banda de rodadura y la alineación afectan la distancia de frenado, el manejo y la vida de la llanta. La alineación de ruedas establece los ángulos de las ruedas para que las llantas se desgasten de manera uniforme y el vehículo se desplace en línea recta. La rotación mueve las llantas a diferentes posiciones para que se desgasten de manera más uniforme. El balanceo reduce la vibración. Las ruedas (rines) pueden repararse o reemplazarse cuando están dobladas o dañadas. Los recauchutados son llantas a las que se les ha aplicado una nueva banda de rodadura. La inspección de seguridad de Pensilvania verifica la profundidad de la banda de rodadura (mínimo 2/32 de pulgada) y la condición de la llanta. En Phoenixville, a un corto viaje de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge, atendemos llantas y ruedas en vehículos de gasolina y diésel.")),
            ("h2", t("Signs you need tire or alignment service", "Señales de que necesita servicio de llantas o alineación")),
            ("ul", [
                t("Uneven or rapid tire wear", "Desgaste desigual o rápido de las llantas"),
                t("Vehicle pulls to one side", "El vehículo se jala hacia un lado"),
                t("Steering wheel is off-center when driving straight", "El volante está descentrado al conducir en línea recta"),
                t("Vibration at highway speeds", "Vibración a velocidades de carretera"),
                t("Visible damage, bulges or low tread", "Daño visible, bultos o banda de rodadura baja"),
            ]),
            ("p", t("The cause is diagnosed before parts are replaced. Uneven wear can be alignment or inflation; vibration can be balance or a damaged wheel. Inspection identifies the needed service.", "Se diagnostica la causa antes de reemplazar piezas. El desgaste desigual puede ser alineación o inflación; la vibración puede ser balanceo o una rueda dañada. La inspección identifica el servicio necesario.")),
            ("h2", t("Tire and wheel work we do", "Trabajo de llantas y ruedas que realizamos")),
            ("ul", [
                t("Tires and tire repairs", "Llantas y reparaciones de llantas"),
                t("Wheel alignments", "Alineaciones de ruedas"),
                t("Tire rotation and balancing", "Rotación y balanceo de llantas"),
                t("Wheel (rim) repair and replacement", "Reparación y reemplazo de rueda (rin)"),
                t("Tire retreads", "Recauchutados de llantas"),
            ]),
            ("h2", t("Tires and the Pennsylvania inspection", "Las llantas y la inspección de Pensilvania")),
            ("p", t("Pennsylvania's safety inspection requires a minimum of 2/32 inch of tread and checks for damage, bulges and proper mounting. See [state inspections](inspections).", "La inspección de seguridad de Pensilvania requiere un mínimo de 2/32 de pulgada de banda de rodadura y verifica daños, bultos y montaje adecuado. Vea [inspecciones estatales](inspections).")),
            ("p", t("Related services include [suspension repair](svc_suspension) and [brake repair](svc_brakes). We also perform [state inspections](inspections).", "Los servicios relacionados incluyen [reparación de suspensión](svc_suspension) y [reparación de frenos](svc_brakes). También realizamos [inspecciones estatales](inspections).")),
        ],
        "faq": [
            (t("How often should tires be rotated?", "¿Con qué frecuencia se deben rotar las llantas?"), t("Follow the interval in your owner's manual. Rotation helps tires wear more evenly. We perform tire rotation and balancing as part of the tire service we offer.", "Siga el intervalo de su manual del propietario. La rotación ayuda a que las llantas se desgasten de manera más uniforme. Realizamos rotación y balanceo de llantas como parte del servicio de llantas que ofrecemos.")),
            (t("What causes a vehicle to pull to one side?", "¿Qué causa que un vehículo se jale hacia un lado?"), t("Pulling can be caused by alignment, uneven tire pressure, or a worn suspension component. Diagnosis checks tires, alignment and related parts before any adjustment or repair.", "El jalón puede ser causado por alineación, presión de llantas desigual o un componente de suspensión desgastado. El diagnóstico verifica llantas, alineación y piezas relacionadas antes de cualquier ajuste o reparación.")),
            (t("Do you repair wheels?", "¿Reparan ruedas?"), t("Yes. Wheel (rim) repair and replacement is part of the service we offer when a wheel is bent or damaged.", "Sí. La reparación y el reemplazo de rueda (rin) es parte del servicio que ofrecemos cuando una rueda está doblada o dañada.")),
            (t("What is a tire retread?", "¿Qué es un recauchutado de llanta?"), t("A retread is a tire that has had new tread applied to a sound casing. We service retreads as part of the tire work we perform.", "Un recauchutado es una llanta a la que se le ha aplicado una nueva banda de rodadura a una carcasa en buen estado. Atendemos recauchutados como parte del trabajo de llantas que realizamos.")),
            (t("Will low tread fail a Pennsylvania inspection?", "¿Una banda de rodadura baja fallará una inspección de Pensilvania?"), t("Yes. Pennsylvania requires a minimum of 2/32 inch of tread. We inspect tires and can replace them so the vehicle can pass. See [state inspections](inspections).", "Sí. Pensilvania requiere un mínimo de 2/32 de pulgada de banda de rodadura. Inspeccionamos las llantas y podemos reemplazarlas para que el vehículo pueda pasar. Vea [inspecciones estatales](inspections).")),
        ],
        "cta": [
            ("h2", t("Schedule tire or alignment service near Phoenixville, PA", "Programe el servicio de llantas o alineación cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule tire or alignment service with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Contacte a Diverse Autoworks para programar el servicio de llantas o alineación con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": ("tires wheel alignment tire rotation balancing tire repair wheel repair retreads uneven wear alignment Phoenixville", "llantas alineación rotación de llantas balanceo reparación de llantas reparación de rueda recauchutado"),
        "sources": [],
        "verify": [
            "Tire, alignment, rotation, wheel and retread scope matches confirmed services",
            "2/32-inch tread statement is standard PA inspection knowledge; confirm against current PennDOT text if needed",
        ],
    },
]
