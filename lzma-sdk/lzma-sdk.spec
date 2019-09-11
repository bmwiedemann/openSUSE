#
# spec file for package lzma-sdk
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


%define _sver   1900
%define _maver  19
%define _miver  00
Name:           lzma-sdk
Version:        19.00
Release:        0
Summary:        An implementation of LZMA compression
# Actually the site says "Public Domain". See license file.
License:        LGPL-2.1-only
Group:          Productivity/Archiving/Compression
URL:            http://www.7-zip.org/sdk.html
Source0:        http://www.7-zip.org/a/lzma%{_sver}.7z
Source1:        lzma-sdk-LICENSE.fedora
Patch1:         lzma-sdk-shlib.patch
BuildRequires:  automake
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  p7zip-full
BuildRequires:  pkg-config

%description
LZMA SDK provides documentation, samples, header files, libraries,
and tools for developing applications with LZMA support.

LZMA uses a dictionary compression algorithm (a variant of LZ77, with
huge dictionary sizes and special support for repeatedly used match
distances), whose output is then encoded with a range encoder, using
a model to make a probability prediction of each bit.
LZMA yields around 20%% better compression when operating at approximately
zlib's speed, and around 40%% when trading more time.

%package devel
Summary:        Development libraries and headers for %{name}
Group:          Development/Languages/C and C++
Requires:       libclzma-suse0 = %{version}

%description devel
This package contains development libraries and headers for %{name}.

%package -n libclzma-suse0
Summary:        LZMA stream encoding/decoding library from 7-Zip
Group:          System/Libraries

%description -n libclzma-suse0
Library for encoding/decoding LZMA streams, using the 7-Zip library
implementation.

%prep
%setup -q -c -n lzma%{_sver}
%patch -P 1 -p1
perl -i -pe 's{AC_INIT.*}{AC_INIT([lzma-sdk], [%version])}' configure.ac
dos2unix DOC/*.txt
install -p -m 0644 %{SOURCE1} .

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la

%post   -n libclzma-suse0 -p /sbin/ldconfig
%postun -n libclzma-suse0 -p /sbin/ldconfig

%files -n libclzma-suse0
%license lzma-sdk-LICENSE.fedora
%doc DOC/lzma.txt DOC/lzma-history.txt
%{_libdir}/libclzma-suse.so.0*

%files devel
%license lzma-sdk-LICENSE.fedora
%doc DOC/7z*.txt DOC/Methods.txt
%{_includedir}/clzma/
%{_libdir}/libclzma.so
%{_libdir}/pkgconfig/clzma.pc

%changelog
