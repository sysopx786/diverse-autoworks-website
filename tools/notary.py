# -*- coding: utf-8 -*-
"""
Notary section copy (English + Spanish) for the Contact page, anchor #notary.
Every text is a dict {"en": ..., "es": ...}; build.py's parity check walks NOTARY.
Source: owner-supplied notary page redesign (Oct 7, 2026). The Spanish is a draft that
still needs a native-speaker review before it is treated as final.
"""
from content import t

NOTARY = {
    "eyebrow": t("Notary public · Phoenixville, PA", "Notario público · Phoenixville, PA"),
    "h2": t("Vehicle titles signed right the first time.", "Títulos de vehículos firmados bien desde la primera vez."),
    "lede": t(
        "In Pennsylvania, the seller’s signature on a vehicle title must be notarized or verified. Bring the title, the signers, and valid photo ID to our Pawlings Road shop, and we handle the notarization.",
        "En Pensilvania, la firma del vendedor en el título de un vehículo debe ser notarizada o verificada. Traiga el título, a las personas que firman y una identificación con foto vigente a nuestro taller de Pawlings Road, y nosotros nos encargamos de la notarización."),
    "cta_how": t("See how it works", "Vea cómo funciona"),
    "chips": [
        t("Mon–Fri · 8 a.m.–3 p.m.", "Lun–vie · 8 a. m.–3 p. m."),
        t("In person at the shop", "En persona en el taller"),
        t("1415 Pawlings Rd", "1415 Pawlings Rd"),
    ],

    "s1_h": t("What we notarize", "Qué notarizamos"),
    "s1_p": t("Vehicle paperwork is our focus. If your document isn’t listed, call first and we’ll tell you whether we can take it.",
              "Nos enfocamos en documentos de vehículos. Si su documento no aparece aquí, llame primero y le diremos si podemos atenderlo."),
    "cards": [
        ("inspection", t("Vehicle title transfers", "Traspasos de título de vehículo"),
         t("The seller’s signature on a Pennsylvania certificate of title, plus any buyer signature the paperwork calls for.",
           "La firma del vendedor en un certificado de título de Pensilvania, más la firma del comprador si los documentos la piden.")),
        ("pin", t("Out-of-state titles", "Títulos de otros estados"),
         t("Titles from other states whose seller signature must be notarized. Check the back of the title or call us.",
           "Títulos de otros estados en los que la firma del vendedor debe ser notarizada. Revise el reverso del título o llámenos.")),
        ("mail", t("Duplicate & correction forms", "Formularios de duplicado y corrección"),
         t("PennDOT forms for lost, damaged or incorrect titles, where the form asks for a notarized signature.",
           "Formularios de PennDOT para títulos perdidos, dañados o incorrectos, cuando el formulario pide una firma notarizada.")),
        ("seal", t("Affidavits & sworn statements", "Declaraciones juradas"),
         t("Vehicle-related statements that must be sworn or affirmed in front of a notary.",
           "Declaraciones relacionadas con vehículos que deben jurarse o afirmarse ante un notario.")),
        ("van", t("Business & fleet vehicles", "Vehículos de empresa y de flotas"),
         t("Titles owned by a company. The signer needs proof they can act for the business.",
           "Títulos a nombre de una empresa. La persona que firma necesita comprobar que puede actuar en nombre del negocio.")),
        ("phone", t("Other documents", "Otros documentos"),
         t("General acknowledgments and signature witnessing. Call ahead so we can confirm the document is one we can notarize.",
           "Reconocimientos de firma generales y certificación de firmas. Llame antes para confirmar que podemos notarizar su documento.")),
    ],

    "s2_h": t("How it works in Pennsylvania", "Cómo funciona en Pensilvania"),
    "s2_p": t("A private vehicle sale in four steps, from signed title to new registration.",
              "Una venta privada de un vehículo en cuatro pasos, desde el título firmado hasta el nuevo registro."),
    "steps": [
        (t("Check the title", "Revise el título"),
         t("Use the original title, in the seller’s name, with any loan released. Do not sign it yet. The signature must happen in front of the notary.",
           "Use el título original, a nombre del vendedor y con cualquier préstamo liberado. Todavía no lo firme. La firma debe hacerse frente al notario.")),
        (t("Come in together", "Vengan juntos"),
         t("Each person who signs appears in person with photo ID. We’re open for notary work Monday–Friday, 8 a.m.–3 p.m. Call ahead.",
           "Cada persona que firma se presenta en persona con identificación con foto. Atendemos asuntos de notario de lunes a viernes, de 8 a. m. a 3 p. m. Llame antes.")),
        (t("Sign before the notary", "Firme ante el notario"),
         t("The seller signs, prints their name as shown on the front of the title, and records the mileage. We verify ID, watch you sign, and complete the notarial certificate.",
           "El vendedor firma, escribe su nombre en letra de molde tal como aparece en el frente del título y anota el millaje. Verificamos la identificación, vemos cómo firma y completamos el certificado notarial.")),
        (t("Apply for the new title", "Solicite el nuevo título"),
         t("The buyer applies through a PennDOT authorized agent within 20 days of the sale. The seller removes the license plate.",
           "El comprador lo solicita por medio de un agente autorizado de PennDOT dentro de los 20 días posteriores a la venta. El vendedor retira la placa.")),
    ],

    "s3_h": t("The Pennsylvania rules, in plain terms", "Las reglas de Pensilvania, en palabras sencillas"),
    "s3_p": t("What PennDOT and the Pennsylvania Department of State require, and how each rule affects your visit.",
              "Lo que exigen PennDOT y el Departamento de Estado de Pensilvania, y cómo afecta cada regla a su visita."),
    "rules": [
        (t("Notarization rule", "Regla de notarización"), t("PennDOT", "PennDOT"), [
            t("The seller’s signature on a Pennsylvania title must be notarized or verified. PennDOT tells buyer and seller to meet at a notary, tag service or motor vehicle dealer so the title application is completed correctly.",
              "La firma del vendedor en un título de Pensilvania debe ser notarizada o verificada. PennDOT recomienda que comprador y vendedor se reúnan en una notaría, un servicio de placas o un concesionario para que la solicitud del título se complete correctamente."),
            t("Some paperwork also asks for the buyer’s signature to be notarized. Bring the buyer, and we notarize whatever the form calls for.",
              "Algunos documentos también piden que la firma del comprador sea notarizada. Traiga al comprador y notarizamos lo que el formulario indique.")]),
        (t("Who signs, and where", "Quién firma y dónde"), t("Seller · Buyer", "Vendedor · Comprador"), [
            t("The seller signs and handprints their name on the title and enters the mileage in the spaces provided. Sign exactly as the name appears on the front.",
              "El vendedor firma y escribe su nombre en letra de molde en el título, y anota el millaje en los espacios indicados. Firme exactamente como aparece el nombre en el frente."),
            t("If several owners are listed, look at how the names are joined on the front. Names joined by “and” generally mean all owners sign. If you’re unsure, call before you come in.",
              "Si hay varios propietarios, fíjese en cómo están unidos los nombres en el frente. Los nombres unidos por “y” generalmente significan que firman todos los propietarios. Si tiene dudas, llame antes de venir.")]),
        (t("Identification", "Identificación"), t("Notary + PennDOT", "Notario + PennDOT"), [
            t("A Pennsylvania notary must know the signer personally or have “satisfactory evidence” of identity. In practice, bring a current government-issued photo ID for every signer.",
              "Un notario de Pensilvania debe conocer personalmente a quien firma o contar con “pruebas satisfactorias” de su identidad. En la práctica, traiga una identificación con foto vigente, emitida por el gobierno, de cada persona que firma."),
            t("For the title application itself, PennDOT asks the buyer for a Pennsylvania driver’s license or photo ID. Sellers should also bring a current photo ID.",
              "Para la solicitud del título, PennDOT pide al comprador una licencia de conducir o identificación con foto de Pensilvania. Los vendedores también deben traer una identificación con foto vigente.")]),
        (t("In person only", "Solo en persona"), t("Pa. Dept. of State", "Depto. de Estado de Pa."), [
            t("Each signer must appear before the notary. A video or phone call doesn’t count. The only exception is notaries the Department of State has specifically authorized for electronic or remote work. We notarize in person at the shop.",
              "Cada persona que firma debe presentarse ante el notario. Una videollamada o una llamada telefónica no cuenta. La única excepción son los notarios que el Departamento de Estado ha autorizado específicamente para trabajo electrónico o remoto. Notarizamos en persona en el taller.")]),
        (t("Business-owned vehicles", "Vehículos de empresas"), t("PennDOT", "PennDOT"), [
            t("The person signing for a company or non-profit must be an authorized individual or bring proof of authorization. PennDOT publishes acceptable identification requirements for business organizations. Bring that proof with you.",
              "La persona que firma por una empresa u organización sin fines de lucro debe ser un representante autorizado o traer prueba de su autorización. PennDOT publica los requisitos de identificación aceptables para organizaciones comerciales. Traiga esa prueba.")]),
        (t("Out-of-state titles", "Títulos de otros estados"), t("PennDOT", "PennDOT"), [
            t("Some out-of-state titles require the seller’s signature to be notarized. PennDOT recommends checking with a dealer, tag service, notary or the Bureau of Motor Vehicles.",
              "Algunos títulos de otros estados exigen que la firma del vendedor sea notarizada. PennDOT recomienda consultar con un concesionario, un servicio de placas, un notario o la Oficina de Vehículos Motorizados."),
            t("PennDOT also requires VIN verification for out-of-state vehicles, and many out-of-state lienholders won’t release a title until the loan is paid. Contact the lienholder first.",
              "PennDOT también exige la verificación del VIN para vehículos de otros estados, y muchos acreedores de otros estados no liberan el título hasta que se paga el préstamo. Comuníquese primero con el acreedor.")]),
        (t("Loans & liens", "Préstamos y gravámenes"), t("Title", "Título"), [
            t("If the vehicle was financed, the lienholder’s release must be shown on the title or provided as a lien release letter before the title can move to the buyer.",
              "Si el vehículo fue financiado, la liberación del acreedor debe aparecer en el título o presentarse como carta de liberación de gravamen antes de que el título pase al comprador.")]),
        (t("Gifts & family sales", "Regalos y ventas entre familiares"), t("PennDOT · Revenue", "PennDOT · Ingresos"), [
            t("For a gift, PennDOT requires Form MV-13ST, Affidavit of Gift, completed by everyone transferring and receiving the vehicle and attached to the title application.",
              "Para un regalo, PennDOT exige el Formulario MV-13ST, Declaración Jurada de Regalo, completado por todas las personas que transfieren y reciben el vehículo y adjunto a la solicitud del título."),
            t("Sales tax is based on the vehicle’s fair market value, not only the price written down. The Department of Revenue can review sales priced far below market value, which is common in family transfers.",
              "El impuesto sobre las ventas se basa en el valor justo de mercado del vehículo, no solo en el precio anotado. El Departamento de Ingresos puede revisar ventas con precios muy por debajo del valor de mercado, algo común en traspasos entre familiares.")]),
        (t("Buyer’s deadline", "Plazo del comprador"), t("Title application", "Solicitud del título"), [
            t("The buyer applies for the new title through a PennDOT authorized agent within 20 days of the sale. The agent completes Form MV-4ST (Vehicle Sales and Use Tax Return/Application for Registration) for a Pennsylvania title. The buyer brings the notarized title, ID and a current insurance card.",
              "El comprador solicita el nuevo título por medio de un agente autorizado de PennDOT dentro de los 20 días posteriores a la venta. El agente completa el Formulario MV-4ST (Declaración de Impuesto sobre Ventas y Uso del Vehículo/Solicitud de Registro) para un título de Pensilvania. El comprador lleva el título notarizado, su identificación y una tarjeta de seguro vigente.")]),
        (t("License plate", "Placa"), t("Seller", "Vendedor"), [
            t("After the title transfers, the seller removes the plate. Move it to another vehicle you own, or return it to PennDOT.",
              "Después de que el título se transfiere, el vendedor retira la placa. Puede pasarla a otro vehículo de su propiedad o devolverla a PennDOT.")]),
        (t("Notary fees", "Tarifas del notario"), t("Pa. Dept. of State", "Depto. de Estado de Pa."), [
            t("The Department of State sets the maximum a notary may charge for each notarial act. Fees must be itemized on your receipt, and any clerical or administrative charge must be disclosed before the notarization. Call us for current details.",
              "El Departamento de Estado fija el máximo que un notario puede cobrar por cada acto notarial. Las tarifas deben detallarse en su recibo y cualquier cargo administrativo debe informarse antes de la notarización. Llámenos para conocer los detalles actuales.")]),
    ],
    # [[1]] [[2]] [[3]] become links to the three official pages, in this order.
    "note": t(
        "Based on PennDOT’s [[1]] page and the Department of State’s [[2]] and [[3]] pages, reviewed October 2026. Requirements change, and every title is different. This page is general information, not legal advice.",
        "Basado en la página de PennDOT [[1]] y en las páginas del Departamento de Estado [[2]] y [[3]], revisadas en octubre de 2026. Los requisitos cambian y cada título es diferente. Esta página es información general, no asesoría legal."),
    "note_links": [
        ("https://www.pa.gov/agencies/dmv/vehicle-services/title-and-registration/buying-or-selling-a-vehicle",
         t("Buying or Selling a Vehicle", "Compra o venta de un vehículo (en inglés)")),
        ("https://www.pa.gov/agencies/dos/resources/notaries-resources-and-information/powers-of-a-notary-public",
         t("Powers of a Notary Public", "Facultades de un notario público (en inglés)")),
        ("https://www.pa.gov/agencies/dos/programs/notaries/notary-public-fees",
         t("Notary Public Fees", "Tarifas de notarios públicos (en inglés)")),
    ],

    "s4_eyebrow": t("Before you come", "Antes de venir"),
    "s4_h": t("Bring the paperwork, not the pen marks.", "Traiga los documentos, sin marcas de pluma."),
    "s4_p": t("A signature in the wrong place or at the wrong time is a common reason a title gets rejected. A few minutes of preparation can save you a duplicate-title application.",
              "Una firma en el lugar equivocado o en el momento equivocado es una razón común por la que se rechaza un título. Unos minutos de preparación pueden evitarle una solicitud de título duplicado."),
    "bring_h": t("Bring", "Traiga"),
    "bring": [
        t("The original title, not a photocopy", "El título original, no una fotocopia"),
        t("Current government-issued photo ID for every signer", "Identificación con foto vigente, emitida por el gobierno, de cada persona que firma"),
        t("The lienholder’s release, if the title shows a loan", "La liberación del acreedor, si el título muestra un préstamo"),
        t("Buyer: Pennsylvania ID and proof of insurance for the title application", "Comprador: identificación de Pensilvania y comprobante de seguro para la solicitud del título"),
        t("Any PennDOT forms you’ve been given, with signature lines left blank", "Cualquier formulario de PennDOT que le hayan dado, con las líneas de firma en blanco"),
        t("Businesses: proof the signer can act for the company", "Empresas: prueba de que quien firma puede actuar en nombre de la empresa"),
    ],
    "avoid_h": t("Avoid", "Evite"),
    "avoid": [
        t("Signing the title before you reach the notary", "Firmar el título antes de llegar con el notario"),
        t("Signing in the buyer’s block as the seller, or the reverse", "Firmar en el recuadro del comprador como vendedor, o al revés"),
        t("A signature or printed name that doesn’t match the front of the title", "Una firma o nombre impreso que no coincide con el frente del título"),
        t("Crossing out, writing over or correcting entries on the title", "Tachar, escribir encima o corregir datos en el título"),
    ],
    # text inside the title illustration (SVG)
    "photo_alt": t("A notary public at a desk guiding a client as she signs a document, with a notary stamp and journal on the desk",
                   "Una notaria en su escritorio guiando a una clienta mientras firma un documento, con un sello notarial y un libro de registro sobre el escritorio"),
    "doc_aria": t("Illustration of a vehicle title with the seller signature block highlighted: sign only in front of the notary",
                  "Ilustración de un título de vehículo con el recuadro de firma del vendedor resaltado: firme solo frente al notario"),
    "doc_top": t("CERTIFICATE OF TITLE · ILLUSTRATION", "CERTIFICADO DE TÍTULO · ILUSTRACIÓN"),
    "doc_assign": t("ASSIGNMENT OF TITLE", "TRASPASO DEL TÍTULO"),
    "doc_seller": t("SELLER · SIGN HERE, IN FRONT OF THE NOTARY", "VENDEDOR · FIRME AQUÍ, ANTE EL NOTARIO"),
    "doc_odo": t("ODOMETER READING", "LECTURA DEL ODÓMETRO"),
    "doc_buyer": t("BUYER SECTION", "SECCIÓN DEL COMPRADOR"),
    "doc_notary": t("NOTARY", "NOTARIO"),

    "shop_eyebrow": t("Also at Diverse Autoworks", "También en Diverse Autoworks"),
    "shop_h": t("Buying or selling a car? We fix and inspect them too.", "¿Compra o vende un auto? También lo reparamos e inspeccionamos."),
    "shop_p": t("State inspections for cars, trucks, trailers and motorcycles, plus repairs, maintenance and fleet service, all at the same Pawlings Road address.",
                "Inspecciones estatales para autos, camiones, remolques y motocicletas, además de reparaciones, mantenimiento y servicio para flotas, todo en la misma dirección de Pawlings Road."),

    "faq_h": t("Notary questions", "Preguntas sobre el notario"),
    "faq": [
        (t("Do I need an appointment?", "¿Necesito cita?"), [
            t("Notary services are available Monday through Friday, 8 a.m.–3 p.m. Call 610-650-0316 before you come to confirm availability and any requirements for your documents. Both the seller and the buyer should be there if the paperwork needs both signatures.",
              "Los servicios de notario público están disponibles de lunes a viernes, de 8 a. m. a 3 p. m. Llame al 610-650-0316 antes de venir para confirmar la disponibilidad y los requisitos para sus documentos. El vendedor y el comprador deben estar presentes si los documentos requieren ambas firmas.")]),
        (t("Does Pennsylvania require a vehicle title to be notarized?", "¿Pensilvania exige que el título de un vehículo sea notarizado?"), [
            t("For a private sale, yes in practice. PennDOT requires the seller’s signature on a Pennsylvania title to be notarized or verified. PennDOT recommends that buyer and seller meet at a notary, tag service or dealer so the application is completed correctly.",
              "En una venta privada, en la práctica sí. PennDOT exige que la firma del vendedor en un título de Pensilvania sea notarizada o verificada. PennDOT recomienda que comprador y vendedor se reúnan en una notaría, un servicio de placas o un concesionario para que la solicitud se complete correctamente.")]),
        (t("Who has to be present?", "¿Quién tiene que estar presente?"), [
            t("Every person who signs must appear in front of the notary in person. Video calls and phone calls do not count as personal appearance under Pennsylvania law, apart from notaries the Department of State has specifically authorized for remote or electronic work.",
              "Cada persona que firma debe presentarse en persona ante el notario. Las videollamadas y las llamadas telefónicas no cuentan como comparecencia personal según la ley de Pensilvania, salvo con notarios que el Departamento de Estado haya autorizado específicamente para trabajo remoto o electrónico."),
            t("If the seller and buyer can’t come together, each can sign separately in front of a notary. Call us first so we know what the paperwork needs.",
              "Si el vendedor y el comprador no pueden venir juntos, cada uno puede firmar por separado ante un notario. Llámenos primero para saber lo que necesitan los documentos.")]),
        (t("What ID should I bring?", "¿Qué identificación debo traer?"), [
            t("A current government-issued photo ID, such as a driver’s license, for every person signing. A Pennsylvania notary must know you personally or have satisfactory evidence of your identity, and the notary decides whether the ID you show is acceptable.",
              "Una identificación con foto vigente emitida por el gobierno, como una licencia de conducir, de cada persona que firma. Un notario de Pensilvania debe conocerle personalmente o contar con pruebas satisfactorias de su identidad, y el notario decide si la identificación que presenta es aceptable."),
            t("For the title application, PennDOT asks the buyer for a Pennsylvania driver’s license or photo ID.",
              "Para la solicitud del título, PennDOT pide al comprador una licencia de conducir o identificación con foto de Pensilvania.")]),
        (t("Can I sign the title before I come in?", "¿Puedo firmar el título antes de ir?"), [
            t("No. Sign only in front of the notary. A title that is signed incorrectly or without the notary present can be rejected, and you may need to apply for a duplicate title before the vehicle can be sold. Don’t cross out or write over entries to fix a mistake.",
              "No. Firme solo frente al notario. Un título firmado incorrectamente o sin el notario presente puede ser rechazado, y es posible que deba solicitar un título duplicado antes de poder vender el vehículo. No tache ni escriba encima para corregir un error.")]),
        (t("What if there’s a loan on the vehicle?", "¿Y si el vehículo tiene un préstamo?"), [
            t("The lienholder’s release must appear on the title or come as a separate lien release letter before the title can transfer. If the title is still held by the lender, contact them first. Many out-of-state lienholders won’t release a title until the loan is paid off.",
              "La liberación del acreedor debe aparecer en el título o venir en una carta de liberación de gravamen aparte antes de que el título pueda transferirse. Si el prestamista todavía tiene el título, comuníquese primero con él. Muchos acreedores de otros estados no liberan el título hasta que el préstamo se paga por completo.")]),
        (t("The title is from another state. Can you notarize it?", "El título es de otro estado. ¿Pueden notarizarlo?"), [
            t("Some out-of-state titles require the seller’s signature to be notarized, and some don’t. Check the back of the title for the seller’s signature and odometer area, and call us with the state name. PennDOT also requires VIN verification for out-of-state vehicles during the Pennsylvania title application.",
              "Algunos títulos de otros estados exigen que la firma del vendedor sea notarizada y otros no. Revise el reverso del título, donde van la firma del vendedor y el odómetro, y llámenos con el nombre del estado. PennDOT también exige la verificación del VIN para vehículos de otros estados durante la solicitud del título de Pensilvania.")]),
        (t("Do you complete the title application and issue plates?", "¿Completan la solicitud del título y entregan placas?"), [
            t("Notarization is the signature step. The buyer’s title application (Form MV-4ST for a Pennsylvania title, Form MV-1 for out-of-state or new vehicles) is completed through a PennDOT authorized agent, and PennDOT’s forms are only available from authorized agents. Call us to confirm what we can help with before you plan your visit.",
              "La notarización es el paso de la firma. La solicitud de título del comprador (Formulario MV-4ST para un título de Pensilvania, Formulario MV-1 para vehículos de otros estados o nuevos) se completa por medio de un agente autorizado de PennDOT, y los formularios de PennDOT solo están disponibles con agentes autorizados. Llámenos para confirmar con qué podemos ayudarle antes de planear su visita.")]),
        (t("How long does the buyer have to apply for the new title?", "¿Cuánto tiempo tiene el comprador para solicitar el nuevo título?"), [
            t("The buyer applies through an authorized agent within 20 days of the sale. Bring the notarized title, Form MV-4ST (completed with the agent), photo ID, and a current insurance card if you want registration issued. Sales tax and fees are collected at the agent.",
              "El comprador lo solicita por medio de un agente autorizado dentro de los 20 días posteriores a la venta. Lleve el título notarizado, el Formulario MV-4ST (que se completa con el agente), una identificación con foto y una tarjeta de seguro vigente si desea que se emita el registro. El impuesto sobre las ventas y las tarifas se cobran con el agente.")]),
        (t("We’re family. Does a gifted vehicle work differently?", "Somos familia. ¿Un vehículo regalado funciona distinto?"), [
            t("If sales tax exemption for a gift is claimed, PennDOT requires Form MV-13ST, Affidavit of Gift, completed by everyone transferring and receiving the vehicle and attached to the title application.",
              "Si se reclama la exención del impuesto sobre las ventas por un regalo, PennDOT exige el Formulario MV-13ST, Declaración Jurada de Regalo, completado por todas las personas que transfieren y reciben el vehículo y adjunto a la solicitud del título."),
            t("If a vehicle is sold for far less than its market value, the Department of Revenue can review the sale, because sales tax is based on fair market value. Ask your PennDOT agent which form applies to you.",
              "Si un vehículo se vende por mucho menos que su valor de mercado, el Departamento de Ingresos puede revisar la venta, porque el impuesto sobre las ventas se basa en el valor justo de mercado. Pregunte a su agente de PennDOT qué formulario le corresponde.")]),
        (t("What should the seller do with the license plate?", "¿Qué debe hacer el vendedor con la placa?"), [
            t("After the title transfers, the seller removes the plate from the vehicle. You can move it to another vehicle you own, or return it to PennDOT’s Bureau of Motor Vehicles Return Tag Unit.",
              "Después de que el título se transfiere, el vendedor retira la placa del vehículo. Puede pasarla a otro vehículo de su propiedad o devolverla a la Unidad de Devolución de Placas de la Oficina de Vehículos Motorizados de PennDOT.")]),
        (t("The vehicle belongs to a business. What do we need?", "El vehículo es de una empresa. ¿Qué necesitamos?"), [
            t("The person signing must be an authorized individual of the business or bring proof of authorization. PennDOT publishes a fact sheet on identification requirements for business organizations and non-profit corporations. Bring that proof along with the signer’s photo ID.",
              "La persona que firma debe ser un representante autorizado de la empresa o traer prueba de su autorización. PennDOT publica una hoja informativa sobre los requisitos de identificación para organizaciones comerciales y corporaciones sin fines de lucro. Traiga esa prueba junto con la identificación con foto de quien firma.")]),
        (t("What does notarization cost?", "¿Cuánto cuesta la notarización?"), [
            t("The Pennsylvania Department of State sets the maximum fee a notary can charge per notarial act. Fees must be itemized on your receipt, and any clerical or administrative charge has to be disclosed before the notarization. Call 610-650-0316 for current details.",
              "El Departamento de Estado de Pensilvania fija la tarifa máxima que un notario puede cobrar por cada acto notarial. Las tarifas deben detallarse en su recibo y cualquier cargo administrativo debe informarse antes de la notarización. Llame al 610-650-0316 para conocer los detalles actuales.")]),
        (t("Can you notarize any document?", "¿Pueden notarizar cualquier documento?"), [
            t("Not always. We can’t notarize if a signer isn’t present, can’t be identified, or the document isn’t one we can take. We can’t advise which document you need or what it means legally. Call ahead with a description of your document and we’ll tell you.",
              "No siempre. No podemos notarizar si una persona que firma no está presente, no puede ser identificada o el documento no es uno que podamos atender. No podemos aconsejarle qué documento necesita ni qué significa legalmente. Llame antes con una descripción de su documento y le diremos.")]),
        (t("What if a mistake is found after the title is notarized?", "¿Y si se encuentra un error después de notarizar el título?"), [
            t("Don’t alter the title. Contact a PennDOT authorized agent. A corrected certificate generally requires a PennDOT correction application, and a title that can’t be fixed may need a duplicate.",
              "No altere el título. Comuníquese con un agente autorizado de PennDOT. Un certificado corregido generalmente requiere una solicitud de corrección de PennDOT, y un título que no se puede corregir puede necesitar un duplicado.")]),
    ],
}
