import uuid
import json
from datetime import datetime
from patternmatcher.constants import (
    TETRAGON_PROCESS_KPROBE_LOG_EXAMPLE,
    OBSERVABLE_STIX_BUNDLE_EXAMPLE,
)


def generate_stix_id(type):
    return f"{type}--{uuid.uuid4()}"


def _get_current_time_iso_format():
    return datetime.utcnow().isoformat(timespec="microseconds") + "Z"


def sanitize_bundle(bundle):
    """
    Recursively remove keys with None values from a dictionary.
    """
    if not isinstance(bundle, dict):
        return bundle
    return {k: sanitize_bundle(v) for k, v in bundle.items() if v is not None}


def get_observable_id(bundle):
    return next(
        (obj["id"] for obj in bundle["objects"] if obj["type"] == "observed-data"), None
    )


def transform_process_exec_to_stix(log):
    parent = log.get("parent", {})
    process = log.get("process", {})

    parent_image_name = parent.get("binary", "").split("/")[-1]
    process_image_name = process.get("binary", "").split("/")[-1]

    parent_file_id = generate_stix_id("file") if parent_image_name else None
    process_file_id = generate_stix_id("file") if process_image_name else None

    stix_objects = []

    if parent_image_name:
        stix_objects.append(
            {"type": "file", "id": parent_file_id, "name": parent_image_name}
        )

    if process_image_name:
        stix_objects.append(
            {"type": "file", "id": process_file_id, "name": process_image_name}
        )

    parent_process_object = {
        "type": "process",
        "id": generate_stix_id("process"),
        "pid": parent.get("pid", -1),
        "command_line": f"{parent.get('binary')} {parent.get('arguments')}",
        "cwd": parent.get("cwd"),
        "created_time": parent.get("start_time", _get_current_time_iso_format()),
        "image_ref": parent_file_id,
        "extensions": {
            "flags": parent.get("flags", ""),
            "parent_exec_id": parent.get("parent_exec_id", ""),
        },
    }
    stix_objects.append(parent_process_object)

    process_object = {
        "type": "process",
        "id": generate_stix_id("process"),
        "pid": process.get("pid", -1),
        "command_line": f"{process.get('binary')} {process.get('arguments')}",
        "cwd": process.get("cwd"),
        "created_time": process.get("start_time", _get_current_time_iso_format()),
        "image_ref": process_file_id,
        "parent_ref": parent_process_object["id"],
        "extensions": {
            "flags": process.get("flags", ""),
            "docker": process.get("docker", ""),
            "container_id": process.get("pod", {}).get("container", {}).get("id", ""),
            "pod_name": process.get("pod", {}).get("name", ""),
            "namespace": process.get("pod", {}).get("namespace", ""),
        },
    }
    stix_objects.append(process_object)

    current_time = log.get("time", _get_current_time_iso_format())
    observed_data_object = {
        "type": "observed-data",
        "id": generate_stix_id("observed-data"),
        "created": current_time,
        "modified": current_time,
        "first_observed": current_time,
        "last_observed": current_time,
        "number_observed": 1,
        "object_refs": [process_object["id"], parent_process_object["id"]],
        "extensions": {"node_info": {"node_name": log.get("node_name")}},
    }
    if parent_file_id:
        observed_data_object["object_refs"].append(parent_file_id)
    if process_file_id:
        observed_data_object["object_refs"].append(process_file_id)

    stix_objects.append(observed_data_object)

    return stix_objects


def transform_process_kprobe_to_stix(log):
    parent = log.get("parent", {})
    process = log.get("process", {})
    file_arg = next(
        (
            arg.get("file_arg", {}).get("path")
            for arg in log.get("args", [])
            if "file_arg" in arg
        ),
        None,
    )

    parent_image_name = parent.get("binary", "").split("/")[-1]
    process_image_name = process.get("binary", "").split("/")[-1]

    parent_file_id = generate_stix_id("file") if parent_image_name else None
    process_file_id = generate_stix_id("file") if process_image_name else None
    file_arg_id = generate_stix_id("file") if file_arg else None

    stix_objects = []

    if parent_image_name:
        stix_objects.append(
            {"type": "file", "id": parent_file_id, "name": parent_image_name}
        )

    if process_image_name:
        stix_objects.append(
            {"type": "file", "id": process_file_id, "name": process_image_name}
        )

    if file_arg:
        stix_objects.append({"type": "file", "id": file_arg_id, "name": file_arg})

    parent_process_object = {
        "type": "process",
        "id": generate_stix_id("process"),
        "pid": parent.get("pid", -1),
        "command_line": f"{parent.get('binary')} {parent.get('arguments')}",
        "cwd": parent.get("cwd"),
        "created_time": parent.get("start_time", _get_current_time_iso_format()),
        "image_ref": parent_file_id,
        "extensions": {"flags": parent.get("flags", "")},
    }
    stix_objects.append(parent_process_object)

    process_object = {
        "type": "process",
        "id": generate_stix_id("process"),
        "pid": process.get("pid", -1),
        "command_line": f"{process.get('binary')} {process.get('arguments')}",
        "cwd": process.get("cwd"),
        "created_time": process.get("start_time", _get_current_time_iso_format()),
        "image_ref": process_file_id,
        "parent_ref": parent_process_object["id"],
        "extensions": {
            "flags": process.get("flags", ""),
            "docker": process.get("docker", ""),
            "container_id": process.get("pod", {}).get("container", {}).get("id", ""),
            "pod_name": process.get("pod", {}).get("name", ""),
            "namespace": process.get("pod", {}).get("namespace", ""),
        },
    }
    stix_objects.append(process_object)

    current_time = log.get("time", _get_current_time_iso_format())
    observed_data_object = {
        "type": "observed-data",
        "id": generate_stix_id("observed-data"),
        "created": current_time,
        "modified": current_time,
        "first_observed": current_time,
        "last_observed": current_time,
        "number_observed": 1,
        "object_refs": [process_object["id"], parent_process_object["id"]],
        "extensions": {"node_info": {"node_name": log.get("node_name")}},
    }

    if parent_file_id:
        observed_data_object["object_refs"].append(parent_file_id)
    if process_file_id:
        observed_data_object["object_refs"].append(process_file_id)
    if file_arg_id:
        observed_data_object["object_refs"].append(file_arg_id)

    stix_objects.append(observed_data_object)

    return stix_objects


def transform_tetragon_to_stix(tetragon_log):
    stix_bundle = {
        "type": "bundle",
        "id": generate_stix_id("bundle"),
        "spec_version": "2.1",
        "objects": [],
    }

    if "process_exec" in tetragon_log:
        stix_objects = transform_process_exec_to_stix(tetragon_log["process_exec"])
        stix_bundle["objects"].extend(stix_objects)
    elif "process_kprobe" in tetragon_log:
        stix_objects = transform_process_kprobe_to_stix(tetragon_log["process_kprobe"])
        stix_bundle["objects"].extend(stix_objects)

    return stix_bundle


if __name__ == "__main__":
    bundle = transform_tetragon_to_stix(TETRAGON_PROCESS_KPROBE_LOG_EXAMPLE)
    print(json.dumps(bundle, indent=2))

    id = get_observable_id(OBSERVABLE_STIX_BUNDLE_EXAMPLE)
    print(id)
