# -*- coding: utf-8 -*-
"""
Fleet repairs page (/fleet-repairs/) body copy and the vehicle lookup, added Oct 31, 2026.

Spec: diverse-autoworks-fleet-page.md in the Claude project.
Scope decisions (Mujtaba, Oct 31, 2026):
- The shop services the common fleet vehicles, gas and diesel, including heavy-duty pickups,
  chassis cabs, dual-rear-wheel trucks and E-Series / Transit cutaways.
- Hybrids: inspections, tires, brakes and suspension only (same scope as the Tesla page).
- No EVs on this page.
Left out until the owner confirms: fleet billing, pricing, daily capacity, pickup, records, and the
"keep your inspection month" 90-day rule.

Block types are the same as brand_pages.py: ("h2", t), ("h3", t), ("p", t), ("ul", [t, ...]),
("table", (t, ...), [(t, ...), ...]). Links in text: [label](pagekey) or [label](pagekey#anchor).
"""


def t(en, es):
    return {"en": en, "es": es}


# ------------------------------------------------------------------ vehicle lookup
LOOKUP = {
    "h": t("Check your vehicle", "Consulte su vehículo"),
    "p": t("Type a make or model to see what we do for it.", "Escriba una marca o un modelo para ver qué trabajos le hacemos."),
    "label": t("Make or model", "Marca o modelo"),
    "ph": t("For example: Transit, F-250, Silverado, Sprinter", "Por ejemplo: Transit, F-250, Silverado, Sprinter"),
    "try": t("Popular:", "Más buscados:"),
    "chips": ["Transit", "F-150", "Super Duty", "ProMaster", "Sprinter", "Silverado", "Ram 2500", "Express"],
    "empty": t("Not on this list? Send the year, make and model in a [fleet inquiry](fleet#request) and we'll tell you.",
               "¿No aparece en la lista? Envíe el año, la marca y el modelo en una [solicitud de flota](fleet#request) y le responderemos."),
    "count1": t("1 match", "1 resultado"),
    "countn": t("{n} matches", "{n} resultados"),
    "details": t("{brand} service details", "Servicio {brand}"),
    "scope": {
        "full": t("Maintenance, repairs and PA inspections", "Mantenimiento, reparaciones e inspecciones de Pennsylvania"),
        "hybrid": t("Basic work: PA inspections, tires, alignments, brakes and suspension. No hybrid battery or high-voltage repairs.",
                    "Trabajos básicos: inspecciones de Pennsylvania, llantas, alineación, frenos y suspensión. No reparamos baterías híbridas ni sistemas de alto voltaje."),
    },
    "badge": {"full": t("Full service", "Servicio completo"), "hybrid": t("Hybrid", "Híbrido")},
}

TYPES = {
    "brand": t("Brand", "Marca"),
    "pickup": t("Pickup", "Pickup"),
    "hd": t("Heavy-duty pickup, gas and diesel", "Pickup de servicio pesado, gasolina y diésel"),
    "cab": t("Chassis cab, gas and diesel", "Chasis cabina, gasolina y diésel"),
    "van": t("Cargo and work van", "Van de carga y de trabajo"),
    "smallvan": t("Small cargo van", "Van de carga pequeña"),
    "cutaway": t("Cutaway, box truck and shuttle", "Cutaway, camión de caja y shuttle"),
    "suv": t("SUV", "SUV"),
    "sedan": t("Sedan", "Sedán"),
    "minivan": t("Minivan", "Minivan"),
    "hybrid": t("Hybrid", "Híbrido"),
}

