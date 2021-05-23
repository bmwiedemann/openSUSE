#
# spec file for package nodejs16
#
# Copyright (c) 2021 SUSE LLC
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

Name:           nodejs16
Version:        16.2.0
Release:        0

# Double DWZ memory limits
%define _dwz_low_mem_die_limit  20000000
%define _dwz_max_die_limit     100000000

%define node_version_number 16

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

# turn on LTO only on non-32bit arches
%ifarch %{ix86} %{arm}
%bcond_with nodejs_lto
%else
%bcond_without nodejs_lto
%endif

%else
%bcond_with nodejs_lto
%endif

%if !0%{?with nodejs_lto}
%define _lto_cflags %{nil}
%endif

%if 0%{?suse_version} == 1110
%define _libexecdir %{_exec_prefix}/lib
%endif

%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 120500
%bcond_with    intree_openssl
%else
%bcond_without intree_openssl
%endif

%if 0%{suse_version} >= 1330
%bcond_with    intree_cares
%else
%bcond_without intree_cares
%endif

%if 0%{?suse_version} >= 1550 
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

%if %node_version_number < 16

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

%else
# don't use binutils_gold for nodejs >= 16
%bcond_with    binutils_gold
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
Patch5:         sle12_python3_compat.patch
Patch7:         manual_configure.patch
Patch13:        openssl_binary_detection.patch

## Patches specific to SUSE and openSUSE
Patch100:       linker_lto_jobs.patch
# PATCH-FIX-OPENSUSE -- set correct path for dtrace if it is built
Patch101:       nodejs-libpath.patch
# PATCH-FIX-UPSTREAM -- use custom addon.gypi by default instead of
# downloading node source
Patch102:       node-gyp-addon-gypi.patch
# PATCH-FIX-SLE -- configure script uses Python check_output method
# which isn't included in Python 2.6 (used in SLE 11).
# PATCH-FIX-OPENSUSE -- install user global npm packages to /usr/local
# instead of /usr
Patch104:       npm_search_paths.patch
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
%if %node_version_number >= 12
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
%if 0%{suse_version} > 1330
BuildRequires:  libopenssl1_1-hmac
%endif

%if 0%{suse_version} >= 1330
BuildRequires:  openssl >= %{openssl_req_ver}
%else
BuildRequires:  openssl-1_1 >= %{openssl_req_ver}
%endif

%else

%if 0%{?suse_version} >= 1330
BuildRequires:  libopenssl-1_0_0-devel
%else
BuildRequires:  openssl-devel >= %{openssl_req_ver}
%endif

%endif
%else
Provides:       bundled(openssl) = 1.1.1k
%endif

%if ! 0%{with intree_cares}
BuildRequires:  pkgconfig(libcares) >= 1.17.0
%else
Provides:       bundled(libcares2) = 1.17.1
%endif

%if ! 0%{with intree_icu}
BuildRequires:  pkgconfig(icu-i18n) >= 68
%else
Provides:       bundled(icu) = 69.1
%endif

%if ! 0%{with intree_nghttp2}
BuildRequires:  libnghttp2-devel >= 1.41.0
%else
Provides:       bundled(nghttp2) = 1.42.0
%endif

%if 0%{with valgrind_tests}
BuildRequires:  valgrind
%endif

Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     npm16

#we need ABI virtual provides where SONAMEs aren't enough/not present so deps
#break when binary compatibility is broken
%global nodejs_abi 16.0
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

%if %node_version_number < 16
ExclusiveArch:  %{arm} %{ix86} x86_64 aarch64 ppc64 ppc64le s390x
%endif

Provides:       bundled(brotli) = 1.0.9
Provides:       bundled(libuv) = 1.41.0
Provides:       bundled(uvwasi) = 0.0.11
Provides:       bundled(v8) = 9.0.257.25

Provides:       bundled(llhttp) = 6.0.1
Provides:       bundled(ngtcp2) = 0.1.0-DEV

