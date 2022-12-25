#
# spec file for package sddm
#
# Copyright (c) 2022 SUSE LLC
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


Name:           sddm
Version:        0.19.0
Release:        0
Summary:        QML-based display manager
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://github.com/sddm/sddm
Source:         https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        X11-displaymanagers-%{name}
Source2:        00-general.conf
Source3:        10-theme.conf
Source4:        sddm-tmpfiles.conf
Source5:        system-user-sddm.conf
# Patch0-100: PATCH-FIX-UPSTREAM
Patch0:         0001-Use-PAM-s-username.patch
Patch1:         0001-Add-fish-etc-profile-and-HOME-.profile-sourcing-1331.patch
Patch2:         0004-Retry-starting-the-display-server.patch
Patch3:         0001-disable-automatic-portal-launching.patch
# Not merged yet: https://github.com/sddm/sddm/pull/997
Patch50:        0001-Remove-suffix-for-Wayland-session.patch
# Not merged yet: https://github.com/sddm/sddm/pull/1230
Patch55:        0001-Redesign-Xauth-handling.patch
# Patch100-?: PATCH-FIX-OPENSUSE
# Use openSUSE pam config
Patch100:       proper_pam.diff
Patch101:       0001-Write-the-daemon-s-PID-to-a-file-on-startup.patch
Patch102:       0001-Set-XAUTHLOCALHOSTNAME-in-sessions.patch
Patch103:       0001-Read-the-DISPLAYMANAGER_AUTOLOGIN-value-from-sysconf.patch
# sddm has some rudimentary support for plymouth handling, which only works with plymouth-quit.service
# (the servce is not enabled on openSUSE). For users of sddm.service, we need to issue plymouth quit command by hand in this case
Patch104:       sddm-service-handle-plymouth.patch
# Use tty7 by default in the systemd service unit
Patch105:       0001-Systemd-service-unit-Use-tty7-by-default.patch
Patch107:       0003-Leave-duplicate-symlinks-out-of-the-SessionModel.patch
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules >= 1.4.0
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  libqt5-linguist-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
# Autodetect UID_MIN and UID_MAX from /etc/login.defs
BuildRequires:  shadow
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(Qt5Core) >= 5.6.0
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xcb-xkb)
%systemd_requires
%sysusers_requires
Requires(post): diffutils
Requires:       sddm-branding = %{version}
Requires:       xdm
# Merged the -lang package back into the main package
Provides:       %{name}-lang = %{version}
Obsoletes:      %{name}-lang < %{version}
BuildRequires:  python3-docutils

%description
SDDM is a display manager for X11. It uses technologies like QtQuick,
which in turn gives the designer the ability to create animated user
interfaces.

%package branding-openSUSE
Summary:        openSUSE branding for SDDM, a QML-based display manager
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Requires:       sddm-theme-openSUSE
Requires(post): %{name}
Requires(post): diffutils
Supplements:    (plasma5-workspace and branding-openSUSE)
Conflicts:      sddm-branding
Provides:       sddm-branding = %{version}

%description branding-openSUSE
SDDM is a display manager for X11. It uses technologies like QtQuick,
which in turn gives the designer the ability to create animated user
interfaces.
This package provides the openSUSE branding for SDDM.

%package branding-upstream
Summary:        Upstream branding for SDDM, a QML-based display manager
Group:          System/GUI/KDE
Requires:       %{name} = %{version}
Requires(post): %{name}
Requires(post): diffutils
Supplements:    (%{name} and branding-upstream)
Conflicts:      sddm-branding
Provides:       sddm-branding = %{version}

%description branding-upstream
SDDM is a display manager for X11. It uses technologies like QtQuick,
which in turn gives the designer the ability to create animated user
interfaces.
This package provides upstream branding for SDDM.

%prep
%autosetup -p1

%build
%sysusers_generate_pre %{SOURCE5} sddm system-user-sddm.conf
LOGIN_DEFS_PATH="%{_sysconfdir}/login.defs"
if test \( -n "%{?_distconfdir}" -a -e "%{_distconfdir}/login.defs" \); then
  LOGIN_DEFS_PATH="%{_distconfdir}/login.defs"
