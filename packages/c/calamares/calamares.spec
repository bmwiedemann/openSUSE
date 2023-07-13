#
# spec file for package calamares
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


# Internal QML import
%global __requires_exclude qmlimport\\(calamares\\.slideshow.*

%define _sover  3
Name:           calamares
Version:        3.2.62
Release:        0
Summary:        Installer from a live CD/DVD/USB to disk
License:        GPL-3.0-or-later
Group:          System/Management
URL:            https://calamares.io/
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source2:        calamares.keyring
# new generic branding.desc with explanations in comments
Source3:        branding.desc
Source4:        %{name}-rpmlintrc
# .desktop file customizations to use kdesu from kde-cli-tools5 instead of Polkit pkexec
Patch0:         %{name}-desktop-file.patch
# adjust some default settings (default shipped .conf files) for openSUSE and openSUSE based appliances
Patch1:         3.2-packages.conf.patch
Patch2:         3.2-bootloader.conf.patch
Patch3:         3.2-show.qml.patch
Patch4:         3.2-settings.conf.patch
Patch5:         3.2.15-unpackfs.conf_Leap15.patch
Patch6:         3.2.15-configuring_autologin_in_sysconfig.patch
Patch7:         3.2-removeuser.conf.patch
Patch8:         3.2-welcome.conf.patch
Patch9:         3.2-networkcfg.patch
Provides:       %{name}-libs%{_sover} = %{version}
Obsoletes:      %{name}-libs%{_sover} < %{version}
BuildRequires:  cmake >= 3.2
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules >= 0.0.13
BuildRequires:  gettext
# Calamares is only supported where live images (and GRUB) are. (rh#1171380)
BuildRequires:  grub2
BuildRequires:  hicolor-icon-theme
BuildRequires:  kconfig-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kparts-devel
BuildRequires:  kpmcore-devel >= 3.3
BuildRequires:  kservice-devel
BuildRequires:  libatasmart-devel
BuildRequires:  libboost_python3-devel
BuildRequires:  libpolkit-qt5-1-devel
BuildRequires:  libqt5-qtbase-devel >= 5.7
BuildRequires:  libqt5-qtdeclarative-devel >= 5.7
BuildRequires:  libqt5-qtsvg-devel >= 5.7
BuildRequires:  libqt5-qttools-devel >= 5.7
BuildRequires:  libqt5-qtwebengine-devel >= 5.7
BuildRequires:  parted-devel
BuildRequires:  pkg-config
BuildRequires:  python3-devel >= 3.3
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
Requires:       kde-cli-tools5
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

%package        webview
Summary:        Calamares webview module
Group:          System/Management
Requires:       %{name}%{?_isa} = %{version}

%description    webview
Optional webview module for the Calamares installer.

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
%cmake_kf5 -d build --  -DINSTALL_CONFIG=ON -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" -DSKIP_MODULES="plasmalnf" -DBoost_NO_BOOST_CMAKE=ON
make %{?_smp_mflags}

%install
%kf5_makeinstall -C build
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
%suse_update_desktop_file -r %{name} Qt System PackageManager

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
%{_datadir}/polkit-1/actions/com.github.%{name}.%{name}.policy
%endif
%{_libdir}/lib%{name}.so.*
%{_libdir}/lib%{name}ui.so.*
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/lib%{name}.so
%{_libdir}/%{name}/modules/
%exclude %{_libdir}/%{name}/modules/webview/

%files lang -f %{name}-python.lang
#%%files -f %%{name}-dummypythonqt.lang

%files webview
%license LICENSES/GPL-3.0-or-later.txt
%{_datadir}/%{name}/modules/webview.conf
%{_libdir}/%{name}/modules/webview/

%files branding-upstream
%license LICENSES/GPL-3.0-or-later.txt
%{_datadir}/%{name}/settings.conf
%dir %{_datadir}/%{name}/branding/
%{_datadir}/%{name}/branding/default/
%{_datadir}/%{name}/modules/
%exclude %{_datadir}/%{name}/modules/webview.conf

%changelog
