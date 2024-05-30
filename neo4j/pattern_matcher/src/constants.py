STIX_VERSION = '2.1'

STIX_INDICATOR_PATTERN_EXAMPLE = "[file:name = '/usr/bin/tail']"
STIX_INDICATOR_PATTERN_EXAMPLE2 = "[process:command_line MATCHES 'kubectl logs .*']"

TETRAGON_PROCESS_KPROBE_LOG_EXAMPLE = {
    "node_name": "k8s-agent-001",
    "process_kprobe": {
        "action": "KPROBE_ACTION_POST",
        "policy_name": "enumerate-service-account",
        "function_name": "security_file_permission",
        "args": [
            {
                "file_arg": {
                    "path": "/run/secrets/kubernetes.io/serviceaccount/..2024_05_30_15_39_47.3115319183/token"
                }
            },
            {
                "int_arg": 4
            }
        ],
        "parent": {
            "arguments": "-- rancher --http-listen-port=80 --https-listen-port=443 --audit-log-path=/var/log/auditlog/rancher-api-audit.log --audit-level=1 --audit-log-maxage=1 --audit-log-maxbackup=1 --audit-log-maxsize=100 --no-cacerts --http-listen-port=80 --https-listen-port=443 --add-local=true",
            "binary": "/usr/bin/tini",
            "cwd": "/var/lib/rancher",
            "docker": "9a3331f9d3ba7a82582f8cc145e3ac9",
            "flags": "procFS auid",
            "pod": {
                "container": {
                    "id": "containerd://9a3331f9d3ba7a82582f8cc145e3ac9546a549f16a76177693354007bd12f1f5",
                    "image": {
                        "id": "docker.io/rancher/rancher@sha256:0c8932d64c47c6e74f914cc02ce6cf606da188f6246dd34f92508fc594c63e38",
                        "name": "docker.io/rancher/rancher:v2.8.3"
                    },
                    "name": "rancher"
                },
                "name": "rancher-55966c8d68-fh7jb",
                "namespace": "cattle-system",
                "pod_labels": {
                    "app": "rancher",
                    "pod-template-hash": "55966c8d68",
                    "release": "rancher"
                },
                "workload": "rancher",
                "workload_kind": "Deployment"
            }
        },
        "process": {
            "arguments": "--http-listen-port=80 --https-listen-port=443 --audit-log-path=/var/log/auditlog/rancher-api-audit.log --audit-level=1 --audit-log-maxage=1 --audit-log-maxbackup=1 --audit-log-maxsize=100 --no-cacerts --http-listen-port=80 --https-listen-port=443 --add-local=true",
            "binary": "/usr/bin/rancher",
            "cwd": "/var/lib/rancher",
            "docker": "9a3331f9d3ba7a82582f8cc145e3ac9",
            "flags": "procFS auid",
            "pod": {
                "container": {
                    "id": "containerd://9a3331f9d3ba7a82582f8cc145e3ac9546a549f16a76177693354007bd12f1f5",
                    "image": {
                        "id": "docker.io/rancher/rancher@sha256:0c8932d64c47c6e74f914cc02ce6cf606da188f6246dd34f92508fc594c63e38",
                        "name": "docker.io/rancher/rancher:v2.8.3"
                    },
                    "name": "rancher"
                },
                "name": "rancher-55966c8d68-fh7jb",
                "namespace": "cattle-system",
                "pod_labels": {
                    "app": "rancher",
                    "pod-template-hash": "55966c8d68",
                    "release": "rancher"
                },
                "workload": "rancher",
                "workload_kind": "Deployment"
            },
            "refcnt": 1
        },
        "return": {
            "int_arg": 0
        }
    }
}

