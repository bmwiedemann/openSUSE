import base64
import json
import os
import struct
import unittest
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import (
    Encoding, PublicFormat
)

import http_ece as ece
from http_ece import ECEException


TEST_VECTORS = os.path.join(os.sep, "..", "encrypt_data.json")[1:]


def logmsg(arg):
    """
    print(arg)
    """
    return


def logbuf(msg, buf):
    """used for debugging test code."""
    if buf is None:
        buf = b''
    logmsg(msg + ': [' + str(len(buf)) + ']')
    for i in list(range(0, len(buf), 48)):
        logmsg('    ' + repr(buf[i:i+48]))
    return


def b64e(arg):
    if arg is None:
        return None
    return base64.urlsafe_b64encode(arg).decode()


def b64d(arg):
    if arg is None:
        return None
    return base64.urlsafe_b64decode(str(arg) + '===='[:len(arg) % 4:])


def make_key():
    return ec.generate_private_key(ec.SECP256R1(), default_backend())


class TestEce(unittest.TestCase):

    def setUp(self):
        self.private_key = make_key()
        self.dh = self.private_key.public_key().public_bytes(
            Encoding.X962,
            PublicFormat.UncompressedPoint
        )
        self.m_key = os.urandom(16)
        self.m_salt = os.urandom(16)

    def test_derive_key_invalid_mode(self):
        with self.assertRaises(ECEException) as ex:
            ece.derive_key('invalid',
                           version='aes128gcm',
                           salt=self.m_salt,
                           key=self.m_key,
                           private_key=self.private_key,
                           dh=None,
                           auth_secret=None,
                           keyid="valid",
                           )
        self.assertEqual(ex.exception.message, "unknown 'mode' specified: invalid")

    def test_derive_key_invalid_salt(self):
        with self.assertRaises(ECEException) as ex:
            ece.derive_key('encrypt',
                           version='aes128gcm',
                           salt=None,
                           key=self.m_key,
                           private_key=self.private_key,
                           dh=None,
                           auth_secret=None,
                           keyid="valid",
                           )
        self.assertEqual(ex.exception.message, "'salt' must be a 16 octet value")

    def test_derive_key_invalid_version(self):
        with self.assertRaises(ECEException) as ex:
            ece.derive_key('encrypt',
                           version='invalid',
                           salt=self.m_salt,
                           key=None,
                           private_key=self.private_key,
                           dh=None,
                           auth_secret=None,
                           keyid="valid",
                           )
        self.assertEqual(ex.exception.message, "Invalid version")

    def test_derive_key_no_private_key(self):
        with self.assertRaises(ECEException) as ex:
            ece.derive_key('encrypt',
                           version='aes128gcm',
                           salt=self.m_salt,
                           key=None,
                           private_key=None,
                           dh=self.dh,
                           auth_secret=None,
                           keyid="valid",
                           )
        self.assertEqual(ex.exception.message, "DH requires a private_key")

    def test_derive_key_no_secret(self):
        with self.assertRaises(ECEException) as ex:
            ece.derive_key('encrypt',
                           version='aes128gcm',
                           salt=self.m_salt,
                           key=None,
                           private_key=None,
                           dh=None,
                           auth_secret=None,
                           keyid="valid",
                           )
        self.assertEqual(ex.exception.message, "unable to determine the secret")

    def test_iv_bad_counter(self):
        with self.assertRaises(ECEException) as ex:
            ece.iv(os.urandom(8), pow(2, 64)+1)
        self.assertEqual(ex.exception.message, "Counter too big")


