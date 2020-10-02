#
# spec file for package xplayer-plparser
#
# Copyright (c) 2020 SUSE LLC
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


%define _sover  18
%define _name   xplayer-pl-parser
Name:           xplayer-plparser
Version:        1.0.2
Release:        0
Summary:        Simple GObject-based library to parse playlist formats
License:        LGPL-2.0-or-later
Group:          Productivity/Multimedia/Video/Players
URL:            https://github.com/linuxmint/xplayer-plparser
Source:         https://github.com/linuxmint/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
#PATCH-FIX-UPSTREAM port to gmime-3.0
Patch:          %{name}-gmime-3.0.patch
BuildRequires:  gnome-common
BuildRequires:  libgcrypt-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(glib-2.0) >= 2.31.0
BuildRequires:  pkgconfig(gmime-3.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libarchive) >= 3.0
BuildRequires:  pkgconfig(libquvi-0.9) >= 0.9.1
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.43.0
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       libquvi-scripts
Recommends:     %{name}-lang

%description
xplayer-plparser is a simple GObject-based library to parse a host
of playlist formats, to save them too.

%lang_package

%package -n lib%{name}%{_sover}
Summary:        A simple GObject-based library to parse playlist formats
# Main package contains libexec files needed for full functionality.
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n lib%{name}%{_sover}
xplayer-plparser is a simple GObject-based library to parse a host
of playlist formats, to save them too.

%package -n typelib-1_0-XplayerPlParser-1_0
Summary:        Simple GObject-based library to parse playlist formats -- Introspection Bindings
# Main package contains libexec files needed for full functionality.
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n typelib-1_0-XplayerPlParser-1_0
xplayer-plparser is a simple GObject-based library to parse a host
of playlist formats, to save them too.

This package provides the GObject Introspection bindings for the
xplayer-plparser library.

%package -n lib%{name}-mini%{_sover}
Summary:        Simple GObject-based library to parse playlist formats -- Mini Version
# Main package contains libexec files needed for full functionality.
Group:          System/Libraries
Requires:       %{name} >= %{version}

%description -n lib%{name}-mini%{_sover}
xplayer-plparser is a simple GObject-based library to parse a host
of playlist formats, to save them too.

%package devel
Summary:        Simple GObject-based library to parse playlist formats
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{_sover} = %{version}
Requires:       lib%{name}-mini%{_sover} = %{version}
Requires:       typelib-1_0-XplayerPlParser-1_0 = %{version}

%description devel
xplayer-plparser is a simple GObject-based library to parse a host
of playlist formats, to save them too.

%prep
%setup -q
%patch -p1

%build
NOCONFIGURE=1 gnome-autogen.sh
%configure \
  --disable-static                     \
  --libexecdir=%{_libexecdir}/%{name}/ \
  --enable-quvi
make %{?_smp_mflags}

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{_name}

%post -n lib%{name}%{_sover} -p /sbin/ldconfig

%postun -n lib%{name}%{_sover} -p /sbin/ldconfig

%post -n lib%{name}-mini%{_sover} -p /sbin/ldconfig

%postun -n lib%{name}-mini%{_sover} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc COPYING.LIB README debian/changelog
%dir %{_libexecdir}/%{name}/
%{_libexecdir}/%{name}/xplayer-pl-parser-videosite

%files lang -f %{_name}.lang
%defattr(-,root,root)

%files -n lib%{name}%{_sover}
%defattr(-,root,root)
%{_libdir}/lib%{name}.so.%{_sover}*

%files -n typelib-1_0-XplayerPlParser-1_0
%defattr(-,root,root)
%{_libdir}/girepository-1.0/XplayerPlParser-1.0.typelib

%files -n lib%{name}-mini%{_sover}
%defattr(-, root, root)
%{_libdir}/lib%{name}-mini.so.%{_sover}*

%files devel
%defattr(-,root,root)
%{_includedir}/%{_name}/
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}-mini.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}-mini.pc
%{_datadir}/gir-1.0/*.gir

%changelog
