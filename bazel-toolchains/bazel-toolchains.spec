#
# spec file for package bazel-toolchains
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


%define src_install_dir /usr/src/%{name}

Name:           bazel-toolchains
Version:        20190102
Release:        0
Summary:        Set of Bazel toolchain configurations
License:        Apache-2.0
Group:          Development/Tools/Building
Url:            https://github.com/bazelbuild/bazel-toolchains
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes

%description
bazel-toolchains is a repository of commonly used Bazel toolchain configuration
files. They are required to configure Bazel to work inside a Docker container
via a remote execution environment.

%package source
Summary:        Source code of bazel-toolchains
Group:          Development/Sources
BuildArch:      noarch

%description source
bazel-toolchains is a repository of commonly used Bazel toolchain configuration
files. They are required to configure Bazel to work inside a Docker container
via a remote execution environment.

This package contains source code of bazel-toolchains.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{src_install_dir}
tar -xJf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}
# Fix env-script-interpreter error.
find %{buildroot}%{src_install_dir} -type f -name "*.py" -exec sed -i 's|#!/usr/bin/env python|#!/usr/bin/python|' "{}" +
# Yes, almost all BUILD and some .bzl files for clang and java have executable bits...
find %{buildroot}%{src_install_dir} \( -name "BUILD" -o -name "CROSSTOOL" -o -name "*.bzl" \) \( -path "*clang*" -o -path "*java*" \) -exec chmod -x "{}" +
# And one Pythos script with sheband does not have executable bit...
chmod +x %{buildroot}%{src_install_dir}/container/build.py
# Remove hidden files and directories
find %{buildroot}%{src_install_dir} -name ".*" -exec rm -rf "{}" +

%fdupes %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog

