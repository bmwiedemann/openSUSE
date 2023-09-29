#
# spec file for package sddm
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


# Packaging for Qt 5 and Qt 6 flavors:
# The daemon using Qt 5 can use sddm-greeter-qt6 and vice versa,
# the only restriction is that the Qt X daemon defaults to run sddm-greeter-qtX
# so that should be treated as a hard requirement. The default flavor builds
# daemon and greeter with Qt 5 while the qt6 flavor builds both with Qt 6:
# sddm builds sddm, sddm-greeter-qt5, sddm-branding-{upstream,openSUSE}
# sddm:qt6 builds sddm-qt6, sddm-greeter-qt6, sddm-qt6-branding-upstream
# There is a PR pending (#1790) to build both greeters in one go, but here we
# build them separately to allow separation with _multibuild flavors.

%if "@BUILD_FLAVOR@" == "qt6"
%global qt6 1
%global qtver 6
%else
%global qt6 0
%global qtver 5
%endif

# The .spec file name has to match the first Name:
%if !%qt6
Name:           sddm
%else
Name:           sddm-qt6
%endif
Version:        0.20.0
Release:        0
Summary:        QML-based display manager (Qt%{qtver})
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            https://github.com/sddm/sddm
Source:         https://github.com/sddm/sddm/archive/v%{version}/sddm-%{version}.tar.gz
Source1:        X11-displaymanagers-sddm
# Distro configs
Source10:       00-general.conf
Source11:       10-theme.conf
# Use kwin_wayland for DisplayServer=wayland.
# Adapted from https://invent.kde.org/plasma/plasma-workspace/-/blob/Plasma/5.27/sddm-wayland-session/plasma-wayland.conf
Source12:       11-kwin_wayland.conf
# PAM configuration
Source20:       sddm.pam
Source21:       sddm-autologin.pam
Source22:       sddm-greeter.pam
# Patch0-100: PATCH-FIX-UPSTREAM
# https://github.com/sddm/sddm/pull/1746
Patch0:         0001-Session-Parse-.desktop-files-manually-again.patch
# https://github.com/sddm/sddm/pull/1753
Patch1:         0001-greeter-Look-at-WAYLAND_DISPLAY-for-platform-detecti.patch
Patch2:         0002-Ignore-InputMethod-qtvirtualkeyboard-on-wayland.patch
# https://github.com/sddm/sddm/pull/1792
Patch3:         0001-Drop-unnecessary-ECM-dependency-and-dead-uninstall-t.patch
# https://github.com/sddm/sddm/pull/1789
Patch4:         0002-Make-sddm-greeter-for-Qt-5-and-Qt-6-coinstallable.patch
Patch5:         0003-Let-themes-specify-the-used-version-of-Qt.patch
# Patch100-?: PATCH-FIX-OPENSUSE
Patch101:       0001-Write-the-daemon-s-PID-to-a-file-on-startup.patch
Patch102:       0001-Set-XAUTHLOCALHOSTNAME-in-sessions.patch
Patch103:       0001-Read-the-DISPLAYMANAGER_AUTOLOGIN-value-from-sysconf.patch
# sddm has some rudimentary support for plymouth handling, which only works with plymouth-quit.service
# (the servce is not enabled on openSUSE). For users of sddm.service, we need to issue plymouth quit command by hand in this case
Patch104:       sddm-service-handle-plymouth.patch
Patch107:       0003-Leave-duplicate-symlinks-out-of-the-SessionModel.patch
BuildRequires:  cmake
BuildRequires:  fdupes
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc10-PIE
BuildRequires:  gcc10-c++
%endif
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
# Autodetect UID_MIN and UID_MAX from /etc/login.defs
BuildRequires:  shadow
BuildRequires:  python3-docutils
BuildRequires:  sysuser-tools
%if %qt6
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickTest)
BuildRequires:  cmake(Qt6Test)
%else
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickTest)
BuildRequires:  cmake(Qt5Test)
%endif
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xcb-xkb)
%systemd_requires
%sysusers_requires
BuildRequires:  update-alternatives
Requires(post): %{_sbindir}/update-alternatives
Requires(postun):%{_sbindir}/update-alternatives
Requires:       %{name}-branding = %{version}
Requires:       sddm-greeter-qt%{qtver} = %{version}
Requires:       xdm
%if %qt6
Provides:       sddm = %{version}
# Most themes use Qt 5, just always provide support for now.
Requires:       sddm-greeter-qt5
Conflicts:      sddm
%else
Provides:       sddm-qt5 = %{version}
# Merged the -lang package back into the main package
Provides:       sddm-lang = %{version}
Obsoletes:      sddm-lang < %{version}
%endif

%description
SDDM is a display manager for X11 and Wayland. It uses technologies like
QtQuick, which gives the designer the ability to create animated user
interfaces.

