#
# spec file for package libkdecoration2
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


%global sover 5
%global private_sover 9
%define lname           libkdecorations2-%{sover}
%define lname_private   libkdecorations2private%{private_sover}
%bcond_without released
Name:           libkdecoration2
Version:        5.26.5
Release:        0
Summary:        KDE's window decorations library
License:        GPL-2.0-or-later
Group:          System/GUI/KDE
URL:            http://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/kdecoration-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/kdecoration-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= 5.98.0
BuildRequires:  kf5-filesystem
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(Qt5Core) >= 5.15.0
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Test)

%description
Plugin based library to create window decorations.

%package devel
Summary:        KDE's window decorations library (development package)
Group:          Development/Libraries/C and C++
Requires:       %{lname_private} = %{version}
Requires:       %{lname} = %{version}
Requires:       cmake(Qt5Gui)
Obsoletes:      libkdecorations-devel < 5.2

%description devel
Development files belonging to kdecoration,
plugin based library to create window decorations.

%package -n %{lname}
Summary:        KDE's window decorations library
Group:          System/GUI/KDE
Obsoletes:      libkdecorations5 < 5.2
Recommends:     %{lname}-lang

%description -n %{lname}
Plugin based library to create window decorations.

%package -n %{lname_private}
Summary:        KDE's window decorations library
Group:          System/GUI/KDE

%description -n %{lname_private}
Plugin based library to create window decorations.

%lang_package -n %{lname}

%prep
%setup -q -n kdecoration-%{version}

%build
  %cmake_kf5 -d build
  %cmake_build

%install
  %kf5_makeinstall -C build
  %if %{with released}
    %find_lang %{name} --all-name
  %endif

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig
%post -n %{lname_private} -p /sbin/ldconfig
%postun -n %{lname_private} -p /sbin/ldconfig

%files -n %{lname}
%license LICENSES/*
%{_kf5_libdir}/libkdecorations2.so.%{sover}
%{_kf5_libdir}/libkdecorations2.so.%{sover}.*

%files -n %{lname_private}
%license LICENSES/*
%{_kf5_libdir}/libkdecorations2private.so.%{private_sover}
%{_kf5_libdir}/libkdecorations2private.so.%{sover}.*

%files devel
%license LICENSES/*
%{_kf5_libdir}/libkdecorations2.so
%{_kf5_libdir}/libkdecorations2private.so
%{_kf5_libdir}/cmake/KDecoration2/
%{_kf5_prefix}/include/KDecoration2/
%{_kf5_includedir}/

%if %{with released}
%files -n %{lname}-lang -f %{name}.lang
%license LICENSES/*
%endif

%changelog
