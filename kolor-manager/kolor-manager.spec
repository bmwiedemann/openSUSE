#
# spec file for package kolor-manager
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2010-2016 Kai-Uwe Behrmann <ku.b@gmx.de>
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


# These macros are not present on the target distribution and are provided explicitly here
%define make_jobs %{__make} %{?_smp_mflags} VERBOSE=1

Name:           kolor-manager
Url:            http://www.oyranos.org/kolormanager
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Colour Management Frontend for KDE
License:        BSD-2-Clause
Group:          System/GUI/KDE
Version:        1.1.0
Release:        0
Source:         %{name}_%{version}.orig.tar.bz2
Source1:        %{name}_%{version}-1.debian.tar.gz

Requires:       icc-examin
Requires:       oyranos
%if 0%{?suse_version}
Recommends:     oyranos-qcmsevents
%endif
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libOyranosSynnefo-devel
BuildRequires:  libXcm-devel >= 0.5.4
BuildRequires:  liboyranos-devel >= 0.9.6
%if 0%{?suse_version}
Recommends:     icc-examin
Recommends:     oyranos-qcmsevents
%endif
BuildRequires:  extra-cmake-modules
BuildRequires:  kcmutils-devel
BuildRequires:  kconfig-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kf5-filesystem
BuildRequires:  ki18n-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kio-devel
BuildRequires:  kitemviews-devel
BuildRequires:  knotifications-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  libQt5DBus-devel
BuildRequires:  libQt5Widgets-devel
BuildRequires:  plasma-framework-devel
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xrandr)

Patch:          patch-remove-icon-files.patch

%description
The KDE5 systemsettings modules provide cross desktop Oyranos Color Management System settings.

%prep
%setup -n %{name}-%{version} -q
%patch -p1

%build
%cmake_kf5 -d build
%make_jobs

%install
%cmake_install

%files
%defattr(-,root,root)
%doc README.md
%{_kf5_plugindir}/*.so
%{_kf5_servicesdir}/kcm_km*.desktop
%{_kf5_servicesdir}/settings-kolor-management.desktop

%changelog