%package -n sddm-greeter-qt%{qtver}
Summary:        SDDM Greeter for Qt%{qtver} themes
Group:          System/GUI/KDE
Requires:       sddm = %{version}

%description -n sddm-greeter-qt%{qtver}
This package provides the SDDM frontend for themes using Qt %qtver.

%package branding-openSUSE
Summary:        openSUSE branding for SDDM (Qt%{qtver})
Group:          System/GUI/KDE
BuildArch:      noarch
Requires:       %{name} = %{version}
Requires:       sddm-theme-openSUSE
%if %qt6
# Make installcheck happy: There needs to be a direct conflict,
# not just via sddm-qt6-branding-foo -> sddm-qt6 <-> sddm-branding-foo -> sddm
Conflicts:      sddm-branding
%else
# See 11-kwin_wayland.conf
Requires:       kwin5 >= 5.26.90
Supplements:    (plasma5-workspace and branding-openSUSE)
%endif
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}

%description branding-openSUSE
This package provides the openSUSE branding for SDDM.

%package branding-upstream
Summary:        Upstream branding for SDDM (Qt%{qtver})
Group:          System/GUI/KDE
BuildArch:      noarch
Requires:       %{name} = %{version}
Supplements:    (%{name} and branding-upstream)
%if %qt6
# Make installcheck happy: There needs to be a direct conflict,
# not just via sddm-qt6-branding-foo -> sddm-qt6 <-> sddm-branding-foo -> sddm
Conflicts:      sddm-branding
%endif
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}

%description branding-upstream
This package provides upstream branding for SDDM.

%prep
%autosetup -p1 -n sddm-%{version}

%build
LOGIN_DEFS_PATH="%{_sysconfdir}/login.defs"
[ -e "$LOGIN_DEFS_PATH" ] || LOGIN_DEFS_PATH="%{_distconfdir}/login.defs"

# SDDM_INITIAL_VT does not work for X: https://github.com/sddm/sddm/issues/1650
%cmake \
      -DBUILD_WITH_QT6:BOOL=%{qt6} \
      -DCMAKE_INSTALL_LIBEXECDIR="%{_libexecdir}/sddm" \
      -DSESSION_COMMAND="%{_sysconfdir}/X11/xdm/Xsession" \
      -DBUILD_MAN_PAGES=ON \
      -DSTATE_DIR="%{_localstatedir}/lib/sddm" \
      -DDBUS_CONFIG_DIR=%{_datadir}/dbus-1/system.d \
      -DRUNTIME_DIR="/run/sddm" \
      -DPID_FILE="/run/sddm.pid" \
      -DLOGIN_DEFS_PATH:path="${LOGIN_DEFS_PATH}" \
%if 0%{?suse_version} <= 1500
      -DCMAKE_C_COMPILER:STRING=gcc-10 \
      -DCMAKE_CXX_COMPILER:STRING=g++-10 \
%endif

  %cmake_build

