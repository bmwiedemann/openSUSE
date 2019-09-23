#
# spec file for package servicelog
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           servicelog
Version:        1.1.14
Release:        0
Summary:        Servicelog Tools
License:        GPL-2.0
Group:          System/Management
BuildRequires:  librtas-devel
BuildRequires:  libservicelog-devel
BuildRequires:  sqlite3-devel
Url:            http://linux-diag.sourceforge.net/servicelog 
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  ppc ppc64 ppc64le

%description
Command-line interfaces for viewing and manipulating the contents of
the servicelog database.  Servicelog contains entries that are useful
for performing system service operations, and for providing a history
of service operations that have been performed on the system.



Authors:
--------
    Mike Strosaker <strosake@austin.ibm.com>
    Nathan Fontenot <nfont@austin.ibm.com>

%prep
%setup -q

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/servicelog
%{_bindir}/servicelog_notify
%{_bindir}/log_repair_action
%{_bindir}/servicelog_manage
%{_bindir}/v1_servicelog
%{_bindir}/v29_servicelog
%{_sbindir}/slog_common_event
%{_mandir}/man*/*

%changelog
