#
# spec file for package go1.22
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


# Specify Go toolchain version used to bootstrap this package's Go toolchain
# go_bootstrap_version bootstrap go toolchain with specific existing go1.x package
# gcc_go_version       bootstrap go toolchain with specific version of gcc-go
%if 0%{?suse_version} > 1500
# openSUSE Tumbleweed
# Usually ahead of bootstrap version specified by upstream Go
# Use Tumbleweed default gccgo and N-1 go1.x for testing
%define gcc_go_version 13
%define go_bootstrap_version go1.20
%else
# Use gccgo and go1.x specified by upstream Go
%define gcc_go_version 11
%define go_bootstrap_version go1.20
%endif

# Bootstrap go toolchain using existing go package go_bootstrap_version
# To bootstrap using gccgo use '--with gccgo'
%bcond_with gccgo

# gccgo on ppc64le with default PIE enabled fails with:
# error while loading shared libraries:
# R_PPC64_ADDR16_HA re10143fb0c for symbol `' out of range
# track https://github.com/golang/go/issues/28531
# linuxppc-dev discussion:
# "PIE binaries are no longer mapped below 4 GiB on ppc64le"
# https://lists.ozlabs.org/pipermail/linuxppc-dev/2018-November/180862.html
%ifarch ppc64le
#!BuildIgnore: gcc-PIE
%endif

# Build go-race only on platforms where C++14 is supported (SLE-15)
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} >= 150000
%define tsan_arch x86_64 aarch64 s390x ppc64le
%else
# Cannot use {nil} here (ifarch doesn't like it) so just make up a fake
# architecture that no build will ever match.
%define tsan_arch openSUSE_FAKE_ARCH
%endif

# Go has precompiled versions of LLVM's compiler-rt inside their source code.
# We cannot ship pre-compiled binaries so we have to recompile said source,
# however they vendor specific commits from upstream. This value comes from
# src/runtime/race/README (and we verify that it matches in check).
#
# In order to update the TSAN version, modify _service. See boo#1052528 for
# more details.
%define tsan_commit 51bfeff0e4b0757ff773da6882f4d538996c9b04

# go_api is the major version of Go.
# Used by go1.x packages and go metapackage for:
# RPM Provides: golang(API), RPM Requires: and rpm_vercmp
# as well as derived variables such as go_label.
%define go_api 1.22

# go_label is the configurable Go toolchain directory name.
# Used for packaging multiple Go toolchains with the same go_api.
# go_label should be defined as go_api with optional suffix, e.g.
# go_api or go_api-foo
%define go_label %{go_api}

# shared library support
%if "%{rpm_vercmp %{go_api} 1.5}" > "0"
%if %{with gccgo}
%define with_shared 1
%else
%ifarch %ix86 %arm x86_64 aarch64
%define with_shared 1
%else
%define with_shared 0
%endif
%endif
%else
%define with_shared 0
%endif
%ifarch ppc64
%define with_shared 0
%endif
# setup go_arch (BSD-like scheme)
%ifarch %ix86
%define go_arch 386
%endif
%ifarch x86_64
%define go_arch amd64
# set GOAMD64 consistently
%define go_amd64 v1
%endif
%ifarch aarch64
%define go_arch arm64
%endif
%ifarch %arm
%define go_arch arm
%endif
%ifarch ppc64
%define go_arch ppc64
%endif
%ifarch ppc64le
%define go_arch ppc64le
%endif
%ifarch s390x
%define go_arch s390x
%endif
%ifarch riscv64
%define go_arch riscv64
%endif

