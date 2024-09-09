from typing import TypedDict

class TetragonLogKubernetes(TypedDict):
    container_id: str
    container_image: str
    container_image_id: str
    container_name: str
    namespace_labels: dict[str, str]
    node_labels: dict[str, str]
    pod_annotations: dict[str, str]
    pod_ip: str
    pod_ips: list[str]
    pod_labels: dict[str, str]
    pod_name: str
    pod_namespace: str
    pod_node_name: str
    pod_owner: str
    pod_uid: str


class TetragonLog(TypedDict):
    file: str
    kubernetes: TetragonLogKubernetes
    message: str
    source_type: str
    stream: str
    timestamp: str

