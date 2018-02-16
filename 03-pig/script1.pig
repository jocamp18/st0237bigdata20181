#cargar datos desde Hbase



# cargar datos
raw_data = load '/user/emontoya/datasets/hdi-data.csv' using PigStorage(',') as (id:chararray, country:chararray, d1:float,d2:float,d3:float,d4:float,d5:float,d6:float,d7:float);

# imprimir los datos
dump raw_data;

#describir los datos
describe raw_data;
