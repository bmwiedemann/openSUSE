#
# spec file for package nodejs10
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


###########################################################
#
#   WARNING! WARNING! WARNING! WARNING! WARNING! WARNING!
#
# This spec file is generated from a template hosted at
# https://github.com/AdamMajer/nodejs-packaging
#
###########################################################

Name:           nodejs10
Version:        10.22.0
Release:        0

%define node_version_number 10

%if %node_version_number >= 12
%define openssl_req_ver 1.1.1
%else
%if %node_version_number >= 10
%define openssl_req_ver 1.1.0
%else
%define openssl_req_ver 1.0.2
%endif
%endif

%bcond_with    valgrind_tests

%if %{node_version_number} >= 12
%bcond_without nodejs_lto
%else
%bcond_with nodejs_lto
%endif

%if !0%{?with nodejs_lto}
%define _lto_cflags %{nil}
%endif

%if 0%{?suse_version} == 1110
%define _libexecdir %{_exec_prefix}/lib
%endif

%if 0%{?suse_version} >= 1500 || 0%{?sle_version} >= 120400
%bcond_with    intree_openssl
%else
%bcond_without intree_openssl
%endif

%if 0%{suse_version} >= 1330
%bcond_with    intree_cares
%else
%bcond_without intree_cares
%endif

%if 0%{?suse_version} >= 1330
%bcond_with    intree_icu
%else
%bcond_without intree_icu
%endif

%if 0%{suse_version} >= 1550
%bcond_with    intree_nghttp2
%else
%bcond_without intree_nghttp2
%endif

%ifarch aarch64 ppc ppc64 ppc64le s390 s390x
%bcond_with    gdb
%else
%bcond_without gdb
%endif

# No binutils_gold on SLE 12 GA (aarch64).
%ifarch aarch64
%if 0%{?sle_version} >= 120100 || 0%{?is_opensuse}
%bcond_without binutils_gold
%else
%bcond_with    binutils_gold
%endif
%endif

# No binutils_gold on all versions of SLE 12 and Leap 42 (s390x).
%ifarch s390x
%if 0%{?suse_version} > 1320
%bcond_without binutils_gold
%else
%bcond_with    binutils_gold
%endif
%endif

%ifarch s390
%bcond_with    binutils_gold
%endif

%ifnarch aarch64 s390x s390
%bcond_without binutils_gold
%endif

%define git_node 0

Summary:        Evented I/O for V8 JavaScript
License:        MIT
Group:          Development/Languages/NodeJS
URL:            https://nodejs.org
Source:         https://nodejs.org/dist/v%{version}/node-v%{version}.tar.xz
Source1:        https://nodejs.org/dist/v%{version}/SHASUMS256.txt
Source2:        https://nodejs.org/dist/v%{version}/SHASUMS256.txt.sig
Source3:        nodejs.keyring
# Only required to run unit tests in NodeJS 10+ 
Source10:       update_npm_tarball.sh 
Source11:       node_modules.tar.xz
Source20:       bash_output_helper.bash

## Patches not distribution specific
Patch3:         fix_ci_tests.patch
Patch7:         manual_configure.patch
Patch11:        valgrind_fixes.patch

## Patches specific to SUSE and openSUSE
# PATCH-FIX-OPENSUSE -- set correct path for dtrace if it is built
Patch101:       nodejs-libpath.patch
# PATCH-FIX-UPSTREAM -- use custom addon.gypi by default instead of
# downloading node source
Patch102:       node-gyp-addon-gypi.patch
# PATCH-FIX-SLE -- configure script uses Python check_output method
# which isn't included in Python 2.6 (used in SLE 11).
Patch103:       nodejs-sle11-python26-check_output.patch
# PATCH-FIX-OPENSUSE -- install user global npm packages to /usr/local
# instead of /usr
Patch104:       npm_search_paths.patch
Patch105:       skip_test_on_lowmem.patch
Patch106:       skip_no_console.patch

