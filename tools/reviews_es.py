"""Spanish translations of customer reviews, matched by position to the source lists.

Order matters: GOOGLE follows google_reviews.json after dropping blank and held entries,
CARFAX follows carfax_reviews.json, YELP follows yelp_reviews.json, YELP_REPLY maps a Yelp
index to the owner's reply, FEATURED follows REVIEWS in content.py.
build.py checks the counts so a new review cannot slip in untranslated.
These are translations of the customers' words, not the originals. Have a native speaker review.
"""

GOOGLE = [
    "¡Excelente servicio! Mi camioneta tuvo un problema camino al trabajo y, por suerte, Diverse quedaba en el camino. Joe y Ariel me devolvieron a la carretera en menos de 2 horas. Fueron amables y serviciales en cada paso. Trabajo de tiempo completo en una agencia de autos y este nivel de atención y de acción inmediata no existe en muchos lugares. ¡Diverse es una verdadera joya en esta industria! Esta gente REALMENTE se preocupa por sus clientes. ¡Gracias otra vez por su apoyo y su ayuda!",
    "Llegué por recomendación de otro motociclista. Joe hace inspecciones de motocicletas. Me atiende rapidísimo, sobre todo cuando está lloviendo. Me gusta el ambiente tranquilo del lugar. Tiene una cafetera Keurig y una estación de carga USB.",
    "Tuvimos un problema con nuestra camioneta mientras manejábamos a casa, en Nueva Jersey, por la 422. No sabíamos adónde ir y encontramos a Desire en internet. ¡Qué experiencia tan positiva y excelente! Nos atendieron de inmediato, diagnosticaron el problema y nos devolvieron a la carretera en poco tiempo, a un precio accesible. Convirtieron lo que pudo ser un día terrible en una pequeña demora para llegar a casa. Y como regalo extra, al subir a la camioneta había una bolsa de dulces de Halloween esperándonos. ¡Qué rico! Se lo recomendaría a cualquiera que busque un mecánico honesto y de confianza. Ojalá encontráramos un mecánico parecido cerca de casa, en Nueva Jersey. ¡Quizás valga la pena manejar dos horas la próxima vez que necesitemos servicio!",
    "Gran precio. Diverse Autoworks ofrece el mejor precio que he tenido. Son honestos, confiables, flexibles con su tiempo y muy corteses. He llevado mi carro dos veces. Las dos veces me atendieron de forma rápida y eficiente, con el precio más bajo que he visto por un trabajo de calidad. Mi carro tiene 11 años y 156,000 millas.",
    "Hice la inspección estatal y la rotación y balanceo de llantas en Diverse Autoworks. Fue una experiencia muy positiva. Programar la cita por teléfono fue rápido y fácil. Cuando llegué a la hora de la cita, ya tenían todo preparado y salí en minutos. La sala de espera es agradable, limpia, amplia y libre de humo. Me informaron del estado del carro con un mensaje telefónico y la factura venía adjunta. Nadie me llamó para tratar de venderme algo más, y eso lo agradezco de verdad. En el futuro también llevaremos allí todos nuestros otros carros. Gracias por hacerlo lo menos molesto posible.",
    "Por más de 4 años le he confiado a Diverse Autoworks el mantenimiento de mis carros. Su personal, que es conocedor y hábil, resolvió con eficiencia cualquier problema de mi carro y me dio explicaciones claras en el camino. El servicio al cliente que recibí fue excepcional, con personal amable y atento que me mantuvo bien informado durante todo el proceso. La calidad de su trabajo es admirable y dejaron mi carro en excelente estado. Sus precios son justos y transparentes, y ofrecen muy buen valor por los servicios prestados. En general, recomiendo mucho a Diverse Autoworks para el mantenimiento y las reparaciones de carros, con confianza y de primera calidad.",
    "Como cliente nuevo, he recibido un servicio sobresaliente de Diverse Autoworks. La oficina está impecable y, por lo que puedo ver, el taller también está limpio y ordenado. He llevado mis vehículos varias veces y la experiencia ha sido muy positiva cada vez. Se adaptaron a mis horarios para dejar y recoger el vehículo y comunican muy bien las novedades. Sus precios son comparables a los de otros talleres; confío en su trabajo y en lo bien que cuidan mis vehículos. Da gusto ver una empresa local que valora a sus clientes, se enorgullece de su trabajo y ofrece un excelente servicio técnico. Denles la oportunidad de ganarse su negocio.",
    "Muy buena experiencia en Diverse para alinear mi Forester hoy. Todos fueron increíblemente amables y me alegra haber encontrado otro negocio local al que apoyar. Ariel fue de gran ayuda para darme cita rápido e incluso llamó el día anterior para recordarme la cita. Diverse hizo la alineación rápido y a un precio justo, y mi carro ahora maneja de maravilla. El taller también está muy limpio y ordenado. De ahora en adelante traeré aquí nuestros otros vehículos para todo lo que no puedo hacer en el garaje de mi casa.",
    "Soy nuevo llevando mis carros al equipo de Diverse y estoy muy contento con sus servicios y su gente amable. Qué bueno tener un taller independiente de confianza en el pueblo.",
    "Llevo casi 2 años yendo a Diverse Autoworks con los varios vehículos que tengo. En cada visita son amables y profesionales. Tienen precios justos y el trabajo siempre se hace a tiempo y con alta calidad. Hace poco llevé un vehículo para que lo revisaran antes de regalarlo; me dieron algunas sugerencias y, después del trabajo, ¡el carro nunca había funcionado mejor! Se llevan 5 estrellas en mi libro y recomiendo mucho que lleven sus vehículos aquí también.",
    "La gente de Diverse Auto de verdad entiende lo que es el servicio al cliente. Son muy amables y hacen todo lo posible por ayudar. Hicieron un esfuerzo extra cuando yo estaba en un apuro, y esa clase de empatía humana en un negocio es lo que me ganará como cliente de por vida. Se lo recomendaría a cualquiera.",
    "¡Gran experiencia en Diverse Autoworks! Tenía una vibración en la parte delantera y Joe y su equipo la diagnosticaron y la resolvieron en poco tiempo. Gran flexibilidad para programar, servicio fantástico, precios competitivos y gente amable. Den una oportunidad a este pequeño negocio de dueño local (Joe) y no quedarán decepcionados.",
    "Fui por la inspección estatal y la rotación de llantas de un Tesla. Fue fácil conseguir cita y son muy agradables para tratar. Sin duda volvería.",
    "Joe y su equipo son los mejores. Buen servicio, explicaciones sencillas y él se esfuerza por encontrar opciones económicas cuando hace falta. También me gusta poder pagar el servicio por teléfono, lo que permite recoger el vehículo fuera del horario de atención.",
    "¡Personal muy amable y conocedor! Hacen el trabajo rápido y con esmero. También son accesibles y muy limpios, tratándose de talleres de carrocería.",
    "Llevé allí el Beetle 2015 de mi sobrina porque no funcionaba el vidrio de la ventana del conductor. Diverse lo arregló por unos $400 y funcionó una semana; lo llevé a VW y lo arreglaron, pero tuvieron que pedir una puerta nueva. VW dijo que quien lo arregló antes arruinó la puerta. ¡¡Costó $2000 repararla!! ¡¡Diverse no, gracias!!",
    "Esta gente es maravillosa. Fui por una reparación de emergencia, la resolvieron a un gran precio e incluso hicieron más de lo esperado. Si viviera por la zona, vendría aquí para todas mis necesidades de reparación y servicio del carro.",
    "Estoy muy impresionada y satisfecha con todos en Diverse. Me trataron muy bien. Se lo recomendaré a cualquiera que me pregunte. Seré clienta frecuente.",
    "Gran taller de reparación de carros. Los usamos desde hace años. Amables, limpios, confiables y con conocimiento.",
    "¡Esta gente es increíble! ¿Quiere alguien honesto, que le dé un buen precio y de vez en cuando un descuento? ¡Vaya a Diverse!",
    "Ariel fue de mucha ayuda para pedir una pieza para mi carro.",
    "¡Diverse es el mejor lugar al que ir! ¡Joe es el mejor de la zona y es excelente para trabajar con él!",
    "Son muy buenos con el trabajo y con la inspección.",
    "Excelente servicio. Profesionales y amables.",
    "Honestos y justos. Se enorgullecen de su trabajo.",
    "Gran taller",
    "Excelente servicio",
]

