#
# spec file for package suse-build-key
#
# Copyright (c) 2021 SUSE LLC
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

# pub  2048R/50A3DD1C 2013-01-14 SuSE Package Signing Key (reserve key) <build@suse.de>
# Fallback key if main key gets lost.
Source1:        gpg-pubkey-50a3dd1c-50f35137.asc

# pub  1024R/307E3D54 2006-03-21 SuSE Package Signing Key <build@suse.de>
# SLES 10 key.
Source2:        gpg-pubkey-307e3d54-5aaa90a5.asc

#pub   rsa2048/0x8EFE1BC4D4ADE9C3 2017-12-11 [SC] [expires: 2027-12-09]
#     Key fingerprint = 0EE9 CA43 0050 9E29 17A0  54ED 8EFE 1BC4 D4AD E9C3
# container key used by Container TUF style signing.
Source3:        build-container-d4ade9c3-5a2e9669.asc

# pub  1024D/B37B98A9 2005-05-11 SUSE PTF Signing Key <support@suse.com>
# SUSE supplied PTF (program temporary fixes) are signed by this key.
# supplied to be not imported by default
Source98:       suse_ptf_key.asc

#pub   rsa4096/0xB205E69BAB2FD922 2020-03-10 [SC] [expires: 2022-03-10]
#Key fingerprint = 2BAB 445F B9B4 F0D3 30E4  7CB0 B205 E69B AB2F D922
#uid                   [  full  ] SUSE Security Team <security@suse.com>
#uid                   [  full  ] SUSE Security Team <security@suse.de>
#sub   rsa4096/0xA679ED66FD417627 2020-03-10 [E] [expires: 2022-03-10]
#      Key fingerprint = DB30 DF8E 6E44 CFF8 25E8  C858 A679 ED66 FD41 7627
# Only used for email communication
Source99:       security_at_suse_de.asc

Source100:      dumpsigs

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%define keydir  %{_prefix}/lib/rpm/gnupg/keys
%define containerkeydir  %{_prefix}/share/container-keys/
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
%{keydir}/suse_ptf_key.asc
%{containerkeydir}/suse-container-key.asc

%changelog
