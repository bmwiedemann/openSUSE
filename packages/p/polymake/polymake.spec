#
# spec file for package polymake
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


%define lname   libpolymake4_11
Name:           polymake
Version:        4.11
Release:        0
Summary:        Application for studying combinatorics and geometry of convex polytopes
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://polymake.org/

Source:         https://github.com/polymake/polymake/archive/V%version.tar.gz
Source9:        %name-rpmlintrc
Patch2:         sympol-system.patch
BuildRequires:  bliss-devel
BuildRequires:  cddlib-devel
BuildRequires:  fdupes
BuildRequires:  flint-devel
BuildRequires:  gcc-c++ >= 5
BuildRequires:  gmp-devel >= 4.2
BuildRequires:  libSingular-devel
BuildRequires:  libboost_headers-devel
BuildRequires:  libxml2-tools
BuildRequires:  libxslt-tools
BuildRequires:  lrslib-devel >= 7.1b
BuildRequires:  memory-constraints
BuildRequires:  mpfr-devel
BuildRequires:  ninja
BuildRequires:  normaliz-devel
BuildRequires:  perl < 5.40
BuildRequires:  perl(JSON)
BuildRequires:  ppl-devel
BuildRequires:  readline-devel >= 5
BuildRequires:  sympol-devel
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       perl(JSON)
Requires:       perl(Term::ReadKey)
Requires:       perl(Term::ReadLine::Gnu)
Requires:       perl(XML::SAX)

%description
polymake is a tool to study the combinatorics and the geometry of
convex polytopes and polyhedra. It is also capable of dealing with
simplicial complexes, matroids, polyhedral fans, graphs, tropical
objects, and other objects.

%package devel
Summary:        Development files for Polymake plugins
Group:          Development/Libraries/C and C++
Requires:       %name = %version

%description devel
polymake is a tool to study the combinatorics and the geometry of
convex polytopes and polyhedra. It is also capable of dealing with
simplicial complexes, matroids, polyhedral fans, graphs, tropical
objects, and other objects.

%prep
%autosetup -p1

%build
# force using system libnormaliz
rm -rf bundled/libnormaliz/external
# It's not autoconf.
./configure --prefix="%_prefix" --libdir="%_libdir" \
	--libexecdir="%_libdir/%name-%version" --without-native \
	--with-bliss="%_prefix" --with-sympol="%_prefix" --with-cdd="%_prefix" \
	--with-permlib="%_prefix"  --with-lrs="%_prefix" --without-callable \
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
%fdupes %buildroot/%_prefix

%files
%_bindir/polymake
%_datadir/polymake/
# plugins or something
%_libdir/polymake-%version/
%doc ChangeLog
%license COPYING

%files devel
%_bindir/polymake-config
%_includedir/polymake/

%changelog
