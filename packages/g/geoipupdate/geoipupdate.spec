#
# spec file for package geoipupdate
#
# Copyright (c) 2020 SUSE LLC
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


# Common info
Name:           geoipupdate
Version:        4.2.2
Release:        0
Summary:        GeoIP update client code
License:        GPL-2.0-only
Group:          Productivity/Networking/Other
URL:            https://github.com/maxmind/geoipupdate
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Source2:        geoipupdate.timer
Source3:        geoipupdate.service
Patch0:         disable-pandoc.patch
# Build-time parameters
BuildRequires:  go >= 1.10
# Manpage
BuildRequires:  perl%{?suse_version:-base}

%description
The GeoIP Update program performs automatic updates of GeoIP2 and GeoIP Legacy
binary databases. Currently the program only supports Linux and other
Unix-like systems.

# Preparation step (unpackung and patching if necessary)
%prep
%setup -q -a1
%patch0 -p1

%build
export GOCACHE=$(pwd -P)/.gocache
export GOTRACEBACK=crash
export GOFLAGS='-a -mod=vendor -buildmode=pie -gcflags=all=-dwarf=false -ldflags=all=-s -ldflags=all=-w'
%make_build \
  CONFFILE=%{_sysconfdir}/GeoIP.conf \
  DATADIR=%{_localstatedir}/lib/GeoIP \
  VERSION=%{version}

%install
install -D -m0644 %{SOURCE2}              %{buildroot}%{_unitdir}/geoipupdate.timer
install -D -m0644 %{SOURCE3}              %{buildroot}%{_unitdir}/geoipupdate.service
install -D -m0755 build/geoipupdate       %{buildroot}%{_bindir}/geoipupdate
install -D -m0644 conf/GeoIP.conf.default %{buildroot}%{_sysconfdir}/GeoIP.conf
install -d -m0755 %{buildroot}%{_localstatedir}/lib/GeoIP
sed -ri \
 -e '/^UserId\s*/     s|YOUR_USER_ID_HERE|999999|' \
 -e '/^LicenseKey\s*/ s|YOUR_LICENSE_KEY_HERE|000000000000|' \
 -e '/^ProductIds\s*/ s|^(\w+s*).+$|\1 GeoLite2-City GeoLite2-Country GeoLite-Legacy-IPv6-City GeoLite-Legacy-IPv6-Country 506 517 533|' \
 -e '/^(#\s*)?DatabaseDirectory/ s|^(#\s*)?(\w+\s*).+$|\2%{_localstatedir}/lib/GeoIP|' \
 %{buildroot}%{_sysconfdir}/GeoIP.conf

%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc README.md build/geoipupdate.md build/GeoIP.conf.md
%license LICENSE-*
%config(noreplace) %{_sysconfdir}/GeoIP.conf
%{_bindir}/geoipupdate
%dir %{_localstatedir}/lib/GeoIP
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer

%changelog
