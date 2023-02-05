import platform
import uuid

def get_system_info():
    sys_name = platform.system()
    node_name = platform.node()
    release = platform.release()
    version = platform.version()
    machine = platform.machine()
    processor = platform.processor()
    uid = uuid.uuid1()

    return f"System Name: {sys_name}\n" \
           f"Node Name:   {node_name}\n" \
           f"Release:     {release}\n" \
           f"Version:     {version}\n" \
           f"Machine:     {machine}\n" \
           f"Processor:   {processor}\n" \
           f"UUID:        {uid}\n"

