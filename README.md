# PySpark Template

This is a template for creating pyspark applications/jobs. It can be cloned and customized based on project specific needs. Its managed using poetry and
used pyspark for local development.

## Setup

1. Clone the project, by running the below command.

```bash
git clone <git url>
```

2. cd into the root folder, by running the folder

```bash
cd pyspark-template
```

3. Install the dependencies

```bash
poetry install
```


## Run the spark job

### In Local

To run the sample_job script using poetry, use the below convention to start the job:

```bash
poetry run sample_job  --input_path path_to_input_file --output_pathpath_to_output_folder
```

Example:

```bash
poetry run sample_job --input_path data/input/userIds_prod.csv --output_path data/output
```

### On AWS EMR

```bash
spark-submit --master yarn --deploy-mode cluster app/jobs/sample_job.py --input_path path_to_input_file --output_path path_to_output_file
```

Example:

```bash
spark-submit --master yarn --deploy-mode cluster app/jobs/sample_job.py --input_path data/input/userIds_prod.csv --output_path data/output
```


## Dev Scripts

To format the code in local, run the below command:

```bash
poetry run black app/*
```