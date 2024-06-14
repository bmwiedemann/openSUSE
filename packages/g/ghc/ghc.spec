#
# spec file for package ghc
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


%define full_version 9.8.2
%define short_version 9.8.2

%ifnarch s390x
%define with_libnuma 1
%else
%define with_libnuma 0
%endif

%global llvm_major 14

# conditionals

# disable prof, docs, perf build
# bcond_with for production builds: disable quick build
%bcond_with quickbuild

# make sure ghc libraries' ABI hashes unchanged (ghcX.Y not supported yet)
%bcond_with abicheck

# bcond_without for production builds: use Hadrian buildsystem
%bcond_without hadrian

# bcond_without for production builds: build hadrian
%bcond_without build_hadrian

# bcond_without for production builds: enable debuginfo
%bcond_without ghc_debuginfo

%if %{without ghc_debuginfo}
%undefine _enable_debug_packages
%endif

# build profiling libraries
# build haddock
# perf production build (disable for quick build)
%if %{with quickbuild}
%undefine with_ghc_prof
%undefine with_haddock
%bcond_with perf_build
%else
%bcond_without ghc_prof
%bcond_without haddock
%bcond_without manual
%bcond_without perf_build
%endif

%if %{without hadrian}
# locked together since disabling haddock causes no manuals built
# and disabling haddock still created index.html
# https://gitlab.haskell.org/ghc/ghc/-/issues/15190
%{?with_haddock:%bcond_without manual}
%endif

%global ghc_llvm_archs s390x riscv64
%global ghc_unregisterized_arches noarch

%global base_ver 4.19.1.0
%global ghc_compact_ver 0.1.0.0
%global hpc_ver 0.7.0.0
%global hsc2hs_ver 0.68.8
%global ghc_bignum_ver 1.3

Name:           ghc
Version:        %{short_version}
Release:        0
Summary:        The Glorious Glasgow Haskell Compiler
License:        BSD-3-Clause
URL:            https://www.haskell.org/ghc/
Source:         https://downloads.haskell.org/~ghc/%{full_version}/ghc-%{version}-src.tar.xz
Source2:        ghc-rpmlintrc
Source4:        9_4_4-bootstrap-sources.tar.gz
Source5:        ghc-pkg.man
Source6:        haddock.man
Source7:        runghc.man
Patch1:         ghc-gen_contents_index-haddock-path.patch
# https://ghc.haskell.org/trac/ghc/ticket/15689
Patch2:         ghc-Cabal-install-PATH-warning.patch
# PATCH-FIX-UPSTREAM Disable-unboxed-arrays.patch ptrommler@icloud.com -- Do not use unboxed arrays on big-endian platforms. See Haskell Trac #15411.
Patch3:         Disable-unboxed-arrays.patch
# PATCH-FIX-UPSTREAM Hadrian: enable GHCi support on riscv64 (dd38aca95a)
Patch100:       ghc-with-interpreter.patch
# PATCH-FIX-UPSTREAM libraries/Cabal: Add support for the 64-bit RISC-V architecture (d89526f98)
Patch101:       cabal-riscv64.patch
Patch200:       ghc-hadrian-s390x-rts--qg.patch
BuildRequires:  binutils-devel
BuildRequires:  gcc-PIE
BuildRequires:  gcc-c++
BuildRequires:  ghc-bootstrap >= 9.4
BuildRequires:  ghc-bootstrap-helpers >= 1.3
BuildRequires:  ghc-rpm-macros-extra => 2.6.1
BuildRequires:  glibc-devel
BuildRequires:  gmp-devel
BuildRequires:  libdw-devel
BuildRequires:  libelf-devel
BuildRequires:  libffi-devel
BuildRequires:  libtool
%ifarch %{ghc_llvm_archs}
BuildRequires:  clang%{llvm_major}
BuildRequires:  llvm%{llvm_major}
BuildRequires:  llvm%{llvm_major}-devel
%endif
BuildRequires:  memory-constraints
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  xz
Requires:       %{name}-compiler = %{version}-%{release}
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-ghc-boot-devel = %{version}-%{release}
Requires:       %{name}-ghc-compact-devel = %{ghc_compact_ver}-%{release}
Requires:       %{name}-ghc-devel = %{version}-%{release}
Requires:       %{name}-ghc-heap-devel = %{version}-%{release}
Requires:       %{name}-ghci-devel = %{version}-%{release}
Requires:       %{name}-hpc-devel = %{hpc_ver}-%{release}
Recommends:     %{name}-compiler-default = %{version}-%{release}
%if %{without ghc_debuginfo}
%undefine _enable_debug_packages
%endif
%if %{with manual}
BuildRequires:  python3-Sphinx
%endif
%if %{with_libnuma}
BuildRequires:  libnuma-devel
%endif
%if %{with haddock}
Suggests:       %{name}-doc = %{version}-%{release}
Suggests:       %{name}-doc-index = %{version}-%{release}
%endif
%if %{with manual}
Suggests:       %{name}-manual = %{version}-%{release}
%endif
%if %{with ghc_prof}
Suggests:       %{name}-prof = %{version}-%{release}
%endif

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
License:        BSD-3-Clause
Requires:       %{name}-filesystem = %{version}-%{release}
Requires:       gcc
Requires:       ghc-base-devel = %{base_ver}-%{release}
Provides:       hsc2hs-%{hsc2hs_ver}-%{release}
%ifarch riscv64 s390x
Requires:       clang%{llvm_major}
Requires:       llvm%{llvm_major}
%endif

