#
# spec file for package pesign
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


Name:           pesign
Version:        113
Release:        0
Summary:        Signing tool for PE-COFF binaries
License:        GPL-3.0-or-later
Group:          Productivity/Security
URL:            https://github.com/rhinstaller/pesign
Source:         https://github.com/rhinstaller/pesign/releases/download/%{version}/%{name}-%{version}.tar.bz2
Source1:        pesign.sysusers
# PATCH-FIX-SUSE pesign-suse-build.patch glin@suse.com -- Adjust Makefile for the build service
Patch1:         pesign-suse-build.patch
# PATCH-FIX-UPSTREAM pesign-privkey_unneeded.diff glin@suse.com -- Don't check the private key when importing the raw signature
Patch2:         pesign-privkey_unneeded.diff
# PATCH-FIX-SUSE pesign-run.patch aj@suse.com - Use /run instead of /var/run
Patch3:         pesign-run.patch
# PATCH-FIX-UPSTREAM pesign-fix-authvar-write-loop.patch glin@suse.com -- Fix the write loop in authvar
Patch4:         pesign-fix-authvar-write-loop.patch
# PATCH-FIX-UPSTREAM pesign-efikeygen-Fix-the-build-with-nss-3.44.patch glin@suse.com -- Fix the NSS 3.44 compilation error
Patch5:         pesign-efikeygen-Fix-the-build-with-nss-3.44.patch
# PATCH-FIX-SUSE pesign-boo1143063-remove-var-tracking.patch -- boo#1143063 Remove var-tracking from default CFLAGS
Patch6:         pesign-boo1143063-remove-var-tracking.patch
# PATCH-FIX-UPSTREAM pesign-boo1158197-fix-pesigncheck-gcc10.patch glin@suse.com -- boo#1158197 Fix the gcc10 errors
Patch7:         pesign-boo1158197-fix-pesigncheck-gcc10.patch
# PATCH-FIX-UPSTREAM pesign-boo1185663-set-rpmmacrodir.patch boo#1185663 glin@suse.com -- Set the rpm macro directory at build time
Patch8:         pesign-boo1185663-set-rpmmacrodir.patch
Patch9:         harden_pesign.service.patch
Patch10:        pesign-bsc1202933-Use-normal-file-permissions-instead-of-ACLs.patch
Patch11:        pesign-bsc1202933-Make-etc-pki-pesign-writeable.patch
BuildRequires:  efivar-devel
BuildRequires:  libuuid-devel
BuildRequires:  mozilla-nss-devel
BuildRequires:  pkg-config
BuildRequires:  popt-devel
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(systemd)
%sysusers_requires
%{?systemd_requires}
ExclusiveArch:  ia64 %ix86 x86_64 aarch64 %arm riscv64

%description
Signing tool for PE-COFF binaries. It is vaguely compliant
with the PE and Authenticode specifications.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1

%build
%sysusers_generate_pre %{SOURCE1} %{name} %{name}.conf
make %{?_smp_mflags} CFLAGS="%{optflags}" LDFLAGS="${LDFLAGS} -pie" libexecdir=%{_libexecdir}

%install
mkdir -p %{buildroot}%{_localstatedir}/lib/pesign
mkdir -p %{buildroot}%{_sbindir}
make INSTALLROOT=%{buildroot} \
     UNITDIR=%{_unitdir} \
     libexecdir=%{_libexecdir} \
     rpmmacrodir=%{_rpmmacrodir} \
     install_systemd

# create rcsymlink
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

# there's some stuff that's not really meant to be shipped yet
rm -rf %{buildroot}/boot %{buildroot}%{_prefix}/include
rm -rf %{buildroot}%{_libdir}/libdpe*

install -Dm0644 %{SOURCE1} %{buildroot}%{_sysusersdir}/%{name}.conf

%pre -f %{name}.pre
%service_add_pre pesign.service

%preun
%service_del_preun pesign.service

%post
%service_add_post pesign.service
systemd-tmpfiles --create %{_tmpfilesdir}/pesign.conf || :

%postun
%service_del_postun pesign.service

%files
%defattr(-,root,root)
%license COPYING
%{_bindir}/pesign
%{_bindir}/pesign-client
%{_bindir}/efikeygen
%{_bindir}/pesigcheck
%{_bindir}/efisiglist
%{_bindir}/authvar
%{_sbindir}/rcpesign
%dir %{_sysconfdir}/pesign
%{_sysconfdir}/pesign/*
%dir %{_sysconfdir}/popt.d
%config %{_sysconfdir}/popt.d/pesign.popt
%{_sysconfdir}/pki/
%{_rpmmacrodir}/macros.pesign
%{_mandir}/man?/*
%{_localstatedir}/lib/pesign
%{_unitdir}/pesign.service
%{_sysusersdir}/pesign.conf
%{_tmpfilesdir}/pesign.conf
%dir %{_libexecdir}/pesign
%{_libexecdir}/pesign/pesign-authorize
%dir %attr(0775,pesign,pesign) %{_sysconfdir}/pki/pesign
%ghost %dir %attr(0770,pesign,pesign) /run/%{name}
%dir %attr(0770,pesign,pesign) %{_localstatedir}/lib/%{name}

%changelog
