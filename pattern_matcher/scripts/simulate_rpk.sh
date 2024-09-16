STR1='{
    "file": "/var/log/pods/kube-system_gke-metadata-server-frk4r_32b90713-8dd1-48bc-ad2a-d9558239b154/gke-metadata-server/0.log",
    "kubernetes": {
      "container_id": "containerd://95170dda2fbbcc71f895af766e9c6a3b09ad7db0ef30be211ee4881afbc2c0f0",
      "container_image": "gke.gcr.io/gke-metadata-server:gke_metadata_server_20240702.00_p0@sha256:aea9cc887c91b9a05e5bb4bb604180772594a01f0828bbfacf30c77562ac7205",
      "container_image_id": "gke.gcr.io/gke-metadata-server@sha256:aea9cc887c91b9a05e5bb4bb604180772594a01f0828bbfacf30c77562ac7205",
      "container_name": "gke-metadata-server",
      "namespace_labels": {
        "kubernetes.io/metadata.name": "kube-system"
      },
      "node_labels": {
        "beta.kubernetes.io/arch": "amd64",
        "beta.kubernetes.io/instance-type": "n1-standard-2",
        "beta.kubernetes.io/os": "linux",
        "cloud.google.com/gke-boot-disk": "pd-standard",
        "cloud.google.com/gke-container-runtime": "containerd",
        "cloud.google.com/gke-cpu-scaling-level": "2",
        "cloud.google.com/gke-logging-variant": "DEFAULT",
        "cloud.google.com/gke-max-pods-per-node": "110",
        "cloud.google.com/gke-memory-gb-scaling-level": "7",
        "cloud.google.com/gke-netd-ready": "true",
        "cloud.google.com/gke-nodepool": "user-pool",
        "cloud.google.com/gke-os-distribution": "cos",
        "cloud.google.com/gke-provisioning": "spot",
        "cloud.google.com/gke-spot": "true",
        "cloud.google.com/gke-stack-type": "IPV4",
        "cloud.google.com/machine-family": "n1",
        "cloud.google.com/private-node": "false",
        "cluster_name": "k8s-caas-0009-dev",
        "failure-domain.beta.kubernetes.io/region": "europe-west1",
        "failure-domain.beta.kubernetes.io/zone": "europe-west1-b",
        "iam.gke.io/gke-metadata-server-enabled": "true",
        "kubernetes.io/arch": "amd64",
        "kubernetes.io/hostname": "gke-k8s-caas-0009-dev-user-pool-0fc5bebd-x99w",
        "kubernetes.io/os": "linux",
        "node.kubernetes.io/instance-type": "n1-standard-2",
        "node_pool": "user-pool",
        "topology.gke.io/zone": "europe-west1-b",
        "topology.kubernetes.io/region": "europe-west1",
        "topology.kubernetes.io/zone": "europe-west1-b"
      },
      "pod_annotations": {
        "components.gke.io/component-name": "gke-metadata-server",
        "components.gke.io/component-version": "0.4.301",
        "monitoring.gke.io/path": "/metricz"
      },
      "pod_ip": "10.0.0.234",
      "pod_ips": [
        "10.0.0.234"
      ],
      "pod_labels": {
        "addonmanager.kubernetes.io/mode": "Reconcile",
        "controller-revision-hash": "868b4759f5",
        "k8s-app": "gke-metadata-server",
        "pod-template-generation": "3"
      },
      "pod_name": "gke-metadata-server-frk4r",
      "pod_namespace": "kube-system",
      "pod_node_name": "gke-k8s-caas-0009-dev-user-pool-0fc5bebd-x99w",
      "pod_owner": "DaemonSet/gke-metadata-server",
      "pod_uid": "32b90713-8dd1-48bc-ad2a-d9558239b154"
    },
    "message": "I0905 16:57:07.878540   74418 access_token.go:112] [conn-id:28ee2e817c5077fa rpc-id:5a52d15ecef3465c background-id:733be5458248c392 remote-addr:10.1.2.8:51444 pod:pacman/minimi-5d4b98fbfd-pfkrj] Fetching access token for service account \"pacman-rancher@adls-046l8ixrg6rj4xuwfh5klxzq1.iam.gserviceaccount.com\" with delegates \"\" in pod pacman/minimi-5d4b98fbfd-pfkrj.",
    "source_type": "kubernetes_logs",
    "stream": "stderr",
    "timestamp": "2024-09-05T16:57:07.878828081Z"
  }';
STR2='{
    "file": "/var/log/pods/kube-system_gke-metadata-server-frk4r_32b90713-8dd1-48bc-ad2a-d9558239b154/gke-metadata-server/0.log",
    "kubernetes": {
      "container_id": "containerd://95170dda2fbbcc71f895af766e9c6a3b09ad7db0ef30be211ee4881afbc2c0f0",
      "container_image": "gke.gcr.io/gke-metadata-server:gke_metadata_server_20240702.00_p0@sha256:aea9cc887c91b9a05e5bb4bb604180772594a01f0828bbfacf30c77562ac7205",
      "container_image_id": "gke.gcr.io/gke-metadata-server@sha256:aea9cc887c91b9a05e5bb4bb604180772594a01f0828bbfacf30c77562ac7205",
      "container_name": "gke-metadata-server",
      "namespace_labels": {
        "kubernetes.io/metadata.name": "kube-system"
      },
      "node_labels": {
        "beta.kubernetes.io/arch": "amd64",
        "beta.kubernetes.io/instance-type": "n1-standard-2",
        "beta.kubernetes.io/os": "linux",
        "cloud.google.com/gke-boot-disk": "pd-standard",
        "cloud.google.com/gke-container-runtime": "containerd",
        "cloud.google.com/gke-cpu-scaling-level": "2",
        "cloud.google.com/gke-logging-variant": "DEFAULT",
        "cloud.google.com/gke-max-pods-per-node": "110",
        "cloud.google.com/gke-memory-gb-scaling-level": "7",
        "cloud.google.com/gke-netd-ready": "true",
        "cloud.google.com/gke-nodepool": "user-pool",
        "cloud.google.com/gke-os-distribution": "cos",
        "cloud.google.com/gke-provisioning": "spot",
        "cloud.google.com/gke-spot": "true",
        "cloud.google.com/gke-stack-type": "IPV4",
        "cloud.google.com/machine-family": "n1",
        "cloud.google.com/private-node": "false",
        "cluster_name": "k8s-caas-0009-dev",
        "failure-domain.beta.kubernetes.io/region": "europe-west1",
        "failure-domain.beta.kubernetes.io/zone": "europe-west1-b",
        "iam.gke.io/gke-metadata-server-enabled": "true",
        "kubernetes.io/arch": "amd64",
        "kubernetes.io/hostname": "gke-k8s-caas-0009-dev-user-pool-0fc5bebd-x99w",
        "kubernetes.io/os": "linux",
        "node.kubernetes.io/instance-type": "n1-standard-2",
        "node_pool": "user-pool",
        "topology.gke.io/zone": "europe-west1-b",
        "topology.kubernetes.io/region": "europe-west1",
        "topology.kubernetes.io/zone": "europe-west1-b"
      },
      "pod_annotations": {
        "components.gke.io/component-name": "gke-metadata-server",
        "components.gke.io/component-version": "0.4.301",
        "monitoring.gke.io/path": "/metricz"
      },
      "pod_ip": "10.0.0.234",
      "pod_ips": [
        "10.0.0.234"
      ],
      "pod_labels": {
        "addonmanager.kubernetes.io/mode": "Reconcile",
        "controller-revision-hash": "868b4759f5",
        "k8s-app": "gke-metadata-server",
        "pod-template-generation": "3"
      },
      "pod_name": "gke-metadata-server-frk4r",
      "pod_namespace": "kube-system",
      "pod_node_name": "gke-k8s-caas-0009-dev-user-pool-0fc5bebd-x99w",
      "pod_owner": "DaemonSet/gke-metadata-server",
      "pod_uid": "32b90713-8dd1-48bc-ad2a-d9558239b154"
    },
    "message": "I0905 16:57:07.923548   74418 loading_cache.go:230] [conn-id:28ee2e817c5077fa rpc-id:5a52d15ecef3465c remote-addr:10.1.2.8:51444 pod:pacman/minimi-5d4b98fbfd-pfkrj] Loading new entry succeeded",
    "source_type": "kubernetes_logs",
    "stream": "stderr",
    "timestamp": "2024-09-05T16:57:07.923896481Z"
  }';
STR3='{
    "file": "/var/log/pods/kube-system_gke-metadata-server-frk4r_32b90713-8dd1-48bc-ad2a-d9558239b154/gke-metadata-server/0.log",
    "kubernetes": {
      "container_id": "containerd://95170dda2fbbcc71f895af766e9c6a3b09ad7db0ef30be211ee4881afbc2c0f0",
      "container_image": "gke.gcr.io/gke-metadata-server:gke_metadata_server_20240702.00_p0@sha256:aea9cc887c91b9a05e5bb4bb604180772594a01f0828bbfacf30c77562ac7205",
      "container_image_id": "gke.gcr.io/gke-metadata-server@sha256:aea9cc887c91b9a05e5bb4bb604180772594a01f0828bbfacf30c77562ac7205",
      "container_name": "gke-metadata-server",
      "namespace_labels": {
        "kubernetes.io/metadata.name": "kube-system"
      },
      "node_labels": {
        "beta.kubernetes.io/arch": "amd64",
        "beta.kubernetes.io/instance-type": "n1-standard-2",
        "beta.kubernetes.io/os": "linux",
        "cloud.google.com/gke-boot-disk": "pd-standard",
        "cloud.google.com/gke-container-runtime": "containerd",
        "cloud.google.com/gke-cpu-scaling-level": "2",
        "cloud.google.com/gke-logging-variant": "DEFAULT",
        "cloud.google.com/gke-max-pods-per-node": "110",
        "cloud.google.com/gke-memory-gb-scaling-level": "7",
        "cloud.google.com/gke-netd-ready": "true",
        "cloud.google.com/gke-nodepool": "user-pool",
        "cloud.google.com/gke-os-distribution": "cos",
        "cloud.google.com/gke-provisioning": "spot",
        "cloud.google.com/gke-spot": "true",
        "cloud.google.com/gke-stack-type": "IPV4",
        "cloud.google.com/machine-family": "n1",
        "cloud.google.com/private-node": "false",
        "cluster_name": "k8s-caas-0009-dev",
        "failure-domain.beta.kubernetes.io/region": "europe-west1",
        "failure-domain.beta.kubernetes.io/zone": "europe-west1-b",
        "iam.gke.io/gke-metadata-server-enabled": "true",
        "kubernetes.io/arch": "amd64",
        "kubernetes.io/hostname": "gke-k8s-caas-0009-dev-user-pool-0fc5bebd-x99w",
        "kubernetes.io/os": "linux",
        "node.kubernetes.io/instance-type": "n1-standard-2",
        "node_pool": "user-pool",
        "topology.gke.io/zone": "europe-west1-b",
        "topology.kubernetes.io/region": "europe-west1",
        "topology.kubernetes.io/zone": "europe-west1-b"
      },
      "pod_annotations": {
        "components.gke.io/component-name": "gke-metadata-server",
        "components.gke.io/component-version": "0.4.301",
        "monitoring.gke.io/path": "/metricz"
      },
      "pod_ip": "10.0.0.234",
      "pod_ips": [
        "10.0.0.234"
      ],
      "pod_labels": {
        "addonmanager.kubernetes.io/mode": "Reconcile",
        "controller-revision-hash": "868b4759f5",
        "k8s-app": "gke-metadata-server",
        "pod-template-generation": "3"
      },
      "pod_name": "gke-metadata-server-frk4r",
      "pod_namespace": "kube-system",
      "pod_node_name": "gke-k8s-caas-0009-dev-user-pool-0fc5bebd-x99w",
      "pod_owner": "DaemonSet/gke-metadata-server",
      "pod_uid": "32b90713-8dd1-48bc-ad2a-d9558239b154"
    },
    "message": "I0905 16:57:07.923670   74385 serviceaccounts.go:168] [conn-id:28ee2e817c5077fa rpc-id:5a52d15ecef3465c remote-addr:10.1.2.8:51444 pod:pacman/minimi-5d4b98fbfd-pfkrj] Fetched token for pod pacman/minimi-5d4b98fbfd-pfkrj",
    "source_type": "kubernetes_logs",
    "stream": "stderr",
    "timestamp": "2024-09-05T16:57:07.923943879Z"
  }';