class TestEceChecking(unittest.TestCase):

    def setUp(self):
        self.m_key = os.urandom(16)
        self.m_input = os.urandom(5)
        # This header is specific to the padding tests, but can be used
        # elsewhere
        self.m_header = b'\xaa\xd2\x05}3S\xb7\xff7\xbd\xe4*\xe1\xd5\x0f\xda'
        self.m_header += struct.pack('!L', 32) + b'\0'

    def test_encrypt_small_rs(self):
        with self.assertRaises(ECEException) as ex:
            ece.encrypt(
                self.m_input,
                version='aes128gcm',
                key=self.m_key,
                rs=1,
            )
        self.assertEqual(ex.exception.message, "Record size too small")

    def test_decrypt_small_rs(self):
        header = os.urandom(16) + struct.pack('!L', 2) + b'\0'
        with self.assertRaises(ECEException) as ex:
            ece.decrypt(
                header + self.m_input,
                version='aes128gcm',
                key=self.m_key,
                rs=1,
            )
        self.assertEqual(ex.exception.message, "Record size too small")

    def test_encrypt_bad_version(self):
        with self.assertRaises(ECEException) as ex:
            ece.encrypt(
                self.m_input,
                version='bogus',
                key=self.m_key,
            )
        self.assertEqual(ex.exception.message, "Invalid version")

    def test_decrypt_bad_version(self):
        with self.assertRaises(ECEException) as ex:
            ece.decrypt(
                self.m_input,
                version='bogus',
                key=self.m_key,
            )
        self.assertEqual(ex.exception.message, "Invalid version")

    def test_decrypt_bad_header(self):
        with self.assertRaises(ECEException) as ex:
            ece.decrypt(
                os.urandom(4),
                version='aes128gcm',
                key=self.m_key,
            )
        self.assertEqual(ex.exception.message, "Could not parse the content header")

    def test_encrypt_long_keyid(self):
        with self.assertRaises(ECEException) as ex:
            ece.encrypt(
                self.m_input,
                version='aes128gcm',
                key=self.m_key,
                keyid=b64e(os.urandom(192)),  # 256 bytes
            )
        self.assertEqual(ex.exception.message, "keyid is too long")

    def test_overlong_padding(self):
        with self.assertRaises(ECEException) as ex:
            ece.decrypt(
                self.m_header + b'\xbb\xc7\xb9ev\x0b\xf0f+\x93\xf4'
                                b'\xe5\xd6\x94\xb7e\xf0\xcd\x15\x9b(\x01\xa5',
                version='aes128gcm',
                key=b'd\xc7\x0ed\xa7%U\x14Q\xf2\x08\xdf\xba\xa0\xb9r',
                keyid=b64e(os.urandom(192)),  # 256 bytes
            )
        self.assertEqual(ex.exception.message, "all zero record plaintext")

    def test_bad_early_delimiter(self):
        with self.assertRaises(ECEException) as ex:
            ece.decrypt(
                self.m_header + b'\xb9\xc7\xb9ev\x0b\xf0\x9eB\xb1\x08C8u'
                                b'\xa3\x06\xc9x\x06\n\xfc|}\xe9R\x85\x91'
                                b'\x8bX\x02`\xf3' +
                b'E8z(\xe5%f/H\xc1\xc32\x04\xb1\x95\xb5N\x9ep\xd4\x0e<\xf3'
                b'\xef\x0cg\x1b\xe0\x14I~\xdc',
                version='aes128gcm',
                key=b'd\xc7\x0ed\xa7%U\x14Q\xf2\x08\xdf\xba\xa0\xb9r',
                keyid=b64e(os.urandom(192)),  # 256 bytes
            )
        self.assertEqual(ex.exception.message, "record delimiter != 1")

    def test_bad_final_delimiter(self):
        with self.assertRaises(ECEException) as ex:
            ece.decrypt(
                self.m_header + b'\xba\xc7\xb9ev\x0b\xf0\x9eB\xb1\x08Ji'
                                b'\xe4P\x1b\x8dI\xdb\xc6y#MG\xc2W\x16',
                version='aes128gcm',
                key=b'd\xc7\x0ed\xa7%U\x14Q\xf2\x08\xdf\xba\xa0\xb9r',
                keyid=b64e(os.urandom(192)),  # 256 bytes
            )
        self.assertEqual(ex.exception.message, "last record delimiter != 2")

    def test_damage(self):
        with self.assertRaises(ECEException) as ex:
            ece.decrypt(
                self.m_header + b'\xbb\xc6\xb1\x1dF:~\x0f\x07+\xbe\xaaD'
                                b'\xe0\xd6.K\xe5\xf9]%\xe3\x86q\xe0}',
                version='aes128gcm',
                key=b'd\xc7\x0ed\xa7%U\x14Q\xf2\x08\xdf\xba\xa0\xb9r',
                keyid=b64e(os.urandom(192)),  # 256 bytes
            )
        self.assertEqual(ex.exception.message, "Decryption error: InvalidTag()")


