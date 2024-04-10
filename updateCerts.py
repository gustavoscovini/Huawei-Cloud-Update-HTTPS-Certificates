import os

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdklive.v1 import (DomainHttpsCertInfo, LiveClient,
                                   UpdateDomainHttpsCertRequest)
from huaweicloudsdklive.v1.region.live_region import LiveRegion

from my_config import config


if __name__ == "__main__":
    certificate_file = os.path.join('cert', config['cert_filename'])
    privkey_file = os.path.join('cert', config['privkey_filename'])

    with open(certificate_file, 'r', encoding='utf-8') as file:
        certificate_file_read = file.read()

    with open(privkey_file, 'r', encoding='utf-8') as file:
        privkey_file_read = file.read()

    credentials = BasicCredentials(config['ak'], config['sk'])
    region = LiveRegion.value_of("ap-southeast-3")
    client = LiveClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(region).build()

    domains = []
    with open('domains.txt') as file:
        domains = file.readlines()

    domains = [d.strip() for d in domains]

    n_domains = len(domains)
    for i_domain, domain in enumerate(domains):
        print(f'[{i_domain+1}/{n_domains}] {domain} : ', end='')

        try:
            request = UpdateDomainHttpsCertRequest()
            request.domain = domain
            request.body = DomainHttpsCertInfo(
                certificate=certificate_file_read,
                certificate_key=privkey_file_read,
                certificate_format="PEM")

            response = client.update_domain_https_cert(request)
            if response.status_code == 200:
                print('done')
            else:
                print('failed, status code =', response.status_code)

        except exceptions.ClientRequestException as e:
            print('failed, status code =', e.status_code)
            print(' - request ID =', e.request_id)
            print(' - error code =', e.error_code)
            print(' - error msg = ', e.error_msg)
