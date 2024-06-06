#
# spec file for package nodejs21
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

###########################################################
#
#   WARNING! WARNING! WARNING! WARNING! WARNING! WARNING!
#
# This spec file is generated from a template hosted at
# https://github.com/AdamMajer/nodejs-packaging
#
###########################################################

# Fedora doesn't have rpm-config-SUSE which provides
# ext_man in /usr/lib/rpm/macros.d/macros.obs
%if 0%{?fedora_version}
%define ext_man .gz
%endif

Name:           nodejs21
Version:        21.7.3
Release:        0

# Double DWZ memory limits
%define _dwz_low_mem_die_limit  20000000
%define _dwz_max_die_limit     100000000

%define node_version_number 21

# openssl bsc#1192489 - fix released
%bcond_without openssl_RSA_get0_pss_params

%if 0%{?suse_version} > 1500 || 0%{?fedora_version}
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

# nodejs20+ is not for SLE12
%if %{node_version_number} >= 20 && 0%{?suse_version} > 0 && 0%{?suse_version} < 1500
ExclusiveArch do_not_build
%endif

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

%if 0%{?suse_version} >= 1500 || 0%{?sle_version} >= 120400 || 0%{?fedora_version} >= 35
%bcond_with    intree_openssl
%else
%bcond_without intree_openssl
%endif

%if 0%{?suse_version} >= 1330 || 0%{?fedora_version} >= 35
%bcond_with    intree_cares
%else
%bcond_without intree_cares
%endif

%if 0%{?suse_version} >= 1330 || 0%{?fedora_version} >= 35
%bcond_with    intree_icu
%else
%bcond_without intree_icu
%endif

%if 0%{?suse_version} >= 1550
%bcond_with    intree_nghttp2
%else
%bcond_without intree_nghttp2
%endif

%if 0%{?suse_version} >= 1550
%bcond_with    intree_brotli
%else
%bcond_without intree_brotli
%endif

%ifnarch x86_64 %{ix86}
%bcond_with    gdb
%else
%bcond_without gdb
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

# Python 3.4 compatible node-gyp 
### https://github.com/nodejs/node-gyp.git 
### git archive v7.1.2 | xz > node-gyp_7.1.2.tar.xz 
Source5:        node-gyp_7.1.2.tar.xz 
# Only required to run unit tests in NodeJS 10+ 
Source10:       update_npm_tarball.sh 
Source11:       node_modules.tar.xz
Source20:       bash_output_helper.bash

## Patches not distribution specific
Patch1:         cares_public_headers.patch
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
Patch110:       legacy_python.patch

Patch120:       flaky_test_rerun.patch

Patch132:       test-skip-y2038-on-32bit-time_t.patch

# Use versioned binaries and paths
Patch200:       versioned.patch

Patch305:       qemu_timeouts_arches.patch
Patch308:       node-gyp-config.patch
Patch309:       gcc13.patch

BuildRequires:  pkg-config
BuildRequires:  fdupes
BuildRequires:  procps
BuildRequires:  xz
BuildRequires:  zlib-devel

%if 0%{?suse_version}
BuildRequires:  config(netcfg)
%endif

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
BuildRequires:   gcc5-c++
%define forced_gcc_version 5
%else
BuildRequires:   gcc48-c++
%define forced_gcc_version 4.8
%endif
%endif
# sles == 11 block

# Pick and stick with "latest" compiler at time of LTS release
# for SLE-12:Update targets
%if 0%{?suse_version} == 1315
%if %node_version_number >= 17
BuildRequires:   gcc12-c++
%define forced_gcc_version 12
%else
%if %node_version_number >= 14
BuildRequires:   gcc9-c++
%define forced_gcc_version 9
%else
%if %node_version_number >= 8
BuildRequires:   gcc7-c++
%define forced_gcc_version 7
%endif
%endif
%endif
%endif

%if 0%{?suse_version} == 1500
%if %node_version_number >= 17
BuildRequires:   gcc12-c++
%define forced_gcc_version 12
%endif
%endif
# compiler selection

# No special version defined, use default.
%if ! 0%{?forced_gcc_version:1}
BuildRequires:  gcc-c++
%endif


# Python dependencies
%if %node_version_number >= 14

%if 0%{?suse_version} && 0%{?suse_version} < 1500
BuildRequires:  python36
%define forced_python_version 3.6m
%else
BuildRequires:  python3
%endif

%else
%if %node_version_number >= 12
BuildRequires:  python3

%else
%if 0%{?suse_version} >= 1500
BuildRequires:  python2
%else
BuildRequires:  python
%endif

%endif
%endif

