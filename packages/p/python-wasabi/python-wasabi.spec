#
# spec file for package python-wasabi
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
%define modname wasabi
Name:           python-wasabi
Version:        1.1.3
Release:        0
Summary:        A lightweight console printing and formatting toolkit
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/explosion/wasabi
Source:         https://github.com/explosion/%{modname}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A lightweight console printing and formatting toolkit.

%prep
%autosetup -n %{modname}-%{version} -p1

%build
%pyproject_wheel

%install
%pyproject_install

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/wasabi
%{python_sitelib}/wasabi-%{version}*-info

%changelog
