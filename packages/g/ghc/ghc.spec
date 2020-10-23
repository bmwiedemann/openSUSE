#
# spec file for package ghc
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


%ifnarch %{arm} s390x
%define with_libnuma 1
%else
%define with_libnuma 0
%endif

%global unregisterised_archs s390 s390x riscv64
%define full_version 8.10.2

Name:           ghc
Version:        8.10.2
Release:        0
URL:            https://www.haskell.org/ghc/
Source:         https://downloads.haskell.org/~ghc/%{full_version}/ghc-%{version}-src.tar.xz
Source1:        https://downloads.haskell.org/~ghc/%{full_version}/ghc-%{version}-src.tar.xz.sig
Source2:        ghc-rpmlintrc
Summary:        The Glorious Glasgow Haskell Compiler
License:        BSD-3-Clause
Group:          Development/Languages/Other
ExclusiveArch:  aarch64 %{arm} %{ix86} x86_64 ppc64 ppc64le riscv64 s390x
BuildRequires:  binutils-devel
BuildRequires:  gcc
BuildRequires:  ghc-bootstrap >= 8.6
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  glibc-devel
BuildRequires:  gmp-devel
BuildRequires:  libdw-devel
BuildRequires:  libelf-devel
BuildRequires:  libffi-devel
BuildRequires:  libtool
BuildRequires:  memory-constraints
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
BuildRequires:  xz
%ifarch aarch64 %{arm}
BuildRequires:  binutils-gold
%endif
%ifarch aarch64 %{arm} %{ix86} x86_64
%if 0%{?suse_version} >= 1550
BuildRequires:  llvm9
BuildRequires:  llvm9-devel
BuildRequires:  clang9 
%else
BuildRequires:  llvm
BuildRequires:  llvm-devel
BuildRequires:  clang 
%endif
%endif
%if %{undefined without_manual}
BuildRequires:  python3-Sphinx
%endif

%if %with_libnuma
BuildRequires:  libnuma-devel
%endif


BuildRequires:  ghc-bootstrap-helpers
PreReq:         update-alternatives

Requires:       ghc-compiler = %{version}-%{release}
Requires:       ghc-ghc-devel = %{version}-%{release}
Requires:       ghc-libraries = %{version}-%{release}

# PATCH-FIX-UPSTREAM Disable-unboxed-arrays.patch ptrommler@icloud.com -- Do not use unboxed arrays on big-endian platforms. See Haskell Trac #15411.
Patch3:         Disable-unboxed-arrays.patch
# PATCH-FIX-UPSTREAM ghc-pie.patch - set linux as default PIE platform
Patch35:        ghc-pie.patch
# PATCH-FIX-OPENSUSE ghc-8.0.2-Cabal-dynlibdir.patch -- Fix shared library directory location.
Patch100:       ghc-8.0.2-Cabal-dynlibdir.patch
# PATCH-FIX-UPSTREAM buildpath-abi-stability.patch -- debian patch for more stable abi-1
Patch110:       buildpath-abi-stability.patch

%description
Haskell is the standard purely functional programming language; the
current language version is Haskell 98, agreed in December 1998.

GHC is a state-of-the-art programming suite for Haskell.  Included is
an optimising compiler generating good code for a variety of
platforms, together with an interactive system for convenient, quick
development.  The distribution includes space and time profiling
facilities, a large collection of libraries, and support for various
language extensions, including concurrency, exceptions, and foreign
language interfaces (C, C++, etc).

A wide variety of Haskell related resources (tutorials, libraries,
specifications, documentation, compilers, interprbeters, references,
contact information, links to research groups) are available from the
Haskell home page at <http://www.haskell.org/>.

%package compiler
Summary:        GHC compiler and utilities
Group:          Development/Languages/Other
Requires:       gcc
Requires:       ghc-base-devel
Requires(post): update-alternatives
Requires(postun): update-alternatives
%ifarch aarch64 %{arm}
Requires:       binutils-gold
%endif
%ifarch aarch64 %{arm}
%if 0%{?suse_version} >= 1550
Requires:       clang9
Requires:       llvm9
%else
Requires:       llvm
Requires:       clang 
%endif
%endif
%ifarch x86_64 %{ix86}
%if 0%{?suse_version} >= 1550
Suggests:       clang9 
Suggests:       llvm9
%else
Suggests:       llvm
Suggests:       clang
%endif
%endif

%description compiler
This package contains the GHC compiler, tools and utilities.

The GHC libraries are provided by ghc-devel.
To install all of GHC install package ghc.

