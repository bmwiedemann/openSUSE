#
# spec file for package libopenraw
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


Name:           libopenraw
Version:        0.3.4
Release:        0
Summary:        A library to decode digital camera RAW files
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://libopenraw.freedesktop.org/
Source0:        http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.bz2
Source1:        http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
# cd lib/mp4 && cargo vendor -s Cargo.toml -s mp4parse/Cargo.toml -s mp4parse_capi/Cargo.toml && tar cf vendor.tar.xz vendor
Source3:        vendor.tar.xz
Source99:       baselibs.conf
BuildRequires:  autoconf >= 2.69
BuildRequires:  cargo
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  rust
BuildRequires:  pkgconfig(gdk-pixbuf-2.0) >= 2.21
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.5.0
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_test-devel >= 1.60.0
%else
BuildRequires:  boost-devel >= 1.60.0
%endif

%description
libopenraw is a library that aim at decoding digital camera RAW files.

%package -n libopenraw9
Summary:        A library to decode digital camera RAW files
Group:          System/Libraries
# libopenraw.so.0, version 0.3.1, was wrongly packaged in libopenraw1
Conflicts:      libopenraw1 >= 0.3

%description -n libopenraw9
libopenraw is a library that aim at decoding digital camera RAW files.

%package -n gdk-pixbuf-loader-libopenraw
Summary:        gdk-pixbuf loader for libopenraw
Group:          System/Libraries
Supplements:    packageand(libopenraw9:gdk-pixbuf)
%{gdk_pixbuf_loader_requires}

%description -n gdk-pixbuf-loader-libopenraw
libopenraw is a library that aim at decoding digital camera RAW files.

This package provides a libopenraw-based gdk-pixbuf loader.

%package -n libopenraw-devel
Summary:        A library to decode digital camera RAW files
Group:          Development/Libraries/C and C++
#include gdk-pixbuf/gdk-pixbuf.h
Requires:       gdk-pixbuf-devel
Requires:       libopenraw9 = %{version}-%{release}

%description  -n libopenraw-devel
libopenraw is a library that aim at decoding digital camera RAW files.

%prep
%autosetup -a3
mv vendor lib/mp4/
cd lib/mp4
sed -i 's/byteorder = "1.2.1"/byteorder = "1.2.2"/' mp4parse/Cargo.toml
mkdir .cargo
cat <<EOF >> .cargo/config.toml
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%post -n libopenraw9 -p /sbin/ldconfig
%postun -n libopenraw9 -p /sbin/ldconfig

%post -n gdk-pixbuf-loader-libopenraw
%{gdk_pixbuf_loader_post}

%postun -n gdk-pixbuf-loader-libopenraw
%{gdk_pixbuf_loader_postun}

%files -n libopenraw9
%license COPYING
%{_libdir}/*.so.*

%files -n gdk-pixbuf-loader-libopenraw
%{_libdir}/gdk-pixbuf-2.0/*/loaders/libopenraw_pixbuf.so

%files -n libopenraw-devel
%doc README TODO ChangeLog
%{_libdir}/*.so
%dir %{_includedir}/libopenraw-0.3
%{_includedir}/libopenraw-0.3/*
%{_libdir}/pkgconfig/*.pc

%changelog
