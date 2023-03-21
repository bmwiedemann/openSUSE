#
# spec file for package geoipupdate
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


# Common info
Name:           geoipupdate
Version:        4.11.1
Release:        0
Summary:        GeoIP update client code
License:        Apache-2.0 OR MIT
Group:          Productivity/Networking/Other
URL:            https://github.com/maxmind/geoipupdate
Source0:        %{name}-%{version}.tar.gz
# go mod vendor && tar cf vendor.tar.gz vendor/
Source1:        vendor.tar.gz
Source2:        geoipupdate.timer
Source3:        geoipupdate.service
Source4:        geoipupdate-legacy
Source5:        README.SUSE
Patch0:         disable-pandoc.patch
%if 0%{?suse_version} >= 1500
# Build-time parameters
BuildRequires:  go >= 1.13
# Manpage
BuildRequires:  perl%{?suse_version:-base}
%endif

%description
The GeoIP Update program performs automatic updates of GeoIP2 and GeoIP Legacy
binary databases. Currently the program only supports Linux and other
Unix-like systems.

%package legacy
Summary:        GeoIP Lagacy Format Updater
Group:          Productivity/Networking/Other
Requires:       geoipupdate
Requires:       geolite2legacy

%description legacy
Script for updating data in GeoIP Legacy format.





# Preparation step (unpackung and patching if necessary)

%prep
%setup -q -a1
%patch0 -p1

%build
%if 0%{?suse_version} >= 1500
export GOCACHE=$(pwd -P)/.gocache
export GOTRACEBACK=crash
export GOFLAGS='-a -mod=vendor -buildmode=pie -gcflags=all=-dwarf=false -ldflags=all=-s -ldflags=all=-w'
%make_build \
  CONFFILE=%{_sysconfdir}/GeoIP.conf \
  DATADIR=%{_localstatedir}/lib/GeoIP \
  VERSION=%{version}
%endif

%install
%if 0%{?suse_version} >= 1500
install -D -m0644 %{SOURCE2}              %{buildroot}%{_unitdir}/geoipupdate.timer
install -D -m0644 %{SOURCE3}              %{buildroot}%{_unitdir}/geoipupdate.service
install -D -m0755 build/geoipupdate       %{buildroot}%{_bindir}/geoipupdate
%endif
install -D -m0755 %{SOURCE4}              %{buildroot}%{_bindir}/geoipupdate-legacy
install -D -m0644 %{SOURCE5}              %{buildroot}%{_docdir}/geoipupdate/README.SUSE
install -D -m0644 conf/GeoIP.conf.default %{buildroot}%{_sysconfdir}/GeoIP.conf
install -d -m0755 %{buildroot}%{_localstatedir}/lib/GeoIP
sed -ri \
 -e 's|YOUR_ACCOUNT_ID_HERE|999999|' \
 -e 's|YOUR_LICENSE_KEY_HERE|000000000000|' \
 -e '/^(#\s*)?DatabaseDirectory/ s|^(#\s*)?(\w+\s*).+$|\2%{_localstatedir}/lib/GeoIP|' \
 %{buildroot}%{_sysconfdir}/GeoIP.conf

%if 0%{?suse_version} >= 1500
%pre
%service_add_pre %{name}.service

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service
%endif

%files
%license LICENSE-*
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/GeoIP.conf
%dir %{_localstatedir}/lib/GeoIP
%if 0%{?suse_version} >= 1500
%doc README.md README.SUSE build/geoipupdate.md build/GeoIP.conf.md
%{_bindir}/geoipupdate
%{_unitdir}/%{name}.service
%{_unitdir}/%{name}.timer
%endif

%files legacy
%{_bindir}/geoipupdate-legacy

%changelog