Provides:       bundled(node-acorn) = 8.0.4
Provides:       bundled(node-acorn-class-fields) = 0.3.1
Provides:       bundled(node-acorn-private-class-elements) = 0.2.0
Provides:       bundled(node-acorn-private-methods) = 0.3.0
Provides:       bundled(node-acorn-static-class-features) = 0.2.0
Provides:       bundled(node-acorn-walk) = 8.0.0
Provides:       bundled(node-cjs-module-lexer) = 1.2.1

%description
Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine. Node.js
uses an event-driven, non-blocking I/O model. Node.js has a package ecosystem
provided by npm.

%package devel
Summary:        Development headers for NodeJS 16.x
Group:          Development/Languages/NodeJS
Provides:       nodejs-devel = %{version}
Requires:       %{name} = %{version}
Requires:       npm16 = %{version}

%description devel
This package provides development headers for Node.js needed for creation
of binary modules.

%package -n npm16
Summary:        Package manager for Node.js
Group:          Development/Languages/NodeJS
Requires:       nodejs-common
Requires:       nodejs16 = %{version}
Provides:       nodejs-npm = %{version}
Obsoletes:      nodejs-npm < 4.0.0
Provides:       npm = %{version}
Provides:       npm(npm) = 7.13.0
%if 0%{?suse_version} >= 1500
%if %{node_version_number} >= 10
Requires:       group(nobody)
Requires:       user(nobody)
%endif
%endif
Provides:       bundled(node-@npmcli/arborist) = 2.5.0
Provides:       bundled(node-@npmcli/ci-detect) = 1.3.0
Provides:       bundled(node-@npmcli/config) = 2.2.0
Provides:       bundled(node-@npmcli/disparity-colors) = 1.0.1
Provides:       bundled(node-@npmcli/git) = 2.0.9
Provides:       bundled(node-@npmcli/installed-package-contents) = 1.0.7
Provides:       bundled(node-@npmcli/map-workspaces) = 1.0.3
Provides:       bundled(node-@npmcli/metavuln-calculator) = 1.1.1
Provides:       bundled(node-@npmcli/move-file) = 1.1.2
Provides:       bundled(node-@npmcli/name-from-folder) = 1.0.1
Provides:       bundled(node-@npmcli/node-gyp) = 1.0.2
Provides:       bundled(node-@npmcli/promise-spawn) = 1.3.2
Provides:       bundled(node-@npmcli/run-script) = 1.8.5
Provides:       bundled(node-@tootallnate/once) = 1.1.2
Provides:       bundled(node-abbrev) = 1.1.1
Provides:       bundled(node-agent-base) = 6.0.2
Provides:       bundled(node-agentkeepalive) = 4.1.4
Provides:       bundled(node-aggregate-error) = 3.1.0
Provides:       bundled(node-ajv) = 6.12.6
Provides:       bundled(node-ansi-regex) = 2.1.1
Provides:       bundled(node-ansi-regex) = 3.0.0
Provides:       bundled(node-ansi-regex) = 5.0.0
Provides:       bundled(node-ansi-styles) = 4.3.0
Provides:       bundled(node-ansicolors) = 0.3.2
Provides:       bundled(node-ansistyles) = 0.1.3
Provides:       bundled(node-aproba) = 1.2.0
Provides:       bundled(node-aproba) = 2.0.0
Provides:       bundled(node-archy) = 1.0.0
Provides:       bundled(node-are-we-there-yet) = 1.1.5
Provides:       bundled(node-asap) = 2.0.6
Provides:       bundled(node-asn1) = 0.2.4
Provides:       bundled(node-assert-plus) = 1.0.0
Provides:       bundled(node-asynckit) = 0.4.0
Provides:       bundled(node-aws-sign2) = 0.7.0
Provides:       bundled(node-aws4) = 1.11.0
Provides:       bundled(node-balanced-match) = 1.0.2
Provides:       bundled(node-bcrypt-pbkdf) = 1.0.2
Provides:       bundled(node-bin-links) = 2.2.1
Provides:       bundled(node-binary-extensions) = 2.2.0
Provides:       bundled(node-brace-expansion) = 1.1.11
Provides:       bundled(node-builtins) = 1.0.3
Provides:       bundled(node-byte-size) = 7.0.1
Provides:       bundled(node-cacache) = 15.0.6
Provides:       bundled(node-caseless) = 0.12.0
Provides:       bundled(node-chalk) = 4.1.1
Provides:       bundled(node-chownr) = 2.0.0
Provides:       bundled(node-cidr-regex) = 3.1.1
Provides:       bundled(node-clean-stack) = 2.2.0
Provides:       bundled(node-cli-columns) = 3.1.2
Provides:       bundled(node-cli-table3) = 0.6.0
Provides:       bundled(node-clone) = 1.0.4
Provides:       bundled(node-cmd-shim) = 4.1.0
Provides:       bundled(node-code-point-at) = 1.1.0
Provides:       bundled(node-color-convert) = 2.0.1
Provides:       bundled(node-color-name) = 1.1.4
Provides:       bundled(node-colors) = 1.4.0
Provides:       bundled(node-columnify) = 1.5.4
Provides:       bundled(node-combined-stream) = 1.0.8
Provides:       bundled(node-common-ancestor-path) = 1.0.1
Provides:       bundled(node-concat-map) = 0.0.1
Provides:       bundled(node-console-control-strings) = 1.1.0
Provides:       bundled(node-core-util-is) = 1.0.2
Provides:       bundled(node-dashdash) = 1.14.1
Provides:       bundled(node-debug) = 4.3.1
Provides:       bundled(node-debuglog) = 1.0.1
Provides:       bundled(node-defaults) = 1.0.3
Provides:       bundled(node-delayed-stream) = 1.0.0
Provides:       bundled(node-delegates) = 1.0.0
Provides:       bundled(node-depd) = 1.1.2
Provides:       bundled(node-dezalgo) = 1.0.3
Provides:       bundled(node-diff) = 5.0.0
Provides:       bundled(node-ecc-jsbn) = 0.1.2
Provides:       bundled(node-emoji-regex) = 8.0.0
Provides:       bundled(node-encoding) = 0.1.13
Provides:       bundled(node-env-paths) = 2.2.1
Provides:       bundled(node-err-code) = 2.0.3
Provides:       bundled(node-extend) = 3.0.2
Provides:       bundled(node-extsprintf) = 1.3.0
Provides:       bundled(node-fast-deep-equal) = 3.1.3
Provides:       bundled(node-fast-json-stable-stringify) = 2.1.0
Provides:       bundled(node-forever-agent) = 0.6.1
Provides:       bundled(node-form-data) = 2.3.3
Provides:       bundled(node-fs-minipass) = 2.1.0
Provides:       bundled(node-fs.realpath) = 1.0.0
Provides:       bundled(node-function-bind) = 1.1.1
Provides:       bundled(node-gauge) = 2.7.4
Provides:       bundled(node-getpass) = 0.1.7
Provides:       bundled(node-glob) = 7.1.7
Provides:       bundled(node-graceful-fs) = 4.2.6
Provides:       bundled(node-har-schema) = 2.0.0
Provides:       bundled(node-har-validator) = 5.1.5
Provides:       bundled(node-has) = 1.0.3
Provides:       bundled(node-has-flag) = 4.0.0
Provides:       bundled(node-has-unicode) = 2.0.1
Provides:       bundled(node-hosted-git-info) = 4.0.2
Provides:       bundled(node-http-cache-semantics) = 4.1.0
Provides:       bundled(node-http-proxy-agent) = 4.0.1
Provides:       bundled(node-http-signature) = 1.2.0
Provides:       bundled(node-https-proxy-agent) = 5.0.0
Provides:       bundled(node-humanize-ms) = 1.2.1
Provides:       bundled(node-iconv-lite) = 0.6.2
Provides:       bundled(node-ignore-walk) = 3.0.4
Provides:       bundled(node-imurmurhash) = 0.1.4
Provides:       bundled(node-indent-string) = 4.0.0
Provides:       bundled(node-infer-owner) = 1.0.4
Provides:       bundled(node-inflight) = 1.0.6
Provides:       bundled(node-inherits) = 2.0.4
Provides:       bundled(node-ini) = 2.0.0
Provides:       bundled(node-init-package-json) = 2.0.3
Provides:       bundled(node-ip) = 1.1.5
Provides:       bundled(node-ip-regex) = 4.3.0
Provides:       bundled(node-is-cidr) = 4.0.2
Provides:       bundled(node-is-core-module) = 2.2.0
Provides:       bundled(node-is-fullwidth-code-point) = 1.0.0
Provides:       bundled(node-is-fullwidth-code-point) = 2.0.0
Provides:       bundled(node-is-fullwidth-code-point) = 3.0.0
Provides:       bundled(node-is-lambda) = 1.0.1
Provides:       bundled(node-is-typedarray) = 1.0.0
Provides:       bundled(node-isarray) = 1.0.0
Provides:       bundled(node-isexe) = 2.0.0
Provides:       bundled(node-isstream) = 0.1.2
Provides:       bundled(node-jsbn) = 0.1.1
Provides:       bundled(node-json-parse-even-better-errors) = 2.3.1
Provides:       bundled(node-json-schema) = 0.2.3
Provides:       bundled(node-json-schema-traverse) = 0.4.1
Provides:       bundled(node-json-stringify-nice) = 1.1.4
Provides:       bundled(node-json-stringify-safe) = 5.0.1
Provides:       bundled(node-jsonparse) = 1.3.1
Provides:       bundled(node-jsprim) = 1.4.1
Provides:       bundled(node-just-diff) = 3.1.1
Provides:       bundled(node-just-diff-apply) = 3.0.0
Provides:       bundled(node-leven) = 3.1.0
Provides:       bundled(node-libnpmaccess) = 4.0.2
Provides:       bundled(node-libnpmdiff) = 2.0.4
Provides:       bundled(node-libnpmexec) = 1.1.1
Provides:       bundled(node-libnpmfund) = 1.1.0
Provides:       bundled(node-libnpmhook) = 6.0.2
Provides:       bundled(node-libnpmorg) = 2.0.2
Provides:       bundled(node-libnpmpack) = 2.0.1
Provides:       bundled(node-libnpmpublish) = 4.0.1
Provides:       bundled(node-libnpmsearch) = 3.1.1
Provides:       bundled(node-libnpmteam) = 2.0.3
Provides:       bundled(node-libnpmversion) = 1.2.0
Provides:       bundled(node-lru-cache) = 6.0.0
Provides:       bundled(node-make-fetch-happen) = 8.0.14
Provides:       bundled(node-mime-db) = 1.47.0
Provides:       bundled(node-mime-types) = 2.1.30
Provides:       bundled(node-minimatch) = 3.0.4
Provides:       bundled(node-minipass) = 3.1.3
Provides:       bundled(node-minipass-collect) = 1.0.2
Provides:       bundled(node-minipass-fetch) = 1.3.3
Provides:       bundled(node-minipass-flush) = 1.0.5
Provides:       bundled(node-minipass-json-stream) = 1.0.1
Provides:       bundled(node-minipass-pipeline) = 1.2.4
Provides:       bundled(node-minipass-sized) = 1.0.3
Provides:       bundled(node-minizlib) = 2.1.2
Provides:       bundled(node-mkdirp) = 1.0.4
Provides:       bundled(node-mkdirp-infer-owner) = 2.0.0
Provides:       bundled(node-ms) = 2.1.2
Provides:       bundled(node-ms) = 2.1.3
Provides:       bundled(node-mute-stream) = 0.0.8
Provides:       bundled(node-node-gyp) = 7.1.2
Provides:       bundled(node-nopt) = 5.0.0
Provides:       bundled(node-normalize-package-data) = 3.0.2
Provides:       bundled(node-npm-audit-report) = 2.1.4
Provides:       bundled(node-npm-bundled) = 1.1.2
Provides:       bundled(node-npm-init) = 0.0.0
Provides:       bundled(node-npm-install-checks) = 4.0.0
Provides:       bundled(node-npm-normalize-package-bin) = 1.0.1
Provides:       bundled(node-npm-package-arg) = 8.1.2
Provides:       bundled(node-npm-packlist) = 2.2.2
Provides:       bundled(node-npm-pick-manifest) = 6.1.1
Provides:       bundled(node-npm-profile) = 5.0.3
Provides:       bundled(node-npm-registry-fetch) = 10.1.1
Provides:       bundled(node-npm-user-validate) = 1.0.1
Provides:       bundled(node-npmlog) = 4.1.2
Provides:       bundled(node-number-is-nan) = 1.0.1
Provides:       bundled(node-oauth-sign) = 0.9.0
Provides:       bundled(node-object-assign) = 4.1.1
Provides:       bundled(node-once) = 1.4.0
Provides:       bundled(node-opener) = 1.5.2
Provides:       bundled(node-p-map) = 4.0.0
Provides:       bundled(node-pacote) = 11.3.3
Provides:       bundled(node-parse-conflict-json) = 1.1.1
Provides:       bundled(node-path-is-absolute) = 1.0.1
Provides:       bundled(node-path-parse) = 1.0.6
Provides:       bundled(node-performance-now) = 2.1.0
Provides:       bundled(node-proc-log) = 1.0.0
Provides:       bundled(node-process-nextick-args) = 2.0.1
Provides:       bundled(node-promise-all-reject-late) = 1.0.1
Provides:       bundled(node-promise-call-limit) = 1.0.1
Provides:       bundled(node-promise-inflight) = 1.0.1
Provides:       bundled(node-promise-retry) = 2.0.1
Provides:       bundled(node-promzard) = 0.3.0
Provides:       bundled(node-psl) = 1.8.0
Provides:       bundled(node-punycode) = 2.1.1
Provides:       bundled(node-qrcode-terminal) = 0.12.0
Provides:       bundled(node-qs) = 6.5.2
Provides:       bundled(node-read) = 1.0.7
Provides:       bundled(node-read-cmd-shim) = 2.0.0
Provides:       bundled(node-read-package-json) = 3.0.1
Provides:       bundled(node-read-package-json-fast) = 2.0.2
Provides:       bundled(node-readable-stream) = 2.3.7
Provides:       bundled(node-readdir-scoped-modules) = 1.1.0
Provides:       bundled(node-request) = 2.88.2
Provides:       bundled(node-resolve) = 1.20.0
Provides:       bundled(node-retry) = 0.12.0
Provides:       bundled(node-rimraf) = 3.0.2
Provides:       bundled(node-safe-buffer) = 5.1.2
Provides:       bundled(node-safer-buffer) = 2.1.2
Provides:       bundled(node-semver) = 7.3.5
Provides:       bundled(node-set-blocking) = 2.0.0
Provides:       bundled(node-signal-exit) = 3.0.3
Provides:       bundled(node-smart-buffer) = 4.1.0
Provides:       bundled(node-socks) = 2.6.1
Provides:       bundled(node-socks-proxy-agent) = 5.0.0
Provides:       bundled(node-spdx-correct) = 3.1.1
Provides:       bundled(node-spdx-exceptions) = 2.3.0
Provides:       bundled(node-spdx-expression-parse) = 3.0.1
Provides:       bundled(node-spdx-license-ids) = 3.0.7
Provides:       bundled(node-sshpk) = 1.16.1
Provides:       bundled(node-ssri) = 8.0.1
Provides:       bundled(node-string-width) = 1.0.2
Provides:       bundled(node-string-width) = 2.1.1
Provides:       bundled(node-string-width) = 4.2.2
Provides:       bundled(node-string_decoder) = 1.1.1
Provides:       bundled(node-stringify-package) = 1.0.1
Provides:       bundled(node-strip-ansi) = 3.0.1
Provides:       bundled(node-strip-ansi) = 4.0.0
Provides:       bundled(node-strip-ansi) = 6.0.0
Provides:       bundled(node-supports-color) = 7.2.0
Provides:       bundled(node-tar) = 6.1.0
Provides:       bundled(node-text-table) = 0.2.0
Provides:       bundled(node-tiny-relative-date) = 1.3.0
Provides:       bundled(node-tough-cookie) = 2.5.0
Provides:       bundled(node-treeverse) = 1.0.4
Provides:       bundled(node-tunnel-agent) = 0.6.0
Provides:       bundled(node-tweetnacl) = 0.14.5
Provides:       bundled(node-typedarray-to-buffer) = 3.1.5
Provides:       bundled(node-unique-filename) = 1.1.1
Provides:       bundled(node-unique-slug) = 2.0.2
Provides:       bundled(node-uri-js) = 4.4.1
Provides:       bundled(node-util-deprecate) = 1.0.2
Provides:       bundled(node-uuid) = 3.4.0
Provides:       bundled(node-validate-npm-package-license) = 3.0.4
Provides:       bundled(node-validate-npm-package-name) = 3.0.0
Provides:       bundled(node-verror) = 1.10.0
Provides:       bundled(node-walk-up-path) = 1.0.0
Provides:       bundled(node-wcwidth) = 1.0.1
Provides:       bundled(node-which) = 2.0.2
Provides:       bundled(node-wide-align) = 1.1.3
Provides:       bundled(node-wrappy) = 1.0.2
Provides:       bundled(node-write-file-atomic) = 3.0.3
Provides:       bundled(node-yallist) = 4.0.0