Patch120:       flaky_test_rerun.patch

# Use versioned binaries and paths
Patch200:       versioned.patch

%if 0%{with binutils_gold}
BuildRequires:  binutils-gold
%endif

BuildRequires:  pkg-config
BuildRequires:  config(netcfg)

# SLE-11 target only
# Node.js 6 requires GCC 4.8.5+.
#
# For Node.js 8.x, upstream requires GCC 4.9.4+, as GCC 4.8 may have
# slightly buggy C++11 support: https://github.com/nodejs/node/pull/13466
#
# If the default compiler is not supported, use the most recent compiler
# version available.
%if 0%{?suse_version} == 1110
# GCC 5 is only available in the SUSE:SLE-11:SP4:Update repository (SDK).
%if %node_version_number >= 8
BuildRequires:  gcc5-c++
%define cc_exec  gcc-5
%define cpp_exec g++-5
%else
BuildRequires:  gcc48-c++
%define cc_exec  gcc-4.8
%define cpp_exec g++-4.8
%endif
%endif
# sles == 11 block

# Pick and stick with "latest" compiler at time of LTS release
# for SLE-12:Update targets
%if 0%{?suse_version} == 1315
%if %node_version_number >= 14
BuildRequires:  gcc9-c++
%define cc_exec  gcc-9
%define cpp_exec g++-9
%else
%if %node_version_number >= 8
BuildRequires:  gcc7-c++
%define cc_exec  gcc-7
%define cpp_exec g++-7
%endif
%endif
%endif
# compiler selection

# No special version defined, use default.
%if ! 0%{?cc_exec:1}
BuildRequires:  gcc-c++
%endif

BuildRequires:  fdupes
BuildRequires:  procps
BuildRequires:  xz
BuildRequires:  zlib-devel

# Python dependencies
%if %node_version_number > 12
BuildRequires:  netcfg
BuildRequires:  python3
%else
%if 0%{?suse_version} >= 1500
BuildRequires:  python2
%else
BuildRequires:  python
%endif
%endif

%if 0%{?suse_version} >= 1500 && %{node_version_number} >= 10
BuildRequires:  group(nobody)
BuildRequires:  user(nobody)
%endif

%if ! 0%{with intree_openssl}

%if %node_version_number >= 8
BuildRequires:  pkgconfig(openssl) >= %{openssl_req_ver}
%else

%if 0%{?suse_version} >= 1330
BuildRequires:  libopenssl-1_0_0-devel
%else
BuildRequires:  openssl-devel >= %{openssl_req_ver}
%endif

%endif
%endif

%if ! 0%{with intree_cares}
BuildRequires:  pkgconfig(libcares) >= 1.10.0
%endif

%if ! 0%{with intree_icu}
BuildRequires:  pkgconfig(icu-i18n) >= 57
%endif

%if ! 0%{with intree_nghttp2}
BuildRequires:  libnghttp2-devel >= 1.41.0
%endif

%if 0%{with valgrind_tests}
BuildRequires:  valgrind
%endif

Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     npm10

#we need ABI virtual provides where SONAMEs aren't enough/not present so deps
#break when binary compatibility is broken
%global nodejs_abi 10.0
Provides:       nodejs(abi) = %{nodejs_abi}

#this corresponds to the "engine" requirement in package.json
Provides:       nodejs(engine) = %{version}

# Multiple versions of NodeJS can be installed at a time, but
# to properly allow correct version execution from 3rd party
# npm software, `env node` requires further help than only
# update-alternatives can provide.
Provides:       nodejs = %{version}
Requires:       nodejs-common

# For SLE11, to be able to use the certificate store we need to have properly
# symlinked certificates. The compatability symlinks are provided by the
# openssl1 library in the Security Module
%if 0%{?suse_version} == 1110
Requires:       openssl1
%endif

