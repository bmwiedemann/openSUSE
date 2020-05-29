#
# spec file for package envoy-proxy
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


%define moonjit_version %(rpm -q --qf '%%{VERSION}' moonjit)
%define moonjit_shortver %(cut -d . -f 1 <<< %{moonjit_version}).%(cut -d . -f 2 <<< %{moonjit_version})
%define src_install_dir /usr/src/%{name}

Name:           envoy-proxy
Version:        1.12.2+git.20200109
Release:        0
Summary:        L7 proxy and communication bus
License:        Apache-2.0
URL:            https://www.envoyproxy.io/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
Patch0:         bazel-Fix-optional-dynamic-linking-of-OpenSSL.patch
Patch1:         compatibility-with-TLS-1.2-and-OpenSSL-1.1.0.patch
Patch2:         logger-Use-spdlog-memory_buf_t-instead-of-fmt-memory.patch
Patch3:         0001-server-add-getTransportSocketFactoryContext-to-Filte.patch
Patch4:         0002-test-Fix-mocks.patch
Patch5:         0003-test-Fix-format.patch
Patch6:         0004-server-Add-comments-pointing-out-implementation-deta.patch
Patch7:         0005-server-Move-setInitManager-to-TransportSocketFactory.patch
Patch8:         0006-fix-format.patch
Patch9:         big-endian-support.patch
BuildRequires:  abseil-cpp-source
BuildRequires:  backward-cpp-devel
BuildRequires:  bazel-apple-support-source
BuildRequires:  bazel-gazelle-source
BuildRequires:  bazel-platforms
BuildRequires:  bazel-rules-apple-source
BuildRequires:  bazel-rules-cc-source
BuildRequires:  bazel-rules-foreign-cc-source
BuildRequires:  bazel-rules-go-source
BuildRequires:  bazel-rules-java-source
BuildRequires:  bazel-rules-proto-source
BuildRequires:  bazel-rules-python-source
BuildRequires:  bazel-rules-swift-source
BuildRequires:  bazel-skylib-source
BuildRequires:  bazel-toolchains-source
BuildRequires:  bazel-workspaces
BuildRequires:  bazel2.0
BuildRequires:  benchmark-devel
BuildRequires:  c-ares-devel
BuildRequires:  cel-cpp-source
BuildRequires:  cmake
BuildRequires:  dd-opentracing-cpp-devel
BuildRequires:  envoy-build-tools
BuildRequires:  envoy-protoc-gen-validate-source
BuildRequires:  fdupes
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  gcovr
BuildRequires:  git
BuildRequires:  golang-github-golang-protobuf
BuildRequires:  golang-org-x-tools
BuildRequires:  golang-packaging
BuildRequires:  googleapis-source
BuildRequires:  gperftools-devel
BuildRequires:  grpc-httpjson-transcoding-source
BuildRequires:  grpc-source
BuildRequires:  gtest
BuildRequires:  http-parser-devel
BuildRequires:  jwt_verify_lib-source
BuildRequires:  kafka-source
BuildRequires:  libcircllhist-devel
BuildRequires:  libcurl-devel
BuildRequires:  libevent-devel
BuildRequires:  libnghttp2-devel
BuildRequires:  libprotobuf-mutator-devel
BuildRequires:  libtool
BuildRequires:  lightstep-tracer-cpp-source
BuildRequires:  moonjit-devel
BuildRequires:  msgpack-devel
BuildRequires:  nghttp2-devel
BuildRequires:  ninja
BuildRequires:  opencensus-cpp-source
BuildRequires:  opencensus-proto-source
BuildRequires:  opentracing-cpp-source
BuildRequires:  prometheus-client-model-source
BuildRequires:  protobuf-source
BuildRequires:  protoc-gen-gogo-source
BuildRequires:  python3
BuildRequires:  python3-Jinja2
BuildRequires:  python3-MarkupSafe
BuildRequires:  rapidjson-devel
BuildRequires:  re2-devel
BuildRequires:  spdlog-devel
BuildRequires:  sql-parser-devel
BuildRequires:  tclap
BuildRequires:  udpa-source
BuildRequires:  upb-source
BuildRequires:  vim
BuildRequires:  xxhash-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  zipkin-api-source
BuildRequires:  zlib-devel
BuildRequires:  golang(API) >= 1.12
BuildRequires:  pkgconfig(openssl)
ExcludeArch:    %ix86

%description
Envoy is an L7 proxy and communication bus designed for large modern service
oriented architectures.

%package source
Summary:        Source code of bazel-rules-cc

%description source
Envoy is an L7 proxy and communication bus designed for large modern service
oriented architectures.

This package contains source code of Envoy.

%prep
%autosetup -p1

# Tell Bazel to look for Python dependencies on Python 3 environment from host.
PATH_JINJA2=$(python3 -c "import jinja2; print(jinja2.__path__[0])")
PATH_MARKUPSAGE=$(python3 -c "import markupsafe; print(markupsafe.__path__[0])")
cat <<EOF >> WORKSPACE

