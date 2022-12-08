#
# spec file for package go1.18
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
# nodebuginfo


# strip will cause Go's .a archives to become invalid because strip appears to
# reassemble the archive incorrectly. This is a known issue upstream
# (https://github.com/golang/go/issues/17890), but we have to deal with it in
# the meantime.
%undefine _build_create_debug
%define __arch_install_post export NO_BRP_STRIP_DEBUG=true NO_BRP_AR=true

# Used to bootstrap go toolchain with specific existing package
%define go_bootstrap_version go1.16

# Used to bootstrap go toolchain using specific version of gcc-go
%if 0%{?suse_version} > 1500
# openSUSE Tumbleweed
%define gcc_go_version 12
%else
%define gcc_go_version 11
%endif

# Bootstrap go toolchain using existing go package go_bootstrap_version
# To bootstrap using gccgo use '--with gccgo'
%bcond_with gccgo

# Boostrapping using existing go package can fail on certain SLE-12 architectures
# Override here as needed
%if 0%{?suse_version} == 1315
%ifarch aarch64 ppc64le ppc64 s390x
%bcond_without gccgo
%endif
%endif

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

# Build go-race only on platforms where it's supported (both amd64 and aarch64
# requires SLE15-or-later because of C++14, and ppc64le doesn't build at all
# on openSUSE yet).
%if 0%{?suse_version} >= 1500 || 0%{?sle_version} >= 150000
%define tsan_arch x86_64 aarch64
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
%define tsan_commit 89f7ccea6f6488c443655880229c54db1f180153

# go_api is the major version of Go.
# Used by go1.x packages and go metapackage for:
# RPM Provides: golang(API), RPM Requires: and rpm_vercmp
# as well as derived variables such as go_label.
%define go_api 1.18

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

Name:           go1.18
Version:        1.18.9
Release:        0
Summary:        A compiled, garbage-collected, concurrent programming language
License:        BSD-3-Clause
Group:          Development/Languages/Other
URL:            http://golang.org
Source:         http://golang.org/dl/go%{version}.src.tar.gz
Source1:        go-rpmlintrc
Source4:        README.SUSE
Source6:        go.gdbinit
# We have to compile TSAN ourselves. boo#1052528
Source100:      llvm-%{tsan_commit}.tar.xz
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
Recommends:     %{name}-doc = %{version}
%ifarch %{tsan_arch}
# Needed to compile compiler-rt/TSAN.
BuildRequires:  gcc-c++
%endif
#BNC#818502 debug edit tool of rpm fails on i586 builds
BuildRequires:  rpm >= 4.11.1
Requires(post): update-alternatives
Requires(postun):update-alternatives
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
Requires:       %{name} = %{version}
Provides:       go-doc = %{version}

%description doc
Go examples and documentation.

%ifarch %{tsan_arch}
# boo#1052528
%package race
Summary:        Go runtime race detector
Group:          Development/Languages/Other
URL:            https://compiler-rt.llvm.org/
Requires:       %{name} = %{version}
Supplements:    %{name} = %{version}
ExclusiveArch:  %{tsan_arch}

%description race
Go runtime race detector libraries. Install this package if you wish to use the
-race option, in order to detect race conditions present in your Go programs.
%endif

%prep
%ifarch %{tsan_arch}
# compiler-rt (from LLVM)
%setup -q -T -b 100 -n llvm-%{tsan_commit}
%endif
# go
%setup -q -n go
%patch7 -p1
%if %{with gccgo}
# Currently gcc-go does not manage an update-alternatives entry and will
# never be symlinked as "go", even if gcc-go is the only installed go toolchain.
# Patch go bootstrap scripts to find hardcoded go-(gcc-go-version) e.g. go-8
# Substitute defined gcc_go_version into gcc-go.patch
sed -i "s/\$gcc_go_version/%{gcc_go_version}/" $RPM_SOURCE_DIR/gcc-go.patch
%patch8 -p1
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
bin/go install -buildmode=shared -linkshared std
%endif

%check
%ifarch %{tsan_arch}
# Make sure that we have the right TSAN checked out.
grep "^race_linux_%{go_arch}.syso built with LLVM %{tsan_commit}" src/runtime/race/README
%endif

%install
export GOROOT="%{buildroot}%{_libdir}/go/%{go_label}"

# locations for third party libraries, see README-openSUSE for info about locations.
install -d  %{buildroot}%{_datadir}/go/%{go_label}/contrib
install -d  $GOROOT/contrib/pkg/linux_%{go_arch}
ln -s %{_libdir}/go/%{go_label}/contrib/pkg/ %{buildroot}%{_datadir}/go/%{go_label}/contrib/pkg
install -d  %{buildroot}%{_datadir}/go/%{go_label}/contrib/cmd
install -d  %{buildroot}%{_datadir}/go/%{go_label}/contrib/src
ln -s %{_datadir}/go/%{go_label}/contrib/src/ %{buildroot}%{_libdir}/go/%{go_label}/contrib/src
install -Dm644 README.SUSE $GOROOT/contrib/
ln -s %{_libdir}/go/%{go_label}/contrib/README.SUSE %{buildroot}%{_datadir}/go/%{go_label}/contrib/README.SUSE

# source files for go install, godoc, etc
install -d %{buildroot}%{_datadir}/go/%{go_label}
for ext in *.{go,c,h,s,S,py,syso,bin}; do
  find src -name ${ext} -exec install -Dm644 \{\} %{buildroot}%{_datadir}/go/%{go_label}/\{\} \;
done
# executable bash scripts called by go tool, etc
find src -name "*.bash" -exec install -Dm655 \{\} %{buildroot}%{_datadir}/go/%{go_label}/\{\} \;

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
mkdir -p $GOROOT/misc/trace
mv misc/trace/* $GOROOT/misc/trace
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
cp -r AUTHORS CONTRIBUTORS CONTRIBUTING.md LICENSE PATENTS README.md README.SUSE %{buildroot}%{_docdir}/go/%{go_label}
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
%doc %{_docdir}/go/%{go_label}/AUTHORS
%doc %{_docdir}/go/%{go_label}/CONTRIBUTORS
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

%files doc
%defattr(-,root,root,-)
%doc %{_docdir}/go/%{go_label}/*.html

%ifarch %{tsan_arch}
%files race
%{_datadir}/go/%{go_label}/src/runtime/race/race_linux_%{go_arch}.syso
%endif

%changelog
