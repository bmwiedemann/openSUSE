#
# spec file for package polymake
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define lname   libpolymake4_15
Name:           polymake
Version:        4.15
Release:        0
Summary:        Application for studying combinatorics and geometry of convex polytopes
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://polymake.org/

Source:         https://github.com/polymake/polymake/releases/download/V%version/polymake-%version-minimal.tar.bz2
Source9:        %name-rpmlintrc
Patch2:         sympol-system.patch
Patch3:         perl.patch
BuildRequires:  bliss-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 5
BuildRequires:  gmp-devel >= 4.2
BuildRequires:  libboost_headers-devel
BuildRequires:  libxml2-tools
BuildRequires:  libxslt-tools
BuildRequires:  lrslib-devel >= 7.1b
BuildRequires:  memory-constraints
BuildRequires:  ninja
BuildRequires:  normaliz-devel
BuildRequires:  perl
BuildRequires:  ppl-devel
BuildRequires:  sympol-devel
BuildRequires:  perl(JSON)
BuildRequires:  perl(Term::ReadKey)
BuildRequires:  perl(Term::ReadLine::Gnu)
BuildRequires:  perl(XML::SAX)
BuildRequires:  pkgconfig(Singular)
BuildRequires:  pkgconfig(cddgmp)
BuildRequires:  pkgconfig(flint)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(readline) >= 5
%if 0%{?suse_version} >= 1690
BuildRequires:  pkgconfig(libbson-1.0)
BuildRequires:  pkgconfig(libmongoc-1.0)
%endif
Requires:       perl(JSON)
Requires:       perl(Term::ReadKey)
Requires:       perl(Term::ReadLine::Gnu)
Requires:       perl(XML::SAX)
Suggests:       4ti2
Suggests:       azove
Suggests:       gfan
Suggests:       graphviz
Suggests:       latte
Suggests:       plantri
Suggests:       povray
Suggests:       qhull
Suggests:       web_browser
Suggests:       vinci
Suggests:       mimehandler(application/pdf)
#Suggests:      porta <https://porta.zib.de/>
# web_browser used for displaying SVG

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
%fdupes %buildroot/%_prefix

%ldconfig_scriptlets -n %lname

%files
%_bindir/polymake
%_datadir/polymake/
# plugins or something
%_libdir/polymake-%version/
%doc ChangeLog
%license COPYING

%files -n %lname
%_libdir/libpolymake*.so.*

%files devel
%_bindir/polymake-config
%_includedir/polymake/
%_libdir/libpolymake*.so

%changelog
