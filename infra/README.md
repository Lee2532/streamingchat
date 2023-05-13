### Helm 명령어

### install

```
kafka

kubectl create namespace kafka-study

helm pull bitnami/kafka

helm upgrade --install -f .\ci\values.yaml -n kafka-study kafka-helm-study .


---
delete

helm uninstall -n kafka-study kafka-helm-study

---
Grafana

kubectl create namespace grafana

helm upgrade --install -f .\ci\with-only-local-values.yaml -n grafana grafana .

helm uninstall -n grafana grafana

http://host.docker.internal:80

---
prometheus

kubectl create namespace prometheus


helm upgrade --install -f .\ci\values.yaml -n prometheus prometheus .
helm uninstall -n prometheus prometheus




```


#### 
```
template


helm template -f .\ci\values.yaml > abc.yaml .
```
