#
# spec file for package gap-semigroups
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


Name:           gap-semigroups
Version:        5.5.4
Release:        0
Summary:        GAP: Computing with Semigroups of Transformations and Partial Permutations
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://semigroups.github.io/Semigroups/
#Git-Clone:     https://github.com/semigroups/Semigroups
Source:         https://github.com/semigroups/Semigroups/releases/download/v%version/semigroups-%version.tar.gz
Patch1:         no-avx.patch
Patch2:         bundled-paths.patch
BuildRequires:  automake
BuildRequires:  c++_compiler
BuildRequires:  chrpath
BuildRequires:  fdupes
BuildRequires:  gap-devel >= 4.12.1
BuildRequires:  gap-rpm-devel
BuildRequires:  gmp-devel
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(fmt) >= 10.1
BuildRequires:  libtool
BuildRequires:  xz
Provides:       bundled(libsemigroups) = 2.7.4
Provides:       bundled(magic_enum)
Provides:       bundled(rx-ranges)
Requires:       gap-core >= 4.12.1
Requires:       gap-datastructures >= 0.2.5
Requires:       gap-digraphs >= 1.6.2
Requires:       gap-genss >= 1.6.5
Requires:       gap-images >= 1.3.1
Requires:       gap-io >= 4.5.1
Requires:       gap-orb >= 4.8.2
Suggests:       gap-autodic >= 2020.08.11
Suggests:       gap-gapdoc >= 1.6.3

%description
The Semigroups package is a GAP package containing methods for
semigroups, principally semigroups of transformations, partial
permutations or subsemigroups of regular Rees 0-matrix semigroups.
Semigroups contains more efficient methods than those available in
the GAP library (and in many cases more efficient than any other
software) for creating semigroups, calculating their Green's classes,
size, elements, group of units, minimal ideal, small generating sets,
testing membership, finding the inverses of a regular element,
factorizing elements over the generators, and many more. It is also
possible to test if a semigroup satisfies a particular property, such
as if it is regular, simple, inverse, completely regular, and a
variety of further properties.

%package -n libsemigroups2
Summary:        Library with algorithms for computing finite and finitely presented semigroups
Group:          System/Libraries

%description -n libsemigroups2
A C++14 library containing implementations of several algorithms for
computing finite and finitely presented semigroups.

%prep
%autosetup -n semigroups-%version

%build
autoreconf -fi
# gap-semigroup use of a just-built bundled libsemigroups is fragile
%set_build_flags
export CFLAGS="$CFLAGS $(pkg-config eigen3 --cflags)"
export CXXFLAGS="$CXXFLAGS $(pkg-config eigen3 --cflags)"
# hpcombi requires AVX-256, which is not guaranteed to exist everywhere
%configure --disable-static --disable-hpcombi \
	--enable-eigen --with-external-eigen \
	--enable-fmt --with-external-fmt \
	--with-gaproot="%gapdir"

%make_build

%install
b="%buildroot"
mkdir -pv "$b/%_libdir"
rm -Rfv libsemigroups bin/include bin/lib/*.la bin/lib/*.so bin/lib/pkgconfig
mv -v bin/lib/* "$b/%_libdir/"

find . -name semigroups.so -exec chrpath -d "{}" "+"
%gappkg_simple_install
cd "%buildroot/$fmoddir/"
rm -Rfv Makefile* configure* config.* cnf/ src/ gapbind14/src/ gapbind14/include/ autom4te.cache
find "%buildroot" "(" -name "*.orig" -o -name .gitignore -o \
	-name .dirstamp -o -name .clang-format -o -name .ccls ")" -print -delete
%fdupes %buildroot/%_prefix

%ldconfig_scriptlets -n libsemigroups2

%files -f %name.files

%files -n libsemigroups2
%_libdir/libsemigroups.so.*

%changelog
