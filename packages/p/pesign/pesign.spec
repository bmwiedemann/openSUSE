#
# spec file for package pesign
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


Name:           pesign
Version:        117
Release:        0
Summary:        Signing tool for PE-COFF binaries
License:        GPL-3.0-or-later
URL:            https://github.com/rhboot/pesign
Source:         https://github.com/rhboot/pesign/releases/download/%{version}/%{name}-%{version}.tar.bz2
Source1:        pesign.sysusers
# PATCH-FIX-SUSE pesign-suse-build.patch glin@suse.com -- Adjust Makefile for the build service
Patch1:         pesign-suse-build.patch
# PATCH-FIX-UPSTREAM pesign-fix-authvar-write-loop.patch glin@suse.com -- Fix the write loop in authvar
Patch2:         pesign-fix-authvar-write-loop.patch
# PATCH-FIX-SUSE pesign-boo1143063-remove-var-tracking.patch -- boo#1143063 Remove var-tracking from default CFLAGS
Patch3:         pesign-boo1143063-remove-var-tracking.patch
# PATCH-FIX-UPSTREAM pesign-boo1185663-set-rpmmacrodir.patch boo#1185663 glin@suse.com -- Set the rpm macro directory at build time
Patch4:         pesign-boo1185663-set-rpmmacrodir.patch
Patch5:         harden_pesign.service.patch
Patch6:         pesign-bsc1202933-Make-etc-pki-pesign-writeable.patch
# PATCH-FIX-SUSE pesign-fix-wincert-maybe-uninitialized.patch -- initialize dd to silence -Werror=maybe-uninitialized (LTO false positive)
Patch7:         pesign-fix-wincert-maybe-uninitialized.patch
BuildRequires:  mandoc
BuildRequires:  pkgconfig
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(efiboot) >= 38
BuildRequires:  pkgconfig(efisec) >= 38
BuildRequires:  pkgconfig(efivar) >= 38
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(nss-util)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(uuid)
Requires:       mozilla-nss-tools
Recommends:     %{name}-systemd
ExclusiveArch:  ia64 %{ix86} x86_64 aarch64 %{arm} riscv64 loongarch64
%sysusers_requires

%description
Signing tool for PE-COFF binaries. It is vaguely compliant
with the PE and Authenticode specifications.

%package systemd
Summary:        Systemd units for pesign
Requires:       %{name} = %{version}
Provides:       pesign:%{_sbindir}/rcpesign
Provides:       pesign:%{_tmpfilesdir}/pesign.conf
Provides:       pesign:%{_unitdir}/pesign.service
BuildArch:      noarch
%{?systemd_requires}

%description systemd
Systemd units for the pesign package.

%prep
%autosetup -p1

%build
%sysusers_generate_pre %{SOURCE1} %{name} %{name}.conf
export CPPFLAGS="%{optflags} -D_GLIBCXX_ASSERTIONS"
%make_build CFLAGS="%{optflags}" LDFLAGS="${LDFLAGS} -pie" libexecdir=%{_libexecdir}

%install
mkdir -p %{buildroot}%{_sbindir}
make INSTALLROOT=%{buildroot} \
     UNITDIR=%{_unitdir} \
     libexecdir=%{_libexecdir} \
     rpmmacrodir=%{_rpmmacrodir} \
     install_systemd

# create rcsymlink
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

# there's some stuff that's not really meant to be shipped yet
rm -rf %{buildroot}/boot %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_libdir}/libdpe*

install -Dm0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

%pre -f %{name}.pre

%pre systemd
%service_add_pre pesign.service

%preun systemd
%service_del_preun pesign.service

%post systemd
%service_add_post pesign.service
systemd-tmpfiles --create %{_tmpfilesdir}/pesign.conf || :

%postun systemd
%service_del_postun pesign.service

%files
%license COPYING
%{_bindir}/pesign
%{_bindir}/pesign-client
%{_bindir}/efikeygen
%{_bindir}/pesigcheck
%{_bindir}/authvar
%{_bindir}/pesum
%dir %{_sysconfdir}/pesign
%{_sysconfdir}/pesign/*
%dir %{_sysconfdir}/popt.d
%config %{_sysconfdir}/popt.d/pesign.popt
%{_rpmmacrodir}/macros.pesign
%{_mandir}/man?/*
%{_sysusersdir}/pesign.conf
%dir %{_libexecdir}/pesign
%{_libexecdir}/pesign/pesign-rpmbuild-helper
%dir %{_sysconfdir}/pki/
%dir %attr(0755,pesign,pesign) %{_sysconfdir}/pki/pesign

%files systemd
%{_sbindir}/rcpesign
%{_unitdir}/pesign.service
%{_tmpfilesdir}/pesign.conf
%ghost %dir %attr(0770,pesign,pesign) /run/%{name}

%changelog
