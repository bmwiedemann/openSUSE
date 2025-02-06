#
# spec file for package sddm-kalpa
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024 Neal Gompa
# Copyright (c) 2024 Shawn W Dunn
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


%bcond x11 0

%define _name sddm

Name:           sddm-kalpa
Version:        0.21.0
Release:        0
Summary:        QML based desktop and login manager - Wayland Only
License:        GPL-2.0-or-later
URL:            https://github.com/sddm/sddm
Source0:        %{url}/archive/v%{version}/%{_name}-%{version}.tar.gz
Source1:        sddm.pam
Source2:        sddm-autologin.pam
Source3:        sddm.conf
Source4:        README.scripts
Source5:        sddm-x11.conf
# sysusers config file. note these are shipped in the upstream tarball, but we
# cannot use the fles from the tarball for %%pre scriptlet generation, so we
# duplicate them as source files for that purpose; this is an ugly hack that
# should be removed if it becomes possible.
# see: https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/thread/TFDMAU7KLMSQTKPJELHSM6PFVXIZ56GK/
Source6:        sddm-systemd-sysusers.conf
Source7:        sddm-greeter.pam
Source8:        10-weston.conf
Source9:        10-kwin.conf

Provides:       sddm = %{version}
Conflicts:      sddm-qt6

# PATCH-FIX-UPSTREAM sddm-PR1876.patch https://github.com/sddm/sddm/pull/1876
Patch1:         sddm-PR1876.patch
# PATCH-FIX-UPSTREAM 0001-Delay-for-logind-and-fallback-to-seat0.patch
# https://github.com/sddm/sddm/pull/1494
Patch2:         0001-Delay-for-logind-and-fallback-to-seat0.patch
# PATCH-FIX-OPENSUSE sddm-0.20.0-fedora_config.patch Stolen from Fedora
Patch3:         sddm-0.20.0-fedora_config.patch
# PATCH-FIX-OPENSUSE sddm-0.21.0-qt6greeter.patch
Patch4:         sddm-0.21.0-qt6greeter.patch

BuildRequires:  cmake >= 3.5.0
BuildRequires:  docutils
BuildRequires:  fdupes
BuildRequires:  shadow
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(Qt6Test)

BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-xkb)

Requires:       sddm-greeter-displayserver
Requires:       systemd
Requires:       group(sddm)
%if %{with x11}
Requires:       xinit
%endif

Conflicts:      sddm
Conflicts:      sddm-greeter-qt5
Conflicts:      sddm-greeter-qt6

%{?systemd_requires}
%{?sysusers_requires}

%description
sddm-kalpa provides a stripped down wayland only version of sddm

SDDM is a modern graphical display manager aiming to be fast, simple and
beautiful. It uses modern technologies like QtQuick, which in turn gives the
designer the ability to create smooth, animated user interfaces.

%lang_package

%package wayland-generic
Summary:        Generic Wayland SDDM greeter configuration
Provides:       sddm-greeter-displayserver
Conflicts:      %{name}-kwin
Conflicts:      sddm-greeter-displayserver
Requires:       %{name} = %{version}
Requires:       qt6-wayland
Requires:       weston
BuildArch:      noarch

%description wayland-generic
This package contains configuration and dependencies for SDDM to use Weston
for the greeter display server.

This is the generic default Wayland configuration provided by SDDM.

%package kwin
Summary:        SDDM Greeter configuration using kwin_wayland
Provides:       sddm-greeter-displayserver
Conflicts:      %{name}-wayland-generic
Conflicts:      sddm-greeter-displayserver
Requires:       %{name} = %{version}
Requires:       breeze6-cursors
Requires:       kwin6
BuildArch:      noarch

%description kwin
This package contains configuration and dependencies for SDDM to use the
kwin_wayland compositor

%if %{with x11}
%package x11
Summary:        X11 SDDM greeter configuration
Provides:       sddm-greeter-displayserver
Conflicts:      sddm-greeter-displayserver
Requires:       %{name} = %{version}
Requires:       xorg-x11-server
Recommends:     libQt6VirtualKeyboard6
BuildArch:      noarch

%description x11
This package contains configuration and dependencies for SDDM to use X11 for
the greeter display server.
%endif

%package themes
Summary:        SDDM Themes
# for upgrade path
Obsoletes:      sddm < 0.2.0
Requires:       %{name} = %{version}
BuildArch:      noarch

%description themes
A collection of sddm themes, including: elarun, maldives, maya

%prep
%autosetup -p1 -n %{_name}-%{version}

%build
LOGIN_DEFS_PATH="%{_sysconfdir}/login.defs"
[ -e "$LOGIN_DEFS_PATH" ] || LOGIN_DEFS_PATH="%{_distconfdir}/login.defs"