# Building Node.js only makes sense on V8 architectures.
ExclusiveArch:  %{ix86} x86_64 armv7hl aarch64 ppc ppc64 ppc64le s390 s390x
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine. Node.js
uses an event-driven, non-blocking I/O model. Node.js has a package ecosystem
provided by npm.

%package devel
Summary:        Files needed for development of NodeJS platforms
Group:          Development/Languages/NodeJS
Provides:       nodejs-devel = %{version}
Requires:       %{name} = %{version}

%description devel
This package provides development headers for Node.js.

%package -n npm10
Summary:        Package manager for Node.js
Group:          Development/Languages/NodeJS
Requires:       %{name} = %{version}
Requires:       nodejs-common
Recommends:     %{name}-devel = %{version}
Provides:       nodejs-npm = %{version}
Obsoletes:      nodejs-npm < 4.0.0
Provides:       npm = %{version}
Provides:       npm(npm) = 6.14.3
%if 0%{?suse_version} >= 1500
%if %{node_version_number} >= 10
Requires:       group(nobody)
Requires:       user(nobody)
%endif
Recommends:     python2
Recommends:     python3
%else
Recommends:     python
%endif

%description -n npm10
A package manager for Node.js that allows developers to install and
publish packages to a package registry.

%package docs
Summary:        Node.js API documentation
Group:          Documentation/Other
%if 0%{?suse_version} >= 1200
# using noarch subpackage seems to break debuginfo on older releases
BuildArch:      noarch
%endif

%description docs
The API documentation for the Node.js JavaScript runtime.

%prep
%if ! %{git_node}
echo "`grep node-v%{version}.tar.xz %{S:1} | head -n1 | cut -c1-64`  %{S:0}" | sha256sum -c
%setup -q -n node-v%{version}
%else
%setup -q -n node-%{version}
%endif

%if %{node_version_number} == 6
# Update NPM
rm -r deps/npm
tar Jxvf %{SOURCE10}
%endif

%if %{node_version_number} >= 10
tar Jxvf %{SOURCE11}
%endif

%patch3 -p1
%if ! 0%{with intree_openssl}
%endif
%patch7 -p1
%if 0%{with valgrind_tests}
%patch11 -p1
%endif
%patch101 -p1
%patch102 -p1
# Add check_output to configure script (not part of Python 2.6 in SLE11).
%if 0%{?suse_version} == 1110
%patch103 -p1
%endif
%patch104 -p1
%patch105 -p1
%patch106 -p1
%patch120 -p1
%patch200 -p1

# remove backup files, if any
find -name \*~ -print0 -delete

# abnormalities from patching
find \( -name \*.js.orig -or -name \*.md.orig \) -delete

%build
# normalize shebang
find -name \*.py -perm -1 -type f -exec sed -i '1 s,^#!\s\?/usr/bin/env python$,#!/usr/bin/python,' {} +
find deps/npm -type f -exec sed -i '1 s,^#!\s\?/usr/bin/env node$,#!/usr/bin/node%{node_version_number},' {} +
find deps/npm -type f -exec sed -i '1 s,^#!\s\?/usr/bin/env \(bash\|sh\)\?$,#!/bin/bash,' {} +

. %{SOURCE20}
# Make sure nothing gets included from bundled deps:
# We only delete the source and header files, because
# the remaining build scripts are still used.
%if ! 0%{with intree_openssl}
find deps/openssl -name *.[ch] -delete
%endif

%if ! 0%{with intree_icu}
rm -rf deps/icu-small
%endif

%if ! 0%{with intree_cares}
find deps/cares -name *.[ch] -delete
%endif

find deps/zlib -name *.[ch] -delete

# percent-configure pulls in something that confuses node's configure
# script, so we'll do it thus:
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -Wno-class-memaccess -Wno-error=return-type -fno-strict-aliasing"
export LDFLAGS="%{?build_ldflags}"

%if 0%{?cc_exec:1}
export CC=%{?cc_exec}
export CXX=%{?cpp_exec}
%endif

