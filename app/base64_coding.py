import json
import base64


def dict_to_base64(message):
    """
        Convert dict to base64 encoding.
        >>> dict_to_base64({'q': 13})
        'eyJxIjogMTN9'
    """
    message = json.dumps(message)
    message_bytes = message.encode('utf-8')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('utf-8')
    return base64_message


def base64_to_dict(base64_message):
    """
        Convert base64 encoding to dict.
        >>> base64_to_dict('eyJxIjogMTN9')
        {'q': 13}
    """
    base64_bytes = base64_message.encode('utf-8')
    message_bytes = base64.b64decode(base64_bytes)
    message = message_bytes.decode('utf-8')
    message = json.loads(message)
    return message