TETRAGON_PROCESS_EXEC_LOG_EXAMPLE = {
    "node_name": "k8s-agent-002",
    "process_exec": {
        "parent": {
            "arguments": "-namespace k8s.io -id e398dd9deb6d850fcc9327f16b3b1204135ed4ea6a27750160d340ca467fa087 -address /run/k3s/containerd/containerd.sock",
            "auid": 4294967295,
            "binary": "/var/lib/rancher/rke2/data/v1.28.8-rke2r1-c4073db9beee/bin/containerd-shim-runc-v2",
            "cwd": "/run/k3s/containerd/io.containerd.runtime.v2.task/k8s.io/e398dd9deb6d850fcc9327f16b3b1204135ed4ea6a27750160d340ca467fa087",
            "exec_id": "azhzLWFnZW50LTAwMjoxMjUxMjMwMDAwMDAwOjEzMzEy",
            "flags": "procFS auid",
            "parent_exec_id": "azhzLWFnZW50LTAwMjo2MDAwMDAwMDox",
            "pid": 13312,
            "start_time": "2024-03-30T18:13:47.987328791Z",
            "tid": 13312,
            "uid": 0
        },
        "process": {
            "arguments": "-F /var/log/auditlog/rancher-api-audit.log",
            "auid": 4294967295,
            "binary": "/usr/bin/tail",
            "cwd": "/",
            "docker": "4b7371b1104abe7634abc1c6f00d04a",
            "exec_id": "azhzLWFnZW50LTAwMjoxMjg2NzUwMDAwMDAwOjE0Mjg3",
            "flags": "procFS auid rootcwd",
            "parent_exec_id": "azhzLWFnZW50LTAwMjoxMjUxMjMwMDAwMDAwOjEzMzEy",
            "pid": 14287,
            "pod": {
                "container": {
                    "id": "containerd://4b7371b1104abe7634abc1c6f00d04a9ab79145d6093bec2783933a206afc632",
                    "image": {
                        "id": "docker.io/rancher/mirrored-bci-micro@sha256:a37513dd5ef92f8a05d995a9024bef02f0faedd64b91d464293a67c50fad068c",
                        "name": "docker.io/rancher/mirrored-bci-micro:15.4.14.3"
                    },
                    "name": "rancher-audit-log",
                    "pid": 1,
                    "start_time": "2024-03-30T18:14:23Z"
                },
                "name": "rancher-55966c8d68-f56sc",
                "namespace": "cattle-system",
                "pod_labels": {
                    "app": "rancher",
                    "pod-template-hash": "55966c8d68",
                    "release": "rancher"
                },
                "workload": "rancher",
                "workload_kind": "Deployment"
            },
            "start_time": "2024-03-30T18:14:23.507328761Z",
            "tid": 14287,
            "uid": 0
        }
    },
    "time": "2024-03-30T18:14:23.507328761Z"
}

OBSERVABLE_STIX_BUNDLE_EXAMPLE = {
  "type": "bundle",
  "id": "bundle--3b3d4e1b-4e4d-4e7c-834d-437eab41a5d3",
  "spec_version": "2.1",
  "objects": [
    {
      "type": "process",
      "id": "process--5b4f20e7-76fd-4bc8-bd23-4b9c4b15a17e",
      "pid": 13312,
      "command_line": "/var/lib/rancher/rke2/data/v1.28.8-rke2r1-c4073db9beee/bin/containerd-shim-runc-v2 -namespace k8s.io -id e398dd9deb6d850fcc9327f16b3b1204135ed4ea6a27750160d340ca467fa087 -address /run/k3s/containerd/containerd.sock",
      "cwd": "/run/k3s/containerd/io.containerd.runtime.v2.task/k8s.io/e398dd9deb6d850fcc9327f16b3b1204135ed4ea6a27750160d340ca467fa087",
      "created_time": "2024-03-30T18:13:47.987328Z",
      "image_ref": "file--3c4b7b8c-2e6e-4c8b-bc5e-7c2e4b5a2d8e",
      "extensions": {
        "flags": "procFS auid",
        "parent_exec_id": "azhzLWFnZW50LTAwMjo2MDAwMDAwMDox"
      }
    },
    {
      "type": "process",
      "id": "process--8afdc739-2c3b-4c7e-8890-7742c0c8f8cd",
      "pid": 14287,
      "command_line": "/usr/bin/tail -F /var/log/auditlog/rancher-api-audit.log",
      "cwd": "/",
      "created_time": "2024-03-30T18:14:23.507328Z",
      "image_ref": "file--3c4b7b8c-2e6e-4c8b-bc5e-7c2e4b5a2d3l",
      "parent_ref": "process--5b4f20e7-76fd-4bc8-bd23-4b9c4b15a17e",
      "extensions": {
        "flags": "procFS auid rootcwd",
        "docker": "4b7371b1104abe7634abc1c6f00d04a",
        "container_id": "containerd://4b7371b1104abe7634abc1c6f00d04a9ab79145d6093bec2783933a206afc632",
        "pod_name": "rancher-55966c8d68-f56sc",
        "namespace": "cattle-system"
      }
    },
    {
      "type": "file",
      "id": "file--3c4b7b8c-2e6e-4c8b-bc5e-7c2e4b5a2d8e",
      "name": "containerd-shim-runc-v2"
    },
    {
      "type": "file",
      "id": "file--3c4b7b8c-2e6e-4c8b-bc5e-7c2e4b5a2d3l",
      "name": "/usr/bin/tail"
    },
    {
      "type": "observed-data",
      "id": "observed-data--5f2d4e5b-3d4e-4e7c-834d-437eab41a5d3",
      "created": "2024-03-30T18:14:23.507328Z",
      "modified": "2024-03-30T18:14:23.507328Z",
      "first_observed": "2024-03-30T18:14:23.507328Z",
      "last_observed": "2024-03-30T18:14:23.507328Z",
      "number_observed": 1,
      "object_refs": [
        "process--8afdc739-2c3b-4c7e-8890-7742c0c8f8cd",
        "process--5b4f20e7-76fd-4bc8-bd23-4b9c4b15a17e",
        "file--3c4b7b8c-2e6e-4c8b-bc5e-7c2e4b5a2d8e",
        "file--3c4b7b8c-2e6e-4c8b-bc5e-7c2e4b5a2d3l"
      ],
      "extensions": {
        "node_info": {
          "node_name": "k8s-agent-002"
        }
      }
    }
  ]
}

