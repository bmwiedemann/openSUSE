#
# spec file for package deepin-control-center
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


%define _name dde-control-center
%if 0%{?is_opensuse}
    %define  distribution  openSUSE-Edition
%else
    %define  distribution  SUSE-Edition
%endif

Name:           deepin-control-center
Version:        5.5.143
Release:        0
Summary:        New control center for Linux Deepin
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dde-control-center
Source0:        https://github.com/linuxdeepin/dde-control-center/archive/%{version}/%{_name}-%{version}.tar.gz
# PATCH-FOR-OPENSUSE deepin-control-center-no-user-experience.patch hillwood@opensuse.org
# Disable User Experience Program on openSUSE
Patch0:         %{name}-no-user-experience.patch
# PATCH-FOR-OPENSUSE systeminfo-deepin-icon.patch hillwood@opensuse.org - Use deepin icons instead of UOS
Patch1:         systeminfo-deepin-icon.patch
# PATCH-FOR-OPENSUSE remove-auth.patch
# Patch3:         remove-auth.patch
# PATCH-FOR-UPSTREAM fix-include-directories.patch hillwood@opensuse.org - Fix boo#1200959
# Patch4:         fix-include-directories.patch
Group:          System/GUI/Other
BuildRequires:  cmake
BuildRequires:  deepin-desktop-base
BuildRequires:  deepin-pw-check-devel
BuildRequires:  desktop-file-utils
BuildRequires:  dtkcommon >= 5.5.20
BuildRequires:  dtkcore
BuildRequires:  fdupes
BuildRequires:  gtest
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libQt5Widgets-private-headers-devel
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtwayland-private-headers-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(KF5NetworkManagerQt)
BuildRequires:  cmake(KF5Wayland)
BuildRequires:  cmake(PolkitQt5-1)
BuildRequires:  cmake(Qt5XkbCommonSupport)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5WaylandClient)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(dareader)
BuildRequires:  pkgconfig(dde-network-utils)
BuildRequires:  pkgconfig(dframeworkdbus) >= 2.0
BuildRequires:  pkgconfig(dtkcore) >= 5.0.0
BuildRequires:  pkgconfig(dtkwidget) >= 5.0.0
BuildRequires:  pkgconfig(gsettings-qt)
BuildRequires:  pkgconfig(udisks2-qt5)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xkbcommon)
Requires:       deepin-account-faces
Requires:       deepin-api
Requires:       deepin-daemon
Requires:       deepin-start
Requires:       libdeepin_pw_check1
Requires:       libqt5-qdbus
Requires:       qt5integration
Requires:       redshift
Recommends:     %{name}-data
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The deepin-control-center is the control panel of Deepin Desktop.

%package data
Summary:        Data of deepin-control-center
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
The deepin-control-center is the control panel of Deepin Desktop.

deepin-control-center-data is the data of deepin-control-center.

%package devel
Summary:        Development tools for deepin-control-center
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}

%description devel
The deepin-control-center-devel package contains the header files and developer
docs for deepin control center.

%lang_package

%prep
%autosetup -p1 -n %{_name}-%{version}
sed -i 's|lrelease|lrelease-qt5|g' translate_generation.sh
sed -i 's/DESTINATION lib/DESTINATION ${CMAKE_INSTALL_LIBDIR}/g' src/frame/CMakeLists.txt
sed -i 's|qdbus|qdbus-qt5|g' com.deepin.dde.ControlCenter.service dde-control-center-wapper
sed -i '/set(VERSION/s|4.0|%{version}-%{distribution}|' abrecovery/CMakeLists.txt \
       src/develop-tool/CMakeLists.txt \
       src/frame/CMakeLists.txt \
       src/reboot-reminder-dialog/CMakeLists.txt

%build
%cmake -DDCC_DISABLE_GRUB=YES \
       -DDISABLE_SYS_UPDATE=YES \
       -DCC_DISABLE_FEEDBACK=YES \
       -DDISABLE_ACTIVATOR=YES \
       -DCC_DISABLE_LANGUAGE=YES \
       -DCVERSION=%{version}-%{distribution}

%cmake_build

%install
%cmake_install

sed -i 's/OnlyShowIn=/X-DEEPIN-OnlyShowIn/g' \
%{buildroot}%{_datadir}/applications/%{_name}.desktop
chmod -x %{buildroot}%{_datadir}/applications/%{_name}.desktop
%suse_update_desktop_file -r %{_name} Settings DesktopSettings X-SuSE-Core-System
rm -rf %{buildroot}%{_datadir}/polkit-1/actions/com.deepin.controlcenter.develop.policy
rm -rf %{buildroot}%{_datadir}/dman

%fdupes %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.md CHANGELOG.md docs/internaltest.md
%license LICENSE
%{_bindir}/%{_name}
%{_bindir}/%{_name}-wapper
%{_bindir}/abrecovery
%{_sysconfdir}/xdg/autostart/deepin-ab-recovery.desktop
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/dbus-1/services/*.service
%{_libdir}/libdccwidgets.so
%dir %{_prefix}/lib/dde-grand-search-daemon
%dir %{_prefix}/lib/dde-grand-search-daemon/plugins
%{_prefix}/lib/dde-grand-search-daemon/plugins/searcher
%dir %{_datadir}/%{_name}/
%{_datadir}/%{_name}/%{_name}.conf
%{_datadir}/glib-2.0/schemas/com.deepin.dde.control-center.gschema.xml
%dir %{_datadir}/dsg
%dir %{_datadir}/dsg/configs
# %dir %{_datadir}/dsg/configs/dde-control-center
%dir %{_datadir}/dsg/configs/org.deepin.dde.control-center
# %{_datadir}/dsg/configs/dde-control-center/*.json
%{_datadir}/dsg/configs/org.deepin.dde.control-center/*.json
# %{_datadir}/dsg/apps/dde-control-center
# %{_datadir}/polkit-1/actions/com.deepin.controlcenter.develop.policy

%files data
%defattr(-,root,root,-)
%{_datadir}/%{_name}/*db
%{_datadir}/dict/MainEnglishDictionary_ProbWL.txt

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{_name}
%{_libdir}/cmake/DdeControlCenter

%files lang
%defattr(-,root,root,-)
%{_datadir}/%{_name}/translations/

%changelog
