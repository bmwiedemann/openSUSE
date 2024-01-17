#
# spec file for package gnome-menus
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


Name:           gnome-menus
Version:        3.36.0
Release:        0
Summary:        The GNOME Desktop Menu
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            http://www.gnome.org
Source0:        https://download.gnome.org/sources/gnome-menus/3.36/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gio-unix-2.0) >= 2.29.15
Requires:       %{name}-branding = %{version}

%description
The package contains an implementation of the draft "Desktop Menu
Specification" from freedesktop.org:

http://www.freedesktop.org/Standards/menu-spec

%package -n libgnome-menu-3-0
Summary:        The GNOME Desktop Menu
Group:          System/Libraries
Requires:       %{name} >= %{version}
#

%description -n libgnome-menu-3-0
The package contains an implementation of the draft "Desktop Menu
Specification" from freedesktop.org:

http://www.freedesktop.org/Standards/menu-spec

%package -n typelib-1_0-GMenu-3_0
Summary:        The GNOME Desktop Menu -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GMenu-3_0
The package contains an implementation of the draft "Desktop Menu
Specification" from freedesktop.org

This package provides the GObject Introspection bindings for the
libgnome-menu library.

%package branding-upstream
Summary:        The GNOME Desktop Menu -- Upstream Menus Definitions
Group:          System/GUI/GNOME
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:branding-upstream)
Conflicts:      %{name}-branding
Provides:       %{name}-branding = %{version}
BuildArch:      noarch
#BRAND: This package contains set of needed .menu files in
#BRAND: /etc/xdg/menus. .directory files in
#BRAND: %%{_datadir}/desktop-directories/Multimedia.directory are part of
#BRAND: the main package. If you need custom one, simply it put there
#BRAND: and modify .menu file to refer to it.

%description branding-upstream
The package contains an implementation of the draft "Desktop Menu
Specification" from freedesktop.org:

http://www.freedesktop.org/Standards/menu-spec

This package provides the upstream definitions for menus.

%package devel
Summary:        The GNOME Desktop Menu
Group:          System/GUI/GNOME
Requires:       libgnome-menu-3-0 = %{version}
Requires:       typelib-1_0-GMenu-3_0 = %{version}

%description devel
The package contains an implementation of the draft "Desktop Menu
Specification" from freedesktop.org:

http://www.freedesktop.org/Standards/menu-spec

%lang_package

%prep
%autosetup -p1

%build
%configure \
	--disable-static
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name} %{?no_lang_C}
for dotdirectory in %{buildroot}%{_datadir}/desktop-directories/*.directory; do
  %suse_update_desktop_file $dotdirectory
done
%fdupes %{buildroot}

%post -n libgnome-menu-3-0 -p /sbin/ldconfig
%postun -n libgnome-menu-3-0 -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%dir %{_datadir}/desktop-directories
%{_datadir}/desktop-directories/*.directory
%dir %{_sysconfdir}/xdg/menus

%files -n libgnome-menu-3-0
%{_libdir}/libgnome-menu-3.so.0*

%files -n typelib-1_0-GMenu-3_0
%{_libdir}/girepository-1.0/GMenu-3.0.typelib

%files lang -f %{name}.lang

%files branding-upstream
%{_sysconfdir}/xdg/menus/gnome-applications.menu

%files devel
%{_includedir}/gnome-menus-3.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/libgnome-menu-3.0.pc
%{_datadir}/gir-1.0/GMenu-3.0.gir

%changelog
