#
# spec file for package go1.4
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


%define with_gccgo 1

%if 0%{?suse_version} > 1320
%define with_gccgo 0
%endif

# By default we don't include tsan. It's only supported on amd64.
%define tsan_arch x86_64

# Go has precompiled versions of LLVM's compiler-rt inside their source code.
# We cannot ship pre-compiled binaries so we have to recompile said source,
# however they vendor specific commits from upstream. This value comes from
# src/runtime/race/README (and we verify that it matches in check).
# See boo#1052528 for more details.
%define tsan_commit 215000

Name:           go1.4
Version:        1.4.3
Release:        0
Summary:        A compiled, garbage-collected, concurrent programming language
License:        BSD-3-Clause
Group:          Development/Languages/Go
URL:            http://golang.org
Source0:        http://golang.org/dl/go%{version}.src.tar.gz
Source1:        go-rpmlintrc
Source3:        macros.go
Source5:        README.SUSE
Source6:        go1.4.gdbinit
# We have to compile TSAN ourselves. boo#1052528
Source100:      compiler-rt-r%{tsan_commit}.tar.xz
# PATCH-FIX-OPENSUSE add -s flag to 'go install' (don't rebuild/install std libs)
Patch1:         go-build-dont-reinstall-stdlibs.patch
# PATCH-FIX-OPENSUSE re-enable build binary only packages (we are binary distro)
# see http://code.google.com/p/go/issues/detail?id=2775 & also issue 3268
Patch2:         allow-binary-only-packages.patch
#PATCH-FIX-OPENSUSE use -x verbose build output for qemu-arm builders
Patch3:         verbose-build.patch
# PATCH-FIX-OPENSUSE BNC#776058
Patch4:         go-install-dont-reinstall-stdlibs.patch
# PATCH-FIX-OPENSUSE enable writing tools outside $GOROOT/pkg/tool for packaging
Patch5:         tools-packaging.patch
# armv6l needs this patch for our build system
# see https://groups.google.com/forum/#!topic/golang-nuts/MqKTX_XIOKE
Patch6:         armv6l.patch
# PATCH-FIX-OPENSUSE fix_certificates_lookup.patch fcastelli@suse.com -- this patch forces Go to look for certificates only in the openSUSE/SLE locations. It also fixes certificate loading on SLE11, see https://github.com/golang/go/issues/6391
# PATCH-FIX-SUSE fix_certificates_lookup.patch fcastelli@suse.com -- this patch forces Go to look for certificates only in the openSUSE/SLE locations. It also fixes certificate loading on SLE11, see https://github.com/golang/go/issues/6391
Patch7:         fix_certificates_lookup.patch
Patch8:         go-1.4.2-rel.plt-alignment.patch
# PATCH-FIX-UPSTREAM binutils support for new 386/amd64 relocations. add support for them in go linker.
Patch9:         go-1.4.3-support-new-386_amd64-relocations.patch
Patch10:        CVE-2016-5386.patch
# PATCH-FIX-UPSTREAM net/smtp: fix PlainAuth to refuse to send passwords to non-TLS servers
Patch11:        net-smtp-fix-PlainAuth-to-refuse-to-send-passwords-to-non-TLS-servers.patch
# PATCH-FIX-UPSTREAM cmd/go: reject update of VCS inside VCS
Patch12:        cmd-go-reject-update-of-VCS-inside-VCS.patch
# PATCH-FIX-UPSTREAM (compiler-rt): Fix sanitizer build against latest glibc
Patch100:       fix-sanitizer-build-against-latest-glibc.patch
Patch101:       gcc9-rsp-clobber.patch
BuildRequires:  rpm
# for go1.4.gdbinit, directory ownership
BuildRequires:  gdb
%if %{with_gccgo}
Requires:       gcc
%endif
%ifarch %{tsan_arch}
# Needed to compile compiler-rt/TSAN.
BuildRequires:  gcc-c++
%endif
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       go = %{version}
Provides:       go-devel = go%{version}
Provides:       go-devel-static = go%{version}
Provides:       golang(API) = 1.4
Obsoletes:      go-devel < go%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %ix86 x86_64 %arm
%if 0%{?suse_version} >= 1210
BuildRequires:  pkgconfig(systemd)
%endif
%if 0%{?suse_version} >= 1100
BuildRequires:  fdupes
Recommends:     %{name}-doc = %{version}
#BNC#818502 debug edit tool of rpm fails on i586 builds
%if 0%{?suse_version} > 1230
BuildRequires:  rpm >= 4.11.1
%endif
%endif

