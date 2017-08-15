/usr/bin/python2.7

# modeled from client example init

import logging

import yaml
from pygenie.client import Genie
from pygenie.conf import GenieConf

logging.basicConfig(level=logging.WARNING)

LOGGER = logging.getLogger(__name__)


def load_yaml(yaml_file):
    with open(yaml_file) as _file:
        return yaml.load(_file)


genie_conf = GenieConf()
genie_conf.genie.url = "http://localhost:8080"

genie = Genie(genie_conf)

hadoop_application = load_yaml("applications/hadoop273.yml")
hadoop_application_id = genie.create_application(hadoop_application)
LOGGER.warn("Created Hadoop 2.7.3 application with id = [%s]" % hadoop_application_id)

spark_application = load_yaml("applications/spark220.yml")
spark_application_id = genie.create_application(spark_application)
LOGGER.warn("Created spark 2.2.0 application with id = [%s]" % spark_application_id)

hadoop_command = load_yaml("commands/hadoop273.yml")
hadoop_command_id = genie.create_command(hadoop_command)
LOGGER.warn("Created Hadoop command with id = [%s]" % hadoop_command_id)

spark_command = load_yaml("commands/sparkSubmit220.yml")
spark_command_id = genie.create_command(spark_command)
LOGGER.warn("Created spark command with id = [%s]" % spark_command_id)

genie.set_application_for_command(hadoop_command_id, [hadoop_application_id])
LOGGER.warn("Set applications for Hadoop command to = [%s]" % hadoop_application_id)

genie.set_application_for_command(spark_command_id, [spark_application_id])
LOGGER.warn("Set applications for Spark submit command to = [%s]" % spark_application_id)

test_cluster = load_yaml("clusters/geniedemo-sandbox.yml")
test_cluster_id = genie.create_cluster(test_cluster)
LOGGER.warn("Created test cluster with id = [%s]" % test_cluster_id)

test2_cluster = load_yaml("clusters/ariatest-sandbox.yml")
test2_cluster_id = genie.create_cluster(test2_cluster)
LOGGER.warn("Created test2 cluster with id = [%s]" % test_cluster_id)

genie.set_commands_for_cluster(
    test_cluster_id,
    [hadoop_command_id, spark_command_id]
)

genie.set_commands_for_cluster(
    test2_cluster_id,
    [hadoop_command_id, spark_command_id]
)
LOGGER.warn("Added all commands to the test cluster with id = [%s]" % test_cluster_id)