# (display name: str, or t() when it has words to translate; brand name on the Brands hub; type; scope; extra search terms)
VEHICLES = [
    # Ford
    ("Ford F-150", "Ford", "pickup", "full", "f150 f 150"),
    ("Ford Ranger", "Ford", "pickup", "full", ""),
    ("Ford Maverick", "Ford", "pickup", "full", "ecoboost"),
    (t("Ford Super Duty F-250 and F-350", "Ford Super Duty F-250 y F-350"), "Ford", "hd", "full", "f250 f350 f 250 f 350 superduty power stroke powerstroke diesel"),
    (t("Ford F-450 and F-550", "Ford F-450 y F-550"), "Ford", "cab", "full", "f450 f550 super duty superduty dually drw power stroke powerstroke diesel"),
    ("Ford Transit", "Ford", "van", "full", "transit 150 250 350 cargo van diesel"),
    (t("Ford Transit cutaway and chassis cab", "Ford Transit cutaway y chasis cabina"), "Ford", "cutaway", "full", "box truck shuttle"),
    ("Ford E-Series cutaway", "Ford", "cutaway", "full", "e350 e450 e 350 e 450 econoline box truck shuttle bus"),
    ("Ford Transit Connect", "Ford", "smallvan", "full", ""),
    ("Ford Explorer", "Ford", "suv", "full", "police interceptor"),
    ("Ford Expedition", "Ford", "suv", "full", ""),
    ("Ford F-150 PowerBoost", "Ford", "hybrid", "hybrid", "f150 powerboost hybrid"),
    ("Ford Maverick Hybrid", "Ford", "hybrid", "hybrid", "hybrid"),
    # Chevrolet / GMC
    ("Chevrolet Silverado 1500", "Chevrolet", "pickup", "full", "chevy"),
    (t("Chevrolet Silverado 2500HD and 3500HD", "Chevrolet Silverado 2500HD y 3500HD"), "Chevrolet", "hd", "full", "chevy silverado hd 2500 3500 duramax diesel dually"),
    (t("Chevrolet Silverado 4500HD, 5500HD and 6500HD", "Chevrolet Silverado 4500HD, 5500HD y 6500HD"), "Chevrolet", "cab", "full", "chevy silverado hd 4500 5500 6500 duramax diesel"),
    ("Chevrolet Colorado", "Chevrolet", "pickup", "full", "chevy"),
    ("Chevrolet Express", "Chevrolet", "van", "full", "chevy 2500 3500 cargo van cutaway"),
    ("Chevrolet Tahoe", "Chevrolet", "suv", "full", "chevy ppv"),
    ("Chevrolet Suburban", "Chevrolet", "suv", "full", "chevy"),
    ("Chevrolet Traverse", "Chevrolet", "suv", "full", "chevy"),
    ("Chevrolet Equinox", "Chevrolet", "suv", "full", "chevy"),
    ("Chevrolet Malibu", "Chevrolet", "sedan", "full", "chevy"),
    ("GMC Sierra 1500", "GMC", "pickup", "full", ""),
    (t("GMC Sierra 2500HD and 3500HD", "GMC Sierra 2500HD y 3500HD"), "GMC", "hd", "full", "sierra hd 2500 3500 duramax diesel dually"),
    ("GMC Canyon", "GMC", "pickup", "full", ""),
    ("GMC Savana", "GMC", "van", "full", "2500 3500 cargo van cutaway"),
    # Ram / Stellantis
    ("Ram 1500", "Ram", "pickup", "full", "dodge"),
    (t("Ram 2500 and 3500", "Ram 2500 y 3500"), "Ram", "hd", "full", "dodge cummins diesel dually"),
    (t("Ram 4500 and 5500", "Ram 4500 y 5500"), "Ram", "cab", "full", "dodge chassis cab cummins diesel"),
    ("Ram ProMaster", "Ram", "van", "full", "promaster 1500 2500 3500 cargo van"),
    ("Ram ProMaster City", "Ram", "smallvan", "full", "promaster city"),
    ("Jeep Gladiator", "Jeep", "pickup", "full", ""),
    ("Jeep Grand Cherokee", "Jeep", "suv", "full", ""),
    ("Jeep Compass", "Jeep", "suv", "full", ""),
    ("Dodge Durango", "Dodge", "suv", "full", "pursuit"),
    ("Dodge Charger", "Dodge", "sedan", "full", "pursuit"),
    ("Dodge Grand Caravan", "Dodge", "minivan", "full", "cargo"),
    ("Chrysler Pacifica", "Chrysler", "minivan", "full", ""),
    ("Chrysler Voyager", "Chrysler", "minivan", "full", ""),
    # Mercedes-Benz
    ("Mercedes-Benz Sprinter", "Mercedes-Benz", "van", "full", "mercedes benz sprinter 2500 3500 cargo van diesel"),
    ("Mercedes-Benz Metris", "Mercedes-Benz", "smallvan", "full", "mercedes benz"),
    # Toyota
    ("Toyota Tacoma", "Toyota", "pickup", "full", ""),
    ("Toyota Tundra", "Toyota", "pickup", "full", ""),
    ("Toyota Corolla", "Toyota", "sedan", "full", ""),
    (t("Toyota Camry, 2024 and older", "Toyota Camry, 2024 y anteriores"), "Toyota", "sedan", "full", "camry"),
    ("Toyota Highlander", "Toyota", "suv", "full", ""),
    ("Toyota RAV4", "Toyota", "suv", "full", "rav 4"),
    (t("Toyota Sienna, 2020 and older", "Toyota Sienna, 2020 y anteriores"), "Toyota", "minivan", "full", "sienna"),
    (t("Toyota Camry, 2025 and newer", "Toyota Camry, 2025 y posteriores"), "Toyota", "hybrid", "hybrid", "camry hybrid"),
    (t("Toyota Sienna, 2021 and newer", "Toyota Sienna, 2021 y posteriores"), "Toyota", "hybrid", "hybrid", "sienna hybrid"),
    ("Toyota Prius", "Toyota", "hybrid", "hybrid", "hybrid"),
    ("Toyota RAV4 Hybrid", "Toyota", "hybrid", "hybrid", "rav 4 hybrid"),
    ("Toyota Tacoma i-FORCE MAX", "Toyota", "hybrid", "hybrid", "iforce max hybrid"),
    ("Toyota Tundra i-FORCE MAX", "Toyota", "hybrid", "hybrid", "iforce max hybrid"),
    # Nissan
    ("Nissan Frontier", "Nissan", "pickup", "full", ""),
    ("Nissan Titan", "Nissan", "pickup", "full", "xd"),
    ("Nissan NV", "Nissan", "van", "full", "nv1500 nv2500 nv3500 cargo van"),
    ("Nissan NV200", "Nissan", "smallvan", "full", "nv 200"),
    ("Nissan Altima", "Nissan", "sedan", "full", ""),
    ("Nissan Sentra", "Nissan", "sedan", "full", ""),
    ("Nissan Rogue", "Nissan", "suv", "full", ""),
    # Honda
    ("Honda Ridgeline", "Honda", "pickup", "full", ""),
    ("Honda Civic", "Honda", "sedan", "full", ""),
    ("Honda Accord", "Honda", "sedan", "full", ""),
    ("Honda CR-V", "Honda", "suv", "full", "crv"),
    ("Honda Odyssey", "Honda", "minivan", "full", ""),
    # Hyundai / Kia / Subaru
    ("Hyundai Santa Cruz", "Hyundai", "pickup", "full", ""),
    ("Hyundai Elantra", "Hyundai", "sedan", "full", ""),
    ("Hyundai Tucson", "Hyundai", "suv", "full", ""),
    ("Kia K5", "Kia", "sedan", "full", "optima"),
    ("Kia Sportage", "Kia", "suv", "full", ""),
    ("Kia Carnival", "Kia", "minivan", "full", ""),
    ("Subaru Outback", "Subaru", "suv", "full", ""),
    ("Subaru Forester", "Subaru", "suv", "full", ""),
]