CARFAX = [
    "¡El equipo de Diverse Auto Works son los mecánicos amigables de su barrio! Son muy meticulosos, honestos y conocedores. Dan información detallada y una explicación clara del trabajo realizado. La sala de espera está limpia y tiene sofás cómodos, si hace falta.",
    "El servicio fue excelente y el carro quedó listo en un tiempo razonable. La comunicación también fue muy buena. Se lo recomendaría a cualquiera.",
    "Siempre cumplen con el horario y puedo esperar con confianza a que terminen el trabajo. También dan evaluaciones honestas del estado del vehículo y hacen recomendaciones razonables para reparaciones o reemplazos.",
    "Joe es maravilloso. El servicio se hace bien y no cuesta una fortuna. Todos ahí son amables y respetuosos.",
    "Siempre un servicio amable, precios competitivos, y pueden recomendar servicios adicionales, pero siempre como recomendación, sin presión.",
    "Diverse AW es una organización de primera, increíble. Servicio mecánico sobresaliente, gente maravillosa y cercana, trabajo honesto y un apoyo administrativo increíble. No puedo decir lo suficiente de lo bueno que es este taller y todo su personal de apoyo.",
    "Este es mi taller de confianza. El servicio es excelente y cercano. La calidad del trabajo es de primera y el costo es más que justo.",
    "Muy amables: me dieron un repaso completo del trabajo de servicio realizado y, al revisar las reparaciones recomendadas, me dijeron con honestidad qué tan crítica era cada una. El vehículo estuvo listo a tiempo. Cobros razonables.",
    "Hacen lo que hay que hacer y no tratan de vender cosas que no hacen falta. Es indescriptiblemente agradable poder confiar en su mecánico.",
    "No puedo decir lo suficiente de lo bueno que es Diverse. Siempre amables, profesionales, muy conocedores, y van más allá de lo necesario pensando en usted. Es como tener un mecánico en la propia familia en quien se puede confiar. Si quiere un gran servicio bien hecho, ¡recomiendo mucho Diverse Auto Works!",
    "¡Negocio maravilloso! Llevo más de 5 años yendo con mi Honda Civic. Se comunican muy bien y hacen todo mucho más fácil. Me avisan qué piezas probablemente habrá que reemplazar en la próxima visita para que pueda prepararme económicamente. ¡Ariel es de gran ayuda! ¡Muy recomendado!",
    "He usado Diverse varias veces y siempre he recibido un excelente servicio, amable. Incluso las personas en el mostrador saben lo que pasa con su carro y explican de maravilla lo que se hizo o lo que hay que hacer. ¡Una vez hasta con fotos! Así que... gran servicio, precios razonables, gente amable y confiable, ¡no hay mucho mejor que eso!",
    "Me escucharon y me ayudaron a diagnosticar el problema.",
    "Mi taller independiente local de confianza",
    "El mejor taller de la zona. Gran servicio.",
    "¡Siempre dispuestos a ayudar cuando es posible!",
    "Siempre el mejor centro de servicio automotriz",
    "Buena gente; hacen videos si reparan algo. ¡Los recomiendo mucho!",
    "Servicio rápido y amable para el mantenimiento de rutina y para los problemas.",
    "Honestos, justos, confiables. ¡Puede confiar en ellos!",
    "¡Joe y su equipo hacen un gran trabajo manteniendo nuestros vehículos! ¡Muy recomendados!",
    "¡Gran servicio! Volveré para los próximos servicios.",
    "Agradezco que la hora de la cita se cumplió como se dijo y que el trabajo se hizo bien y con prontitud.",
    "La recepción respondió rápido y el vehículo se atendió a tiempo.",
    "¡¡¡Estupendos como siempre!!!",
    "Excelente: servicio amable y profesional, ¡SIEMPRE!",
    "Siempre atentos y con excelente servicio",
    "Muy amables y eficientes. Espero menos de 30 minutos para un cambio de aceite.",
    "Gran lugar para ir. Amables y muy competentes.",
    "¡Diverse es increíble! Gran trabajo a un gran precio. ¡Justos y honestos! Joe y su equipo son los mejores.",
    "Muy amables y serviciales. Sin duda seré cliente de nuevo.",
    "¡Llevo más de 15 años viniendo aquí, y eso lo dice todo!",
    "¡Sin quejas! Los empleados fueron amables y respetuosos. Sin duda los volveré a usar.",
    "Un servicio excelente que va mucho más allá de lo normal. Gente maravillosa, considerada y honesta. No podríamos estar más contentos y agradecidos de que estén en la zona para un servicio de confianza. JHR",
    "Diverse Auto es un taller muy completo. Son amables, puntuales y cobran precios justos. Los recomiendo mucho a cualquiera que necesite un buen taller.",
    "Buena gente. Me encanta llevar la van allí sabiendo que recibimos un gran servicio de un taller automotriz honesto y confiable.",
    "Servicio amable y cortés. El personal conocedor se asegura de que usted conozca y entienda los problemas de su automóvil para tomar las decisiones adecuadas sobre cómo mantener mejor su vehículo.",
    "Se puede dejar el carro por la noche y recogerlo terminado a la mañana siguiente; además envían un mensaje de texto para recordarme la cita.",
    "Extremadamente serviciales y eficientes, y el único taller en el que confío para trabajar en mi carro. Arreglan lo que hay que arreglar y nada innecesario; son confiables y honestos.",
    "¡Ariel, en la recepción, es muy amable y lo explica todo! Como mujer soltera, ¡confío en sus recomendaciones y en su servicio!",
    "Diagnósticos cuidadosos. Recomendaciones sobre lo que hay que hacer y lo que puede esperar. Generan confianza.",
    "Son excelentes para programar y siempre explican bien los costos y las opciones de cualquier trabajo que he necesitado.",
    "Gran servicio, reparaciones puntuales",
    "Excelente servicio, taller bien administrado. ¡¡Ariel es la mejor!!",
    "Atención al cliente increíble. Gran trabajo mecánico a precio razonable.",
    "Joe es el mejor. ¡¡¡Entrar y salir en menos de 2 horas!!!",
    "¡¡¡Muy recomendado!!! Personal muy amable y conocedor.",
    "Todo estuvo bien. Diverse Auto Works es un buen lugar para llevar su carro.",
    "Gente honesta y gran trabajo.",
    "Amables, puntuales, conocedores y razonables. Gran lugar.",
    "Servicio excelente y justo para el cliente",
    "Se brindó un servicio rápido y amable",
    "Gran servicio, rápido y amable. Conocedores.",
    "Excelente servicio como siempre, Ariel es increíble.",
    "Gran comunicación, servicio puntual y explicación del trabajo realizado.",
    "¡Honestos y confiables! Las cualidades más importantes cuando le trabajan a su vehículo.",
    "Diverse es increíble y son honestos. Llevamos varios años yendo y confiamos en ellos.",
    "Gente excelente para trabajar, muy amable. Revisaron todo.",
    "Se atendió como se esperaba. Precios justos",
    "Muy profesionales y hacen todo lo posible por ayudar.",
    "¡Gran servicio y muy serviciales!",
]

