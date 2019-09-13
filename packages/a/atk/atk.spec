#
# spec file for package atk
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


Name:           atk
Version:        2.32.0
Release:        0
Summary:        An Accessibility Toolkit
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.gtk.org/
Source0:        https://download.gnome.org/sources/atk/2.32/%{name}-%{version}.tar.xz
Source99:       baselibs.conf

BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel >= 2.31.2
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson >= 0.46.0
BuildRequires:  translation-update-upstream

Requires:       %{name}-lang = %{version}
Requires:       libatk-1_0-0

%description
The ATK library provides a set of accessibility interfaces. By
supporting the ATK interfaces, an application or toolkit can be used
with screen readers, magnifiers, and alternate input devices.

%package -n libatk-1_0-0
Summary:        An Accessibility Toolkit
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libatk-1_0-0
The ATK library provides a set of accessibility interfaces. By
supporting the ATK interfaces, an application or toolkit can be used
with screen readers, magnifiers, and alternate input devices.

%package -n typelib-1_0-Atk-1_0
Summary:        Introspection bindings for the ATK accessibility toolkit
Group:          System/Libraries

%description -n typelib-1_0-Atk-1_0
The ATK library provides a set of accessibility interfaces. By
supporting the ATK interfaces, an application or toolkit can be used
with screen readers, magnifiers, and alternate input devices.

This package provides the GObject Introspection bindings for ATK.

%package devel
Summary:        Development files for the ATK accessibility toolkit
Group:          Development/Libraries/GNOME
Requires:       libatk-1_0-0 = %{version}
Requires:       typelib-1_0-Atk-1_0 = %{version}
#

%description devel
This package contains the header files for developing
applications that want to make use of atk.

%package doc
Summary:        Additional Package Documentation for atk
Group:          Documentation/HTML
Requires:       libatk-1_0-0 = %{version}
BuildArch:      noarch

%description doc
This package contains additional documentation for the ATK Library.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
%meson \
	-Ddocs=true \
	-Dintrospection=true \
	%{nil}
%meson_build

%install
%meson_install

%check
%meson_test

%find_lang %{name}10
%fdupes %{buildroot}%{_prefix}

%post -n libatk-1_0-0 -p /sbin/ldconfig
%postun -n libatk-1_0-0 -p /sbin/ldconfig

%files -n libatk-1_0-0
%license COPYING
%{_libdir}/lib*.so.*

%files -n typelib-1_0-Atk-1_0
%{_libdir}/girepository-1.0/Atk-1.0.typelib

%files lang -f %{name}10.lang

%files devel
%{_includedir}/atk-1.0
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir

%files doc
%doc AUTHORS NEWS README
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/atk

%changelog
