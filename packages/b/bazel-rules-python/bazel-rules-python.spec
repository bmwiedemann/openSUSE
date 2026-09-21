#
# spec file for package bazel-rules-python
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define src_install_dir %{_prefix}/src/%{name}
Name:           bazel-rules-python
Version:        2.3.3
Release:        0
Summary:        Python rules for Bazel
License:        Apache-2.0
URL:            https://github.com/bazel-contrib/rules_python
Source0:        https://github.com/bazel-contrib/rules_python/releases/download/%{version}/rules_python-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  fdupes

%description
Bazel rules for packaging and distributing software written in Python.

%package source
Summary:        Source code of bazel-rules-python
BuildArch:      noarch

%description source
Bazel rules for packaging and distributing software written in Python.

This package contains source code of bazel-rules-python.

%prep
%setup -q -n rules_python-%{version}

%build

%install
mkdir -p %{buildroot}%{src_install_dir}
tar -xzf %{SOURCE0} --strip-components=1 -C %{buildroot}%{src_install_dir}
%fdupes %{buildroot}%{src_install_dir}

%files source
%license LICENSE
%doc README.md
%{src_install_dir}

%changelog
