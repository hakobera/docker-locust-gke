# docker-locust-gke

Sample of locust cluster for Google Container Engine using [hakober/locust](https://github.com/hakobera/docker-locust) image.

## Push image

First, you should push image into your private repository.

```
$ export IMAGE_ID=locust-gke
$ ./script/cluster push
```

## Cluster management

## Set common environment value

```
$ export GKE_CLUSTER=<your-cluster>
$ export GKE_ZONE=<your-zone>
$ export GKE_NETWORK=<your-network>
```

### Start cluster

```
$ TARGET_URL=<your-load-test-target-url> \
  LOCUST_SLAVE_COUNT=2 \
  ./script/cluster start
```

### Stop cluster

```
$ ./script/cluster stop
```

### Show cluster status

```
$ ./script/cluster status
```

### Open kubernetes web console

```
$ ./script/cluster open-kubernetes
```

### Open locust web console

```
$ ./script/cluster open-locust
```
