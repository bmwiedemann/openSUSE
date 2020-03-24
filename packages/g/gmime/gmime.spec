#
# spec file for package gmime
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


# Define a base version
%define base_ver 3.0
# Define a so version
# NOTE - also update baselibs.conf when bumping this
%define so_ver 3_0
Name:           gmime
Version:        3.2.7
Release:        0
Summary:        MIME Parser and Utility Library
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Email/Utilities
URL:            http://spruce.sourceforge.net/gmime/
Source:         https://download.gnome.org/sources/gmime/3.2/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  gobject-introspection-devel >= 1.30.0
BuildRequires:  gpgme-devel
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libidn) >= 0.0.0
BuildRequires:  pkgconfig(vapigen)

%description
GMime is a C/C++ library for parsing and creating messages using
the Multipurpose Internet Mail Extension (MIME).

%package -n libgmime-%{so_ver}-0
Summary:        MIME Parser and Utility Library
Group:          System/Libraries

%description -n libgmime-%{so_ver}-0
GMime is a C/C++ library for parsing and creating messages using
the Multipurpose Internet Mail Extension (MIME).

%package -n typelib-1_0-GMime-%{so_ver}
Summary:        MIME Parser and Utility Library -- Introspection bindings
Group:          System/Libraries

%description -n typelib-1_0-GMime-%{so_ver}
GMime is a C/C++ library for parsing and creating messages using
the Multipurpose Internet Mail Extension (MIME).

%package devel
Summary:        MIME Parser and Utility Library -- Development Files
Group:          Development/Libraries/C and C++
Requires:       libgmime-%{so_ver}-0 = %{version}

%description devel
GMime is a C/C++ library for parsing and creating messages using
the Multipurpose Internet Mail Extension (MIME).

%prep
%setup -q

%build
%configure\
	--enable-largefile\
	--disable-static\
	--enable-gtk-doc \
	--enable-crypto \
        --with-gacdir=%{_prefix}/lib
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libgmime-%{so_ver}-0 -p /sbin/ldconfig
%postun -n libgmime-%{so_ver}-0 -p /sbin/ldconfig

%files -n libgmime-%{so_ver}-0
%license COPYING
%{_libdir}/*.so.*

%files -n typelib-1_0-GMime-%{so_ver}
%{_libdir}/girepository-1.0/GMime-%{base_ver}.typelib

%files devel
%doc AUTHORS PORTING README TODO
%doc %{_datadir}/gtk-doc/html/gmime-3.2/
%{_datadir}/gir-1.0/GMime-%{base_ver}.gir
%{_includedir}/gmime-%{base_ver}
%{_libdir}/*.so
%{_libdir}/pkgconfig/gmime-%{base_ver}.pc
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gmime-3.0.deps
%{_datadir}/vala/vapi/gmime-3.0.vapi

%changelog