%global ghc_version_override %{version}

%global ghc_pkg_c_deps ghc-compiler = %{ghc_version_override}-%{release}

%if %with_libnuma
%define libnuma_dep ,libnuma-devel
%else
%define libnuma_dep %{nil}
%endif

%if %{defined ghclibdir}
#!ForceMultiversion
%ghc_lib_subpackage -d Cabal-3.2.0.0
%ghc_lib_subpackage -d array-0.5.4.0
%ghc_lib_subpackage -d -c gmp-devel,libffi-devel,libdw-devel,libelf-devel%{libnuma_dep} base-4.14.1.0
%ghc_lib_subpackage -d binary-0.8.8.0
%ghc_lib_subpackage -d bytestring-0.10.10.0
%ghc_lib_subpackage -d containers-0.6.2.1
%ghc_lib_subpackage -d deepseq-1.4.4.0
%ghc_lib_subpackage -d directory-1.3.6.0
%ghc_lib_subpackage -d exceptions-0.10.4 
%ghc_lib_subpackage -d filepath-1.4.2.1
%ghc_lib_subpackage -d -x ghc-%{ghc_version_override}
%ghc_lib_subpackage -d ghc-boot-%{ghc_version_override}
%ghc_lib_subpackage -d ghc-boot-th-%{ghc_version_override}
%ghc_lib_subpackage -d ghc-compact-0.1.0.0
%ghc_lib_subpackage -d ghc-heap-%{ghc_version_override}
%ghc_lib_subpackage -d -x ghci-%{ghc_version_override}
%ghc_lib_subpackage -d haskeline-0.8.0.1
%ghc_lib_subpackage -d hpc-0.6.1.0
%ghc_lib_subpackage -d libiserv-%{ghc_version_override}
%ghc_lib_subpackage -d mtl-2.2.2
%ghc_lib_subpackage -d parsec-3.1.14.0
%ghc_lib_subpackage -d pretty-1.1.3.6
%ghc_lib_subpackage -d process-1.6.9.0
%ghc_lib_subpackage -d stm-2.5.0.0
%ghc_lib_subpackage -d template-haskell-2.16.0.0
%ghc_lib_subpackage -d -c ncurses-devel terminfo-0.4.1.4
%ghc_lib_subpackage -d text-1.2.3.2
%ghc_lib_subpackage -d time-1.9.3
%ghc_lib_subpackage -d transformers-0.5.6.2
# 2.8.0.0
%ghc_lib_subpackage -d unix-2.7.2.2
%ghc_lib_subpackage -d xhtml-3000.2.2.1
%endif

%global version %{ghc_version_override}

%package libraries
Summary:        GHC development libraries meta package
Group:          Development/Libraries/Other
Requires:       ghc-compiler = %{version}-%{release}
Obsoletes:      ghc-devel < %{version}-%{release}
Provides:       ghc-devel = %{version}-%{release}
Obsoletes:      ghc-prof < %{version}-%{release}
Provides:       ghc-prof = %{version}-%{release}
%{?ghc_packages_list:Requires: %(echo %{ghc_packages_list} | sed -e "s/\([^ ]*\)-\([^ ]*\)/ghc-\1-devel = \2-%{release},/g")}

%description libraries
This is a meta-package for all the development library packages in GHC
except the ghc library, which is installed by the toplevel ghc metapackage.

%prep
%setup -q
%ifarch ppc64 s390 s390x
%patch3 -p1
%endif
%patch35 -p1
%patch100 -p1
%patch110 -p1

%build
cat > mk/build.mk <<EOF
%ifarch aarch64 %{arm}
BuildFlavour = perf-llvm
%else
BuildFlavour = perf
%endif
EOF

# BuildFlavours are defined in mk/build.mk.sample
cat mk/build.mk.sample >> mk/build.mk
# override some settings
cat >> mk/build.mk << EOF
GhcLibWays = v %{!?ghc_without_shared:dyn} %{!?without_prof:p}
%if %{defined ghc_without_shared}
DYNAMIC_BY_DEFAULT   = NO
DYNAMIC_GHC_PROGRAMS = NO
%endif
%ifarch  %{unregisterised_archs}
GhcUnregisterised    = YES
GhcWithNativeCodeGen = NO
SRC_HC_OPTS          = -O -H64m
GhcStage1HcOpts      = -O
GhcStage2HcOpts      = -O
GhcHcOpts            = -Rghc-timing
GhcLibHcOpts         = -O
SRC_HC_OPTS         += -optc-fno-builtin -optc-Wno-return-type
SRC_CC_OPTS         += -fno-builtin -Wno-return-type
%endif
%if %{defined without_haddock}
HADDOCK_DOCS = NO
%endif
BUILD_SPHINX_PS   = NO
%if %{defined without_manual}
BUILD_SPHINX_HTML = NO
BUILD_SPHINX_PDF  = NO
%endif
%if %{defined without_hscolour}
HSCOLOUR_SRCS = NO
%endif
EOF

