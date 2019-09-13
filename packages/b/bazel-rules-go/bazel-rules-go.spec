#
# spec file for package bazel-rules-go
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


%define src_install_dir /usr/src/%{name}

Name:           bazel-rules-go
Version:        0.16.5
Release:        0
Summary:        Go rules for Bazel
License:        Apache-2.0
Group:          Development/Tools/Building
Url:            https://github.com/bazelbuild/rules_go
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes

%description
Bazel rules which support building software written in Go, specifically:
- building libraries
- building binaries
- executing tests
- vendoring
- cgo builds
- cross compilation
- auto generating Bazel BUILD files
- build-time code analysis via nogo

%package source
Summary:        Source code of bazel-rules-go
Group:          Development/Sources
BuildArch:      noarch

%description source
Bazel rules which support building software written in Go, specifically:
- building libraries
- building binaries
- executing tests
- vendoring
- cgo builds
- cross compilation
- auto generating Bazel BUILD files
- build-time code analysis via nogo

This package contains source code of bazel-rules-go.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{src_install_dir}
tar -xJf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}
# Fix hidden-dile-or-dir warning.
find %{buildroot}%{src_install_dir} -name ".*" -exec rm -rf "{}" +
# Fix env-script-interpreter error.
find %{buildroot}%{src_install_dir} -type f -name "*.py" -exec sed -i 's|#!/usr/bin/env python|#!/usr/bin/python|' "{}" +

%fdupes %{buildroot}%{src_install_dir}

%files source
%license LICENSE.txt
%doc README.rst
%{src_install_dir}

%changelog