# Brand rows: every brand page except Tesla (no EVs on this page).
LOOKUP_EXCLUDE_BRANDS = {"Tesla"}

# ------------------------------------------------------------------ page copy
PAGE = {
    "desc": t("Fleet repair in Phoenixville, PA: maintenance, brakes, PA inspections and tag and title work for business trucks and vans by ASE-certified technicians.",
              "Reparación de flotas en Phoenixville, PA: mantenimiento, frenos, inspecciones estatales y trámites de placas y títulos para camionetas y vans de trabajo."),
    "h1": t("Fleet Repair & Maintenance in Phoenixville, PA", "Reparación y mantenimiento de flotas en Phoenixville, PA"),
    "lead": t("Diverse Autoworks keeps business pickups, vans, SUVs and cars on the road. Our ASE-certified technicians handle maintenance, repairs, Pennsylvania state inspections, and tag and title work for your fleet, all at one shop in Phoenixville.",
              "Diverse Autoworks mantiene en marcha las camionetas, vans, SUV y autos de su negocio. Nuestros técnicos certificados por ASE se encargan del mantenimiento, las reparaciones, las inspecciones estatales de Pennsylvania y los trámites de placas y títulos de su flota, todo en un solo taller en Phoenixville."),
}

BLOCKS = [
    ("h2", t("Fleet service in Phoenixville, PA", "Servicio de flotas en Phoenixville, PA")),
    ("p", t("A work vehicle sitting in a bay is a job that isn't getting done. We service your vehicles for the way your business uses them and tell you what each one needs.",
            "Un vehículo de trabajo parado en el taller es un trabajo que no se está haciendo. Le damos servicio a sus vehículos según el uso que les da su negocio y le decimos qué necesita cada uno.")),
    ("p", t("Contractors, landscapers, HVAC, plumbing and electrical companies, delivery services, and sales and real estate teams all run vehicles that work harder than a daily commute. Whether you run one work truck or several, you can bring them to one shop for maintenance, repairs, inspections and paperwork.",
            "Contratistas, jardineros, empresas de calefacción y aire acondicionado, plomería y electricidad, servicios de entrega y equipos de ventas y bienes raíces usan vehículos que trabajan más que un auto de uso diario. Ya sea que tenga una camioneta de trabajo o varias, puede traerlas a un solo taller para el mantenimiento, las reparaciones, las inspecciones y los trámites.")),
    ("p", t("You don't need the dealer for routine service. Under federal law, a manufacturer or dealer can't deny your warranty coverage just because an independent shop did your routine maintenance. Keep your receipts from every service.",
            "No necesita ir al concesionario para el mantenimiento de rutina. Según la ley federal, un fabricante o concesionario no puede negarle la cobertura de la garantía solo porque un taller independiente hizo su mantenimiento de rutina. Guarde los recibos de cada servicio.")),

    ("h2", t("Business vehicles we service", "Vehículos de negocio que atendemos")),
    ("table", (t("Vehicle type", "Tipo de vehículo"), t("Examples", "Ejemplos")), [
        (t("Pickups", "Pickups"),
         t("Ford F-150 and Ranger, Chevrolet Silverado and Colorado, GMC Sierra and Canyon, Ram 1500, Toyota Tacoma and Tundra, Nissan Frontier",
           "Ford F-150 y Ranger, Chevrolet Silverado y Colorado, GMC Sierra y Canyon, Ram 1500, Toyota Tacoma y Tundra, Nissan Frontier")),
        (t("Heavy-duty pickups and chassis cabs", "Pickups de servicio pesado y chasis cabina"),
         t("Ford Super Duty F-250 through F-550, Chevrolet Silverado HD, GMC Sierra HD, Ram 2500 through 5500, including dual-rear-wheel trucks",
           "Ford Super Duty F-250 a F-550, Chevrolet Silverado HD, GMC Sierra HD, Ram 2500 a 5500, incluidas las de doble rueda trasera")),
        (t("Cargo and work vans", "Vans de carga y de trabajo"),
         t("Ford Transit, Ram ProMaster, Chevrolet Express, GMC Savana and Mercedes-Benz Sprinter",
           "Ford Transit, Ram ProMaster, Chevrolet Express, GMC Savana y Mercedes-Benz Sprinter")),
        (t("Box trucks and shuttles", "Camiones de caja y shuttles"),
         t("Ford E-Series and Transit cutaways", "Chasis cutaway Ford E-Series y Transit")),
        (t("SUVs, sedans and minivans", "SUV, sedanes y minivans"),
         t("Sales, service-call and real estate vehicles from the brands we service",
           "Vehículos de ventas, de servicio a domicilio y de bienes raíces de las marcas que atendemos")),
    ]),
    ("p", t("We service gas and diesel models. See the maintenance details for [Ford](brand_ford), [Chevrolet](brand_chevrolet), [GMC](brand_gmc), [Ram](brand_ram) and [Mercedes-Benz](brand_mercedes_benz), or browse [all the brands we service](brands).",
            "Atendemos modelos de gasolina y diésel. Vea los detalles de mantenimiento de [Ford](brand_ford), [Chevrolet](brand_chevrolet), [GMC](brand_gmc), [Ram](brand_ram) y [Mercedes-Benz](brand_mercedes_benz), o consulte [todas las marcas que atendemos](brands).")),
    ("h3", t("Hybrid fleet vehicles", "Vehículos híbridos de flota")),
    ("p", t("For hybrids, such as the Toyota Camry, Toyota Sienna and Ford Maverick Hybrid, we do basic work: Pennsylvania inspections, tires, alignments, brakes and suspension. We don't repair hybrid batteries or high-voltage systems.",
            "En los híbridos, como el Toyota Camry, el Toyota Sienna y la Ford Maverick Hybrid, hacemos trabajos básicos: inspecciones de Pennsylvania, llantas, alineación, frenos y suspensión. No reparamos baterías híbridas ni sistemas de alto voltaje.")),

    ("h2", t("Fleet maintenance for work use", "Mantenimiento de flotas para uso de trabajo")),
    ("p", t("Towing, hauling, idling on job sites, short trips and stop-and-go routes all count as severe service in most owner's manuals. Most fleet vehicles fall into that group, so they need service sooner than the same model driven gently.",
            "Remolcar, cargar peso, dejar el motor encendido en las obras, los viajes cortos y las rutas con muchas paradas cuentan como servicio severo en la mayoría de los manuales del propietario. Casi todos los vehículos de flota están en ese grupo, así que necesitan servicio antes que el mismo modelo con un uso ligero.")),
    ("p", t("Many work trucks set their own oil change timing. Here's how the common ones work:",
            "Muchas camionetas de trabajo calculan solas cuándo toca el cambio de aceite. Así funcionan las más comunes:")),
    ("table", (t("Make", "Marca"), t("What sets the oil change", "Qué indica el cambio de aceite"), t("Firm limit", "Límite fijo")), [
        (t("Ford (F-Series, Transit)", "Ford (Serie F, Transit)"), t("Intelligent Oil-Life Monitor", "El Intelligent Oil-Life Monitor"),
         t("1 year or 10,000 miles", "1 año o 10,000 millas")),
        (t("Chevrolet and GMC", "Chevrolet y GMC"), t("Engine Oil Life System", "El Engine Oil Life System"),
         t("At least once a year", "Al menos una vez al año")),
        (t("Ram (2025 Ram 1500)", "Ram (Ram 1500 2025)"), t("Oil change indicator", "Indicador de cambio de aceite"),
         t("10,000 miles, 12 months or 350 hours of engine run time", "10,000 millas, 12 meses o 350 horas de funcionamiento del motor")),
    ]),
    ("p", t("The 350-hour limit catches trucks that idle a lot: they can reach it long before 10,000 miles. We reset each monitor after the oil change, so the next reminder is accurate. Your owner's manual lists the severe-service schedule for each vehicle.",
            "El límite de 350 horas afecta a las camionetas que pasan mucho tiempo con el motor encendido: pueden llegar a ese límite mucho antes de las 10,000 millas. Reiniciamos cada monitor después del cambio de aceite para que el siguiente aviso sea correcto. El manual del propietario de cada vehículo indica el programa de servicio severo.")),
    ("h3", t("Keep one vehicle down at a time", "Un vehículo fuera de servicio a la vez")),
    ("p", t("Plan maintenance and inspections so only one vehicle is out of service at a time. A short list of what's due on each vehicle makes that easy, and we'll tell you what's coming up when each one is in.",
            "Planifique el mantenimiento y las inspecciones para que solo un vehículo esté fuera de servicio a la vez. Una lista corta de lo que le toca a cada vehículo lo hace fácil, y cada vez que uno venga le diremos qué servicio se acerca.")),

    ("h2", t("Fleet repairs in Phoenixville, PA", "Reparación de flotas en Phoenixville, PA")),
    ("p", t("When a vehicle breaks down, we diagnose the cause before we replace parts. Fleet work we do:",
            "Cuando un vehículo se descompone, diagnosticamos la causa antes de cambiar piezas. Trabajos que hacemos en vehículos de flota:")),
    ("ul", [
        t("Check engine light diagnosis and engine repair", "Diagnóstico de la luz de revisión del motor y reparación del motor"),
        t("Oil changes, filters and belts", "Cambios de aceite, filtros y correas"),
        t("Brakes, rotors and brake fluid flush", "Frenos, rotores y cambio de líquido de frenos"),
        t("Tires, rotation, balancing and alignments", "Llantas, rotación, balanceo y alineación"),
        t("Steering and suspension: ball joints, control arms, tie rods and sway bar links", "Dirección y suspensión: rótulas, brazos de control, terminales de dirección y bieletas de la barra estabilizadora"),
        t("Differential repair, wheel bearings and hubs, CV axles and joints", "Reparación del diferencial, baleros y mazas de rueda, ejes CV y juntas"),
        t("Drivetrain and transmission maintenance", "Mantenimiento del tren motriz y de la transmisión"),
        t("Cooling system, water pump and thermostat; A/C and heater service", "Sistema de enfriamiento, bomba de agua y termostato; servicio de aire acondicionado y calefacción"),
        t("Batteries, alternators and starters", "Baterías, alternadores y motores de arranque"),
        t("Timing belt and chain service, oil leaks and gaskets, motor and transmission mounts", "Correa y cadena de distribución, fugas de aceite y empaques, soportes de motor y de transmisión"),
        t("Exhaust, catalytic converters, oxygen sensors and emission control repair", "Escape, convertidores catalíticos, sensores de oxígeno y reparación del control de emisiones"),
        t("Corrosion and rust control", "Control de corrosión y óxido"),
    ]),
    ("p", t("See all our [auto repair services](services).", "Vea todos nuestros [servicios de reparación](services).")),

    ("h2", t("Pennsylvania inspections for fleet vehicles", "Inspecciones de Pennsylvania para vehículos de flota")),
    ("p", t("Every vehicle needs Pennsylvania's annual safety inspection. Whether it also needs an emissions test depends on its fuel, its weight rating and where it's registered.",
            "Todos los vehículos necesitan la inspección anual de seguridad de Pennsylvania. Si además necesitan la prueba de emisiones depende del combustible, del peso bruto vehicular nominal y de dónde estén registrados.")),
    ("table", (t("Vehicle registered in Chester or Montgomery County", "Vehículo registrado en el condado de Chester o Montgomery"),
               t("Safety inspection", "Inspección de seguridad"), t("Emissions test", "Prueba de emisiones")), [
        (t("Gas or hybrid, gross vehicle weight rating (GVWR) of 9,000 lb or less: most cars, SUVs and half-ton pickups",
           "Gasolina o híbrido, peso bruto vehicular nominal (GVWR) de 9,000 lb o menos: la mayoría de los autos, SUV y pickups de media tonelada"),
         t("Yes", "Sí"), t("Yes", "Sí")),
        (t("Gas, GVWR over 9,000 lb: many 3/4- and 1-ton pickups and vans", "Gasolina, GVWR de más de 9,000 lb: muchas pickups y vans de 3/4 y de 1 tonelada"),
         t("Yes", "Sí"), t("No", "No")),
        (t("Diesel", "Diésel"), t("Yes", "Sí"), t("No", "No")),
    ]),
    ("p", t("You'll find the GVWR on the label inside the driver's door. We do the safety inspection and emissions test at the same visit. See [state inspections](inspections).",
            "El GVWR aparece en la etiqueta del marco de la puerta del conductor. Hacemos la inspección de seguridad y la prueba de emisiones en la misma visita. Vea [inspecciones estatales](inspections).")),

    ("h2", t("Tag, title and notary services", "Placas, títulos y notario")),
    ("p", t("Diverse Autoworks is a PennDOT authorized agent. We handle [tag and title work](tags) and license plates for the vehicles your business buys and sells, at the same shop that maintains them. Our notary is available Monday through Friday, 8 a.m. to 3 p.m. See [notary services](contact#notary).",
            "Diverse Autoworks es agente autorizado de PennDOT. Hacemos los [trámites de placas y títulos](tags) de los vehículos que su negocio compra y vende, en el mismo taller que les da mantenimiento. Nuestro notario atiende de lunes a viernes, de 8 a. m. a 3 p. m. Vea [servicios de notario](contact#notary).")),
]

