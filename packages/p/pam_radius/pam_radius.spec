#
# spec file for package pam_radius
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


Name:           pam_radius
Version:        3.0.0
Release:        0
Summary:        A PAM Module for User Authentication using a Radius Server
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            http://freeradius.org/pam_radius_auth/
Source:         pam_radius-3.0.0.tar.bz2
Source1:        baselibs.conf
BuildRequires:  pam-devel
Requires:       pam

%description
This is the PAM to RADIUS authentication module. It allows any PAM-capable
machine to become a RADIUS client for authentication and accounting
requests. You will need a RADIUS server to perform the actual
authentication.

%prep
%setup -q -n %{name}-%{version}

%build
export CFLAGS="%{optflags} -fPIC"
%configure --disable-developer
%make_build

%install
install -d -m 755 %{buildroot}%{_pam_moduledir}
install -m 755 pam_radius_auth.so %{buildroot}%{_pam_moduledir}

install -d -m 755 %{buildroot}%{_sysconfdir}
install -m 600 pam_radius_auth.conf %{buildroot}%{_sysconfdir}/pam_radius_auth.conf

%files
%defattr(-,root,root)
%license LICENSE
%doc Changelog README.md TODO USAGE index.html pam_radius_auth.conf
%config(noreplace) %{_sysconfdir}/pam_radius_auth.conf
%{_pam_moduledir}/pam_radius_auth.so

%changelog