STR4='{
    "file": "/var/log/pods/kube-system_gke-metadata-server-frk4r_32b90713-8dd1-48bc-ad2a-d9558239b154/gke-metadata-server/0.log",
    "kubernetes": {
      "container_id": "containerd://95170dda2fbbcc71f895af766e9c6a3b09ad7db0ef30be211ee4881afbc2c0f0",
      "container_image": "gke.gcr.io/gke-metadata-server:gke_metadata_server_20240702.00_p0@sha256:aea9cc887c91b9a05e5bb4bb604180772594a01f0828bbfacf30c77562ac7205",
      "container_image_id": "gke.gcr.io/gke-metadata-server@sha256:aea9cc887c91b9a05e5bb4bb604180772594a01f0828bbfacf30c77562ac7205",
      "container_name": "gke-metadata-server",
      "namespace_labels": {
        "kubernetes.io/metadata.name": "kube-system"
      },
      "node_labels": {
        "beta.kubernetes.io/arch": "amd64",
        "beta.kubernetes.io/instance-type": "n1-standard-2",
        "beta.kubernetes.io/os": "linux",
        "cloud.google.com/gke-boot-disk": "pd-standard",
        "cloud.google.com/gke-container-runtime": "containerd",
        "cloud.google.com/gke-cpu-scaling-level": "2",
        "cloud.google.com/gke-logging-variant": "DEFAULT",
        "cloud.google.com/gke-max-pods-per-node": "110",
        "cloud.google.com/gke-memory-gb-scaling-level": "7",
        "cloud.google.com/gke-netd-ready": "true",
        "cloud.google.com/gke-nodepool": "user-pool",
        "cloud.google.com/gke-os-distribution": "cos",
        "cloud.google.com/gke-provisioning": "spot",
        "cloud.google.com/gke-spot": "true",
        "cloud.google.com/gke-stack-type": "IPV4",
        "cloud.google.com/machine-family": "n1",
        "cloud.google.com/private-node": "false",
        "cluster_name": "k8s-caas-0009-dev",
        "failure-domain.beta.kubernetes.io/region": "europe-west1",
        "failure-domain.beta.kubernetes.io/zone": "europe-west1-b",
        "iam.gke.io/gke-metadata-server-enabled": "true",
        "kubernetes.io/arch": "amd64",
        "kubernetes.io/hostname": "gke-k8s-caas-0009-dev-user-pool-0fc5bebd-x99w",
        "kubernetes.io/os": "linux",
        "node.kubernetes.io/instance-type": "n1-standard-2",
        "node_pool": "user-pool",
        "topology.gke.io/zone": "europe-west1-b",
        "topology.kubernetes.io/region": "europe-west1",
        "topology.kubernetes.io/zone": "europe-west1-b"
      },
      "pod_annotations": {
        "components.gke.io/component-name": "gke-metadata-server",
        "components.gke.io/component-version": "0.4.301",
        "monitoring.gke.io/path": "/metricz"
      },
      "pod_ip": "10.0.0.234",
      "pod_ips": [
        "10.0.0.234"
      ],
      "pod_labels": {
        "addonmanager.kubernetes.io/mode": "Reconcile",
        "controller-revision-hash": "868b4759f5",
        "k8s-app": "gke-metadata-server",
        "pod-template-generation": "3"
      },
      "pod_name": "gke-metadata-server-frk4r",
      "pod_namespace": "kube-system",
      "pod_node_name": "gke-k8s-caas-0009-dev-user-pool-0fc5bebd-x99w",
      "pod_owner": "DaemonSet/gke-metadata-server",
      "pod_uid": "32b90713-8dd1-48bc-ad2a-d9558239b154"
    },
    "message": "I0905 16:57:07.923775   74385 metadata.go:216] [conn-id:28ee2e817c5077fa rpc-id:5a52d15ecef3465c remote-addr:10.1.2.8:51444 pod:pacman/minimi-5d4b98fbfd-pfkrj] \"/computeMetadata/v1/instance/service-accounts/default/token\" HTTP/200, started at 2024-09-05 16:57:07.877386649 +0000 UTC m=+128164.085248183",
    "source_type": "kubernetes_logs",
    "stream": "stderr",
    "timestamp": "2024-09-05T16:57:07.924210030Z"
  }';
