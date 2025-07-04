#
# spec file for package id3lib
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


%define lname	libid3-3_8-3
Name:           id3lib
Version:        3.8.3
Release:        0
Summary:        A Library for Manipulating ID3v1 and ID3v2 tags
License:        LGPL-2.1-or-later
URL:            http://id3lib.sourceforge.net/
Source0:        http://sourceforge.net/projects/id3lib/files/id3lib/%{version}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch1:         id3lib-%{version}-autoconf.patch
Patch2:         id3lib-%{version}-cleanup.patch
Patch3:         id3lib-%{version}-doxygen.patch
Patch4:         id3lib-%{version}-gcc34.patch
Patch5:         id3lib-%{version}-UTF16-writing-bug.patch
Patch6:         id3lib-%{version}-zlib.patch
Patch7:         id3lib-%{version}-uninitialized.patch
# This patch fixes CVE-2007-4460 - id3lib doesn't use mkstemp() to create a name of a temporary file.
Patch8:         id3lib-%{version}-CVE-2007-4460.patch
Patch9:         id3lib-%{version}-missing_c_includes.patch
Patch10:        id3lib-%{version}-fix_m4_quoting.patch
Patch11:        id3lib-%{version}-unsigned_argc.patch
Patch12:        id3lib-%{version}-iomanip_h.patch
Patch13:        id3lib-%{version}-fix-stack-overrun.patch
Patch14:        id3lib-3.8.3-fix-utf16-stringlists.patch
Patch15:        add-c-wrapper-functions.patch
Patch16:        id3lib-missing-nullpointer-check.patch
# taken from https://gitweb.gentoo.org/repo/gentoo.git/plain/media-libs/id3lib/files/id3lib-3.8.3-fix-c23.patch
Patch17:        id3lib-3.8.3-fix-c23.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  zlib-devel

%description
A software library for manipulating ID3v1 and ID3v2 tags.

%package -n %{lname}
Summary:        A Library for Manipulating ID3v1 and ID3v2 tags
Obsoletes:      id3lib < %{version}-%{release}
Provides:       id3lib = %{version}-%{release}

%description -n %{lname}
This package provides a software library for manipulating ID3v1 and
ID3v2 tags. It provides a convenient interface for software developers
to include standards-compliant ID3v1/2 tagging capabilities in their
applications. Features include identification of valid tags, automatic
size conversions, synchronization and resynchronization of tag frames,
seamless tag compression and decompression, and optional padding
facilities.

%package      devel
Summary:        Documentation and Headers for id3lib
Requires:       %{lname} = %{version}
Requires:       libstdc++-devel

%description	devel
This package contains the headers and documentation for the id3lib API
that programmers will need to develop applications which use id3lib,
the software library for ID3v1 and ID3v2 tag manipulation.

%package      examples
Summary:        Example Applications for the id3lib Library
Requires:       %{name} = %{version}

%description	examples
This package contains simple example applications that make use of
id3lib, a software library for ID3v1 and ID3v2 tag manipulation.

%prep
%setup -q
%patch -P 1
%patch -P 2
%patch -P 3
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6
%patch -P 7
%patch -P 8
%patch -P 9
%patch -P 10
%patch -P 11
%patch -P 12
%patch -P 13 -p1
%patch -P 14 -p1
%patch -P 15 -p1
%patch -P 16 -p1
%if %{pkg_vcmp gcc >= 15}
%patch -P 17 -p1 -b .c23
%endif
for i in doc/id3v2.3.0{.txt,.html}; do
  dos2unix $i
done

%build
export CXXFLAGS="%{optflags} -fvisibility-inlines-hidden"
rm acconfig.h
autoreconf -fiv
%configure \
  --disable-static \
  --enable-debug=no
%make_build
%make_build docs -j1

%install
%make_install
make -C examples clean
rm -rf examples/.deps
chmod 644 examples/*
# strip down the doc and examples directories so we can copy w/impunity
for i in doc/ examples/ ; do \
    find ./$i  -name 'Makefile*' -delete
done
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes -s doc

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%license COPYING
%{_libdir}/*.so.*

%files devel
%doc AUTHORS ChangeLog HISTORY NEWS README THANKS TODO
%{_includedir}/id3*.h
%{_includedir}/id3
%{_libdir}/*.so
%doc doc/*.*
%doc doc/api

%files examples
%doc examples
%{_bindir}/id3*

%changelog