Name:           go1.22
Version:        1.22.5
Release:        0
Summary:        A compiled, garbage-collected, concurrent programming language
License:        BSD-3-Clause
Group:          Development/Languages/Go
URL:            https://go.dev/
Source:         https://go.dev/dl/go%{version}.src.tar.gz
Source1:        go-rpmlintrc
Source4:        README.SUSE
Source6:        go.gdbinit
# We have to compile TSAN ourselves. boo#1052528
# Preferred form when all arches share llvm race version
# Source100:      llvm-%{tsan_commit}.tar.xz
Source100:      llvm-51bfeff0e4b0757ff773da6882f4d538996c9b04.tar.xz
# PATCH-FIX-OPENSUSE: https://go-review.googlesource.com/c/go/+/391115
Patch7:         dont-force-gold-on-arm64.patch
# PATCH-FIX-UPSTREAM marguerite@opensuse.org - find /usr/bin/go-8 when bootstrapping with gcc8-go
Patch8:         gcc-go.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# boostrap
%if %{with gccgo}
BuildRequires:  gcc%{gcc_go_version}-go
%else
# no gcc-go
BuildRequires:  %{go_bootstrap_version}
%endif
BuildRequires:  fdupes
Suggests:       %{name}-doc = %{version}
%if 0%{?suse_version} > 1500
# openSUSE Tumbleweed
Suggests:       %{name}-libstd = %{version}
%endif
%ifarch %{tsan_arch}
# Needed to compile compiler-rt/TSAN.
BuildRequires:  gcc-c++
%endif
#BNC#818502 debug edit tool of rpm fails on i586 builds
BuildRequires:  rpm >= 4.11.1
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires:       gcc
Provides:       go = %{version}
Provides:       go-devel = go%{version}
Provides:       go-devel-static = go%{version}
Provides:       golang(API) = %{go_api}
Obsoletes:      go-devel < go%{version}
# go-vim/emacs were separate projects starting from 1.4
Obsoletes:      go-emacs <= 1.3.3
Obsoletes:      go-vim <= 1.3.3
ExclusiveArch:  %ix86 x86_64 %arm aarch64 ppc64 ppc64le s390x riscv64

%description
Go is an expressive, concurrent, garbage collected systems programming language
that is type safe and memory safe. It has pointers but no pointer arithmetic.
Go has fast builds, clean syntax, garbage collection, methods for any type, and
run-time reflection. It feels like a dynamic language but has the speed and
safety of a static language.

%package doc
Summary:        Go documentation
Group:          Documentation/Other
Provides:       go-doc = %{version}

%description doc
Go examples and documentation.

%ifarch %{tsan_arch}
# boo#1052528
%package race
Summary:        Go runtime race detector
Group:          Development/Languages/Go
URL:            https://compiler-rt.llvm.org/
Requires:       %{name} = %{version}
Supplements:    %{name} = %{version}
ExclusiveArch:  %{tsan_arch}

%description race
Go runtime race detector libraries. Install this package if you wish to use the
-race option, in order to detect race conditions present in your Go programs.
%endif

%if %{with_shared}
%if 0%{?suse_version} > 1500
# openSUSE Tumbleweed
%package libstd
Summary:        Go compiled shared library libstd.so
Group:          Development/Languages/Go
Provides:       go-libstd = %{version}

%description libstd
Go standard library compiled to a dynamically loadable shared object libstd.so
%endif
%endif

%prep
%ifarch %{tsan_arch}
# compiler-rt (from LLVM)
%setup -q -T -b 100 -n llvm-%{tsan_commit}
%endif

# go
%setup -q -n go
%patch -P 7 -p1
%if %{with gccgo}
# Currently gcc-go does not manage an update-alternatives entry and will
# never be symlinked as "go", even if gcc-go is the only installed go toolchain.
# Patch go bootstrap scripts to find hardcoded go-(gcc-go-version) e.g. go-8
# Substitute defined gcc_go_version into gcc-go.patch
sed -i "s/\$gcc_go_version/%{gcc_go_version}/" $RPM_SOURCE_DIR/gcc-go.patch
%patch -P 8 -p1
%endif

cp %{SOURCE4} .

%build
# Remove the pre-included .sysos, to avoid shipping things we didn't compile
# (which is against the openSUSE guidelines for packaging).
find . -type f -name '*.syso' -print -delete

