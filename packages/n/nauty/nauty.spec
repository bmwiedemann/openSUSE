#
# spec file for package nauty
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


Name:           nauty
%define lname   libnauty-2_9_3
%define fuv     2_9_3
Version:        2.9.3
Release:        0
Summary:        Tools for computing automorphism groups of graphs
License:        Apache-2.0
Group:          Productivity/Scientific/Math
URL:            https://pallini.di.uniroma1.it/
Source:         https://pallini.di.uniroma1.it/nauty%fuv.tar.gz
Patch1:         nauty-am.diff
Patch3:         autoconf-2.72.patch
Patch4:         gcc15.patch
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gmp-devel
BuildRequires:  libtool >= 2
BuildRequires:  zlib-devel

%description
nauty and Traces are programs for computing automorphism groups of
graphs and digraphs (*Traces does not accept digraphs at this time).
They can also produce a canonical label. They are written in a
portable subset of C, and run on a considerable number of different
systems.

There is a small suite of programs called gtools included in the
package. For example, geng can generate non-isomorphic graphs very
quickly. There are also generators for bipartite graphs, digraphs,
and multigraphs.

%package -n %lname
Summary:        Graph automorphism group computation with Nauty
Group:          System/Libraries

%description -n %lname
nauty and Traces are programs for computing automorphism groups of
graphs and digraphs. They can also produce a canonical label.

%package devel
Summary:        Development files for nauty, a math library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version-%release

%description devel
nauty and Traces are programs for computing automorphism groups of
graphs and digraphs. They can also produce a canonical label.

This subpackage contains the header files for developing
applications that want to make use of libnauty.

%prep
%autosetup -v -p1 -n nauty%fuv

%build
rm -f aclocal.m4 makefile
autoreconf -fi
#export CFLAGS="%optflags -Wno-unused"
%configure --enable-generic --disable-popcnt --disable-clz
%make_build

%install
%make_install
rm -f "%buildroot/%_libdir"/*.la
%fdupes %buildroot/%_bindir

%ldconfig_scriptlets -n %lname

%files
%_bindir/*
%doc changes24-29.txt
%license COPYRIGHT

%files -n %lname
%_libdir/libnauty*-%version.so

%files devel
%_includedir/nauty/
%_libdir/libnauty.so
%_libdir/libnauty?0.so
%_libdir/libnauty?1.so

%changelog
