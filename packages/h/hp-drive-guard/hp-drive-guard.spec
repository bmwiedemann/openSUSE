#
# spec file for package hp-drive-guard
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define polkitdir	%{_datadir}/polkit-1/actions

Name:           hp-drive-guard
Version:        0.3.12
Release:        0
Summary:        HP DriveGuard for SUSE
License:        GPL-2.0-or-later
Group:          Hardware/Mobile
Source:         hp-drive-guard-%{version}.tar.bz2
Source1:        hp-drive-guard.service
Patch1:         0001-Fix-misc-compile-warnings.patch
Patch2:         0002-Fix-build-with-the-new-libnotify.patch
Patch3:         use-new-polkit.diff
Patch4:         use-gtk3.diff
Patch5:         hp-drive-guard-gcc14-fix.patch
URL:            http://www.gnome.org
BuildRequires:  dbus-1-glib-devel
BuildRequires:  fdupes
BuildRequires:  gnome-common
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  libnotify-devel
BuildRequires:  libupower-glib-devel
BuildRequires:  libxslt
BuildRequires:  polkit-devel
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}

%description
HP DriveGuard for SUSE. Can protect hard disks on HP laptops by
spinning them down when shaking or free-fall is detected.

%lang_package

%prep
%autosetup -p1
%define pm_method	upower
%define user_setup	--enable-user-setup

%build
autoreconf -f -i
%configure --with-pm=%{pm_method} %user_setup \
	--disable-schemas-install \
	--disable-scrollkeeper
%{?make_build:%make_build}
%{?!make_build:make %{?_smp_mflags}}

%install
%make_install
mkdir -p %{buildroot}/%{_unitdir}
install -cm 0644 %{S:1} %{buildroot}/%{_unitdir}/hp-drive-guard.service
# do not ship the init.d script on a systemd setup
rm %{buildroot}%{_sysconfdir}/init.d/hp-drive-guard
%find_lang %{name}
%fdupes %buildroot/%_prefix

%pre
%service_add_pre hp-drive-guard.service

%post
%service_add_post hp-drive-guard.service

%preun
%service_del_preun hp-drive-guard.service

%postun
%service_del_postun hp-drive-guard.service

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%license COPYING
%config(noreplace) /etc/*.conf
%{_bindir}/*
%{_sbindir}/*
%{_libexecdir}/hp-drive-guard
%{_sysconfdir}/xdg/autostart/hp-drive-guard-client.desktop
%{_sysconfdir}/dbus-1/system.d/hp-drive-guard-dbus.conf
%{polkitdir}/*
%{_unitdir}/hp-drive-guard.service

%changelog
