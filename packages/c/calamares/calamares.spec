#
# spec file for package calamares
#
# Copyright (c) 2026 SUSE LLC and contributors
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


# Internal QML import
%global __requires_exclude qmlimport\\(calamares\\.slideshow.*

%define _sover  3
Name:           calamares
Version:        3.4.0
Release:        0
Summary:        Installer from a live CD/DVD/USB to disk
License:        GPL-3.0-or-later
Group:          System/Management
URL:            https://calamares.io/
Source0:        https://codeberg.org/Calamares/%{name}/releases/download/v%{version}/calamares-%{version}.tar.gz
Source1:        https://codeberg.org/Calamares/%{name}/releases/download/v%{version}/calamares-%{version}.tar.gz.asc
# Keyring from https://codeberg.org/adridg.gpg
Source2:        calamares.keyring
# new generic branding.desc with explanations in comments
Source3:        branding.desc
Source4:        %{name}-rpmlintrc
# .desktop file customizations to use kdesu from kde-cli-tools5 instead of Polkit pkexec
Patch0:         %{name}-desktop-file.patch
# adjust some default settings (default shipped .conf files) for openSUSE and openSUSE based appliances
Patch1:         3.4-packages.conf.patch
Patch2:         3.4-bootloader.conf.patch
Patch3:         3.4-show.qml.patch
Patch4:         3.4-settings.conf.patch
Patch5:         3.4-unpackfs.conf_Leap15.patch
Patch6:         3.4-configuring_autologin_in_sysconfig.patch
Patch7:         3.4-removeuser.conf.patch
Patch8:         3.4-welcome.conf.patch
Patch9:         3.4-networkcfg.patch
Patch10:        3.4-dracut.conf.patch
Patch11:        3.4-partition.conf.patch
Provides:       %{name}-libs%{_sover} = %{version}
Obsoletes:      %{name}-libs%{_sover} < %{version}

# Compilation
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  qt6-macros
BuildRequires:  kf6-extra-cmake-modules

# QT6
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(PolkitQt6-1)

# KF6
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Package)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6WidgetsAddons)

# Plasma
BuildRequires:  cmake(Plasma)

BuildRequires:  cmake(KPMcore)

# Python
BuildRequires:  python3-devel >= 3.3
BuildRequires:  libboost_python3-devel
BuildRequires:  boost-devel
BuildRequires:  python3-PyYAML
BuildRequires:  python3-jsonschema

BuildRequires:  cmake(AppStreamQt)
BuildRequires:  libpwquality-devel
BuildRequires:  libxcrypt-devel

# Calamares is only supported where live images (and GRUB) are. (rh#1171380)
BuildRequires:  grub2
BuildRequires:  hicolor-icon-theme
BuildRequires:  libatasmart-devel
BuildRequires:  parted-devel
BuildRequires:  pkg-config
BuildRequires:  solid-devel
BuildRequires:  update-desktop-files
BuildRequires:  yaml-cpp-devel >= 0.5.1
Requires:       %name-branding >= 3
Requires:       NetworkManager
Requires:       console-setup
Requires:       coreutils
Requires:       dmidecode
Requires:       dosfstools
Requires:       dracut
Requires:       e2fsprogs
Requires:       gawk
Requires:       gptfdisk
Requires:       grub2
Requires:       kde-cli-tools6
Requires:       kpmcore >= 3.3
Requires:       ntfsprogs
Requires:       os-prober
Requires:       parted
%if 0%{?suse_version} > 1500
Requires:       polkit
%endif
Requires:       python3
Requires:       rsync
Requires:       shadow
Requires:       squashfs
Requires:       systemd
Requires:       upower
Requires:       util-linux
Requires:       xdg-utils
Requires:       xkbutils
Requires:       zypper
Requires:       dosfstools
Requires:       shadow
Requires:       efibootmgr
Recommends:     btrfsprogs
Recommends:     hfsutils
Recommends:     jfsutils
Recommends:     ntfs-3g
Recommends:     reiserfs
Recommends:     xfsprogs
%ifarch x86_64
# EFI currently only supported on x86_64
Requires:       grub2-efi
%endif

