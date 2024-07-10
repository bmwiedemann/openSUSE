#
# spec file for package openfst
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


%define lname libfst26
Name:           openfst
Version:        1.8.3
Release:        0
Summary:        Weighted finite-state transducer library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            http://www.openfst.org/
Source:         http://www.openfst.org/twiki/pub/FST/FstDownload/%name-%version.tar.gz
Patch1:         i586-80bitfp.patch
%if 0%{?suse_version} && 0%{?suse_version} < 1600
BuildRequires:  gcc12-c++ >= 8.1.0
%else
BuildRequires:  gcc-c++ >= 8.1.0
%endif
BuildRequires:  libtool
BuildRequires:  pkgconfig(zlib)

%description
OpenFst is a library for constructing, combining, optimizing and
searching weighted finite-state transducers (FSTs).

%package -n %lname
Summary:        Development files for OpenFST
Group:          System/Libraries

%description -n %lname
OpenFST is a library for constructing, combining, optimizing and
searching weighted finite-state transducers (FSTs).

This package requires SSE on 32-bit x86 to function.

%package devel
Summary:        Development files for OpenFST
Group:          Development/Libraries/C and C++
Requires:       %lname = %version-%release

%description devel
OpenFST is a library for constructing, combining, optimizing and
searching weighted finite-state transducers (FSTs).

%prep
%autosetup -p1

%build
%if 0%{?suse_version} && 0%{?suse_version} < 1600
export CXX=g++-12
%endif
autoreconf -fi
%configure
%make_build

%install
%make_install
find %buildroot/%_libdir -type f -name "*.la" -print -delete

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%license COPYING
%_bindir/fst*

%files -n %lname
%_libdir/lib*fst*.so.*

%files devel
%_includedir/fst/
%_libdir/*.so

%changelog