# Node.js 4.x does not include the ICU database in the source tarball.
%define has_small_icu %(test -d "deps/icu-small" && echo 1 || echo 0)

./configure \
    --prefix=%{_prefix} \
%if 0%{?with nodejs_lto}
    --enable-lto \
%endif
%if ! 0%{with intree_openssl}
    --shared-openssl \
%endif
    --shared-zlib \
%if ! 0%{with intree_cares}
    --shared-cares \
%endif
%if ! 0%{with intree_icu}
    --with-intl=system-icu \
%else
%if %{has_small_icu}
    --with-intl=small-icu \
    --with-icu-source=deps/icu-small \
%endif
%endif
%if ! 0%{with intree_nghttp2}
    --shared-nghttp2 \
%endif
%if 0%{with gdb}
    --gdb \
%endif
    --without-dtrace \
    --openssl-use-def-ca-store

decoupled_cmd make %{?_smp_mflags}

# Fix documentation permissions
find doc/api -type f -exec chmod 0644 {} +

%install
. %{SOURCE20}

export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -Wno-class-memaccess -Wno-error=return-type -fno-strict-aliasing"
export LDFLAGS="%{?build_ldflags}"

%if 0%{?cc_exec:1}
export CC=%{?cc_exec}
export CXX=%{?cpp_exec}
%endif

decoupled_cmd %make_install %{?_smp_mflags}
rm %{buildroot}%{_datadir}/doc/node/gdbinit
rm -f %{buildroot}%{_datadir}/doc/node/lldbinit
rm -f %{buildroot}%{_datadir}/doc/node/lldb_commands.py

# remove .bak files, if any
find %{buildroot} -name \*.bak -print -delete

# npm/npx man page
install -D -m 644 deps/npm/man/man1/npm.1 %{buildroot}%{_mandir}/man1/npm%{node_version_number}.1
%if %{node_version_number} >= 8
install -D -m 644 deps/npm/man/man1/npx.1 %{buildroot}%{_mandir}/man1/npx%{node_version_number}.1
%endif

#node-gyp needs common.gypi too
install -D -m 644 common.gypi \
	%{buildroot}%{_libdir}/node_modules/npm%{node_version_number}/node_modules/node-gyp/common.gypi
#       %%{buildroot}%%{_datadir}/node/common.gypi
# install addon-rpm.gypi
install -D -m 644 addon-rpm.gypi \
       %{buildroot}%{_libdir}/node_modules/npm%{node_version_number}/node_modules/node-gyp/addon-rpm.gypi

# clean
# hidden files and directories
find %{buildroot}%{_libdir}/node_modules/npm%{node_version_number} -name ".*" -exec rm -Rf -- {} +
# windows stuff
find %{buildroot}%{_libdir}/node_modules/npm%{node_version_number} -name "*.bat" -delete
find %{buildroot}%{_libdir}/node_modules/npm%{node_version_number} -name "*.cmd" -delete
# build stuff
find %{buildroot}%{_libdir}/node_modules/npm%{node_version_number} -name "Makefile" -delete
rm -rf %{buildroot}%{_libdir}/node_modules/npm%{node_version_number}/{test,scripts}
find %{buildroot}%{_libdir}/node_modules/npm%{node_version_number}/node_modules -name "*.sh" -delete
rm -rf %{buildroot}%{_libdir}/node_modules/npm%{node_version_number}/node_modules/node-gyp/src
# remove examples/tests/benchmark stuff
find %{buildroot}%{_libdir}/node_modules/npm%{node_version_number}/node_modules -name "example*" -exec rm -Rf -- {} +
find %{buildroot}%{_libdir}/node_modules/npm%{node_version_number}/node_modules -name "*_test.*" -delete
find %{buildroot}%{_libdir}/node_modules/npm%{node_version_number}/node_modules -type d -name "benchmark" -exec rm -Rf -- {} +

