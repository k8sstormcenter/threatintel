from patternmatcher.model import TetragonLog
from patternmatcher.parse import transform_log_to_stix


def test_transform_log_to_stix():
    log: TetragonLog = {
        "file": "/var/log/pods/kube-system_gke-metadata-server-frk4r_32b90713-8dd1-48bc-ad2a-d9558239b154/gke-metadata-server/0.log",
        "kubernetes": {
            "container_id": "containerd://95170dda2fbbcc71f895af766e9c6a3b09ad7db0ef30be211ee4881afbc2c0f0",
            "container_image": "gke.gcr.io/gke-metadata-server:gke_metadata_server_20240702.00_p0@sha256:aea9cc887c91b9a05e5bb4bb604180772594a01f0828bbfacf30c77562ac7205",
            "container_image_id": "gke.gcr.io/gke-metadata-server@sha256:aea9cc887c91b9a05e5bb4bb604180772594a01f0828bbfacf30c77562ac7205",
            "container_name": "gke-metadata-server",
            "namespace_labels": {"kubernetes.io/metadata.name": "kube-system"},
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
                "topology.kubernetes.io/zone": "europe-west1-b",
            },
            "pod_annotations": {
                "components.gke.io/component-name": "gke-metadata-server",
                "components.gke.io/component-version": "0.4.301",
                "monitoring.gke.io/path": "/metricz",
            },
            "pod_ip": "10.0.0.234",
            "pod_ips": ["10.0.0.234"],
            "pod_labels": {
                "addonmanager.kubernetes.io/mode": "Reconcile",
                "controller-revision-hash": "868b4759f5",
                "k8s-app": "gke-metadata-server",
                "pod-template-generation": "3",
            },
            "pod_name": "gke-metadata-server-frk4r",
            "pod_namespace": "kube-system",
            "pod_node_name": "gke-k8s-caas-0009-dev-user-pool-0fc5bebd-x99w",
            "pod_owner": "DaemonSet/gke-metadata-server",
            "pod_uid": "32b90713-8dd1-48bc-ad2a-d9558239b154",
        },
        "message": "I0905 16:57:07.923548   74418 loading_cache.go:230] [conn-id:28ee2e817c5077fa rpc-id:5a52d15ecef3465c remote-addr:10.1.2.8:51444 pod:pacman/minimi-5d4b98fbfd-pfkrj] Loading new entry succeeded",
        "source_type": "kubernetes_logs",
        "stream": "stderr",
        "timestamp": "2024-09-05T16:57:07.923896481Z",
    }

    transformed = transform_log_to_stix(log)

    print(transformed)