export CFLAGS="${CFLAGS:-%optflags}"
./configure --prefix=%{_prefix} --exec-prefix=%{_exec_prefix} \
  --bindir=%{_bindir} --sbindir=%{_sbindir} --sysconfdir=%{_sysconfdir} \
  --datadir=%{_datadir} --includedir=%{_includedir} --libdir=%{_libdir} \
  --libexecdir=%{_libexecdir} --localstatedir=%{_localstatedir} \
  --sharedstatedir=%{_sharedstatedir} --mandir=%{_mandir} \
%ifarch %{unregisterised_archs}
  --enable-unregisterised \
%endif
  --with-system-libffi
  
%if 0%{?suse_version} >= 1500
%ifarch %{unregisterised_archs}
%if 0%{?qemu_user_space_build}
%limit_build -m 15000
%else
%limit_build -m 8000
%endif
%else
%limit_build -m 2000
%endif
make %{?_smp_mflags}
%else 
make -j 2
%endif


%install
%makeinstall

for i in %{ghc_packages_list}; do
name=$(echo $i | sed -e "s/\(.*\)-.*/\1/")
ver=$(echo $i | sed -e "s/.*-\(.*\)/\1/")
%ghc_gen_filelists $name $ver
# TODO: containers have license in $name/$name
#echo "%%doc libraries/$name/LICENSE" >> ghc-$name.files
done

# ghc-base should own ghclibdir
echo "%dir %{ghclibdir}" >> ghc-base.files

%ghc_gen_filelists ghc %{ghc_version_override}
%ghc_gen_filelists ghci %{ghc_version_override}
%ghc_gen_filelists ghc-prim 0.6.1
%ghc_gen_filelists integer-gmp 1.0.3.0

%define merge_filelist()\
cat ghc-%1.files >> ghc-%2.files\
cat ghc-%1-devel.files >> ghc-%2-devel.files\
cp -p libraries/%1/LICENSE libraries/LICENSE.%1\
echo "%doc libraries/LICENSE.%1" >> ghc-%2.files

%merge_filelist integer-gmp base
%merge_filelist ghc-prim base

%if %{undefined ghc_without_shared}
echo %%dir %{ghclibdir}/rts >> ghc-base.files
ls %{buildroot}%{ghclibdir}/rts/libHS*.so >> ghc-base.files
sed -i -e "s|^%{buildroot}||g" ghc-base.files
%endif
echo %%dir %{ghclibdir}/rts >> ghc-base-devel.files
ls -d %{buildroot}%{ghclibdir}/rts/libHS*.a  %{buildroot}%{ghclibdir}/package.conf.d/rts.conf %{buildroot}%{ghclibdir}/include >> ghc-base-devel.files
sed -i -e "s|^%{buildroot}||g" ghc-base-devel.files

# these are handled as alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
for i in hsc2hs runhaskell; do
  if [ -x %{buildroot}%{_bindir}/$i-ghc ]; then
    rm %{buildroot}%{_bindir}/$i
  else
    mv %{buildroot}%{_bindir}/$i{,-ghc}
  fi
  ln -s -f %{_sysconfdir}/alternatives/$i %{buildroot}%{_bindir}/$i
  touch %{buildroot}%{_sysconfdir}/alternatives/$i
done

find %{buildroot}%{ghclibdocdir} -name LICENSE -exec rm '{}' ';'

