#
# spec file for package knemo
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2007-2009,2011,2012 Herbert Graeber
# Copyright (c) 2010 Pascal Bleser
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           knemo
Version:        0.7.7git.20170520T005915~f3afe2e
Release:        0
Summary:        The KDE Network Monitor
License:        GPL-2.0+
Group:          System/GUI/KDE
Url:            http://kde-apps.org/content/show.php/KNemo?content=12956
Source:         %{name}-%{version}.tar.xz
Source1:        knemo-rpmlintrc
Source2:        knemo-translations.tar.xz
BuildRequires:  extra-cmake-modules
BuildRequires:  kcmutils-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  kglobalaccel-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  ki18n-devel
BuildRequires:  kio-devel
BuildRequires:  knotifications-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  libiw-devel
BuildRequires:  libksysguard5-devel
BuildRequires:  libnl3-devel
BuildRequires:  update-desktop-files
BuildRequires:  wireless-tools
BuildRequires:  plasma-framework-devel
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
KNemo offers a network monitor similar to the one found in Windows. For every
network interface it displays an icon in the systray.

%lang_package

%prep
%setup -q -a 2
# build translations
echo "add_subdirectory( po )" >> CMakeLists.txt

%build
%cmake_kf5 -d build
%make_jobs

%install
%kf5_makeinstall -C build

%suse_update_desktop_file %{buildroot}%_kf5_applicationsdir/knemo.desktop Qt KDE System Monitor

%find_lang %{name} %{name}.lang
%find_lang kcm_%{name} %{name}.lang

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%{_kf5_bindir}/knemo
%{_kf5_servicesdir}/*.desktop
%{_kf5_plugindir}/*.so
%{_kf5_notifydir}/*rc
%{_kf5_applicationsdir}/*.desktop
%{_kf5_configdir}/autostart/*.desktop
%{_kf5_iconsdir}/hicolor/*/apps/knemo.*
%{_kf5_iconsdir}/hicolor/*/status/knemo*.*
%{_kf5_sharedir}/knemo/
%{_kf5_sharedir}/kconf_update/
%{_kf5_iconsdir}/breeze-dark/
%{_kf5_iconsdir}/breeze/
%{_kf5_iconsdir}/oxygen/scalable/status/*.svg
%{_kf5_plasmadir}/desktoptheme/

%files lang -f %{name}.lang
%doc COPYING

%changelog
