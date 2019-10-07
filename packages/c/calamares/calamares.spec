#
# spec file for package calamares
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://github.com/calamares/calamares/issues

%define _sover  3
Name:           calamares
Version:        3.1.11
Release:        0
Summary:        Installer from a live CD/DVD/USB to disk
Group:          System/Management
License:        GPL-3.0
Url:            http://calamares.io/
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# new generic branding.desc with explanations in comments
Source1:        branding.desc
Source2:        %{name}-rpmlintrc
# .desktop file customizations for openSUSE
Patch0:         %{name}-desktop-file.patch
# adjust some default settings (default shipped .conf files) for openSUSE and openSUSE based appliances
Patch1:         3.1.11-packages.conf.patch
Patch2:         2.4-bootloader.conf.patch
Patch3:         2.4-services.conf.patch
Patch4:         3.0-settings.conf.patch
%if %{?suse_version} >= 1500
Patch5:         3.1.4-unpackfs.conf_Leap15.patch
%else
Patch5:         3.1.4-unpackfs.conf.patch
%endif
Patch6:         3.1.2-configuring_autologin_in_sysconfig.patch
Patch7:         2.4-removeuser.conf.patch
Patch8:         3.1.1-welcome.conf.patch
Patch9:         3.1-show.qml.patch
Provides:       %{name}-libs%{_sover} = %{version}
Obsoletes:      %{name}-libs%{_sover} < %{version}
%if %{?suse_version} >= 1500
BuildRequires:  libboost_python3-devel
%else
BuildRequires:  boost-devel >= 1.59.0
%endif
BuildRequires:  cmake >= 2.8.12
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
BuildRequires:  kpmcore-devel >= 3.0.2
BuildRequires:  kservice-devel
BuildRequires:  libatasmart-devel
BuildRequires:  libpolkit-qt5-1-devel
BuildRequires:  libqt5-qtbase-devel >= 5.4
BuildRequires:  libqt5-qtdeclarative-devel >= 5.4
BuildRequires:  libqt5-qtsvg-devel >= 5.4
BuildRequires:  libqt5-qttools-devel >= 5.4
BuildRequires:  libqt5-qtwebengine-devel >= 5.6
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
Requires:       kpmcore >= 3.0.2
Requires:       ntfsprogs
Requires:       os-prober
Requires:       parted
#Requires:       polkit
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
# C++11
# Calamares needs at least gcc5
%if 0%{?sle_version} == 120200
BuildRequires:  gcc5-c++
%endif
%if 0%{?sle_version} == 120300
BuildRequires:  gcc7-c++
%endif
%if %{?suse_version} > 1320
BuildRequires:  gcc-c++ >= 5.0
%endif
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
Group:          System/Management
# This theme is nor pure upstream, nor specific to openSUSE,
# but is close to upstream
Supplements:    packageand(%name:branding-upstream)
#Supplements:    packageand(%%{name}:branding-openSUSE)
Conflicts:      otherproviders(%{name}-branding)
Provides:       %name-branding = %{version}
BuildArch:      noarch

%description branding-upstream
This package provides configuration files and "look and feel" for
Calamares installer. "Look and feel" files are simplified upstream files.
Meanwhile configuration files adopted to work with openSUSE and SUSE
based custom appliances.

%prep
%setup -q -n %{name}-%{version}
cp -f %{SOURCE1} src/branding/default/
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
# fix shebang 
find . -wholename "./src/modules/*/main.py" -exec sed -re "1s/^#\!\/usr\/bin\/env python3/#\!\/usr\/bin\/python3/" -i {} \;

%build
# Calamares needs at least gcc5
%if 0%{?sle_version} == 120200
export CC=gcc-5
export CXX=g++-5
%endif
%if 0%{?sle_version} == 120300
export CC=gcc-7
export CXX=g++-7
%endif
%cmake_kf5 -d build --  -DCMAKE_INSTALL_PREFIX=%{_prefix} -DCMAKE_BUILD_TYPE:STRING="RelWithDebInfo" -DSKIP_MODULES="plasmalnf" -DBoost_NO_BOOST_CMAKE=ON
make %{?_smp_mflags}

%install
# Calamares needs at least gcc5
%if 0%{?sle_version} == 120200
export CC=gcc-5
export CXX=g++-5
%endif
%if 0%{?sle_version} == 120300
export CC=gcc-7
export CXX=g++-7
%endif
%kf5_makeinstall -C build
# if we don't want polkit (and you want use xdg-su instead)
rm -fr %{buildroot}%{_datadir}/polkit-1
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
%suse_update_desktop_file -r %{name} Qt System PackageManager

# localization
%find_lang %{name}-python
%find_lang %{name}-dummypythonqt

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
%files -f %{name}-python.lang -f %{name}-dummypythonqt.lang
%doc LICENSE AUTHORS
%{_mandir}/*/*
%{_bindir}/%{name}
%{_sysconfdir}/%{name}/
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/qml/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
# if we want polkit (you can use xdg-su instead)
#%%{_datadir}/polkit-1/actions/com.github.%%{name}.%%{name}.policy
%{_libdir}/lib%{name}.so.*
%{_libdir}/lib%{name}ui.so.*
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/lib%{name}.so
%{_libdir}/%{name}/modules/
%exclude %{_libdir}/%{name}/modules/webview/

%files webview
%{_datadir}/%{name}/modules/webview.conf
%{_libdir}/%{name}/modules/webview/

%files branding-upstream
%doc LICENSE
%{_datadir}/%{name}/settings.conf
%dir %{_datadir}/%{name}/branding/
%{_datadir}/%{name}/branding/default/
%{_datadir}/%{name}/modules/
%exclude %{_datadir}/%{name}/modules/webview.conf

%changelog
