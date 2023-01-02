#
# spec file for package tgt
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
#Compat macro for make_build macro (needed in SLE12-SP5)
%if ! %{defined make_build}
  %define make_build %{__make} %{?_smp_mflags}
%endif
Name:           tgt
Version:        1.0.85
Release:        0
Summary:        Generic Linux target framework (tgt)
License:        GPL-2.0-only
Group:          System/Daemons
URL:            https://github.com/fujita/tgt
Source:         https://github.com/fujita/tgt/archive/refs/tags/v%{version}.tar.gz
Source1:        sysconfig.%{name}
Patch1:         %{name}-fix-build
Patch2:         %{name}-install-examples-in-documentation-dir.patch
Patch3:         harden_tgtd.service.patch
Patch4:         %{name}-systemd-service-update.patch
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libaio-devel
BuildRequires:  libxslt-tools
BuildRequires:  libxslt1
BuildRequires:  openssl-devel
BuildRequires:  perl-Config-General
BuildRequires:  systemd-rpm-macros
Requires:       perl-Config-General
Requires(pre):  %fillup_prereq
Obsoletes:      iscsitarget
%{?systemd_requires}

%description
Linux target framework (tgt) aims to simplify various SCSI target
driver (iSCSI, Fibre Channel, SRP, etc) creation and maintenance.

Tgt consists of kernel modules, user-space daemon, and user-space
tools. Some target drivers uses all of them and some use only
user-space daemon and tools (i.e. they completely runs in user space).

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%ifarch ppc ppc64 ppc64le
%define backends ISCSI=1 FCP=1 FCOE=1 IBMVIO=1
%else
%define backends ISCSI=1 FCP=1 FCOE=1
%endif
%make_build OPTFLAGS="%{optflags}" %{backends}

%install
make DESTDIR=%{buildroot} docdir=%{_docdir}/%{name} install
install -vDm644 scripts/tgtd.service %{buildroot}%{_unitdir}/tgtd.service
install -vD %{S:1} %{buildroot}%{_fillupdir}/sysconfig.%{name}
ln -sf service %{buildroot}/%{_sbindir}/rc%{name}d

%pre
%service_add_pre %{name}d.service

%post
%fillup_only
%service_add_post %{name}d.service

%preun
%service_del_preun %{name}d.service

%postun
%service_del_postun %{name}d.service

%files
%license LICENSE
%doc README.md doc/README.iscsi doc/README.iser doc/README.lu_configuration
%doc doc/README.mmc doc/README.passthrough doc/README.sbcjukebox doc/README.ssc
%doc doc/README.rbd doc/README.glfs doc/README.sheepdog doc/README.vtl
%doc doc/tmf.txt
%doc %{_defaultdocdir}/%{name}/examples
%doc %{_defaultdocdir}/%{name}/html
%{_sbindir}/rctgtd
%{_sbindir}/tgt-admin
%{_sbindir}/tgt-setup-lun
%{_sbindir}/tgtadm
%{_sbindir}/tgtd
%{_sbindir}/tgtimg
%dir %{_sysconfdir}/tgt
%dir %{_sysconfdir}/tgt/conf.d
%config %attr(0644,root,root) %{_sysconfdir}/tgt/targets.conf
%{_fillupdir}/sysconfig.tgt
%{_unitdir}/%{name}d.service
%{_mandir}/man5/*
%{_mandir}/man8/*

%changelog
