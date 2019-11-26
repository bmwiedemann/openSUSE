#
# spec file for package opencensus-cpp
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define sover 0
%define libname lib%{name}%{sover}
%define src_install_dir /usr/src/%{name}

Name:           opencensus-cpp
Version:        0.4.0
Release:        0
Summary:        A stats collection and distributed tracing framework
License:        Apache-2.0
Url:            https://github.com/census-instrumentation/opencensus-cpp
Source:         %{name}-%{version}.tar.xz
Patch0:         0001-bazel-Remove-and-add-deps-in-WORKSPACE.patch
Patch1:         0002-Stackdriver-stats-Return-false-in-matcher-when-type-.patch
BuildRequires:  abseil-cpp-source
BuildRequires:  bazel-apple-support-source
BuildRequires:  bazel-rules-apple-source
BuildRequires:  bazel-rules-cc-source
BuildRequires:  bazel-rules-go-source
BuildRequires:  bazel-rules-java-source
BuildRequires:  bazel-rules-proto-source
BuildRequires:  bazel-skylib-source
BuildRequires:  bazel-workspaces
BuildRequires:  bazel0.29
BuildRequires:  benchmark-devel
BuildRequires:  c-ares-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  golang(API) >= 1.10.4
BuildRequires:  googleapis-source
BuildRequires:  grpc-source
BuildRequires:  gmock
BuildRequires:  gtest
BuildRequires:  libcurl-devel
BuildRequires:  nanopb-source
BuildRequires:  patchelf
BuildRequires:  prometheus-cpp-devel
BuildRequires:  protobuf-source
BuildRequires:  rapidjson-devel
BuildRequires:  upb-source
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(openssl)
ExcludeArch:    %ix86

%description
OpenCensus is a toolkit for collecting application performance and behavior
data. It currently includes an API for tracing and stats.

%package -n %{libname}
Summary:        Shared libraries for opencensus-cpp

%description -n %{libname}
OpenCensus is a toolkit for collecting application performance and behavior
data. It currently includes an API for tracing and stats.

This package provides shared libraries for opencensus-cpp.

%package devel
Summary:        Development files for opencensus-cpp
Requires:       %{libname} = %{version}

%description devel
OpenCensus is a toolkit for collecting application performance and behavior
data. It currently includes an API for tracing and stats.

This package provides development files for opencensus-cpp.

%package source
Summary:        Source code of opencensus-cpp

%description source
OpenCensus is a toolkit for collecting application performance and behavior
data. It currently includes an API for tracing and stats.

This package provides source code of opencensus-cpp.

%prep
%autosetup -p1
cat <<EOF >> WORKSPACE
OPENSSL_BUILD_CONTENT = """
cc_library(
    name = "openssl-lib",
    hdrs = glob([
        "thirdparty_build/include/openssl",
        "thirdparty_build/include/ssl",
    ]),
    copts = [
        "-I/usr/include/openssl",
        "-I/usr/include/ssl",
    ],
    linkopts = ["-lssl", "-lcrypto"],
    visibility = ["//visibility:public"],
    linkstatic = False,
)
"""

new_local_repository(
    name = "openssl",
    path = "%{_libdir}",
    build_file_content = OPENSSL_BUILD_CONTENT,
)
EOF

sed -i \
    -e "s|@com_github_jupp0r_prometheus_cpp//core|@com_github_jupp0r_prometheus_cpp//:core|" \
    -e "s|com_github_jupp0r_prometheus_cpp//pull|com_github_jupp0r_prometheus_cpp//:pull|" \
    opencensus/exporters/stats/prometheus/BUILD
find examples/ -type f -name BUILD -exec rm -f {} +

