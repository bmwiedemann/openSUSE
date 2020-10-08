#
# spec file for package nodejs14
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

Name:           nodejs14
Version:        14.13.0
Release:        0

%define node_version_number 14

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
Patch5:         sle12_python3_compat.patch
Patch7:         manual_configure.patch

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
Patch107:       old_icu.patch

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
%else
Provides:       bundled(openssl) = 1.1.1g
%endif

%if ! 0%{with intree_cares}
BuildRequires:  pkgconfig(libcares) >= 1.10.0
%else
Provides:       bundled(libcares2) = 1.16.1
%endif

%if ! 0%{with intree_icu}
BuildRequires:  pkgconfig(icu-i18n) >= 63
%else
Provides:       bundled(icu) = 67.1
%endif

%if ! 0%{with intree_nghttp2}
BuildRequires:  libnghttp2-devel >= 1.41.0
%else
Provides:       bundled(nghttp2) = 1.41.0
%endif

%if 0%{with valgrind_tests}
BuildRequires:  valgrind
%endif

Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     npm14

#we need ABI virtual provides where SONAMEs aren't enough/not present so deps
#break when binary compatibility is broken
%global nodejs_abi 14.0
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
ExclusiveArch:  x86_64 aarch64 ppc64 ppc64le s390x
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Provides:       bundled(brotli) = 1.0.9
Provides:       bundled(libuv) = 1.40.0
Provides:       bundled(uvwasi) = 0.0.11
Provides:       bundled(v8) = 8.4.371.19

Provides:       bundled(llhttp) = 2.1.2

Provides:       bundled(node-acorn) = 7.1.1
Provides:       bundled(node-acorn-class-fields) = 0.3.1
Provides:       bundled(node-acorn-numeric-separator) = 0.3.0
Provides:       bundled(node-acorn-private-class-elements) = 0.2.0
Provides:       bundled(node-acorn-private-methods) = 0.3.0
Provides:       bundled(node-acorn-static-class-features) = 0.2.0
Provides:       bundled(node-acorn-walk) = 7.1.1
Provides:       bundled(node-cjs-module-lexer) = 0.3.3
Provides:       bundled(node-node-inspect) = 2.0.0

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