%if 0%{?suse_version} >= 1500 && %{node_version_number} >= 10
BuildRequires:  user(nobody)
BuildRequires:  group(nobody)
%endif

# shared openssl
%if ! 0%{with intree_openssl}

BuildRequires:  pkgconfig(openssl) >= %{openssl_req_ver}

%if 0%{?suse_version}

%if 0%{?suse_version} >= 1500
BuildRequires:  openssl >= %{openssl_req_ver}
BuildRequires:  (libopenssl1_1-hmac if libopenssl-1_1-devel)
BuildRequires:  (libopenssl3-hmac if libopenssl-3-devel)
%else
BuildRequires:  openssl-1_1 >= %{openssl_req_ver}
BuildRequires:  libopenssl1_1-hmac
%endif


# /suse_version
%endif

%if 0%{?fedora_version}
BuildRequires:  openssl >= %{openssl_req_ver}
%endif

%else
# bundled openssl
%if %node_version_number <= 12 && 0%{?suse_version} == 1315 && 0%{?sle_version} < 120400
Provides:       bundled(openssl) = 3.0.13
%else
BuildRequires:  bundled_openssl_should_not_be_required
%endif

# /bundled openssl
%endif

%if ! 0%{with intree_cares}
BuildRequires:  pkgconfig(libcares) >= 1.17.0
%else
Provides:       bundled(libcares2) = 1.27.0
%endif

%if ! 0%{with intree_icu}
BuildRequires:  pkgconfig(icu-i18n) >= 71
%else
Provides:       bundled(icu) = 74.2
%endif

%if ! 0%{with intree_nghttp2}
BuildRequires:  libnghttp2-devel >= 1.41.0
%else
Provides:       bundled(nghttp2) = 1.60.0
%endif

%if 0%{with valgrind_tests}
BuildRequires:  valgrind
%endif

%if %{with libalternatives}
Suggests:       alts
%else
Requires(postun): %{_sbindir}/update-alternatives
%endif
# either for update-alternatives, or their removal
Requires(post): %{_sbindir}/update-alternatives

Recommends:     npm21

#we need ABI virtual provides where SONAMEs aren't enough/not present so deps
#break when binary compatibility is broken
%global nodejs_abi 21.0
Provides:       nodejs(abi) = %{nodejs_abi}

#this corresponds to the "engine" requirement in package.json
Provides:       nodejs(engine) = %{version}

# Multiple versions of NodeJS can be installed at a time, but
# to properly allow correct version execution from 3rd party
# npm software, `env node` requires further help than only
# update-alternatives can provide.
Provides:       nodejs = %{version}
%if %{with libalternatives}
Requires:       nodejs-common >= 5.0
%else
Requires:       nodejs-common
%endif

# For SLE11, to be able to use the certificate store we need to have properly
# symlinked certificates. The compatability symlinks are provided by the
# openssl1 library in the Security Module
%if 0%{?suse_version} == 1110
Requires:       openssl1
%endif

%if %node_version_number >= 12
%ifarch s390
ExclusiveArch:  not_buildable
%endif
%endif

Provides:       bundled(uvwasi) = 0.0.20
Provides:       bundled(libuv) = 1.48.0
Provides:       bundled(v8) = 11.8.172.17
%if %{with intree_brotli}
Provides:       bundled(brotli) = 1.1.0
%else
BuildRequires:  pkgconfig(libbrotlidec)
%endif


Provides:       bundled(llhttp) = 9.2.1
Provides:       bundled(ngtcp2) = 1.3.0
Provides:       bundled(base64) = 0.5.2
Provides:       bundled(simdutf) = 4.0.8
Provides:       bundled(simdjson) = 3.7.0
# bundled url-ada parser, not ada
Provides:       bundled(ada) = 2.7.6

Provides:       bundled(node-acorn) = 8.11.3
Provides:       bundled(node-acorn-walk) = 8.3.2
Provides:       bundled(node-cjs-module-lexer) = 1.2.2
Provides:       bundled(node-corepack) = 0.25.2
Provides:       bundled(node-minimatch) = 9.0.3
Provides:       bundled(node-undici) = 6.11.1

%description
Node.js is a JavaScript runtime built on Chrome's V8 JavaScript engine. Node.js
uses an event-driven, non-blocking I/O model. Node.js has a package ecosystem
provided by npm.

%package devel
Summary:        Development headers for NodeJS 21.x
Group:          Development/Languages/NodeJS
Provides:       nodejs-devel = %{version}
Requires:       npm21 = %{version}
Requires:       %{name} = %{version}

%description devel
This package provides development headers for Node.js needed for creation
of binary modules.

