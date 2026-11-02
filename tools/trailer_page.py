# -*- coding: utf-8 -*-
"""Owner-approved trailer service details and searchable bilingual trailer directory.
Trailer-weight limit: 10,000 pounds or less, not towing-vehicle weight and not
an asserted GVWR limit. Each listed type is an inquiry category, not a promise
of service for every trailer or specialty appliance.
"""
def t(en, es):
    return {"en": en, "es": es}

PAGE = {
    "title": t("Trailer Repair Phoenixville, PA | Diverse Autoworks",
               "Reparación de remolques Phoenixville | Diverse Autoworks"),
    "desc": t("Trailer repair and maintenance in Phoenixville, PA. Most makes and models, trailer weight up to 10,000 lb. Call 610-650-0316.",
              "Reparación de remolques en Phoenixville, PA. La mayoría de marcas y modelos, hasta 10,000 lb de peso. Llame al 610-650-0316."),
    "h1": t("Trailer Repair & Maintenance in Phoenixville, PA",
            "Reparación y mantenimiento de remolques en Phoenixville, PA"),
    "lead": t("We work on most makes and models of trailers weighing 10,000 pounds (4,536 kg) or less. Tell us about your trailer and the problem so we can confirm the work.",
              "Atendemos la mayoría de marcas y modelos de remolques que pesen 10,000 libras (4,536 kg) o menos. Cuéntenos sobre su remolque y el problema para confirmar el trabajo."),
}
GROUPS = [
    (t("Utility & Cargo", "Utilitarios y de carga"), [
        t("Utility trailers", "Remolques utilitarios"), t("Single-axle utility trailers", "Remolques utilitarios de un eje"),
        t("Tandem-axle utility trailers", "Remolques utilitarios de dos ejes"), t("Open cargo trailers", "Remolques de carga abiertos"),
        t("Enclosed cargo trailers", "Remolques de carga cerrados"), t("Box trailers", "Remolques tipo caja"),
        t("Flatbed trailers", "Remolques de plataforma"), t("Deckover trailers", "Remolques de plataforma sobre ruedas"),
        t("Tilt-deck trailers", "Remolques de plataforma inclinable")]),
    (t("Landscaping & Construction", "Jardinería y construcción"), [
        t("Landscaping trailers", "Remolques de jardinería"), t("Enclosed landscaping trailers", "Remolques de jardinería cerrados"),
        t("Lawn mower trailers", "Remolques para cortacéspedes"), t("Equipment trailers", "Remolques para maquinaria"),
        t("Skid-steer trailers", "Remolques para minicargadoras"), t("Mini-excavator trailers", "Remolques para miniexcavadoras"),
        t("Compact tractor trailers", "Remolques para tractores compactos"), t("Dump trailers", "Remolques basculantes"),
        t("Construction material trailers", "Remolques para materiales de construcción"),
        t("Contractor tool trailers", "Remolques de herramientas para contratistas")]),
    (t("Vehicle & Powersports", "Vehículos y deportes de motor"), [
        t("Open car haulers", "Remolques abiertos para autos"), t("Enclosed car haulers", "Remolques cerrados para autos"),
        t("Classic car transport trailers", "Remolques para autos clásicos"), t("Race car trailers", "Remolques para autos de carrera"),
        t("Motorcycle trailers", "Remolques para motocicletas"), t("ATV trailers", "Remolques para vehículos todoterreno ATV"),
        t("UTV / side-by-side trailers", "Remolques para vehículos UTV"), t("Golf cart trailers", "Remolques para carritos de golf"),
        t("Snowmobile trailers", "Remolques para motos de nieve"), t("Tow dollies", "Plataformas de remolque de dos ruedas")]),
    (t("Marine & Outdoor", "Náuticos y recreativos"), [
        t("Boat trailers", "Remolques para barcos"), t("Pontoon boat trailers", "Remolques para pontones"),
        t("Sailboat trailers", "Remolques para veleros"), t("Personal watercraft / Jet Ski trailers", "Remolques para motos acuáticas"),
        t("Kayak trailers", "Remolques para kayaks"), t("Canoe trailers", "Remolques para canoas"),
        t("Pop-up camper trailers", "Remolques camper plegables"), t("Teardrop camping trailers", "Remolques camper tipo lágrima"),
        t("Lightweight travel trailers", "Remolques de viaje ligeros")]),
    (t("Farm & Livestock", "Agrícolas y ganaderos"), [
        t("Horse trailers", "Remolques para caballos"), t("Livestock trailers", "Remolques para ganado"),
        t("Farm utility trailers", "Remolques utilitarios agrícolas"), t("Hay trailers", "Remolques para heno"),
        t("Small agricultural equipment trailers", "Remolques para equipos agrícolas pequeños"),
        t("Small feed trailers", "Remolques pequeños para alimento animal")]),
    (t("Business & Specialty", "Comerciales y especializados"), [
        t("Food concession trailers", "Remolques de comida"), t("Mobile vending trailers", "Remolques de venta móvil"),
        t("Mobile workshop trailers", "Remolques de taller móvil"), t("Generator trailers", "Remolques para generadores"),
        t("Air compressor trailers", "Remolques para compresores de aire"), t("Pressure washer trailers", "Remolques para lavado a presión"),
        t("Portable restroom trailers", "Remolques con baños portátiles"), t("Event and display trailers", "Remolques para eventos y exhibiciones"),
        t("Mobile office trailers", "Remolques de oficina móvil"), t("Cable reel trailers", "Remolques para bobinas de cable")]),
]
REPAIRS = [
    t("Brakes and brake concerns", "Frenos y problemas de frenado"),
    t("Wheel bearings and hubs", "Rodamientos de ruedas y cubos"),
    t("Axles and suspension", "Ejes y suspensión"),
    t("Trailer lights and wiring", "Luces y cableado de remolques"),
    t("Tires and wheels", "Neumáticos y ruedas"),
    t("Couplers and towing connections", "Acoples y conexiones de remolque"),
]
FAQ = [
    (t("What trailer makes and models do you work on?", "¿Qué marcas y modelos de remolques atienden?"),
     t("Most makes and models weighing 10,000 pounds or less. Tell us about your trailer to confirm the service.",
       "La mayoría de marcas y modelos que pesen 10,000 libras o menos. Consulte para confirmar el servicio.")),
    (t("Does the 10,000-pound limit apply to my truck?", "¿El límite de 10,000 libras se aplica a mi camioneta?"),
     t("No. The limit refers to the trailer's weight, not the towing vehicle. Please also provide the manufacturer's weight rating when asking about service.",
       "No. El límite se refiere al peso del remolque, no al vehículo que lo remolca. Indique también la clasificación de peso del fabricante.")),
    (t("Can you repair an enclosed cargo trailer?", "¿Reparan remolques de carga cerrados?"),
     t("Contact us with its make, model, weight and the specific problem. We will confirm what we can repair.",
       "Indique marca, modelo, peso y el problema. Confirmaremos qué podemos reparar.")),
    (t("Do you work on landscaping or equipment trailers?", "¿Atienden remolques de jardinería o maquinaria?"),
     t("We accept inquiries for these types within our weight limit. Individual repairs are confirmed after we review the details.",
       "Aceptamos consultas sobre estos tipos dentro del límite de peso. Confirmamos las reparaciones al revisar los detalles.")),
    (t("Can you service a boat or camper trailer?", "¿Atienden remolques para barcos o campers?"),
     t("Ask us about the trailer's roadgoing components. We have not confirmed repair of boats, RV appliances or living quarters.",
       "Consúltenos sobre los componentes rodantes. No se han confirmado reparaciones de barcos, aparatos de RV o áreas habitables.")),
    (t("Do you perform Pennsylvania trailer inspections?", "¿Hacen inspecciones estatales de remolques en Pennsylvania?"),
     t("Trailers are listed among our Pennsylvania safety inspection services. Call with the trailer classification and weight to confirm eligibility and availability.",
       "Los remolques figuran entre nuestros servicios de inspección estatal. Llame con la clasificación y el peso para confirmar disponibilidad.")),
    (t("Are online requests confirmed appointments?", "¿Una solicitud en línea confirma una cita?"),
     t("No. Our staff will review your request and contact you to confirm availability.",
       "No. Nuestro personal revisará la solicitud y se comunicará para confirmar disponibilidad.")),
]
