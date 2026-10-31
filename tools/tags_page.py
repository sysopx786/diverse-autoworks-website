# -*- coding: utf-8 -*-
"""
Tag and title page (/tag-and-title/) copy, added Oct 31, 2026.

Owner-confirmed facts used here (Oct 30, 2026): Diverse Autoworks is a PennDOT authorized agent,
handles tag and title work and issues plates; notary Mon-Fri 8 a.m.-3 p.m.; the shop does PA safety
inspections and emissions tests.

NOT claimed until the owner confirms (agent types differ in what they may issue):
- temporary 90-day registration plates / in-transit plates
- registration renewals, duplicate titles, lien recording, disability placards
- VIN verification by the shop's own inspection mechanic or notary
- tag and title hours, payment methods, the shop's service fee, same-day plates

PennDOT rules and fees come from the pages in SOURCES (reviewed Oct 31, 2026). Re-check the fee
table when PennDOT changes its fees (Act 89 adjustments).

Block types are the same as brand_pages.py. Links in text: [label](pagekey) or [label](pagekey#anchor).
"""


def t(en, es):
    return {"en": en, "es": es}


PAGE = {
    "title": t("Tag & Title Service in Phoenixville, PA | Diverse Autoworks",
               "Placas y títulos en Phoenixville, PA | Diverse Autoworks"),
    "desc": t("PennDOT authorized agent in Phoenixville, PA: title transfers, registration and license plates, out-of-state transfers, plus notary and PA inspections.",
              "Agente autorizado de PennDOT en Phoenixville, PA: traspasos de título, registro y placas, vehículos de otros estados, notario e inspecciones."),
    "h1": t("Tag & Title Service in Phoenixville, PA", "Placas y títulos en Phoenixville, PA"),
    "lead": t("Diverse Autoworks is a PennDOT authorized agent. We handle title transfers, registration and license plates at our Pawlings Road shop, with a notary and Pennsylvania state inspections at the same address.",
              "Diverse Autoworks es agente autorizado de PennDOT. Hacemos traspasos de título, registros y placas en nuestro taller de Pawlings Road, con notario e inspecciones estatales de Pennsylvania en la misma dirección."),
    "crumb": t("Tag & title", "Placas y títulos"),
}