%package -n npm21
Summary:        Package manager for Node.js
Group:          Development/Languages/NodeJS
%if %{with libalternatives}
Requires:       nodejs-common >= 5.0
%else
Requires:       nodejs-common
%endif
Requires:       nodejs21 = %{version}
Provides:       nodejs-npm = %{version}
Obsoletes:      nodejs-npm < 4.0.0
Provides:       npm(npm) = 10.5.0
Provides:       npm = %{version}
%if 0%{?suse_version} >= 1500
%if %{node_version_number} >= 10
Requires:       user(nobody)
Requires:       group(nobody)
%endif
%endif
Provides:       bundled(node-abbrev) = 2.0.0
Provides:       bundled(node-agent-base) = 7.1.0
Provides:       bundled(node-aggregate-error) = 3.1.0
Provides:       bundled(node-ansi-regex) = 5.0.1
Provides:       bundled(node-ansi-regex) = 6.0.1
Provides:       bundled(node-ansi-styles) = 4.3.0
Provides:       bundled(node-ansi-styles) = 6.2.1
Provides:       bundled(node-aproba) = 2.0.0
Provides:       bundled(node-archy) = 1.0.0
Provides:       bundled(node-are-we-there-yet) = 4.0.2
Provides:       bundled(node-balanced-match) = 1.0.2
Provides:       bundled(node-bin-links) = 4.0.3
Provides:       bundled(node-binary-extensions) = 2.2.0
Provides:       bundled(node-brace-expansion) = 2.0.1
Provides:       bundled(node-builtins) = 5.0.1
Provides:       bundled(node-cacache) = 18.0.2
Provides:       bundled(node-chalk) = 5.3.0
Provides:       bundled(node-chownr) = 2.0.0
Provides:       bundled(node-ci-info) = 4.0.0
Provides:       bundled(node-cidr-regex) = 4.0.3
Provides:       bundled(node-clean-stack) = 2.2.0
Provides:       bundled(node-cli-columns) = 4.0.0
Provides:       bundled(node-cli-table3) = 0.6.3
Provides:       bundled(node-clone) = 1.0.4
Provides:       bundled(node-cmd-shim) = 6.0.2
Provides:       bundled(node-color-convert) = 2.0.1
Provides:       bundled(node-color-name) = 1.1.4
Provides:       bundled(node-color-support) = 1.1.3
Provides:       bundled(node-columnify) = 1.6.0
Provides:       bundled(node-common-ancestor-path) = 1.0.1
Provides:       bundled(node-console-control-strings) = 1.1.0
Provides:       bundled(node-cross-spawn) = 7.0.3
Provides:       bundled(node-cssesc) = 3.0.0
Provides:       bundled(node-debug) = 4.3.4
Provides:       bundled(node-defaults) = 1.0.4
Provides:       bundled(node-diff) = 5.2.0
Provides:       bundled(node-eastasianwidth) = 0.2.0
Provides:       bundled(node-emoji-regex) = 8.0.0
Provides:       bundled(node-emoji-regex) = 9.2.2
Provides:       bundled(node-encoding) = 0.1.13
Provides:       bundled(node-env-paths) = 2.2.1
Provides:       bundled(node-err-code) = 2.0.3
Provides:       bundled(node-exponential-backoff) = 3.1.1
Provides:       bundled(node-fastest-levenshtein) = 1.0.16
Provides:       bundled(node-foreground-child) = 3.1.1
Provides:       bundled(node-fs-minipass) = 2.1.0
Provides:       bundled(node-fs-minipass) = 3.0.3
Provides:       bundled(node-function-bind) = 1.1.2
Provides:       bundled(node-gauge) = 5.0.1
Provides:       bundled(node-glob) = 10.3.10
Provides:       bundled(node-graceful-fs) = 4.2.11
Provides:       bundled(node-has-unicode) = 2.0.1
Provides:       bundled(node-hasown) = 2.0.1
Provides:       bundled(node-hosted-git-info) = 7.0.1
Provides:       bundled(node-http-cache-semantics) = 4.1.1
Provides:       bundled(node-http-proxy-agent) = 7.0.2
Provides:       bundled(node-https-proxy-agent) = 7.0.4
Provides:       bundled(node-iconv-lite) = 0.6.3
Provides:       bundled(node-ignore-walk) = 6.0.4
Provides:       bundled(node-imurmurhash) = 0.1.4
Provides:       bundled(node-indent-string) = 4.0.0
Provides:       bundled(node-ini) = 4.1.1
Provides:       bundled(node-init-package-json) = 6.0.0
Provides:       bundled(node-ip-address) = 9.0.5
Provides:       bundled(node-ip-regex) = 5.0.0
Provides:       bundled(node-is-cidr) = 5.0.3
Provides:       bundled(node-is-core-module) = 2.13.1
Provides:       bundled(node-is-fullwidth-code-point) = 3.0.0
Provides:       bundled(node-is-lambda) = 1.0.1
Provides:       bundled(node-isexe) = 2.0.0
Provides:       bundled(node-isexe) = 3.1.1
Provides:       bundled(node-jackspeak) = 2.3.6
Provides:       bundled(node-jsbn) = 1.1.0
Provides:       bundled(node-json-parse-even-better-errors) = 3.0.1
Provides:       bundled(node-json-stringify-nice) = 1.1.4
Provides:       bundled(node-jsonparse) = 1.3.1
Provides:       bundled(node-just-diff) = 6.0.2
Provides:       bundled(node-just-diff-apply) = 5.5.0
Provides:       bundled(node-libnpmaccess) = 8.0.2
Provides:       bundled(node-libnpmdiff) = 6.0.7
Provides:       bundled(node-libnpmexec) = 7.0.8
Provides:       bundled(node-libnpmfund) = 5.0.5
Provides:       bundled(node-libnpmhook) = 10.0.1
Provides:       bundled(node-libnpmorg) = 6.0.2
Provides:       bundled(node-libnpmpack) = 6.0.7
Provides:       bundled(node-libnpmpublish) = 9.0.4
Provides:       bundled(node-libnpmsearch) = 7.0.1
Provides:       bundled(node-libnpmteam) = 6.0.1
Provides:       bundled(node-libnpmversion) = 5.0.2
Provides:       bundled(node-lru-cache) = 10.2.0
Provides:       bundled(node-lru-cache) = 6.0.0
Provides:       bundled(node-make-fetch-happen) = 13.0.0
Provides:       bundled(node-minimatch) = 9.0.3
Provides:       bundled(node-minipass) = 3.3.6
Provides:       bundled(node-minipass) = 5.0.0
Provides:       bundled(node-minipass) = 7.0.4
Provides:       bundled(node-minipass-collect) = 2.0.1
Provides:       bundled(node-minipass-fetch) = 3.0.4
Provides:       bundled(node-minipass-flush) = 1.0.5
Provides:       bundled(node-minipass-json-stream) = 1.0.1
Provides:       bundled(node-minipass-pipeline) = 1.2.4
Provides:       bundled(node-minipass-sized) = 1.0.3
Provides:       bundled(node-minizlib) = 2.1.2
Provides:       bundled(node-mkdirp) = 1.0.4
Provides:       bundled(node-ms) = 2.1.2
Provides:       bundled(node-ms) = 2.1.3
Provides:       bundled(node-mute-stream) = 1.0.0
Provides:       bundled(node-negotiator) = 0.6.3
Provides:       bundled(node-node-gyp) = 10.0.1
Provides:       bundled(node-nopt) = 7.2.0
Provides:       bundled(node-normalize-package-data) = 6.0.0
Provides:       bundled(node-npm-audit-report) = 5.0.0
Provides:       bundled(node-npm-bundled) = 3.0.0
Provides:       bundled(node-npm-install-checks) = 6.3.0
Provides:       bundled(node-npm-normalize-package-bin) = 3.0.1
Provides:       bundled(node-npm-package-arg) = 11.0.1
Provides:       bundled(node-npm-packlist) = 8.0.2
Provides:       bundled(node-npm-pick-manifest) = 9.0.0
Provides:       bundled(node-npm-profile) = 9.0.0
Provides:       bundled(node-npm-registry-fetch) = 16.1.0
Provides:       bundled(node-npm-user-validate) = 2.0.0
Provides:       bundled(node-npmlog) = 7.0.1
Provides:       bundled(node-p-map) = 4.0.0
Provides:       bundled(node-pacote) = 17.0.6
Provides:       bundled(node-parse-conflict-json) = 3.0.1
Provides:       bundled(node-path-key) = 3.1.1
Provides:       bundled(node-path-scurry) = 1.10.1
Provides:       bundled(node-postcss-selector-parser) = 6.0.15
Provides:       bundled(node-proc-log) = 3.0.0
Provides:       bundled(node-promise-all-reject-late) = 1.0.1
Provides:       bundled(node-promise-call-limit) = 3.0.1
Provides:       bundled(node-promise-inflight) = 1.0.1
Provides:       bundled(node-promise-retry) = 2.0.1
Provides:       bundled(node-promzard) = 1.0.0
Provides:       bundled(node-qrcode-terminal) = 0.12.0
Provides:       bundled(node-read) = 2.1.0
Provides:       bundled(node-read-cmd-shim) = 4.0.0
Provides:       bundled(node-read-package-json) = 7.0.0
Provides:       bundled(node-read-package-json-fast) = 3.0.2
Provides:       bundled(node-retry) = 0.12.0
Provides:       bundled(node-safer-buffer) = 2.1.2
Provides:       bundled(node-semver) = 7.6.0
Provides:       bundled(node-set-blocking) = 2.0.0
Provides:       bundled(node-shebang-command) = 2.0.0
Provides:       bundled(node-shebang-regex) = 3.0.0
Provides:       bundled(node-signal-exit) = 4.1.0
Provides:       bundled(node-sigstore) = 2.2.2
Provides:       bundled(node-smart-buffer) = 4.2.0
Provides:       bundled(node-socks) = 2.8.0
Provides:       bundled(node-socks-proxy-agent) = 8.0.2
Provides:       bundled(node-spdx-correct) = 3.2.0
Provides:       bundled(node-spdx-exceptions) = 2.5.0
Provides:       bundled(node-spdx-expression-parse) = 3.0.1
Provides:       bundled(node-spdx-license-ids) = 3.0.17
Provides:       bundled(node-sprintf-js) = 1.1.3
Provides:       bundled(node-ssri) = 10.0.5
Provides:       bundled(node-string-width) = 4.2.3
Provides:       bundled(node-string-width) = 5.1.2
Provides:       bundled(node-strip-ansi) = 6.0.1
Provides:       bundled(node-strip-ansi) = 7.1.0
Provides:       bundled(node-supports-color) = 9.4.0
Provides:       bundled(node-tar) = 6.2.0
Provides:       bundled(node-text-table) = 0.2.0
Provides:       bundled(node-tiny-relative-date) = 1.3.0
Provides:       bundled(node-treeverse) = 3.0.0
Provides:       bundled(node-tuf-js) = 2.2.0
Provides:       bundled(node-unique-filename) = 3.0.0
Provides:       bundled(node-unique-slug) = 4.0.0
Provides:       bundled(node-util-deprecate) = 1.0.2
Provides:       bundled(node-validate-npm-package-license) = 3.0.4
Provides:       bundled(node-validate-npm-package-name) = 5.0.0
Provides:       bundled(node-walk-up-path) = 3.0.1
Provides:       bundled(node-wcwidth) = 1.0.1
Provides:       bundled(node-which) = 2.0.2
Provides:       bundled(node-which) = 4.0.0
Provides:       bundled(node-wide-align) = 1.1.5
Provides:       bundled(node-wrap-ansi) = 7.0.0
Provides:       bundled(node-wrap-ansi) = 8.1.0
Provides:       bundled(node-write-file-atomic) = 5.0.1
Provides:       bundled(node-yallist) = 4.0.0

