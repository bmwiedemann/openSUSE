#
# spec file for package gap
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


Name:           gap
Version:        4.12.2
Release:        0
Summary:        System for Computational Discrete Algebra
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gap-system.org/

Source:         https://github.com/gap-system/gap/releases/download/v%version/gap-%version-core.tar.gz
Source2:        macros.gap
Source3:        %name-rpmlintrc
BuildRequires:  gcc-c++
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif
BuildRequires:  gmp-devel
BuildRequires:  libtool
BuildRequires:  readline-devel
BuildRequires:  unzip
BuildRequires:  zlib-devel
Provides:       gap-core = %version-%release
Requires:       gap-gapdoc >= 1.2
Requires:       gap-primgrp >= 3.4.3
Requires:       gap-smallgrp >= 1.5.1
Requires:       gap-transgrp >= 3.6.3

%define lname libgap8
%global gap_sitearch %_libdir/gap/pkg
%global gap_sitelib  %_datadir/gap/pkg

%description
GAP is a system for computational discrete algebra, with particular
emphasis on Computational Group Theory. GAP provides a programming
language, a library of thousands of functions implementing algebraic
algorithms written in the GAP language as well as large data
libraries of algebraic objects. GAP is used in research and teaching
for studying groups and their representations, rings, vector spaces,
algebras, combinatorial structures, and more.

%package -n %lname
Summary:        Kernel for the GAP computation algebra system
Group:          System/Libraries

%description -n %lname
This package contains the GAP kernel in a C library that can be
linked to.

%package devel
Summary:        Development environment for GAP
Group:          Development/Tools/Other
Requires:       %lname = %version

%description devel
GAP is a system for computational discrete algebra, with particular
emphasis on Computational Group Theory.

This package will pull in the current version of the GAP compiler
"gac", as well as utilities required to build GAP packages that need
compilation.

%package rpm-devel
Summary:        RPM macros for building GAP packages
# Not noarch: contains arch-specific paths in RPM macros
Group:          Development/Tools/Other

%description rpm-devel
GAP is a system for computational discrete algebra, with particular
emphasis on Computational Group Theory.

This subpackage provides RPM macros for building GAP modules as RPMs.