FAQ = [
    (t("What business vehicles do you service?", "¿Qué vehículos de negocio atienden?"),
     t("Gas and diesel pickups, heavy-duty pickups, chassis cabs, cargo vans, box trucks, SUVs, sedans and minivans, including the Ford F-150, Super Duty and Transit, Chevrolet Silverado and Express, GMC Sierra, Ram 1500 through 5500, Ram ProMaster and Mercedes-Benz Sprinter. For hybrids, we handle inspections, tires, brakes and suspension.",
       "Pickups de gasolina y diésel, pickups de servicio pesado, chasis cabina, vans de carga, camiones de caja, SUV, sedanes y minivans, incluidos el Ford F-150, Super Duty y Transit, Chevrolet Silverado y Express, GMC Sierra, Ram 1500 a 5500, Ram ProMaster y Mercedes-Benz Sprinter. En los híbridos, hacemos inspecciones y servicio de llantas, frenos y suspensión.")),
    (t("Can you do Pennsylvania inspections for all our vehicles?", "¿Pueden hacer las inspecciones de Pennsylvania de todos nuestros vehículos?"),
     t("Yes. We do the annual safety inspection and, for vehicles that need it, the emissions test at the same visit.",
       "Sí. Hacemos la inspección anual de seguridad y, en los vehículos que la necesitan, la prueba de emisiones en la misma visita.")),
    (t("Do our work trucks need an emissions test?", "¿Nuestras camionetas de trabajo necesitan la prueba de emisiones?"),
     t("Gas and hybrid vehicles with a GVWR of 9,000 lb or less that are registered in Chester or Montgomery County need one. Diesel vehicles and gas vehicles over 9,000 lb GVWR need only the safety inspection. The GVWR is on the label inside the driver's door.",
       "La necesitan los vehículos de gasolina e híbridos con un GVWR de 9,000 lb o menos registrados en el condado de Chester o Montgomery. Los vehículos diésel y los de gasolina con un GVWR de más de 9,000 lb solo necesitan la inspección de seguridad. El GVWR aparece en la etiqueta del marco de la puerta del conductor.")),
    (t("Can you handle tags, titles and plates for new fleet vehicles?", "¿Pueden hacer los trámites de placas y títulos de vehículos nuevos de la flota?"),
     t("Yes. Diverse Autoworks is a PennDOT authorized agent, so we handle tag and title work and issue plates. Our notary is available Monday through Friday, 8 a.m. to 3 p.m.",
       "Sí. Diverse Autoworks es agente autorizado de PennDOT, así que hacemos los trámites de placas y títulos y entregamos placas. Nuestro notario atiende de lunes a viernes, de 8 a. m. a 3 p. m.")),
    (t("What should I include in a fleet inquiry?", "¿Qué debo incluir en una solicitud de flota?"),
     t("The number of vehicles, the year, make and model of each, the work needed, your preferred scheduling and a contact person for your business.",
       "El número de vehículos, el año, la marca y el modelo de cada uno, el trabajo que necesitan, los horarios que prefiere y una persona de contacto de su negocio.")),
    (t("Will servicing fleet vehicles at an independent shop void the warranty?", "¿Darles servicio a los vehículos de flota en un taller independiente anula la garantía?"),
     t("No. Under federal law, a manufacturer or dealer can't deny warranty coverage just because someone other than the dealer did your routine maintenance. Keep your receipts from every service.",
       "No. Según la ley federal, un fabricante o concesionario no puede negar la cobertura de la garantía solo porque alguien que no es el concesionario hizo su mantenimiento de rutina. Guarde los recibos de cada servicio.")),
]

