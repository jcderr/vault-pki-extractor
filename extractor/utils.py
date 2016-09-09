class VaultPKIData(object):
    certificate = None
    issuing_ca = None
    private_key = None
    private_key_type = None
    serial_number = None

    def __init__(self, obj):
        self.certificate = obj['certificate']
        self.issuing_ca = obj['issuing_ca']
        self.private_key = obj['private_key']
        self.private_key_type = obj['private_key_type']
        self.serial_number = obj['serial_number']

class VaultPKIObject(object):
    request_id = None
    lease_id = None
    renewable = False
    lease_duration = 0
    data = None
    wrap_info = None
    warnings = None
    auth = None
    obj = None

    def __init__(self, obj):
        self.request_id = obj['request_id']
        self.lease_id = obj['lease_id']
        self.renewable = obj['renewable']
        self.lease_duration = obj['lease_duration']
        self.wrap_info = obj['wrap_info']
        self.warnings = obj['warnings']
        self.auth = obj['auth']
        self.data = VaultPKIData(obj['data'])
        self.obj = obj

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '''
Request ID: {}
Lease ID: {}
Renewable: {}
Lease Duration: {}
Wrap: {}
Warnings: {}
Auth: {}
Key Type: {}
Serial Number: {}
---------------
Certificate:
{}
CA:
{}
Private Key:
{}
        '''.format(
            self.request_id, self.lease_id, self.renewable, self.lease_duration,
            self.wrap_info, self.warnings, self.auth,
            self.data.private_key_type, self.data.serial_number,
            self.data.certificate, self.data.issuing_ca, self.data.private_key
        )
