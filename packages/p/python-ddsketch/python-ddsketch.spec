#
# spec file for package python-ddsketch
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

%{?sle15_python_module_pythons}
Name:           python-ddsketch
Version:        3.0.1
Release:        0
Summary:        Distributed quantile sketches
License:        Apache-2.0
URL:            http://github.com/datadog/sketches-py
Source:         https://files.pythonhosted.org/packages/source/d/ddsketch/ddsketch-%{version}.tar.gz
Patch1:         python-ddsketch-no-six.patch 
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module protobuf}
BuildRequires:  %{python_module numpy}
BuildRequires:  fdupes
Suggests:       python-protobuf >= 3.0.0
BuildArch:      noarch
%python_subpackages

%description
Distributed quantile sketches

%prep
%autosetup -p1 -n ddsketch-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE LICENSE-3rdparty.csv
%{python_sitelib}/ddsketch
%{python_sitelib}/ddsketch-%{version}.dist-info

%changelog
