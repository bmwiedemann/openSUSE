#
# spec file for package bootkitd
#
# Copyright (c) 2025 SUSE LLC
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

Name: bootkitd
Version: 0.4.1
Release: 0%{?dist}
Summary: Service for editing bootloader configurations
License: MIT
URL:            https://github.com/Nykseli/bootkitd
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.xz
Source3:        vendor.tar.zst
ExclusiveArch:  %{rust_arches}

BuildRequires: cargo >= 1.74.0
BuildRequires: cargo-packaging
BuildRequires: sqlite3

%description
Service for editing bootloader configurations

%prep
%autosetup -a3

%build

# sqlx database setup
./scripts/setup_local_db.sh
export DATABASE_URL=sqlite://`pwd`/tmp/bootkit.db
%{cargo_build}
./scripts/clean_local_db.sh

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_prefix}/share/dbus-1/system.d
mkdir -p %{buildroot}%{_prefix}/share/dbus-1/system-services
install -m 0755 ./target/release/bootkit %{buildroot}%{_sbindir}/bootkitd
install -m 0644 ./dbus/bootkitd.service %{buildroot}%{_unitdir}/bootkitd.service
install -m 0644 ./dbus/org.opensuse.bootkit.conf %{buildroot}%{_prefix}/share/dbus-1/system.d/org.opensuse.bootkit.conf
install -m 0644 ./dbus/org.opensuse.bootkit.service %{buildroot}%{_prefix}/share/dbus-1/system-services/org.opensuse.bootkit.service

mkdir -p %{buildroot}/var/lib/bootkit
touch %{buildroot}/var/lib/bootkit/bootkit.db

%check

%preun
%systemd_preun bootkitd.service

%postun
%systemd_postun_with_restart bootkitd.service

%files
%license LICENSE

%dir %{_prefix}/share/dbus-1
%dir %{_prefix}/share/dbus-1/system.d
%dir %{_prefix}/share/dbus-1/system-services
%dir /var/lib/bootkit
%ghost %attr(0640,root,root) /var/log/bootkitd.log
%ghost /var/lib/bootkit/bootkit.db
%{_sbindir}/bootkitd
%{_unitdir}/bootkitd.service
%{_prefix}/share/dbus-1/system.d/org.opensuse.bootkit.conf
%{_prefix}/share/dbus-1/system-services/org.opensuse.bootkit.service

%changelog
