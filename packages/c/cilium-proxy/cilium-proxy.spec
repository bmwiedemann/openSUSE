#
# spec file for package cilium-proxy
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           cilium-proxy
Version:        20200109
Release:        0
Summary:        L7 proxy and communication bus for Cilium
License:        Apache-2.0
Url:            https://github.com/cilium/proxy
Source0:        %{name}-%{version}.tar.xz
Source1:        BUILD
Patch0:         0001-Adjust-cilium-proxy-to-Envoy-1.12.2.patch
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
BuildRequires:  envoy-proxy-source
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
Cilium Proxy is an L7 proxy for microservices which forms a microservice mesh.
It's a part of Cilium infrastructure.

%prep
%autosetup -p1
# Point cilium-proxy TLS bits to the module with OpenSSL support.
sed -i \
    "s|@envoy//source/extensions/transport_sockets/tls|@envoy_openssl//source/extensions/transport_sockets/tls|" \
    cilium/BUILD

# cilium-proxy is built from the envoy-proxy source tree, with cilium-proxy
# sources included as a dependency.
cp -r /usr/src/envoy-proxy %{_builddir}
cd %{_builddir}/envoy-proxy
cp %{SOURCE1} .

# Add cilium-proxy as a depencency
cat <<EOF >> WORKSPACE

local_repository(
    name = "cilium_proxy",
    path = "%{_builddir}/%{name}-%{version}",
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

%build
cd %{_builddir}/envoy-proxy
# TODO(mrostecki): Create a macro in bazel package.
GO_PROTOBUF_DIR=$(find %{_datadir}/go -name protobuf -type d | grep -v vendor)
GO_TOOLS_DIR=$(find %{_datadir}/go -name tools -type d | grep -v vendor)
bazel build \
    -c dbg \
    --color=no \
    --copt="-Wno-error=old-style-cast" \
    --cxxopt="-Wno-error=old-style-cast" \
    --copt="-Wno-unused-parameter" \
    --cxxopt="-Wno-unused-parameter" \
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
    --override_repository="upb=/usr/src/upb" \
    --override_repository="zlib=%{_datadir}/bazel-workspaces/zlib" \
    --strip=never \
    --verbose_failures \
    //:envoy
bazel shutdown

%install
cd %{_builddir}/envoy-proxy
install -D -m0755 bazel-bin/envoy %{buildroot}%{_bindir}/cilium-envoy

%files
%license LICENSE
%doc README.md
%{_bindir}/cilium-envoy

%changelog

