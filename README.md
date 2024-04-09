
# HUAWEI CLOUD Batch Update HTTPS Certificates

This repository contains Python scripts that helps to update HTTPS certificates for the Live service in batch.

# DISCLAIMER

The developers of this tool are not responsible for data loss neither for unexpected cost increases. You, the user of this tool, are the sole responsible for checking the source code.

# Requirements

- Python: <https://www.python.org/>
- pip: <https://pip.pypa.io/en/stable/installation/>
- Huawei SDK Python: <https://support.huaweicloud.com/intl/en-us/ssdk-live/live_18_0003.html>

# Installation of SDK

With Python and pip installed, installing the Huawei SDK is straightforward. Simply execute the following commands to install both the Python SDK core library and the related service libraries:

```python
# Install the core library.
pip install huaweicloudsdkcore
# Install the Live service library.
pip install huaweicloudsdklive
```

Once you've installed the Huawei SDK, to start using it for the **Live** service, simply import the necessary modules into your Python script:

```python
from huaweicloudsdkcore.auth.credentials import BasicCredentials, GlobalCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdklive.v1 import *
from huaweicloudsdklive.v1.region.live_region import LiveRegion
```

# Configuration

1. Create a `my_config.py` file and place your credentials(AK/SK). Take `my_config_example.py` as reference.
2. Copy the certificate and the private key into the `cert/` directory and modify the value of `cert_name` and `private_key_name` in the `updateCerts.py` file. **Make sure that the certificate is in PEM format**
3. Create a `domains.txt` file into the root folder and place all the domain that will be updated. You can use `domains.example.txt` as reference.
4. Run the `updateCerts.py` file using `python ./updateCerts.py`

# References

- Huawei Cloud API: <https://console-intl.huaweicloud.com/apiexplorer/#/openapi/Live/debug?api=UpdateDomainHttpsCert>
- HTTPS Certificate Requirements: <https://support.huaweicloud.com/intl/en-us/iLive-live/live_01_0045.html>
