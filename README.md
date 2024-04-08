
# HUAWEI CLOUD Batch Update HTTPS Certificates

This repository contains a Python script to update HTTPS certificates in Live service.

# DISCLAIMER

The developers of this tool are not responsible for data loss neither for unexpected cost increases. You, the user of this tool, are the sole responsible for checking the source code.

# Requirements

- Python: <https://www.python.org/>
- Huawei SDK Python: <https://support.huaweicloud.com/intl/en-us/ssdk-live/live_18_0003.html>

# Guide

1. After installing **Python** and **Huawei SDK**, create a `my_config.py` file and place your credentials(AK/SK). Take `my_config_example.py` as reference.
2. Copy the certificate and the private key into the `cert/` directory and modify the value of `cert_name` and `private_key_name` in the `updateCerts.py` file. **Make sure that the certificate is in PEM format**
3. Create a `domains.txt` file into the root folder and place all the domain that will be updated. You can use `domains.example.txt` as reference.
4. Run the `updateCerts.py` file using `python ./updateCerts.py`

# References

- Huawei Cloud API: <https://console-intl.huaweicloud.com/apiexplorer/#/openapi/Live/debug?api=UpdateDomainHttpsCert>
- HTTPS Certificate Requirements: <https://support.huaweicloud.com/intl/en-us/iLive-live/live_01_0045.html>
