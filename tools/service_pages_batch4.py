# -*- coding: utf-8 -*-
"""Service pages batch 4: svc_suspension, svc_bearing, svc_climate, svc_cooling. Written by Grok, 2026-10-31. Needs fact check before publishing."""


def t(en, es):
    return {"en": en, "es": es}


SERVICE_PAGES = [
    {
        "key": "svc_suspension",
        "slug": "suspension-repair",
        "covers": ["suspension"],
        "primary_kw": "suspension repair Phoenixville",
        "secondary_kws": [
            "struts", "shocks", "control arm", "ball joint", "sway bar",
            "bouncing ride", "uneven tire wear", "clunking noise",
            "suspension near me", "suspension service Phoenixville"
        ],
        "page": {
            "title": t("Suspension Repair in Phoenixville, PA | Diverse Autoworks", "Reparación de suspensión en Phoenixville, PA"),
            "desc": t("Suspension repair by ASE-certified technicians for domestic and foreign vehicles in Phoenixville, PA.", "Reparación de suspensión por técnicos certificados por ASE para vehículos nacionales y extranjeros en Phoenixville, PA."),
            "h1": t("Suspension Repair in Phoenixville, PA", "Reparación de suspensión en Phoenixville, PA"),
            "lead": t("Diverse Autoworks diagnoses and repairs suspension systems on domestic and foreign vehicles in Phoenixville. ASE-certified technicians find the worn component before any parts are replaced.", "Diverse Autoworks diagnostica y repara sistemas de suspensión en vehículos nacionales y extranjeros en Phoenixville. Los técnicos certificados por ASE encuentran el componente desgastado antes de reemplazar cualquier pieza."),
            "crumb": t("Suspension repair", "Suspensión"),
        },
        "service_type": t("Suspension repair", "Reparación de suspensión"),
        "blocks": [
            ("h2", t("Suspension repair in Phoenixville, PA", "Reparación de suspensión en Phoenixville, PA")),
            ("p", t("The suspension system controls how the wheels move relative to the body. It includes springs, struts or shocks, control arms, ball joints, bushings and sway bars. These parts keep the tires in contact with the road, absorb bumps and help the vehicle handle predictably. When a strut, ball joint or bushing wears, the ride can become bouncy, the vehicle can pull or wander, and tires can wear unevenly. A clunk over bumps is a common sign of a worn joint or mount. Pennsylvania's safety inspection checks suspension components for looseness and damage. In Phoenixville, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge, we diagnose and repair these systems on gas and diesel vehicles.", "El sistema de suspensión controla cómo se mueven las ruedas en relación con la carrocería. Incluye resortes, amortiguadores o struts, brazos de control, rótulas, bujes y barras estabilizadoras. Estas piezas mantienen las llantas en contacto con la carretera, absorben baches y ayudan a que el vehículo se maneje de manera predecible. Cuando un strut, una rótula o un buje se desgasta, el viaje puede volverse rebotante, el vehículo puede jalarse o desviarse, y las llantas pueden desgastarse de manera desigual. Un golpeteo sobre baches es una señal común de una junta o un montaje desgastado. La inspección de seguridad de Pensilvania verifica los componentes de suspensión en busca de holgura y daño. En Phoenixville, a un corto viaje de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge, diagnosticamos y reparamos estos sistemas en vehículos de gasolina y diésel.")),
            ("h2", t("Signs you need suspension repair", "Señales de que necesita reparación de suspensión")),
            ("ul", [
                t("Bouncy or harsh ride", "Viaje rebotante o áspero"),
                t("Vehicle pulls or wanders on a straight road", "El vehículo se jala o se desvía en una carretera recta"),
                t("Clunking or rattling over bumps", "Golpeteo o cascabeleo sobre baches"),
                t("Uneven tire wear", "Desgaste desigual de las llantas"),
                t("Nose dive or body roll that feels excessive", "Hundimiento de la nariz o balanceo de la carrocería que se siente excesivo"),
            ]),
            ("p", t("The cause is diagnosed before parts are replaced. A clunk can be a ball joint, a control-arm bushing or a strut mount. Inspection and a road test identify the worn component.", "Se diagnostica la causa antes de reemplazar piezas. Un golpeteo puede ser una rótula, un buje del brazo de control o un montaje del strut. La inspección y una prueba de manejo identifican el componente desgastado.")),
            ("h2", t("Suspension work we do", "Trabajo de suspensión que realizamos")),
            ("ul", [
                t("Suspension repair", "Reparación de suspensión"),
            ]),
            ("p", t("We repair worn or damaged suspension components after diagnosis confirms which part has failed.", "Reparamos componentes de suspensión desgastados o dañados después de que el diagnóstico confirma qué pieza ha fallado.")),
            ("p", t("Related services include [tires and alignment](svc_tires) and [wheel bearing replacement](svc_bearing). We also perform [state inspections](inspections).", "Los servicios relacionados incluyen [llantas y alineación](svc_tires) y [reemplazo de balero de rueda](svc_bearing). También realizamos [inspecciones estatales](inspections).")),
        ],
        "faq": [
            (t("What causes a clunking noise over bumps?", "¿Qué causa un ruido de golpeteo sobre baches?"), t("A clunk over bumps is often a worn ball joint, control-arm bushing or strut mount. Diagnosis identifies the component before it is replaced.", "Un golpeteo sobre baches a menudo es una rótula desgastada, un buje del brazo de control o un montaje del strut. El diagnóstico identifica el componente antes de reemplazarlo.")),
            (t("Can worn suspension cause uneven tire wear?", "¿Una suspensión desgastada puede causar desgaste desigual de las llantas?"), t("Yes. Worn suspension parts can change wheel alignment and cause tires to wear unevenly. Diagnosis checks both the suspension and the alignment.", "Sí. Las piezas de suspensión desgastadas pueden cambiar la alineación de las ruedas y hacer que las llantas se desgasten de manera desigual. El diagnóstico verifica tanto la suspensión como la alineación.")),
            (t("Do you repair struts and control arms?", "¿Reparan struts y brazos de control?"), t("Yes. Suspension repair covers the components that diagnosis shows are worn, including struts, shocks, control arms and related parts.", "Sí. La reparación de suspensión cubre los componentes que el diagnóstico muestra que están desgastados, incluyendo struts, amortiguadores, brazos de control y piezas relacionadas.")),
            (t("Will a suspension problem fail a Pennsylvania inspection?", "¿Un problema de suspensión fallará una inspección de Pensilvania?"), t("Pennsylvania's safety inspection checks suspension components for looseness and damage. We diagnose and repair the system so the vehicle can pass. See [state inspections](inspections).", "La inspección de seguridad de Pensilvania verifica los componentes de suspensión en busca de holgura y daño. Diagnosticamos y reparamos el sistema para que el vehículo pueda pasar. Vea [inspecciones estatales](inspections).")),
            (t("Is a bouncy ride always bad shocks?", "¿Un viaje rebotante siempre son amortiguadores malos?"), t("Not always. A bouncy ride can come from worn shocks or struts, but other suspension parts can contribute. Diagnosis finds the worn component.", "No siempre. Un viaje rebotante puede provenir de amortiguadores o struts desgastados, pero otras piezas de suspensión pueden contribuir. El diagnóstico encuentra el componente desgastado.")),
        ],
        "cta": [
            ("h2", t("Schedule suspension repair near Phoenixville, PA", "Programe la reparación de suspensión cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule suspension repair with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Contacte a Diverse Autoworks para programar la reparación de suspensión con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": ("suspension repair struts shocks control arm ball joint clunking noise uneven tire wear bouncing ride", "reparación de suspensión struts amortiguadores brazo de control rótula golpeteo desgaste desigual de llantas"),
        "sources": [],
        "verify": [
            "Suspension scope matches confirmed service",
            "No unconfirmed claims",
        ],
    },
    {
        "key": "svc_bearing",
        "slug": "wheel-bearings",
        "covers": ["bearing"],
        "primary_kw": "wheel bearing replacement Phoenixville",
        "secondary_kws": [
            "wheel bearing noise", "humming bearing", "ABS light",
            "hub bearing", "wheel bearing near me", "bearing noise when turning",
            "wheel bearing service Phoenixville"
        ],
        "page": {
            "title": t("Wheel Bearing Replacement in Phoenixville, PA", "Baleros de rueda en Phoenixville, PA"),
            "desc": t("Wheel bearing diagnosis and replacement by ASE-certified technicians in Phoenixville, PA.", "Diagnóstico y reemplazo de balero de rueda por técnicos certificados por ASE en Phoenixville, PA."),
            "h1": t("Wheel Bearing Replacement in Phoenixville, PA", "Reemplazo de balero de rueda en Phoenixville, PA"),
            "lead": t("Diverse Autoworks diagnoses and replaces wheel bearings on domestic and foreign vehicles in Phoenixville. ASE-certified technicians confirm the noisy or worn bearing before any parts are replaced.", "Diverse Autoworks diagnostica y reemplaza baleros de rueda en vehículos nacionales y extranjeros en Phoenixville. Los técnicos certificados por ASE confirman el balero ruidoso o desgastado antes de reemplazar cualquier pieza."),
            "crumb": t("Wheel bearings", "Baleros de rueda"),
        },
        "service_type": t("Wheel bearing replacement", "Reemplazo de balero de rueda"),
        "blocks": [
            ("h2", t("Wheel bearing replacement in Phoenixville, PA", "Reemplazo de balero de rueda en Phoenixville, PA")),
            ("p", t("Wheel bearings let the wheels turn smoothly while supporting the weight of the vehicle. Most modern vehicles use a sealed hub-bearing assembly. When a bearing wears it can produce a humming, growling or grinding noise that changes with vehicle speed or when the vehicle turns. A failed bearing can also affect the ABS sensor and set a warning light. Pennsylvania's safety inspection checks for excessive play in the wheel bearings. In Phoenixville, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge, we diagnose and replace wheel bearings on gas and diesel vehicles.", "Los baleros de rueda permiten que las ruedas giren suavemente mientras soportan el peso del vehículo. La mayoría de los vehículos modernos usan un conjunto de balero de cubo sellado. Cuando un balero se desgasta puede producir un zumbido, un gruñido o un rechinido que cambia con la velocidad del vehículo o cuando el vehículo gira. Un balero fallido también puede afectar el sensor del ABS y encender una luz de advertencia. La inspección de seguridad de Pensilvania verifica el juego excesivo en los baleros de rueda. En Phoenixville, a un corto viaje de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge, diagnosticamos y reemplazamos baleros de rueda en vehículos de gasolina y diésel.")),
            ("h2", t("Signs you need a wheel bearing", "Señales de que necesita un balero de rueda")),
            ("ul", [
                t("Humming, growling or grinding that changes with speed", "Zumbido, gruñido o rechinido que cambia con la velocidad"),
                t("Noise that gets louder or quieter when turning", "Ruido que se hace más fuerte o más suave al girar"),
                t("ABS warning light", "Luz de advertencia del ABS"),
                t("Vibration that increases with speed", "Vibración que aumenta con la velocidad"),
                t("Excessive play when the wheel is rocked by hand", "Juego excesivo cuando la rueda se balancea a mano"),
            ]),
            ("p", t("The cause is diagnosed before parts are replaced. A road test and inspection identify which bearing is noisy or has play. Other components that can make similar noises are checked as well.", "Se diagnostica la causa antes de reemplazar piezas. Una prueba de manejo y la inspección identifican qué balero está ruidoso o tiene juego. También se verifican otros componentes que pueden hacer ruidos similares.")),
            ("h2", t("Wheel bearing work we do", "Trabajo de balero de rueda que realizamos")),
            ("ul", [
                t("Wheel bearing diagnosis and replacement", "Diagnóstico y reemplazo de balero de rueda"),
            ]),
            ("p", t("We replace the worn or failed wheel bearing after diagnosis confirms it is the source of the noise or play.", "Reemplazamos el balero de rueda desgastado o fallido después de que el diagnóstico confirma que es la fuente del ruido o el juego.")),
            ("p", t("Related services include [suspension repair](svc_suspension) and [brake repair](svc_brakes). We also perform [state inspections](inspections).", "Los servicios relacionados incluyen [reparación de suspensión](svc_suspension) y [reparación de frenos](svc_brakes). También realizamos [inspecciones estatales](inspections).")),
        ],
        "faq": [
            (t("What does a bad wheel bearing sound like?", "¿Cómo suena un balero de rueda malo?"), t("A worn wheel bearing often produces a humming, growling or grinding noise that changes with vehicle speed or when the vehicle turns. Diagnosis confirms the bearing before it is replaced.", "Un balero de rueda desgastado a menudo produce un zumbido, un gruñido o un rechinido que cambia con la velocidad del vehículo o cuando el vehículo gira. El diagnóstico confirma el balero antes de reemplazarlo.")),
            (t("Can a wheel bearing cause an ABS light?", "¿Un balero de rueda puede causar una luz del ABS?"), t("Yes. Many wheel-bearing assemblies include the ABS sensor. A failed bearing can set an ABS warning light. Diagnosis checks both the bearing and the sensor.", "Sí. Muchos conjuntos de balero de rueda incluyen el sensor del ABS. Un balero fallido puede encender una luz de advertencia del ABS. El diagnóstico verifica tanto el balero como el sensor.")),
            (t("Do you replace the whole hub or just the bearing?", "¿Reemplazan todo el cubo o solo el balero?"), t("Most modern vehicles use a sealed hub-bearing assembly that is replaced as a unit. Diagnosis confirms the design of your vehicle and the condition of the bearing.", "La mayoría de los vehículos modernos usan un conjunto de balero de cubo sellado que se reemplaza como una unidad. El diagnóstico confirma el diseño de su vehículo y la condición del balero.")),
            (t("Will a noisy wheel bearing fail a Pennsylvania inspection?", "¿Un balero de rueda ruidoso fallará una inspección de Pensilvania?"), t("Pennsylvania's safety inspection checks for excessive play in the wheel bearings. We diagnose and replace the bearing so the vehicle can pass. See [state inspections](inspections).", "La inspección de seguridad de Pensilvania verifica el juego excesivo en los baleros de rueda. Diagnosticamos y reemplazamos el balero para que el vehículo pueda pasar. Vea [inspecciones estatales](inspections).")),
            (t("Is wheel bearing noise the same as a tire noise?", "¿El ruido del balero de rueda es lo mismo que el ruido de una llanta?"), t("No. A road test and inspection distinguish bearing noise from tire noise or other driveline sounds. Diagnosis identifies the source before any part is replaced.", "No. Una prueba de manejo y la inspección distinguen el ruido del balero del ruido de la llanta u otros sonidos del tren motriz. El diagnóstico identifica la fuente antes de reemplazar cualquier pieza.")),
        ],
        "cta": [
            ("h2", t("Schedule wheel bearing replacement near Phoenixville, PA", "Programe el reemplazo de balero de rueda cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule wheel bearing replacement with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Contacte a Diverse Autoworks para programar el reemplazo de balero de rueda con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": ("wheel bearing replacement humming growling grinding ABS light hub bearing wheel bearing noise", "balero de rueda reemplazo zumbido gruñido rechinido luz ABS cubo de balero"),
        "sources": [],
        "verify": [
            "Wheel bearing scope matches confirmed service",
            "No unconfirmed claims",
        ],
    },
    {
        "key": "svc_climate",
        "slug": "ac-and-heating",
        "covers": ["ac", "heating"],
        "primary_kw": "AC repair Phoenixville PA",
        "secondary_kws": [
            "air conditioning recharge", "heater not working", "no heat",
            "AC not cold", "blower motor", "heater core", "climate control",
            "AC service near me", "heating repair Phoenixville"
        ],
        "page": {
            "title": t("A/C & Heating Repair in Phoenixville, PA", "Aire acondicionado y calefacción en Phoenixville, PA"),
            "desc": t("Air conditioning and heating system repair by ASE-certified technicians in Phoenixville, PA.", "Reparación de sistemas de aire acondicionado y calefacción por técnicos certificados por ASE en Phoenixville, PA."),
            "h1": t("A/C and Heating Repair in Phoenixville, PA", "Reparación de aire acondicionado y calefacción en Phoenixville, PA"),
            "lead": t("Diverse Autoworks diagnoses and repairs air conditioning and heating systems on domestic and foreign vehicles in Phoenixville. ASE-certified technicians find the cause of no cold air or no heat before any parts are replaced.", "Diverse Autoworks diagnostica y repara sistemas de aire acondicionado y calefacción en vehículos nacionales y extranjeros en Phoenixville. Los técnicos certificados por ASE encuentran la causa de la falta de aire frío o la falta de calor antes de reemplazar cualquier pieza."),
            "crumb": t("A/C & heating", "A/C y calefacción"),
        },
        "service_type": t("Air conditioning and heating repair", "Reparación de aire acondicionado y calefacción"),
        "blocks": [
            ("h2", t("A/C and heating repair in Phoenixville, PA", "Reparación de aire acondicionado y calefacción en Phoenixville, PA")),
            ("p", t("The air conditioning system cools and dehumidifies the air that enters the cabin. It uses a compressor, condenser, evaporator, expansion device and refrigerant. When the system is low on refrigerant, the compressor is failing, or a control component has failed, the air may not get cold. The heating system uses engine coolant flowing through the heater core to warm the air. A low coolant level, a restricted heater core, or a blend-door problem can mean little or no heat. Diagnosis checks refrigerant pressure, coolant flow and controls before any parts are replaced. In Phoenixville, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge, we service both A/C and heating systems on gas and diesel vehicles.", "El sistema de aire acondicionado enfría y deshumidifica el aire que entra en la cabina. Usa un compresor, un condensador, un evaporador, un dispositivo de expansión y refrigerante. Cuando el sistema tiene poco refrigerante, el compresor está fallando o un componente de control ha fallado, el aire puede no enfriarse. El sistema de calefacción usa el refrigerante del motor que fluye a través del núcleo del calentador para calentar el aire. Un nivel bajo de refrigerante, un núcleo del calentador restringido o un problema de la puerta de mezcla pueden significar poco o ningún calor. El diagnóstico verifica la presión del refrigerante, el flujo de refrigerante y los controles antes de reemplazar cualquier pieza. En Phoenixville, a un corto viaje de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge, atendemos tanto sistemas de A/C como de calefacción en vehículos de gasolina y diésel.")),
            ("h2", t("Signs you need A/C or heating repair", "Señales de que necesita reparación de A/C o calefacción")),
            ("ul", [
                t("Air conditioning does not get cold", "El aire acondicionado no enfría"),
                t("Little or no heat from the vents", "Poco o ningún calor de las ventilaciones"),
                t("Unusual smells from the vents", "Olores inusuales de las ventilaciones"),
                t("Weak airflow from the vents", "Flujo de aire débil de las ventilaciones"),
                t("A/C compressor cycles on and off rapidly", "El compresor del A/C se enciende y apaga rápidamente"),
            ]),
            ("p", t("The cause is diagnosed before parts are replaced. Low refrigerant, a failed compressor clutch, a blend door, or a coolant-flow problem can produce similar symptoms. Testing identifies the failed component.", "Se diagnostica la causa antes de reemplazar piezas. Bajo refrigerante, un embrague de compresor fallido, una puerta de mezcla o un problema de flujo de refrigerante pueden producir síntomas similares. Las pruebas identifican el componente fallido.")),
            ("h2", t("A/C and heating work we do", "Trabajo de A/C y calefacción que realizamos")),
            ("h3", t("Air conditioning", "Aire acondicionado")),
            ("p", t("We diagnose and repair air conditioning systems, including refrigerant-related service when the system is low or has a leak.", "Diagnosticamos y reparamos sistemas de aire acondicionado, incluyendo servicio relacionado con refrigerante cuando el sistema está bajo o tiene una fuga.")),
            ("h3", t("Heating", "Calefacción")),
            ("p", t("We diagnose and repair heating systems, including coolant flow and heater-core related problems.", "Diagnosticamos y reparamos sistemas de calefacción, incluyendo problemas relacionados con el flujo de refrigerante y el núcleo del calentador.")),
            ("ul", [
                t("Air conditioning repair", "Reparación de aire acondicionado"),
                t("Heating system repair", "Reparación del sistema de calefacción"),
            ]),
            ("p", t("Related services include [cooling system service](svc_cooling) and [engine repair](services). We also perform [state inspections](inspections).", "Los servicios relacionados incluyen [servicio del sistema de enfriamiento](svc_cooling) y [reparación de motor](services). También realizamos [inspecciones estatales](inspections).")),
        ],
        "faq": [
            (t("Why is my A/C not cold?", "¿Por qué mi A/C no enfría?"), t("The system can be low on refrigerant, the compressor may not be engaging, or a control component may have failed. Diagnosis checks pressures and operation before any repair is made.", "El sistema puede tener poco refrigerante, el compresor puede no estar enganchando, o un componente de control puede haber fallado. El diagnóstico verifica las presiones y la operación antes de realizar cualquier reparación.")),
            (t("Why is there no heat?", "¿Por qué no hay calor?"), t("No heat can be caused by low coolant, a restricted heater core, a blend-door problem, or an engine that is not reaching operating temperature. Diagnosis finds the cause.", "La falta de calor puede ser causada por bajo refrigerante, un núcleo del calentador restringido, un problema de la puerta de mezcla, o un motor que no alcanza la temperatura de operación. El diagnóstico encuentra la causa.")),
            (t("Do you recharge air conditioning systems?", "¿Recargan sistemas de aire acondicionado?"), t("We diagnose the air conditioning system first. If the system is low on refrigerant and the cause has been identified, refrigerant service is performed as part of the repair.", "Diagnosticamos el sistema de aire acondicionado primero. Si el sistema tiene poco refrigerante y la causa ha sido identificada, el servicio de refrigerante se realiza como parte de la reparación.")),
            (t("Can a cooling system problem affect the heater?", "¿Un problema del sistema de enfriamiento puede afectar el calentador?"), t("Yes. The heater uses engine coolant. Low coolant or a cooling-system problem can reduce heat. We check coolant level and flow as part of heating diagnosis.", "Sí. El calentador usa refrigerante del motor. Bajo refrigerante o un problema del sistema de enfriamiento puede reducir el calor. Verificamos el nivel y el flujo de refrigerante como parte del diagnóstico de calefacción.")),
            (t("Is weak airflow an A/C problem?", "¿El flujo de aire débil es un problema del A/C?"), t("Weak airflow can be a cabin filter, a blower motor, or a duct problem rather than a refrigerant issue. Diagnosis checks airflow and controls separately from cooling performance.", "El flujo de aire débil puede ser un filtro de cabina, un motor del soplador o un problema de conductos en lugar de un problema de refrigerante. El diagnóstico verifica el flujo de aire y los controles por separado del rendimiento de enfriamiento.")),
        ],
        "cta": [
            ("h2", t("Schedule A/C or heating repair near Phoenixville, PA", "Programe la reparación de A/C o calefacción cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule A/C or heating repair with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Contacte a Diverse Autoworks para programar la reparación de A/C o calefacción con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": ("AC repair air conditioning heating no heat no cold air heater core blower motor climate control", "reparación de A/C aire acondicionado calefacción sin calor sin aire frío núcleo del calentador motor del soplador"),
        "sources": [],
        "verify": [
            "A/C and heating scope matches confirmed services",
            "No unconfirmed claims",
        ],
    },
    {
        "key": "svc_cooling",
        "slug": "cooling-system",
        "covers": ["cooling", "waterpump"],
        "primary_kw": "cooling system repair Phoenixville",
        "secondary_kws": [
            "overheating", "radiator", "water pump", "thermostat",
            "coolant leak", "hose", "cooling system flush", "engine overheating",
            "water pump replacement Phoenixville"
        ],
        "page": {
            "title": t("Cooling System Repair in Phoenixville, PA", "Sistema de enfriamiento en Phoenixville, PA"),
            "desc": t("Cooling system service and water pump replacement by ASE-certified technicians in Phoenixville, PA.", "Servicio del sistema de enfriamiento y reemplazo de bomba de agua por técnicos certificados por ASE en Phoenixville, PA."),
            "h1": t("Cooling System Repair in Phoenixville, PA", "Reparación del sistema de enfriamiento en Phoenixville, PA"),
            "lead": t("Diverse Autoworks diagnoses and services cooling systems and replaces water pumps on domestic and foreign engines in Phoenixville. ASE-certified technicians find the cause of overheating or a coolant leak before any parts are replaced.", "Diverse Autoworks diagnostica y atiende sistemas de enfriamiento y reemplaza bombas de agua en motores nacionales y extranjeros en Phoenixville. Los técnicos certificados por ASE encuentran la causa del sobrecalentamiento o una fuga de refrigerante antes de reemplazar cualquier pieza."),
            "crumb": t("Cooling system", "Sistema de enfriamiento"),
        },
        "service_type": t("Cooling system and water pump service", "Servicio de sistema de enfriamiento y bomba de agua"),
        "blocks": [
            ("h2", t("Cooling system repair in Phoenixville, PA", "Reparación del sistema de enfriamiento en Phoenixville, PA")),
            ("p", t("The cooling system keeps the engine at a safe operating temperature. Coolant circulates through the engine, radiator, hoses, thermostat and water pump. The water pump moves the coolant; the thermostat controls when coolant flows to the radiator; the radiator transfers heat to the air. A low coolant level, a failed water pump, a stuck thermostat, a leaking hose or a clogged radiator can cause the engine to overheat. Overheating can damage the engine. Diagnosis checks coolant level, pressure, temperature and component condition before any parts are replaced. In Phoenixville, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge, we service cooling systems on gas and diesel engines.", "El sistema de enfriamiento mantiene el motor a una temperatura de operación segura. El refrigerante circula a través del motor, el radiador, las mangueras, el termostato y la bomba de agua. La bomba de agua mueve el refrigerante; el termostato controla cuándo el refrigerante fluye al radiador; el radiador transfiere calor al aire. Un nivel bajo de refrigerante, una bomba de agua fallida, un termostato atascado, una manguera que fuga o un radiador obstruido pueden hacer que el motor se sobrecaliente. El sobrecalentamiento puede dañar el motor. El diagnóstico verifica el nivel de refrigerante, la presión, la temperatura y la condición de los componentes antes de reemplazar cualquier pieza. En Phoenixville, a un corto viaje de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge, atendemos sistemas de enfriamiento en motores de gasolina y diésel.")),
            ("h2", t("Signs you need cooling system service", "Señales de que necesita servicio del sistema de enfriamiento")),
            ("ul", [
                t("Temperature gauge reads high or warning light comes on", "El indicador de temperatura lee alto o se enciende la luz de advertencia"),
                t("Coolant puddle under the vehicle", "Charco de refrigerante debajo del vehículo"),
                t("Sweet smell of coolant", "Olor dulce de refrigerante"),
                t("Steam from under the hood", "Vapor de debajo del capó"),
                t("Heater blows cold air", "El calentador sopla aire frío"),
            ]),
            ("p", t("The cause is diagnosed before parts are replaced. Overheating can be a low coolant level, a failed water pump, a thermostat, or a radiator problem. Pressure testing and inspection identify the failed component.", "Se diagnostica la causa antes de reemplazar piezas. El sobrecalentamiento puede ser un nivel bajo de refrigerante, una bomba de agua fallida, un termostato o un problema del radiador. La prueba de presión y la inspección identifican el componente fallido.")),
            ("h2", t("Cooling system work we do", "Trabajo del sistema de enfriamiento que realizamos")),
            ("h3", t("Cooling system service", "Servicio del sistema de enfriamiento")),
            ("p", t("We diagnose and service the cooling system, including leaks, thermostats, hoses and related components.", "Diagnosticamos y atendemos el sistema de enfriamiento, incluyendo fugas, termostatos, mangueras y componentes relacionados.")),
            ("h3", t("Water pump", "Bomba de agua")),
            ("p", t("We replace water pumps when diagnosis shows the pump is leaking or not circulating coolant.", "Reemplazamos bombas de agua cuando el diagnóstico muestra que la bomba está fugando o no está circulando refrigerante.")),
            ("ul", [
                t("Cooling system service", "Servicio del sistema de enfriamiento"),
                t("Water pump replacement", "Reemplazo de bomba de agua"),
            ]),
            ("p", t("If the engine is overheating and cannot be driven, we can arrange or accept a tow, and we offer drop-off and after-hours arrangements.", "Si el motor se está sobrecalentando y no puede conducirse, podemos organizar o aceptar un remolque, y ofrecemos arreglos de entrega y después de horas.")),
            ("p", t("Related services include [engine repair](services) and [A/C and heating](svc_climate). We also perform [state inspections](inspections).", "Los servicios relacionados incluyen [reparación de motor](services) y [aire acondicionado y calefacción](svc_climate). También realizamos [inspecciones estatales](inspections).")),
        ],
        "faq": [
            (t("What causes an engine to overheat?", "¿Qué causa que un motor se sobrecaliente?"), t("Overheating can be caused by low coolant, a failed water pump, a stuck thermostat, a leaking hose, or a radiator problem. Diagnosis identifies the cause before parts are replaced.", "El sobrecalentamiento puede ser causado por bajo refrigerante, una bomba de agua fallida, un termostato atascado, una manguera que fuga o un problema del radiador. El diagnóstico identifica la causa antes de reemplazar piezas.")),
            (t("Do you replace water pumps?", "¿Reemplazan bombas de agua?"), t("Yes. Water pump replacement is part of the cooling-system service we perform when diagnosis shows the pump is leaking or not circulating coolant.", "Sí. El reemplazo de la bomba de agua es parte del servicio del sistema de enfriamiento que realizamos cuando el diagnóstico muestra que la bomba está fugando o no está circulando refrigerante.")),
            (t("Can a coolant leak cause no heat?", "¿Una fuga de refrigerante puede causar falta de calor?"), t("Yes. Low coolant can reduce or eliminate heat from the heater. Diagnosis checks the coolant level and looks for leaks as part of both cooling and heating service.", "Sí. El bajo refrigerante puede reducir o eliminar el calor del calentador. El diagnóstico verifica el nivel de refrigerante y busca fugas como parte del servicio tanto de enfriamiento como de calefacción.")),
            (t("How do you find a coolant leak?", "¿Cómo encuentran una fuga de refrigerante?"), t("We inspect the system and can pressure-test it to find the leak. The visible puddle is not always the source; coolant can travel before it drips.", "Inspeccionamos el sistema y podemos probarlo a presión para encontrar la fuga. El charco visible no siempre es la fuente; el refrigerante puede viajar antes de gotear.")),
            (t("Can I keep driving if the temperature gauge is high?", "¿Puedo seguir conduciendo si el indicador de temperatura está alto?"), t("No. Continued driving with an overheating engine can cause serious damage. Have the vehicle towed so the cooling system can be diagnosed.", "No. Continuar conduciendo con un motor sobrecalentado puede causar daños graves. Haga que el vehículo sea remolcado para que se pueda diagnosticar el sistema de enfriamiento.")),
        ],
        "cta": [
            ("h2", t("Schedule cooling system repair near Phoenixville, PA", "Programe la reparación del sistema de enfriamiento cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule cooling system repair with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Contacte a Diverse Autoworks para programar la reparación del sistema de enfriamiento con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": ("cooling system repair overheating radiator water pump thermostat coolant leak hose engine overheating", "sistema de enfriamiento reparación sobrecalentamiento radiador bomba de agua termostato fuga de refrigerante"),
        "sources": [],
        "verify": [
            "Cooling system and water pump scope matches confirmed services",
            "No unconfirmed claims",
        ],
    },
]