# fix permissions
chmod 0755 %{buildroot}%{_libdir}/node_modules/npm%{node_version_number}/bin/np*-cli.js
chmod 0755 %{buildroot}%{_libdir}/node_modules/npm%{node_version_number}/bin/node-gyp-bin/node-gyp
chmod 0755 %{buildroot}%{_libdir}/node_modules/npm%{node_version_number}/node_modules/node-gyp/bin/node-gyp.js
%if %{node_version_number} >= 8
chmod 0755 %{buildroot}%{_libdir}/node_modules/npm%{node_version_number}/node_modules/npm-lifecycle/node-gyp-bin/node-gyp
%endif

# browser.js is useless for npm cli
find %{buildroot}%{_libdir}/node_modules/npm%{node_version_number} -name "browser.js" -delete

# file duplicates
%fdupes %{buildroot}%{_libdir}/node_modules/npm%{node_version_number}
%fdupes %{buildroot}%{_includedir}/node%{node_version_number}

# Update alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f node-default     %{buildroot}%{_sysconfdir}/alternatives/node-default
ln -s -f node.1%{ext_man} %{buildroot}%{_sysconfdir}/alternatives/node.1%{ext_man}
ln -s -f npm-default      %{buildroot}%{_sysconfdir}/alternatives/npm-default
ln -s -f npm.1%{ext_man}  %{buildroot}%{_sysconfdir}/alternatives/npm.1%{ext_man}
ln -s %{_sysconfdir}/alternatives/node-default         %{buildroot}%{_bindir}/node-default
ln -s %{_sysconfdir}/alternatives/node.1%{ext_man}     %{buildroot}%{_mandir}/man1/node.1%{ext_man}
ln -s %{_sysconfdir}/alternatives/npm-default          %{buildroot}%{_bindir}/npm-default
ln -s %{_sysconfdir}/alternatives/npm.1%{ext_man}      %{buildroot}%{_mandir}/man1/npm.1%{ext_man}
%if %{node_version_number} >= 8
ln -s -f npx-default      %{buildroot}%{_sysconfdir}/alternatives/npx-default
ln -s -f npx.1%{ext_man}  %{buildroot}%{_sysconfdir}/alternatives/npx.1%{ext_man}
ln -s %{_sysconfdir}/alternatives/npx-default          %{buildroot}%{_bindir}/npx-default
ln -s %{_sysconfdir}/alternatives/npx.1%{ext_man}      %{buildroot}%{_mandir}/man1/npx.1%{ext_man}
%endif

# We need to own license directory on old versions of SLE
%if 0%{?suse_version} < 1500
mkdir -p %{buildroot}%{_defaultlicensedir}
%endif

%check
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -Wno-class-memaccess -Wno-error=return-type -fno-strict-aliasing"
export LDFLAGS="%{?build_ldflags}"

%if 0%{?cc_exec:1}
export CC=%{?cc_exec}
export CXX=%{?cpp_exec}
%endif

export NODE_TEST_NO_INTERNET=1
%if %{node_version_number} >= 12
find test \( -name \*.out -or -name \*.js \) -exec sed -i 's,Use `node ,Use `node%{node_version_number} ,' {} \;
%endif

strip node%{node_version_number}

ln addon-rpm.gypi deps/npm/node_modules/node-gyp/addon-rpm.gypi
# Tarball doesn't have eslint package distributed, so disable some tests
find test -name \*-eslint-\* -print -delete
# No documentation is generated, don't bother checking it
rm -f test/doctool/test-make-doc.js
# DNS lookup doesn't work in build root
rm -f test/parallel/test-dns-cancel-reverse-lookup.js \
      test/parallel/test-dns-resolveany.js
# multicast test fail since no socket?
rm -f test/parallel/test-dgram-membership.js
# Run CI tests
%if 0%{with valgrind_tests}
# valgrind may have false positives, so do not fail on these by default
make test-valgrind ||:
%endif
make test-ci

