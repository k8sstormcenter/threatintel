---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.2
  kernelspec:
    display_name: .venv
    language: python
    name: python3
---

```python
import os
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
print("set") if GOOGLE_API_KEY else print("unset")
```

```python
from llama_index.llms.gemini import Gemini

resp = Gemini().complete("""Create a STIX indicator to match following observable: 
{
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
""")
print(resp)
```