BLOCKS = [
    ("h2", t("PennDOT authorized agent in Phoenixville, PA", "Agente autorizado de PennDOT en Phoenixville, PA")),
    ("p", t("Authorized agents are private businesses under contract to PennDOT to complete title and registration applications. PennDOT's title applications, Form MV-4ST for a Pennsylvania title and Form MV-1 for a vehicle titled in another state, aren't available online. An agent completes them with you.",
            "Los agentes autorizados son negocios privados con contrato con PennDOT para completar solicitudes de título y registro. Las solicitudes de título de PennDOT, el Formulario MV-4ST para un título de Pennsylvania y el Formulario MV-1 para un vehículo con título de otro estado, no están disponibles en línea. Un agente las completa con usted.")),
    ("p", t("At Diverse Autoworks you can get the title signed in front of our notary, file the title and registration, get your plates, and pass the state inspection, all at one shop.",
            "En Diverse Autoworks puede firmar el título ante nuestro notario, tramitar el título y el registro, recibir sus placas y pasar la inspección estatal, todo en un solo taller.")),

    ("h2", t("Tag and title work we handle", "Trámites de placas y títulos que hacemos")),
    ("ul", [
        t("Title transfers when you buy or sell a vehicle privately", "Traspasos de título cuando compra o vende un vehículo entre particulares"),
        t("Pennsylvania registration and license plates", "Registro y placas de Pennsylvania"),
        t("Moving your current plate to a vehicle you just bought", "Pasar su placa actual a un vehículo que acaba de comprar"),
        t("Titling and registering a vehicle from another state when you move to Pennsylvania", "Título y registro de un vehículo de otro estado cuando se muda a Pennsylvania"),
        t("Titles and plates for business and [fleet vehicles](fleet)", "Títulos y placas de vehículos de empresa y de [flotas](fleet)"),
        t("Notarizing title signatures, Monday through Friday, 8 a.m. to 3 p.m. See [notary services](contact#notary).",
          "Notarización de firmas en títulos, de lunes a viernes, de 8 a. m. a 3 p. m. Vea [servicios de notario](contact#notary)."),
    ]),

    ("h2", t("Buying or selling a car privately", "Comprar o vender un auto entre particulares")),
    ("p", t("In Pennsylvania, the seller's signature on the title must be notarized or verified, and the buyer has 20 days from the sale to apply for the new title. Do the signing and the title application in one visit.",
            "En Pennsylvania, la firma del vendedor en el título debe ser notarizada o verificada, y el comprador tiene 20 días desde la venta para solicitar el nuevo título. Haga la firma y la solicitud del título en una sola visita.")),
    ("table", (t("Who", "Quién"), t("What to bring", "Qué debe traer")), [
        (t("Seller", "Vendedor"),
         t("The original title in your name, unsigned; current photo ID; the lien release if the vehicle had a loan",
           "El título original a su nombre, sin firmar; identificación con foto vigente; la liberación del gravamen si el vehículo tuvo un préstamo")),
        (t("Buyer", "Comprador"),
         t("Photo ID that matches the name on the application; proof of Pennsylvania insurance for the vehicle",
           "Identificación con foto que coincida con el nombre de la solicitud; comprobante de seguro de Pennsylvania para el vehículo")),
    ]),
    ("h3", t("What happens to the plate", "Qué pasa con la placa")),
    ("p", t("After the title transfers, the seller removes the plate and keeps it for another vehicle or returns it to PennDOT. Never give the plate to the buyer. If the buyer already has a Pennsylvania plate, we can move it to the vehicle they're buying.",
            "Después de que se transfiere el título, el vendedor retira la placa y la guarda para otro vehículo o la devuelve a PennDOT. Nunca le entregue la placa al comprador. Si el comprador ya tiene una placa de Pennsylvania, podemos pasarla al vehículo que está comprando.")),
    ("h3", t("Inspection after the sale", "Inspección después de la venta")),
    ("p", t("PennDOT requires the vehicle to be inspected within 10 days of the sale unless it shows a valid inspection sticker. We do Pennsylvania safety inspections and emissions tests here. See [state inspections](inspections).",
            "PennDOT exige que el vehículo se inspeccione dentro de los 10 días posteriores a la venta, a menos que tenga una calcomanía de inspección vigente. Hacemos inspecciones de seguridad y pruebas de emisiones de Pennsylvania aquí. Vea [inspecciones estatales](inspections).")),
    ("p", t("For signing rules, joint owners, gifts between family members and out-of-state titles, see our [notary guide](contact#notary).",
            "Para las reglas de firma, los títulos con varios propietarios, los regalos entre familiares y los títulos de otros estados, vea nuestra [guía del notario](contact#notary).")),

    ("h2", t("Moving to Pennsylvania with your vehicle", "Mudarse a Pennsylvania con su vehículo")),
    ("p", t("New residents must apply for a Pennsylvania title and registration within 20 days of moving here. Bring:",
            "Los nuevos residentes deben solicitar el título y el registro de Pennsylvania dentro de los 20 días posteriores a su mudanza. Traiga:")),
    ("ul", [
        t("Your out-of-state title, issued in your name", "Su título de otro estado, a su nombre"),
        t("Proof of Pennsylvania insurance, such as an insurance ID card or declaration page", "Comprobante de seguro de Pennsylvania, como una tarjeta de seguro o la página de declaraciones de la póliza"),
        t("Photo ID", "Identificación con foto"),
        t("A VIN tracing, or a VIN verification by a certified inspection mechanic or notary", "Un calco del VIN, o una verificación del VIN hecha por un mecánico de inspección certificado o un notario"),
    ]),
    ("p", t("If a lender holds your title, contact them first: many out-of-state lenders won't release a title until the loan is paid off.",
            "Si un prestamista tiene su título, comuníquese primero con él: muchos prestamistas de otros estados no liberan el título hasta que se paga el préstamo.")),
    ("p", t("Once the vehicle is registered in Pennsylvania, it must pass a safety inspection within 10 days. Most gas and hybrid vehicles registered in Chester and Montgomery counties also need the emissions test, and we do both at the same visit.",
            "Una vez registrado en Pennsylvania, el vehículo debe pasar la inspección de seguridad dentro de los 10 días siguientes. La mayoría de los vehículos de gasolina e híbridos registrados en los condados de Chester y Montgomery también necesitan la prueba de emisiones, y hacemos ambas en la misma visita.")),

    ("h2", t("PennDOT fees and sales tax", "Tarifas de PennDOT e impuesto sobre las ventas")),
    ("table", (t("Item", "Concepto"), t("Amount", "Monto")), [
        (t("Certificate of title", "Certificado de título"), t("$72", "$72")),
        (t("Passenger vehicle registration, per year", "Registro de vehículo de pasajeros, por año"), t("$48", "$48")),
        (t("Sales tax on a vehicle purchase", "Impuesto sobre las ventas por la compra de un vehículo"),
         t("6% of the purchase price or current market value (7% in Allegheny County, 8% in Philadelphia)",
           "6% del precio de compra o del valor actual de mercado (7% en el condado de Allegheny, 8% en Filadelfia)")),
    ]),
    ("p", t("These are the fees PennDOT lists, and they change from time to time. Authorized agents may also charge their own service fee, which PennDOT leaves to each agent. Call us for the total on your transaction before you come.",
            "Estas son las tarifas que indica PennDOT, y cambian de vez en cuando. Los agentes autorizados también pueden cobrar su propia tarifa de servicio, que PennDOT deja a cada agente. Llámenos antes de venir para saber el total de su trámite.")),
]

