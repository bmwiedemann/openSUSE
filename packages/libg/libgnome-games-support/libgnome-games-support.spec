#
# spec file for package libgnome-games-support
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


%define sover 4
%define api 2

Name:           libgnome-games-support
Version:        2.0.0
Release:        0
Summary:        Internal support library for GNOME games
License:        LGPL-3.0-or-later
Group:          Development/Libraries/GNOME
URL:            https://git.gnome.org/browse/libgnome-games-support/
Source0:        https://download.gnome.org/sources/libgnome-games-support/2.0/%{name}-%{version}.tar.xz
Source1:        https://download.gnome.org/sources/libgnome-games-support/2.0/%{name}-%{version}.sha256sum

BuildRequires:  intltool >= 0.50.2
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.40
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0) >= 2.40
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gtk4)

%description
libgnome-games-support is a small library intended for internal use by
GNOME Games, but it may be used by others. The API will only break
with the major version number. The ABI is unstable.

%package -n libgnome-games-support-%{api}-%{sover}
Summary:        Internal support library for GNOME games
# In order for the -lang package to be installable
Group:          System/Libraries
Provides:       %{name} = %{version}

%description -n libgnome-games-support-%{api}-%{sover}
libgnome-games-support is a small library intended for internal use by
GNOME Games, but it may be used by others. The API will only break
with the major version number. The ABI is unstable.

%package devel
Summary:        Development files for the GNOME Internal games library
Group:          Development/Libraries/C and C++
Requires:       libgnome-games-support-%{api}-%{sover} = %{version}

%description devel
libgnome-games-support is a small library intended for internal use by
GNOME Games, but it may be used by others. The API will only break
with the major version number. The ABI is unstable.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang libgnome-games-support2 %{name}.lang

%check
%meson_test

%ldconfig_scriptlets -n libgnome-games-support-%{api}-%{sover}

%files -n libgnome-games-support-%{api}-%{sover}
%license COPYING COPYING.LESSER
%{_libdir}/libgnome-games-support-%{api}.so.%{sover}*

%files devel
%{_includedir}/gnome-games-support-%{api}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/vala/

%files lang -f %{name}.lang

%changelog
