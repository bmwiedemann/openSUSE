#
# spec file for package apache2-mod_dnssd
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2009 Dominique Leuenberger, Almere, The Netherlands.
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


%define _name   mod_dnssd
Name:           apache2-mod_dnssd
Version:        0.6
Release:        0
Summary:        Apache2 module for Zeroconf support via DNS-SD
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
URL:            http://0pointer.de/lennart/projects/mod_dnssd/
Source:         %{_name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE apache2-mod_dnssd-apxs2-prefork.patch
Patch0:         apache2-mod_dnssd-apxs2-prefork.patch
# work with apache 2.4
Patch1:         apache2-mod_dnssd-httpd24.patch
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
BuildRequires:  apr-devel
BuildRequires:  autoconf
BuildRequires:  pkg-config
Requires:       %{apache_mmn}
Requires:       %{apache_suse_maintenance_mmn}
Supplements:    packageand(apache2-prefork:gnome-user-share)
Supplements:    packageand(apache2-worker:gnome-user-share)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} > 1020
BuildRequires:  libavahi-devel
%else
BuildRequires:  avahi-devel
%endif

%description
mod_dnssd is an Apache HTTPD module which adds Zeroconf support via
DNS-SD using Avahi.

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
%configure \
	--disable-lynx
make %{?_smp_mflags}

%install
# make install can't work, as apxs -i apparently does not like redirection
mkdir -p %{buildroot}/%{apache_libexecdir}
cp -p src/.libs/%{_name}.so %{buildroot}/%{apache_libexecdir}

%files
%defattr(-,root,root)
%doc README LICENSE
%dir %{apache_libexecdir}
%{apache_libexecdir}/%{_name}.so

%changelog
