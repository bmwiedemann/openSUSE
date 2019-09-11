#
# spec file for package pam_radius
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pam_radius
Version:        1.4.0
Release:        0
Summary:        A PAM Module for User Authentication using a Radius Server
License:        GPL-2.0+
Group:          Productivity/Security
Url:            http://freeradius.org/pam_radius_auth/
Source:         ftp://ftp.freeradius.org/pub/radius/%{name}-%{version}.tar.gz
Source2:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  pam-devel
Requires:       pam

%description
This is the PAM to RADIUS authentication module. It allows any PAM-capable
machine to become a RADIUS client for authentication and accounting
requests. You will need a RADIUS server to perform the actual
authentication.

%prep
%setup -q

%build
%configure

export CFLAGS="%{optflags} -fPIC"
make %{?_smp_mflags}

%install
install -d -m 755 %{buildroot}/%{_lib}/security/
install -m 755 pam_radius_auth.so %{buildroot}/%{_lib}/security/
install -d -m 750 %{buildroot}%{_sysconfdir}/raddb/
install -m 600 pam_radius_auth.conf %{buildroot}%{_sysconfdir}/raddb/server

%files
%defattr(-,root,root)
%doc Changelog LICENSE README.rst TODO USAGE index.html pam_radius_auth.conf
%attr(750,root,radiusd) %dir %{_sysconfdir}/raddb/
%config(noreplace) %{_sysconfdir}/raddb/server
/%{_lib}/security/pam_radius_auth.so

%changelog