new_local_repository(
    name = "com_github_pallets_jinja",
    path = "${PATH_JINJA2}",
    build_file_content = """py_library(
    name = "jinja2",
    srcs = glob(["**/*.py"]),
    visibility = ["//visibility:public"],
)
""",
)

new_local_repository(
    name = "com_github_pallets_markupsafe",
    path = "${PATH_MARKUPSAFE}",
    build_file_content = """py_library(
    name = "markupsafe",
    srcs = glob(["**/*.py"]),
    visibility = ["//visibility:public"],
)
""",
)
EOF

# Envoy has to be built as a git repository, so let's create one...
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git init
git add .
# use fixed date for reproducible builds (boo#1047218):
GIT_AUTHOR_DATE=2000-01-01T01:01:01 GIT_COMMITTER_DATE=2000-01-01T01:01:01 \
git commit -m "Dummy commit just to satisfy bazel" &> /dev/null

# Tell Bazel to use Go from host.
sed -i -e "s|1.13.5|host|" envoy/bazel/dependency_imports.bzl

# Get rid of:
# - Bazel rules for Python dependencies - to use them from host Python instead
#   of creating a separate Python environment.
# - Dependencies using "foreign_cc" utility - thanks to our bazel-workspaces
#   project, we can just link those C/C++ libraries dynamically.
sed -i \
    -e "/    _python_deps()/d" \
    -e "s|@envoy//bazel/foreign_cc:ares|@com_github_c_ares_c_ares//:ares|" \
    -e "s|@envoy//bazel/foreign_cc:yaml|@com_github_jbeder_yaml_cpp//:all|" \
    -e "s|@envoy//bazel/foreign_cc:event|@com_github_libevent_libevent//:libevent|" \
    -e "s|@envoy//bazel/foreign_cc:zlib|@zlib//:zlib|" \
    -e "s|@envoy//bazel/foreign_cc:nghttp2|@com_github_nghttp2_nghttp2//:all|" \
    -e "s|@envoy//bazel/foreign_cc:curl|@com_github_curl//:curl|" \
    -e "s|@envoy//bazel/foreign_cc:luajit|@com_github_luajit_luajit//:luajit|" \
    -e "s|@envoy//bazel/foreign_cc:gperftools|@com_github_gperftools_gperftools//:gperftools|" \
    envoy/bazel/repositories.bzl

# Bump the version of luajit.
sed -i "s|luajit-2.1|moonjit-%{moonjit_shortver}|g" envoy/source/extensions/filters/common/lua/lua.h

# Fix includes of sqlparser headers.
find . -type f "(" -name "*.cc" -o -name "*.h" ")" -exec sed -i -e "s|include/sqlparser|sqlparser|" {} +

# Link OpenSSL dynamically.
sed -i \
    -e "s|openssl_repository()|# openssl_repository|" \
    -e "s|# openssl_shared_repository()|openssl_shared_repository()|" \
    WORKSPACE
sed -i "s|/usr/lib/x86_64-linux-gnu|%{_libdir}|g" openssl.bzl

# Fix shebangs in scripts.
find . -type f -exec sed -i \
    -e "s|#!/usr/bin/env bash.*$|#!/bin/bash|" \
    -e "s|#!/usr/bin/env python.*$|#!/usr/bin/python3|" \
    -e "s|#!/usr/bin/env sh.*$|#!/bin/sh|" \
    "{}" +

# Adjust envoy-openssl code to getTransportSocketFactoryContext changes.
sed -i \
    "s|context.statsScope|context.scope|" \
    source/extensions/transport_sockets/tls/config.cc

# Yes, someone seriously added an executable bit to a header file...
find . -type f -name "*.h" -exec chmod -x "{}" +