STR5='{
    "file": "/var/log/pods/ingress-nginx_ingress-nginx-controller-cf668668c-zjq26_7d2b6ad9-7098-42a0-9231-bfeb2811f1c1/controller/0.log",
    "kubernetes": {
      "container_id": "containerd://7627d9dc3f4db8275bf5b06480ef128caacaefb3a2d7d38ec0df04ac8b292c59",
      "container_image": "registry.k8s.io/ingress-nginx/controller:v1.10.1@sha256:e24f39d3eed6bcc239a56f20098878845f62baa34b9f2be2fd2c38ce9fb0f29e",
      "container_image_id": "registry.k8s.io/ingress-nginx/controller@sha256:e24f39d3eed6bcc239a56f20098878845f62baa34b9f2be2fd2c38ce9fb0f29e",
      "container_name": "controller",
      "namespace_labels": {
        "kubernetes.io/metadata.name": "ingress-nginx",
        "name": "ingress-nginx"
      },
      "node_labels": {
        "beta.kubernetes.io/arch": "amd64",
        "beta.kubernetes.io/instance-type": "n1-standard-2",
        "beta.kubernetes.io/os": "linux",
        "cloud.google.com/gke-boot-disk": "pd-standard",
        "cloud.google.com/gke-container-runtime": "containerd",
        "cloud.google.com/gke-cpu-scaling-level": "2",
        "cloud.google.com/gke-logging-variant": "DEFAULT",
        "cloud.google.com/gke-max-pods-per-node": "110",
        "cloud.google.com/gke-memory-gb-scaling-level": "7",
        "cloud.google.com/gke-netd-ready": "true",
        "cloud.google.com/gke-nodepool": "user-pool",
        "cloud.google.com/gke-os-distribution": "cos",
        "cloud.google.com/gke-provisioning": "spot",
        "cloud.google.com/gke-spot": "true",
        "cloud.google.com/gke-stack-type": "IPV4",
        "cloud.google.com/machine-family": "n1",
        "cloud.google.com/private-node": "false",
        "cluster_name": "k8s-caas-0009-dev",
        "failure-domain.beta.kubernetes.io/region": "europe-west1",
        "failure-domain.beta.kubernetes.io/zone": "europe-west1-b",
        "iam.gke.io/gke-metadata-server-enabled": "true",
        "kubernetes.io/arch": "amd64",
        "kubernetes.io/hostname": "gke-k8s-caas-0009-dev-user-pool-0fc5bebd-x99w",
        "kubernetes.io/os": "linux",
        "node.kubernetes.io/instance-type": "n1-standard-2",
        "node_pool": "user-pool",
        "topology.gke.io/zone": "europe-west1-b",
        "topology.kubernetes.io/region": "europe-west1",
        "topology.kubernetes.io/zone": "europe-west1-b"
      },
      "pod_ip": "10.1.2.7",
      "pod_ips": [
        "10.1.2.7"
      ],
      "pod_labels": {
        "app.kubernetes.io/component": "controller",
        "app.kubernetes.io/instance": "ingress-nginx",
        "app.kubernetes.io/managed-by": "Helm",
        "app.kubernetes.io/name": "ingress-nginx",
        "app.kubernetes.io/part-of": "ingress-nginx",
        "app.kubernetes.io/version": "1.10.1",
        "helm.sh/chart": "ingress-nginx-4.10.1",
        "pod-template-hash": "cf668668c"
      },
      "pod_name": "ingress-nginx-controller-cf668668c-zjq26",
      "pod_namespace": "ingress-nginx",
      "pod_node_name": "gke-k8s-caas-0009-dev-user-pool-0fc5bebd-x99w",
      "pod_owner": "ReplicaSet/ingress-nginx-controller-cf668668c",
      "pod_uid": "7d2b6ad9-7098-42a0-9231-bfeb2811f1c1"
    },
    "message": "213.225.5.111 - - [05/Sep/2024:16:57:07 +0000] \"GET /curl?url=http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/token HTTP/2.0\" 200 1083 \"-\" \"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36\" 594 0.085 [pacman-minimi-80] [] 10.1.2.8:8080 1083 0.085 200 92ac5d91aaa6a3625044b661fce963ea",
    "source_type": "kubernetes_logs",
    "stream": "stdout",
    "timestamp": "2024-09-05T16:57:07.932937874Z"
  }';


echo $STR1 | rpk topic produce signal;
echo $STR2 | rpk topic produce signal;
echo $STR3 | rpk topic produce signal;
echo $STR4 | rpk topic produce signal;
echo $STR5 | rpk topic produce signal;
