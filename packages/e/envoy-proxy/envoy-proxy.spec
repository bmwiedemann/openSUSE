#
# spec file for package envoy-proxy
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           envoy-proxy
Version:        1.8.0+git20181105
Release:        0
Summary:        L7 proxy and communication bus
License:        Apache-2.0
Group:          Productivity/Networking/Web/Proxy
Url:            https://www.envoyproxy.io/
Source0:        %{name}-%{version}.tar.xz
Source1:        envoy-proxy-WORKSPACE
Source2:        envoy-proxy-api-repositories.bzl
Source3:        envoy-proxy-repositories.bzl
Source4:        envoy-proxy-target_recipes.bzl
Source5:        envoy-proxy-BUILD
Source6:        java_grpc_library.bzl
Patch0:         0001-Remove-deprecated-Blaze-PACKAGE_NAME-macro-5330.patch
Patch1:         0001-Upgrade-gabime-spdlog-dependency-to-1.3.0-5604.patch
Patch2:         0001-bazel-transport-sockets-Update-grpc-to-1.19.1.patch
BuildRequires:  abseil-cpp-devel
BuildRequires:  backward-cpp-devel
BuildRequires:  bazel
BuildRequires:  bazel-gazelle-source
BuildRequires:  bazel-rules-go-source
BuildRequires:  bazel-skylib-source
BuildRequires:  benchmark-devel
BuildRequires:  boringssl-devel
BuildRequires:  c-ares-devel
BuildRequires:  cmake
BuildRequires:  dd-opentracing-cpp-devel
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  gcovr
BuildRequires:  git
BuildRequires:  golang-org-x-tools
BuildRequires:  golang-packaging
BuildRequires:  googleapis-source
BuildRequires:  gperftools-devel
BuildRequires:  grpc-httpjson-transcoding-source
BuildRequires:  grpc-source
BuildRequires:  gtest
BuildRequires:  http-parser-devel
BuildRequires:  jwt_verify_lib-devel
BuildRequires:  libcircllhist-devel
BuildRequires:  libevent-devel
BuildRequires:  libnghttp2-devel
BuildRequires:  libprotobuf-mutator-devel
BuildRequires:  libtool
BuildRequires:  lightstep-tracer-cpp-source
BuildRequires:  lua51-luajit-devel
BuildRequires:  msgpack-devel
BuildRequires:  nanopb-source
BuildRequires:  opentracing-cpp-source
BuildRequires:  prometheus-client-model-source
BuildRequires:  protobuf-source
BuildRequires:  protoc-gen-go-source
BuildRequires:  protoc-gen-gogo-source
BuildRequires:  protoc-gen-validate-source
BuildRequires:  python
BuildRequires:  python2-Jinja2
BuildRequires:  python2-MarkupSafe
BuildRequires:  python2-six
BuildRequires:  python2-thrift
BuildRequires:  python2-twitter.common.finagle-thrift
BuildRequires:  python2-twitter.common.lang
BuildRequires:  python2-twitter.common.rpc
BuildRequires:  rapidjson-devel
BuildRequires:  spdlog-devel
BuildRequires:  tclap
BuildRequires:  xxhash-devel
BuildRequires:  yaml-cpp-devel
BuildRequires:  zlib-devel
BuildRequires:  golang(API) >= 1.10.4
BuildRequires:  pkgconfig(openssl)
ExcludeArch:    %ix86

%description
Envoy is an L7 proxy and communication bus designed for large modern service
oriented architectures.

%prep
# Prepare golang-org-x-tools sources.
mkdir golang-org-x-tools
cp -r /usr/share/go/1.11/contrib/src/golang.org/x/tools/* golang-org-x-tools
pushd golang-org-x-tools
patch -p1 < /usr/src/bazel-rules-go/third_party/org_golang_x_tools-gazelle.patch
patch -p1 < /usr/src/bazel-rules-go/third_party/org_golang_x_tools-extras.patch
touch WORKSPACE
popd

# Prepare a fake grpc-java repository. googleapis Bazel rules require
# grpc-java, but we don't build any Java modules.
mkdir grpc-java
cp %{SOURCE6} ./grpc-java

%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# Copy our custom Bazel rules.
cp %{SOURCE1} ./WORKSPACE
cp %{SOURCE2} ./api/bazel/repositories.bzl
cp %{SOURCE3} ./bazel/repositories.bzl
cp %{SOURCE4} ./bazel/target_recipes.bzl
cp %{SOURCE5} ./ci/prebuilt/BUILD

# To avoid conflicts with openssl development files, boringssl package in
# openSUSE installs headers to /usr/include/boringssl.
find . -type f -exec sed -i 's|openssl|boringssl|' "{}" +

# Bump the version of luajit.
sed -i 's|luajit-2.0|luajit-5_1-2.1|g' ./source/extensions/filters/common/lua/lua.h
# path_matched is a part of grpc_transcoding which we link dynamically.
sed -i '/path_matcher/d' ./source/extensions/filters/http/grpc_json_transcoder/BUILD

git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git init
git add .
# use fixed date for reproducible builds (boo#1047218):
GIT_AUTHOR_DATE=2000-01-01T01:01:01 GIT_COMMITTER_DATE=2000-01-01T01:01:01 \
git commit -m "Dummy commit just to satisfy bazel" &> /dev/null

%build
# TODO(mrostecki): Create a macro in bazel package.
bazel build \
    -c dbg \
    --color=no \
    %(for opt in %{optflags}; do echo -e "--copt=${opt} \c"; done) \
    --curses=no \
    --distdir=%{_sourcedir} \
    --genrule_strategy=standalone \
    --spawn_strategy=standalone \
    --strip=never \
    --verbose_failures \
    //source/exe:envoy
bazel shutdown

%install
# The binary name "envoy-static" is just defined in Envoy's buildsystem, but
# after applying our downstream patches libraries are linked dynamically.
install -D -m0755 bazel-bin/source/exe/envoy-static %{buildroot}%{_bindir}/envoy-proxy

%files
%license LICENSE
%doc README.md
%{_bindir}/envoy-proxy

%changelog