%description compiler
This package contains the GHC compiler, tools and utilities.

The GHC libraries are provided by ghc-devel.
To install all of GHC install package ghc.


%if %{with haddock} || (%{with hadrian} && %{with manual})
%package doc
Summary:        Haskell library documentation meta package
License:        BSD-3-Clause

%description doc
Installing this package causes %{name}-*-doc packages corresponding to
%{name}-*-devel packages to be automatically installed too.

%package doc-index
Summary:        GHC library documentation indexing
License:        BSD-3-Clause
Requires:       %{name}-compiler = %{version}-%{release}
BuildArch:      noarch

%description doc-index
The package enables re-indexing of installed library documention.

%package filesystem
Summary:        Shared directories for Haskell documentation
License:        BSD-3-Clause
BuildArch:      noarch

%description filesystem
This package provides some common directories used for
Haskell libraries documentation.
%endif

%if %{with manual}
%package manual
Summary:        GHC manual
License:        BSD-3-Clause
Requires:       %{name}-filesystem = %{version}-%{release}
BuildArch:      noarch

%description manual
This package provides the User Guide and Haddock manual.
%endif

%global ghc_version_override %{version}
%global ghc_pkg_c_deps ghc-compiler = %{ghc_version_override}-%{release}
%global version %{ghc_version_override}
%if %{with_libnuma}
%define libnuma_dep ,libnuma-devel
%else
%define libnuma_dep %{nil}
%endif
#!ForceMultiversion
%ghc_lib_subpackage -d Cabal-3.10.2.0
%ghc_lib_subpackage -d Cabal-syntax-3.10.2.0
%ghc_lib_subpackage -d array-0.5.6.0
%ghc_lib_subpackage -d -c gmp-devel,libffi-devel,libdw-devel,libelf-devel%{libnuma_dep} base-%{base_ver}
%ghc_lib_subpackage -d binary-0.8.9.1
%ghc_lib_subpackage -d -x ghc-bignum-%{ghc_bignum_ver}
%ghc_lib_subpackage -d bytestring-0.12.1.0
%ghc_lib_subpackage -d containers-0.6.8
%ghc_lib_subpackage -d deepseq-1.5.0.0
%ghc_lib_subpackage -d directory-1.3.8.1
%ghc_lib_subpackage -d exceptions-0.10.7
%ghc_lib_subpackage -d filepath-1.4.200.1
%ghc_lib_subpackage -d -x ghc-%{ghc_version_override}
%ghc_lib_subpackage -d -x ghc-boot-%{ghc_version_override}
%ghc_lib_subpackage -d ghc-boot-th-%{ghc_version_override}
%ghc_lib_subpackage -d -x ghc-compact-%{ghc_compact_ver}
%ghc_lib_subpackage -d -x ghc-heap-%{ghc_version_override}
%ghc_lib_subpackage -d -x ghci-%{ghc_version_override}
%ghc_lib_subpackage -d haskeline-0.8.2.1
%ghc_lib_subpackage -d -x hpc-%{hpc_ver}
%ghc_lib_subpackage -d mtl-2.3.1
%ghc_lib_subpackage -d parsec-3.1.17.0
%ghc_lib_subpackage -d pretty-1.1.3.6
%ghc_lib_subpackage -d process-1.6.18.0
%ghc_lib_subpackage -d semaphore-compat-1.0.0
%ghc_lib_subpackage -d stm-2.5.2.1
%ghc_lib_subpackage -d template-haskell-2.21.0.0
%ghc_lib_subpackage -d -c ncurses-devel terminfo-0.4.1.6
%ghc_lib_subpackage -d text-2.1.1
%ghc_lib_subpackage -d time-1.12.2
%ghc_lib_subpackage -d transformers-0.6.1.0
%ghc_lib_subpackage -d unix-2.8.4.0
%ghc_lib_subpackage -d xhtml-3000.2.2.1

