#
# spec file for package ovmf-KEKUpdate
#
# Copyright (c) 2026 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#
# needssslcertforbuild


Name:           ovmf-KEKUpdate
Version:        1.6.5
Release:        0
Summary:        SUSE signed Microsoft KEK package for OVMF
License:        BSD-2-Clause-Patent
Group:          System/Boot
URL:            https://github.com/microsoft/secureboot_objects/releases
# x64, sha256:624c8629f4aab631064fde7d098ad60204288267b6e6edaab50a852ba7dd382b
Source0:        https://github.com/microsoft/secureboot_objects/releases/download/v%{version}/edk2-x64-secureboot-binaries.tar.gz
# aarch64, sha256:bf5a51e79815698013b9a062d489235cd042d0b1f9370a0a7c27a05367c95ed3
Source1:        https://github.com/microsoft/secureboot_objects/releases/download/v%{version}/edk2-aarch64-secureboot-binaries.tar.gz
BuildRequires:  efitools
BuildRequires:  pesign-obs-integration
ExclusiveArch:  x86_64 aarch64

%description
SUSE signed Microsoft KEK package for OVMF. The KEKUpdate_SUSE_PK.bin file
can be used to update kek in SUSE ovmf by efi-updatevar tool.

%prep
%ifarch x86_64
tar -xf %{SOURCE0}
%endif
%ifarch aarch64
tar -xf %{SOURCE1}
%endif

%build
# Microsoft uses a fixed magic timestamp. The reason is in this issue:
# https://github.com/microsoft/secureboot_objects/issues/157
export TIMESTAMP="2010-03-06 19:17:21"

# Input file: The KEK.bin from edk2-$arch-secureboot-binaries.tar.gz is
#             a ESL (EFI Signature List)
# Output file: The KEKUpdate_openSUSE_PK.bin is a signable binary format
#              which is the source file for signing a ESL:
# [ Variable Name ][   Vendor GUID  ][   Attributes  ][    EFI_TIME    ][ Payload (ESL) ]
# |<-- N bytes -->||<-- 16 bytes -->||<-- 4 bytes -->||<-- 16 bytes -->||<-- N bytes -->|
#
# We also set EFI_VARIABLE_APPEND_WRITE attribute for writing by efi-updatevar.
#
# The KEKUpdate_openSUSE_PK.bin file will directly overwriten by pesign-obs-integration.
# The pesign-obs-integration attach timestamp and signature (PKCS#7 SignedData)
# to a EFI_VARIABLE_AUTHENTICATION_2 as the header of the signed auth file.
#
# The output signed auth file KEKUpdate_SUSE_PK.bin will be renamed manually to
# KEKUpdate_<SUSE|openSUSE>_PK<number>.bin for uploading to secureboot_objects project
sign-efi-sig-list -t "$TIMESTAMP" -a -o KEK MicrosoftAndThirdParty/Firmware/KEK.bin KEKUpdate_SUSE_PK.bin
# TODO: auto generate json file?

# copy signkey, will be included in rpm for user reference
cert=%{_sourcedir}/_projectcert.crt
openssl x509 -in $cert -outform DER -out KEKUpdate_signkey.der

%install
export BRP_PESIGN_FILES='%{_sysconfdir}/uefi/certs/KEKUpdate_SUSE_PK.bin'
install -d %{buildroot}/%{_sysconfdir}/uefi/certs/
install -m 644 KEKUpdate_SUSE_PK.bin %{buildroot}/%{_sysconfdir}/uefi/certs/KEKUpdate_SUSE_PK.bin

fpr=$(openssl x509 -sha1 -fingerprint -inform DER -noout -in KEKUpdate_signkey.der | cut -c 18- | cut -d ":" -f 1,2,3,4 | sed 's/://g')
install -m 644 KEKUpdate_signkey.der %{buildroot}/%{_sysconfdir}/uefi/certs/${fpr}-KEKUpdate_signkey.crt

%files
%license MicrosoftAndThirdParty/Firmware/README.md
%defattr(-,root,root)
%dir %{_sysconfdir}/uefi/
%dir %{_sysconfdir}/uefi/certs/
%{_sysconfdir}/uefi/certs/*.bin
%{_sysconfdir}/uefi/certs/*.crt

%changelog
