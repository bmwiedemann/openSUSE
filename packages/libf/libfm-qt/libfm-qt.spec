#
# spec file for package libfm-qt
#
# Copyright (c) 2024 SUSE LLC
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


%define   _ver  14
%define  _name  libfm-qt6
Name:           libfm-qt
Version:        2.0.2
Release:        0
Summary:        Core library of PCManFM-Qt (Qt binding for libfm)
License:        BSD-3-Clause AND LGPL-2.1-or-later
URL:            https://github.com/lxqt/libfm-qt
Source0:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.18.0
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  qt6-gui-private-devel
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Widgets) >= 6.6.0
BuildRequires:  cmake(lxqt-menu-data)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libmenu-cache) >= 1.1.0
BuildRequires:  pkgconfig(xcb)

%description
Libfm-Qt is a companion library providing components to build desktop file managers

%lang_package -n %{_name}

%package -n %{_name}-%{_ver}
Summary:        Libfm-qt libraries
Requires:       %{_name}-data >= %{version}
Provides:       %{_name} >= %{version}

%description -n %{_name}-%{_ver}
Libfm-Qt is a companion library providing components to build desktop file managers

%package -n %{_name}-data
Summary:        Data files for libfm library
BuildArch:      noarch

%description -n %{_name}-data
Provides data to be read by libfm-qt

%package -n %{_name}-devel
Summary:        Development files for libfm-qt
Requires:       %{_name}-%{_ver} = %{version}-%{release}

%description -n %{_name}-devel
Libfm-Qt libraries for development

%prep
%autosetup

%build
%cmake_qt6
%{qt6_build}

%install
%{qt6_install}

%find_lang %{name} --with-qt

%ldconfig_scriptlets -n %{_name}-%{_ver}

%check
%ctest

%files -n %{_name}-%{_ver}
%doc AUTHORS CHANGELOG README.md
%{_libdir}/%{_name}.so.*
%license LICENSE

%files -n %{_name}-data
%dir %{_datadir}/%{_name}
%{_datadir}/%{_name}/archivers.list
%{_datadir}/%{_name}/terminals.list
%{_datadir}/mime/packages/%{_name}-mimetypes.xml

%files -n %{_name}-devel
%dir %{_datadir}/cmake/fm-qt6
%{_includedir}/%{_name}/
%{_libdir}/%{_name}.so
%{_libdir}/pkgconfig/%{_name}.pc
%{_datadir}/cmake/fm-qt6/fm-qt6-config-version.cmake
%{_datadir}/cmake/fm-qt6/fm-qt6-config.cmake
%{_datadir}/cmake/fm-qt6/fm-qt6-targets-*.cmake
%{_datadir}/cmake/fm-qt6/fm-qt6-targets.cmake
%license LICENSE.BSD-3-Clause

%files -n %{_name}-lang -f %{name}.lang
%dir %{_datadir}/%{_name}/translations/
%if 0%{?sle_version}
%{_datadir}/%{_name}/translations/%{name}_???.qm
%endif

%changelog