%global version %{ghc_version_override}

%package devel
Summary:        GHC development libraries meta package
Requires:       ghc-compiler = %{version}-%{release}
Obsoletes:      ghc-libraries < %{version}-%{release}
Provides:       ghc-libraries = %{version}-%{release}
%{?ghc_packages_list:Requires: %(echo %{ghc_packages_list} | sed -e "s/\([^ ]*\)-\([^ ]*\)/%{name}-\1-devel = \2-%{release},/g")}

%description devel
This is a meta-package for all the development library packages in GHC
except the ghc library, which is installed by the toplevel ghc metapackage.

%if %{with ghc_prof}
%package prof
Summary:        GHC profiling libraries meta package
License:        BSD-3-Clause
Requires:       %{name}-compiler = %{version}-%{release}

%description prof
Installing this package causes %{name}-*-prof packages corresponding to
%{name}-*-devel packages to be automatically installed too.
%endif

%prep
%setup -q
%patch -P 1 -p1
%patch -P 2 -p1
%ifarch s390x
%patch -P 3 -p1
%endif
%patch -P 100 -p1
%patch -P 101 -p1
%ifarch ppc64le s390x riscv64
%patch -P 200 -p1
%endif

rm libffi-tarballs/libffi-*.tar.gz

%build
cp %{SOURCE4} ./
hadrian/bootstrap/bootstrap.py --bootstrap-sources 9_4_4-bootstrap-sources.tar.gz

%global hadrian _build/bin/hadrian

%ghc_set_gcc_flags

export CC=%{_bindir}/gcc
export LD=%{_bindir}/ld
export LANG=C.utf8

autoupdate

python3 boot.source --hadrian

./configure --prefix=%{_prefix} --exec-prefix=%{_exec_prefix} \
  --bindir=%{_bindir} --sbindir=%{_sbindir} --sysconfdir=%{_sysconfdir} \
  --datadir=%{_datadir} --includedir=%{_includedir} --libdir=%{_libdir} \
  --libexecdir=%{_libexecdir} --localstatedir=%{_localstatedir} \
  --sharedstatedir=%{_sharedstatedir} --mandir=%{_mandir} \
  --docdir=%{_docdir}/%{name}-%{version} \
  --with-system-libffi \
%ifarch %{ghc_unregisterized_arches}
  --enable-unregisterised \
%endif
%{nil}

%undefine _ghcdynlibdir

