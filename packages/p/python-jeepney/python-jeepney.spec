#
# spec file for package python-jeepney
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-jeepney
Version:        0.8.0
Release:        0
Summary:        Low-level, pure Python DBus protocol wrapper
License:        MIT
Group:          Development/Languages/Python
URL:            https://gitlab.com/takluyver/jeepney
Source:         https://files.pythonhosted.org/packages/source/j/jeepney/jeepney-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testpath}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This is a low-level, pure Python DBus protocol client. It has an I/O-free
core, and integration modules for different event loops.

%prep
%setup -q -n jeepney-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest jeepney/tests

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/jeepney
%{python_sitelib}/jeepney-%{version}*-info

%changelog