SETUP_NOTE = t("We'll talk through scheduling and billing with you before the first visit.",
               "Antes de la primera visita hablaremos con usted sobre los horarios y la facturación.")

CTA = [
    ("h2", t("Schedule fleet service near Phoenixville, PA", "Programe el servicio de flota cerca de Phoenixville, PA")),
    ("p", t("Contact Diverse Autoworks to set up maintenance, repairs or inspections for your business vehicles with an ASE-certified technician. Send a [fleet inquiry](fleet#request) or [request an appointment](contact#request) online.",
            "Comuníquese con Diverse Autoworks para programar el mantenimiento, las reparaciones o las inspecciones de los vehículos de su negocio con un técnico certificado por ASE. Envíe una [solicitud de flota](fleet#request) o [solicite una cita](contact#request) en línea.")),
]

SEARCH = ("fleet repair fleet maintenance fleet services business vehicles commercial work truck work van cargo van box truck chassis cab dually diesel heavy duty "
          "f-150 f-250 f-350 f-450 f-550 super duty ranger e-series transit promaster sprinter express savana silverado hd sierra hd ram 2500 3500 4500 5500 hybrid gvwr tag title",
          "reparación de flotas mantenimiento de flotas vehículos de negocio comerciales camionetas de trabajo vans de carga camiones de caja chasis cabina diésel servicio pesado "
          "f-150 f-250 f-350 super duty transit promaster sprinter express savana silverado sierra ram 2500 3500 híbridos placas títulos")
