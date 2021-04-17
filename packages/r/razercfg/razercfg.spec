#
# spec file for package razercfg
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


Name:           razercfg
Version:        0.42
Release:        0
Summary:        A Razer device configuration tool
# Icons are http://creativecommons.org/licenses/by/4.0/
License:        GPL-2.0-or-later AND CC-BY-SA-4.0
Group:          Hardware/Other
URL:            https://bues.ch/cms/hacking/razercfg.html
Source0:        https://bues.ch/razercfg/%{name}-%{version}.tar.xz
Source1:        https://bues.ch/razercfg/%{name}-%{version}.tar.xz.asc
Source98:       %{name}.keyring
Source99:       %{name}-rpmlintrc
# PATCH-FIX-OPENSUSE razercfg-fix-install-in-libdir -- Install libraries in matching directories (e.g. lib64 for 64bit).
# Reported upstream 21. July 2015
Patch0:         razercfg-fix-install-in-libdir.patch
BuildRequires:  cmake
BuildRequires:  help2man
BuildRequires:  hicolor-icon-theme
BuildRequires:  libusb-1_0-devel
BuildRequires:  python3-base
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(udev)
Requires:       python3-qt5
%{?systemd_ordering}

%description
Razercfg is the next generation Razer device configuration
tool bringing the Razer gaming experience to the free Open Source world.
Including commandline tool (razercfg) and QT GUI qrazercfg.

%prep
%setup -q
%patch0 -p1

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install
rm %{buildroot}%{_libdir}/librazer.so
# Systemd service and udev rule
install -D -m 444 build/razerd.service %{buildroot}%{_unitdir}/razerd.service
install -D -m 444 build/udev.rules %{buildroot}%{_udevrulesdir}/80-razer.rules
# backwards compatibility with rcNAME
mkdir -p %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcrazerd
# install man pages
mkdir -p %{buildroot}%{_mandir}/man1
help2man -N ./ui/razercfg > %{buildroot}%{_mandir}/man1/razercfg.1
help2man -N -n "Use specific profiles per game" ./ui/razer-gamewrapper > %{buildroot}%{_mandir}/man1/razer-gamewrapper.1
LD_LIBRARY_PATH=./build/librazer/ help2man -N ./build/razerd/razerd > %{buildroot}%{_mandir}/man1/razerd.1
#Desktop file
%suse_update_desktop_file -r %{name} Settings System HardwareSettings Qt

%pre
%service_add_pre razerd.service

%post
%service_add_post razerd.service
%tmpfiles_create %_tmpfilesdir/razerd.conf
%icon_theme_cache_post
udevadm control --reload-rules 2>&1 > /dev/null || :
/sbin/ldconfig

%preun
%service_del_preun razerd.service

%postun
%service_del_postun razerd.service
%icon_theme_cache_postun
udevadm control --reload-rules 2>&1 > /dev/null || :
/sbin/ldconfig

%files
%defattr(-,root,root)
%doc HACKING.md README.md COPYING ui/icons/LICENSE
%{python3_sitelib}/*
%{_sbindir}/rcrazerd
%{_bindir}/razerd
%{_bindir}/razercfg
%{_bindir}/qrazercfg
%{_bindir}/razer-gamewrapper
%{_bindir}/qrazercfg-applet
%{_libdir}/librazer.so.1
%{_unitdir}/razerd.service
%{_tmpfilesdir}/razerd.conf
%{_udevrulesdir}/80-razer.rules
%ghost %{_rundir}/razerd
%{_datadir}/icons/hicolor/scalable/apps/razercfg*.svg
%{_datadir}/applications/razercfg.desktop
%{_mandir}/man1/razer*
%dir %{_sysconfdir}/pm
%dir %{_sysconfdir}/pm/sleep.d
%{_sysconfdir}/pm/sleep.d/50-razer

%changelog
