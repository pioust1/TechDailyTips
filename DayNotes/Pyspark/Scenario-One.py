"""
Spark Scenario practice:
Split the columns with multiple delimiters ( one column having another delimiter)
like:
range,500|600|700
marks,102|103|105

output: should contain four columns and also convert to multiple rows
range,500,600,700
marks,102,103,105
"""

import logging
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, split, explode

logging.basicConfig(filename="scenario.log", level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def create_session():
    """
    Create Spark Session to communicate with the spark cluster
    :return: Spark Session
    """
    logging.debug(f" Create a Spark Session")
    spark_sess = SparkSession.builder.appName("Spark-Session-One").getOrCreate()

    return spark_sess


def main():
    """

    :return:
    """
    logging.debug(f" Entered the main function")
    spark_session = create_session()
    schema_file = "value_one  string , value_two string"
    read_file = spark_session.read.format("csv").schema(schema_file). \
        load(
       "C:\\Users\pious.tiwari\OneDrive - Accenture\CANADA\INTERVIEW\SPARK\practice\Scenario1Dataset\\scenario-one.csv")
    read_file.printSchema()
    read_file.show(2, truncate=False)
    # first we split the value using split function , it will create an array (list)
    read_file = read_file.withColumn("Temp_{}".format("value_two"), split(col("value_two"), "\\|"))
    # We can convert the multiple values coming in the array to the rows using the explode function
    read_file = read_file.withColumn("Temp1_{}".format("value_two"), explode(col("Temp_{}".format("value_two"))))
    read_file.show()
    read_file.printSchema()
    total_array_length = len(read_file.select("Temp_{}".format("value_two")).first()["Temp_value_two"])
    logging.debug(f" array_value {total_array_length}")
    df_list = read_file.columns
    logging.debug(f" the total number of columns are {df_list}")
    # Now, we need to convert the array created to the multiple columns, here in our case we know that the list contains
    # three values we need three more columns, but it can be dynamic as well, so we identify the length
    # of the array, and then we loop through  each value and create a new column
    read_file_new = read_file.select(df_list +
                                     [(col("Temp_{}".format("value_two"))[x]).alias("Value_{}".format(x+1))
                                      for x in range(0, total_array_length)])
    read_file_new.printSchema()
    read_file_new.show()


if __name__ == '__main__':
    main()