%description
Go is an expressive, concurrent, garbage collected systems programming language
that is type safe and memory safe. It has pointers but no pointer arithmetic.
Go has fast builds, clean syntax, garbage collection, methods for any type, and
run-time reflection. It feels like a dynamic language but has the speed and
safety of a static language.

%package doc
Summary:        Go documentation
License:        BSD-3-Clause
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description doc
Go examples and documentation.

%ifarch %{tsan_arch}
# boo#1052528
%package race
Summary:        Go runtime race detector
License:        NCSA OR MIT
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
# compiler-rt
%setup -q -T -b 100 -n compiler-rt-r%{tsan_commit}
%patch100 -p1
%patch101 -p1
%endif
# go
%setup -q -n go
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%ifarch armv6hl
%patch6 -p1
%endif
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
cp %{SOURCE5} .

# setup go_arch (BSD-like scheme)
cp %{SOURCE3} go.macros
%ifarch %ix86
sed -i 's|GOARCH|386|' go.macros
%define go_arch 386
%endif
%ifarch x86_64
sed -i 's|GOARCH|amd64|' go.macros
%define go_arch amd64
%endif
%ifarch %arm
sed -i 's|GOARCH|arm|' go.macros
%define go_arch arm
%endif

%build
# Remove the pre-included .sysos, to avoid shipping things we didn't compile
# (which is against the openSUSE guidelines for packaging).
find . -type f -name '*.syso' -exec rm -vf {} \;

# First, compile LLVM's TSAN, and replace the built-in with it. We can only do
# this for amd64.
%ifarch %{tsan_arch}
pushd ../compiler-rt*/lib/tsan/go
./buildgo.sh
popd
cp ../compiler-rt*/lib/tsan/go/race_linux_%{go_arch}.syso src/runtime/race/race_linux_%{go_arch}.syso
%endif

# Now, compile Go.
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
export GOROOT_FINAL=%{_libdir}/%{name}
export GOBIN="$GOROOT/bin"
%if !%{with_gccgo}
export CGO_ENABLED=0
%endif
mkdir -p "$GOBIN"
cd src
HOST_EXTRA_CFLAGS="%{optflags} -Wno-error" ./make.bash

cd ../
%ifarch %{tsan_arch}
# Install TSAN-friendly version of the std libraries.
bin/go install -race std
%endif

%check
%ifarch %{tsan_arch}
# Make sure that we have the right TSAN checked out.
grep "%{tsan_commit}" src/runtime/race/README
%endif

%install
export GOROOT="%{buildroot}%{_libdir}/%{name}"

# locations for third party libraries, see README.SUSE for info about locations.
install -d  %{buildroot}%{_datadir}/%{name}/contrib
install -d  $GOROOT/contrib/pkg/linux_%{go_arch}
ln -s %{_libdir}/%{name}/contrib/pkg/ %{buildroot}%{_datadir}/%{name}/contrib/pkg
install -d  %{buildroot}%{_datadir}/%{name}/contrib/cmd
install -d  %{buildroot}%{_datadir}/%{name}/contrib/src
ln -s %{_datadir}/%{name}/contrib/src/ %{buildroot}%{_libdir}/%{name}/contrib/src
install -Dm644 README.SUSE $GOROOT/contrib/
ln -s %{_libdir}/%{name}/contrib/README.SUSE %{buildroot}%{_datadir}/%{name}/contrib/README.SUSE

# source files for go install, godoc, etc
install -d %{buildroot}%{_datadir}/%{name}
for ext in *.{go,c,h,s,S,py,syso}; do
  find src -name ${ext} -exec install -Dm644 \{\} %{buildroot}%{_datadir}/%{name}/\{\} \;
done
mkdir -p $GOROOT/src
for i in $(ls %{buildroot}%{_datadir}/%{name}/src);do
  ln -s %{_datadir}/%{name}/src/$i $GOROOT/src/$i
done
# add lib files that are needed (such as the timezone database).
install -d $GOROOT/lib
find lib -type f -exec install -D -m644 {} $GOROOT/{} \;