%package full
Summary:        Metapackage to cause installation of the GAP Distribution
Group:          Metapackages
BuildArch:      noarch
Requires:       gap >= %version
Requires:       gap-4ti2interface >= 2022.09.01
Requires:       gap-ace >= 5.6.1
Requires:       gap-aclib >= 1.3.2
Requires:       gap-agt >= 0.2
Requires:       gap-alnuth >= 3.2.1
Requires:       gap-anupq >= 3.2.6
Requires:       gap-atlasrep >= 2.1.6
Requires:       gap-autodoc >= 2022.10.20
Requires:       gap-automata >= 1.15
Requires:       gap-automgrp >= 1.3.2
Requires:       gap-autpgrp >= 1.11
Requires:       gap-browse >= 1.8.19
Requires:       gap-cap >= 2022.12.11
Requires:       gap-caratinterface >= 2.3.4
Requires:       gap-cddinterface >= 2022.11.01
Requires:       gap-circle >= 1.6.5
Requires:       gap-classicpres >= 1.22
Requires:       gap-cohomolo >= 1.6.10
Requires:       gap-congruence >= 1.2.4
Requires:       gap-corelg >= 1.56
Requires:       gap-crime >= 1.6
Requires:       gap-crisp >= 1.4.6
Requires:       gap-crypting >= 0.10.4
Requires:       gap-cryst >= 4.1.25
Requires:       gap-crystcat >= 1.1.10
Requires:       gap-ctbllib >= 1.3.4
Requires:       gap-cubefree >= 1.19
Requires:       gap-curlinterface >= 2.3.1
Requires:       gap-cvec >= 2.7.6
Requires:       gap-datastructures >= 0.3.0
Requires:       gap-deepthought >= 1.0.6
Requires:       gap-design >= 1.7
Requires:       gap-difsets >= 2.3.1
Requires:       gap-digraphs >= 1.6.1
Requires:       gap-edim >= 1.3.6
Requires:       gap-example >= 4.3.2
Requires:       gap-examplesforhomalg >= 2022.11.01
Requires:       gap-factint >= 1.6.3
Requires:       gap-ferret >= 1.0.9
Requires:       gap-fga >= 1.4.0
Requires:       gap-fining >= 1.5.4
#ftbfs#Requires: gap-float >= 1.0.3
Requires:       gap-format >= 1.4.3
Requires:       gap-forms >= 1.2.9
Requires:       gap-fplsa >= 1.2.5
Requires:       gap-fr >= 2.4.12
#dependson jupyterkernel#Requires:       gap-francy >= 1.2.5
Requires:       gap-fwtree >= 1.3
Requires:       gap-gapdoc >= 1.6.6
Requires:       gap-gauss >= 2022.11.01
Requires:       gap-gaussforhomalg >= 2022.08.03
Requires:       gap-gbnp >= 1.0.5
Requires:       gap-generalizedmorphismsforcap >= 2022.12.01
Requires:       gap-genss >= 1.6.8
Requires:       gap-gradedmodules >= 2022.09.02
Requires:       gap-gradedringforhomalg >= 2022.11.01
Requires:       gap-grape >= 4.9.0
Requires:       gap-groupoids >= 1.71
Requires:       gap-grpconst >= 2.6.3
Requires:       gap-guarana >= 0.96.3
Requires:       gap-guava >= 3.17
Requires:       gap-hap >= 1.47
Requires:       gap-hapcryst >= 0.1.15
Requires:       gap-hecke >= 1.5.3
Requires:       gap-help >= 3.5
Requires:       gap-homalg >= 2022.11.01
Requires:       gap-homalgtocas >= 2022.11.02
Requires:       gap-idrel >= 2.44
Requires:       gap-images >= 1.3.1
Requires:       gap-intpic >= 0.3.0
Requires:       gap-io >= 4.8.0
Requires:       gap-io_forhomalg >= 2022.11.01
Requires:       gap-irredsol >= 1.4.4
Requires:       gap-itc >= 1.5.1
Requires:       gap-json >= 2.1.1
#notready#Requires: gap-jupyterkernel >= 1.4.1
#notready#Requires: gap-jupyterviz >= 1.5.6
Requires:       gap-kan >= 1.34
Requires:       gap-kbmag >= 1.5.10
Requires:       gap-laguna >= 3.9.5
Requires:       gap-liealgdb >= 2.2.1
Requires:       gap-liepring >= 2.8
Requires:       gap-liering >= 2.4.2
Requires:       gap-linearalgebraforcap >= 2022.12.04
Requires:       gap-localizeringforhomalg >= 2022.11.01
Requires:       gap-loops >= 3.4.3
Requires:       gap-lpres >= 1.0.3
Requires:       gap-majoranaalgebras >= 1.5.1
Requires:       gap-mapclass >= 1.4.6
Requires:       gap-matgrp >= 0.70
Requires:       gap-matricesforhomalg >= 2022.12.01
Requires:       gap-modisom >= 2.5.3
# gap-modulepresentationsforcap requires a non-existent gap-complexesandfilteredobjectsforgap
#Requires:      gap-modulepresentationsforcap >= 2022.12.01
Requires:       gap-modules >= 2022.11.01
Requires:       gap-monoidalcategories >= 2022.12.01
Requires:       gap-nconvex >= 2022.09.01
Requires:       gap-nilmat >= 1.4.2
Requires:       gap-nock >= 1.5
Requires:       gap-normalizinterface >= 1.3.5
Requires:       gap-nq >= 2.5.9
Requires:       gap-numericalsgps >= 1.3.1
Requires:       gap-openmath >= 11.5.2
Requires:       gap-orb >= 4.9.0
#Needs separate gap-core built with openmpi and update-alternatives
#Requires:      gap-pargap >= 1.4.0
Requires:       gap-patternclass >= 2.4.3
Requires:       gap-permut >= 2.0.4
Requires:       gap-polenta >= 1.3.10
Requires:       gap-polycyclic >= 2.16
Requires:       gap-polymaking >= 0.8.6
Requires:       gap-primgrp >= 3.4.3
Requires:       gap-profiling >= 2.5.1
Requires:       gap-qpa >= 1.34
Requires:       gap-quagroup >= 1.8.3
Requires:       gap-radiroot >= 2.9
Requires:       gap-rcwa >= 4.7.1
Requires:       gap-rds >= 1.8
Requires:       gap-recog >= 1.4.2
Requires:       gap-repndecomp >= 1.2.1
Requires:       gap-repsn >= 3.1.0
Requires:       gap-resclasses >= 4.7.3
Requires:       gap-ringsforhomalg >= 2022.11.01
Requires:       gap-sco >= 2022.09.01
Requires:       gap-scscp >= 2.4.0
Requires:       gap-semigroups >= 5.2.0
Requires:       gap-sglppow >= 2.3
Requires:       gap-sgpviz >= 0.999.5
Requires:       gap-simpcomp >= 2.1.14
Requires:       gap-singular >= 2022.09.23
Requires:       gap-sl2reps >= 1.1
Requires:       gap-sla >= 1.5.3
Requires:       gap-smallgrp >= 1.5.1
Requires:       gap-smallsemi >= 0.6.13
Requires:       gap-sonata >= 2.9.6
Requires:       gap-sophus >= 1.27
Requires:       gap-spinsym >= 1.5.2
Requires:       gap-standardff >= 0.9.4
Requires:       gap-symbcompcc >= 1.3.2
Requires:       gap-thelma >= 1.3
Requires:       gap-tomlib >= 1.2.9
Requires:       gap-toolsforhomalg >= 2022.12.01
Requires:       gap-toric >= 1.9.5
Requires:       gap-toricvarieties >= 2022.07.13
Requires:       gap-transgrp >= 3.6.3
Requires:       gap-ugaly >= 4.0.3
Requires:       gap-unipot >= 1.2
Requires:       gap-unitlib >= 4.1.0
Requires:       gap-utils >= 0.81
Requires:       gap-uuid >= 0.7
Requires:       gap-walrus >= 0.9991
Requires:       gap-wedderga >= 4.10.2
Requires:       gap-xgap >= 4.31
Requires:       gap-xmod >= 2.88
Requires:       gap-xmodalg >= 1.23
Requires:       gap-yangbaxter >= 0.10.2
Requires:       gap-zeromqinterface >= 0.14

