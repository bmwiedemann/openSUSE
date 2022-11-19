#
# spec file for package polymake
#
# Copyright (c) 2022 SUSE LLC
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


%define lname   libpolymake4_7
Name:           polymake
Version:        4.7
Release:        0
Summary:        Application for studying combinatorics and geometry of convex polytopes
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://polymake.org/

Source:         https://github.com/polymake/polymake/archive/V%version.tar.gz
Source9:        %name-rpmlintrc
Patch2:         sympol-system.patch
Patch3:         vertices-31.patch
BuildRequires:  bliss-devel
BuildRequires:  cddlib-devel
BuildRequires:  flint-devel
BuildRequires:  gcc-c++ >= 5
BuildRequires:  gmp-devel >= 4.2
BuildRequires:  libboost_headers-devel
BuildRequires:  libxml2-tools
BuildRequires:  libxslt-tools
BuildRequires:  lrslib-devel >= 7.1b
BuildRequires:  memory-constraints
BuildRequires:  mpfr-devel
BuildRequires:  ninja
BuildRequires:  normaliz-devel
BuildRequires:  perl-base >= 5.8.1
BuildRequires:  ppl-devel
BuildRequires:  readline-devel >= 5
BuildRequires:  sympol-devel
BuildRequires:  perl(JSON)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Term::ReadLine::Gnu)
BuildRequires:  perl(XML::LibXML)
BuildRequires:  perl(XML::LibXSLT)
BuildRequires:  perl(XML::Writer)
BuildRequires:  pkgconfig(libxml-2.0)

%description
polymake is a tool to study the combinatorics and the geometry of
convex polytopes and polyhedra. It is also capable of dealing with
simplicial complexes, matroids, polyhedral fans, graphs, tropical
objects, and other objects.

%package -n %lname
Summary:        Library for studying combinatorics and geometry of convex polytopes
Group:          System/Libraries

%description -n %lname
polymake is a tool to study the combinatorics and the geometry of
convex polytopes and polyhedra. It is also capable of dealing with
simplicial complexes, matroids, polyhedral fans, graphs, tropical
objects, and other objects.

%package devel
Summary:        Development files for the polymake library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version-%release

%description devel
polymake is a tool to study the combinatorics and the geometry of
convex polytopes and polyhedra. It is also capable of dealing with
simplicial complexes, matroids, polyhedral fans, graphs, tropical
objects, and other objects.

%prep
%autosetup -p1

%build
# Not AC.
./configure --prefix="%_prefix" --libdir="%_libdir" \
	--libexecdir="%_libdir/%name-%version" --without-native \
	--with-bliss="%_prefix" --with-sympol="%_prefix" --with-cdd="%_prefix" \
	--with-permlib="%_prefix"  --with-lrs="%_prefix" \
	CFLAGS="%optflags" CXXFLAGS="%optflags -g0" CXXOPT="%optflags"
# can't replace limit_build by _constraints file:
# * asking memoryperjob=3400 -> unsatisfiable i586 workers
#   (github.com/openSUSE/open-build-service/issues/10167)
# * asking physicalmemory=13600 -> unsatisfiable ppc64 workers
%limit_build -m 3400
make NINJA="ninja %{?_smp_mflags} -v"

%install
%make_install
find "%buildroot/%_includedir" -type f -exec chmod a-x {} +
mv "%buildroot/%_libdir/polymake-%version/lib"/libp* "%buildroot/%_libdir/"
# zero size file, why
rm -f "%buildroot/%_libdir/polymake-%version/lib/ideal.so"

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%_bindir/polymake
%_datadir/polymake/
# plugins or something
%_libdir/polymake-%version/
%doc ChangeLog
%license COPYING

%files -n %lname
%_libdir/libpolymake*.so.%version

%files devel
%_bindir/polymake-config
%_includedir/polymake/
%_libdir/libpoly*.so

%changelog