%description -n npm21
A package manager for Node.js that allows developers to install and
publish packages to a package registry.

%package -n corepack21
Summary:        Helper bridge between NodeJS projects and their dependencies
Group:          Development/Languages/NodeJS
Requires:       nodejs-common >= 5.0

%description -n corepack21
Zero-runtime-dependency package acting as bridge between Node projects
and their package managers.

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

%if %{node_version_number} == 16
tar zxf %{S:12}
%endif

%if %{node_version_number} <= 10
rm -r deps/npm/*
pushd deps/npm
tar zxf %{SOURCE9} --strip-components=1
tar Jxf %{SOURCE90}
popd
%endif

%if %{node_version_number} >= 10
tar Jxf %{SOURCE11}
%endif

# downgrade node-gyp to last version that supports python 3.4 for SLE12
%if 0%{?suse_version} && 0%{?suse_version} < 1500 && %{node_version_number} >= 16 && %{node_version_number} < 22
rm -r  deps/npm/node_modules/node-gyp
mkdir deps/npm/node_modules/node-gyp
pushd deps/npm/node_modules/node-gyp
tar Jxf %{SOURCE5}
popd

%if %{node_version_number} >= 19
%patch -P 308 -p1
%else
%endif
%endif

%patch -P 1 -p1
%patch -P 3 -p1
%if 0%{?suse_version} < 1500
%endif
%if %{node_version_number} <= 12 && 0%{?suse_version} < 1500
%patch -P 5 -p1
%endif
%patch -P 7 -p1
%if 0%{with valgrind_tests}
%endif
%patch -P 13 -p1
%patch -P 100 -p1
%patch -P 101 -p1
%if 0%{?suse_version} >= 1500 || 0%{?suse_version} == 0
%patch -P 102 -p1
%endif
# Add check_output to configure script (not part of Python 2.6 in SLE11).
%if 0%{?suse_version} == 1110
%endif
%patch -P 104 -p1
%patch -P 106 -p1
%patch -P 110 -p1
%patch -P 120 -p1
%patch -P 132 -p1
%if ! 0%{with openssl_RSA_get0_pss_params}
%endif
%patch -P 200 -p1

%patch -P 305 -p1
%patch -P 309 -p1

%if %{node_version_number} == 12
# minimist security update - patch50
rm -r deps/npm/node_modules/mkdirp/node_modules/minimist
rmdir ./deps/npm/node_modules/mkdirp/node_modules
%endif

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
export PREFIX=/usr
export CFLAGS="%{?build_cflags:%build_cflags}%{?!build_cflags:%optflags} -fno-strict-aliasing"
# -Wno-class-memaccess is not available in gcc < 8 (= system compiler on Leap until at least 15.3 is gcc7)
export CXXFLAGS="%{?build_cxxflags:%build_cxxflags}%{?!build_cxxflags:%optflags} -Wno-error=return-type -fno-strict-aliasing"
%if 0%{?forced_gcc_version} >= 8 || 0%{?suse_version} > 1500 || 0%{?fedora_version} >= 35
export CXXFLAGS="\${CXXFLAGS} -Wno-class-memaccess"
%endif
export LDFLAGS="%{?build_ldflags}"

%if !0%{?with nodejs_lto}
export LDFLAGS="\${LDFLAGS} -fno-lto"
%endif

# reduce disk space pressure
export CFLAGS="\${CFLAGS} -g1"
export CXXFLAGS="\${CXXFLAGS} -g1"
export LDFLAGS="\${LDFLAGS} -Wl,--reduce-memory-overhead"

%if 0%{?forced_gcc_version:1}
export CC=gcc-%{forced_gcc_version}
export CXX=g++-%{forced_gcc_version}
%endif

EOF

. ./spec.build.config

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
%endif
%if ! 0%{with intree_nghttp2}
    --shared-nghttp2 \
%endif
%if ! 0%{with intree_brotli}
    --shared-brotli \
%endif
%if 0%{with gdb}
    --gdb \
%endif
%if %{node_version_number} < 19
    --without-dtrace \
%endif
%if %{node_version_number} >= 16 && (0%{?suse_version} > 1550 || 0%{?sle_version} >= 150400)
    --openssl-default-cipher-list=PROFILE=SYSTEM \
%endif
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
install -D -m 644 deps/npm/man/man1/npx.1 %{buildroot}%{_mandir}/man1/npx%{node_version_number}.1

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
%if ! %{with libalternatives}
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f node-default     %{buildroot}%{_sysconfdir}/alternatives/node-default
ln -s -f node.1%{ext_man} %{buildroot}%{_sysconfdir}/alternatives/node.1%{ext_man}
ln -s -f npm-default      %{buildroot}%{_sysconfdir}/alternatives/npm-default
ln -s -f npm.1%{ext_man}  %{buildroot}%{_sysconfdir}/alternatives/npm.1%{ext_man}
ln -s %{_sysconfdir}/alternatives/node-default         %{buildroot}%{_bindir}/node-default
ln -s %{_sysconfdir}/alternatives/node.1%{ext_man}     %{buildroot}%{_mandir}/man1/node.1%{ext_man}
ln -s %{_sysconfdir}/alternatives/npm-default          %{buildroot}%{_bindir}/npm-default
ln -s %{_sysconfdir}/alternatives/npm.1%{ext_man}      %{buildroot}%{_mandir}/man1/npm.1%{ext_man}
ln -s -f npx-default      %{buildroot}%{_sysconfdir}/alternatives/npx-default
ln -s -f npx.1%{ext_man}  %{buildroot}%{_sysconfdir}/alternatives/npx.1%{ext_man}
ln -s %{_sysconfdir}/alternatives/npx-default          %{buildroot}%{_bindir}/npx-default
ln -s %{_sysconfdir}/alternatives/npx.1%{ext_man}      %{buildroot}%{_mandir}/man1/npx.1%{ext_man}
%if %{node_version_number} >= 14
ln -s -f corepack-default      %{buildroot}%{_sysconfdir}/alternatives/corepack-default
ln -s -f corepack.1%{ext_man}  %{buildroot}%{_sysconfdir}/alternatives/corepack.1%{ext_man}
ln -s %{_sysconfdir}/alternatives/corepack-default          %{buildroot}%{_bindir}/corepack-default
ln -s %{_sysconfdir}/alternatives/corepack.1%{ext_man}      %{buildroot}%{_mandir}/man1/corepack.1%{ext_man}
%endif
%endif

# libalternatives - can always ship
mkdir -p %{buildroot}%{_datadir}/libalternatives/{node,npm,npx};
cat > %{buildroot}%{_datadir}/libalternatives/node/%{node_version_number}.conf <<EOF
binary=%{_bindir}/node%{node_version_number}
man=node%{node_version_number}.1
EOF
cat > %{buildroot}%{_datadir}/libalternatives/npm/%{node_version_number}.conf <<EOF
binary=%{_bindir}/npm%{node_version_number}
man=npm%{node_version_number}.1
group=npm,npx
EOF
cat > %{buildroot}%{_datadir}/libalternatives/npx/%{node_version_number}.conf <<EOF
binary=%{_bindir}/npx%{node_version_number}
man=npx%{node_version_number}.1
group=npm,npx
EOF
%if %{node_version_number} >= 14
mkdir -p %{buildroot}%{_datadir}/libalternatives/corepack;
cat > %{buildroot}%{_datadir}/libalternatives/corepack/%{node_version_number}.conf <<EOF
binary=%{_bindir}/corepack%{node_version_number}
man=corepack%{node_version_number}.1
EOF
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

%if %{node_version_number} >= 20
rm test/parallel/test-strace-openat-openssl.js
%endif

# Update the python3 executable name to point at forced python version
# needed to fix build on SLE12 SP5
%if 0%{?forced_python_version:1}
sed -i -e "s,'python3','python%{forced_python_version}'," test/parallel/test-child-process-set-blocking.js
test -e tools/pseudo-tty.py && sed -i -e "s,^#!/usr/bin/env python3$,#!/usr/bin/python%{forced_python_version}," tools/pseudo-tty.py ||:
%endif

ln addon-rpm.gypi deps/npm/node_modules/node-gyp/addon-rpm.gypi
# Tarball doesn't have eslint package distributed, so disable some tests
find test -name \*-eslint-\* -print -delete
# No documentation is generated, don't bother checking it, and check broken on older nodejs
%if %{node_version_number} <= 10
rm test/doctool/test-make-doc.js
%endif
# DNS lookup doesn't work in build root
rm test/parallel/test-dns-cancel-reverse-lookup.js \
   test/parallel/test-dns-resolveany.js
# multicast test fail since no socket?
rm test/parallel/test-dgram-membership.js

%if %{node_version_number} >= 18
# OBS broken /etc/hosts -- https://github.com/openSUSE/open-build-service/issues/13104
rm test/parallel/test-net-socket-connect-without-cb.js test/parallel/test-tcp-wrap-listen.js
%endif

%if 0%{?fedora_version}
# test/parallel/test-crypto-certificate.js requires OPENSSL_ENABLE_MD5_VERIFY=1
# as SPKAC required MD5 for verification
# https://src.fedoraproject.org/rpms/openssl/blob/rawhide/f/0006-Disable-signature-verification-with-totally-unsafe-h.patch
export OPENSSL_ENABLE_MD5_VERIFY=1

# test failures
# error:14094410:SSL routines:ssl3_read_bytes:sslv3 alert handshake
# failure:ssl/record/rec_layer_s3.c:1543:SSL alert number 40
rm test/parallel/test-tls-no-sslv3.js
%if %{node_version_number} >= 18
rm -r test/addons/openssl-providers
rm test/parallel/test-crypto-fips.js
%endif

%endif
# fedora

# qemu test failures
%if %{node_version_number} >= 18 && 0%{?qemu_user_space_build}
# sequential/test-debugger-*: timeout hit?
rm -v test/*/test-debugger-*.js
# parallel tests are not parallel under qemu
rm -v test/parallel/test-*.js test/parallel/test-*.mjs
# RuntimeError: memory access out of bounds
rm -v test/wasi/test-*.js
# ESM import hits assertion, timeout error?
rm -v test/es-module/test-esm-*.js
# AssertionError [ERR_ASSERTION]: Missing expected exception
rm -v test/js-native-api/test_constructor/test*.js
# Too slow for performance tests
rm -v test/sequential/test-perf-*.js test/sequential/test-diagnostic-*.js
%endif