OBSERVABLE_STIX_BUNDLE_EXAMPLE2 = {
    "type": "bundle",
    "id": "bundle--0749b3fa-5f45-41fc-b132-15f909b0e855",
    "spec_version": "2.1",
    "objects": [
        {
            "type": "file",
            "id": "file--cc48c445-caaa-41ed-a067-9333c7841cc3",
            "name": "tini"
        },
        {
            "type": "file",
            "id": "file--ce73aa8b-a8eb-4fd0-b492-cc90103ec689",
            "name": "rancher"
        },
        {
            "type": "file",
            "id": "file--d6fa1f7f-867f-4023-91ab-c63281be2243",
            "name": "/run/secrets/kubernetes.io/serviceaccount/..2024_05_30_17_59_36.871209644/token"
        },
        {
            "type": "process",
            "id": "process--9690fcaa-f707-44e1-a9ea-2341a4304c8a",
            "pid": None,
            "command_line": "/usr/bin/tini -- rancher --http-listen-port=80 --https-listen-port=443 --audit-log-path=/var/log/auditlog/rancher-api-audit.log --audit-level=1 --audit-log-maxage=1 --audit-log-maxbackup=1 --audit-log-maxsize=100 --no-cacerts --http-listen-port=80 --https-listen-port=443 --add-local=true",
            "cwd": "/var/lib/rancher",
            "created_time": None,
            "image_ref": "file--cc48c445-caaa-41ed-a067-9333c7841cc3",
            "extensions": {
                "flags": "procFS auid"
            }
        },
        {
            "type": "process",
            "id": "process--07176c3f-4514-4114-b764-572bea195d62",
            "pid": None,
            "command_line": "/usr/bin/rancher --http-listen-port=80 --https-listen-port=443 --audit-log-path=/var/log/auditlog/rancher-api-audit.log --audit-level=1 --audit-log-maxage=1 --audit-log-maxbackup=1 --audit-log-maxsize=100 --no-cacerts --http-listen-port=80 --https-listen-port=443 --add-local=true",
            "cwd": "/var/lib/rancher",
            "created_time": None,
            "image_ref": "file--ce73aa8b-a8eb-4fd0-b492-cc90103ec689",
            "parent_ref": "process--9690fcaa-f707-44e1-a9ea-2341a4304c8a",
            "extensions": {
                "flags": "procFS auid",
                "docker": "7bd7197f085f946549f2e4fa0c28489",
                "container_id": "containerd: //7bd7197f085f946549f2e4fa0c28489cf179745364be4c174bd96673061b10bd",
                "pod_name": "rancher-55966c8d68-f56sc",
                "namespace": "cattle-system"
            }
        },
        {
            "type": "observed-data",
            "id": "observed-data--c4bd5cf6-86da-4446-bd76-25da430e9498",
            "created": None,
            "modified": None,
            "first_observed": "2024-03-30T18:14:23.507328Z",
            "last_observed": "2024-03-30T18:14:23.507328Z",
            "number_observed": 1,
            "object_refs": [
                "process--07176c3f-4514-4114-b764-572bea195d62",
                "process--9690fcaa-f707-44e1-a9ea-2341a4304c8a",
                "file--cc48c445-caaa-41ed-a067-9333c7841cc3",
                "file--ce73aa8b-a8eb-4fd0-b492-cc90103ec689",
                "file--d6fa1f7f-867f-4023-91ab-c63281be2243"
            ]
        }
    ]
}