BRING_H = t("Bring to every tag and title visit", "Traiga a cualquier trámite de placas y títulos")
BRING = [
    t("Current photo ID for everyone signing", "Identificación con foto vigente de cada persona que firma"),
    t("The original title, unsigned", "El título original, sin firmar"),
    t("Proof of Pennsylvania insurance", "Comprobante de seguro de Pennsylvania"),
    t("The lien release, if there was a loan", "La liberación del gravamen, si hubo un préstamo"),
    t("Payment for sales tax and fees", "El pago del impuesto sobre las ventas y las tarifas"),
]
BRING_NOTE = t("Every transaction is a little different. Call before you come and we'll tell you exactly what yours needs.",
               "Cada trámite es un poco diferente. Llame antes de venir y le diremos exactamente qué necesita el suyo.")

SRC_LEAD = t("PennDOT rules and fees on this page come from:", "Las reglas y tarifas de PennDOT en esta página vienen de:")
SOURCES = [
    (t("PennDOT: Authorized Agents and Messengers", "PennDOT: agentes y mensajeros autorizados (en inglés)"),
     "https://www.pa.gov/agencies/dmv/resources/business-partners/authorized-agents-messengers"),
    (t("PennDOT fact sheet: Buying or Selling a Vehicle (PDF)", "Hoja informativa de PennDOT: compra o venta de un vehículo (PDF, en inglés)"),
     "https://www.dot.state.pa.us/public/dvspubsforms/bmv/bmv%20fact%20sheets/fs-buysell.pdf"),
    (t("PennDOT: Transfer Vehicle Registration from Another State", "PennDOT: transferir el registro de un vehículo de otro estado (en inglés)"),
     "https://www.pa.gov/services/dmv/transfer-vehicle-registration-from-another-state"),
    (t("PennDOT: Payments and Fees", "PennDOT: pagos y tarifas (en inglés)"),
     "https://www.pa.gov/agencies/dmv/resources/payments-and-fees"),
    (t("Pennsylvania Vehicle Code, 75 Pa.C.S. § 1111", "Código de Vehículos de Pennsylvania, 75 Pa.C.S. § 1111 (en inglés)"),
     "https://codes.findlaw.com/pa/title-75-pacsa-vehicles/pa-csa-sect-75-1111/"),
]
SRC_NOTE = t("Reviewed October 2026. This page is general information, not legal advice.",
             "Revisado en octubre de 2026. Esta página es información general, no asesoría legal.")

