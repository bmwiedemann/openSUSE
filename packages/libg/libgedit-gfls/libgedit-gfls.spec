#
# spec file for package libgedit-gfls
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


Name:           libgedit-gfls
Version:        0.2.1
Release:        0
Summary:        Gedit Technology - File loading and saving
License:        LGPL-3.0-or-later
URL:            https://gedit-technology.github.io/
Source:         %{name}-%{version}.tar.zst
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0) >= 2.78
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22

%description
libgedit-gfls is a module dedicated to file loading and saving for the needs of gedit and other similar text editors.

%package -n libgedit-gfls-1-0
Summary:        Gedit Technology - File loading and saving
# Needed to make lang package installable
Provides:       libgedit-gfls = %{version}

%description -n libgedit-gfls-1-0
libgedit-gfls is a module dedicated to file loading and saving for the needs of gedit and other similar text editors.

%package -n typelib-1_0-Gfls-1
Summary:        Gedit Technology - File loading and saving

%description -n typelib-1_0-Gfls-1
libgedit-gfls is a module dedicated to file loading and saving for the needs of gedit and other similar text editors.

%package devel
Summary:        Gedit Technology - File loading and saving; development package
Requires:       libgedit-gfls-1-0 = %{version}
Requires:       typelib-1_0-Gfls-1 = %{version}

%description devel
libgedit-gfls is a module dedicated to file loading and saving for the needs of gedit and other similar text editors.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}-1 %{?no_lang_C}

%check
%meson_test

%ldconfig_scriptlets -n libgedit-gfls-1-0

%files -n libgedit-gfls-1-0
%{_libdir}/libgedit-gfls-1.so.0

%files -n typelib-1_0-Gfls-1
%{_libdir}/girepository-1.0/Gfls-1.typelib

%files devel
%{_libdir}/libgedit-gfls-1.so
%{_libdir}/pkgconfig/libgedit-gfls-1.pc
%{_datadir}/gir-1.0/Gfls-1.gir
%{_datadir}/gtk-doc/html/libgedit-gfls-1/
%{_includedir}/libgedit-gfls-1/

%files lang -f %{name}-1.lang

%changelog
