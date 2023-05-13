### Helm 명령어

### install

```
helm upgrade --install -f .\values.yaml -n kafka-study kafka-helm-study .

helm upgrade --install -f .\ci\values.yaml -n kafka-study kafka-helm-study .

helm uninstall -n kafka-study kafka-helm-study


helm upgrade --install -f .\ci\with-only-local-values.yaml -n kafka-study grafana .

```


#### 
```
cd .\infra\kafka\
helm template -f .\ci\values.yaml > abc.yaml .
```
