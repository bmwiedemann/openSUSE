#
# spec file for package menu-cache
#
# Copyright (c) 2025 SUSE LLC
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


Name:           menu-cache
Version:        1.1.1
Release:        0
Summary:        A tool speed up menus
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/GUI/LXDE
URL:            https://www.lxde.org
Source0:        https://github.com/lxde/%{name}/archive/%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gtk-doc
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libtool
#BuildRequires:  m4
BuildRequires:  pkgconfig(libfm-extra)

%description
Libmenu-cache is a library creating and utilizing caches to speed up
the manipulation for freedesktop.org defined application menus.
It can be used as a replacement of libgnome-menu of gnome-menus.

%package devel
Summary:        Menu-cache Headers
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libmenu-cache3 = %{version}
Requires:       pkgconfig(glib-2.0)
Requires:       pkgconfig(libfm-extra)

%description devel
%{name} development files

%package -n libmenu-cache3
Summary:        Menu-cache libraries
Group:          System/Libraries

%description  -n libmenu-cache3
%{name} libraries for development

%prep
%autosetup -p1
sh autogen.sh

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}

%post -n libmenu-cache3 -p /sbin/ldconfig

%postun -n libmenu-cache3 -p /sbin/ldconfig

%files
%license COPYING
%doc README AUTHORS NEWS
%{_libexecdir}/%{name}

%files devel
%{_includedir}/%{name}
%{_libdir}/libmenu-cache.so
%{_libdir}/pkgconfig/libmenu-cache.pc

%files -n libmenu-cache3
%{_libdir}/libmenu-cache.so.*

%changelog