%build
# TODO(mrostecki): Create a macro in bazel package.
GO_PROTOBUF_DIR=$(find %{_datadir}/go -name protobuf -type d | grep -v vendor)
GO_TOOLS_DIR=$(find %{_datadir}/go -name tools -type d | grep -v vendor)
bazel build \
    -c dbg \
    --color=no \
    --copt="-Wno-unused-parameter" \
    --copt="-Wno-deprecated-declarations" \
    --cxxopt="-Wno-unused-parameter" \
    --cxxopt="-Wno-deprecated-declarations" \
    --curses=no \
    --host_force_python=PY3 \
    --incompatible_bzl_disallow_load_after_statement=false \
    --override_repository="bazel_gazelle=/usr/src/bazel-gazelle" \
    --override_repository="bazel_skylib=/usr/src/bazel-skylib" \
    --override_repository="bazel_toolchains=/usr/src/bazel-toolchains" \
    --override_repository="bssl_wrapper=%{_datadir}/bazel-workspaces/bsslwrapper" \
    --override_repository="build_bazel_apple_support=/usr/src/bazel-apple-support" \
    --override_repository="build_bazel_rules_apple=/usr/src/bazel-rules-apple" \
    --override_repository="build_bazel_rules_swift=/usr/src/bazel-rules-swift" \
    --override_repository="com_envoyproxy_protoc_gen_validate=/usr/src/envoy-protoc-gen-validate" \
    --override_repository="com_lightstep_tracer_cpp=/usr/src/lightstep-tracer-cpp" \
    --override_repository="com_github_c_ares_c_ares=%{_datadir}/bazel-workspaces/c-ares" \
    --override_repository="com_github_circonus_labs_libcircllhist=%{_datadir}/bazel-workspaces/libcircllhist" \
    --override_repository="com_github_cncf_udpa=/usr/src/udpa" \
    --override_repository="com_github_curl=%{_datadir}/bazel-workspaces/curl" \
    --override_repository="com_github_cyan4973_xxhash=%{_datadir}/bazel-workspaces/xxhash" \
    --override_repository="com_github_datadog_dd_opentracing_cpp=%{_datadir}/bazel-workspaces/dd-opentracing-cpp" \
    --override_repository="com_github_mirror_tclap=%{_datadir}/bazel-workspaces/tclap" \
    --override_repository="com_github_eile_tclap=%{_datadir}/bazel-workspaces/tclap" \
    --override_repository="com_github_envoyproxy_sqlparser=%{_datadir}/bazel-workspaces/sql-parser" \
    --override_repository="com_github_fmtlib_fmt=%{_datadir}/bazel-workspaces/fmtlib" \
    --override_repository="com_github_gabime_spdlog=%{_datadir}/bazel-workspaces/spdlog" \
    --override_repository="com_github_gogo_protobuf=/usr/src/protoc-gen-gogo" \
    --override_repository="com_github_golang_protobuf=${GO_PROTOBUF_DIR}" \
    --override_repository="com_github_google_jwt_verify=/usr/src/jwt_verify_lib" \
    --override_repository="com_github_google_jwt_verify_patched=/usr/src/jwt_verify_lib" \
    --override_repository="com_github_google_libprotobuf_mutator=%{_datadir}/bazel-workspaces/libprotobuf-mutator" \
    --override_repository="com_github_gperftools_gperftools=%{_datadir}/bazel-workspaces/gperftools" \
    --override_repository="com_github_grpc_grpc=/usr/src/grpc" \
    --override_repository="com_github_jbeder_yaml_cpp=%{_datadir}/bazel-workspaces/yaml-cpp" \
    --override_repository="com_github_libevent_libevent=%{_datadir}/bazel-workspaces/libevent" \
    --override_repository="com_github_luajit_luajit=%{_datadir}/bazel-workspaces/luajit" \
    --override_repository="com_github_nghttp2_nghttp2=%{_datadir}/bazel-workspaces/nghttp2" \
    --override_repository="com_github_nodejs_http_parser=%{_datadir}/bazel-workspaces/http-parser" \
    --override_repository="com_github_openzipkin_zipkinapi=/usr/src/zipkin-api" \
    --override_repository="com_github_tencent_rapidjson=%{_datadir}/bazel-workspaces/rapidjson" \
    --override_repository="com_google_absl=/usr/src/abseil-cpp" \
    --override_repository="com_google_cel_cpp=/usr/src/cel-cpp" \
    --override_repository="com_google_googleapis=/usr/src/googleapis" \
    --override_repository="com_google_protobuf=/usr/src/protobuf" \
    --override_repository="com_googlesource_code_re2=%{_datadir}/bazel-workspaces/re2" \
    --override_repository="envoy_build_tools=%{_datadir}/envoy-build-tools" \
    --override_repository="grpc_httpjson_transcoding=/usr/src/grpc-httpjson-transcoding" \
    --override_repository="io_bazel_rules_go=/usr/src/bazel-rules-go" \
    --override_repository="io_opencensus_cpp=/usr/src/opencensus-cpp" \
    --override_repository="io_opentracing_cpp=/usr/src/opentracing-cpp" \
    --override_repository="kafka_source=/usr/src/kafka" \
    --override_repository="opencensus_proto=/usr/src/opencensus-proto/src" \
    --override_repository="openssl_cbs=%{_datadir}/bazel-workspaces/openssl-cbs" \
    --override_repository="org_golang_x_tools=${GO_TOOLS_DIR}" \
    --override_repository="platforms=/usr/share/bazel-platforms" \
    --override_repository="prometheus_metrics_model=/usr/src/prometheus-client-model" \
    --override_repository="rules_cc=/usr/src/bazel-rules-cc" \
    --override_repository="rules_foreign_cc=/usr/src/bazel-rules-foreign-cc" \
    --override_repository="rules_java=/usr/src/bazel-rules-java" \
    --override_repository="rules_proto=/usr/src/bazel-rules-proto" \
    --override_repository="rules_python=/usr/src/bazel-rules-python" \
    --override_repository="upb=/usr/src/upb" \
    --override_repository="zlib=%{_datadir}/bazel-workspaces/zlib" \
    --strip=never \
    --verbose_failures \
%ifarch ppc64le
    --local_cpu_resources=HOST_CPUS*.5 \
%endif
    //:envoy
bazel shutdown

%install
install -D -m0755 bazel-bin/envoy %{buildroot}%{_bindir}/envoy-proxy

# Install sources
rm -rf .git bazel-*
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}
fdupes %{buildroot}%{src_install_dir}

%files
%license LICENSE
%doc README.md
%{_bindir}/envoy-proxy

%files source
%{src_install_dir}

%changelog