%install
  %cmake_install

  pushd %{buildroot}%{_datadir}/dbus-1/system.d
  mv org.freedesktop.DisplayManager.conf sddm_org.freedesktop.DisplayManager.conf
  popd

  install -Dm 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/X11/displaymanagers/sddm
  install -Dm 0644 %{SOURCE10} %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d/00-general.conf
  # Adjust paths to X session scripts in 00-general.conf
  sed -e 's-/usr/etc-%{?_distconfdir}%{!?_distconfdir:%{_sysconfdir}}-g' -i %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d/00-general.conf
  %if !%qt6
    install -Dm 0644 %{SOURCE11} %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d/10-theme.conf
    install -Dm 0644 %{SOURCE12} %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d/11-kwin_wayland.conf
  %endif

  # Install PAM config
  rm -r %{buildroot}%{_sysconfdir}/pam.d # Remove sddm's config, for debian only
  pam_dest="%{?_pam_vendordir}%{!?_pam_vendordir:%{_sysconfdir}/pam.d}"
  install -Dm 0644 %{SOURCE20} %{buildroot}${pam_dest}/sddm
  install -Dm 0644 %{SOURCE21} %{buildroot}${pam_dest}/sddm-autologin
  install -Dm 0644 %{SOURCE22} %{buildroot}${pam_dest}/sddm-greeter

  # Make it compatible on older systems
  %if 0%{?suse_version} < 1550
    sed -i'' '/postlogin-/d' %{buildroot}${pam_dest}/*
  %endif

  mkdir -p %{buildroot}%{_sysconfdir}/alternatives
  touch %{buildroot}%{_sysconfdir}/alternatives/default-displaymanager
  ln -s %{_sysconfdir}/alternatives/default-displaymanager %{buildroot}%{_prefix}/lib/X11/displaymanagers/default-displaymanager

  install -d %{buildroot}%{_rundir}/sddm
  install -d %{buildroot}%{_localstatedir}/lib/sddm
  install -d %{buildroot}%{_sysconfdir}/sddm.conf.d

  install -d %{buildroot}%{_sbindir}
  ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcsddm

  %sysusers_generate_pre %{buildroot}%{_sysusersdir}/sddm.conf sddm sddm.conf

  %fdupes %{buildroot}%{_datadir}/sddm

%check
  %ctest

%pre -f sddm.pre
%service_add_pre sddm.service
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in pam.d/sddm pam.d/sddm-autologin pam.d/sddm-greeter ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif
# Previous versions owned /etc/sddm.conf, on upgrade it will be moved to .rpmsave if it was changed
# on disk. To keep the user configuration intact, it has to be moved back in posttrans.
# This also works for switching between sddm and sddm-qt6 in one transaction.
# However, if both /etc/sddm.conf and /etc/sddm.conf.rpmsave exist already, there are special cases:
# 1. /etc/sddm.conf was not changed on disk. It will be deleted instead of renamed to .rpmsave.
#    The posttrans script would rename the *old* .rpmsave file, restoring some ancient config.
# 2. /etc/sddm.conf was changed. The old .rpmsave file will be overwritten.
# Avoid this by moving any preexisting .rpmsave to .rpmsave.old. There is no rename back though,
# to prevent that every upgrade of the package renames it back and forth...
if [ -f %{_sysconfdir}/sddm.conf.rpmsave ]; then
    mv -v %{_sysconfdir}/sddm.conf.rpmsave %{_sysconfdir}/sddm.conf.rpmsave.old
fi

%post
%service_add_post sddm.service
%{_bindir}/systemd-tmpfiles --create %{_tmpfilesdir}/sddm.conf
%{_sbindir}/update-alternatives --install %{_prefix}/lib/X11/displaymanagers/default-displaymanager \
  default-displaymanager %{_prefix}/lib/X11/displaymanagers/sddm 25

%posttrans
%if 0%{?suse_version} > 1500
# Migration to /usr/lib/pam.d/, restore just created .rpmsave
for i in pam.d/sddm pam.d/sddm-autologin pam.d/sddm-greeter; do
    [ -f %{_sysconfdir}/${i}.rpmsave ] && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} || :
done
%endif
# See the pre script above
if [ -f %{_sysconfdir}/sddm.conf.rpmsave ] && ! [ -f %{_sysconfdir}/sddm.conf ]; then
    mv %{_sysconfdir}/sddm.conf.rpmsave %{_sysconfdir}/sddm.conf
fi

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

%files
%license LICENSE*
%doc README*
%dir %{_sysconfdir}/sddm.conf.d/
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/sddm
%{_pam_vendordir}/sddm-autologin
%{_pam_vendordir}/sddm-greeter
%else
%config %{_sysconfdir}/pam.d/sddm
%config %{_sysconfdir}/pam.d/sddm-autologin
%config %{_sysconfdir}/pam.d/sddm-greeter
%endif
%{_datadir}/dbus-1/system.d/sddm_org.freedesktop.DisplayManager.conf
%dir %{_prefix}/lib/X11/displaymanagers/
%{_prefix}/lib/X11/displaymanagers/sddm
%{_prefix}/lib/X11/displaymanagers/default-displaymanager
%ghost %{_sysconfdir}/alternatives/default-displaymanager
%{_bindir}/sddm
%{_sbindir}/rcsddm
%dir %{_datadir}/sddm/
%dir %{_prefix}/lib/sddm/
%dir %{_prefix}/lib/sddm/sddm.conf.d/
%{_prefix}/lib/sddm/sddm.conf.d/00-general.conf
%dir %{_libexecdir}/sddm
%{_libexecdir}/sddm/sddm-helper
%{_libexecdir}/sddm/sddm-helper-start-wayland
%{_libexecdir}/sddm/sddm-helper-start-x11user
%{_datadir}/sddm/faces/
%{_datadir}/sddm/flags/
%{_datadir}/sddm/scripts/
%{_datadir}/sddm/themes/
%ghost %attr(711,root,root) %dir %{_rundir}/sddm
%ghost %attr(750,sddm,sddm) %dir %{_localstatedir}/lib/sddm
%{_mandir}/man*/sddm*%{ext_man}
%{_unitdir}/sddm.service
%{_sysusersdir}/sddm.conf
%{_tmpfilesdir}/sddm.conf

%files -n sddm-greeter-qt%{qtver}
%if %qtver == 5
%{_bindir}/sddm-greeter
%else
%{_bindir}/sddm-greeter-qt%{qtver}
%endif
%{_libdir}/qt%{qtver}/qml/
%{_datadir}/sddm/translations-qt%{qtver}/

# No openSUSE branding for Qt 6 yet
%if !%qt6
%files branding-openSUSE
%license LICENSE*
%doc README*
%{_prefix}/lib/sddm/sddm.conf.d/10-theme.conf
%{_prefix}/lib/sddm/sddm.conf.d/11-kwin_wayland.conf
%endif

%files branding-upstream
%license LICENSE*
%doc README*

%changelog
