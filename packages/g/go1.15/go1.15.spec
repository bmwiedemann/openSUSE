#
# spec file for package go1.15
#
# Copyright (c) 2020 SUSE LLC
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

%if 0%{?suse_version} == 1315
%define gcc_go_version 6
%define go_bootstrap_version go1.4
%else
%ifarch riscv64
%define go_bootstrap_version go1.14
%else
%define go_bootstrap_version go1.9
%endif
%if 0%{?sle_version} == 150000
# SLE15 or Leap 15.x
%define gcc_go_version 7
%else
%define gcc_go_version 9
%endif
%endif

# By default use go and not gccgo
%bcond_with    gccgo

# The fallback boostrap method via %%{go_bootstrap_version} would work for Leap
# but we don't have %%{go_bootstrap_version} in there. Same for SLE15+
#if ( 0%{?suse_version} < 1550 && 0%{?is_opensuse} ) || ( 0%{?suse_version} >= 1500 && ! 0%{?is_opensuse} )
#bcond_without gccgo
#endif

# The fallback bootstrap method via go1.4 doesn't work
# for aarch64 nor ppc64le because go 1.4 did not support that architecture.
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
%define tsan_commit 6c75db8b4bc59eace18143ce086419d37da24746

%define go_api 1.15

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

Name:           go1.15
Version:        1.15.2
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
# PATCH-FIX-OPENSUSE enable writing tools outside $GOROOT/pkg/tool for packaging
Patch5:         tools-packaging.patch
# PATCH-FIX-UPSTREAM marguerite@opensuse.org - find /usr/bin/go-5 when bootstrapping with gcc5-go
Patch8:         gcc6-go.patch
Patch9:         gcc7-go.patch
# PATCH-FIX-UPSTREAM prefer /etc/hosts over DNS when /etc/nsswitch.conf not present boo#1172868 gh#golang/go#35305
Patch12:        go1.x-prefer-etc-hosts-over-dns.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# boostrap
%if %{with gccgo}
%ifnarch s390 s390x
BuildRequires:  binutils-gold
%endif
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
# Needed on arm aarch64 to avoid
# collect2: fatal error: cannot find 'ld'-
%ifarch %arm aarch64
BuildRequires:  binutils-gold
%endif
Requires(post):	update-alternatives
Requires(postun):	update-alternatives
# Needed on arm aarch64 to avoid
# collect2: fatal error: cannot find 'ld'-
%ifarch %arm aarch64
%if 0%{?is_opensuse}
Requires:       binutils-gold
%else
Recommends:     binutils-gold
%endif
%endif
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
%patch5 -p1
%patch12 -p1
%if %{with gccgo}
%if 0%{?gcc_go_version} == 6
%patch8 -p1
%endif
%if 0%{?gcc_go_version} == 7
%patch9 -p1
%endif
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
export GOROOT_FINAL=%{_libdir}/go/%{go_api}
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
export GOROOT="%{buildroot}%{_libdir}/go/%{go_api}"

# locations for third party libraries, see README-openSUSE for info about locations.
install -d  %{buildroot}%{_datadir}/go/%{go_api}/contrib
install -d  $GOROOT/contrib/pkg/linux_%{go_arch}
ln -s %{_libdir}/go/%{go_api}/contrib/pkg/ %{buildroot}%{_datadir}/go/%{go_api}/contrib/pkg
install -d  %{buildroot}%{_datadir}/go/%{go_api}/contrib/cmd
install -d  %{buildroot}%{_datadir}/go/%{go_api}/contrib/src
ln -s %{_datadir}/go/%{go_api}/contrib/src/ %{buildroot}%{_libdir}/go/%{go_api}/contrib/src
install -Dm644 README.SUSE $GOROOT/contrib/
ln -s %{_libdir}/go/%{go_api}/contrib/README.SUSE %{buildroot}%{_datadir}/go/%{go_api}/contrib/README.SUSE

# source files for go install, godoc, etc
install -d %{buildroot}%{_datadir}/go/%{go_api}
for ext in *.{go,c,h,s,S,py,syso}; do
  find src -name ${ext} -exec install -Dm644 \{\} %{buildroot}%{_datadir}/go/%{go_api}/\{\} \;
done
mkdir -p $GOROOT/src
for i in $(ls %{buildroot}/usr/share/go/%{go_api}/src);do
  ln -s /usr/share/go/%{go_api}/src/$i $GOROOT/src/$i
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
sed -i "s/\$go_api/%{go_api}/" $GOROOT/bin/gdbinit.d/go.gdb
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
mkdir -p %{buildroot}%{_docdir}/go/%{go_api}
cp -r AUTHORS CONTRIBUTORS CONTRIBUTING.md LICENSE PATENTS README.md README.SUSE %{buildroot}%{_docdir}/go/%{go_api}
cp -r doc/* %{buildroot}%{_docdir}/go/%{go_api}

%fdupes -s %{buildroot}%{_prefix}

%post

update-alternatives \
  --install %{_bindir}/go go %{_libdir}/go/%{go_api}/bin/go $((20+$(echo %{go_api} | cut -d. -f2))) \
  --slave %{_bindir}/gofmt gofmt %{_libdir}/go/%{go_api}/bin/gofmt \
  --slave %{_sysconfdir}/gdbinit.d/go.gdb go.gdb %{_libdir}/go/%{go_api}/bin/gdbinit.d/go.gdb

%postun
if [ $1 -eq 0 ] ; then
	update-alternatives --remove go %{_libdir}/go/%{go_api}/bin/go
fi

%files
%{_bindir}/go
%{_bindir}/gofmt
%dir %{_libdir}/go
%{_libdir}/go/%{go_api}
%dir %{_datadir}/go
%{_datadir}/go/%{go_api}
%dir %{_sysconfdir}/gdbinit.d/
%config %{_sysconfdir}/gdbinit.d/go.gdb
%ghost %{_sysconfdir}/alternatives/go
%ghost %{_sysconfdir}/alternatives/gofmt
%ghost %{_sysconfdir}/alternatives/go.gdb
%dir %{_docdir}/go
%dir %{_docdir}/go/%{go_api}
%doc %{_docdir}/go/%{go_api}/AUTHORS
%doc %{_docdir}/go/%{go_api}/CONTRIBUTORS
%doc %{_docdir}/go/%{go_api}/CONTRIBUTING.md
%doc %{_docdir}/go/%{go_api}/PATENTS
%doc %{_docdir}/go/%{go_api}/README.md
%doc %{_docdir}/go/%{go_api}/README.SUSE
%if 0%{?suse_version} < 1500
%doc %{_docdir}/go/%{go_api}/LICENSE
%else
%license %{_docdir}/go/%{go_api}/LICENSE
%endif%

# We don't include TSAN in the main Go package.
%ifarch %{tsan_arch}
%exclude %{_datadir}/go/%{go_api}/src/runtime/race/race_linux_%{go_arch}.syso
%endif

%files doc
%defattr(-,root,root,-)
%doc %{_docdir}/go/%{go_api}/codewalk
%doc %{_docdir}/go/%{go_api}/articles
%doc %{_docdir}/go/%{go_api}/progs
%doc %{_docdir}/go/%{go_api}/play
%doc %{_docdir}/go/%{go_api}/gopher
%doc %{_docdir}/go/%{go_api}/*.html
%doc %{_docdir}/go/%{go_api}/*.css
%doc %{_docdir}/go/%{go_api}/*.png

%ifarch %{tsan_arch}
%files race
%{_datadir}/go/%{go_api}/src/runtime/race/race_linux_%{go_arch}.syso
%endif

%changelog
