#
# spec file for package pam_radius
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


Name:           pam_radius
Version:        2.0.0
Release:        0
Summary:        A PAM Module for User Authentication using a Radius Server
License:        GPL-2.0+
Group:          Productivity/Security
URL:            http://freeradius.org/pam_radius_auth/
Source0:        https://github.com/FreeRADIUS/pam_radius/archive/release_2_0_0.tar.gz#/%{name}-release_2_0_0.tar.gz
Source1:        baselibs.conf
BuildRequires:  pam-devel
Requires:       pam

%description
This is the PAM to RADIUS authentication module. It allows any PAM-capable
machine to become a RADIUS client for authentication and accounting
requests. You will need a RADIUS server to perform the actual
authentication.

%prep
%setup -q -n %{name}-release_2_0_0

%build
export CFLAGS="%{optflags} -fPIC"
%configure
%make_build

%install
install -d -m 755 %{buildroot}/%{_lib}/security/
install -m 755 pam_radius_auth.so %{buildroot}/%{_lib}/security/
install -d -m 750 %{buildroot}%{_sysconfdir}/raddb/
install -m 600 pam_radius_auth.conf %{buildroot}%{_sysconfdir}/raddb/server

%files
%license LICENSE
%doc Changelog README.rst TODO USAGE index.html pam_radius_auth.conf
%attr(750,root,radiusd) %dir %{_sysconfdir}/raddb/
%config(noreplace) %{_sysconfdir}/raddb/server
/%{_lib}/security/pam_radius_auth.so

%changelog
