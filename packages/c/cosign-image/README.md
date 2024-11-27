# openSUSE Tumbleweed cosign
![Redistributable](https://img.shields.io/badge/Redistributable-Yes-green)

## Description
Cosign aims to make signatures management easy.

Cosign supports the following functionality:

* "Keyless signing" with the Sigstore public good Fulcio certificate authority and Rekor transparency log (default)
* Hardware and KMS signing
* Signing with a Cosign-generated encrypted private/public keypair
* Container signing, verification and storage in an OCI registry.
* Bring-your-own public key infrastructure (PKI)


## Usage

### Verify a container image

To verify the image, specify a certificate subject
and a certificate issuer using the `--certificate-identity` and
`--certificate-oidc-issuer` flags:

```ShellSession
$ podman run registry.opensuse.org/opensuse/cosign:2.4 \
    verify $IMAGE \
    --certificate-identity=$IDENTITY \
    --certificate-oidc-issuer=$OIDC_ISSUER
```

You can also provide a regex for the certificate identity and issuer flags,
`--certificate-identity-regexp` and `--certificate-oidc-issuer-regexp`. For more information, see
[Keyless verification using OpenID Connect](https://docs.sigstore.dev/cosign/verifying/verify/#keyless-verification-using-openid-connect).

### Verify a container image against a public key

The `verify` command returns `0` if *at least one* `cosign`-formatted signature for
the image is found matching the public key. See the detailed usage below for
information and caveats on other signature formats.

Valid payload is printed to stdout, in JSON format. Note that the
signed payload includes the digest of the container image, which indicated that these "detached" signatures apply to the correct image.

```ShellSession
$ podman run registry.opensuse.org/opensuse/cosign:2.4 verify --key cosign.pub $IMAGE_URI:1h
The following checks were performed on these signatures:
  - The cosign claims were validated
  - The signatures were verified against the specified public key
{"Critical":{"Identity":{"docker-reference":""},"Image":{"Docker-manifest-digest":"sha256:87ef60f558bad79beea6425a3b28989f01dd417164150ab3baab98dcbf04def8"},"Type":"cosign container image signature"},"Optional":null}
```

For more use cases and information, refer to the
[sigstore cosign Quickstart](https://docs.sigstore.dev/quickstart/quickstart-cosign/).

## Licensing

`SPDX-License-Identifier: Apache-2.0`

This documentation and the build recipe are licensed as Apache-2.0.
The container itself contains various software components under various open source licenses listed in the associated
Software Bill of Materials (SBOM).

This image is based on [openSUSE Tumbleweed](https://get.opensuse.org/tumbleweed/).