fi

%cmake \
      -DCMAKE_BUILD_TYPE=Release \
      -DMINIMUM_VT=7 \
      -DCMAKE_INSTALL_LIBEXECDIR="%{_libexecdir}/%{name}" \
      -DIMPORTS_INSTALL_DIR="%{_libdir}/qt5/qml" \
      -DSESSION_COMMAND="%{_sysconfdir}/X11/xdm/Xsession" \
      -DBUILD_MAN_PAGES=ON \
      -DSTATE_DIR="%{_localstatedir}/lib/sddm" \
      -DDBUS_CONFIG_DIR=%{_datadir}/dbus-1/system.d \
      -DRUNTIME_DIR="/run/sddm" \
      -DPID_FILE="/run/sddm.pid" \
      -DLOGIN_DEFS_PATH:path="${LOGIN_DEFS_PATH}"
  %make_jobs

%install
  %kf5_makeinstall -C build

  # We don't want the example config.
  # However, we need to package the file so it does not end up being removed.
  echo > %{buildroot}%{_sysconfdir}/sddm.conf

  pushd %{buildroot}%{_datadir}/dbus-1/system.d
  mv org.freedesktop.DisplayManager.conf sddm_org.freedesktop.DisplayManager.conf
  popd

  install -Dm 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/X11/displaymanagers/%{name}
  install -Dm 0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d/00-general.conf
  install -Dm 0644 %{SOURCE3} %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d/10-theme.conf
  install -Dm 0644 %{SOURCE4} %{buildroot}%{_tmpfilesdir}/sddm.conf

  # Adjust paths to X session scripts in 00-general.conf
  sed -e 's-/usr/etc-%{?_distconfdir}%{!?_distconfdir:%{_sysconfdir}}-g' -i %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d/00-general.conf

  mkdir -p %{buildroot}%{_sysconfdir}/alternatives
  touch %{buildroot}%{_sysconfdir}/alternatives/default-displaymanager
  ln -s %{_sysconfdir}/alternatives/default-displaymanager %{buildroot}%{_prefix}/lib/X11/displaymanagers/default-displaymanager

  install -d %{buildroot}%{_rundir}/sddm
  install -d %{buildroot}%{_localstatedir}/lib/sddm
  install -d %{buildroot}%{_sysconfdir}/sddm.conf.d

  install -d %{buildroot}%{_sbindir}
  ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcsddm

  install -Dm 0644 %{SOURCE5} %{buildroot}%{_sysusersdir}/system-user-sddm.conf

  %fdupes %{buildroot}%{_datadir}/sddm

%pre -f sddm.pre
%service_add_pre sddm.service

%post
%service_add_post sddm.service
%{_bindir}/systemd-tmpfiles --create %{_tmpfilesdir}/sddm.conf
if [ $1 -eq 2 -a -f %{_sysconfdir}/sddm.conf ]; then
    # Avoid changing sddm.conf's timestamp if no modifications done
    tempconf="$(mktemp)"

    # SDDM 0.14.0 moved maui into the built-in resources
    # SDDM <= 0.15.0 had no system config dir, so we need to remove the
    # moved configuration options from the old single config file
    sed -e 's/^Current=maui$/Current=/g' \
        -e '\#^DisplayCommand=%{_sysconfdir}/X11/xdm/Xsetup#d' \
        -e '\#^MinimumVT=7$#d' \
        -e '\#^ServerPath=%{_bindir}/X$#d' \
        -e '\#^SessionCommand=%{_sysconfdir}/X11/xdm/Xsession$#d' \
        %{_sysconfdir}/sddm.conf > "${tempconf}"

    cmp -s "${tempconf}" "%{_sysconfdir}/sddm.conf" || cp "${tempconf}" "%{_sysconfdir}/sddm.conf"
    rm "${tempconf}"
fi
%{_sbindir}/update-alternatives --install %{_prefix}/lib/X11/displaymanagers/default-displaymanager \
  default-displaymanager %{_prefix}/lib/X11/displaymanagers/sddm 25

