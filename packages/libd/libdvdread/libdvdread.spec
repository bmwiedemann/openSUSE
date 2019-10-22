#
# spec file for package libdvdread
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


Name:           libdvdread
Version:        6.0.2
Release:        0
Summary:        Library for Reading DVD Video Images
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Other
URL:            https://www.videolan.org/developers/libdvdnav.html
Source0:        http://download.videolan.org/videolan/%{name}/%{version}/%{name}-%{version}.tar.bz2
#Source1:        http://download.videolan.org/videolan/%{name}/%{version}/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
Source3:        baselibs.conf
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)

%description
This package contains shared libraries for accessing DVD images (this
package does not contain DeCSS algorithms).

%package -n libdvdread7
Summary:        Library for Reading DVD Video Images
Group:          Productivity/Multimedia/Other
Provides:       %{name} = %{version}
Obsoletes:      %{name} <= 0.9.7

%description -n libdvdread7
This package contains shared libraries for accessing DVD images (this
package does not contain DeCSS algorithms).

%package devel
Summary:        Development Environment for libdvdread
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libdvdread7 = %{version}

%description devel
This package contains the include-files and static libraries for
libdvdread.

%prep
%setup -q

%build
autoreconf -fiv
%configure \
  --disable-silent-rules \
  --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# We install the files on our own, using %%doc
rm -rf %{buildroot}%{_datadir}/doc/libdvdread/

%post   -n libdvdread7 -p /sbin/ldconfig
%postun -n libdvdread7 -p /sbin/ldconfig

%files -n libdvdread7
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/libdvdread.so.7
%{_libdir}/libdvdread.so.7.*

%files devel
%{_includedir}/dvdread
%{_libdir}/libdvdread.so
%{_libdir}/pkgconfig/dvdread.pc

%changelog