YELP = [
    "Gran experiencia con la inspección de motocicleta. Mucha disponibilidad para la cita. ¡Servicio rápido!",
    "El motor de mi camioneta F150 hacía un ruido como de golpeteo. Pudieron haberme cobrado de más, pero encontraron una bujía defectuosa. Mi veredicto: ¡Cinco estrellas y DOS PULGARES ARRIBA!",
    "Me alegra haber encontrado al equipo de Diverse Auto Works. Lo mantienen informado de lo que pasa con su carro y lo devuelven a la carretera de forma segura, sin tratar de engañarlo con trabajos innecesarios para cobrar más. Trabajo de calidad, precios justos, constantes y amables, pero sobre todo honestos. Joe y Ariel son excelentes para trabajar. ¡Muy recomendado si necesita un taller local confiable en el que pueda confiar!",
    "¡Gente increíble! Me han dado donas, bagels y galletas. Los quiero mucho por ayudarme con los problemas de mi carro. Ariel es mi favorita. Con cariño, Fabi",
    "¡Esta gente es increíble, Ariel es fantástica! Si quiere un grupo automotriz honesto y un descuento de vez en cuando en el servicio, ¡vaya con Joe y su equipo!",
    "¡Gran experiencia ayer con este grupo! Viajaba por negocios en un día lluvioso y se me murió el alternador. Respondieron rápido, consiguieron la pieza y la cambiaron en cuestión de horas, lo que me permitió salvar el resto de mi jornada de trabajo, a un precio razonable. ¡Agradezco de verdad que se hayan adaptado a mi situación y me hayan ayudado a volver a la carretera tan rápido!",
    "Llevo muchos años trayendo mis carros a Diverse Autoworks. Joe y su equipo son excelentes, claros y honestos. Las instalaciones y las salas de espera están muy limpias y son cómodas.",
    "Mi primera experiencia con Diverse Autoworks fue después de un accidente de carro. La aseguradora me pidió que obtuviera un presupuesto de la reparación con ellos. Fueron amables, profesionales y eficientes. Lamentablemente, el carro terminó siendo pérdida total, pero después empecé a usarlos para el trabajo de rutina. Son puntuales y es bastante fácil conseguir cita para cambios de aceite y demás. Sus precios son muy razonables y se nota que tratan a sus clientes con honestidad. Pulgar arriba.",
]

