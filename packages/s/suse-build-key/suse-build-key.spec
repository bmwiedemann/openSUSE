#
# spec file for package suse-build-key
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           suse-build-key
BuildRequires:  gpg
Provides:       build-key
Requires:       gpg
AutoReqProv:    off
Summary:        The public gpg key for rpm package signature verification
License:        GPL-2.0+
Group:          System/Packages
Version:        12.0
Release:        0

# pub  2048R/39DB7C82 2013-01-31 SuSE Package Signing Key <build@suse.de>
# The main package signing key.
Source0:        gpg-pubkey-39db7c82-5847eb1f.asc

# pub  2048R/50A3DD1C 2013-01-14 SuSE Package Signing Key (reserve key) <build@suse.de>
# Fallback key if main key gets lost.
Source1:        gpg-pubkey-50a3dd1c-50f35137.asc

# pub  1024R/307E3D54 2006-03-21 SuSE Package Signing Key <build@suse.de>
# SLES 10 key.
Source2:        gpg-pubkey-307e3d54-5aaa90a5.asc

# pub  1024D/B37B98A9 2005-05-11 SUSE PTF Signing Key <support@suse.com>
# SUSE supplied PTF (program temporary fixes) are signed by this key.
# supplied to be not imported by default
Source98:       suse_ptf_key.asc

#pub   rsa4096/0x21FE92322BA9E067 2018-03-15 [SC] [expires: 2020-03-14]
#      Key fingerprint = EC7C 5EAB 2C34 09A6 4F3B  BE6E 21FE 9232 2BA9 E067
#uid                             SUSE Security Team <security@suse.com>
#uid                             SUSE Security Team <security@suse.de>
#sub   rsa4096/0xFF97314EC1E11A0E 2018-03-15 [E] [expires: 2020-03-14]
# Only used for email communication
Source99:       security_at_suse_de.asc

Source100:      dumpsigs

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%define keydir  %{_prefix}/lib/rpm/gnupg/keys
PreReq:         sh-utils gpg fileutils mktemp

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
install -m 755 %{SOURCE100} $RPM_BUILD_ROOT/usr/lib/rpm/gnupg

%files
%defattr(644,root,root)
%doc security_at_suse_de.asc
%attr(755,root,root) %dir %{_prefix}/lib/rpm/gnupg
%attr(755,root,root) %dir %{keydir}
%attr(755,root,root) %{_prefix}/lib/rpm/gnupg/dumpsigs
%{keydir}/gpg-pubkey-50a3dd1c-50f35137.asc
%{keydir}/gpg-pubkey-39db7c82-5847eb1f.asc
%{keydir}/gpg-pubkey-307e3d54-5aaa90a5.asc
%{keydir}/suse_ptf_key.asc

%changelog
