# -*- coding: utf-8 -*-
"""Classic car repair & maintenance page (EN/ES).

Editorial scope: owner approval needed for classic-car intake and any specialized
capabilities. General mechanical services below are confirmed shop offerings;
their availability on an individual older vehicle is not assumed.
"""


def t(en, es):
    return {"en": en, "es": es}


SERVICE_PAGES = [
    {
        "key": "svc_classic",
        "slug": "classic-car-repair",
        "covers": [],
        "primary_kw": "classic car repair Phoenixville PA",
        "secondary_kws": [
            "classic car mechanic Phoenixville", "vintage car repair",
            "antique car maintenance", "older car mechanic",
            "classic car brakes", "classic car engine repair",
            "collector car maintenance", "classic car inspection Pennsylvania",
            "classic car repair Chester County", "vintage car service near me",
        ],
        "page": {
            "title": t(
                "Classic Car Repair Phoenixville, PA | Diverse Autoworks",
                "Reparación de autos clásicos en Phoenixville, PA"
            ),
            "desc": t(
                "Keep your classic on the road. Ask Diverse Autoworks in Phoenixville, PA about vintage-car engine, brake, cooling, electrical and maintenance needs.",
                "Mantenga su auto clásico en marcha. Consulte en Diverse Autoworks, Phoenixville, sobre motor, frenos, enfriamiento, electricidad y mantenimiento."
            ),
            "h1": t(
                "Keeping Legends on the Road: Classic Car Repair in Phoenixville, PA",
                "Clásicos que siguen rodando: reparación de autos clásicos en Phoenixville, PA"
            ),
            "lead": t(
                "Some cars get you from A to B. Others make every drive worth remembering. From American muscle and European roadsters to Japanese classics and family heirlooms, we understand why you want to keep yours moving. At Diverse Autoworks in Phoenixville, we focus on mechanical maintenance and repair, not paint or restoration. Tell us about your car and the work it needs so we can confirm the right service for your model.",
                "Algunos autos solo sirven para trasladarse. Otros convierten cada salida en un recuerdo. Desde los deportivos estadounidenses y europeos hasta los clásicos japoneses y autos familiares conservados por generaciones, sabemos por qué quiere mantener el suyo en marcha. En Diverse Autoworks, Phoenixville, nos centramos en mantenimiento y reparación mecánica, no en pintura ni restauración. Cuéntenos sobre su auto para confirmar el servicio adecuado."
            ),
            "crumb": t("Classic car repair", "Autos clásicos"),
        },
        "service_type": t(
            "Classic vehicle mechanical maintenance and repair inquiries",
            "Consultas sobre mantenimiento y reparación mecánica de autos clásicos"
        ),
        "blocks": [
            ("h2", t(
                "Old-School Character. Thoughtful Mechanical Care.",
                "Carácter de otra época. Atención mecánica con criterio."
            )),
            ("p", t(
                "That familiar engine note. The shape of the dashboard. The feeling of turning a key that has been in the family for decades. A classic deserves attention to what makes it special, but sentiment alone cannot tell you why it stalls, leaks or pulls to one side. Many older vehicles have changed over the years: engines swapped, wiring altered, components rebuilt and service records lost. We begin with the car in front of us—its history, condition, modifications and actual symptoms—rather than assuming that two vehicles of the same year need the same fix.",
                "El sonido inconfundible del motor. Las formas del tablero. La sensación de girar una llave que ha pasado de una generación a otra. Un clásico merece respeto por su historia, pero ese cariño no explica por qué se apaga, pierde aceite o se desvía al frenar. Muchos vehículos antiguos han cambiado con los años: motores reemplazados, cableado modificado, componentes reconstruidos e historiales incompletos. Empezamos por el auto que tenemos delante: su historia, su estado, sus modificaciones y sus síntomas reales, sin suponer que dos unidades del mismo año necesitan la misma reparación."
            )),
            ("p", t(
                "Our general mechanical services include engines, brakes, steering, suspension, cooling, batteries, electrical systems and fuel systems. On a classic, the details matter: original or modified components, available parts, and the tools required for the job. We review those details with you before confirming work on an individual older vehicle. Our focus is the mechanical side of keeping a classic usable—not making promises about every model or every rare part.",
                "Nuestros servicios mecánicos generales incluyen motores, frenos, dirección, suspensión, enfriamiento, baterías, electricidad y combustible. En un clásico importan los detalles: piezas originales o modificadas, disponibilidad de repuestos y herramientas necesarias. Revisamos esos datos con usted antes de confirmar un trabajo en un vehículo antiguo. Nos concentramos en su funcionamiento mecánico, sin prometer atención para cada modelo o pieza poco común."
            )),
            ("h2", t(
                "When Your Classic Is Trying to Tell You Something",
                "Cuando su clásico le está avisando que algo falla"
            )),
            ("ul", [
                t("Hard starting, stalling, hesitation or an uneven idle.", "Dificultad para arrancar, apagones, falta de respuesta o ralentí irregular."),
                t("Brake pull, long pedal travel, fluid loss or unfamiliar braking noises.", "El auto se desvía al frenar, el pedal tiene recorrido excesivo, pierde líquido o hace ruidos."),
                t("Cooling-system leaks, rising temperature or coolant loss.", "Fugas del sistema de enfriamiento, aumento de temperatura o pérdida de refrigerante."),
                t("Cracked belts or hoses, damp seals, oil leaks or fuel odor.", "Correas o mangueras agrietadas, juntas húmedas, fugas de aceite u olor a combustible."),
                t("Loose steering, uneven tire wear or suspension noises.", "Dirección con juego, desgaste irregular de llantas o ruidos de suspensión."),
                t("A battery that repeatedly loses charge or unreliable lights and wiring.", "Batería que se descarga repetidamente o fallas intermitentes en luces y cableado."),
            ]),
            ("p", t(
                "A symptom points to an area to inspect; it does not prove which part has failed. Older vehicles may not have modern onboard diagnostics, so a routine scan cannot replace mechanical inspection or testing. If you notice a fuel leak, unsafe braking, severe overheating or an oil-pressure problem, do not continue driving the car. Arrange transport and describe the problem before bringing it in.",
                "Una señal indica qué sistema conviene revisar, pero no identifica por sí sola la pieza dañada. Algunos autos antiguos no tienen diagnóstico electrónico moderno; un escáner no sustituye una inspección o prueba mecánica. Si detecta una fuga de combustible, frenos inseguros, sobrecalentamiento grave o problemas de presión de aceite, no siga conduciendo. Organice el traslado y describa la falla antes de llevar el auto."
            )),
            ("h2", t(
                "Mechanical Care for the Miles Ahead",
                "Cuidado mecánico para seguir sumando kilómetros"
            )),
            ("ul", [
                t("Engine and ignition — starting, rough idle, oil leaks and tune-up concerns.", "Motor y encendido: arranque, ralentí irregular, fugas de aceite y afinación."),
                t("Brakes, steering and suspension — pedal feel, pulling, play and worn parts.", "Frenos, dirección y suspensión: respuesta del pedal, desvíos, holguras y desgaste."),
                t("Cooling — radiator, hoses, water pump, thermostat and overheating symptoms.", "Enfriamiento: radiador, mangueras, bomba, termostato y sobrecalentamiento."),
                t("Starting and electrical — battery, charging system, lights and wiring issues.", "Arranque y electricidad: batería, sistema de carga, luces y problemas de cableado."),
                t("Fuel and exhaust — fuel-delivery symptoms, tank concerns and exhaust leaks.", "Combustible y escape: fallas de alimentación, tanque y fugas del escape."),
                t("Routine care — tires, wheel bearings, seals and fluids suited to the vehicle.", "Mantenimiento: llantas, rodamientos, juntas y líquidos adecuados para el vehículo."),
            ]),
            ("p", t(
                "These are types of work within Diverse Autoworks' broader mechanical offering, not a fixed classic-car package. Acceptance depends on the vehicle and the specific task. For details, see [engine repair](svc_engine), [brake repair](svc_brakes), [cooling-system repair](svc_cooling), [electrical repair](svc_electrical), [battery service](svc_battery) and [rust and corrosion concerns](svc_rust). Discuss any unusual setup, non-original parts or specialized tools before scheduling.",
                "Estos trabajos forman parte de la oferta mecánica general de Diverse Autoworks; no constituyen un paquete fijo para autos clásicos. La aceptación depende del vehículo y de la tarea específica. Consulte nuestras páginas de [reparación de motor](svc_engine), [frenos](svc_brakes), [enfriamiento](svc_cooling), [reparación eléctrica](svc_electrical), [baterías](svc_battery) y [óxido y corrosión](svc_rust). Informe sobre modificaciones, piezas no originales o herramientas especiales antes de programar."
            )),
            ("h2", t(
                "The Right Oil, the Right Parts, the Right Questions",
                "El aceite adecuado, las piezas adecuadas y las preguntas correctas"
            )),
            ("p", t(
                "Older engines are not all alike. Some flat-tappet camshaft designs have particular oil and antiwear-additive requirements; others do not need a special high-zinc formula. The correct choice depends on the engine and any rebuild or modification history. Likewise, a low-mileage collector car may have tires that are old even when the tread looks good. Tell us what you know about past work and storage so the appropriate checks and maintenance items can be discussed before a visit.",
                "No todos los motores antiguos son iguales. Algunos diseños con árbol de levas y taqués planos tienen requisitos específicos de aceite y aditivos antidesgaste; otros no necesitan una fórmula especial con más zinc. La elección depende del motor y de las reconstrucciones o modificaciones realizadas. Además, las llantas de un auto de colección con poco uso pueden haber envejecido aunque la banda de rodadura se vea bien. Cuéntenos qué sabe sobre las reparaciones y el almacenamiento para hablar de las revisiones y el mantenimiento adecuados antes de una visita."
            )),
            ("h2", t(
                "From the Garage Back to the Open Road",
                "Del garaje de vuelta a la carretera"
            )),
            ("p", t(
                "A car that has been parked for months or years may need a careful review before its first drive. Fuel can age, seals and hoses can deteriorate, batteries can lose charge, and tire condition may not be obvious from the tread alone. Braking components can also develop problems while a vehicle sits. AAA's vintage-car care guidance recommends checking brakes, tires, belts, hoses, battery and fluids when returning a stored vehicle to use. Start with safety and condition rather than assuming that a running engine makes the car road-ready.",
                "Un auto que ha permanecido estacionado durante meses o años puede necesitar una revisión antes de volver a circular. El combustible envejece, las juntas y mangueras se deterioran, las baterías se descargan y el estado de las llantas no siempre se aprecia en la banda de rodadura. Los frenos también pueden presentar problemas durante el almacenamiento. La guía de AAA para vehículos antiguos recomienda revisar frenos, llantas, correas, mangueras, batería y líquidos antes de volver a usarlos. Que el motor encienda no significa que el auto esté listo para circular."
            )),
            ("p", t(
                "Tell the shop how long the vehicle has been parked, where it was stored, when it last ran and any work already attempted. Do not start a car with a suspected fuel leak or drive one with uncertain braking. Ask about an initial assessment before planning a longer trip. The appropriate checks will depend on the car's construction and condition; there is no single maintenance checklist that fits every vintage model.",
                "Indique cuánto tiempo estuvo guardado, dónde permaneció, cuándo funcionó por última vez y qué reparaciones ya se intentaron. No arranque un vehículo con una posible fuga de combustible ni conduzca si desconoce el estado de los frenos. Solicite una evaluación inicial antes de planear un viaje largo. La revisión adecuada depende del diseño y el estado del auto; no existe una lista idéntica para todos los modelos antiguos."
            )),
            ("h2", t(
                "Under the Hood, Not in the Paint Booth",
                "Bajo el capó, no en el taller de pintura"
            )),
            ("p", t(
                "A mechanical repair aims to address a specific operating or safety concern. A restoration may involve body fabrication, paint, upholstery, cosmetic refinishing or a complete rebuild to original specifications. Those are separate projects with different equipment, parts and costs. This page discusses mechanical work, not full restoration, concours preparation, collision repair, custom fabrication or a guarantee of original-equipment parts. If your project includes those tasks, explain that scope when you contact the shop so expectations are clear.",
                "Una reparación mecánica busca resolver una falla de funcionamiento o seguridad. Una restauración puede incluir fabricación de carrocería, pintura, tapicería, acabados o reconstrucción completa según las especificaciones originales. Son proyectos distintos, con equipos, piezas y costos diferentes. Esta página trata sobre trabajos mecánicos; no ofrece restauraciones integrales, preparación para concursos, reparación de choques, fabricación personalizada ni una garantía de piezas originales. Si su proyecto incluye esas tareas, descríbalas al comunicarse con el taller."
            )),
            ("h2", t(
                "Classic Plates, Antique Plates & Pennsylvania Inspections",
                "Placas de clásico, placas de antiguo e inspecciones en Pensilvania"
            )),
            ("p", t(
                "Pennsylvania uses specific registration categories for classic and antique vehicles, and the plate type matters. Under 67 Pa. Code § 175.4, antique vehicles are excluded from the normal safety-inspection requirement; a vehicle with classic plates does not automatically receive that same exemption. Registration eligibility and permitted use are separate questions from a car's mechanical condition. Check current PennDOT requirements for your exact registration, and see our [Pennsylvania inspection](inspections) and [tag and title](tags) information for related services.",
                "Pensilvania tiene categorías de registro específicas para vehículos clásicos y antiguos, y el tipo de placa importa. Según 67 Pa. Code § 175.4, los vehículos registrados como antiguos están exentos del requisito habitual de inspección de seguridad; una placa de vehículo clásico no concede automáticamente la misma exención. Las condiciones de registro y uso son distintas del estado mecánico del auto. Consulte las reglas vigentes de PennDOT según su matrícula y revise nuestra información sobre [inspecciones de Pensilvania](inspections) y [trámites de título y placas](tags)."
            )),
            ("h2", t(
                "Your Classic Car, Right Here in Phoenixville",
                "Su auto clásico, aquí mismo en Phoenixville"
            )),
            ("p", t(
                "Diverse Autoworks is at 1415 Pawlings Road in Phoenixville, PA. Owners from Spring City, Royersford, Collegeville, Kimberton, Oaks, Chester Springs and nearby communities can contact the shop about their older vehicles. Include the make, model, year, engine, whether it runs, and the repair or symptom you want evaluated. Photographs and maintenance records can help explain an unusual setup. We will discuss the request and confirm service availability for the specific vehicle before you bring it to the shop.",
                "Diverse Autoworks se encuentra en 1415 Pawlings Road, Phoenixville, PA. Los propietarios de Spring City, Royersford, Collegeville, Kimberton, Oaks, Chester Springs y otras comunidades cercanas pueden consultar sobre sus vehículos antiguos. Indique marca, modelo, año, motor, si el auto funciona y la reparación o falla que desea evaluar. Las fotografías y los registros de mantenimiento pueden aclarar modificaciones poco comunes. El taller revisará la solicitud y confirmará la disponibilidad del servicio para ese vehículo antes de que lo lleve."
            )),
        ],
        "faq": [
            (t(
                "Does Diverse Autoworks repair classic or vintage cars?",
                "¿Diverse Autoworks repara autos clásicos o antiguos?"
            ), t(
                "Contact the shop with the year, make, model and requested mechanical work. We can discuss the job and confirm whether we can accept that particular vehicle; our general repair list does not automatically cover every classic car.",
                "Comuníquese con el taller e indique año, marca, modelo y trabajo mecánico solicitado. Podemos evaluar su consulta y confirmar si aceptamos ese vehículo; la lista general de reparaciones no incluye automáticamente a todos los autos clásicos."
            )),
            (t(
                "Can you work on a car that has been stored for years?",
                "¿Pueden atender un auto guardado durante años?"
            ), t(
                "Tell us how long it has been parked, whether it starts, and what you have checked. We can review the request and confirm the appropriate next step. Do not drive a car with suspected fuel leaks or unsafe brakes.",
                "Indique cuánto tiempo estuvo guardado, si arranca y qué ha revisado. Podemos evaluar la solicitud y confirmar el siguiente paso. No conduzca un auto con posibles fugas de combustible o frenos inseguros."
            )),
            (t(
                "Do you rebuild carburetors or specialize in points ignition?",
                "¿Reconstruyen carburadores o se especializan en encendido por platinos?"
            ), t(
                "Those specialized procedures are not confirmed by this page. Describe the vehicle and the exact task so the shop can say whether it is available.",
                "Esta página no confirma esos trabajos especializados. Describa el vehículo y la tarea exacta para que el taller pueda indicar si ofrece ese servicio."
            )),
            (t(
                "Can you repair a modified or restomod classic?",
                "¿Pueden reparar un auto clásico modificado o restomod?"
            ), t(
                "A modified vehicle needs a vehicle-specific review. Tell us about engine swaps, wiring changes and other modifications before arranging service; acceptance is not guaranteed.",
                "Un vehículo modificado requiere una evaluación específica. Informe sobre cambios de motor, cableado y otras modificaciones antes de solicitar servicio; la aceptación no está garantizada."
            )),
            (t(
                "Do classic cars need a Pennsylvania safety inspection?",
                "¿Los autos clásicos necesitan inspección de seguridad en Pensilvania?"
            ), t(
                "A classic plate is not the same as an antique plate. Pennsylvania's inspection regulations exempt antique vehicles, but not every vehicle people casually call a classic. Check the registration category and current PennDOT requirements.",
                "Una placa de vehículo clásico no es igual a una placa de vehículo antiguo. La normativa de Pensilvania exime de inspección a los vehículos registrados como antiguos, pero no a todos los que se llaman clásicos. Revise la categoría de matrícula y las reglas de PennDOT."
            )),
            (t(
                "Do you offer complete restorations, paint or body work?",
                "¿Ofrecen restauraciones completas, pintura o carrocería?"
            ), t(
                "No full restoration, paint or body-repair service is advertised here. This page focuses on discussing mechanical maintenance and repairs that may be appropriate for an older vehicle.",
                "Esta página no anuncia restauraciones completas ni trabajos de pintura o carrocería. Se centra en consultas sobre mantenimiento y reparaciones mecánicas que pueden corresponder a un vehículo antiguo."
            )),
        ],
        "cta": [
            ("h2", t(
                "Ready for the Next Sunday Drive?",
                "¿Listo para el próximo paseo de domingo?"
            )),
            ("p", t(
                "That next drive starts with a conversation. Tell Diverse Autoworks what you love about your classic—and what it needs right now. Share the year, make, model, engine, modifications and symptoms. [Request a callback](contact#request) or call us to discuss the mechanical work and confirm availability before bringing it in.",
                "El próximo paseo empieza con una conversación. Cuéntenos qué le gusta de su clásico y qué necesita hoy. Indique año, marca, modelo, motor, modificaciones y síntomas. [Solicite que le llamemos](contact#request) o comuníquese con nosotros para hablar del trabajo mecánico y confirmar disponibilidad antes de llevarlo."
            )),
        ],
        "search": (
            "classic car classic cars vintage car antique vehicle collector car restoration mechanical repair older car mechanic vintage engine classic brakes carburetor inquiry collector car stored car Pennsylvania inspections Phoenixville Chester County",
            "auto clásico autos clásicos vehículo antiguo auto de colección mecánico reparación vintage motor frenos mantenimiento autos antiguos inspección Pensilvania Phoenixville Chester County"
        ),
        "sources": [
            ("AAA — How To Care for Your Vintage Car", "https://www.acg.aaa.com/connect/blogs/4c/auto/how-to-care-for-your-vintage-car"),
            ("Hagerty — Your Year-Round Seasonal Guide to Classic Car Maintenance", "https://www.hagerty.com/resources/car-maintenance/seasonal-guide-to-classic-car-maintenance"),
            ("Pennsylvania Code — 67 Pa. Code § 175.4", "https://pacodeandbulletin.gov/secure/pacode/data/067/chapter175/s175.4.html"),
            ("NHTSA — Tire Safety and Aging", "https://www.nhtsa.gov/vehicle-safety/tires"),
            ("Petroleum Quality Institute of America — Motor Oils for Classic and Vintage Cars", "https://pqia.org/2021/04/15/motor-oils-for-classic-and-vintage-cars/amp/"),
            ("PennDOT — Specialty Vehicle Title and Registration", "https://www.pa.gov/agencies/dmv/vehicle-services/title-and-registration"),
        ],
        "verify": [
            "[VERIFY] Classic/vintage vehicle intake and year/model eligibility are handled case by case; do not advertise universal make/model acceptance.",
            "[VERIFY] Confirm scope for carburetors, distributor/points ignition, vintage wiring, parts sourcing and modifications. Do not advertise these as offered yet.",
            "[VERIFY] Do not imply body/paint restoration; body work was explicitly removed from the confirmed service list.",
        ],
    },
]