YELP_REPLY = {
    6: "¡Muchas gracias por esta reseña! Nos ha encantado trabajar con usted y esperamos que sepa cuánto agradecemos su preferencia.",
}

FEATURED = [
    "También dan evaluaciones honestas del estado del vehículo y hacen recomendaciones razonables para reparaciones o reemplazos.",
    "Gran experiencia con la inspección de motocicleta. Mucha disponibilidad para la cita. ¡Servicio rápido!",
    "siempre un servicio amable, precios competitivos, y pueden recomendar servicios adicionales, pero siempre como recomendación, sin presión",
    "Me escucharon y me ayudaron a diagnosticar el problema.",
    "La comunicación también fue muy buena. Se lo recomendaría a cualquiera.",
    "Se comunican muy bien y hacen todo mucho más fácil.",
    "Llevo muchos años trayendo mis carros a Diverse Autoworks. Joe y su equipo son excelentes, claros y honestos. Las instalaciones y las salas de espera están muy limpias y son cómodas.",
    "Confiables y trabajadores. Llevamos todos nuestros carros allí para todo, desde inspecciones hasta llantas, etc.",
]

_AGE_UNITS = {"day": ("día", "días"), "week": ("semana", "semanas"), "month": ("mes", "meses"), "year": ("año", "años")}


def age_es(age):
    """'2 months ago' -> 'hace 2 meses'; 'a year ago' -> 'hace 1 año'."""
    parts = age.split()
    if len(parts) == 3 and parts[2] == "ago":
        n = 1 if parts[0] in ("a", "an") else int(parts[0])
        one, many = _AGE_UNITS[parts[1].rstrip("s")]
        return f"hace {n} {one if n == 1 else many}"
    return age
