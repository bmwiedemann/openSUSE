#
# spec file for package libgnome-games-support
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover 3

Name:           libgnome-games-support
Version:        1.4.4
Release:        0
Summary:        Internal support library for GNOME games
License:        LGPL-3.0-or-later
Group:          Development/Libraries/GNOME
URL:            https://git.gnome.org/browse/libgnome-games-support/
Source0:        https://download.gnome.org/sources/libgnome-games-support/1.4/%{name}-%{version}.tar.xz

BuildRequires:  intltool >= 0.50.2
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.40
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0) >= 2.40
BuildRequires:  pkgconfig(glib-2.0) >= 2.40
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.19.2
Recommends:     %{name}-lang

%description
libgnome-games-support is a small library intended for internal use by
GNOME Games, but it may be used by others. The API will only break
with the major version number. The ABI is unstable.

%package -n libgnome-games-support-1-%{sover}
Summary:        Internal support library for GNOME games
# In order for the -lang package to be installable
Group:          System/Libraries
Provides:       %{name} = %{version}

%description -n libgnome-games-support-1-%{sover}
libgnome-games-support is a small library intended for internal use by
GNOME Games, but it may be used by others. The API will only break
with the major version number. The ABI is unstable.

%package devel
Summary:        Development files for the GNOME Internal games library
Group:          Development/Libraries/C and C++
Requires:       libgnome-games-support-1-%{sover} = %{version}

%description devel
libgnome-games-support is a small library intended for internal use by
GNOME Games, but it may be used by others. The API will only break
with the major version number. The ABI is unstable.

%lang_package

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%post -n libgnome-games-support-1-%{sover} -p /sbin/ldconfig
%postun -n libgnome-games-support-1-%{sover} -p /sbin/ldconfig

%files -n libgnome-games-support-1-%{sover}
%license COPYING.LESSER
%{_libdir}/libgnome-games-support-1.so.%{sover}*

%files devel
%{_includedir}/gnome-games-support-1/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/vala/

%files lang -f %{name}.lang

%changelog