# First, compile LLVM's TSAN, and replace the built-in with it. We can only do
# this for amd64.
%ifarch %{tsan_arch}
TSAN_DIR="../llvm-%{tsan_commit}/compiler-rt/lib/tsan/go"
pushd "$TSAN_DIR"
./buildgo.sh
popd
cp -v "$TSAN_DIR/race_linux_%{go_arch}.syso" src/runtime/race/
%endif

# Now, compile Go.
%if %{with gccgo}
export GOROOT_BOOTSTRAP=%{_prefix}
%else
export GOROOT_BOOTSTRAP=%{_libdir}/%{go_bootstrap_version}
%endif
# Ensure ARM arch is set properly - boo#1169832
%ifarch armv6l armv6hl
export GOARCH=arm
export GOARM=6
%endif
%ifarch armv7l armv7hl
export GOARCH=arm
export GOARM=7
%endif
%ifarch x86_64 %{?x86_64}
# use the baseline defined above. Other option is GOAMD64=v3 for x86_64_v3 support
export GOAMD64=%go_amd64
%endif
export GOROOT="`pwd`"
export GOROOT_FINAL=%{_libdir}/go/%{go_label}
export GOBIN="$GOROOT/bin"
mkdir -p "$GOBIN"
cd src
HOST_EXTRA_CFLAGS="%{optflags} -Wno-error" ./make.bash -v

cd ../
%ifarch %{tsan_arch}
# Install TSAN-friendly version of the std libraries.
bin/go install -race std
%endif

%if %{with_shared}
%if 0%{?suse_version} > 1500
# openSUSE Tumbleweed
# Compile Go standard library as a dynamically loaded shared object libstd.so
# for inclusion in a subpackage which can be installed standalone.
# Upstream Go binary releases do not ship a compiled libstd.so.
# Standard practice is to build Go binaries as a single executable.
# Upstream Go discussed removing this feature, opted to fix current support:
# Relevant upstream comments on: https://github.com/golang/go/issues/47788
#
# -buildmode=shared
#    Combine all the listed non-main packages into a single shared
#    library that will be used when building with the -linkshared
#    option. Packages named main are ignored.
#
# -linkshared
#    build code that will be linked against shared libraries previously
#    created with -buildmode=shared.
bin/go install -buildmode=shared std
%endif
%endif

%check
%ifarch %{tsan_arch}
# Make sure that we have the right TSAN checked out.
# As of go1.20, README x86_64 race_linux.syso
# includes path prefix and omits arch in filename e.g.
# internal/amd64v1/race_linux.syso
%ifarch x86_64 %{?x86_64}
grep "^internal/amd64%{go_amd64}/race_linux.syso built with LLVM %{tsan_commit}" src/runtime/race/README
%else
grep "^race_linux_%{go_arch}.syso built with LLVM %{tsan_commit}" src/runtime/race/README
%endif
%endif

%install
export GOROOT="%{buildroot}%{_libdir}/go/%{go_label}"

# remove pre-compiled .a package archives no longer used as of go1.20
# find %{_builddir}/go/pkg -name "*.a" -type f |wc -l
# 259
# TODO isolate the build step where .a files are created and delete then
find %{_builddir}/go/pkg -name "*.a" -type f -delete

# locations for third party libraries, see README-openSUSE for info about locations.
install -d  %{buildroot}%{_datadir}/go/%{go_label}/contrib
install -d  $GOROOT/contrib/pkg/linux_%{go_arch}
ln -s %{_libdir}/go/%{go_label}/contrib/pkg/ %{buildroot}%{_datadir}/go/%{go_label}/contrib/pkg
install -d  %{buildroot}%{_datadir}/go/%{go_label}/contrib/cmd
install -d  %{buildroot}%{_datadir}/go/%{go_label}/contrib/src
ln -s %{_datadir}/go/%{go_label}/contrib/src/ %{buildroot}%{_libdir}/go/%{go_label}/contrib/src
install -Dm644 README.SUSE $GOROOT/contrib/
ln -s %{_libdir}/go/%{go_label}/contrib/README.SUSE %{buildroot}%{_datadir}/go/%{go_label}/contrib/README.SUSE