%preun
%service_del_preun sddm.service

%postun
# Don't restart on upgrades (boo#1161826)
%if 0%{?suse_version} > 1500
%service_del_postun_without_restart sddm.service
%else
%service_del_postun -n sddm.service
%endif
[ -f %{_prefix}/lib/X11/displaymanagers/sddm ] || %{_sbindir}/update-alternatives \
  --remove default-displaymanager %{_prefix}/lib/X11/displaymanagers/sddm

%post branding-upstream
if [ $1 -eq 2 -a -f %{_sysconfdir}/sddm.conf ]; then
    # Avoid changing sddm.conf's timestamp if no modifications done
    tempconf="$(mktemp)"

    # SDDM <= 0.15.0 had no system config dir, so we need to remove the
    # theme configuration from the old single config file
    sed -e '/^Current=$/d' %{_sysconfdir}/sddm.conf > "${tempconf}"

    cmp -s "${tempconf}" "%{_sysconfdir}/sddm.conf" || cp "${tempconf}" "%{_sysconfdir}/sddm.conf"
    rm "${tempconf}"
fi
:

%post branding-openSUSE
if [ $1 -eq 2 -a -f %{_sysconfdir}/sddm.conf ]; then
    # Avoid changing sddm.conf's timestamp if no modifications done
    tempconf="$(mktemp)"

    # Upgrade from previous theme name
    # SDDM <= 0.15.0 had no system config dir, so we need to remove the
    # theme configuration from the old single config file
    sed -e 's/^Current=breeze$/Current=breeze-openSUSE/g' \
        -e 's/^Current=maui$/Current=breeze-openSUSE/g' \
        -e '/^Current=breeze-openSUSE$/d' \
        -e '/^CursorTheme=breeze_cursors$/d' %{_sysconfdir}/sddm.conf > "${tempconf}"

    cmp -s "${tempconf}" "%{_sysconfdir}/sddm.conf" || cp "${tempconf}" "%{_sysconfdir}/sddm.conf"
    rm "${tempconf}"
fi
:

%files
%license LICENSE*
%doc README*
%config(noreplace) %{_sysconfdir}/sddm.conf
%dir %{_sysconfdir}/sddm.conf.d/
%config %{_sysconfdir}/pam.d/sddm
%config %{_sysconfdir}/pam.d/sddm-autologin
%config %{_sysconfdir}/pam.d/sddm-greeter
%{_datadir}/dbus-1/system.d/sddm_org.freedesktop.DisplayManager.conf
%dir %{_prefix}/lib/X11/displaymanagers/
%{_prefix}/lib/X11/displaymanagers/%{name}
%{_prefix}/lib/X11/displaymanagers/default-displaymanager
%ghost %{_sysconfdir}/alternatives/default-displaymanager
%{_bindir}/sddm
%{_bindir}/sddm-greeter
%{_sbindir}/rcsddm
%{_libdir}/qt5/qml/
%dir %{_datadir}/sddm/
%dir %{_prefix}/lib/sddm/
%dir %{_prefix}/lib/sddm/sddm.conf.d/
%{_prefix}/lib/sddm/sddm.conf.d/00-general.conf
%dir %{_libexecdir}/sddm
%{_libexecdir}/sddm/sddm-helper
%{_datadir}/sddm/faces/
%{_datadir}/sddm/flags/
%{_datadir}/sddm/scripts/
%{_datadir}/sddm/themes/
%{_datadir}/sddm/translations/
%ghost %attr(711,sddm,sddm) %dir %{_rundir}/sddm
%ghost %attr(750,sddm,sddm) %dir %{_localstatedir}/lib/sddm
%{_mandir}/man*/sddm*%{ext_man}
%{_unitdir}/sddm.service
%{_sysusersdir}/system-user-sddm.conf
%{_tmpfilesdir}/sddm.conf

%files branding-openSUSE
%license LICENSE*
%doc README*
%{_prefix}/lib/sddm/sddm.conf.d/10-theme.conf

%files branding-upstream
%license LICENSE*
%doc README*

%changelog
