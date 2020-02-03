#
# spec file for package opencensus-cpp
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define src_install_dir /usr/src/%{name}

Name:           opencensus-cpp
Version:        0.4.0+git.20190924
Release:        0
Summary:        A stats collection and distributed tracing framework
License:        Apache-2.0
Url:            https://github.com/census-instrumentation/opencensus-cpp
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildArch:      noarch

%description
OpenCensus is a toolkit for collecting application performance and behavior
data. It currently includes an API for tracing and stats.

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

sed -i -e "s|#define OPENCENSUS_VERSION .*|#define OPENCENSUS_VERSION \"%{version}\"|" \
    opencensus/common/version.h

sed -i \
    -e "/load_civetweb/d" \
    -e "s|go_register_toolchains()|go_register_toolchains(\"host\")|g" \
    WORKSPACE

sed -i \
    -e "s|@com_github_jupp0r_prometheus_cpp//core|@com_github_jupp0r_prometheus_cpp//:core|" \
    -e "s|com_github_jupp0r_prometheus_cpp//pull|com_github_jupp0r_prometheus_cpp//:pull|" \
    opencensus/exporters/stats/prometheus/BUILD

%build

%install
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}
%fdupes %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog
