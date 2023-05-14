#!/bin/bash

# create Command
create() {
  echo "create namespace"
  kubectl create namespace kafka
  kubectl create namespace grafana
  kubectl create namespace prometheus

  echo "install kafka"
  helm upgrade --install -f infra/kafka/ci/values.yaml -n kafka kafka infra/kafka/

  echo "install grafana"
  helm upgrade --install -f infra/grafana/ci/with-only-local-values.yaml -n grafana grafana infra/grafana/

  echo "install prometheus"
  helm upgrade --install -f infra/prometheus/ci/values.yaml -n prometheus prometheus infra/prometheus/

}

# Upgrade Command
upgrade() {
  # helm upgrade $RELEASE_NAME $CHART_NAME --namespace $NAMESPACE_NAME -f values.yaml
}

# Delete Command
delete() {
  helm uninstall -n kafka kafka
  helm uninstall -n grafana grafana
  helm uninstall -n prometheus prometheus

  kubectl delete namespace kafka
  kubectl delete namespace grafana
  kubectl delete namespace prometheus


}

# Main Menu
while true; do
  echo "Select the option:"
  echo "0. create the chart"
  echo "1. Upgrade the chart"
  echo "2. Delete the chart"
  echo "3. Exit"
  read OPTION

  case $OPTION in
    0) create ;;
    1) upgrade ;;
    2) delete ;;
    3) break ;;
    *) echo "Invalid Option" ;;
  esac
done
