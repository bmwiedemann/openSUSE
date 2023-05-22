#
# spec file for package suse-build-key
#
# Copyright (c) 2023 SUSE LLC
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


Name:           suse-build-key
BuildRequires:  gpg
Provides:       build-key
Requires:       gpg
AutoReqProv:    off
Summary:        The public gpg key for rpm package signature verification
License:        GPL-2.0-or-later
Group:          System/Packages
Version:        12.0
Release:        0

# pub  2048R/39DB7C82 2013-01-31 SuSE Package Signing Key <build@suse.de>
# The main package signing key.
Source0:        gpg-pubkey-39db7c82-5f68629b.asc
#pub   rsa4096/0xF74F09BC3FA1D6CE 2023-01-19 [SC] [expires: 2027-01-18]
#      Key fingerprint = 7F00 9157 B127 B994 D5CF  BE76 F74F 09BC 3FA1 D6CE
#uid                             SUSE Package Signing Key <build@suse.de>
Source4:        gpg-pubkey-3fa1d6ce-63c9481c.asc

# pub  2048R/50A3DD1C 2013-01-14 SuSE Package Signing Key (reserve key) <build@suse.de>
# Fallback key if main key gets lost.
Source1:        gpg-pubkey-50a3dd1c-50f35137.asc
# new reserver key RSA 4096 bit
#pub   rsa4096/0xA1BFC02BD588DC46 2023-01-19 [SC] [expires: 2033-01-16]
#      Key fingerprint = B56E 5601 41D8 F654 2DFF  3BF9 A1BF C02B D588 DC46
#uid                             SUSE Package Signing Key (reserve key) <build@suse.de>
Source9:        gpg-pubkey-25db7ae0-645bae34.asc

# pub  1024R/307E3D54 2006-03-21 SuSE Package Signing Key <build@suse.de>
# SLES 10 key.
Source2:        gpg-pubkey-307e3d54-5aaa90a5.asc

#pub   rsa2048/0x8EFE1BC4D4ADE9C3 2017-12-11 [SC] [expires: 2027-12-09]
#     Key fingerprint = 0EE9 CA43 0050 9E29 17A0  54ED 8EFE 1BC4 D4AD E9C3
# container key used by Container TUF style signing.
Source3:        build-container-d4ade9c3-5a2e9669.asc

# New ALP Keys
#pub   rsa4096/0xFEC28EAF09D9EA69 2023-05-10 [SC] [expires: 2027-05-09]
#      Key fingerprint = 1C59 D66F CD52 563A 1693  3DBC FEC2 8EAF 09D9 EA69
#uid                             ALP Package Signing Key <build-alp@suse.de>
Source5:        gpg-pubkey-09d9ea69-645b99ce.asc
# reserve key
#pub   rsa4096/0xC7B81E4373F03759 2022-04-29 [SC] [expires: 2032-04-26]
#      Key fingerprint = 5056 7568 F292 0FF1 65B2  5FB2 C7B8 1E43 73F0 3759
#uid                             ALP Package Signing Key (reserve key) <build-alp@suse.de>
Source6:        gpg-pubkey-73f03759-626bd414.asc

# new 4096 bit SLES container key.
#pub   rsa4096/0x100CEB438FD6C337 2023-01-19 [SC] [expires: 2027-01-18]
#      Key fingerprint = 2BFA 4649 1A1C FFA8 31EF  C4B6 100C EB43 8FD6 C337
#uid                             SUSE Linux Container Signing Key <build-container@suse.de>
Source7:        build-container-8fd6c337-63c94b45.asc
# Exact same key in PEM format for notary and cosign
Source8:        build-container-8fd6c337-63c94b45.pem

