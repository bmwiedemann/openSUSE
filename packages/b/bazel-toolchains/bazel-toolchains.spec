#
# spec file for package bazel-toolchains
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

Name:           bazel-toolchains
Version:        2.0.0
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
cp -r * %{buildroot}%{src_install_dir}

%fdupes %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog
