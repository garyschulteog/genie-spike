#!/bin/bash

export YARN_CONF_DIR=${GENIE_CLUSTER_DIR}/config/

set -o errexit -o nounset -o pipefail

# copy hive-site.xml configuration
#cp ${GENIE_COMMAND_DIR}/config/* ${SPARK_CONF_DIR}