# SUSE supplied PTF (program temporary fixes) are signed by this key.
# supplied to be not imported by default
#pub   rsa2048/0x46DFA05C6F5DA62B 2022-02-25 [SC] [expires: 2026-02-24]
#      Key fingerprint = 1604 494D 38DA 2FA7 AA26  97AE 46DF A05C 6F5D A62B
#uid                             SUSE PTF Signing Key <support@suse.com>
Source97:       suse_ptf_key.asc
#pub   rsa4096/0x09461C70AF5425F7 2023-01-19 [SC] [expires: 2027-01-18]
#      Key fingerprint = 6D6C 8072 BF35 2152 3062  D823 0946 1C70 AF54 25F7
#uid                             SUSE PTF Signing Key <support@suse.com>
Source98:       suse_ptf_4096_key.asc

# Use only for email communication!
#pub   rsa4096/0xB205E69BAB2FD922 2020-03-10 [SC] [expires: 2024-02-24]
#      Key fingerprint = 2BAB 445F B9B4 F0D3 30E4  7CB0 B205 E69B AB2F D922
#uid                             SUSE Security Team <security@suse.com>
#uid                             SUSE Security Team <security@suse.de>
#sub   rsa4096/0xA679ED66FD417627 2020-03-10 [E] [expires: 2024-02-24]
Source99:       security_at_suse_de.asc

Source100:      dumpsigs

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%define keydir  %{_prefix}/lib/rpm/gnupg/keys
%define containerkeydir  %{_prefix}/share/container-keys/
%define pemcontainerkeydir  %{_prefix}/share/pki/containers/
PreReq:         fileutils
PreReq:         gpg
PreReq:         mktemp
PreReq:         sh-utils

%description
This package contains the gpg keys that are used to sign the
SUSE rpm packages. The keys installed here are not actually
used by anything. rpm/zypper use the keys in the rpm db instead.

%prep
%setup -qcT

%build
cp %SOURCE98 .
cp %SOURCE99 .

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{keydir}
for i in %sources; do
    case "$i" in
        */gpg-pubkey-*.asc|*/*ptf*.asc)
        install -m 644 "$i" $RPM_BUILD_ROOT%{keydir}
        ;;
    esac
done
%if 0%{?suse_version} &&  0%{?suse_version} < 1120
install -m 755 %{SOURCE100} $RPM_BUILD_ROOT/usr/lib/rpm/gnupg
%endif

install -d -m 755 $RPM_BUILD_ROOT%{containerkeydir}/
install -c -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{containerkeydir}/suse-container-key.asc
install -c -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{containerkeydir}/suse-container-key-4096.asc
install -d -m 755 $RPM_BUILD_ROOT%{pemcontainerkeydir}/
install -c -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{pemcontainerkeydir}/suse-container-key.pem
install -c -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{pemcontainerkeydir}/suse-container-key-4096.pem

%files
%defattr(644,root,root)
%doc security_at_suse_de.asc
%attr(755,root,root) %dir %{_prefix}/lib/rpm/gnupg
%attr(755,root,root) %dir %{keydir}
%attr(755,root,root) %dir %{containerkeydir}
%if 0%{?suse_version} &&  0%{?suse_version} < 1120
%attr(755,root,root) %{_prefix}/lib/rpm/gnupg/dumpsigs
%endif
%{keydir}/gpg-pubkey-50a3dd1c-50f35137.asc
%{keydir}/gpg-pubkey-39db7c82-5f68629b.asc
%{keydir}/gpg-pubkey-307e3d54-5aaa90a5.asc
%{keydir}/gpg-pubkey-09d9ea69-645b99ce.asc
%{keydir}/gpg-pubkey-3fa1d6ce-63c9481c.asc
%{keydir}/gpg-pubkey-73f03759-626bd414.asc
%{keydir}/gpg-pubkey-25db7ae0-645bae34.asc
%{keydir}/suse_ptf_4096_key.asc
%{keydir}/suse_ptf_key.asc
%{containerkeydir}/suse-container-key.asc
%{containerkeydir}/suse-container-key-4096.asc
%dir /usr/share/pki/
%dir %{pemcontainerkeydir}/
%{pemcontainerkeydir}/suse-container-key.pem
%{pemcontainerkeydir}/suse-container-key-4096.pem

%changelog
