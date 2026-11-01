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
                "Classic car repair in Phoenixville, PA. Ask Diverse Autoworks about mechanical maintenance, brakes, engine, cooling and electrical work on your vehicle.",
                "Reparación de autos clásicos en Phoenixville, PA. Consulte por mantenimiento, frenos, motor, enfriamiento y electricidad según su vehículo."
            ),
            "h1": t(
                "Classic Car Repair & Maintenance in Phoenixville, PA",
                "Reparación y mantenimiento de autos clásicos en Phoenixville, PA"
            ),
            "lead": t(
                "Keeping an older car on the road starts with understanding its condition, history and mechanical needs. Diverse Autoworks in Phoenixville offers a range of general mechanical repairs. Contact our team with the year, make, model and requested work so we can confirm what we can handle on your particular classic or vintage vehicle.",
                "Mantener un auto antiguo en circulación comienza por conocer su estado, historial y necesidades mecánicas. Diverse Autoworks en Phoenixville ofrece distintos servicios de reparación mecánica. Comuníquese con el taller e indique el año, la marca, el modelo y el trabajo solicitado para confirmar qué podemos atender en su vehículo clásico o antiguo."
            ),
            "crumb": t("Classic car repair", "Autos clásicos"),
        },
        "service_type": t(
            "Classic vehicle mechanical maintenance and repair inquiries",
            "Consultas sobre mantenimiento y reparación mecánica de autos clásicos"
        ),
        "blocks": [
            ("h2", t(
                "Classic Car Repair in Phoenixville: Start With the Car",
                "Reparación de autos clásicos en Phoenixville: primero, el vehículo"
            )),
            ("p", t(
                "A classic car is rarely just an older version of a modern daily driver. Its service history may be incomplete, the engine or transmission may have been replaced, and earlier repairs may have changed the original specifications. Two cars of the same model year can need very different work. Before suggesting a repair, it helps to know the vehicle's year, make, model, engine, current condition, modifications and how often it is driven. A car that runs every weekend raises different questions from one that has sat in storage for years.",
                "Un auto clásico no es simplemente una versión antigua de un vehículo moderno. Puede tener un historial de mantenimiento incompleto, un motor o una transmisión reemplazados y modificaciones hechas durante reparaciones anteriores. Dos autos del mismo año y modelo pueden necesitar trabajos muy distintos. Antes de recomendar una reparación conviene conocer el año, la marca, el modelo, el motor, el estado actual, las modificaciones y la frecuencia de uso. Un auto que sale cada fin de semana no presenta las mismas necesidades que otro guardado durante años."
            )),
            ("p", t(
                "Our shop's published mechanical services cover areas such as engines, brakes, steering, suspension, cooling, batteries, electrical problems and fuel systems. That general service list is not a promise that every procedure, vintage component or collector vehicle can be accepted. Older-car parts, equipment requirements and the extent of the job must be reviewed for the individual vehicle before an appointment is confirmed.",
                "Los servicios mecánicos publicados por el taller incluyen motores, frenos, dirección, suspensión, enfriamiento, baterías, electricidad y sistemas de combustible. Esa lista general no significa que podamos aceptar cualquier vehículo de colección, componente antiguo o procedimiento especializado. Debemos revisar la disponibilidad de piezas, los requisitos del trabajo y las características de cada vehículo antes de confirmar una visita."
            )),
            ("h2", t(
                "Warning Signs on an Older or Collector Car",
                "Señales de problemas en un auto antiguo o de colección"
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
                "Mechanical Services to Discuss for Your Classic Car",
                "Servicios mecánicos que puede consultar para su auto clásico"
            )),
            ("ul", [
                t("Engine concerns, ignition components and tune-up needs.", "Fallas de motor, componentes de encendido y necesidades de afinación."),
                t("Brake wear, brake fluid, steering and suspension condition.", "Desgaste de frenos, líquido de frenos y estado de la dirección y suspensión."),
                t("Radiator, cooling hoses, water pump and thermostat concerns.", "Problemas de radiador, mangueras, bomba de agua y termostato."),
                t("Battery, starting, charging and electrical-system problems.", "Problemas de batería, arranque, carga y sistema eléctrico."),
                t("Fuel delivery, tank concerns, leaks and exhaust issues.", "Suministro de combustible, tanque, fugas y problemas de escape."),
                t("Tires, wheel bearings, seals, fluids and routine maintenance.", "Llantas, rodamientos de rueda, juntas, líquidos y mantenimiento rutinario."),
            ]),
            ("p", t(
                "These are types of work within Diverse Autoworks' broader mechanical offering, not a fixed classic-car package. Acceptance depends on the vehicle and the specific task. For details, see [engine repair](svc_engine), [brake repair](svc_brakes), [cooling-system repair](svc_cooling), [electrical repair](svc_electrical), [battery service](svc_battery) and [rust and corrosion concerns](svc_rust). Discuss any unusual setup, non-original parts or specialized tools before scheduling.",
                "Estos trabajos forman parte de la oferta mecánica general de Diverse Autoworks; no constituyen un paquete fijo para autos clásicos. La aceptación depende del vehículo y de la tarea específica. Consulte nuestras páginas de [reparación de motor](svc_engine), [frenos](svc_brakes), [enfriamiento](svc_cooling), [reparación eléctrica](svc_electrical), [baterías](svc_battery) y [óxido y corrosión](svc_rust). Informe sobre modificaciones, piezas no originales o herramientas especiales antes de programar."
            )),
            ("h2", t(
                "Getting a Classic Car Back on the Road After Storage",
                "Cómo volver a circular con un auto clásico después de guardarlo"
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
                "Mechanical Repair Is Different From Full Restoration",
                "La reparación mecánica no es lo mismo que una restauración completa"
            )),
            ("p", t(
                "A mechanical repair aims to address a specific operating or safety concern. A restoration may involve body fabrication, paint, upholstery, cosmetic refinishing or a complete rebuild to original specifications. Those are separate projects with different equipment, parts and costs. This page discusses mechanical work, not full restoration, concours preparation, collision repair, custom fabrication or a guarantee of original-equipment parts. If your project includes those tasks, explain that scope when you contact the shop so expectations are clear.",
                "Una reparación mecánica busca resolver una falla de funcionamiento o seguridad. Una restauración puede incluir fabricación de carrocería, pintura, tapicería, acabados o reconstrucción completa según las especificaciones originales. Son proyectos distintos, con equipos, piezas y costos diferentes. Esta página trata sobre trabajos mecánicos; no ofrece restauraciones integrales, preparación para concursos, reparación de choques, fabricación personalizada ni una garantía de piezas originales. Si su proyecto incluye esas tareas, descríbalas al comunicarse con el taller."
            )),
            ("h2", t(
                "Pennsylvania Classic and Antique Vehicle Inspections",
                "Inspecciones de autos clásicos y antiguos en Pensilvania"
            )),
            ("p", t(
                "Pennsylvania uses specific registration categories for classic and antique vehicles, and the plate type matters. Under 67 Pa. Code § 175.4, antique vehicles are excluded from the normal safety-inspection requirement; a vehicle with classic plates does not automatically receive that same exemption. Registration eligibility and permitted use are separate questions from a car's mechanical condition. Check current PennDOT requirements for your exact registration, and see our [Pennsylvania inspection](inspections) and [tag and title](tags) information for related services.",
                "Pensilvania tiene categorías de registro específicas para vehículos clásicos y antiguos, y el tipo de placa importa. Según 67 Pa. Code § 175.4, los vehículos registrados como antiguos están exentos del requisito habitual de inspección de seguridad; una placa de vehículo clásico no concede automáticamente la misma exención. Las condiciones de registro y uso son distintas del estado mecánico del auto. Consulte las reglas vigentes de PennDOT según su matrícula y revise nuestra información sobre [inspecciones de Pensilvania](inspections) y [trámites de título y placas](tags)."
            )),
            ("h2", t(
                "Classic Car Service Near Phoenixville and Chester County",
                "Servicio para autos clásicos en Phoenixville y Chester County"
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
                "Ask About Classic Car Repair in Phoenixville, PA",
                "Consulte por reparación de autos clásicos en Phoenixville, PA"
            )),
            ("p", t(
                "Tell Diverse Autoworks about your classic car before arranging a visit. Include its year, make, model, engine, condition and the work you need. Use [our contact page](contact#request) to request a callback or call the shop to confirm availability.",
                "Cuéntenos sobre su auto clásico antes de llevarlo al taller. Indique año, marca, modelo, motor, estado y trabajo solicitado. Use [nuestra página de contacto](contact#request) para solicitar que le llamemos o comuníquese con el taller para confirmar disponibilidad."
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
            ("PennDOT — Specialty Vehicle Title and Registration", "https://www.pa.gov/agencies/dmv/vehicle-services/title-and-registration"),
        ],
        "verify": [
            "[VERIFY] Joe must confirm Diverse Autoworks accepts classic/vintage vehicles before publication.",
            "[VERIFY] Confirm scope for carburetors, distributor/points ignition, vintage wiring, parts sourcing and modifications. Do not advertise these as offered yet.",
            "[VERIFY] Do not imply body/paint restoration; body work was explicitly removed from the confirmed service list.",
        ],
    },
]