%description -n npm16
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
tar Jxf %{SOURCE10}
%endif

%if %{node_version_number} >= 10
tar Jxf %{SOURCE11}
%endif

%patch3 -p1
%if ! 0%{with intree_openssl}
%endif
%patch5 -p1
%patch7 -p1
%if 0%{with valgrind_tests}
%endif
%patch13 -p1
%patch100 -p1
%patch101 -p1
%patch102 -p1
# Add check_output to configure script (not part of Python 2.6 in SLE11).
%if 0%{?suse_version} == 1110
%endif
%patch104 -p1
%patch106 -p1
%patch120 -p1
%patch200 -p1

# remove backup files, if any
find -name \*~ -print0 -delete

# abnormalities from patching
find \( -name \*.js.orig -or -name \*.md.orig -or -name \*.1.orig \) -delete

%build
# normalize shebang
%if %{node_version_number} >= 12
find -type f -exec sed -i -e '1 s,^#!\s\?/usr/bin/env python\d*$,#!/usr/bin/python3,' -e '1 s,^#!\s\?/usr/bin/python$,#!/usr/bin/python3,' {} +
%else
find -type f -exec sed -i '1 s,^#!\s\?/usr/bin/env python$,#!/usr/bin/python,' {} +
%endif
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

cat > spec.build.config <<EOF
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS="%{optflags} -Wno-class-memaccess -Wno-error=return-type -fno-strict-aliasing"
export LDFLAGS="%{?build_ldflags}"

