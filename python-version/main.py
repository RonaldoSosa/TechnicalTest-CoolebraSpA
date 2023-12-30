import create_data_function as cdf
import create_query_function as cq
import group_by_function as gbf

# Creo la base de datos
cdf.create_data()
# Realizo la consulta a la base de datos
data = cq.create_query()
# LLamo a la función group_by_ean para agrupar los datos
grouped_data = gbf.group_by_ean(data)
# Imprimo los datos
print(grouped_data)
# Se muestran los datos de la lista con salto de línea
print(*grouped_data, sep='\n')