%cmake -DBUILD_WITH_QT6:BOOL=ON \
       -DBUILD_MAN_PAGES:BOOL=ON \
       -DCMAKE_BUILD_TYPE:STRING="Release" \
       -DENABLE_JOURNALD:BOOL=ON \
       -DPID_FILE="/run/sddm.pid" \
       -DLOGIN_DEFS_PATH:PATH="${LOGIN_DEFS_PATH}" \
       -DSESSION_COMMAND:PATH=%{_sysconfdir}/X11/xdm/Xsession \
       -DWAYLAND_SESSION_COMMAND:PATH=%{_sysconfdir}/sddm/wayland-session \
       -DINSTALL_PAM_CONFIGURATION:BOOL=OFF

%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_sysconfdir}/sddm.conf.d
mkdir -p %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
# Install PAM Configuration
pam_dest="%{?_pam_vendordir}%{!?_pam_vendordir:%{_sysconfdir}/pam.d}"
install -Dm 0644 %{SOURCE1} %{buildroot}${pam_dest}/sddm
install -Dm 0644 %{SOURCE2} %{buildroot}${pam_dest}/sddm-autologin
install -Dm 0644 %{SOURCE7} %{buildroot}${pam_dest}/sddm-greeter

install -Dpm 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/sddm.conf
install -Dpm 644 %{SOURCE4} %{buildroot}%{_datadir}/sddm/scripts/README.scripts
install -Dpm 644 %{SOURCE8} %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d/10-weston.conf
install -Dpm 644 %{SOURCE9} %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d/10-kwin.conf

%if %{with x11}
install -Dpm 644 %{SOURCE5} %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d/x11.conf
%endif
mkdir -p %{buildroot}/run/sddm
mkdir -p %{buildroot}%{_localstatedir}/lib/sddm
mkdir -p %{buildroot}%{_sysconfdir}/sddm/
cp -a %{buildroot}%{_datadir}/sddm/scripts/* %{buildroot}%{_sysconfdir}/sddm/
# We're using /etc/X11/xinit/Xsession (by default) instead
rm -fv %{buildroot}%{_sysconfdir}/sddm/Xsession

# De-conflict the dbus file
mv %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager.conf \
   %{buildroot}%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager-sddm.conf

%if 0%{?suse_version}
# Provide unversioned greeter
ln -sr %{buildroot}%{_bindir}/sddm-greeter-qt6 %{buildroot}%{_bindir}/sddm-greeter
%endif

%fdupes -s %{buildroot}%{_datadir}

%find_lang %{name} --with-qt --all-name

%pre
%sysusers_create_package %{name} %{SOURCE6}
%service_add_pre sddm.service

%post
%service_add_post sddm.service

%preun
%service_del_preun sddm.service

%postun
%service_del_postun sddm.service

%check
%ctest

%files
%license LICENSE
%doc README.md CONTRIBUTORS
%dir %{_sysconfdir}/sddm/
%dir %{_sysconfdir}/sddm.conf.d
%dir %{_prefix}/lib/sddm
%dir %{_prefix}/lib/sddm/sddm.conf.d
%dir %{_datadir}/sddm
%dir %{_datadir}/sddm/themes
%config %{_sysconfdir}/sddm/*
%config %{_sysconfdir}/sddm.conf
%{_pam_vendordir}/sddm
%{_pam_vendordir}/sddm-autologin
%{_pam_vendordir}/sddm-greeter
%{_datadir}/dbus-1/system.d/org.freedesktop.DisplayManager-sddm.conf
%{_bindir}/sddm
%{_bindir}/sddm-greeter*
%{_libexecdir}/sddm-helper
%{_libexecdir}/sddm-helper-start-wayland
%{_libexecdir}/sddm-helper-start-x11user
%{_tmpfilesdir}/sddm.conf
%{_sysusersdir}/sddm.conf
%ghost %attr(0711, root, sddm) %dir /run/sddm
%attr(1770, sddm, sddm) %dir %{_localstatedir}/lib/sddm
%{_unitdir}/sddm.service
%{_qt6_archdatadir}/qml/SddmComponents/
%{_datadir}/sddm/faces/
%{_datadir}/sddm/flags/
%{_datadir}/sddm/scripts/
%{_mandir}/man?/sddm*

%files wayland-generic
%{_prefix}/lib/sddm/sddm.conf.d/10-weston.conf

%files kwin
%{_prefix}/lib/sddm/sddm.conf.d/10-kwin.conf

%if %{with x11}
%files x11
%{_prefix}/lib/sddm/sddm.conf.d/x11.conf
%endif

%files themes
%{_datadir}/sddm/themes/elarun/
%{_datadir}/sddm/themes/maldives/
%{_datadir}/sddm/themes/maya/

%files lang -f %{name}.lang
%dir %{_datadir}/sddm/translations-qt6

%changelog
