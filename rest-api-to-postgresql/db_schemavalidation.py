
launch_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "launch_id": {
                "type": "string"
            },
        "launch_name": {
                "type": "string"
                },
        "launch_status": {
                "type": "string"
                },
        "launch_status_description": {
                "type": "string",
                },
        "launch_window_start": {
                "type": "string"
                },
        "launch_window_end": {
                "type": "string"
                },
        "launch_provider_name": {
                "type": "string"
                }
    },
    "required": [
        "launch_id",
        "launch_name",
        "launch_provider_name",
        "launch_status",
        "launch_status_description",
        "launch_window_start",
        "launch_window_end"

    ]
}

mission_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "mission_id": {
                "type": "number"
            },
        "launch_id": {
                "type": "string"
                },
        "mission_name": {
                "type": "string"
                },
        "mission_description": {
                "type": "string",
                },
        "mission_type": {
                "type": "string"
                }
    },
    "required": [
        "mission_id",
        "launch_id",
        "mission_name",
        "mission_description",
        "mission_type",
    ]
}

rocket_schema = {

     "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "rocket_id": {
                "type": "number"
            },
        "launch_id": {
                "type": "string"
                },
        "rocket_fullname": {
                "type": "string"
                },
        "rocket_family": {
                "type": "string",
                },
        "rocket_variant": {
                "type": "string"
                }
    },
    "required": [
        "rocket_id",
        "launch_id",
        "rocket_fullname",
        "rocket_family",
        "rocket_variant",
    ]
}