%package -n npm14
Summary:        Package manager for Node.js
Group:          Development/Languages/NodeJS
Requires:       %{name} = %{version}
Requires:       nodejs-common
Recommends:     %{name}-devel = %{version}
Provides:       nodejs-npm = %{version}
Obsoletes:      nodejs-npm < 4.0.0
Provides:       npm = %{version}
Provides:       npm(npm) = 6.14.8
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
Provides:       bundled(node-JSONStream) = 1.3.5
Provides:       bundled(node-abbrev) = 1.1.1
Provides:       bundled(node-agent-base) = 4.2.1
Provides:       bundled(node-agent-base) = 4.3.0
Provides:       bundled(node-agentkeepalive) = 3.5.2
Provides:       bundled(node-ajv) = 5.5.2
Provides:       bundled(node-ansi-align) = 2.0.0
Provides:       bundled(node-ansi-regex) = 2.1.1
Provides:       bundled(node-ansi-regex) = 3.0.0
Provides:       bundled(node-ansi-regex) = 4.1.0
Provides:       bundled(node-ansi-styles) = 3.2.1
Provides:       bundled(node-ansicolors) = 0.3.2
Provides:       bundled(node-ansistyles) = 0.1.3
Provides:       bundled(node-aproba) = 1.2.0
Provides:       bundled(node-aproba) = 2.0.0
Provides:       bundled(node-archy) = 1.0.0
Provides:       bundled(node-are-we-there-yet) = 1.1.4
Provides:       bundled(node-asap) = 2.0.6
Provides:       bundled(node-asn1) = 0.2.4
Provides:       bundled(node-assert-plus) = 1.0.0
Provides:       bundled(node-asynckit) = 0.4.0
Provides:       bundled(node-aws-sign2) = 0.7.0
Provides:       bundled(node-aws4) = 1.8.0
Provides:       bundled(node-balanced-match) = 1.0.0
Provides:       bundled(node-bcrypt-pbkdf) = 1.0.2
Provides:       bundled(node-bin-links) = 1.1.8
Provides:       bundled(node-bluebird) = 3.5.5
Provides:       bundled(node-boxen) = 1.3.0
Provides:       bundled(node-brace-expansion) = 1.1.11
Provides:       bundled(node-buffer-from) = 1.0.0
Provides:       bundled(node-builtins) = 1.0.3
Provides:       bundled(node-byline) = 5.0.0
Provides:       bundled(node-byte-size) = 5.0.1
Provides:       bundled(node-cacache) = 12.0.3
Provides:       bundled(node-call-limit) = 1.1.1
Provides:       bundled(node-camelcase) = 4.1.0
Provides:       bundled(node-camelcase) = 5.3.1
Provides:       bundled(node-capture-stack-trace) = 1.0.0
Provides:       bundled(node-caseless) = 0.12.0
Provides:       bundled(node-chalk) = 2.4.1
Provides:       bundled(node-chownr) = 1.1.4
Provides:       bundled(node-ci-info) = 1.6.0
Provides:       bundled(node-ci-info) = 2.0.0
Provides:       bundled(node-cidr-regex) = 2.0.10
Provides:       bundled(node-cli-boxes) = 1.0.0
Provides:       bundled(node-cli-columns) = 3.1.2
Provides:       bundled(node-cli-table3) = 0.5.1
Provides:       bundled(node-cliui) = 5.0.0
Provides:       bundled(node-clone) = 1.0.4
Provides:       bundled(node-cmd-shim) = 3.0.3
Provides:       bundled(node-co) = 4.6.0
Provides:       bundled(node-code-point-at) = 1.1.0
Provides:       bundled(node-color-convert) = 1.9.1
Provides:       bundled(node-color-name) = 1.1.3
Provides:       bundled(node-colors) = 1.3.3
Provides:       bundled(node-columnify) = 1.5.4
Provides:       bundled(node-combined-stream) = 1.0.6
Provides:       bundled(node-concat-map) = 0.0.1
Provides:       bundled(node-concat-stream) = 1.6.2
Provides:       bundled(node-config-chain) = 1.1.12
Provides:       bundled(node-configstore) = 3.1.5
Provides:       bundled(node-console-control-strings) = 1.1.0
Provides:       bundled(node-copy-concurrently) = 1.0.5
Provides:       bundled(node-core-util-is) = 1.0.2
Provides:       bundled(node-create-error-class) = 3.0.2
Provides:       bundled(node-cross-spawn) = 5.1.0
Provides:       bundled(node-crypto-random-string) = 1.0.0
Provides:       bundled(node-cyclist) = 0.2.2
Provides:       bundled(node-dashdash) = 1.14.1
Provides:       bundled(node-debug) = 3.1.0
Provides:       bundled(node-debuglog) = 1.0.1
Provides:       bundled(node-decamelize) = 1.2.0
Provides:       bundled(node-decode-uri-component) = 0.2.0
Provides:       bundled(node-deep-extend) = 0.6.0
Provides:       bundled(node-defaults) = 1.0.3
Provides:       bundled(node-define-properties) = 1.1.3
Provides:       bundled(node-delayed-stream) = 1.0.0
Provides:       bundled(node-delegates) = 1.0.0
Provides:       bundled(node-detect-indent) = 5.0.0
Provides:       bundled(node-detect-newline) = 2.1.0
Provides:       bundled(node-dezalgo) = 1.0.3
Provides:       bundled(node-dot-prop) = 4.2.1
Provides:       bundled(node-dotenv) = 5.0.1
Provides:       bundled(node-duplexer3) = 0.1.4
Provides:       bundled(node-duplexify) = 3.6.0
Provides:       bundled(node-ecc-jsbn) = 0.1.2
Provides:       bundled(node-editor) = 1.0.0
Provides:       bundled(node-emoji-regex) = 7.0.3
Provides:       bundled(node-encoding) = 0.1.12
Provides:       bundled(node-end-of-stream) = 1.4.1
Provides:       bundled(node-env-paths) = 2.2.0
Provides:       bundled(node-err-code) = 1.1.2
Provides:       bundled(node-errno) = 0.1.7
Provides:       bundled(node-es-abstract) = 1.12.0
Provides:       bundled(node-es-to-primitive) = 1.2.0
Provides:       bundled(node-es6-promise) = 4.2.8
Provides:       bundled(node-es6-promisify) = 5.0.0
Provides:       bundled(node-escape-string-regexp) = 1.0.5
Provides:       bundled(node-execa) = 0.7.0
Provides:       bundled(node-extend) = 3.0.2
Provides:       bundled(node-extsprintf) = 1.3.0
Provides:       bundled(node-fast-deep-equal) = 1.1.0
Provides:       bundled(node-fast-json-stable-stringify) = 2.0.0
Provides:       bundled(node-figgy-pudding) = 3.5.1
Provides:       bundled(node-find-npm-prefix) = 1.0.2
Provides:       bundled(node-find-up) = 3.0.0
Provides:       bundled(node-flush-write-stream) = 1.0.3
Provides:       bundled(node-forever-agent) = 0.6.1
Provides:       bundled(node-form-data) = 2.3.2
Provides:       bundled(node-from2) = 1.3.0
Provides:       bundled(node-from2) = 2.3.0
Provides:       bundled(node-fs-minipass) = 1.2.7
Provides:       bundled(node-fs-vacuum) = 1.2.10
Provides:       bundled(node-fs-write-stream-atomic) = 1.0.10
Provides:       bundled(node-fs.realpath) = 1.0.0
Provides:       bundled(node-function-bind) = 1.1.1
Provides:       bundled(node-gauge) = 2.7.4
Provides:       bundled(node-genfun) = 5.0.0
Provides:       bundled(node-gentle-fs) = 2.3.1
Provides:       bundled(node-get-caller-file) = 2.0.5
Provides:       bundled(node-get-stream) = 3.0.0
Provides:       bundled(node-get-stream) = 4.1.0
Provides:       bundled(node-getpass) = 0.1.7
Provides:       bundled(node-glob) = 7.1.6
Provides:       bundled(node-global-dirs) = 0.1.1
Provides:       bundled(node-got) = 6.7.1
Provides:       bundled(node-graceful-fs) = 4.2.4
Provides:       bundled(node-har-schema) = 2.0.0
Provides:       bundled(node-har-validator) = 5.1.0
Provides:       bundled(node-has) = 1.0.3
Provides:       bundled(node-has-flag) = 3.0.0
Provides:       bundled(node-has-symbols) = 1.0.0
Provides:       bundled(node-has-unicode) = 2.0.1
Provides:       bundled(node-hosted-git-info) = 2.8.8
Provides:       bundled(node-http-cache-semantics) = 3.8.1
Provides:       bundled(node-http-proxy-agent) = 2.1.0
Provides:       bundled(node-http-signature) = 1.2.0
Provides:       bundled(node-https-proxy-agent) = 2.2.4
Provides:       bundled(node-humanize-ms) = 1.2.1
Provides:       bundled(node-iconv-lite) = 0.4.23
Provides:       bundled(node-iferr) = 0.1.5
Provides:       bundled(node-iferr) = 1.0.2
Provides:       bundled(node-ignore-walk) = 3.0.3
Provides:       bundled(node-import-lazy) = 2.1.0
Provides:       bundled(node-imurmurhash) = 0.1.4
Provides:       bundled(node-infer-owner) = 1.0.4
Provides:       bundled(node-inflight) = 1.0.6
Provides:       bundled(node-inherits) = 2.0.4
Provides:       bundled(node-ini) = 1.3.5
Provides:       bundled(node-init-package-json) = 1.10.3
Provides:       bundled(node-ip) = 1.1.5
Provides:       bundled(node-ip-regex) = 2.1.0
Provides:       bundled(node-is-callable) = 1.1.4
Provides:       bundled(node-is-ci) = 1.2.1
Provides:       bundled(node-is-cidr) = 3.0.0
Provides:       bundled(node-is-date-object) = 1.0.1
Provides:       bundled(node-is-fullwidth-code-point) = 1.0.0
Provides:       bundled(node-is-fullwidth-code-point) = 2.0.0
Provides:       bundled(node-is-installed-globally) = 0.1.0
Provides:       bundled(node-is-npm) = 1.0.0
Provides:       bundled(node-is-obj) = 1.0.1
Provides:       bundled(node-is-path-inside) = 1.0.1
Provides:       bundled(node-is-redirect) = 1.0.0
Provides:       bundled(node-is-regex) = 1.0.4
Provides:       bundled(node-is-retry-allowed) = 1.2.0
Provides:       bundled(node-is-stream) = 1.1.0
Provides:       bundled(node-is-symbol) = 1.0.2
Provides:       bundled(node-is-typedarray) = 1.0.0
Provides:       bundled(node-isarray) = 0.0.1
Provides:       bundled(node-isarray) = 1.0.0
Provides:       bundled(node-isexe) = 2.0.0
Provides:       bundled(node-isstream) = 0.1.2
Provides:       bundled(node-jsbn) = 0.1.1
Provides:       bundled(node-json-parse-better-errors) = 1.0.2
Provides:       bundled(node-json-schema) = 0.2.3
Provides:       bundled(node-json-schema-traverse) = 0.3.1
Provides:       bundled(node-json-stringify-safe) = 5.0.1
Provides:       bundled(node-jsonparse) = 1.3.1
Provides:       bundled(node-jsprim) = 1.4.1
Provides:       bundled(node-latest-version) = 3.1.0
Provides:       bundled(node-lazy-property) = 1.0.0
Provides:       bundled(node-libcipm) = 4.0.8
Provides:       bundled(node-libnpm) = 3.0.1
Provides:       bundled(node-libnpmaccess) = 3.0.2
Provides:       bundled(node-libnpmconfig) = 1.2.1
Provides:       bundled(node-libnpmhook) = 5.0.3
Provides:       bundled(node-libnpmorg) = 1.0.1
Provides:       bundled(node-libnpmpublish) = 1.1.2
Provides:       bundled(node-libnpmsearch) = 2.0.2
Provides:       bundled(node-libnpmteam) = 1.0.2
Provides:       bundled(node-libnpx) = 10.2.4
Provides:       bundled(node-locate-path) = 3.0.0
Provides:       bundled(node-lock-verify) = 2.1.0
Provides:       bundled(node-lockfile) = 1.0.4
Provides:       bundled(node-lodash._baseindexof) = 3.1.0
Provides:       bundled(node-lodash._baseuniq) = 4.6.0
Provides:       bundled(node-lodash._bindcallback) = 3.0.1
Provides:       bundled(node-lodash._cacheindexof) = 3.0.2
Provides:       bundled(node-lodash._createcache) = 3.1.2
Provides:       bundled(node-lodash._createset) = 4.0.3
Provides:       bundled(node-lodash._getnative) = 3.9.1
Provides:       bundled(node-lodash._root) = 3.0.1
Provides:       bundled(node-lodash.clonedeep) = 4.5.0
Provides:       bundled(node-lodash.restparam) = 3.6.1
Provides:       bundled(node-lodash.union) = 4.6.0
Provides:       bundled(node-lodash.uniq) = 4.5.0
Provides:       bundled(node-lodash.without) = 4.4.0
Provides:       bundled(node-lowercase-keys) = 1.0.1
Provides:       bundled(node-lru-cache) = 4.1.5
Provides:       bundled(node-lru-cache) = 5.1.1
Provides:       bundled(node-make-dir) = 1.3.0
Provides:       bundled(node-make-fetch-happen) = 5.0.2
Provides:       bundled(node-meant) = 1.0.2
Provides:       bundled(node-mime-db) = 1.35.0
Provides:       bundled(node-mime-types) = 2.1.19
Provides:       bundled(node-minimatch) = 3.0.4
Provides:       bundled(node-minimist) = 1.2.5
Provides:       bundled(node-minipass) = 2.9.0
Provides:       bundled(node-minizlib) = 1.3.3
Provides:       bundled(node-mississippi) = 3.0.0
Provides:       bundled(node-mkdirp) = 0.5.5
Provides:       bundled(node-move-concurrently) = 1.0.1
Provides:       bundled(node-ms) = 2.0.0
Provides:       bundled(node-ms) = 2.1.1
Provides:       bundled(node-mute-stream) = 0.0.7
Provides:       bundled(node-node-fetch-npm) = 2.0.2
Provides:       bundled(node-node-gyp) = 5.1.0
Provides:       bundled(node-nopt) = 4.0.3
Provides:       bundled(node-normalize-package-data) = 2.5.0
Provides:       bundled(node-npm-audit-report) = 1.3.3
Provides:       bundled(node-npm-bundled) = 1.1.1
Provides:       bundled(node-npm-cache-filename) = 1.0.2
Provides:       bundled(node-npm-init) = 0.0.0
Provides:       bundled(node-npm-install-checks) = 3.0.2
Provides:       bundled(node-npm-lifecycle) = 3.1.5
Provides:       bundled(node-npm-logical-tree) = 1.2.1
Provides:       bundled(node-npm-normalize-package-bin) = 1.0.1
Provides:       bundled(node-npm-package-arg) = 6.1.1
Provides:       bundled(node-npm-packlist) = 1.4.8
Provides:       bundled(node-npm-pick-manifest) = 3.0.2
Provides:       bundled(node-npm-profile) = 4.0.4
Provides:       bundled(node-npm-registry-fetch) = 4.0.7
Provides:       bundled(node-npm-run-path) = 2.0.2
Provides:       bundled(node-npm-user-validate) = 1.0.0
Provides:       bundled(node-npmlog) = 4.1.2
Provides:       bundled(node-number-is-nan) = 1.0.1
Provides:       bundled(node-oauth-sign) = 0.9.0
Provides:       bundled(node-object-assign) = 4.1.1
Provides:       bundled(node-object-keys) = 1.0.12
Provides:       bundled(node-object.getownpropertydescriptors) = 2.0.3
Provides:       bundled(node-once) = 1.4.0
Provides:       bundled(node-opener) = 1.5.1
Provides:       bundled(node-os-homedir) = 1.0.2
Provides:       bundled(node-os-tmpdir) = 1.0.2
Provides:       bundled(node-osenv) = 0.1.5
Provides:       bundled(node-p-finally) = 1.0.0
Provides:       bundled(node-p-limit) = 2.2.0
Provides:       bundled(node-p-limit) = 2.3.0
Provides:       bundled(node-p-locate) = 3.0.0
Provides:       bundled(node-p-try) = 2.2.0
Provides:       bundled(node-package-json) = 4.0.1
Provides:       bundled(node-pacote) = 9.5.12
Provides:       bundled(node-parallel-transform) = 1.1.0
Provides:       bundled(node-path-exists) = 3.0.0
Provides:       bundled(node-path-is-absolute) = 1.0.1
Provides:       bundled(node-path-is-inside) = 1.0.2
Provides:       bundled(node-path-key) = 2.0.1
Provides:       bundled(node-path-parse) = 1.0.6
Provides:       bundled(node-performance-now) = 2.1.0
Provides:       bundled(node-pify) = 3.0.0
Provides:       bundled(node-prepend-http) = 1.0.4
Provides:       bundled(node-process-nextick-args) = 2.0.0
Provides:       bundled(node-promise-inflight) = 1.0.1
Provides:       bundled(node-promise-retry) = 1.1.1
Provides:       bundled(node-promzard) = 0.3.0
Provides:       bundled(node-proto-list) = 1.2.4
Provides:       bundled(node-protoduck) = 5.0.1
Provides:       bundled(node-prr) = 1.0.1
Provides:       bundled(node-pseudomap) = 1.0.2
Provides:       bundled(node-psl) = 1.1.29
Provides:       bundled(node-pump) = 2.0.1
Provides:       bundled(node-pump) = 3.0.0
Provides:       bundled(node-pumpify) = 1.5.1
Provides:       bundled(node-punycode) = 1.4.1
Provides:       bundled(node-qrcode-terminal) = 0.12.0
Provides:       bundled(node-qs) = 6.5.2
Provides:       bundled(node-query-string) = 6.8.2
Provides:       bundled(node-qw) = 1.0.1
Provides:       bundled(node-rc) = 1.2.8
Provides:       bundled(node-read) = 1.0.7
Provides:       bundled(node-read-cmd-shim) = 1.0.5
Provides:       bundled(node-read-installed) = 4.0.3
Provides:       bundled(node-read-package-json) = 2.1.1
Provides:       bundled(node-read-package-tree) = 5.3.1
Provides:       bundled(node-readable-stream) = 1.1.14
Provides:       bundled(node-readable-stream) = 2.3.6
Provides:       bundled(node-readable-stream) = 3.6.0
Provides:       bundled(node-readdir-scoped-modules) = 1.1.0
Provides:       bundled(node-registry-auth-token) = 3.4.0
Provides:       bundled(node-registry-url) = 3.1.0
Provides:       bundled(node-request) = 2.88.0
Provides:       bundled(node-require-directory) = 2.1.1
Provides:       bundled(node-require-main-filename) = 2.0.0
Provides:       bundled(node-resolve) = 1.10.0
Provides:       bundled(node-resolve-from) = 4.0.0
Provides:       bundled(node-retry) = 0.10.1
Provides:       bundled(node-retry) = 0.12.0
Provides:       bundled(node-rimraf) = 2.7.1
Provides:       bundled(node-run-queue) = 1.0.3
Provides:       bundled(node-safe-buffer) = 5.1.2
Provides:       bundled(node-safe-buffer) = 5.2.0
Provides:       bundled(node-safe-buffer) = 5.2.1
Provides:       bundled(node-safer-buffer) = 2.1.2
Provides:       bundled(node-semver) = 5.7.1
Provides:       bundled(node-semver-diff) = 2.1.0
Provides:       bundled(node-set-blocking) = 2.0.0
Provides:       bundled(node-sha) = 3.0.0
Provides:       bundled(node-shebang-command) = 1.2.0
Provides:       bundled(node-shebang-regex) = 1.0.0
Provides:       bundled(node-signal-exit) = 3.0.2
Provides:       bundled(node-slide) = 1.1.6
Provides:       bundled(node-smart-buffer) = 4.1.0
Provides:       bundled(node-socks) = 2.3.3
Provides:       bundled(node-socks-proxy-agent) = 4.0.2
Provides:       bundled(node-sorted-object) = 2.0.1
Provides:       bundled(node-sorted-union-stream) = 2.1.3
Provides:       bundled(node-spdx-correct) = 3.0.0
Provides:       bundled(node-spdx-exceptions) = 2.1.0
Provides:       bundled(node-spdx-expression-parse) = 3.0.0
Provides:       bundled(node-spdx-license-ids) = 3.0.5
Provides:       bundled(node-split-on-first) = 1.1.0
Provides:       bundled(node-sshpk) = 1.14.2
Provides:       bundled(node-ssri) = 6.0.1
Provides:       bundled(node-stream-each) = 1.2.2
Provides:       bundled(node-stream-iterate) = 1.2.0
Provides:       bundled(node-stream-shift) = 1.0.0
Provides:       bundled(node-strict-uri-encode) = 2.0.0
Provides:       bundled(node-string-width) = 1.0.2
Provides:       bundled(node-string-width) = 2.1.1
Provides:       bundled(node-string-width) = 3.1.0
Provides:       bundled(node-string_decoder) = 0.10.31
Provides:       bundled(node-string_decoder) = 1.1.1
Provides:       bundled(node-string_decoder) = 1.3.0
Provides:       bundled(node-stringify-package) = 1.0.1
Provides:       bundled(node-strip-ansi) = 3.0.1
Provides:       bundled(node-strip-ansi) = 4.0.0
Provides:       bundled(node-strip-ansi) = 5.2.0
Provides:       bundled(node-strip-eof) = 1.0.0
Provides:       bundled(node-strip-json-comments) = 2.0.1
Provides:       bundled(node-supports-color) = 5.4.0
Provides:       bundled(node-tar) = 4.4.13
Provides:       bundled(node-term-size) = 1.2.0
Provides:       bundled(node-text-table) = 0.2.0
Provides:       bundled(node-through) = 2.3.8
Provides:       bundled(node-through2) = 2.0.3
Provides:       bundled(node-timed-out) = 4.0.1
Provides:       bundled(node-tiny-relative-date) = 1.3.0
Provides:       bundled(node-tough-cookie) = 2.4.3
Provides:       bundled(node-tunnel-agent) = 0.6.0
Provides:       bundled(node-tweetnacl) = 0.14.5
Provides:       bundled(node-typedarray) = 0.0.6
Provides:       bundled(node-uid-number) = 0.0.6
Provides:       bundled(node-umask) = 1.1.0
Provides:       bundled(node-unique-filename) = 1.1.1
Provides:       bundled(node-unique-slug) = 2.0.0
Provides:       bundled(node-unique-string) = 1.0.0
Provides:       bundled(node-unpipe) = 1.0.0
Provides:       bundled(node-unzip-response) = 2.0.1
Provides:       bundled(node-update-notifier) = 2.5.0
Provides:       bundled(node-url-parse-lax) = 1.0.0
Provides:       bundled(node-util-deprecate) = 1.0.2
Provides:       bundled(node-util-extend) = 1.0.3
Provides:       bundled(node-util-promisify) = 2.1.0
Provides:       bundled(node-uuid) = 3.3.3
Provides:       bundled(node-validate-npm-package-license) = 3.0.4
Provides:       bundled(node-validate-npm-package-name) = 3.0.0
Provides:       bundled(node-verror) = 1.10.0
Provides:       bundled(node-wcwidth) = 1.0.1
Provides:       bundled(node-which) = 1.3.1
Provides:       bundled(node-which-module) = 2.0.0
Provides:       bundled(node-wide-align) = 1.1.2
Provides:       bundled(node-widest-line) = 2.0.1
Provides:       bundled(node-worker-farm) = 1.7.0
Provides:       bundled(node-wrap-ansi) = 5.1.0
Provides:       bundled(node-wrappy) = 1.0.2
Provides:       bundled(node-write-file-atomic) = 2.4.3
Provides:       bundled(node-xdg-basedir) = 3.0.0
Provides:       bundled(node-xtend) = 4.0.1
Provides:       bundled(node-y18n) = 4.0.0
Provides:       bundled(node-yallist) = 2.1.2
Provides:       bundled(node-yallist) = 3.0.3
Provides:       bundled(node-yargs) = 14.2.3
Provides:       bundled(node-yargs-parser) = 15.0.1

%description -n npm14
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
%patch100 -p1
%patch101 -p1
%patch102 -p1
# Add check_output to configure script (not part of Python 2.6 in SLE11).
%if 0%{?suse_version} == 1110
%endif
%patch104 -p1
%patch106 -p1
%patch107 -p1
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
