# devices.py

from logger import log_event

log_event("device_event","Device connected", source="devices")

# Global device list
devices = []

def add_device(device_info):
    """
    Add a new device to the list.
    device_info: dict with keys like 'id', 'nickname', 'device_type', 'capabilities', 'connected'
    """
    # Check if device already exists by ID
    if any(d['id'] == device_info['id'] for d in devices):
        print(f"Device with ID {device_info['id']} already exists.")
        return False
    devices.append(device_info)
    print(f"Added device: {device_info['nickname']} ({device_info['id']})")
    return True

def get_devices():
    """Return the list of all devices."""
    return devices

def get_device_by_id(device_id):
    """Return a device dict by its ID or None if not found."""
    for device in devices:
        if device['id'] == device_id:
            return device
    return None

def update_device_status(device_id, connected):
    """Update the connected status of a device."""
    device = get_device_by_id(device_id)
    if device:
        device['connected'] = connected
        print(f"Updated device {device['nickname']} status to {'connected' if connected else 'disconnected'}.")
        return True
    else:
        print(f"No device found with ID {device_id}.")
        return False

def activate_device_capability(device_id, capability_name):
    """
    Stub function to 'activate' a device capability.
    In real app, this would send commands via HTTP API to device.
    """
    device = get_device_by_id(device_id)
    if not device:
        print(f"No device found with ID {device_id}. Cannot activate capability.")
        return False
    if capability_name not in device.get('capabilities', []):
        print(f"Device {device['nickname']} does not support capability {capability_name}.")
        return False
    # For now, just print activation stub
    print(f"Activating capability '{capability_name}' on device '{device['nickname']}'...")
    # TODO: Replace with real HTTP API calls
    return True

def display_devices():
    """Print all registered devices and their status."""
    if not devices:
        print("No devices registered yet.")
        return
    for device in devices:
        print(f"ID: {device['id']}, Name: {device['nickname']}, Type: {device['device_type']}, Connected: {device.get('connected', False)}")
        print(f"Capabilities: {device.get('capabilities', [])}")
        print("-" * 40)



# Add a couple of devices
add_device({
    'id': 'device-001',
    'nickname': 'Living Room Lamp',
    'device_type': 'lamp',
    'capabilities': ['light_on_off', 'brightness_control'],
    'connected': True
})

add_device({
    'id': 'device-002',
    'nickname': 'Bedroom Fan',
    'device_type': 'fan',
    'capabilities': ['fan_on_off', 'speed_control'],
    'connected': False
})

# Display all devices
display_devices()

# Activate capability
activate_device_capability('device-001', 'light_on_off')
activate_device_capability('device-002', 'speed_control')

# Update status
update_device_status('device-002', True)

# Display again
display_devices()