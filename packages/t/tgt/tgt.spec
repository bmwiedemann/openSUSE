#
# spec file for package tgt
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           tgt
Version:        1.0.74
Release:        0
Summary:        Generic Linux target framework (tgt)
License:        GPL-2.0-only
Group:          System/Daemons
Url:            http://stgt.sourceforge.net/
Source:         https://github.com/fujita/%{name}/archive/v%{version}.tar.gz
Source1:        %{name}d.service
Source4:        sysconfig.%{name}
Patch1:         %{name}-fix-build
Patch2:         setup-tgt-conf-d.patch
Patch3:         %{name}-include-sys-macros-for-major.patch
Patch4:         %{name}-Fix-gcc7-string-truncation-warnings.patch
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libaio-devel
BuildRequires:  libxslt
BuildRequires:  openssl-devel
BuildRequires:  perl-Config-General
BuildRequires:  systemd-rpm-macros
Requires:       perl-Config-General
Requires(pre):  %fillup_prereq
Obsoletes:      iscsitarget

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
make OPTFLAGS="%{optflags}" %{backends}

%install
make DESTDIR=%{buildroot} docdir=%{_docdir}/%{name} install
install -vD -m 644 %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}d.service
install -vD %{SOURCE4} %{buildroot}%{_fillupdir}/sysconfig.%{name}
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
%defattr(-,root,root)
%{_sbindir}/*
%dir %{_sysconfdir}/tgt
%dir %{_sysconfdir}/tgt/conf.d
%config %attr(0644,root,root) %{_sysconfdir}/tgt/targets.conf
%{_fillupdir}/sysconfig.tgt
%{_unitdir}/%{name}d.service
%doc README doc/README.iscsi doc/README.iser doc/README.lu_configuration
%doc doc/README.mmc doc/README.passthrough doc/README.sbcjukebox doc/README.ssc
%doc doc/README.rbd doc/tmf.txt
%doc %_defaultdocdir/%name/examples
%doc %_defaultdocdir/%name/html
%{_mandir}/man5/*
%{_mandir}/man8/*

%changelog
