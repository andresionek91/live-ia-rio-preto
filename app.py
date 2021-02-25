from aws_cdk import core
from bootcamp_data_platform_turma_3.data_lake.stack import DataLakeStack
from bootcamp_data_platform_turma_3.kinesis import KinesisStack

app = core.App()
data_lake = DataLakeStack(app)
kinesis_stack = KinesisStack(app, data_lake_raw_bucket=data_lake.data_lake_raw_bucket)
app.synth()
