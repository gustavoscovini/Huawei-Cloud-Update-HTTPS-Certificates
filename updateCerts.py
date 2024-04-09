from huaweicloudsdkcore.auth.credentials import BasicCredentials, GlobalCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdklive.v1 import *
from huaweicloudsdklive.v1.region.live_region import LiveRegion

from my_config import config


if __name__ == "__main__":
    certificate_file = 'cert/' + config.cert_filename
    privkey_file = 'cert/' + config.privkey_filename

    # Read the certificate file and storage it in a variable
    with open(certificate_file, 'r', encoding='utf-8') as file:
        certificate_file_read = file.read()

    # Read the private key file and storage it in a variable
    with open(privkey_file, 'r', encoding='utf-8') as file:
        privkey_file_read = file.read()

    # Authenticate API with your AK/SK
    credentials = BasicCredentials(config['ak'], config['sk'])

    client = LiveClient.new_builder().with_credentials(credentials).with_region(
        LiveRegion.value_of("ap-southeast-3")).build()

    # Open the domains.txt file and get all domain to be updated
    with open('domains.txt') as file:
        domains = file.readlines()

    # Make the update for all domains in a loop
    for domain in domains:
        try:
            request = UpdateDomainHttpsCertRequest()
            request.domain = domain.strip()
            request.body = DomainHttpsCertInfo(
                certificate=certificate_file_read,
                certificate_key=privkey_file_read,
                certificate_format="PEM")

            response = client.update_domain_https_cert(request)
            print(response.status_code)

        except exceptions.ClientRequestException as e:
            print(e.status_code)
            print(e.request_id)
            print(e.error_code)
            print(e.error_msg)