%build
cat /usr/src/grpc/WORKSPACE
TARGETS=$(bazel query \
    --override_repository="bazel_skylib=/usr/src/bazel-skylib" \
    --override_repository="com_github_cares_cares=%{_datadir}/bazel-workspaces/c-ares" \
    --override_repository="com_github_curl=%{_datadir}/bazel-workspaces/curl" \
    --override_repository="com_github_google_benchmark=%{_datadir}/bazel-workspaces/benchmark" \
    --override_repository="com_github_grpc_grpc=/usr/src/grpc" \
    --override_repository="com_github_jupp0r_prometheus_cpp=%{_datadir}/bazel-workspaces/prometheus-cpp" \
    --override_repository="com_github_nanopb_nanopb=/usr/src/nanopb" \
    --override_repository="com_github_tencent_rapidjson=%{_datadir}/bazel-workspaces/rapidjson" \
    --override_repository="com_google_absl=/usr/src/abseil-cpp" \
    --override_repository="com_google_googleapis=/usr/src/googleapis" \
    --override_repository="com_google_googletest=%{_datadir}/bazel-workspaces/googletest" \
    --override_repository="com_google_protobuf=/usr/src/protobuf" \
    --override_repository="io_bazel_rules_go=/usr/src/bazel-rules-go" \
    --override_repository="rules_cc=/usr/src/bazel-rules-cc" \
    --override_repository="rules_go=/usr/src/bazel-rules-go" \
    --override_repository="rules_java=/usr/src/bazel-rules-java" \
    --override_repository="upb=/usr/src/upb" \
    --override_repository="zlib=%{_datadir}/bazel-workspaces/zlib" \
    '//... except kind(.*test, //...)')
bazel build \
    -c dbg \
    --color=no \
    --copt=-Wno-error \
    --curses=no \
    --host_javabase=@local_jdk//:jdk \
    --incompatible_use_jdk11_as_host_javabase \
    --override_repository="bazel_skylib=/usr/src/bazel-skylib" \
    --override_repository="com_github_cares_cares=%{_datadir}/bazel-workspaces/c-ares" \
    --override_repository="com_github_curl=%{_datadir}/bazel-workspaces/curl" \
    --override_repository="com_github_google_benchmark=%{_datadir}/bazel-workspaces/benchmark" \
    --override_repository="com_github_grpc_grpc=/usr/src/grpc" \
    --override_repository="com_github_jupp0r_prometheus_cpp=%{_datadir}/bazel-workspaces/prometheus-cpp" \
    --override_repository="com_github_nanopb_nanopb=/usr/src/nanopb" \
    --override_repository="com_github_tencent_rapidjson=%{_datadir}/bazel-workspaces/rapidjson" \
    --override_repository="com_google_absl=/usr/src/abseil-cpp" \
    --override_repository="com_google_googleapis=/usr/src/googleapis" \
    --override_repository="com_google_googletest=%{_datadir}/bazel-workspaces/googletest" \
    --override_repository="com_google_protobuf=/usr/src/protobuf" \
    --override_repository="io_bazel_rules_go=/usr/src/bazel-rules-go" \
    --override_repository="rules_cc=/usr/src/bazel-rules-cc" \
    --override_repository="rules_go=/usr/src/bazel-rules-go" \
    --override_repository="rules_java=/usr/src/bazel-rules-java" \
    --override_repository="upb=/usr/src/upb" \
    --override_repository="zlib=%{_datadir}/bazel-workspaces/zlib" \
    --strip=never \
    --verbose_failures \
    ${TARGETS}
bazel shutdown

%install
for lib in $(find bazel-bin/opencensus -name "*.so"); do
    lib_basename=$(basename ${lib} | sed -e "s|^lib|libopencensus-cpp-|")
    install -D -m0755 ${lib} %{buildroot}%{_libdir}/${lib_basename}.%{sover}
    patchelf --set-soname ${lib_basename}.%{sover} %{buildroot}%{_libdir}/${lib_basename}.%{sover}
    ln -sf ${lib_basename}.%{sover} %{buildroot}%{_libdir}/${lib_basename}
done
for header in $(find opencensus -name "*.h"); do
    install -D -m0644 ${header} %{buildroot}%{_includedir}/${header}
done

ls
rm -rf bazel-bin
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}
%fdupes %{buildroot}%{src_install_dir}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}*.so.%{sover}

%files devel
%{_includedir}/opencensus
%{_libdir}/lib%{name}*.so

%files source
%{src_install_dir}

%changelog