%ifarch %{ghc_llvm_archs}
%global hadrian_llvm +llvm
%endif
%define hadrian_docs %{!?with_haddock:--docs=no-haddocks} %{!?with_manual:--docs=no-sphinx}%{?with_manual:--docs=no-sphinx-pdfs --docs=no-sphinx-man}

%if 0%{?suse_version} >= 1500
%ifarch %{unregisterised_archs} riscv64
%if 0%{?qemu_user_space_build}
%limit_build -m 15000
%else
%limit_build -m 8000
%endif
%else
%limit_build -m 2000
%endif
%global jobs_nr %{?_smp_mflags}
%else
%global jobs_nr -j1
%endif
%{hadrian} %{jobs_nr} --flavour=%{?with_quickbuild:quick+no_profiled_libs}%{!?with_quickbuild:perf%{!?with_ghc_prof:+no_profiled_libs}}%{?hadrian_llvm} %{hadrian_docs} binary-dist-dir --hash-unit-ids

%install

(
cd _build/bindist/ghc-%{version}-*
./configure --prefix=%{buildroot}%{ghclibdir} --bindir=%{buildroot}%{_bindir} --libdir=%{buildroot}%{_libdir} --mandir=%{buildroot}%{_mandir} --docdir=%{buildroot}%{_docdir}/%{name}-%{version}
make install
)
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{ghclibplatform}" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}.conf

# avoid 'E: binary-or-shlib-defines-rpath'
for i in $(find %{buildroot} -type f -executable -exec sh -c "file {} | grep -q 'dynamically linked'" \; -print); do
  chrpath -d $i
done

%if %{with haddock}
# remove short hashes
for d in %{buildroot}%{ghc_html_libraries_dir}/*/; do
mv $d $(echo $d | sed -e "s/\(.*\)-.*/\\1/")
done
%endif

# containers src moved to a subdir
cp -p libraries/containers/containers/LICENSE libraries/containers/LICENSE
# hack for Cabal-syntax/LICENSE
mkdir -p libraries/Cabal-syntax
cp -p libraries/Cabal/Cabal-syntax/LICENSE libraries/Cabal-syntax

rm -f %{name}-*.files

# FIXME replace with ghc_subpackages_list
for i in %{ghc_packages_list}; do
name=$(echo $i | sed -e "s/\(.*\)-.*/\1/")
ver=$(echo $i | sed -e "s/.*-\(.*\)/\1/")
%ghc_gen_filelists $name $ver
echo "%%license libraries/$name/LICENSE" >> %{name}-$name.files
done

echo "%%dir %{ghclibdir}" >> %{name}-base%{?_ghcdynlibdir:-devel}.files

%ghc_gen_filelists ghc %{ghc_version_override}
%ghc_gen_filelists ghc-boot %{ghc_version_override}
%ghc_gen_filelists ghc-bignum %{ghc_bignum_ver}
%ghc_gen_filelists ghc-compact %{ghc_compact_ver}
%ghc_gen_filelists ghc-heap %{ghc_version_override}
%ghc_gen_filelists ghci %{ghc_version_override}
%ghc_gen_filelists hpc %{hpc_ver}

%ghc_gen_filelists ghc-prim 0.11.0
%ghc_gen_filelists integer-gmp 1.1
%ghc_gen_filelists rts 1.0.2

%ghc_merge_filelist ghc-prim base
%ghc_merge_filelist integer-gmp base
%ghc_merge_filelist rts base

# add rts libs
for i in %{buildroot}%{ghclibplatform}/libHSrts*ghc%{ghc_version}.so; do
  echo $i >> %{name}-base.files
done
echo "%{_sysconfdir}/ld.so.conf.d/%{name}.conf" >> %{name}-base.files
if [ -f %{buildroot}%{ghcliblib}/package.conf.d/system-cxx-std-lib-1.0.conf ]; then
ls -d %{buildroot}%{ghcliblib}/package.conf.d/system-cxx-std-lib-1.0.conf >> %{name}-base-devel.files
fi

