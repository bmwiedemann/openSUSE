#
# spec file for package openSUSE-build-key
#
# Copyright (c) 2020 SUSE LLC
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


Name:           openSUSE-build-key
BuildRequires:  gpg
Provides:       build-key
Conflicts:      suse-build-key
Requires:       gpg
AutoReqProv:    off
Summary:        The public gpg keys for rpm package signature verification
License:        GPL-2.0-or-later
Group:          System/Packages
Version:        1.0
Release:        0
# build@suse.de for SLE11
Source0:        gpg-pubkey-307e3d54-5aaa90a5.asc
# opensuse@opensuse.org
Source1:        gpg-pubkey-3dbdc284-53674dd4.asc
# build@suse.de for SLE12 / SLE15
Source2:        gpg-pubkey-39db7c82-5f68629b.asc
# RISCV
Source3:        gpg-pubkey-697ba1e5-5c755904.asc
# zSystems
Source5:        gpg-pubkey-f6ab3975-5ad08cb7.asc
# PowerPC
Source6:        gpg-pubkey-8ede3e07-5c755f3a.asc
# Container key openSUSE
Source7:        opensuse-container-9ab48ce9-5ae3116a.asc
# Container key SUSE Linux Enterprise
Source8:        build-container-d4ade9c3-5a2e9669.asc
Source98:       security_at_suse_de.asc
Source99:       security_at_suse_de_old.asc
Source100:      dumpsigs
%define keydir  %{_prefix}/lib/rpm/gnupg/keys/
%define containerkeydir  %{_prefix}/share/container-keys/

%description
This package contains the gpg keys that are used to sign the
openSUSE rpm packages. The keys installed here are not actually
used by anything. rpm/zypper use the keys in the rpm db instead.

%prep
%setup -qcT

%build
cp %SOURCE98 .
cp %SOURCE99 .
%ifarch riscv64
cp %SOURCE3 .
%endif
%ifarch s390 s390x
cp %SOURCE5 .
%endif
%ifarch ppc ppc64 ppc64le
cp %SOURCE6 .
%endif

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{keydir}
for i in %{S:0} %{S:1} %{S:2} \
%ifarch riscv64
%{S:3} \
%endif
%ifarch s390 s390x
%{S:5} \
%endif
%ifarch ppc ppc64 ppc64le
%{S:6} \
%endif
; do
    case "$i" in
	*/gpg-pubkey-*.asc)
	install -m 644 "$i" $RPM_BUILD_ROOT%{keydir}
	;;
    esac
done
install -m 755 %{SOURCE100} $RPM_BUILD_ROOT/usr/lib/rpm/gnupg

mkdir -p $RPM_BUILD_ROOT%{containerkeydir}/
install -c -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{containerkeydir}/opensuse-container-key.asc
install -c -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{containerkeydir}/suse-container-key.asc

%files
%defattr(644,root,root)
%doc security_at_suse_de.asc security_at_suse_de_old.asc
%attr(755,root,root) %dir %{_prefix}/lib/rpm/gnupg
%attr(755,root,root) %dir %{keydir}
%attr(755,root,root) %dir %{containerkeydir}
%attr(755,root,root) %{_prefix}/lib/rpm/gnupg/dumpsigs
%{keydir}/gpg-pubkey-307e3d54-5aaa90a5.asc
%{keydir}/gpg-pubkey-3dbdc284-53674dd4.asc
%{keydir}/gpg-pubkey-39db7c82-5f68629b.asc
%{containerkeydir}/opensuse-container-key.asc
%{containerkeydir}/suse-container-key.asc
%ifarch riscv64
%{keydir}/gpg-pubkey-697ba1e5-5c755904.asc
%endif
%ifarch s390 s390x
%{keydir}/gpg-pubkey-f6ab3975-5ad08cb7.asc
%endif
%ifarch ppc ppc64 ppc64le
%{keydir}/gpg-pubkey-8ede3e07-5c755f3a.asc
%endif

%changelog