%description
Calamares is a distribution-independent installer framework, designed to install
from a live CD/DVD/USB environment to a hard disk. It includes a graphical
installation program based on Qt 5. Calamares can replace YaST2 Live Installer.

%package branding-upstream
Summary:        Branding for %{name}
# This theme is nor pure upstream, nor specific to openSUSE,
# but is close to upstream
Group:          System/Management
Supplements:    (%name and branding-upstream)
%if 0%{?sle_version} == 150000
Conflicts:      otherproviders(%{name}-branding)
%endif
%if 0%{?suse_version} > 1500
Conflicts:      %{name}-branding
%endif
Provides:       %name-branding = %{version}
BuildArch:      noarch

%description branding-upstream
This package provides configuration files and "look and feel" for
Calamares installer. "Look and feel" files are simplified upstream files.
Meanwhile configuration files adopted to work with openSUSE and SUSE
based custom appliances.

%lang_package

%prep
%autosetup -N
cp -f %{SOURCE3} src/branding/default/
%autopatch -p1
# fix shebang
find . -wholename "./src/modules/*/main.py" -exec sed -re "1s/^#\!\/usr\/bin\/env python3/#\!\/usr\/bin\/python3/" -i {} \;

%build
%cmake_kf6   -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" \
			 -DINSTALL_CONFIG=ON \
			 -DCMAKE_INSTALL_PREFIX=%{_prefix} \
			 -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
			 -DCMAKE_C_COMPILER_WORKS=1 \
			 -DCMAKE_CXX_COMPILER_WORKS=1 \
			 -DSKIP_MODULES="plasmalnf" \
			 -DWITH_QT6:BOOL=ON \
			 -DBUILD_TESTING:BOOL=OFF \
			 %{nil}

# make %{?_smp_mflags}
cmake --build build

%install
DESTDIR=%{buildroot} cmake --install build
# if we don't want polkit (and you want use kdesu from kde-cli-tools5 instead)
%if 0%{?suse_version} == 1500
rm -fr %{buildroot}%{_datadir}/polkit-1
%endif
# add executable bits
chmod +x %{buildroot}%{_libdir}/%{name}/modules/*/main.py
chmod +x %{buildroot}%{_libdir}/%{name}/modules/initramfscfg/encrypt_hook*
# own the local settings directories
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/modules
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/branding
# remove -devel files: calamares libraries are not expected to be used in other programs
rm -fr %{buildroot}%{_includedir}/lib%{name}/
rm -f  %{buildroot}%{_libdir}/lib%{name}.so
rm -f  %{buildroot}%{_libdir}/lib%{name}ui.so
rm -fr %{buildroot}%{_libdir}/cmake/Calamares/
# fix exec bits
chmod +x %{buildroot}%{_libdir}/%{name}/modules/unpackfs/runtests.sh

# localization
%find_lang %{name}-python
#%%find_lang %%{name}-dummypythonqt

%post
%desktop_database_post
/sbin/ldconfig

%postun
%desktop_database_postun
/sbin/ldconfig

# Non-standart placement of files comes from upstream.
# Authors of Calamares already asked to install libs
# in the standard search path, see responses of authors in
# https://github.com/calamares/calamares/issues/729

%files
%license LICENSES/GPL-3.0-or-later.txt
%doc AUTHORS
%{_mandir}/*/*
%{_bindir}/%{name}
%{_sysconfdir}/%{name}/
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/qml/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
# if we want polkit (you can use kdesu from kde-cli-tools5 instead)
%if 0%{?suse_version} > 1500
%{_datadir}/polkit-1/actions/io.%{name}.%{name}.policy
%endif
%{_libdir}/lib%{name}.so.*
%{_libdir}/lib%{name}ui.so.*
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/lib%{name}.so
%{_libdir}/%{name}/modules/

%files lang -f %{name}-python.lang
#%%files -f %%{name}-dummypythonqt.lang

%files branding-upstream
%license LICENSES/GPL-3.0-or-later.txt
%{_datadir}/%{name}/settings.conf
%dir %{_datadir}/%{name}/branding/
%{_datadir}/%{name}/branding/default/
%{_datadir}/%{name}/modules/

%changelog
