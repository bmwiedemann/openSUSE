#
# spec file for package xar
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define sover 1
Name:           xar
Version:        1.6.1
Release:        0
Summary:        Extensible Archive Format Tools
License:        BSD-3-Clause
Group:          Productivity/Archiving/Compression
Url:            http://mackyle.github.com/xar
Source:         https://github.com/mackyle/xar/archive/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM ext2.patch gh#mackyle/xar#10
Patch0:         ext2.patch
Patch1:         openssl-checks.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  e2fsprogs-devel
BuildRequires:  libacl-devel
BuildRequires:  libbz2-devel
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

%description
The XAR project aims to provide an easily extensible archive format. Important
design decisions include an easily extensible XML table of contents for random
access to archived files, storing the toc at the beginning of the archive to
allow for efficient handling of streamed archives, the ability to handle files
of arbitrarily large sizes, the ability to choose independent encodings for
individual files in the archive, the ability to store checksums for individual
files in both compressed and uncompressed form, and the ability to query the
table of content's rich meta-data.

%package -n libxar%{sover}
Summary:        Extensive Archive Format Library
Group:          Development/Libraries/C and C++

%description -n libxar%{sover}
The XAR project aims to provide an easily extensible archive format. Important
design decisions include an easily extensible XML table of contents for random
access to archived files, storing the toc at the beginning of the archive to
allow for efficient handling of streamed archives, the ability to handle files
of arbitrarily large sizes, the ability to choose independent encodings for
individual files in the archive, the ability to store checksums for individual
files in both compressed and uncompressed form, and the ability to query the
table of content's rich meta-data.

%package -n libxar-devel
Summary:        Extensive Archive Format Library
Group:          Development/Libraries/C and C++
Requires:       libxar%{sover} = %{version}

%description -n libxar-devel
The XAR project aims to provide an easily extensible archive format. Important
design decisions include an easily extensible XML table of contents for random
access to archived files, storing the toc at the beginning of the archive to
allow for efficient handling of streamed archives, the ability to handle files
of arbitrarily large sizes, the ability to choose independent encodings for
individual files in the archive, the ability to store checksums for individual
files in both compressed and uncompressed form, and the ability to query the
table of content's rich meta-data.

%prep
%setup -q -n %{name}-%{name}-%{version}
%patch0
%patch1 -p1
%build
pushd xar
./autogen.sh --noconfigure
%configure --disable-static
make %{?_smp_mflags}
popd

%install
pushd xar
%make_install
popd
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libxar%{sover} -p /sbin/ldconfig
%postun -n libxar%{sover} -p /sbin/ldconfig

%files
%doc xar/ChangeLog xar/LICENSE xar/NEWS
%{_bindir}/xar
%{_mandir}/man1/xar.1%{ext_man}

%files -n libxar%{sover}
%doc xar/ChangeLog xar/LICENSE xar/NEWS
%{_libdir}/libxar.so.%{sover}

%files -n libxar-devel
%doc xar/ChangeLog xar/LICENSE xar/NEWS
%{_includedir}/xar
%{_libdir}/libxar.so

%changelog
