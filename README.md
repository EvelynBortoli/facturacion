# facturacion
Sistema de facturación de llamadas telefónicas

Este sistema simplificado invoca a la función seleccionar usuario, ésta llama a la funcion facturar donde le pasamos como parametero el usuario seleccionado.
En la funcion facturar, recorremos la planilla de llamadas del usuario y vamos desagregandola en planillas mas pequeñas segun el tipo de llamada.
Luego le pasamos las planillas simplificadas a las funciones subTotalLocales,subtotalNacionales y subTotalInternacional. Estas funciones imprimen un detalle de las llamadas segun horario normal y reducido y luego retorna el costo de cada tipo de llamada.
Por ultimo, la funcion facturar realiza la suma de estos tres subtotales, calcula los impuestos y el total a facturar e imprime lo anterior mencionado por pantalla. 