FAQ = [
    (t("Are you a PennDOT authorized agent?", "¿Son agentes autorizados de PennDOT?"),
     t("Yes. Diverse Autoworks is a PennDOT authorized agent. We handle tag and title work and issue license plates at 1415 Pawlings Road in Phoenixville.",
       "Sí. Diverse Autoworks es agente autorizado de PennDOT. Hacemos trámites de placas y títulos y entregamos placas en 1415 Pawlings Road, en Phoenixville.")),
    (t("I bought a car from a private seller. What do I need to transfer the title?", "Compré un auto a un particular. ¿Qué necesito para traspasar el título?"),
     t("The seller's signed and notarized title, photo ID that matches the name on the application, and proof of Pennsylvania insurance for the vehicle. If the seller hasn't signed yet, come in together and our notary can witness the signature. Sales tax and PennDOT fees are paid when we file the application.",
       "El título firmado por el vendedor y notarizado, una identificación con foto que coincida con el nombre de la solicitud y un comprobante de seguro de Pennsylvania para el vehículo. Si el vendedor todavía no ha firmado, vengan juntos y nuestro notario puede presenciar la firma. El impuesto sobre las ventas y las tarifas de PennDOT se pagan cuando presentamos la solicitud.")),
    (t("How long do I have to title a vehicle I bought?", "¿Cuánto tiempo tengo para tramitar el título de un vehículo que compré?"),
     t("Pennsylvania law gives the buyer 20 days from the sale to apply for a new title. The vehicle also needs a safety inspection within 10 days of the sale, unless it has a valid sticker.",
       "La ley de Pennsylvania le da al comprador 20 días desde la venta para solicitar un nuevo título. El vehículo también necesita la inspección de seguridad dentro de los 10 días posteriores a la venta, a menos que tenga una calcomanía vigente.")),
    (t("Can I move my license plate to the car I just bought?", "¿Puedo pasar mi placa al auto que acabo de comprar?"),
     t("Yes. If you have a Pennsylvania plate from a vehicle you sold or traded, we can transfer it to the vehicle you bought.",
       "Sí. Si tiene una placa de Pennsylvania de un vehículo que vendió o cambió, podemos pasarla al vehículo que compró.")),
    (t("I just moved to Pennsylvania. How do I register my car?", "Me acabo de mudar a Pennsylvania. ¿Cómo registro mi auto?"),
     t("Apply within 20 days of moving. Bring your out-of-state title in your name, proof of Pennsylvania insurance, photo ID and a VIN tracing or verification. We complete Form MV-1 with you. After registration, the vehicle needs a Pennsylvania safety inspection within 10 days, and we do that here too.",
       "Haga el trámite dentro de los 20 días posteriores a su mudanza. Traiga su título de otro estado a su nombre, un comprobante de seguro de Pennsylvania, una identificación con foto y un calco o una verificación del VIN. Completamos el Formulario MV-1 con usted. Después del registro, el vehículo necesita la inspección de seguridad de Pennsylvania dentro de los 10 días siguientes, y también la hacemos aquí.")),
    (t("How much does a title transfer cost?", "¿Cuánto cuesta un traspaso de título?"),
     t("PennDOT lists a $72 title fee and $48 a year to register a passenger vehicle, plus 6% sales tax on the purchase price or market value for Chester County residents. Agents may add a service fee. Call us for the total on your transaction.",
       "PennDOT indica una tarifa de título de $72 y $48 al año por registrar un vehículo de pasajeros, más el 6% de impuesto sobre las ventas del precio de compra o del valor de mercado para los residentes del condado de Chester. Los agentes pueden agregar una tarifa de servicio. Llámenos para saber el total de su trámite.")),
    (t("What should the seller do with the license plate?", "¿Qué debe hacer el vendedor con la placa?"),
     t("Remove it after the title transfers. Keep it to move to another vehicle you own, or return it to PennDOT. Don't give the plate to the buyer.",
       "Retirarla después de que se transfiere el título. Guárdela para pasarla a otro vehículo de su propiedad o devuélvala a PennDOT. No le entregue la placa al comprador.")),
    (t("Is tag and title work the same as your notary service?", "¿Los trámites de placas y títulos son lo mismo que el servicio de notario?"),
     t("No. The notary witnesses signatures on the title and other documents, Monday through Friday, 8 a.m. to 3 p.m. Tag and title work is the PennDOT application, registration and plates. Most title transfers need both, and you can do both here in one visit.",
       "No. El notario presencia las firmas en el título y en otros documentos, de lunes a viernes, de 8 a. m. a 3 p. m. Los trámites de placas y títulos son la solicitud ante PennDOT, el registro y las placas. La mayoría de los traspasos de título necesitan ambos, y puede hacer los dos aquí en una sola visita.")),
]

CTA = [
    ("h2", t("Tag and title service near Phoenixville, PA", "Placas y títulos cerca de Phoenixville, PA")),
    ("p", t("Call Diverse Autoworks before you come and we'll tell you what to bring for your title transfer, registration or plates. We're at 1415 Pawlings Road, Phoenixville, PA 19460.",
            "Llame a Diverse Autoworks antes de venir y le diremos qué debe traer para su traspaso de título, registro o placas. Estamos en 1415 Pawlings Road, Phoenixville, PA 19460.")),
]

SEARCH = ("tag and title tags titles title transfer registration license plate plates penndot authorized agent tag service notary out of state new resident mv-1 mv-4st sales tax",
          "placas títulos traspaso de título registro placa penndot agente autorizado servicio de placas notario otro estado nuevo residente mv-1 mv-4st impuesto")