%if !0%{?with nodejs_lto}
export LDFLAGS="\${LDFLAGS} -fno-lto"
%endif

%ifarch %{ix86} %{arm}
# Reduce memory consumption on 32bit arches
export CFLAGS="\${CFLAGS} -g1"
export CXXFLAGS="\${CXXFLAGS} -g1"
export LDFLAGS="\${LDFLAGS} -Wl,--reduce-memory-overhead"
%endif

%if 0%{?cc_exec:1}
export CC=%{?cc_exec}
export CXX=%{?cpp_exec}
%endif

EOF

. ./spec.build.config

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
. ./spec.build.config

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
! test -f %{buildroot}%{_libdir}/node_modules/npm%{node_version_number}/bin/node-gyp-bin/node-gyp || \
    chmod 0755 %{buildroot}%{_libdir}/node_modules/npm%{node_version_number}/bin/node-gyp-bin/node-gyp
chmod 0755 %{buildroot}%{_libdir}/node_modules/npm%{node_version_number}/node_modules/node-gyp/bin/node-gyp.js
! test -f %{buildroot}%{_libdir}/node_modules/npm%{node_version_number}/node_modules/npm-lifecycle/node-gyp-bin/node-gyp || \
    chmod 0755 %{buildroot}%{_libdir}/node_modules/npm%{node_version_number}/node_modules/npm-lifecycle/node-gyp-bin/node-gyp

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
. ./spec.build.config

# Relax the crypto policies for the test-suite
export OPENSSL_SYSTEM_CIPHERS_OVERRIDE=xyz_nonexistent_file
export OPENSSL_CONF=''

export CI_JS_SUITES=default
export NODE_TEST_NO_INTERNET=1

%if %{node_version_number} >= 12
find test \( -name \*.out -or -name \*.js \) -exec sed -i 's,Use `node ,Use `node%{node_version_number} ,' {} \;
%endif

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
