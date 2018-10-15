""" import sys
import os
import ssl
from pprint import pprint as pp


def main():
    cert_file_name = os.path.join(os.path.dirname(__file__), "my_cert.crt")
    try:
        cert_dict = ssl._ssl._test_decode_cert(cert_file_name)
        pp(cert_dict)

    except Exception as e:
        print("Error decoding certificate: {:}".format(e))


if __name__ == "__main__":
    print("Python {:s} on {:s}\n".format(sys.version, sys.platform))
    main() """

def isCertValid(cert):
    validCert = r'''-----BEGIN CERTIFICATE-----
MIICQDCCAakCAgPoMA0GCSqGSIb3DQEBBQUAMGgxCzAJBgNVBAYTAlVTMQswCQYD
VQQIDAJDQTEWMBQGA1UECgwNc29tZSBvcmcgbmFtZTEZMBcGA1UECwwQbXkgb3Jn
IHVuaXQgbmFtZTEZMBcGA1UEAwwQc29tZSBjb21tb24gbmFtZTAeFw0xODEwMTQy
MjA3MzhaFw0yODEwMTEyMjA3MzhaMGgxCzAJBgNVBAYTAlVTMQswCQYDVQQIDAJD
QTEWMBQGA1UECgwNc29tZSBvcmcgbmFtZTEZMBcGA1UECwwQbXkgb3JnIHVuaXQg
bmFtZTEZMBcGA1UEAwwQc29tZSBjb21tb24gbmFtZTCBnzANBgkqhkiG9w0BAQEF
AAOBjQAwgYkCgYEApeK6iztZlQWL9bBwxuMwINM1Y2dANSSF8LsL3bedJPTQ8Wik
k26ue26Kfu5dKTmHEiulaJwrfvwxoW4Rnz9yglFL+kWxymo3H9d6dCIbgGuNKYXG
G/IqXiYpG3bkSwikaQwIJCRljzSF/9f4p/Kt8csQNElEI10jcNZOXh/B2UUCAwEA
ATANBgkqhkiG9w0BAQUFAAOBgQAsHDfHb1+pFsu6NCPKDcUCTRstkoqju92KLlJZ
WW8YPWBPYXwNA/5uRCyYCLLvfyxCJpjLa3zg0/AiXfGtkgjKubvPeoR9hoRaN/Od
HEgKa5RSnyDuYb3jkqe29cZx+4c48arGuBM+OsX4IqFTq0O+poRy9KmFGMAynraW
KxSHgg==
-----END CERTIFICATE-----
    '''
    if cert in validCert:
        return True
    else:
        return False