%files
%defattr(-, root, root)
%license LICENSE
%doc AUTHORS *.md
%doc deps/v8/tools/gdbinit
%dir %{_libdir}/node_modules
%{_bindir}/node%{node_version_number}
%{_mandir}/man1/node%{node_version_number}.1%{ext_man}
%ghost %{_bindir}/node-default
%ghost %{_mandir}/man1/node.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/node-default
%ghost %{_sysconfdir}/alternatives/node.1%{ext_man}
%exclude %{_libdir}/node_modules/npm%{node_version_number}
# We need to own directory on old versions of SLE
%if 0%{?suse_version} < 1500
%dir %{_defaultlicensedir}
%endif

%files -n npm%{node_version_number}
%defattr(-, root, root)
%{_bindir}/npm%{node_version_number}
%{_libdir}/node_modules/npm%{node_version_number}
%{_mandir}/man1/npm%{node_version_number}.1%{ext_man}
%ghost %{_bindir}/npm-default
%ghost %{_mandir}/man1/npm.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/npm-default
%ghost %{_sysconfdir}/alternatives/npm.1%{ext_man}

%if %{node_version_number} >= 8
%{_bindir}/npx%{node_version_number}
%{_mandir}/man1/npx%{node_version_number}.1%{ext_man}
%ghost %{_bindir}/npx-default
%ghost %{_mandir}/man1/npx.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/npx-default
%ghost %{_sysconfdir}/alternatives/npx.1%{ext_man}
%endif

%files devel
%defattr(-, root, root)
%{_includedir}/node%{node_version_number}
%dir %{_datadir}/systemtap
%dir %{_datadir}/systemtap/tapset
%{_datadir}/systemtap/tapset/node%{node_version_number}.stp

%files docs
%defattr(-,root,root)
%doc doc/api

%pre
# remove files that are no longer owned but provided by update-alternatives
if ! [ -L %{_mandir}/man1/node.1%{ext_man} ]; then
    rm -f %{_mandir}/man1/node.1%{ext_man}
fi

%post
update-alternatives \
        --install %{_bindir}/node-default node-default %{_bindir}/node%{node_version_number} %{node_version_number} \
        --slave %{_mandir}/man1/node.1%{ext_man} node.1%{ext_man} %{_mandir}/man1/node%{node_version_number}.1%{ext_man}

%postun
if [ ! -f %{_bindir}/node%{node_version_number} ] ; then
    update-alternatives --remove node-default %{_bindir}/node%{node_version_number}
fi

%pre -n npm%{node_version_number}
# remove files that are no longer owned but provided by update-alternatives
if ! [ -L %{_mandir}/man1/npm.1%{ext_man} ]; then
    rm -f %{_mandir}/man1/npm.1%{ext_man}
fi

%post -n npm%{node_version_number}
update-alternatives \
        --install %{_bindir}/npm-default npm-default %{_bindir}/npm%{node_version_number} %{node_version_number} \
        --slave %{_mandir}/man1/npm.1%{ext_man} npm.1%{ext_man} %{_mandir}/man1/npm%{node_version_number}.1%{ext_man}
%if %{node_version_number} >= 8
update-alternatives \
        --install %{_bindir}/npx-default npx-default %{_bindir}/npx%{node_version_number} %{node_version_number} \
        --slave %{_mandir}/man1/npx.1%{ext_man} npx.1%{ext_man} %{_mandir}/man1/npx%{node_version_number}.1%{ext_man}
%endif

%postun -n npm%{node_version_number}
if [ ! -f %{_bindir}/npm%{node_version_number} ] ; then
    update-alternatives --remove npm-default %{_bindir}/npm%{node_version_number}
fi
%if %{node_version_number} >= 8
if [ ! -f %{_bindir}/npx%{node_version_number} ] ; then
    update-alternatives --remove npx-default %{_bindir}/npx%{node_version_number}
fi
%endif

%changelog
