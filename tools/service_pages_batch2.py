# -*- coding: utf-8 -*-
"""Service pages batch 2: svc_clutch, svc_axle, svc_timing, svc_oilleak. Written by Grok, 2026-10-31. Needs fact check before publishing."""


def t(en, es):
    return {"en": en, "es": es}


SERVICE_PAGES = [
    {
        "key": "svc_clutch",
        "slug": "clutch-repair",
        "covers": ["clutch"],
        "primary_kw": "clutch repair Phoenixville",
        "secondary_kws": [
            "clutch replacement", "slipping clutch", "clutch pedal", "manual transmission clutch",
            "clutch noise", "hard to shift", "clutch cable", "clutch master cylinder",
            "clutch near me", "clutch service Phoenixville PA"
        ],
        "page": {
            "title": t("Clutch Repair in Phoenixville, PA | Diverse Autoworks", "Reparación de embrague en Phoenixville, PA"),
            "desc": t("Clutch replacement and service by ASE-certified technicians for manual-transmission vehicles in Phoenixville, PA.", "Reemplazo y servicio de embrague por técnicos certificados por ASE para vehículos de transmisión manual en Phoenixville, PA."),
            "h1": t("Clutch Repair in Phoenixville, PA", "Reparación de embrague en Phoenixville, PA"),
            "lead": t("Diverse Autoworks replaces and services clutches on domestic and foreign manual-transmission vehicles in Phoenixville. ASE-certified technicians diagnose slipping, noise and hard shifting before any parts are replaced.", "Diverse Autoworks reemplaza y da servicio a embragues en vehículos nacionales y extranjeros de transmisión manual en Phoenixville. Los técnicos certificados por ASE diagnostican deslizamiento, ruido y cambios difíciles antes de reemplazar cualquier pieza."),
            "crumb": t("Clutch repair", "Embrague"),
        },
        "service_type": t("Clutch replacement and service", "Reemplazo y servicio de embrague"),
        "blocks": [
            ("h2", t("Clutch repair in Phoenixville, PA", "Reparación de embrague en Phoenixville, PA")),
            ("p", t("A clutch connects and disconnects the engine from the transmission so the driver can shift gears. The clutch disc, pressure plate and release bearing (or hydraulic release system) work together. When the disc wears, the clutch can slip under load. When the release bearing or hydraulics fail, the pedal can feel spongy or the gears can be hard to select. Diagnosis checks pedal free play, engagement point and noise before parts are replaced. In Phoenixville, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge, we service clutches on gas and diesel manual vehicles.", "Un embrague conecta y desconecta el motor de la transmisión para que el conductor pueda cambiar de marcha. El disco de embrague, el plato de presión y el rodamiento de desembrague (o el sistema de liberación hidráulica) trabajan juntos. Cuando el disco se desgasta, el embrague puede deslizarse bajo carga. Cuando el rodamiento de desembrague o el sistema hidráulico fallan, el pedal puede sentirse esponjoso o las marchas pueden ser difíciles de seleccionar. El diagnóstico verifica el juego libre del pedal, el punto de enganche y el ruido antes de reemplazar piezas. En Phoenixville, a un corto viaje de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge, atendemos embragues en vehículos manuales de gasolina y diésel.")),
            ("h2", t("Signs you need clutch repair", "Señales de que necesita reparación de embrague")),
            ("ul", [
                t("Clutch slips when accelerating or climbing a hill", "El embrague se desliza al acelerar o subir una colina"),
                t("Hard or grinding shifts into gear", "Cambios duros o con rechinido al engranar"),
                t("Clutch pedal feels soft, spongy or goes to the floor", "El pedal del embrague se siente suave, esponjoso o llega al piso"),
                t("Noise when the clutch pedal is depressed or released", "Ruido cuando se pisa o se suelta el pedal del embrague"),
                t("Burning smell during hard acceleration", "Olor a quemado durante una aceleración fuerte"),
            ]),
            ("p", t("The cause is diagnosed before parts are replaced. Slipping can be a worn disc; hard shifting can be hydraulics or a release bearing. Testing identifies the failed component.", "Se diagnostica la causa antes de reemplazar piezas. El deslizamiento puede ser un disco desgastado; los cambios difíciles pueden ser el sistema hidráulico o un rodamiento de desembrague. Las pruebas identifican el componente fallido.")),
            ("h2", t("Clutch work we do", "Trabajo de embrague que realizamos")),
            ("ul", [
                t("Clutch replacement and service", "Reemplazo y servicio de embrague"),
            ]),
            ("p", t("We replace the clutch assembly and related components when diagnosis shows they are worn or failed. Service includes inspection of the release system and adjustment where the design allows it.", "Reemplazamos el conjunto del embrague y los componentes relacionados cuando el diagnóstico muestra que están desgastados o fallidos. El servicio incluye la inspección del sistema de liberación y el ajuste donde el diseño lo permite.")),
            ("p", t("If the clutch cannot be driven, we can arrange or accept a tow, and we offer drop-off and after-hours arrangements.", "Si el embrague no puede conducirse, podemos organizar o aceptar un remolque, y ofrecemos arreglos de entrega y después de horas.")),
            ("p", t("Related services include [transmission repair](services) and [engine repair](services). We also perform [state inspections](inspections).", "Los servicios relacionados incluyen [reparación de transmisión](services) y [reparación de motor](services). También realizamos [inspecciones estatales](inspections).")),
        ],
        "faq": [
            (t("What are the signs of a worn clutch?", "¿Cuáles son las señales de un embrague desgastado?"), t("Slipping under acceleration, a high engagement point, hard shifting, or a burning smell are common signs. Diagnosis confirms whether the disc, pressure plate or release system needs replacement.", "Deslizamiento bajo aceleración, un punto de enganche alto, cambios difíciles u olor a quemado son señales comunes. El diagnóstico confirma si el disco, el plato de presión o el sistema de liberación necesitan reemplazo.")),
            (t("Can you replace just the clutch disc?", "¿Pueden reemplazar solo el disco del embrague?"), t("We replace the clutch assembly as needed after diagnosis. The exact parts replaced depend on what the inspection shows is worn or failed.", "Reemplazamos el conjunto del embrague según sea necesario después del diagnóstico. Las piezas exactas reemplazadas dependen de lo que la inspección muestre que está desgastado o fallido.")),
            (t("Do you work on both cable and hydraulic clutches?", "¿Trabajan en embragues de cable e hidráulicos?"), t("Yes. We service both cable-operated and hydraulic clutch systems on domestic and foreign vehicles.", "Sí. Atendemos sistemas de embrague operados por cable e hidráulicos en vehículos nacionales y extranjeros.")),
            (t("Is clutch noise always a bad release bearing?", "¿El ruido del embrague siempre es un rodamiento de desembrague malo?"), t("Not always. Noise can come from the release bearing, the pilot bearing, or other components. Diagnosis identifies the source before parts are replaced.", "No siempre. El ruido puede provenir del rodamiento de desembrague, el rodamiento piloto u otros componentes. El diagnóstico identifica la fuente antes de reemplazar piezas.")),
            (t("Can I keep driving with a slipping clutch?", "¿Puedo seguir conduciendo con un embrague que se desliza?"), t("Continued driving with a slipping clutch increases wear and can leave the vehicle undrivable. Have it diagnosed so the correct repair can be made.", "Continuar conduciendo con un embrague que se desliza aumenta el desgaste y puede dejar el vehículo inconducible. Haga que se diagnostique para que se pueda realizar la reparación correcta.")),
        ],
        "cta": [
            ("h2", t("Schedule clutch repair near Phoenixville, PA", "Programe la reparación de embrague cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule clutch repair with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Contacte a Diverse Autoworks para programar la reparación de embrague con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": ("clutch repair clutch replacement slipping clutch clutch pedal manual transmission hard to shift clutch noise", "embrague reparación reemplazo de embrague embrague que se desliza pedal de embrague transmisión manual"),
        "sources": [],
        "verify": [
            "Clutch scope matches confirmed service only",
            "No unconfirmed claims",
        ],
    },
    {
        "key": "svc_axle",
        "slug": "cv-axle-differential-repair",
        "covers": ["cvaxle", "differential"],
        "primary_kw": "CV axle replacement Phoenixville",
        "secondary_kws": [
            "CV joint", "clicking when turning", "differential repair", "axle seal",
            "CV boot", "vibration when accelerating", "differential noise",
            "rear axle", "CV axle near me", "differential service Phoenixville"
        ],
        "page": {
            "title": t("CV Axle & Differential Repair in Phoenixville, PA", "Ejes CV y diferencial en Phoenixville, PA"),
            "desc": t("CV axle and joint replacement plus differential repair and related axle work by ASE-certified technicians in Phoenixville, PA.", "Reemplazo de ejes CV y juntas más reparación de diferencial y trabajo de ejes relacionado por técnicos certificados por ASE en Phoenixville, PA."),
            "h1": t("CV Axle and Differential Repair in Phoenixville, PA", "Reparación de ejes CV y diferencial en Phoenixville, PA"),
            "lead": t("Diverse Autoworks replaces CV axles and joints and repairs differentials and related axle work on domestic and foreign vehicles in Phoenixville. ASE-certified technicians diagnose clicking, vibration and leaks before parts are replaced.", "Diverse Autoworks reemplaza ejes CV y juntas y repara diferenciales y trabajo de ejes relacionado en vehículos nacionales y extranjeros en Phoenixville. Los técnicos certificados por ASE diagnostican clics, vibración y fugas antes de reemplazar piezas."),
            "crumb": t("CV axle & differential", "Ejes CV y diferencial"),
        },
        "service_type": t("CV axle and differential repair", "Reparación de ejes CV y diferencial"),
        "blocks": [
            ("h2", t("CV axle and differential repair in Phoenixville, PA", "Reparación de ejes CV y diferencial en Phoenixville, PA")),
            ("p", t("CV axles carry power from the transmission or differential to the front (or rear) wheels while allowing the suspension to move and the wheels to turn. The joints are protected by rubber boots. When a boot tears, grease escapes and dirt enters, and the joint can click when turning. A differential lets the drive wheels turn at different speeds in a corner. It contains gears and bearings that can wear, and seals that can leak. Diagnosis checks for clicking on turns, vibration on acceleration, and fluid leaks before parts are replaced. In Phoenixville, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge, we service both CV axles and differentials.", "Los ejes CV llevan potencia de la transmisión o el diferencial a las ruedas delanteras (o traseras) mientras permiten que la suspensión se mueva y las ruedas giren. Las juntas están protegidas por fundas de goma. Cuando una funda se rasga, la grasa se escapa y entra suciedad, y la junta puede hacer clic al girar. Un diferencial permite que las ruedas motrices giren a diferentes velocidades en una curva. Contiene engranajes y cojinetes que pueden desgastarse, y sellos que pueden fugar. El diagnóstico verifica clics en las curvas, vibración al acelerar y fugas de fluido antes de reemplazar piezas. En Phoenixville, a un corto viaje de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge, atendemos tanto ejes CV como diferenciales.")),
            ("h2", t("Signs you need CV axle or differential service", "Señales de que necesita servicio de eje CV o diferencial")),
            ("ul", [
                t("Clicking or popping when turning", "Clics o estallidos al girar"),
                t("Vibration that increases with speed or under acceleration", "Vibración que aumenta con la velocidad o bajo aceleración"),
                t("Grease sprayed on the inside of a wheel or on the underbody", "Grasa rociada en el interior de una rueda o en el chasis"),
                t("Whining or humming from the differential that changes with speed", "Zumbido o gemido del diferencial que cambia con la velocidad"),
                t("Gear oil leak at the axle or differential", "Fuga de aceite de engranajes en el eje o el diferencial"),
            ]),
            ("p", t("The cause is diagnosed before parts are replaced. Clicking on turns is often a CV joint; vibration or a leak can be an axle or a differential seal. Testing identifies the failed part.", "Se diagnostica la causa antes de reemplazar piezas. Los clics al girar a menudo son una junta CV; la vibración o una fuga pueden ser un eje o un sello del diferencial. Las pruebas identifican la pieza fallida.")),
            ("h2", t("CV axle and differential work we do", "Trabajo de eje CV y diferencial que realizamos")),
            ("h3", t("CV axles and joints", "Ejes CV y juntas")),
            ("p", t("We replace CV axles and joints when the boots are torn or the joints are worn.", "Reemplazamos ejes CV y juntas cuando las fundas están rasgadas o las juntas están desgastadas.")),
            ("h3", t("Differential", "Diferencial")),
            ("p", t("We repair differentials and perform related axle work, including seals and bearings as diagnosis requires.", "Reparamos diferenciales y realizamos trabajo de ejes relacionado, incluyendo sellos y cojinetes según requiera el diagnóstico.")),
            ("ul", [
                t("CV axle and joint replacement", "Reemplazo de ejes CV y juntas"),
                t("Differential repair and related axle work", "Reparación de diferencial y trabajo de ejes relacionado"),
            ]),
            ("p", t("If the axle cannot be driven, we can arrange or accept a tow, and we offer drop-off and after-hours arrangements.", "Si el eje no puede conducirse, podemos organizar o aceptar un remolque, y ofrecemos arreglos de entrega y después de horas.")),
            ("p", t("Related services include [transmission repair](services) and [suspension repair](svc_suspension). We also perform [state inspections](inspections).", "Los servicios relacionados incluyen [reparación de transmisión](services) y [reparación de suspensión](svc_suspension). También realizamos [inspecciones estatales](inspections).")),
        ],
        "faq": [
            (t("What does a clicking sound when turning mean?", "¿Qué significa un sonido de clic al girar?"), t("A clicking or popping noise when turning is a common sign of a worn CV joint. We diagnose the joint and replace the axle or joint when testing confirms it is the source.", "Un ruido de clic o estallido al girar es una señal común de una junta CV desgastada. Diagnosticamos la junta y reemplazamos el eje o la junta cuando las pruebas confirman que es la fuente.")),
            (t("Can a torn CV boot be repaired?", "¿Se puede reparar una funda de eje CV rasgada?"), t("Once a boot is torn and the joint has lost grease or taken in dirt, the joint is usually replaced along with the axle. Diagnosis determines the condition of the joint.", "Una vez que una funda está rasgada y la junta ha perdido grasa o ha entrado suciedad, la junta generalmente se reemplaza junto con el eje. El diagnóstico determina la condición de la junta.")),
            (t("Do you repair differentials?", "¿Reparan diferenciales?"), t("Yes. Differential repair and related axle work, including seals and bearings, is part of the service we offer.", "Sí. La reparación de diferencial y el trabajo de ejes relacionado, incluyendo sellos y cojinetes, es parte del servicio que ofrecemos.")),
            (t("What causes differential noise?", "¿Qué causa el ruido del diferencial?"), t("Worn gears or bearings can produce a whine or hum that changes with vehicle speed. Diagnosis identifies whether the noise is from the differential or another component.", "Los engranajes o cojinetes desgastados pueden producir un zumbido o gemido que cambia con la velocidad del vehículo. El diagnóstico identifica si el ruido proviene del diferencial o de otro componente.")),
            (t("Is a CV axle the same as a drive shaft?", "¿Un eje CV es lo mismo que un cardán?"), t("A CV axle is the half-shaft that connects the differential or transmission to the wheel and contains constant-velocity joints. A driveshaft is the longer shaft used in some rear-wheel-drive and four-wheel-drive layouts. We service CV axles and related differential work.", "Un eje CV es el semieje que conecta el diferencial o la transmisión a la rueda y contiene juntas de velocidad constante. Un cardán es el eje más largo usado en algunos diseños de tracción trasera y cuatro ruedas. Atendemos ejes CV y trabajo de diferencial relacionado.")),
        ],
        "cta": [
            ("h2", t("Schedule CV axle or differential repair near Phoenixville, PA", "Programe la reparación de eje CV o diferencial cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule CV axle or differential repair with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Contacte a Diverse Autoworks para programar la reparación de eje CV o diferencial con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": ("CV axle replacement CV joint clicking when turning differential repair axle seal CV boot vibration", "eje CV reemplazo junta CV clic al girar diferencial reparación sello de eje funda CV"),
        "sources": [],
        "verify": [
            "CV axle and differential scope matches confirmed services",
            "No unconfirmed claims",
        ],
    },
    {
        "key": "svc_timing",
        "slug": "timing-belt",
        "covers": ["timing"],
        "primary_kw": "timing belt replacement Phoenixville",
        "secondary_kws": [
            "timing chain", "timing belt interval", "interference engine",
            "timing belt noise", "engine timing", "timing belt kit",
            "when to replace timing belt", "timing belt near me"
        ],
        "page": {
            "title": t("Timing Belt Replacement in Phoenixville, PA", "Correa de distribución en Phoenixville, PA"),
            "desc": t("Timing belt and timing chain service by ASE-certified technicians in Phoenixville, PA. Intervals follow your owner's manual.", "Servicio de correa y cadena de distribución por técnicos certificados por ASE en Phoenixville, PA. Los intervalos siguen su manual del propietario."),
            "h1": t("Timing Belt Replacement in Phoenixville, PA", "Reemplazo de correa de distribución en Phoenixville, PA"),
            "lead": t("Diverse Autoworks services timing belts and timing chains on domestic and foreign engines in Phoenixville. ASE-certified technicians follow the interval in your owner's manual and diagnose noise or starting problems before any work is done.", "Diverse Autoworks atiende correas de distribución y cadenas de distribución en motores nacionales y extranjeros en Phoenixville. Los técnicos certificados por ASE siguen el intervalo de su manual del propietario y diagnostican ruido o problemas de arranque antes de realizar cualquier trabajo."),
            "crumb": t("Timing belt", "Correa de distribución"),
        },
        "service_type": t("Timing belt and timing chain service", "Servicio de correa y cadena de distribución"),
        "blocks": [
            ("h2", t("Timing belt service in Phoenixville, PA", "Servicio de correa de distribución en Phoenixville, PA")),
            ("p", t("A timing belt or timing chain synchronizes the crankshaft and camshaft so the valves open and close at the correct time relative to the pistons. Many engines use a rubber timing belt that must be replaced at a set interval. Others use a metal timing chain that is designed to last longer but can still stretch or need service. On an interference engine, a broken belt can allow the pistons to strike the valves. AAA notes that most manufacturers recommend replacement somewhere between 60,000 and 100,000 miles; Gates has long advised replacing the belt at the manufacturer interval or every 72 months, whichever comes first. Your owner's manual lists the exact interval for your engine. In Phoenixville, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge, we service both belts and chains.", "Una correa de distribución o una cadena de distribución sincroniza el cigüeñal y el árbol de levas para que las válvulas se abran y cierren en el momento correcto en relación con los pistones. Muchos motores usan una correa de distribución de goma que debe reemplazarse en un intervalo establecido. Otros usan una cadena de distribución de metal que está diseñada para durar más pero aún puede estirarse o necesitar servicio. En un motor de interferencia, una correa rota puede permitir que los pistones golpeen las válvulas. AAA señala que la mayoría de los fabricantes recomiendan el reemplazo en algún lugar entre 60,000 y 100,000 millas; Gates ha aconsejado durante mucho tiempo reemplazar la correa en el intervalo del fabricante o cada 72 meses, lo que ocurra primero. Su manual del propietario indica el intervalo exacto para su motor. En Phoenixville, a un corto viaje de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge, atendemos tanto correas como cadenas.")),
            ("h2", t("Signs you need timing belt service", "Señales de que necesita servicio de correa de distribución")),
            ("ul", [
                t("Mileage or age is at or past the interval in the owner's manual", "El kilometraje o la edad está en o más allá del intervalo del manual del propietario"),
                t("Ticking or rattling from the timing cover area", "Tic-tac o cascabeleo del área de la cubierta de distribución"),
                t("Engine misfire or hard starting that appears suddenly", "Fallo del motor o arranque difícil que aparece de repente"),
                t("Oil leak near the timing cover", "Fuga de aceite cerca de la cubierta de distribución"),
            ]),
            ("p", t("The cause is diagnosed before parts are replaced. A noise or a leak is inspected; the belt or chain is replaced on the schedule in the manual even if no symptoms are present.", "Se diagnostica la causa antes de reemplazar piezas. Se inspecciona un ruido o una fuga; la correa o la cadena se reemplaza según el programa del manual incluso si no hay síntomas presentes.")),
            ("h2", t("Timing belt work we do", "Trabajo de correa de distribución que realizamos")),
            ("ul", [
                t("Timing belt service", "Servicio de correa de distribución"),
                t("Timing chain service", "Servicio de cadena de distribución"),
            ]),
            ("p", t("We replace the timing belt or service the timing chain according to the interval and procedure for your engine. Related components such as the tensioner are addressed when the service requires it.", "Reemplazamos la correa de distribución o atendemos la cadena de distribución según el intervalo y el procedimiento para su motor. Los componentes relacionados como el tensor se abordan cuando el servicio lo requiere.")),
            ("h2", t("Timing belt intervals", "Intervalos de correa de distribución")),
            ("p", t("Your owner's manual lists the interval for your engine. AAA reports that most manufacturers recommend replacement between 60,000 and 100,000 miles. Gates recommends replacing the belt at the manufacturer interval or every 72 months, whichever comes first, because rubber ages even if the vehicle is driven little. Severe conditions can shorten the interval on some engines. We follow the schedule in your manual.", "Su manual del propietario indica el intervalo para su motor. AAA informa que la mayoría de los fabricantes recomiendan el reemplazo entre 60,000 y 100,000 millas. Gates recomienda reemplazar la correa en el intervalo del fabricante o cada 72 meses, lo que ocurra primero, porque la goma envejece incluso si el vehículo se conduce poco. Las condiciones severas pueden acortar el intervalo en algunos motores. Seguimos el programa de su manual.")),
            ("p", t("Related services include [engine repair](services) and [oil leak repair](svc_oilleak). We also perform [state inspections](inspections).", "Los servicios relacionados incluyen [reparación de motor](services) y [reparación de fugas de aceite](svc_oilleak). También realizamos [inspecciones estatales](inspections).")),
        ],
        "faq": [
            (t("How often should a timing belt be replaced?", "¿Con qué frecuencia se debe reemplazar una correa de distribución?"), t("Follow the interval in your owner's manual. AAA notes that most manufacturers recommend replacement between 60,000 and 100,000 miles. Gates advises the manufacturer interval or every 72 months, whichever comes first.", "Siga el intervalo de su manual del propietario. AAA señala que la mayoría de los fabricantes recomiendan el reemplazo entre 60,000 y 100,000 millas. Gates aconseja el intervalo del fabricante o cada 72 meses, lo que ocurra primero.")),
            (t("What is an interference engine?", "¿Qué es un motor de interferencia?"), t("On an interference engine the pistons and valves occupy the same space at different times. If the timing belt breaks, the pistons can strike the valves. Your owner's manual or a technician can tell you whether your engine is an interference design.", "En un motor de interferencia los pistones y las válvulas ocupan el mismo espacio en diferentes momentos. Si la correa de distribución se rompe, los pistones pueden golpear las válvulas. Su manual del propietario o un técnico puede decirle si su motor es de diseño de interferencia.")),
            (t("Do you service timing chains?", "¿Atienden cadenas de distribución?"), t("Yes. Timing chain service is part of the timing work we perform, in addition to timing belt replacement.", "Sí. El servicio de cadena de distribución es parte del trabajo de distribución que realizamos, además del reemplazo de la correa de distribución.")),
            (t("Can I wait until the belt makes noise?", "¿Puedo esperar hasta que la correa haga ruido?"), t("No. A timing belt is replaced on the schedule in the owner's manual because it can fail without warning. Waiting for noise risks engine damage on an interference engine.", "No. Una correa de distribución se reemplaza según el programa del manual del propietario porque puede fallar sin aviso. Esperar al ruido arriesga daño al motor en un motor de interferencia.")),
            (t("Does a timing belt need to be replaced if the car has low miles?", "¿Hay que reemplazar una correa de distribución si el auto tiene pocas millas?"), t("Yes, if the age is past the time interval. Rubber ages even when the vehicle is driven little. Gates recommends every 72 months or the manufacturer interval, whichever comes first.", "Sí, si la edad supera el intervalo de tiempo. La goma envejece incluso cuando el vehículo se conduce poco. Gates recomienda cada 72 meses o el intervalo del fabricante, lo que ocurra primero.")),
        ],
        "cta": [
            ("h2", t("Schedule timing belt service near Phoenixville, PA", "Programe el servicio de correa de distribución cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule timing belt or timing chain service with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Contacte a Diverse Autoworks para programar el servicio de correa o cadena de distribución con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": ("timing belt replacement timing chain interference engine timing belt interval when to replace timing belt timing belt noise", "correa de distribución cadena de distribución motor de interferencia intervalo de correa de distribución"),
        "sources": [
            ("AAA – When Should Timing Belts Be Replaced?", "https://cluballiance.aaa.com/the-extra-mile/advice/car/when-should-timing-belts-be-replaced"),
            ("Gates Timing Belt Replacement Interval Guide (PDF)", "https://www.freeautomechanic.com/TimingBeltReplacementGuide.pdf"),
        ],
        "verify": [
            "AAA 60k–100k mile range matches the linked article",
            "Gates 72-month recommendation matches the linked guide",
        ],
    },
    {
        "key": "svc_oilleak",
        "slug": "oil-leak-repair",
        "covers": ["oilleak"],
        "primary_kw": "oil leak repair Phoenixville",
        "secondary_kws": [
            "oil leak", "gasket replacement", "valve cover gasket", "oil pan gasket",
            "rear main seal", "oil smell", "oil spots", "oil leak near me",
            "engine oil leak Phoenixville"
        ],
        "page": {
            "title": t("Oil Leak Repair in Phoenixville, PA | Diverse Autoworks", "Reparación de fugas de aceite en Phoenixville, PA"),
            "desc": t("Oil leak repair and gasket replacement by ASE-certified technicians in Phoenixville, PA. Diagnosis finds the source before parts are replaced.", "Reparación de fugas de aceite y juntas por técnicos ASE en Phoenixville, PA. El diagnóstico encuentra la fuente."),
            "h1": t("Oil Leak Repair in Phoenixville, PA", "Reparación de fugas de aceite en Phoenixville, PA"),
            "lead": t("Diverse Autoworks diagnoses and repairs oil leaks and replaces gaskets on domestic and foreign engines in Phoenixville. ASE-certified technicians locate the source of the leak before any parts are replaced.", "Diverse Autoworks diagnostica y repara fugas de aceite y reemplaza juntas en motores nacionales y extranjeros en Phoenixville. Los técnicos certificados por ASE localizan la fuente de la fuga antes de reemplazar cualquier pieza."),
            "crumb": t("Oil leak repair", "Fugas de aceite"),
        },
        "service_type": t("Oil leak repair and gasket replacement", "Reparación de fugas de aceite y reemplazo de juntas"),
        "blocks": [
            ("h2", t("Oil leak repair in Phoenixville, PA", "Reparación de fugas de aceite en Phoenixville, PA")),
            ("p", t("Engine oil is held inside the engine by gaskets and seals at the valve cover, oil pan, front and rear main seals, and other joints. Heat, age and mileage cause these gaskets and seals to harden and crack. Oil then seeps out, leaves spots on the driveway, and can drip onto the exhaust and create a burning smell. A leak can also lower the oil level over time. Diagnosis uses dye or careful inspection to find the exact joint that is leaking before any gasket is replaced. In Phoenixville, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge, we repair oil leaks on gas and diesel engines.", "El aceite del motor se mantiene dentro del motor mediante juntas y sellos en la tapa de válvulas, el cárter, los sellos principales delantero y trasero, y otras uniones. El calor, la edad y el kilometraje hacen que estas juntas y sellos se endurezcan y agrieten. El aceite entonces se filtra, deja manchas en el camino de entrada y puede gotear sobre el escape y crear un olor a quemado. Una fuga también puede bajar el nivel de aceite con el tiempo. El diagnóstico usa tinte o una inspección cuidadosa para encontrar la unión exacta que está fugando antes de reemplazar cualquier junta. En Phoenixville, a un corto viaje de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge, reparamos fugas de aceite en motores de gasolina y diésel.")),
            ("h2", t("Signs you need oil leak repair", "Señales de que necesita reparación de fugas de aceite")),
            ("ul", [
                t("Oil spots on the driveway or garage floor", "Manchas de aceite en el camino de entrada o el piso del garaje"),
                t("Burning oil smell while driving", "Olor a aceite quemado mientras conduce"),
                t("Low oil level between changes", "Nivel de aceite bajo entre cambios"),
                t("Oil visible on the engine, valve cover or oil pan", "Aceite visible en el motor, la tapa de válvulas o el cárter"),
                t("Blue or white smoke from the exhaust on startup", "Humo azul o blanco del escape al arrancar"),
            ]),
            ("p", t("The cause is diagnosed before parts are replaced. Oil can travel along the engine before it drips, so the visible spot is not always the source. Testing locates the leaking joint.", "Se diagnostica la causa antes de reemplazar piezas. El aceite puede viajar a lo largo del motor antes de gotear, por lo que el punto visible no siempre es la fuente. Las pruebas localizan la unión que fuga.")),
            ("h2", t("Oil leak work we do", "Trabajo de fugas de aceite que realizamos")),
            ("ul", [
                t("Oil leak repair", "Reparación de fugas de aceite"),
                t("Gasket replacement", "Reemplazo de juntas"),
            ]),
            ("p", t("We replace the gasket or seal that is leaking after diagnosis confirms the source. Common locations include the valve cover, oil pan and main seals.", "Reemplazamos la junta o el sello que está fugando después de que el diagnóstico confirma la fuente. Las ubicaciones comunes incluyen la tapa de válvulas, el cárter y los sellos principales.")),
            ("p", t("Related services include [engine repair](services) and [timing belt service](svc_timing). We also perform [state inspections](inspections).", "Los servicios relacionados incluyen [reparación de motor](services) y [servicio de correa de distribución](svc_timing). También realizamos [inspecciones estatales](inspections).")),
        ],
        "faq": [
            (t("How do you find the source of an oil leak?", "¿Cómo encuentran la fuente de una fuga de aceite?"), t("We inspect the engine and can use dye to trace the oil to the exact gasket or seal that is leaking. The visible drip is not always the source.", "Inspeccionamos el motor y podemos usar tinte para rastrear el aceite hasta la junta o el sello exacto que está fugando. El goteo visible no siempre es la fuente.")),
            (t("Can a small oil leak be ignored?", "¿Se puede ignorar una fuga de aceite pequeña?"), t("A small leak can grow and can lower the oil level over time. Diagnosis identifies the source so the correct gasket can be replaced.", "Una fuga pequeña puede crecer y puede bajar el nivel de aceite con el tiempo. El diagnóstico identifica la fuente para que se pueda reemplazar la junta correcta.")),
            (t("Do you replace valve cover and oil pan gaskets?", "¿Reemplazan juntas de tapa de válvulas y de cárter?"), t("Yes. Gasket replacement, including valve cover and oil pan gaskets, is part of the oil-leak repair we perform after diagnosis.", "Sí. El reemplazo de juntas, incluyendo juntas de tapa de válvulas y de cárter, es parte de la reparación de fugas de aceite que realizamos después del diagnóstico.")),
            (t("What causes a burning oil smell?", "¿Qué causa un olor a aceite quemado?"), t("Oil dripping onto a hot exhaust manifold or pipe can produce a burning smell. Diagnosis finds the leak so it can be repaired.", "El aceite que gotea sobre un múltiple o tubo de escape caliente puede producir un olor a quemado. El diagnóstico encuentra la fuga para que pueda repararse.")),
            (t("Will an oil leak fail a Pennsylvania inspection?", "¿Una fuga de aceite fallará una inspección de Pensilvania?"), t("A significant oil leak that leaves the engine area oily or that affects other systems can be a concern. We diagnose and repair the leak so the vehicle can be inspected. See [state inspections](inspections).", "Una fuga de aceite significativa que deja el área del motor aceitosa o que afecta otros sistemas puede ser una preocupación. Diagnosticamos y reparamos la fuga para que el vehículo pueda ser inspeccionado. Vea [inspecciones estatales](inspections).")),
        ],
        "cta": [
            ("h2", t("Schedule oil leak repair near Phoenixville, PA", "Programe la reparación de fugas de aceite cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule oil leak repair with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Contacte a Diverse Autoworks para programar la reparación de fugas de aceite con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": ("oil leak repair gasket replacement valve cover gasket oil pan gasket rear main seal oil spots burning oil smell", "fuga de aceite reparación reemplazo de juntas junta de tapa de válvulas junta de cárter sello principal trasero"),
        "sources": [],
        "verify": [
            "Oil leak and gasket scope matches confirmed service",
            "No unconfirmed claims",
        ],
    },
]
