# -*- coding: utf-8 -*-
"""Service pages batch 2: svc_fuel, svc_rust, svc_prepurchase, svc_hybrid. Written by ChatGPT, 2026-11-01. Needs fact check before publishing."""


def t(en, es):
    return {"en": en, "es": es}


SERVICE_PAGES = [
    {
        "key": "svc_fuel",
        "slug": "fuel-system-gas-tank",
        "covers": ["fuelsys"],
        "primary_kw": "gas tank repair Phoenixville",
        "secondary_kws": [
            "fuel tank leak", "gas smell near car", "fuel tank corrosion", "gas tank service",
            "fuel tank damage", "fuel odor after filling up", "gasoline leak under car",
            "fuel tank inspection", "fuel system warning signs", "car fuel storage",
            "fuel tank problems Chester County", "Pennsylvania fuel system inspection"
        ],
        "page": {
            "title": t(
                "Gas Tank Repair Phoenixville, PA | Diverse Autoworks",
                "Reparación tanque gasolina en Phoenixville, PA | Taller"
            ),
            "desc": t(
                "Gas tank repair Phoenixville: Diverse Autoworks assesses fuel-tank concerns and performs tank service and repair. Learn the warning signs and schedule a visit.",
                "Servicio de tanque de gasolina en Phoenixville. Diverse Autoworks evalúa problemas y repara tanques. Conozca las señales y solicite una cita."
            ),
            "h1": t(
                "Gas Tank Repair Phoenixville, PA",
                "Reparación de tanque de gasolina en Phoenixville, PA"
            ),
            "lead": t(
                "Gas tank repair Phoenixville drivers need starts with understanding where the concern comes from. At Diverse Autoworks in Phoenixville, PA, ASE-certified technicians provide gas tank service and repair. A fuel smell, visible wet spot or tank damage deserves attention before it becomes a larger safety concern.",
                "Si nota olor a gasolina, humedad debajo del vehículo o daños en el tanque, conviene atenderlo cuanto antes. En Diverse Autoworks, en Phoenixville, PA, nuestros técnicos certificados por ASE realizan servicio y reparación de tanques de gasolina. Primero es importante entender de dónde proviene el problema."
            ),
            "crumb": t("Gas tank repair", "Tanque de gasolina"),
        },
        "service_type": t("Gas tank service and repair", "Servicio y reparación del tanque de gasolina"),
        "blocks": [
            ("h2", t("Gas Tank Repair Phoenixville, PA: What the Tank Does", "Reparación de tanque de gasolina en Phoenixville, PA: su función")),
            ("p", t(
                "The fuel tank holds the gasoline a vehicle uses to run. It is one part of a larger fuel system that includes the filler area, lines, pump and components that deliver fuel to the engine. A tank issue is different from a problem with the engine's fuel injectors or ignition system, even though some symptoms can overlap. Describing exactly when you notice a smell, leak or change in the vehicle helps put the concern in context. The purpose of gas tank service is to address a problem with the tank itself, rather than assume that every fuel-related symptom means a tank repair is needed.",
                "El tanque almacena la gasolina que utiliza el vehículo. Forma parte de un sistema más amplio que incluye el área de llenado, las líneas, la bomba y los componentes que llevan combustible al motor. Un problema del tanque no es lo mismo que una falla de los inyectores o del encendido, aunque algunas señales puedan parecerse. Indique cuándo aparece el olor, la fuga o el cambio de funcionamiento. El servicio del tanque busca atender problemas del propio depósito, sin suponer que toda falla relacionada con combustible se origina allí."
            )),
            ("p", t(
                "Gasoline and its vapors create a fire risk when they escape the fuel system. If you see an active leak or strongly suspect one, do not start or drive the vehicle. Move away from ignition sources and arrange a safe way to have the issue assessed. A fuel smell is a reason to investigate, not proof that the tank is leaking. Fuel can be spilled during refueling, and problems elsewhere in the system may also produce an odor. Avoid trying to locate a suspected leak with a flame or by working beneath an unsupported vehicle.",
                "La gasolina y sus vapores pueden incendiarse si salen del sistema de combustible. Si observa una fuga activa o tiene motivos claros para sospecharla, no encienda ni conduzca el vehículo. Manténgase lejos de fuentes de ignición y organice una manera segura de revisar el problema. Un olor a gasolina requiere atención, pero no demuestra por sí solo que el tanque tenga una fuga. También puede haber combustible derramado al cargar o una falla en otra parte del sistema. Nunca busque una fuga con una llama ni se coloque debajo de un vehículo sin apoyo adecuado."
            )),
            ("h2", t("Signs You May Need Gas Tank Service", "Señales de que el tanque necesita atención")),
            ("ul", [
                t("A persistent gasoline odor around the vehicle, especially near the rear or after refueling.", "Olor persistente a gasolina alrededor del vehículo, sobre todo cerca de la parte trasera o después de cargar combustible."),
                t("A wet area or liquid under the vehicle that may be fuel rather than water.", "Una zona húmeda o líquido debajo del vehículo que pudiera ser combustible y no agua."),
                t("Visible damage or corrosion around the fuel tank area.", "Daño visible o corrosión cerca del tanque de gasolina."),
                t("A concern that began after the underside of the vehicle struck an object.", "Un problema que apareció después de golpear un objeto con la parte inferior del vehículo."),
                t("A fuel-related warning or symptom whose actual source has not yet been identified.", "Una advertencia o falla relacionada con combustible cuyo origen todavía no se ha identificado."),
            ]),
            ("p", t(
                "These signs do not identify a failed part by themselves. The source of a symptom should be established before anyone decides that a gas tank repair is the answer. For example, a damp patch may be unrelated condensation, and a fuel odor can come from several places. Note where the vehicle was parked, when the symptom occurred and if it followed a fill-up. Share those observations rather than guessing at a replacement part. If you suspect leaking gasoline, safety takes priority over gathering more clues by driving the car.",
                "Estas señales no identifican por sí solas una pieza dañada. Es necesario conocer el origen antes de decidir que el tanque requiere reparación. Por ejemplo, una mancha puede ser condensación y un olor a combustible puede venir de distintos lugares. Tome nota del lugar donde estaba estacionado, cuándo ocurrió y si fue después de cargar gasolina. Comparta esas observaciones en lugar de adivinar qué pieza cambiar. Si sospecha una fuga de gasolina, la seguridad importa más que seguir conduciendo para buscar pistas."
            )),
            ("h2", t("Gas Tank Work We Do", "Trabajos que realizamos en el tanque")),
            ("ul", [
                t("Gas tank service for concerns involving the tank itself.", "Servicio de tanque de gasolina para problemas relacionados con el propio depósito."),
                t("Gas tank repair when the condition and appropriate repair can be established.", "Reparación del tanque cuando se puede determinar su condición y la reparación adecuada."),
            ]),
            ("p", t(
                "The confirmed scope here is gas tank service and repair. That is intentionally narrower than promising a full menu of fuel-system work on this page. A fuel-system warning may involve the tank, but it may instead point to an engine, sensor, pump or line concern. Diverse Autoworks also provides engine diagnosis and repair on its separate engine service page. If the initial concern appears to be outside the tank, ask which service fits before approving work. Describing the symptom accurately makes it easier to discuss the next step without treating every gasoline odor as the same problem.",
                "El servicio confirmado para esta página es la atención y reparación del tanque de gasolina. No significa que se ofrezca aquí cualquier reparación posible del sistema de combustible. Una advertencia puede estar relacionada con el tanque, pero también con el motor, sensores, bomba o líneas. Diverse Autoworks ofrece diagnóstico y reparación de motor en una página independiente. Si el problema parece provenir de otra parte, pregunte qué servicio corresponde antes de autorizar trabajos. Una descripción precisa del síntoma ayuda a decidir el siguiente paso."
            )),
            ("h2", t("Why Fuel Tank Problems Should Not Be Ignored", "Por qué no conviene ignorar los problemas del tanque")),
            ("p", t(
                "Fuel is supposed to stay contained until the vehicle uses it. Damage from road debris, corrosion or wear can raise questions about the condition of the storage area. Not every stain is gasoline and not every smell calls for tank repair, but neither should be dismissed without knowing the source. If the problem involves a liquid fuel leak, the immediate concern is exposure to a flammable substance. If the concern is an odor without visible liquid, it still deserves an informed conversation about what was observed and the conditions under which it happens.",
                "El combustible debe permanecer contenido hasta que el vehículo lo utiliza. Los golpes de objetos en el camino, la corrosión o el desgaste pueden afectar el área de almacenamiento. No toda mancha es gasolina ni todo olor requiere reparar el tanque, pero tampoco conviene descartarlos sin conocer su origen. Si existe una fuga de combustible líquido, el riesgo inmediato es la exposición a una sustancia inflamable. Si hay olor sin líquido visible, también es importante explicar en qué circunstancias se presenta."
            )),
            ("p", t(
                "The owner's manual is the right starting point for vehicle-specific fuel information and maintenance guidance. It explains the recommended fuel type and how the manufacturer expects the vehicle to be operated. There is no universal tank-repair interval: a tank is addressed when a condition calls for attention, not simply because a generic calendar date has arrived. Keep track of unusual smells, changes after refueling and visible underside damage. Reporting the change early can help distinguish a new symptom from a longstanding one, without promising that every concern will require a repair.",
                "El manual del propietario es la referencia para conocer el combustible indicado y las recomendaciones específicas del vehículo. No existe un intervalo universal para reparar el tanque: se atiende cuando su condición lo requiere, no por una fecha general. Conviene observar olores inusuales, cambios después de cargar gasolina y daños visibles en la parte inferior. Informar cuándo comenzó una señal ayuda a diferenciar una falla reciente de una antigua, sin asumir que todos los casos necesitan reparación."
            )),
            ("h2", t("Fuel Systems and Pennsylvania Safety Inspections", "Sistema de combustible e inspecciones de seguridad en Pennsylvania")),
            ("p", t(
                "Pennsylvania's passenger-vehicle safety inspection includes the fuel system. That makes a suspected fuel leak relevant beyond everyday driving concerns, although a routine state inspection and a specific tank service are different appointments. If the vehicle is due for its state inspection, ask how the issues should be handled. You can review the shop's [state inspections](inspections) page. Some fuel-related warnings may also connect to emissions controls, but a tank concern should not be labeled an emissions failure until the underlying issue is known.",
                "La inspección estatal de seguridad de Pennsylvania incluye el sistema de combustible. Por eso una posible fuga importa tanto para la conducción como para la inspección, aunque una inspección general y un servicio específico del tanque son trabajos distintos. Si le corresponde la inspección, pregunte cómo tratar el problema. Consulte la página de [inspecciones estatales](inspections). Algunas advertencias también pueden relacionarse con las emisiones, pero no debe afirmarse que hay una falla de emisiones sin conocer la causa."
            )),
            ("p", t(
                "If it can't be driven, we can arrange or accept a tow, and we offer drop-off and after-hours arrangements. Diverse Autoworks is at 1415 Pawlings Road in Phoenixville, Chester County, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge. If your concern is an engine fuel-delivery problem rather than a tank problem, read about [engine diagnosis and repair](svc_engine). Related information is also available on [emissions-system repair](svc_emissions) and [rust and corrosion assessment](svc_rust). Use the service descriptions to explain the concern; you do not need to identify the part on your own.",
                "Si el vehículo no se puede conducir, podemos coordinar o recibir una grúa y ofrecemos arreglos de entrega y recogida fuera del horario. Diverse Autoworks está en 1415 Pawlings Road, Phoenixville, condado de Chester, a poca distancia en auto de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge. Si el problema está en la alimentación de combustible del motor y no en el tanque, consulte [diagnóstico y reparación de motor](svc_engine). También encontrará información sobre [reparación del sistema de emisiones](svc_emissions) y [evaluación de óxido y corrosión](svc_rust). Basta con describir lo que observa; no necesita identificar una pieza por su cuenta."
            )),
        ],
        "faq": [
            (t("Why does my car smell like gasoline after filling up?", "¿Por qué huele a gasolina mi auto después de cargar?"), t("Fuel may have been spilled during filling, or there may be a fuel-system concern. If the smell persists or you suspect a leak, do not keep driving to see whether it goes away; arrange an assessment.", "Puede haberse derramado combustible al cargar o existir un problema en el sistema. Si el olor persiste o sospecha una fuga, no siga conduciendo para ver si desaparece; solicite una evaluación.")),
            (t("Is a gas smell always a leaking fuel tank?", "¿El olor a gasolina siempre significa que el tanque tiene fuga?"), t("No. The tank is only one part of the fuel system. A smell should be investigated before choosing a repair.", "No. El tanque es solo una parte del sistema de combustible. Es necesario investigar el olor antes de elegir una reparación.")),
            (t("Can I drive with gasoline leaking under the car?", "¿Puedo conducir si hay gasolina goteando debajo del auto?"), t("No. Do not start or drive a vehicle with a suspected active gasoline leak. Keep clear of ignition sources and arrange safe transport.", "No. No encienda ni conduzca un vehículo si sospecha una fuga activa de gasolina. Evite fuentes de ignición y organice el traslado seguro.")),
            (t("Do you repair gas tanks in Phoenixville?", "¿Reparan tanques de gasolina en Phoenixville?"), t("Yes. Diverse Autoworks provides gas tank service and repair. Explain the symptoms and ask about the appropriate next step for your vehicle.", "Sí. Diverse Autoworks realiza servicio y reparación de tanques de gasolina. Explique los síntomas y consulte cuál es el siguiente paso para su vehículo.")),
            (t("Does a fuel tank problem affect Pennsylvania inspection?", "¿Un problema del tanque afecta la inspección de Pennsylvania?"), t("The fuel system is among the items checked in Pennsylvania passenger-vehicle safety inspections. The result depends on the vehicle's actual condition and applicable inspection criteria.", "El sistema de combustible forma parte de la inspección estatal de seguridad para automóviles de pasajeros en Pennsylvania. El resultado depende de la condición real del vehículo y de las reglas aplicables.")),
            (t("When should a fuel tank be serviced?", "¿Cuándo se debe revisar el tanque de gasolina?"), t("There is no one-size-fits-all tank repair schedule. Follow the owner's manual and address leaks, damage or persistent odors promptly.", "No hay un calendario universal para reparar el tanque. Siga el manual del propietario y atienda pronto las fugas, los daños o los olores persistentes.")),
        ],
        "cta": [
            ("h2", t("Schedule Gas Tank Service Near Phoenixville, PA", "Programe servicio del tanque cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule gas tank service with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Comuníquese con Diverse Autoworks para programar servicio del tanque de gasolina con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": (
            "gas tank repair gasoline tank fuel tank service fuel tank leak gas smell fuel odor petrol smell gas tank rust fuel tank corrosion fuel tank damage gas leak after fueling fuel tank Phoenixville Chester County tank service gas container fuel tank problems fuel system",
            "reparación tanque gasolina servicio depósito combustible fuga gasolina olor gasolina tanque oxidado corrosión tanque problema tanque combustible gotera de gasolina tanque Phoenixville condado Chester revisión depósito combustible"
        ),
        "sources": [
            ("Car Care Council — Vehicle Systems Overview: Fuel System", "https://www.carcare.org/vehicle-systems-overview/"),
            ("AAA Club Alliance — Identify Car Leaks Like a Pro", "https://cluballiance.aaa.com/the-extra-mile/advice/car/identify-leaks-like-a-pro"),
            ("PennDOT — Safety Inspection Program (Consumer FAQs)", "https://www.pa.gov/agencies/dmv/faqs/motor-vehicle-faqs/safety-inspection-consumers-faqs"),
            ("Pennsylvania Code — Passenger Car Safety Inspection Procedure", "https://pacodeandbulletin.gov/secure/pacode/data/067/chapter175/s175.80.html"),
        ],
        "verify": [
            "[VERIFY] Confirm which types of fuel-tank damage can be repaired rather than referred elsewhere; no specific method or replacement is promised.",
        ],
    },
    {
        "key": "svc_rust",
        "slug": "rust-corrosion-control",
        "covers": ["corrosion"],
        "primary_kw": "undercarriage rust repair Chester County",
        "secondary_kws": [
            "underbody corrosion", "car rust assessment", "vehicle rust treatment", "road salt corrosion",
            "surface rust versus structural rust", "frame rust inspection", "rust on suspension parts",
            "undercarriage rust Phoenixville", "winter road salt", "corroded vehicle underside",
            "rust prevention questions", "Pennsylvania inspection rust"
        ],
        "page": {
            "title": t(
                "Undercarriage Rust Repair Chester County | Phoenixville",
                "Óxido bajo el auto en Chester County | Phoenixville"
            ),
            "desc": t(
                "Undercarriage rust repair Chester County: Diverse Autoworks in Phoenixville assesses and treats vehicle rust and corrosion. Learn what needs closer attention.",
                "Diverse Autoworks en Phoenixville evalúa y trata óxido y corrosión debajo del vehículo en Chester County. Conozca las señales de alerta."
            ),
            "h1": t(
                "Undercarriage Rust Repair Chester County: Phoenixville, PA",
                "Evaluación y tratamiento de óxido bajo el auto en Phoenixville, PA"
            ),
            "lead": t(
                "Undercarriage rust repair Chester County vehicle owners search for begins with an honest assessment of the metal's condition. Diverse Autoworks in Phoenixville, PA assesses and treats vehicle corrosion and rust with ASE-certified technicians. The right conversation is about how extensive the corrosion is, not a promise that every rusted part can be restored.",
                "El óxido debajo del vehículo requiere evaluar su ubicación y gravedad antes de decidir qué hacer. Diverse Autoworks, en Phoenixville, PA, cuenta con técnicos certificados por ASE que evalúan y tratan la corrosión y el óxido. No todo metal oxidado puede recuperarse, por lo que conviene conocer primero la condición real."
            ),
            "crumb": t("Rust and corrosion", "Óxido y corrosión"),
        },
        "service_type": t("Rust assessment and corrosion treatment", "Evaluación del óxido y tratamiento de la corrosión"),
        "blocks": [
            ("h2", t("Undercarriage Rust Repair Chester County: Start With Assessment", "Óxido debajo del auto en Chester County: primero la evaluación")),
            ("p", t(
                "Rust forms when metal reacts with moisture and oxygen. Salt left on winter roads can make corrosion develop faster, particularly on exposed vehicle surfaces underneath the body. A vehicle can show light discoloration on one component and more serious deterioration on another. Those conditions should not be treated as interchangeable. Diverse Autoworks assesses corrosion and rust, then addresses treatment within its confirmed service scope. The goal of the initial conversation is to understand what area is affected and whether treatment is appropriate for the material in front of the technician.",
                "El óxido aparece cuando el metal reacciona con la humedad y el oxígeno. La sal utilizada en los caminos durante el invierno puede acelerar la corrosión, especialmente en superficies expuestas debajo del vehículo. Puede haber decoloración ligera en una pieza y deterioro serio en otra. No deben tratarse como situaciones iguales. Diverse Autoworks evalúa el óxido y la corrosión y ofrece tratamientos dentro de sus servicios confirmados. Primero hay que identificar la zona afectada y determinar si el tratamiento es adecuado para ese material."
            )),
            ("p", t(
                "People often use the phrase undercarriage rust repair for several different concerns: orange surface rust, flaking corrosion, a rusty fastener or deteriorated structural metal. These are not equivalent problems. Rust treatment cannot be assumed to restore metal that has already lost its strength. It is especially important to distinguish the appearance of a part from its structural condition. A coating or cosmetic change must never be taken as proof that a weakened frame is sound. If there is concern about serious deterioration, identifying that concern comes before discussing appearance.",
                "La expresión reparación de óxido bajo el auto puede referirse a cosas muy distintas: corrosión superficial anaranjada, escamas de metal, tornillos oxidados o deterioro de piezas estructurales. No son problemas equivalentes. Un tratamiento contra el óxido no recupera automáticamente la resistencia del metal que ya se ha perdido. Es importante separar la apariencia de una pieza de su estado estructural. Un recubrimiento o cambio de color no demuestra que un chasis debilitado sea seguro. Si existe deterioro serio, primero se debe reconocer ese riesgo."
            )),
            ("h2", t("Signs You Need a Rust and Corrosion Assessment", "Señales de que conviene evaluar el óxido y la corrosión")),
            ("ul", [
                t("Flaking rust or loose scale visible underneath the car.", "Óxido que se desprende en escamas debajo del automóvil."),
                t("Corrosion around exposed metal pieces and attachment points.", "Corrosión alrededor de piezas metálicas y puntos de sujeción."),
                t("A section of the underbody that looks noticeably different from nearby metal.", "Una zona inferior que se ve muy diferente del metal a su alrededor."),
                t("Rust that appears to have spread since a previous inspection.", "Óxido que parece haberse extendido desde la última revisión."),
                t("Concerns raised about the underside during a Pennsylvania safety inspection.", "Observaciones sobre la parte inferior durante una inspección de seguridad de Pennsylvania."),
            ]),
            ("p", t(
                "These are reasons to ask questions, not a diagnosis made from a photograph or a glance. The amount of visible discoloration does not always show how much usable metal remains. Do not scrape, strike or drill a component to test its strength yourself. A rust concern should be assessed before deciding on treatment, and a suspected structural problem deserves particular caution. When you contact the shop, explain where the corrosion appears, when it was first noticed and if an inspection station identified a specific issue.",
                "Son motivos para hacer preguntas, no diagnósticos que puedan darse solo por una fotografía. La cantidad de color oxidado no siempre indica cuánto metal resistente queda. No raspe, golpee ni perfore una pieza para comprobar su fuerza por su cuenta. Hay que evaluar la corrosión antes de elegir un tratamiento, especialmente si podría afectar una parte estructural. Al comunicarse con el taller, explique dónde está el óxido, desde cuándo lo observa y si una estación de inspección señaló algún problema concreto."
            )),
            ("h2", t("Rust and Corrosion Work We Do", "Servicios de óxido y corrosión que realizamos")),
            ("ul", [
                t("Assessment of vehicle rust and corrosion.", "Evaluación del óxido y la corrosión del vehículo."),
                t("Treatment of corrosion and rust where appropriate to the condition.", "Tratamiento del óxido y la corrosión cuando corresponde según su condición."),
            ]),
            ("p", t(
                "The published scope is assessing and treating rust and corrosion. It does not establish that the shop performs metal reconstruction, structural welding or replacement of rust-damaged frame sections. Those procedures should never be implied by the word treatment. Ask about the condition of the specific area and what kind of treatment, if any, is suitable before authorizing work. Sometimes the most useful outcome of an assessment is understanding the seriousness of the condition and the limits of a surface-focused approach.",
                "Los servicios publicados son evaluación y tratamiento del óxido y la corrosión. Eso no significa que el taller reconstruya metal, haga soldadura estructural o reemplace secciones dañadas del chasis. La palabra tratamiento no debe interpretarse como ese tipo de trabajo. Pregunte por la condición de la zona afectada y por el tratamiento adecuado, si existe, antes de autorizarlo. En algunos casos, lo más útil de la evaluación es saber qué tan serio es el deterioro y cuáles son los límites de una solución superficial."
            )),
            ("h2", t("Road Salt, Winter Moisture and Maintenance", "Sal de carretera, humedad invernal y mantenimiento")),
            ("p", t(
                "Chester County drivers see winter conditions that can leave moisture and road-treatment material on the underside of a vehicle. Salt and water help create conditions in which corrosion can spread. Keeping the underside reasonably clean after winter exposure and watching for changes are sensible ownership habits, but cleaning is not the same as repairing damaged metal. The vehicle owner's manual should guide any model-specific care or inspection interval. There is no single calendar interval that can tell every driver when rust treatment will be necessary.",
                "En Chester County, las condiciones invernales pueden dejar humedad y materiales usados para tratar las carreteras debajo del vehículo. El agua y la sal favorecen condiciones en las que el óxido puede avanzar. Mantener razonablemente limpia la parte inferior después del invierno y observar cambios son hábitos útiles, pero limpiar no equivale a reparar metal dañado. Consulte el manual del propietario para recomendaciones e intervalos específicos. No hay una fecha universal que indique cuándo todos los vehículos necesitarán tratamiento de corrosión."
            )),
            ("p", t(
                "Take care not to confuse prevention, treatment and repair. Prevention is about limiting future exposure where possible. Treatment addresses corrosion that is present and suitable for that approach. Repair of a failed structural member is a separate issue with different safety implications. If you are shopping for a used vehicle, visible rust is also a good reason to ask about its history and arrange an independent pre-purchase inspection. The presence of road salt alone does not prove that a car is unsafe, just as a clean-looking underside does not prove that every hidden surface is sound.",
                "Conviene distinguir prevención, tratamiento y reparación. La prevención busca reducir la exposición futura cuando sea posible. El tratamiento atiende la corrosión existente cuando es apropiado hacerlo. Reparar un componente estructural que ya falló es un asunto aparte, con consecuencias distintas para la seguridad. Si piensa comprar un auto usado, el óxido visible es motivo para preguntar por su historial y solicitar una inspección independiente antes de comprarlo. La presencia de sal no demuestra por sí sola que un vehículo sea inseguro, y una parte inferior limpia tampoco demuestra que todo esté en buen estado."
            )),
            ("h2", t("What Pennsylvania Inspection Rules Say About Rust", "Qué dicen las inspecciones de Pennsylvania sobre el óxido")),
            ("p", t(
                "Pennsylvania safety inspection rules consider the actual condition of the vehicle's frame and other specified parts. PennDOT has explained that rust on an exterior surface, by itself, is not an automatic failure under a blanket 'rust' rule. Structural deterioration is different: a frame that is not solid or has dangerously deteriorated components can fail the inspection. This is why an assessment should focus on the affected component and applicable criteria rather than calling all rust cosmetic or all rust a failure. For the shop's inspection offering, see [state inspections](inspections).",
                "Las reglas de inspección de seguridad de Pennsylvania consideran el estado real del chasis y otras piezas señaladas. PennDOT explica que el óxido visible en una superficie exterior no causa automáticamente un rechazo por una regla general sobre óxido. El deterioro estructural es distinto: un chasis que no está sólido o tiene componentes peligrosamente deteriorados puede reprobar. Por eso la evaluación debe centrarse en la pieza afectada y las reglas aplicables, sin decir que todo óxido es cosmético ni que todo óxido causa rechazo. Consulte [inspecciones estatales](inspections)."
            )),
            ("p", t(
                "Diverse Autoworks is located at 1415 Pawlings Road in Phoenixville, Chester County, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge. Rust concerns sometimes overlap with the condition of parts covered by [suspension repair](svc_suspension), [steering components](svc_steering) and [brake repair](svc_brakes), but each of those services has its own scope. If you are considering a used car with visible underside corrosion, see [pre-purchase inspections](svc_prepurchase). Those links help you ask about the right issue without assuming that rust treatment automatically includes other repairs.",
                "Diverse Autoworks se encuentra en 1415 Pawlings Road, Phoenixville, condado de Chester, a poca distancia en auto de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge. El óxido a veces coincide con problemas de piezas relacionadas con [suspensión](svc_suspension), [dirección](svc_steering) o [frenos](svc_brakes), pero cada servicio tiene su propio alcance. Si piensa comprar un auto usado con corrosión visible abajo, consulte [inspecciones antes de comprar](svc_prepurchase). Los enlaces ayudan a preguntar por el problema correcto sin suponer que el tratamiento del óxido incluye otras reparaciones."
            )),
        ],
        "faq": [
            (t("Does all undercarriage rust need repair?", "¿Todo el óxido debajo del auto necesita reparación?"), t("No. Light surface corrosion and damaged structural metal are different conditions. An assessment is needed before deciding what treatment, if any, is appropriate.", "No. La corrosión superficial ligera y el metal estructural deteriorado son condiciones distintas. Hay que evaluar el estado antes de decidir si conviene tratarlo.")),
            (t("Can rust cause a car to fail PA inspection?", "¿Puede el óxido hacer que un auto repruebe la inspección de PA?"), t("Yes, if corrosion results in a condition that meets a rejection criterion, such as a dangerously deteriorated frame. Visible exterior surface rust alone is not an automatic failure.", "Sí, si la corrosión provoca una condición que exige rechazar el vehículo, como un chasis peligrosamente deteriorado. El óxido superficial exterior por sí solo no significa rechazo automático.")),
            (t("Does road salt make undercarriage corrosion worse?", "¿La sal de carretera empeora la corrosión debajo del auto?"), t("Salt and moisture can accelerate corrosion on exposed metal. The extent of damage still depends on the vehicle and the condition of its parts.", "La sal y la humedad pueden acelerar la corrosión del metal expuesto. El daño real depende del vehículo y del estado de sus piezas.")),
            (t("Can rust treatment fix a weakened frame?", "¿Un tratamiento contra el óxido puede reparar un chasis debilitado?"), t("Do not assume so. Treating corrosion is not the same as restoring the strength of structurally damaged metal. The shop's confirmed scope is rust assessment and treatment.", "No debe suponerse. Tratar la corrosión no equivale a recuperar la resistencia de un metal estructural dañado. El servicio confirmado del taller es evaluar y tratar el óxido.")),
            (t("Do you assess rust in Phoenixville?", "¿Evalúan el óxido en Phoenixville?"), t("Yes. Diverse Autoworks assesses and treats corrosion and rust. Explain where you see it and any concerns noted during an inspection.", "Sí. Diverse Autoworks evalúa y trata la corrosión y el óxido. Explique dónde lo observa y si se señaló algún problema durante una inspección.")),
            (t("Should I check for rust before buying a used car?", "¿Debo revisar el óxido antes de comprar un auto usado?"), t("Yes. Visible corrosion is worth discussing as part of an independent pre-purchase evaluation. Ask in advance what the inspection covers.", "Sí. Vale la pena preguntar por la corrosión visible al solicitar una evaluación independiente antes de comprar. Consulte de antemano qué incluye la inspección.")),
        ],
        "cta": [
            ("h2", t("Schedule Rust and Corrosion Assessment Near Phoenixville, PA", "Programe una evaluación de óxido cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule rust and corrosion assessment with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online.", "Comuníquese con Diverse Autoworks para programar una evaluación de óxido y corrosión con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": (
            "undercarriage rust repair Chester County corrosion control underbody rust treatment surface rust frame rust assessment structural rust salt corrosion car rust chassis rust suspension corrosion rusty underside road salt Pennsylvania inspection rust Phoenixville",
            "óxido abajo auto corrosión debajo vehículo tratamiento óxido revisión chasis corrosión sal carretera óxido superficial daño estructural inspección estatal óxido Phoenixville Chester County evaluación corrosión"
        ),
        "sources": [
            ("PennDOT — Safety Bulletin on Rust and Frame Inspection", "https://www.pa.gov/content/dam/copapwp-pagov/en/dmv/documents/vehicle-services/bmv-safety-inspection-bulletins/bi23-03.pdf"),
            ("Pennsylvania Code — Passenger Car Inspection Procedure", "https://pacodeandbulletin.gov/secure/pacode/data/067/chapter175/s175.80.html"),
            ("U.S. Department of Energy — How Salt Ions Drive Corrosion", "https://www.energy.gov/science/articles/new-perspective-corrosive-problem"),
        ],
        "verify": [
            "[VERIFY] Owner to confirm treatment methods and which corrosion conditions can be addressed; no structural repair claim is made.",
        ],
    },
    {
        "key": "svc_prepurchase",
        "slug": "pre-purchase-inspection",
        "covers": ["prepurchase"],
        "primary_kw": "pre-purchase car inspection Phoenixville",
        "secondary_kws": [
            "used car inspection", "independent mechanic before buying", "pre-purchase vehicle check",
            "buying a used car Chester County", "used car warning signs", "vehicle history report",
            "used car inspection scope", "car inspection before purchase", "private seller car",
            "dealer used car", "Pennsylvania safety inspection versus pre-purchase",
            "used vehicle condition", "used car buyer questions"
        ],
        "page": {
            "title": t(
                "Pre-Purchase Car Inspection Phoenixville | Autoworks",
                "Inspección antes de comprar en Phoenixville | Taller"
            ),
            "desc": t(
                "Pre-purchase car inspection Phoenixville: Diverse Autoworks offers used-vehicle inspections. Call to ask what the inspection covers before you buy.",
                "Inspección de autos usados antes de comprar en Phoenixville con Diverse Autoworks. Llame para preguntar qué incluye la revisión."
            ),
            "h1": t(
                "Pre-Purchase Car Inspection Phoenixville, PA",
                "Inspección de auto antes de comprar en Phoenixville, PA"
            ),
            "lead": t(
                "A pre-purchase car inspection Phoenixville shoppers arrange can provide another perspective before a used-car purchase. Diverse Autoworks offers pre-purchase inspections in Phoenixville, PA with ASE-certified technicians. Call to ask what the inspection covers, since the shop has not published a fixed checklist for this service.",
                "Antes de comprar un auto usado, una inspección independiente puede aportar información adicional. Diverse Autoworks ofrece inspecciones previas a la compra en Phoenixville, PA, con técnicos certificados por ASE. Llame para preguntar qué incluye la inspección, ya que el taller no ha publicado una lista fija de puntos de revisión."
            ),
            "crumb": t("Pre-purchase inspection", "Inspección antes de comprar"),
        },
        "service_type": t("Pre-purchase used-vehicle inspection", "Inspección de vehículos usados antes de comprar"),
        "blocks": [
            ("h2", t("Pre-Purchase Car Inspection Phoenixville: Why Ask First?", "Inspección antes de comprar en Phoenixville: por qué consultar primero")),
            ("p", t(
                "Buying a used vehicle involves information you can see, information the seller provides and details you may not know yet. A test drive can tell you how the car feels on one outing, but it cannot answer every question about its condition. A vehicle history report may describe recorded events and title information, yet it is not a mechanical inspection. The Federal Trade Commission recommends getting a separate inspection from an independent mechanic before purchasing a used car. At Diverse Autoworks, the confirmed offering is a pre-purchase inspection; its exact checklist must be discussed before scheduling.",
                "Comprar un auto usado implica evaluar lo que puede observar, lo que dice el vendedor y lo que todavía desconoce. Una prueba de manejo permite sentir cómo se comporta el vehículo en ese momento, pero no responde todas las preguntas sobre su condición. Un reporte de historial puede mostrar registros y datos del título, pero no equivale a una inspección mecánica. La Comisión Federal de Comercio recomienda una inspección independiente antes de comprar. Diverse Autoworks ofrece este servicio; hay que consultar el alcance exacto antes de programarlo."
            )),
            ("p", t(
                "A seller's description, a clean exterior and an inspection sticker are separate pieces of information. None substitutes for asking informed questions about the vehicle you intend to buy. A state safety inspection focuses on defined safety criteria, while a pre-purchase inspection serves a buyer making a purchase decision. Do not assume that one inspection automatically includes everything covered by the other. Ask what the shop will examine, how findings will be communicated and what information you should bring. These are sensible questions to settle in advance, not promises about services or documents included in the appointment.",
                "La descripción del vendedor, una carrocería limpia y una calcomanía de inspección son datos distintos. Ninguno sustituye las preguntas sobre el vehículo que piensa adquirir. La inspección estatal se centra en criterios específicos de seguridad; la inspección antes de comprar ayuda al comprador a tomar una decisión. No suponga que una incluye automáticamente todo lo de la otra. Pregunte qué se revisará, cómo se comunicarán los hallazgos y qué información debe llevar. Son preguntas que conviene resolver de antemano, no promesas sobre pruebas o documentos incluidos."
            )),
            ("h2", t("Signs You Should Request a Used-Car Inspection", "Señales para solicitar una inspección de auto usado")),
            ("ul", [
                t("The seller cannot explain a warning light or an unusual sound.", "El vendedor no puede explicar una luz de advertencia o un ruido extraño."),
                t("The vehicle's maintenance history is incomplete or difficult to follow.", "El historial de mantenimiento está incompleto o es difícil de entender."),
                t("You notice uneven tire wear, unusual vibration or inconsistent braking on a test drive.", "Durante la prueba de manejo observa desgaste irregular de llantas, vibraciones o frenado inusual."),
                t("There are visible leaks, rust or signs of previous repairs that raise questions.", "Hay fugas visibles, óxido o señales de reparaciones anteriores que generan dudas."),
                t("The seller says an independent inspection is unnecessary because the car already passed a different check.", "El vendedor dice que no hace falta otra inspección porque el auto ya pasó una revisión distinta."),
            ]),
            ("p", t(
                "Those examples are prompts for a conversation, not proof of a defect or a list of items Diverse Autoworks promises to test. A vibration might have several causes; a warning lamp can point toward different systems. Asking for an independent opinion is useful even when nothing obvious seems wrong. The reason for a pre-purchase inspection is to make a decision with better information, not to guess at parts that need replacement. Any particular symptom should be understood in context before someone treats it as a confirmed repair need.",
                "Estos ejemplos sirven para conversar, no prueban una falla ni representan una lista de pruebas prometidas por Diverse Autoworks. Una vibración puede tener varias causas y una luz puede apuntar a distintos sistemas. Una opinión independiente también es útil cuando nada parece estar mal. La idea es decidir con más información, no adivinar qué piezas deben cambiarse. Cada síntoma necesita contexto antes de tratarse como una reparación confirmada."
            )),
            ("h2", t("Pre-Purchase Inspection Work We Do", "Servicio de inspección antes de comprar")),
            ("ul", [
                t("Pre-purchase inspections for used vehicles.", "Inspecciones de vehículos usados antes de comprar."),
                t("Discussion of the inspection scope by phone before the visit; call to ask what the inspection covers.", "Consulta telefónica previa sobre el alcance del servicio; llame para preguntar qué incluye la inspección."),
            ]),
            ("p", t(
                "The shop's published service description does not specify a standard set of checks. For that reason, this page does not promise a road test, scan, lift inspection, printed report or assessment of every vehicle system. Those details need to be discussed with the shop. When you call, identify the vehicle's make, model, year and any concerns you have already noticed. You can also ask how the vehicle should arrive and how to coordinate with the person selling it. Confirming the scope before a purchase decision avoids assuming that a broad service name means an unlimited inspection.",
                "La descripción publicada por el taller no indica una lista estándar de revisiones. Por eso esta página no promete una prueba de manejo, escaneo, elevación del vehículo, informe impreso ni evaluación de todos sus sistemas. Esos detalles deben consultarse directamente. Al llamar, indique la marca, el modelo, el año y cualquier problema que haya notado. También puede preguntar cómo debe llegar el vehículo y cómo coordinar con el vendedor. Aclarar el alcance antes de comprar evita pensar que el nombre del servicio incluye una revisión ilimitada."
            )),
            ("h2", t("What to Prepare Before Seeing a Used Car", "Qué preparar antes de ver un auto usado")),
            ("p", t(
                "Write down the questions that matter for your purchase rather than relying on memory at the seller's location. Request the vehicle identification number, commonly called the VIN, and compare available vehicle records. Ask for maintenance documents that the seller can provide. Check the vehicle's recall status through the official NHTSA recall lookup. A record can identify a reported event without telling you the entire mechanical condition of the car today. Keep the difference clear when weighing a report against what an independent inspection may reveal.",
                "Anote sus preguntas importantes antes de visitar al vendedor. Solicite el número de identificación del vehículo, conocido como VIN, y compare los registros disponibles. Pida los documentos de mantenimiento que el vendedor tenga. Consulte las campañas de retiro de seguridad en el buscador oficial de NHTSA. Un registro puede mostrar un hecho reportado, pero no necesariamente describir el estado mecánico actual del auto. Es importante distinguir el historial escrito de lo que una inspección independiente pueda encontrar."
            )),
            ("p", t(
                "Consider the car's intended use as well. A vehicle bought for commuting, longer trips or carrying family members may raise different questions for the buyer. Think about what changes in steering feel, braking, noise or warning lights you noticed during your own viewing of the car. Share observations without asking the shop to certify outcomes that are outside the agreed inspection. A pre-purchase inspection is a piece of evidence to consider alongside the vehicle's records, your own observations and the seller's answers. It cannot remove every uncertainty about future reliability.",
                "También piense cómo utilizará el vehículo. Un auto para ir al trabajo, viajar o transportar a la familia puede generar distintas preguntas. Recuerde qué notó sobre la dirección, el frenado, los ruidos o las luces de advertencia al ver el auto. Comparta esas observaciones sin pedir que el taller certifique aspectos que queden fuera de la inspección acordada. La revisión previa a la compra es una fuente de información que debe considerar junto con los registros del vehículo, sus observaciones y las respuestas del vendedor. No puede eliminar toda incertidumbre sobre el funcionamiento futuro."
            )),
            ("h2", t("Pennsylvania Safety Inspection Is a Separate Question", "La inspección estatal de Pennsylvania es otra cuestión")),
            ("p", t(
                "Pennsylvania has a safety inspection program with defined items and rejection criteria. Diverse Autoworks also offers [state safety inspections](inspections), but that existing service should not be confused with the pre-purchase visit described here. A current inspection sticker does not replace thoughtful research when deciding to buy a used car, and a pre-purchase visit does not automatically substitute for the state's official inspection requirements. Ask about the specific service you need. If you are buying the car in Pennsylvania, you can also consult the shop's existing [tags and title](tags) page for a separate administrative service.",
                "Pennsylvania tiene un programa de inspección de seguridad con puntos de revisión y criterios definidos. Diverse Autoworks también ofrece [inspecciones estatales de seguridad](inspections), pero ese servicio existente no debe confundirse con la visita previa a la compra. Una calcomanía vigente no reemplaza la investigación que conviene hacer antes de comprar, y una revisión previa no sustituye automáticamente los requisitos oficiales del estado. Pregunte por el servicio que necesita. Si compra el auto en Pennsylvania, también puede consultar [placas y títulos](tags), un servicio administrativo independiente."
            )),
            ("p", t(
                "Diverse Autoworks is at 1415 Pawlings Road in Phoenixville, Chester County, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge. If a vehicle's history raises specific questions, the site also explains [engine repair](svc_engine), [brake service](svc_brakes), [tires and alignment](svc_tires) and [rust and corrosion](svc_rust). Those links describe separate services, not an automatic checklist for this appointment. Before arranging the visit, call to ask what the pre-purchase inspection covers for the used vehicle you are considering.",
                "Diverse Autoworks está en 1415 Pawlings Road, Phoenixville, condado de Chester, a poca distancia en auto de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge. Si el historial plantea dudas específicas, el sitio también explica [reparación del motor](svc_engine), [servicio de frenos](svc_brakes), [llantas y alineación](svc_tires) y [óxido y corrosión](svc_rust). Esos enlaces describen servicios independientes, no una lista automática para esta cita. Antes de organizarla, llame para preguntar qué incluye la inspección previa a la compra del vehículo que está considerando."
            )),
        ],
        "faq": [
            (t("What does your pre-purchase car inspection include?", "¿Qué incluye su inspección de auto antes de comprar?"), t("The shop has not published a fixed checklist. Call Diverse Autoworks to ask what the inspection covers for the vehicle you are considering.", "El taller no ha publicado una lista fija. Llame a Diverse Autoworks para preguntar qué incluye la inspección del vehículo que piensa comprar.")),
            (t("Is a vehicle history report enough before buying a used car?", "¿Basta un reporte de historial para comprar un auto usado?"), t("No. The FTC explains that a history report does not replace an independent mechanical inspection. A report and an inspection answer different questions.", "No. La FTC explica que un historial no reemplaza una inspección mecánica independiente. El reporte y la inspección responden preguntas distintas.")),
            (t("Should I get a used car inspected even if it has a PA sticker?", "¿Debo revisar un auto usado aunque tenga calcomanía de PA?"), t("It is sensible to consider one. A state safety inspection addresses defined safety criteria, while a pre-purchase inspection helps you gather information for a buying decision.", "Es razonable considerarla. La inspección estatal verifica ciertos criterios de seguridad, mientras que una revisión previa ayuda a reunir información para decidir la compra.")),
            (t("Can I arrange an inspection before paying the seller?", "¿Puedo organizar una inspección antes de pagar al vendedor?"), t("That is the purpose of a pre-purchase inspection. Coordinate access with the seller and ask the shop about scheduling and scope before making commitments.", "Ese es el objetivo de una inspección previa a la compra. Coordine el acceso con el vendedor y consulte al taller sobre la cita y el alcance antes de comprometerse.")),
            (t("Will the inspection reveal every future problem?", "¿La inspección puede detectar todas las fallas futuras?"), t("No inspection can predict every future problem. Use its findings alongside vehicle records and the seller's information when making your decision.", "Ninguna inspección puede predecir todas las fallas futuras. Considere sus hallazgos junto con los registros del vehículo y la información del vendedor.")),
            (t("What information should I have when I call?", "¿Qué información necesito al llamar?"), t("Have the vehicle's make, model, year, seller coordination details and any specific concerns ready. Ask what the inspection covers before scheduling.", "Tenga a mano marca, modelo, año, detalles para coordinar con el vendedor y sus dudas específicas. Pregunte qué incluye la inspección antes de programarla.")),
        ],
        "cta": [
            ("h2", t("Schedule a Pre-Purchase Inspection Near Phoenixville, PA", "Programe una inspección antes de comprar cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule a pre-purchase inspection with an ASE-certified technician. Call to ask what the inspection covers, then send us a message or [request an appointment](contact#request) online.", "Comuníquese con Diverse Autoworks para programar una inspección antes de comprar con un técnico certificado por ASE. Llame para preguntar qué incluye la revisión; después envíenos un mensaje o [solicite una cita](contact#request) en línea.")),
        ],
        "search": (
            "pre-purchase car inspection Phoenixville used car inspection prepurchase inspection pre buy vehicle inspection mechanic before buying independent used auto check PPI vehicle history VIN secondhand car buyer car condition inspection dealership private seller Pennsylvania Chester County",
            "inspección antes de comprar auto usado revisión precompra mecánico independiente chequeo vehículo usado verificación de auto compra inspección mecánica VIN historial del vehículo compra particular concesionario Phoenixville condado Chester"
        ),
        "sources": [
            ("Federal Trade Commission — Buying a Used Car From a Dealer", "https://consumer.ftc.gov/articles/buying-used-car-dealer"),
            ("Federal Trade Commission — Used Cars", "https://consumer.ftc.gov/features/feature-0040-used-cars"),
            ("PennDOT — Safety Inspection Program", "https://www.pa.gov/agencies/dmv/vehicle-services/inspection-and-safety-requirements/safety-inspection-program"),
            ("NHTSA — Recalls Lookup", "https://www.nhtsa.gov/recalls"),
        ],
        "verify": [
            "[VERIFY] Owner must describe the exact inspection checklist and how findings are provided before any such claims are added to this page.",
        ],
    },
    {
        "key": "svc_hybrid",
        "slug": "hybrid-ev-service",
        "covers": ["ev"],
        "primary_kw": "hybrid car service Phoenixville",
        "secondary_kws": [
            "hybrid state inspection", "electric vehicle safety inspection", "EV tires and alignment",
            "hybrid brake service", "electric car suspension", "Tesla tire service",
            "Tesla state inspection", "hybrid alignment", "regenerative braking",
            "electric vehicle maintenance limits", "EV inspection Chester County",
            "hybrid emissions Pennsylvania", "electric vehicle brake inspection"
        ],
        "page": {
            "title": t(
                "Hybrid Car Service Phoenixville, PA | Diverse Autoworks",
                "Servicio híbridos en Phoenixville, PA | Taller"
            ),
            "desc": t(
                "Hybrid car service Phoenixville: Diverse Autoworks handles basic hybrid/EV inspections, tires, alignment, brakes and suspension. No high-voltage repairs.",
                "Servicio básico para híbridos y eléctricos en Phoenixville: inspecciones, llantas, alineación, frenos y suspensión. Sin reparaciones de alto voltaje."
            ),
            "h1": t(
                "Hybrid Car Service Phoenixville, PA",
                "Servicio de autos híbridos en Phoenixville, PA"
            ),
            "lead": t(
                "Hybrid car service Phoenixville drivers can request at Diverse Autoworks is limited to basic vehicle work. ASE-certified technicians in Phoenixville, PA perform state inspections, tire and alignment work, brake work and suspension service for eligible hybrids and electric vehicles. High-voltage battery, electric-drive and vehicle software repairs are not offered.",
                "Diverse Autoworks ofrece servicio básico para autos híbridos y eléctricos en Phoenixville, PA. Sus técnicos certificados por ASE realizan inspecciones estatales y trabajos de llantas, alineación, frenos y suspensión en vehículos admitidos. El taller no realiza reparaciones de baterías de alto voltaje, sistemas de propulsión eléctrica ni software del vehículo."
            ),
            "crumb": t("Hybrid and EV service", "Híbridos y eléctricos"),
        },
        "service_type": t("Basic hybrid and electric vehicle maintenance", "Servicio básico para híbridos y vehículos eléctricos"),
        "blocks": [
            ("h2", t("Hybrid Car Service Phoenixville, PA: What Is Included", "Servicio para autos híbridos en Phoenixville, PA: qué incluye")),
            ("p", t(
                "Hybrid and battery-electric vehicles use different power systems, but they still travel on tires, steer through suspension components and rely on brakes. That is the practical reason basic work remains relevant even when a vehicle does not rely exclusively on a gasoline engine. Diverse Autoworks offers a clearly limited selection of services for eligible hybrids and EVs. This is not a promise of comprehensive electric-vehicle repair. If you are unsure that a requested job falls in the permitted scope, describe the vehicle and the exact concern before scheduling so the distinction is clear.",
                "Los vehículos híbridos y completamente eléctricos utilizan sistemas de propulsión diferentes, pero siguen usando llantas, componentes de suspensión y frenos. Por eso los servicios básicos continúan siendo relevantes aunque el auto no dependa únicamente de un motor de gasolina. Diverse Autoworks ofrece una selección limitada de trabajos para híbridos y eléctricos admitidos. No se trata de un servicio integral de reparación de vehículos eléctricos. Si no sabe si un trabajo está incluido, indique el vehículo y el problema específico antes de programar."
            )),
            ("p", t(
                "A hybrid may combine an internal-combustion engine with an electric motor, while a fully electric vehicle uses electric propulsion. That difference matters when discussing maintenance and state emissions requirements. It does not change the limits of the shop's hybrid/EV service offering. The confirmed work here consists of state inspections, tires and alignments, brakes and suspension. There is no claim on this page of high-voltage testing, charging-system repair, traction-battery service, electric-motor repair or software troubleshooting. Questions about those systems should be directed to a provider that offers that specialization.",
                "Un híbrido puede combinar un motor de combustión con uno eléctrico; un vehículo completamente eléctrico utiliza propulsión eléctrica. La diferencia importa para el mantenimiento y los requisitos de emisiones. Sin embargo, no cambia los límites del servicio que ofrece el taller. Los trabajos confirmados son inspecciones estatales, llantas y alineaciones, frenos y suspensión. Esta página no ofrece pruebas de alto voltaje, reparación de carga, servicio de batería de tracción, reparación del motor eléctrico ni diagnóstico de software. Para esos sistemas, busque un proveedor especializado."
            )),
            ("h2", t("Signs Your Hybrid or EV Needs Basic Service", "Señales de que su híbrido o eléctrico necesita servicio básico")),
            ("ul", [
                t("Tires that show uneven tread wear or a change in road feel.", "Llantas con desgaste irregular o cambios en la sensación al manejar."),
                t("A steering wheel that sits off-center or a vehicle that pulls to one side.", "Un volante descentrado o un auto que se desvía hacia un lado."),
                t("Brake noises, changes in pedal feel or vibration when slowing down.", "Ruidos de frenos, cambios al pisar el pedal o vibraciones al reducir la velocidad."),
                t("Bumps accompanied by knocks or unusual suspension movement.", "Golpes en baches acompañados de ruidos o movimientos extraños de suspensión."),
                t("An upcoming Pennsylvania state safety inspection date.", "Una fecha próxima para la inspección estatal de seguridad de Pennsylvania."),
            ]),
            ("p", t(
                "These observations do not establish which part needs repair. A pull may have more than one cause, and a noise cannot be identified reliably from a short description. Tire, brake and suspension concerns should be evaluated before replacing parts. A warning related to the high-voltage system or electric drive, on the other hand, falls outside this shop's confirmed hybrid/EV scope. Do not describe such a warning as a basic brake or tire problem merely to fit it into the available services. Explain the actual message shown by the vehicle and seek the appropriate specialist if needed.",
                "Estas observaciones no identifican la pieza que necesita reparación. Un desvío puede tener distintas causas y un ruido no se puede diagnosticar solo con una descripción breve. Hay que evaluar problemas de llantas, frenos y suspensión antes de cambiar piezas. Una advertencia sobre el sistema de alto voltaje o la propulsión eléctrica, en cambio, queda fuera del servicio confirmado del taller. No presente esa advertencia como un problema sencillo de llantas o frenos solo para incluirlo en la lista. Describa el mensaje real del vehículo y consulte a un especialista cuando corresponda."
            )),
            ("h2", t("Hybrid and EV Work We Do", "Trabajos que realizamos en híbridos y eléctricos")),
            ("h3", t("State Safety Inspections", "Inspecciones estatales de seguridad")),
            ("p", t(
                "State safety inspections are included for eligible hybrid and electric vehicles. The official inspection follows Pennsylvania criteria; it is not a high-voltage system health assessment. For the shop's existing inspection service, see [state inspections](inspections). If the vehicle has a model-specific issue beyond the state inspection, describe it separately rather than assuming the inspection includes specialized EV diagnosis.",
                "Las inspecciones estatales de seguridad se ofrecen para híbridos y eléctricos admitidos. La inspección oficial sigue los criterios de Pennsylvania; no es una evaluación del sistema de alto voltaje. Consulte [inspecciones estatales](inspections). Si su auto presenta un problema particular fuera de la inspección, explíquelo por separado y no suponga que el trámite incluye diagnóstico especializado de vehículos eléctricos."
            )),
            ("h3", t("Tires and Alignments", "Llantas y alineaciones")),
            ("p", t(
                "Tires carry the load and maintain contact with the road regardless of how the vehicle is powered. Tire wear, pressure and alignment questions remain important on a hybrid or EV. Diverse Autoworks performs tire and alignment work within the allowed basic scope. The owner's manual and tire information label are the starting points for vehicle-specific requirements. See [tires and alignment](svc_tires) for the existing service page rather than expecting a separate set of promises for electric cars.",
                "Las llantas soportan el peso del vehículo y mantienen el contacto con el camino sin importar cómo se impulse. El desgaste, la presión y la alineación también importan en híbridos y eléctricos. Diverse Autoworks realiza trabajos de llantas y alineación dentro de su alcance básico. El manual y la etiqueta de información de llantas indican los requisitos del modelo. Consulte [llantas y alineación](svc_tires), la página existente de ese servicio."
            )),
            ("h3", t("Brakes and Suspension", "Frenos y suspensión")),
            ("p", t(
                "Many electrified vehicles use regenerative braking to recover energy, but they still have conventional friction-braking components. Brake concerns should not be dismissed because regeneration is present. The shop's allowed hybrid/EV work includes brakes and suspension, the mechanical systems that help control stopping and road contact. See the established [brake repair](svc_brakes) and [suspension repair](svc_suspension) pages for those services. Nothing in this scope authorizes work on high-voltage components tied to the propulsion system.",
                "Muchos vehículos electrificados utilizan frenado regenerativo para recuperar energía, pero también conservan componentes de fricción en los frenos. No se debe ignorar un problema de frenos porque exista regeneración. El servicio permitido incluye frenos y suspensión, sistemas mecánicos que ayudan a detener el auto y mantener contacto con el camino. Consulte [reparación de frenos](svc_brakes) y [reparación de suspensión](svc_suspension). Este alcance no incluye trabajos en componentes de alto voltaje del sistema de propulsión."
            )),
            ("h2", t("Tesla Service and Vehicle Brands We Cannot Take", "Servicio para Tesla y marcas que no atendemos")),
            ("p", t(
                "For Tesla vehicles, Diverse Autoworks limits service to state inspections, tires, brakes and suspension. Ask specifically about alignment before assuming it is included for a Tesla, because the Tesla-specific confirmed list does not separately name it. The shop does not repair Rivian, Lucid, Karma or Polestar vehicles. These are service boundaries, not statements about a brand's quality or reliability. Describe your exact model and requested work before planning a visit; the shop can only accept a job that fits its stated scope.",
                "Para Tesla, Diverse Autoworks limita el servicio a inspecciones estatales, llantas, frenos y suspensión. Pregunte específicamente por la alineación antes de asumir que se incluye para Tesla, ya que la lista confirmada para esa marca no la menciona por separado. El taller no repara vehículos Rivian, Lucid, Karma ni Polestar. Son límites del servicio, no opiniones sobre la calidad o confiabilidad de las marcas. Indique el modelo y el trabajo que necesita antes de planear su visita."
            )),
            ("h2", t("Maintenance and Pennsylvania Emissions Rules", "Mantenimiento y reglas de emisiones de Pennsylvania")),
            ("p", t(
                "Use the owner's manual to identify inspection and maintenance intervals for the exact vehicle. Electrified vehicles do not all share one schedule, and their brake and tire needs can differ by model and use. In Chester County, gasoline-powered hybrids can be subject to Pennsylvania emissions testing when they meet the program's criteria. Fully electric vehicles do not undergo gasoline emissions testing, although state safety inspection requirements can still apply. Diesel vehicles also fall outside the gasoline emissions test. Ask about the correct inspection for your registration and vehicle type rather than assuming the rules are identical for every hybrid and EV.",
                "Consulte el manual del propietario para conocer los intervalos de inspección y mantenimiento de su modelo. Los vehículos electrificados no comparten un único calendario; las necesidades de frenos y llantas varían. En Chester County, los híbridos con motor de gasolina pueden necesitar prueba de emisiones si cumplen los criterios del programa de Pennsylvania. Los eléctricos puros no pasan la prueba de emisiones de gasolina, aunque todavía pueden requerir inspección estatal de seguridad. Los vehículos diésel también quedan fuera de esa prueba de gasolina. Pregunte qué inspección corresponde a su tipo de vehículo y registro."
            )),
            ("p", t(
                "Diverse Autoworks is at 1415 Pawlings Road in Phoenixville, Chester County, a short drive from Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs and Valley Forge. For a gas-powered hybrid with a separate conventional-engine issue, this hybrid/EV page should not be read as authorization for additional repair categories. Use the [engine repair](svc_engine) page to understand the shop's general engine offering, then ask which specific work is accepted for your hybrid. The same distinction applies to other linked services: a published page is not an automatic promise that its entire scope applies to every EV model.",
                "Diverse Autoworks está en 1415 Pawlings Road, Phoenixville, condado de Chester, a poca distancia en auto de Spring City, Royersford, Collegeville, Oaks, Kimberton, Chester Springs y Valley Forge. Si un híbrido de gasolina tiene un problema independiente en el motor de combustión, esta página no autoriza otras categorías de reparación. Consulte [reparación de motor](svc_engine) para conocer el servicio general y pregunte qué trabajo específico se acepta para su híbrido. Lo mismo ocurre con los demás servicios: la existencia de una página no significa que todas sus tareas se ofrezcan para cualquier modelo eléctrico."
            )),
        ],
        "faq": [
            (t("Does Diverse Autoworks work on hybrid cars?", "¿Diverse Autoworks atiende autos híbridos?"), t("Yes, for basic services: state inspections, tires and alignment, brakes and suspension. High-voltage battery, electric-drive and software repairs are outside the offered scope.", "Sí, para servicios básicos: inspecciones estatales, llantas y alineación, frenos y suspensión. No ofrece reparaciones de baterías de alto voltaje, propulsión eléctrica ni software.")),
            (t("Can you service a Tesla in Phoenixville?", "¿Pueden atender un Tesla en Phoenixville?"), t("Tesla service is limited to state inspections, tires, brakes and suspension. Ask about the exact requested job before scheduling.", "El servicio para Tesla se limita a inspecciones estatales, llantas, frenos y suspensión. Consulte el trabajo específico antes de programar.")),
            (t("Do you replace hybrid or EV high-voltage batteries?", "¿Cambian baterías de alto voltaje de híbridos o eléctricos?"), t("No. Diverse Autoworks does not offer high-voltage battery repair or replacement for hybrid or electric vehicles.", "No. Diverse Autoworks no ofrece reparación ni reemplazo de baterías de alto voltaje de vehículos híbridos o eléctricos.")),
            (t("Do you repair Rivian, Lucid, Karma or Polestar?", "¿Reparan Rivian, Lucid, Karma o Polestar?"), t("No. The shop does not offer repairs for those brands.", "No. El taller no ofrece reparaciones para esas marcas.")),
            (t("Do electric vehicles need Pennsylvania emissions testing?", "¿Los autos eléctricos necesitan prueba de emisiones en Pennsylvania?"), t("Fully electric vehicles are not subject to the gasoline emissions test. Pennsylvania safety inspection requirements can still apply, and gas-powered hybrids may need emissions testing when covered by the program.", "Los eléctricos puros no están sujetos a la prueba de emisiones de gasolina. Pueden seguir sujetos a inspección estatal de seguridad, y algunos híbridos con motor de gasolina necesitan prueba de emisiones según el programa.")),
            (t("Do EVs still need brake and tire attention?", "¿Los eléctricos todavía necesitan revisar frenos y llantas?"), t("Yes. Electric vehicles use tires and friction brakes even if they also use regenerative braking. Refer to the owner's manual for the vehicle-specific maintenance schedule.", "Sí. Los eléctricos usan llantas y frenos de fricción aunque también tengan frenado regenerativo. Consulte el manual del propietario para los intervalos del modelo.")),
            (t("Can you fix a charging or electric-drive warning?", "¿Pueden reparar una falla de carga o propulsión eléctrica?"), t("No. Charging-system, electric-drive, high-voltage and software work is not part of the confirmed basic hybrid/EV service. Seek a qualified provider for that concern.", "No. Los trabajos de carga, propulsión eléctrica, alto voltaje y software no forman parte del servicio básico confirmado. Consulte a un proveedor especializado.")),
        ],
        "cta": [
            ("h2", t("Schedule Basic Hybrid or EV Service Near Phoenixville, PA", "Programe servicio básico para híbridos y eléctricos cerca de Phoenixville, PA")),
            ("p", t("Contact Diverse Autoworks to schedule eligible basic hybrid or EV service with an ASE-certified technician. Send us a message or [request an appointment](contact#request) online, describing the model and requested work.", "Comuníquese con Diverse Autoworks para programar servicio básico permitido para híbridos o eléctricos con un técnico certificado por ASE. Envíenos un mensaje o [solicite una cita](contact#request) en línea, indicando el modelo y el trabajo que necesita.")),
        ],
        "search": (
            "hybrid car service Phoenixville hybrid vehicle basic service electric vehicle EV state inspection EV brakes hybrid tires alignment suspension Tesla tires brake service Tesla inspection regenerative braking hybrid emissions Chester County hybrid mechanic electric car maintenance",
            "servicio automóvil híbrido Phoenixville vehículo eléctrico inspección estatal llantas alineación frenos suspensión Tesla servicio básico inspección Tesla frenado regenerativo emisiones híbridos condado Chester auto eléctrico mantenimiento"
        ),
        "sources": [
            ("U.S. Department of Energy — Maintenance and Safety of Electric Vehicles", "https://afdc.energy.gov/vehicles/electric-maintenance"),
            ("PennDOT — Safety Inspection Program", "https://www.pa.gov/agencies/dmv/vehicle-services/inspection-and-safety-requirements/safety-inspection-program"),
            ("PennDOT — Emissions Inspection Program", "https://www.pa.gov/agencies/dmv/vehicle-services/inspection-and-safety-requirements/emission-inspections-program"),
            ("Pennsylvania Code — Subject Vehicles for Emissions Inspection", "https://regulations.justia.com/states/pennsylvania/title-67/part-i/subpart-a/article-vii/chapter-177/subchapter-b/section-177-101/"),
        ],
        "verify": [
            "[VERIFY] Confirm model-by-model acceptance before publishing any broader hybrid, EV or Tesla service claims; Tesla alignment is not assumed.",
        ],
    },
]