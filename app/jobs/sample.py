"""sample batch job"""

import click
import logging

from pyspark.sql import SparkSession, DataFrame

from app.readers.csv import read_csv
from app.writers.csv import write_csv
from app.utils.spark import get_spark_session
from app.transform.common import rename_cols


logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


@click.command()
@click.option(
    "--input_path",
    "-i",
    type=str,
    required=True,
    default="data/input/userIds_prod.csv",
    help="Path to input csv file",
)
@click.option(
    "--output_path",
    "-o",
    type=str,
    required=True,
    default="data/output",
    help="Path to output folder (e.g data/output)",
)
def sample_job(input_path: str, output_path: str) -> None:
    # Get spark session
    logging.info("Creating Spark session")
    spark: SparkSession = get_spark_session(app_name="PySpark Job")

    # Read data
    logging.info(f"Reading data from {input_path}")
    df: DataFrame = read_csv(spark, input_path)

    # Transform data
    logging.info("Transforming data")
    df_transformed: DataFrame = rename_cols(df, columns={"offerAmount": "offer_amount"})

    # Write result data
    logging.info(f"Writing data to {output_path}")
    write_csv(df_transformed, output_path)