# copy document templates, packages, obj libs and command utilities
mkdir -p $GOROOT/bin
mv pkg $GOROOT
mv bin/* $GOROOT/bin
rm -f $GOROOT/bin/{hgpatch,quietgcc}

# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
mkdir -p %{buildroot}%{_bindir}
touch %{buildroot}%{_sysconfdir}/alternatives/{go,gofmt}
ln -sf %{_sysconfdir}/alternatives/go %{buildroot}%{_bindir}/go
ln -sf %{_sysconfdir}/alternatives/gofmt %{buildroot}%{_bindir}/gofmt

# documentation and examples
# fix documetation permissions (rpmlint warning)
find doc/ misc/ -type f -exec chmod 0644 '{}' \;
# remove unwanted arch-dependant binaries (rpmlint warning)
rm -rf misc/cgo/test/{_*,*.o,*.out,*.6,*.8}
rm -f misc/dashboard/builder/{gobuilder,*6,*.8}
# prepare for go-doc sub-package
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -r AUTHORS CONTRIBUTORS LICENSE PATENTS README README.SUSE %{buildroot}%{_docdir}/%{name}
cp -r doc/* %{buildroot}%{_docdir}/%{name}

# gdbinit
mkdir -p %{buildroot}%{_sysconfdir}/gdbinit.d
install -m 0644 %{SOURCE6} %{buildroot}%{_sysconfdir}/gdbinit.d/go1.4.gdb
%if "%{_lib}" == "lib64"
sed -i "s/lib/lib64/" %{buildroot}%{_sysconfdir}/gdbinit.d/go1.4.gdb
%endif

# install RPM macros ($GOARCH prepared in %%prep section)
install -Dm644 go.macros %{buildroot}%{_sysconfdir}/rpm/macros.%{name}

%if 0%{?suse_version} >= 1100
%fdupes -s %{buildroot}%{_prefix}
%endif

%post
update-alternatives \
	--install %{_bindir}/go go %{_libdir}/%{name}/bin/go 60 \
	--slave %{_bindir}/gofmt gofmt %{_libdir}/%{name}/bin/gofmt

%postun
if [ $1 -eq 0 ] ; then
	update-alternatives --remove go %{_libdir}/%{name}/bin/go
fi

%files
%defattr(-,root,root,-)
%{_bindir}/go
%{_bindir}/gofmt
%ifarch %ix86
%{_libdir}/%{name}/pkg/tool/linux_%{go_arch}/8*
%endif
%ifarch x86_64
%{_libdir}/%{name}/pkg/tool/linux_%{go_arch}/6*
%endif
%ifarch %arm
%{_libdir}/%{name}/pkg/tool/linux_%{go_arch}/5*
%endif
%{_libdir}/%{name}
%{_datadir}/%{name}/
%ghost %{_sysconfdir}/alternatives/go
%ghost %{_sysconfdir}/alternatives/gofmt
%config %{_sysconfdir}/gdbinit.d/%{name}.gdb
%config %{_sysconfdir}/rpm/macros.%{name}
%dir %{_docdir}/%{name}/
%doc %{_docdir}/%{name}/AUTHORS
%doc %{_docdir}/%{name}/CONTRIBUTORS
%doc %{_docdir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/PATENTS
%doc %{_docdir}/%{name}/README
%doc %{_docdir}/%{name}/README.SUSE

# We don't include TSAN in the main Go package.
%ifarch %{tsan_arch}
%exclude %{_datadir}/go1.4/src/runtime/race/race_linux_%{go_arch}.syso
%endif

%files doc
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/codewalk
%doc %{_docdir}/%{name}/articles
%doc %{_docdir}/%{name}/progs
%doc %{_docdir}/%{name}/play
%doc %{_docdir}/%{name}/gopher
%doc %{_docdir}/%{name}/devel
%doc %{_docdir}/%{name}/*.html
%doc %{_docdir}/%{name}/*.css
%doc %{_docdir}/%{name}/*.png
%doc %{_docdir}/%{name}/*.gif

%ifarch %{tsan_arch}
%files race
%defattr(-,root,root,-)
%{_datadir}/go1.4/src/runtime/race/race_linux_%{go_arch}.syso
%endif

%changelog