%if %{with ghc_prof}
ls %{buildroot}%{ghclibdir}/bin/ghc-iserv-prof* >> %{name}-base-prof.files
ls %{buildroot}%{ghclibdir}/lib/bin/ghc-iserv-prof >> %{name}-base-prof.files
echo "%%dir %{ghcliblib}/bin"
%endif

sed -i -e "s|^%{buildroot}||g" %{name}-base*.files
sed -i -e "s|%{buildroot}||g" %{buildroot}%{_bindir}/*

%if %{with haddock}
rm %{buildroot}%{_docdir}/ghc-%{version}/archives/libraries.html.tar.xz
%endif
%if %{with manual}
rm %{buildroot}%{_docdir}/ghc-%{version}/archives/Haddock.html.tar.xz
rm %{buildroot}%{_docdir}/ghc-%{version}/archives/users_guide.html.tar.xz
%endif

mkdir -p %{buildroot}%{_mandir}/man1
install -p -m 0644 %{SOURCE5} %{buildroot}%{_mandir}/man1/ghc-pkg.1
install -p -m 0644 %{SOURCE6} %{buildroot}%{_mandir}/man1/haddock.1
install -p -m 0644 %{SOURCE7} %{buildroot}%{_mandir}/man1/runghc.1

rm %{buildroot}%{ghclibdir}/lib/package.conf.d/.stamp
rm %{buildroot}%{ghclibdir}/lib/package.conf.d/*.conf.copy

# https://gitlab.haskell.org/ghc/ghc/-/issues/24121
rm %{buildroot}%{ghclibdir}/share/doc/%{ghcplatform}/*/LICENSE

(
cd %{buildroot}%{ghclibdir}/lib/bin
for i in *; do
  if [ -f %{buildroot}%{ghclibdir}/bin/$i ]; then
     ln -sf ../../bin/$i
  fi
done
)