# go.env sets defaults for: GOPROXY GOSUMDB GOTOOLCHAIN
install -Dm644 go.env $GOROOT/

# Change go.env GOTOOLCHAIN default to "local" so Go app builds never
# automatically download newer toolchains as specified by go.mod files.
# When GOTOOLCHAIN is set to local, the go command always runs the bundled Go toolchain.
# See https://go.dev/doc/toolchain for details.
# The default behavior "auto":
# a) Assumes network access that is not available in OBS
# b) Downloads third-party toolchain binaries that would be used in build
# Need for "auto" is rare as openSUSE and SUSE ship go1.x versions near their release date.
# The user can override the defaults in ~/.config/go/env.
sed -i "s/GOTOOLCHAIN=auto/GOTOOLCHAIN=local/" $GOROOT/go.env

# source files for go install, godoc, etc
install -d %{buildroot}%{_datadir}/go/%{go_label}
for ext in *.{go,c,h,s,S,py,syso,bin}; do
  find src -name ${ext} -exec install -Dm644 \{\} %{buildroot}%{_datadir}/go/%{go_label}/\{\} \;
done
# executable bash scripts called by go tool, etc
find src -name "*.bash" -exec install -Dm655 \{\} %{buildroot}%{_datadir}/go/%{go_label}/\{\} \;
# VERSION file referenced by go tool dist and go tool distpack
find . -name VERSION -exec install -Dm655 \{\} %{buildroot}%{_datadir}/go/%{go_label}/\{\} \;
# Trace viewer html and javascript files have moved in recent Go versions
# Prior to go1.19   misc/trace
# go1.19 to go1.21  src/cmd/trace/static
# go1.22            src/internal/trace/traceviewer/static
# Static contains pprof trace viewer html javascript and markdown
install -d  %{buildroot}%{_datadir}/go/%{go_label}/src/internal/trace/traceviewer/static
install -Dm644 src/internal/trace/traceviewer/static/* %{buildroot}%{_datadir}/go/%{go_label}/src/internal/trace/traceviewer/static
# pprof viewer html templates are needed for import runtime/pprof
install -d  %{buildroot}%{_datadir}/go/%{go_label}/src/cmd/vendor/github.com/google/pprof/internal/driver/html
install -Dm644 src/cmd/vendor/github.com/google/pprof/internal/driver/html/* %{buildroot}%{_datadir}/go/%{go_label}/src/cmd/vendor/github.com/google/pprof/internal/driver/html

mkdir -p $GOROOT/src
for i in $(ls %{buildroot}/usr/share/go/%{go_label}/src);do
  ln -s /usr/share/go/%{go_label}/src/$i $GOROOT/src/$i
done
# add lib files that are needed (such as the timezone database).
install -d $GOROOT/lib
find lib -type f -exec install -D -m644 {} $GOROOT/{} \;

# copy document templates, packages, obj libs and command utilities
mkdir -p $GOROOT/bin
# remove bootstrap
rm -rf pkg/bootstrap
mv pkg $GOROOT
mv bin/* $GOROOT/bin
# add wasm (Web Assembly) boo#1139210
mkdir -p $GOROOT/misc/wasm
mv misc/wasm/* $GOROOT/misc/wasm
rm -f %{buildroot}%{_bindir}/{hgpatch,quietgcc}

# gdbinit
install -Dm644 %{SOURCE6} $GOROOT/bin/gdbinit.d/go.gdb
%if "%{_lib}" == "lib64"
sed -i "s/lib/lib64/" $GOROOT/bin/gdbinit.d/go.gdb
sed -i "s/\$go_label/%{go_label}/" $GOROOT/bin/gdbinit.d/go.gdb
%endif

# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
mkdir -p %{buildroot}%{_sysconfdir}/gdbinit.d
touch %{buildroot}%{_sysconfdir}/alternatives/{go,gofmt,go.gdb}
ln -sf %{_sysconfdir}/alternatives/go %{buildroot}%{_bindir}/go
ln -sf %{_sysconfdir}/alternatives/gofmt %{buildroot}%{_bindir}/gofmt
ln -sf %{_sysconfdir}/alternatives/go.gdb %{buildroot}%{_sysconfdir}/gdbinit.d/go.gdb

# documentation and examples
# fix documetation permissions (rpmlint warning)
find doc/ misc/ -type f -exec chmod 0644 '{}' +
# remove unwanted arch-dependant binaries (rpmlint warning)
rm -rf misc/cgo/test/{_*,*.o,*.out,*.6,*.8}
# prepare go-doc
mkdir -p %{buildroot}%{_docdir}/go/%{go_label}
cp -r CONTRIBUTING.md LICENSE PATENTS README.md README.SUSE %{buildroot}%{_docdir}/go/%{go_label}
cp -r doc/* %{buildroot}%{_docdir}/go/%{go_label}

%fdupes -s %{buildroot}%{_prefix}

%post

update-alternatives \
  --install %{_bindir}/go go %{_libdir}/go/%{go_label}/bin/go $((20+$(echo %{go_label} | cut -d. -f2))) \
  --slave %{_bindir}/gofmt gofmt %{_libdir}/go/%{go_label}/bin/gofmt \
  --slave %{_sysconfdir}/gdbinit.d/go.gdb go.gdb %{_libdir}/go/%{go_label}/bin/gdbinit.d/go.gdb

%postun
if [ $1 -eq 0 ] ; then
	update-alternatives --remove go %{_libdir}/go/%{go_label}/bin/go
fi

%files
%{_bindir}/go
%{_bindir}/gofmt
%dir %{_libdir}/go
%{_libdir}/go/%{go_label}
%dir %{_datadir}/go
%{_datadir}/go/%{go_label}
%dir %{_sysconfdir}/gdbinit.d/
%config %{_sysconfdir}/gdbinit.d/go.gdb
%ghost %{_sysconfdir}/alternatives/go
%ghost %{_sysconfdir}/alternatives/gofmt
%ghost %{_sysconfdir}/alternatives/go.gdb
%dir %{_docdir}/go
%dir %{_docdir}/go/%{go_label}
%doc %{_docdir}/go/%{go_label}/CONTRIBUTING.md
%doc %{_docdir}/go/%{go_label}/PATENTS
%doc %{_docdir}/go/%{go_label}/README.md
%doc %{_docdir}/go/%{go_label}/README.SUSE
%if 0%{?suse_version} < 1500
%doc %{_docdir}/go/%{go_label}/LICENSE
%else
%license %{_docdir}/go/%{go_label}/LICENSE
%endif

# We don't include TSAN in the main Go package.
%ifarch %{tsan_arch}
%exclude %{_datadir}/go/%{go_label}/src/runtime/race/race_linux_%{go_arch}.syso
%endif

# We don't include libstd.so in the main Go package.
%if %{with_shared}
%if 0%{?suse_version} > 1500
# openSUSE Tumbleweed
# ./go/1.22/pkg/linux_amd64_dynlink/libstd.so
%exclude %{_libdir}/go/%{go_label}/pkg/linux_%{go_arch}_dynlink/libstd.so
%endif
%endif

%files doc
# SLE-12 SP5 rpm macro environment does not work with single glob {*.html,godebug.md}
%doc %{_docdir}/go/%{go_label}/*.html
%doc %{_docdir}/go/%{go_label}/godebug.md

%ifarch %{tsan_arch}
%files race
%{_datadir}/go/%{go_label}/src/runtime/race/race_linux_%{go_arch}.syso
%endif

%if %{with_shared}
%if 0%{?suse_version} > 1500
# openSUSE Tumbleweed
%files libstd
%{_libdir}/go/%{go_label}/pkg/linux_%{go_arch}_dynlink/libstd.so
%endif
%endif

%changelog
