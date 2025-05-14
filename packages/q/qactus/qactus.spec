#
# spec file for package qactus
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2015-2025 Javier Llorente <javier@opensuse.org>
# Copyright (c) 2018 Neal Gompa <ngompa13@gmail.com>.
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


%global libmajor 3
%global libprefix libqobs
%global libname %{libprefix}%{libmajor}
%global devname %{libprefix}-devel

Name:           qactus
Version:        3.0.0
Release:        0
Summary:        A GUI client for OBS
License:        Apache-2.0
Group:          Development/Tools/Building
URL:            https://github.com/javierllorente/qactus
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.16
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description
A Qt-based Open Build Service (OBS) client featuring a browser, request
management and more.

%package -n %{libname}
Summary:        A Qt-based OBS library
Group:          System/Libraries

%description -n %{libname}
A library for interacting with the Open Build Service (OBS).

%package -n %{devname}
Summary:        Development files for %{libprefix}
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{libprefix}, a Qt-based
Open Build Service (OBS) library.

%prep
%autosetup -p1

%build
%cmake_qt6
%qt6_build

%install
%qt6_install

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%doc README.md
%license LICENSE NOTICE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%files -n %{libname}
%license LICENSE NOTICE
%{_libdir}/%{libprefix}.so.%{libmajor}
%{_libdir}/%{libprefix}.so.%{libmajor}.*

%files -n %{devname}
%{_libdir}/%{libprefix}.so
%{_libdir}/pkgconfig/%{libprefix}.pc
%{_includedir}/qobs

%changelog