# Run CI tests
%if 0%{with valgrind_tests}
# valgrind may have false positives, so do not fail on these by default
make test-valgrind ||:
%endif
make test-ci

%files
%defattr(-, root, root)
%license LICENSE
%doc doc/changelogs/CHANGELOG_V%{node_version_number}.md
%doc *.md
%doc deps/v8/tools/gdbinit
%dir %{_libdir}/node_modules
%dir %{_datadir}/libalternatives
%dir %{_datadir}/libalternatives/node
%{_datadir}/libalternatives/node/%{node_version_number}.conf
%{_bindir}/node%{node_version_number}
%{_mandir}/man1/node%{node_version_number}.1%{ext_man}
%if ! 0%{with libalternatives}
%ghost %{_bindir}/node-default
%ghost %{_mandir}/man1/node.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/node-default
%ghost %{_sysconfdir}/alternatives/node.1%{ext_man}
%endif
%exclude %{_libdir}/node_modules/npm%{node_version_number}
# We need to own directory on old versions of SLE
%if 0%{?suse_version} < 1500
%dir %{_defaultlicensedir}
%endif

%files -n npm%{node_version_number}
%defattr(-, root, root)
%dir %{_datadir}/libalternatives
%dir %{_datadir}/libalternatives/npm
%dir %{_datadir}/libalternatives/npx
%{_datadir}/libalternatives/npm/%{node_version_number}.conf
%{_datadir}/libalternatives/npx/%{node_version_number}.conf
%{_bindir}/npm%{node_version_number}
%{_libdir}/node_modules/npm%{node_version_number}
%{_mandir}/man1/npm%{node_version_number}.1%{ext_man}
%if ! 0%{with libalternatives}
%ghost %{_bindir}/npm-default
%ghost %{_mandir}/man1/npm.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/npm-default
%ghost %{_sysconfdir}/alternatives/npm.1%{ext_man}
%endif

