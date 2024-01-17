#
# spec file for package libgepub
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


%define basever 0.7
%define soname 0_7
%global sover   0

Name:           libgepub
Version:        0.7.1
Release:        0
Summary:        EPUB document reader and render library
License:        LGPL-2.1-or-later
Group:          Development/Languages/C and C++
URL:            https://gitlab.gnome.org/GNOME/libgepub
Source0:        https://download.gnome.org/sources/%{name}/%{basever}/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.30.0
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(webkit2gtk-4.1)

%description
A GObject-based library for handling and rendering EPUB documents.

%package -n %{name}-%{soname}-%{sover}
Summary:        EPUB document reader library
Group:          System/Libraries

%description -n %{name}-%{soname}-%{sover}
A GObject-based library for handling and rendering EPUB documents.

%package -n typelib-1_0-Gepub-%{soname}
Summary:        Introspection bindings for libgepub
Group:          System/Libraries

%description -n typelib-1_0-Gepub-%{soname}
A GObject-based library for handling and rendering EPUB documents.

%package devel
Summary:        Development files for libgepub
Group:          Development/Languages/C and C++
Requires:       %{name}-%{soname}-%{sover} = %{version}
Requires:       typelib-1_0-Gepub-%{soname} = %{version}

%description devel
A GObject-based library for handling and rendering EPUB documents.

%prep
%autosetup

%build
%meson \
	-D introspection=true \
	%{nil}
%meson_build

%install
%meson_install

%ldconfig_scriptlets -n %{name}-%{soname}-%{sover}

%files -n %{name}-%{soname}-%{sover}
%license COPYING
%{_libdir}/%{name}-%{basever}.so.*

%files -n typelib-1_0-Gepub-%{soname}
%{_libdir}/girepository-1.0/Gepub-%{basever}.typelib

%files devel
%doc AUTHORS MAINTAINERS NEWS README
%{_includedir}/%{name}-%{basever}/
%{_libdir}/%{name}-%{basever}.so
%{_libdir}/pkgconfig/%{name}-%{basever}.pc
%{_datadir}/gir-1.0/Gepub-%{basever}.gir

%changelog
