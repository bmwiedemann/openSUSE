#
# spec file for package colord-kde
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Summary:        KDE interfaces and session daemon to colord
License:        GPL-2.0+
Group:          System/GUI/KDE
Name:           colord-kde
Version:        0.5.0
Release:        0
Source0:        http://download.kde.org/stable/%{name}/%{version}/src/%{name}-%{version}.tar.xz
Url:            https://projects.kde.org/projects/playground/graphics/colord-kde
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
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
BuildRequires:  liblcms2-devel
BuildRequires:  plasma-framework-devel
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xrandr)
Requires:       colord
# Enable calibrate functional if gnome-color-manager installed
Suggests:       gnome-color-manager
Recommends:     %{name}-lang

%description
Colord-kde provides KCM module and KDE daemon module for colord support.

%lang_package

%prep
%setup -q

%build
%cmake_kf5 -d build
%make_jobs

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%find_lang %{name}

%files
%defattr(-,root,root)
%doc COPYING MAINTAINERS TODO
%{_kf5_bindir}/%{name}-icc-importer
%{_kf5_applicationsdir}/colordkdeiccimporter.desktop
%{_kf5_plugindir}/*.so
%{_kf5_servicesdir}/kcm_colord.desktop
%dir %{_kf5_servicesdir}/kded
%{_kf5_servicesdir}/kded/colord.desktop

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