%description full
GAP is a system for computational discrete algebra, with particular
emphasis on Computational Group Theory.

This subpackage will pull in all optional packages of the GAP distribution.

%prep
%autosetup
echo "This package causes installation of optional GAP packages" >FULL.txt

%build
%configure
%make_build GAP_BUILD_DATETIME=""

%install
# Can not use "install" target, as that includes the "install-doc" target
make DESTDIR="%buildroot" INSTALL="install -p" \
  install-bin install-gaproot install-sysinfo install-headers install-libgap

# Fixup
rm -fv "%buildroot/%_libdir"/*.la
chmod +x %buildroot/%_datadir/gap%_sysconfdir/convert.pl

# For ancient modules
ln -s "%_bindir/gac" "%buildroot/%_libdir/gap/gac"

# openSUSE-specific extras for RPMs
install -D -m 0644 -t "%buildroot/%_prefix/lib/rpm/macros.d/" "%_sourcedir/macros.gap"
cat >> "%buildroot/%_prefix/lib/rpm/macros.d/macros.gapdirs" <<-EOF
	# Directory for modules extending the core
	%%gap_sitelib %gap_sitelib
	%%gap_sitearch %gap_sitearch
	%%gap_sitelib_anchor %_datadir
	%%gap_sitearch_anchor %_libdir
	%%gapdir %_libdir/gap
EOF
%fdupes %buildroot/%_includedir

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%_bindir/gap*
%dir %_libdir/gap/
%_libdir/gap/gap
%_datadir/gap/

%files -n %lname
%_libdir/libgap.so.8*

%files devel
%_bindir/gac*
%_includedir/gap/
%_libdir/libgap.so
%dir %_libdir/gap
%_libdir/gap/gac
%_libdir/gap/sysinfo.gap*

%files full
%doc FULL.txt

%files rpm-devel
%_prefix/lib/rpm/

%changelog
