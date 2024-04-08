from huaweicloudsdkcore.auth.credentials import BasicCredentials, GlobalCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdklive.v1 import *
from huaweicloudsdklive.v1.region.live_region import LiveRegion

from my_config import config

cert_name = ""
private_key_name = ""

if __name__ == "__main__":
    certificate_file = 'cert/' + cert_name
    privkey_file = 'cert/' + private_key_name
    
    with open(certificate_file, 'r', encoding='utf-8') as file:
        certificate_file_read = file.read()

    with open(privkey_file, 'r', encoding='utf-8') as file:
        privkey_file_read = file.read()

    credentials = BasicCredentials(config['ak'], config['sk'])

    client = LiveClient.new_builder().with_credentials(credentials).with_region(
        LiveRegion.value_of("ap-southeast-3")).build()

    with open('domains.txt') as f:
        domains = f.readlines()
    
    for domain in domains:
        try:        
            request = UpdateDomainHttpsCertRequest()
            request.domain = domain.strip()
            print(domain)
            request.body = DomainHttpsCertInfo(
                certificate=certificate_file_read,
                certificate_key=privkey_file_read,
                certificate_format="PEM"
                                            )
            response = client.update_domain_https_cert(request)
            print(response.status_code)
        except exceptions.ClientRequestException as e:
            print(e.status_code)
            print(e.request_id)
            print(e.error_code)
            print(e.error_msg)