%check
# Actually, I took this from Jens Petersen's Fedora package
# stolen from ghc6/debian/rules:
#Do some very simple tests that the compiler actually works
export LANG=C.utf8
export LD_LIBRARY_PATH=%{buildroot}%{ghclibplatform}:
GHC=%{buildroot}%{ghclibdir}/bin/ghc
# Do some very simple tests that the compiler actually works
rm -rf testghc
mkdir testghc
echo 'main = putStrLn "Foo"' > testghc/foo.hs
$GHC testghc/foo.hs -o testghc/foo
[ "$(testghc/foo)" = "Foo" ]
rm testghc/*
echo 'main = putStrLn "Foo"' > testghc/foo.hs
$GHC testghc/foo.hs -o testghc/foo -O2
[ "$(testghc/foo)" = "Foo" ]
rm testghc/*
echo 'main = putStrLn "Foo"' > testghc/foo.hs
$GHC testghc/foo.hs -o testghc/foo -dynamic
[ "$(testghc/foo)" = "Foo" ]
rm testghc/*

$GHC --info

%transfiletriggerin compiler -- %{ghcliblib}/package.conf.d
%ghc_pkg_recache
%end

%transfiletriggerpostun compiler -- %{ghcliblib}/package.conf.d
%ghc_pkg_recache
%end

%files
%license LICENSE

%files compiler
%license LICENSE
%doc README.md
%{_bindir}/ghc-%{version}
%{_bindir}/ghc-pkg-%{version}
%{_bindir}/ghci-%{version}
%{_bindir}/hp2ps-%{?with_hadrian:ghc-}%{version}
%{_bindir}/hpc-%{?with_hadrian:ghc-}%{version}
%{_bindir}/hsc2hs-%{?with_hadrian:ghc-}%{version}
%{_bindir}/runghc-%{version}
%{_bindir}/runhaskell-%{version}
%{_bindir}/ghc
%{_bindir}/ghc-pkg
%{_bindir}/ghci
%{_bindir}/haddock
%{_bindir}/hp2ps
%{_bindir}/hpc
%{_bindir}/hsc2hs
%{_bindir}/runghc
%{_bindir}/runhaskell
%dir %{ghclibdir}
%dir %{ghcliblib}
%dir %{ghcliblib}/%{ghcplatform}
%dir %{ghclibdir}/bin
%dir %{ghcliblib}/bin
%{ghclibdir}/bin/ghc
%{ghclibdir}/bin/ghc-iserv
%{ghclibdir}/bin/ghc-iserv-dyn
%{ghclibdir}/bin/ghc-pkg
%{ghclibdir}/bin/hpc
%{ghclibdir}/bin/hsc2hs
%{ghclibdir}/bin/runghc
%{ghclibdir}/bin/hp2ps
%{ghclibdir}/bin/unlit
%{ghclibdir}/bin/ghc-%{version}
%{ghclibdir}/bin/ghc-iserv-ghc-%{version}
%{ghclibdir}/bin/ghc-iserv-dyn-ghc-%{version}
%{ghclibdir}/bin/ghc-pkg-%{version}
%{ghclibdir}/bin/haddock
%{ghclibdir}/bin/haddock-ghc-%{version}
%{ghclibdir}/bin/hp2ps-ghc-%{version}
%{ghclibdir}/bin/hpc-ghc-%{version}
%{ghclibdir}/bin/hsc2hs-ghc-%{version}
%{ghclibdir}/bin/runghc-%{version}
%{ghclibdir}/bin/runhaskell
%{ghclibdir}/bin/runhaskell-%{version}
%{ghclibdir}/bin/unlit-ghc-%{version}
%{ghclibdir}/lib/bin/ghc-iserv
%{ghclibdir}/lib/bin/ghc-iserv-dyn
%{ghclibdir}/lib/bin/unlit
%{ghcliblib}/ghc-interp.js
%{ghcliblib}/ghc-usage.txt
%{ghcliblib}/ghci-usage.txt
%{ghcliblib}/llvm-passes
%{ghcliblib}/llvm-targets
%dir %{ghcliblib}/package.conf.d
%ghost %{ghcliblib}/package.conf.d/package.cache
%{ghcliblib}/package.conf.d/package.cache.lock
%{ghcliblib}/settings
%{ghcliblib}/template-hsc.h
%{_mandir}/man1/ghc-pkg.1%{?ext_man}
%{_mandir}/man1/haddock.1%{?ext_man}
%{_mandir}/man1/runghc.1%{?ext_man}
%{_bindir}/haddock-ghc-%{version}
%{ghcliblib}/html
%{ghcliblib}/latex
%if %{with haddock} || (%{with hadrian} && %{with manual})
%{ghc_html_libraries_dir}/prologue.txt
%endif
%if %{with haddock}
%verify(not size mtime) %{ghc_html_libraries_dir}/haddock-bundle.min.js
%verify(not size mtime) %{ghc_html_libraries_dir}/linuwial.css
%verify(not size mtime) %{ghc_html_libraries_dir}/quick-jump.css
%verify(not size mtime) %{ghc_html_libraries_dir}/synopsis.png
%endif
%if %{with manual} && %{without hadrian}
%{_mandir}/man1/ghc.1%{?ext_man}
%endif

%files devel

%if %{with haddock} || (%{with hadrian} && %{with manual})
%files doc
%{ghc_html_dir}/index.html

%files doc-index
%{ghc_html_libraries_dir}/gen_contents_index
%if %{with haddock}
%verify(not size mtime) %{ghc_html_libraries_dir}/doc-index*.html
%verify(not size mtime) %{ghc_html_libraries_dir}/index*.html
%endif

%files filesystem
%dir %_ghc_doc_dir
%dir %ghc_html_dir
%dir %ghc_html_libraries_dir
%endif

%if %{with manual}
%files manual
%{ghc_html_dir}/users_guide
%if %{with hadrian}
%{ghc_html_dir}/Haddock
%else
%if %{with haddock}
%{ghc_html_dir}/haddock
%endif
%endif
%endif

%if %{with ghc_prof}
%files prof
%endif

%changelog