%check
# Actually, I took this from Jens Petersen's Fedora package
# stolen from ghc6/debian/rules:
# Do some very simple tests that the compiler actually works
rm -rf testghc
mkdir testghc
echo 'main = putStrLn "Foo"' > testghc/foo.hs
inplace/bin/ghc-stage2 testghc/foo.hs -o testghc/foo
[ "$(testghc/foo)" = "Foo" ]
# doesn't seem to work inplace:
#[ "$(inplace/bin/runghc testghc/foo.hs)" = "Foo" ]
rm testghc/*
echo 'main = putStrLn "Foo"' > testghc/foo.hs
inplace/bin/ghc-stage2 testghc/foo.hs -o testghc/foo -O2
[ "$(testghc/foo)" = "Foo" ]
rm testghc/*
%if %{undefined ghc_without_shared}
echo 'main = putStrLn "Foo"' > testghc/foo.hs
#inplace/bin/ghc-stage2 testghc/foo.hs -o testghc/foo -dynamic
#[ "$(testghc/foo)" = "Foo" ]
rm testghc/*
%endif

%post compiler
# Alas, GHC, Hugs and nhc all come with different set of tools in addition to
# a runFOO:
#
#   * GHC:  hsc2hs
#   * Hugs: hsc2hs, cpphs
#   * nhc:  cpphs
#
# Therefore it is currently not possible to use --slave below to form link
# groups under a single name 'runhaskell'. Either these tools should be
# disentangled from the Haskell implementations or all implementations should
# have the same set of tools. *sigh*
%{_sbindir}/update-alternatives --install %{_bindir}/runhaskell runhaskell %{_bindir}/runghc     500
%{_sbindir}/update-alternatives --install %{_bindir}/hsc2hs     hsc2hs     %{_bindir}/hsc2hs-ghc 500

%preun compiler
if test "$1" = 0; then
  %{_sbindir}/update-alternatives --remove runhaskell %{_bindir}/runghc
  %{_sbindir}/update-alternatives --remove hsc2hs     %{_bindir}/hsc2hs-ghc
fi

%files
%license LICENSE

%files compiler
%license LICENSE
%{_bindir}/ghc
%{_bindir}/ghc-%{version}
%{_bindir}/ghc-pkg
%{_bindir}/ghc-pkg-%{version}
%{_bindir}/ghci
%{_bindir}/ghci-%{version}
%{_bindir}/hp2ps
%{_bindir}/hpc
%{_bindir}/hsc2hs
%ghost %{_sysconfdir}/alternatives/hsc2hs
%{_bindir}/hsc2hs-ghc
%{_bindir}/runghc
%{_bindir}/runghc-%{version}
%{_bindir}/runhaskell
%ghost %{_sysconfdir}/alternatives/runhaskell
%{_bindir}/runhaskell-ghc
%dir %{ghclibdir}
%{ghclibdir}/settings
%dir %{ghclibdir}/bin
%{ghclibdir}/bin/ghc
%{ghclibdir}/bin/ghc-pkg
%{ghclibdir}/bin/ghc-iserv
%{ghclibdir}/bin/ghc-iserv-dyn
%{ghclibdir}/bin/ghc-iserv-prof
%{ghclibdir}/bin/hp2ps
%{ghclibdir}/bin/hpc
%{ghclibdir}/bin/hsc2hs
%{ghclibdir}/ghc-usage.txt
%{ghclibdir}/ghci-usage.txt
%dir %{ghclibdir}/package.conf.d
%ghost %{ghclibdir}/package.conf.d/package.cache
%ghost %{ghclibdir}/package.conf.d/package.cache.lock
%{ghclibdir}/platformConstants
%{ghclibdir}/bin/runghc
%{ghclibdir}/template-hsc.h
%{ghclibdir}/bin/unlit
%dir %{_datadir}/doc/ghc-%{version}
%dir %{ghcdocbasedir}
%dir %{ghcdocbasedir}/libraries
%if %{undefined without_manual}
%{_mandir}/man1/ghc.*
%endif
%if %{undefined without_haddock}
%{_bindir}/haddock
%{_bindir}/haddock-ghc-%{version}
%{ghclibdir}/html
%{ghclibdir}/latex
%{ghclibdir}/llvm-passes
%{ghclibdir}/llvm-targets
%{ghclibdir}/bin/haddock
%if %{undefined without_manual}
%{ghcdocbasedir}/haddock
%{ghcdocbasedir}/users_guide
%endif
%{ghcdocbasedir}/libraries/gen_contents_index
%{ghcdocbasedir}/libraries/*.css
%{ghcdocbasedir}/libraries/prologue.txt
%{ghcdocbasedir}/libraries/synopsis.png
%{ghcdocbasedir}/index.html
%ghost %{ghcdocbasedir}/libraries/doc-index*.html
%ghost %{ghcdocbasedir}/libraries/haddock-bundle.min.js
%ghost %{ghcdocbasedir}/libraries/haddock-util.js
%ghost %{ghcdocbasedir}/libraries/index*.html
%ghost %{ghcdocbasedir}/libraries/minus.gif
%ghost %{ghcdocbasedir}/libraries/plus.gif
%endif

%files libraries
%license LICENSE

%changelog
