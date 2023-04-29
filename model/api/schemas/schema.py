from voluptuous import Schema, PREVENT_EXTRA

get_list_users = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": [
            {
                "id": int,
                "email": str,
                "first_name": str,
                "last_name": str,
                "avatar": str
            },
            {
                "id": int,
                "email": str,
                "first_name": str,
                "last_name": str,
                "avatar": str
            },
            {
                "id": int,
                "email": str,
                "first_name": str,
                "last_name": str,
                "avatar": str
            },
            {
                "id": int,
                "email": str,
                "first_name": str,
                "last_name": str,
                "avatar": str
            },
            {
                "id": int,
                "email": str,
                "first_name": str,
                "last_name": str,
                "avatar": str
            },
            {
                "id": int,
                "email": str,
                "first_name": str,
                "last_name": str,
                "avatar": str
            }
        ],
        "support": {
            "url": str,
            "text": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)

get_single_user = Schema(
    {
        "data": {
            "id": int,
            "email": str,
            "first_name": str,
            "last_name": str,
            "avatar": str
        },
        "support": {
            "url": str,
            "text": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)

get_single_user_not_found = Schema(
    {

    }
)

get_list_resource = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": [
            {
                "id": int,
                "name": str,
                "year": int,
                "color": str,
                "pantone_value": str
            },
            {
                "id": int,
                "name": str,
                "year": int,
                "color": str,
                "pantone_value": str
            },
            {
                "id": int,
                "name": str,
                "year": int,
                "color": str,
                "pantone_value": str
            },
            {
                "id": int,
                "name": str,
                "year": int,
                "color": str,
                "pantone_value": str
            },
            {
                "id": int,
                "name": str,
                "year": int,
                "color": str,
                "pantone_value": str
            },
            {
                "id": int,
                "name": str,
                "year": int,
                "color": str,
                "pantone_value": str
            }
        ],
        "support": {
            "url": str,
            "text": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)

get_single_resource = Schema(
    {
        "data": {
            "id": int,
            "name": str,
            "year": int,
            "color": str,
            "pantone_value": str
        },
        "support": {
            "url": str,
            "text": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)

get_single_resource_not_found = Schema(
    {

    }
)

create_single_user = Schema(
    {
        "name": str,
        "job": str,
        "id": str,
        "createdAt": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

update_user = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

partially_update_user = Schema(
    {
        "name": str,
        "job": str,
        "updatedAt": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

successful_register_user = Schema(
    {
        "id": int,
        "token": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

unsuccessful_register_user = Schema(
    {
        "error": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

successful_login_user = Schema(
    {
        "token": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

unsuccessful_login_user = Schema(
    {
        "error": str
    },
    extra=PREVENT_EXTRA,
    required=True
)

get_delayed_response = Schema(
    {
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": [
            {
                "id": int,
                "email": str,
                "first_name": str,
                "last_name": str,
                "avatar": str
            },
            {
                "id": int,
                "email": str,
                "first_name": str,
                "last_name": str,
                "avatar": str
            },
            {
                "id": int,
                "email": str,
                "first_name": str,
                "last_name": str,
                "avatar": str
            },
            {
                "id": int,
                "email": str,
                "first_name": str,
                "last_name": str,
                "avatar": str
            },
            {
                "id": int,
                "email": str,
                "first_name": str,
                "last_name": str,
                "avatar": str
            },
            {
                "id": int,
                "email": str,
                "first_name": str,
                "last_name": str,
                "avatar": str
            }
        ],
        "support": {
            "url": str,
            "text": str
        }
    },
    extra=PREVENT_EXTRA,
    required=True
)