class TestEceIntegration(unittest.TestCase):

    def setUp(self):
        ece.keys = {}
        ece.labels = {}

    def tearDown(self):
        ece.keys = {}
        ece.labels = {}

    def _rsoverhead(self, version):
        if version == 'aesgcm128':
            return 1
        if version == 'aesgcm':
            return 2
        return 18

    def _generate_input(self, minLen=0):
        length = struct.unpack('!B', os.urandom(1))[0] + minLen
        return os.urandom(length)

    def encrypt_decrypt(self, input, encrypt_params, decrypt_params=None,
                        version=None):
        """Run and encrypt/decrypt cycle on some test data

        :param input: data for input
        :type length: bytearray
        :param encrypt_params: Dictionary of encryption parameters
        :type encrypt_params: dict
        :param decrypt_params: Optional dictionary of decryption parameters
        :type decrypt_params: dict
        :param version: Content-Type of the body, formulating encryption
        :type enumerate("aes128gcm", "aesgcm", "aesgcm128"):
        """
        if decrypt_params is None:
            decrypt_params = encrypt_params
        logbuf("Input", input)
        if "key" in encrypt_params:
            logbuf("Key", encrypt_params["key"])
        if version != "aes128gcm":
            salt = os.urandom(16)
            decrypt_rs_default = 4096
        else:
            salt = None
            decrypt_rs_default = None
        logbuf("Salt", salt)
        if "auth_secret" in encrypt_params:
            logbuf("Auth Secret", encrypt_params["auth_secret"])
        encrypted = ece.encrypt(input,
                                salt=salt,
                                key=encrypt_params.get("key"),
                                keyid=encrypt_params.get("keyid"),
                                dh=encrypt_params.get("dh"),
                                private_key=encrypt_params.get("private_key"),
                                auth_secret=encrypt_params.get("auth_secret"),
                                rs=encrypt_params.get("rs", 4096),
                                version=version)
        logbuf("Encrypted", encrypted)
        decrypted = ece.decrypt(encrypted,
                                salt=salt,
                                key=decrypt_params.get("key"),
                                keyid=decrypt_params.get("keyid"),
                                dh=decrypt_params.get("dh"),
                                private_key=decrypt_params.get("private_key"),
                                auth_secret=decrypt_params.get("auth_secret"),
                                rs=decrypt_params.get("rs",
                                                      decrypt_rs_default),
                                version=version)
        logbuf("Decrypted", decrypted)
        self.assertEqual(input, decrypted)

    def use_explicit_key(self, version=None):
        params = {
            "key": os.urandom(16),
        }
        self.encrypt_decrypt(self._generate_input(), params, version=version)

    def auth_secret(self, version):
        params = {
            "key": os.urandom(16),
            "auth_secret": os.urandom(16)
        }
        self.encrypt_decrypt(self._generate_input(), params, version=version)

    def exactly_one_record(self, version=None):
        input = self._generate_input(1)
        params = {
            "key": os.urandom(16),
            "rs": len(input) + self._rsoverhead(version)
        }
        self.encrypt_decrypt(input, params, version=version)

    def detect_truncation(self, version):
        if version == "aes128gcm":
            return

        input = self._generate_input(2)
        key = os.urandom(16)
        salt = os.urandom(16)

        rs = len(input) + self._rsoverhead(version) - 1
        encrypted = ece.encrypt(input, salt=salt, key=key, rs=rs,
                                version=version)
        if version == 'aes128gcm':
            chunk = encrypted[0:21+rs]
        else:
            chunk = encrypted[0:rs+16]
        with self.assertRaises(ECEException) as ex:
            ece.decrypt(chunk, salt=salt, key=key, rs=rs, version=version)
        self.assertEqual(ex.exception.message, "Message truncated")

    def use_dh(self, version):
        def pubbytes(k):
            return k.public_key().public_bytes(
                Encoding.X962,
                PublicFormat.UncompressedPoint
            )

        def privbytes(k):
            d = k.private_numbers().private_value
            b = b''
            for i in range(0,
                           k.private_numbers().public_numbers.curve.key_size,
                           32):
                b = struct.pack("!L", (d >> i) & 0xffffffff) + b
            return b

        def logec(s, k):
            logbuf(s + " private", privbytes(k))
            logbuf(s + " public", pubbytes(k))

        def is_uncompressed(k):
            b1 = pubbytes(k)[0:1]
            assert struct.unpack("B", b1)[0] == 4, "is an uncompressed point"

        # the static key is used by the receiver
        static_key = make_key()
        is_uncompressed(static_key)

        logec("receiver", static_key)

        # the ephemeral key is used by the sender
        ephemeral_key = make_key()
        is_uncompressed(ephemeral_key)

        logec("sender", ephemeral_key)

        auth_secret = os.urandom(16)

        if version != "aes128gcm":
            decrypt_dh = pubbytes(ephemeral_key)
        else:
            decrypt_dh = None

        encrypt_params = {
            "private_key": ephemeral_key,
            "dh": static_key.public_key(),
            "auth_secret": auth_secret,
        }
        decrypt_params = {
            "private_key": static_key,
            "dh": decrypt_dh,
            "auth_secret": auth_secret,
        }

        self.encrypt_decrypt(self._generate_input(), encrypt_params,
                             decrypt_params, version)

    def test_types(self):
        for ver in ["aes128gcm", "aesgcm", "aesgcm128"]:
            for f in (
                    self.use_dh,
                    self.use_explicit_key,
                    self.auth_secret,
                    self.exactly_one_record,
                    self.detect_truncation,
                    ):
                ece.keys = {}
                ece.labels = {}
                f(version=ver)


class TestNode(unittest.TestCase):
    """Testing using data from the node.js version.
    """
    def setUp(self):
        if not os.path.exists(TEST_VECTORS):
            self.skipTest("No %s file found" % TEST_VECTORS)
        f = open(TEST_VECTORS, 'r')
        self.legacy_data = json.loads(f.read())
        f.close()

    def _run(self, mode):
        if mode == 'encrypt':
            func = ece.encrypt
            local = 'sender'
            inp = 'input'
            outp = 'encrypted'
        else:
            func = ece.decrypt
            local = 'receiver'
            inp = 'encrypted'
            outp = 'input'

        for data in self.legacy_data:
            logmsg('%s: %s' % (mode, data['test']))
            p = data['params'][mode]

            if 'pad' in p and mode == 'encrypt':
                # This library doesn't pad in exactly the same way.
                continue

            if 'keys' in data:
                key = None
                decode_pub = ec.EllipticCurvePublicNumbers.from_encoded_point
                pubnum = decode_pub(ec.SECP256R1(),
                                    b64d(data['keys'][local]['public']))
                d = 0
                dbin = b64d(data['keys'][local]['private'])
                for i in range(0, len(dbin), 4):
                    d = (d << 32) + struct.unpack('!L', dbin[i:i + 4])[0]
                privnum = ec.EllipticCurvePrivateNumbers(d, pubnum)
                private_key = privnum.private_key(default_backend())
            else:
                key = b64d(p['key'])
                private_key = None

            if 'authSecret' in p:
                auth_secret = b64d(p['authSecret'])
            else:
                auth_secret = None
            if 'dh' in p:
                dh = b64d(p['dh'])
            else:
                dh = None

            result = func(
                b64d(data[inp]),
                salt=b64d(p['salt']),
                key=key,
                dh=dh,
                auth_secret=auth_secret,
                keyid=p.get('keyid'),
                private_key=private_key,
                rs=p.get('rs', 4096),
                version=p['version'],
            )
            self.assertEqual(b64d(data[outp]), result)

    def test_decrypt(self):
        self._run('decrypt')

    def test_encrypt(self):
        self._run('encrypt')