%{_bindir}/npx%{node_version_number}
%{_mandir}/man1/npx%{node_version_number}.1%{ext_man}
%if ! %{with libalternatives}
%ghost %{_bindir}/npx-default
%ghost %{_mandir}/man1/npx.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/npx-default
%ghost %{_sysconfdir}/alternatives/npx.1%{ext_man}
%endif

%if %{node_version_number} >= 14
%files -n corepack%{node_version_number}
%defattr(-, root, root)
%{_bindir}/corepack%{node_version_number}
%{_libdir}/node_modules/corepack%{node_version_number}
%dir %{_datadir}/libalternatives/corepack
%{_datadir}/libalternatives/corepack/%{node_version_number}.conf
%if ! %{with libalternatives}
%ghost %{_bindir}/corepack-default
%ghost %{_mandir}/man1/corepack.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/corepack-default
%ghost %{_sysconfdir}/alternatives/corepack.1%{ext_man}
%endif
%endif

%files devel
%defattr(-, root, root)
%{_includedir}/node%{node_version_number}
%if %{node_version_number} < 19
%dir %{_datadir}/systemtap
%dir %{_datadir}/systemtap/tapset
%{_datadir}/systemtap/tapset/node%{node_version_number}.stp
%endif

%files docs
%defattr(-,root,root)
%doc doc/api

