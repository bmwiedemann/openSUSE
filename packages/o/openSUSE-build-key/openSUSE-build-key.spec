#
# spec file for package openSUSE-build-key
#
# Copyright (c) 2022 SUSE LLC
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
# needspubkeyforbuild


%define keydir  %{_prefix}/lib/rpm/gnupg/keys/
%define containerkeydir  %{_datadir}/container-keys/
%define pemcontainerkeydir  /%{_datadir}/pki/containers/

Name:           openSUSE-build-key
Version:        1.0
Release:        0
Summary:        The public gpg keys for rpm package signature verification
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            https://en.opensuse.org/openSUSE:Security_team
Source:         key2rpmname
# opensuse@opensuse.org
Source1:        gpg-pubkey-3dbdc284-53674dd4.asc
# openSUSE RSA 4096 key
Source10:       gpg-pubkey-29b700a4-62b07e22.asc
# build@suse.de for SLE12 / SLE15
Source2:        gpg-pubkey-39db7c82-5f68629b.asc
# RISCV
Source3:        gpg-pubkey-697ba1e5-5c755904.asc
# zSystems
Source5:        gpg-pubkey-f6ab3975-5edd7d4f.asc
# PowerPC
Source6:        gpg-pubkey-8ede3e07-5c755f3a.asc
# Container key openSUSE
Source7:        opensuse-container-9ab48ce9-5ae3116a.asc
# Container key SUSE Linux Enterprise
Source8:        build-container-d4ade9c3-5a2e9669.asc
# openSUSE Backports key (previously PackageHub, now also Leap 15.3 / 15.4)
Source9:        gpg-pubkey-65176565-61a0ee8f.asc
# Container key SUSE Linux Enterprise in PEM format
Source11:       build-container-d4ade9c3-5a2e9669.pem
Source98:       security_at_suse_de.asc
BuildRequires:  gpg
Conflicts:      suse-build-key
Provides:       build-key = %{version}

# Old 1024 bit RSA key for SLE11.
Obsoletes:      gpg-pubkey = 307e3d54-5aaa90a5

%description
This package contains the gpg keys that are used to sign the
openSUSE rpm packages. The keys installed here are not actually
used by anything. rpm/zypper use the keys in the rpm db instead.

%prep
%setup -qcT

%build
cp %{SOURCE98} .
%ifarch riscv64
cp %{SOURCE3} .
%endif
%ifarch s390 s390x
cp %{SOURCE5} .
%endif
%ifarch ppc ppc64 ppc64le
cp %{SOURCE6} .
%endif

%install
mkdir -p %{buildroot}%{keydir}
for i in %{SOURCE1} %{SOURCE10} %{SOURCE2} \
%if 0%{?sle_version}
%{SOURCE9} \
%endif
%ifarch riscv64
%{SOURCE3} \
%endif
%ifarch s390 s390x
%{SOURCE5} \
%endif
%ifarch ppc ppc64 ppc64le
%{SOURCE6} \
%endif
; do
    case "$i" in
	*/gpg-pubkey-*.asc)
	install -m 644 "$i" %{buildroot}%{keydir}
	;;
    esac
done
mkdir -p %{buildroot}%{containerkeydir}/
install -c -m 644 %{SOURCE7} %{buildroot}%{containerkeydir}/opensuse-container-key.asc
install -c -m 644 %{SOURCE8} %{buildroot}%{containerkeydir}/suse-container-key.asc
mkdir -p %{buildroot}%{pemcontainerkeydir}/
install -c -m 644 %{SOURCE11} %{buildroot}%{pemcontainerkeydir}/suse-container-key.pem
if [ -e "%_sourcedir/_pubkey" ]; then
    name="$(sh %{SOURCE0} %_sourcedir/_pubkey).asc"
    if [ ! -e "%_sourcedir/$name" ]; then
	install -D -m 644 %_sourcedir/_pubkey %{buildroot}%keydir/"$name"
    fi
fi

%files
%defattr(644,root,root)
%doc security_at_suse_de.asc
%attr(755,root,root) %dir %{_prefix}/lib/rpm/gnupg
%attr(755,root,root) %dir %{keydir}
%attr(755,root,root) %dir %{containerkeydir}
%attr(755,root,root) %dir %{_datadir}/pki/
%attr(755,root,root) %dir %{pemcontainerkeydir}
%{keydir}/gpg-pubkey-*.asc
%{containerkeydir}/opensuse-container-key.asc
%{containerkeydir}/suse-container-key.asc
%{pemcontainerkeydir}/suse-container-key.pem

%changelog
