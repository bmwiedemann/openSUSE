#
# spec file for package NetworkManager-branding
#
# Copyright (c) 2024 SUSE LLC
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


%define flavor @BUILD_FLAVOR@%nil
%if "%{flavor}" == ""
%define branding_name %{nil}
ExclusiveArch:  %{nil}
%else
%define branding_name %{flavor}
%define dash -
%if "%{flavor}" == "SLE"
%define build_SLE 1
%else
%define build_openSUSE 1
%endif
%endif
Name:           NetworkManager-branding%{?dash}%{branding_name}
Version:        42.1
Release:        0
Summary:        Default %{branding_name} branding for NetworkManager configuration file
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
URL:            http://www.gnome.org/projects/NetworkManager/
Source0:        NetworkManager.conf.in
Source1:        NetworkManager-branding-COPYING
BuildRequires:  NetworkManager
BuildRequires:  NetworkManager-branding-upstream
%requires_eq    NetworkManager
Supplements:    (NetworkManager and branding-%{branding_name})
Conflicts:      NetworkManager-branding
Provides:       NetworkManager-branding = %{version}
BuildArch:      noarch
%if (0%{?build_SLE} && 0%{?is_opensuse}) || (0%{?build_openSUSE} && ! 0%{?is_opensuse})
# Don't build SLE branding on openSUSE and vice-versa
ExclusiveArch:  do-not-build
%endif

%description
NetworkManager attempts to keep an active network connection available
at all times.  The point of NetworkManager is to make networking
configuration and setup as painless and automatic as possible.	If
using DHCP, NetworkManager is intended to replace default routes,
obtain IP addresses from a DHCP server, and change name servers
whenever it sees fit.

This package provides the default %{branding_name} configuration for
/usr/lib/NetworkManager/conf.d/conncheck.conf, configured to
check connectivity against http://conncheck.opensuse.org.

%prep
%setup -q -T -c %{name}-%{version}
cp %{SOURCE1} COPYING

%build

%install
install -m0644 -D %{SOURCE0} %{buildroot}%{_prefix}/lib/NetworkManager/conf.d/conncheck-%{branding_name}.conf

%files
%license COPYING
%{_prefix}/lib/NetworkManager/conf.d/conncheck-%{branding_name}.conf

%changelog