%if %{with libalternatives}

%post
update-alternatives --remove node-default %{_bindir}/node%{node_version_number}

%post -n npm%{node_version_number}
update-alternatives --remove npm-default %{_bindir}/npm%{node_version_number}
update-alternatives --remove npx-default %{_bindir}/npx%{node_version_number}

%if %{node_version_number} >= 14
%post -n corepack%{node_version_number}
update-alternatives --remove corepack-default %{_bindir}/corepack%{node_version_number}
%endif

%else
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
update-alternatives \
        --install %{_bindir}/npx-default npx-default %{_bindir}/npx%{node_version_number} %{node_version_number} \
        --slave %{_mandir}/man1/npx.1%{ext_man} npx.1%{ext_man} %{_mandir}/man1/npx%{node_version_number}.1%{ext_man}

%postun -n npm%{node_version_number}
if [ ! -f %{_bindir}/npm%{node_version_number} ] ; then
    update-alternatives --remove npm-default %{_bindir}/npm%{node_version_number}
fi
if [ ! -f %{_bindir}/npx%{node_version_number} ] ; then
    update-alternatives --remove npx-default %{_bindir}/npx%{node_version_number}
fi

%if %{node_version_number} >= 14
%pre -n corepack%{node_version_number}
# remove files that are no longer owned but provided by update-alternatives
if ! [ -L %{_mandir}/man1/corepack.1%{ext_man} ]; then
    rm -f %{_mandir}/man1/corepack.1%{ext_man}
fi

%post -n corepack%{node_version_number}
update-alternatives \
        --install %{_bindir}/corepack-default corepack-default %{_bindir}/corepack%{node_version_number} %{node_version_number} \
        --slave %{_mandir}/man1/corepack.1%{ext_man} corepack.1%{ext_man} %{_mandir}/man1/corepack%{node_version_number}.1%{ext_man}

%postun -n corepack%{node_version_number}
if [ ! -f %{_bindir}/corepack%{node_version_number} ] ; then
    update-alternatives --remove corepack-default %{_bindir}/corepack%{node_version_number}
fi
%endif

%endif

%changelog
