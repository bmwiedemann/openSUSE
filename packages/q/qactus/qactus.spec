#
# spec file for package qactus
#
# Copyright (c) 2020 SUSE LLC
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


%global libmajor 2
%global libprefix libqobs
%global libname %{libprefix}%{libmajor}
%global devname %{libprefix}-devel

Name:           qactus
Version:        2.0.2
Release:        0
Summary:        A GUI client for OBS
License:        GPL-2.0-only OR GPL-3.0-only
Group:          Development/Tools/Building
URL:            https://github.com/javierllorente/qactus
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.5
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Widgets)
# Needed to ensure Qt5Keychain can be used properly
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Keychain)
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description
A Qt-based Open Build Service (OBS) client featuring a browser, request management and more

%package -n %{libname}
Summary:        A Qt-based OBS library
Group:          System/Libraries

%description -n %{libname}
A library for interacting with the Open Build Service (OBS)

%package -n %{devname}
Summary:        Development files for %{libprefix}
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{?_isa} = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{libprefix}, a Qt-based
Open Build Service (OBS) library

%prep
%setup -q

%build
%cmake
%make_build

%install
%make_install -C build

%suse_update_desktop_file %{name}

%post
%desktop_database_post

%postun
%desktop_database_postun

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%doc README.md
%license COPYING gpl-*.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png

%files -n %{libname}
%license COPYING gpl-*.txt
%{_libdir}/%{libprefix}.so.%{libmajor}
%{_libdir}/%{libprefix}.so.%{libmajor}.*

%files -n %{devname}
%{_libdir}/%{libprefix}.so
%{_libdir}/pkgconfig/%{libprefix}.pc
%{_includedir}/qobs

%changelog
