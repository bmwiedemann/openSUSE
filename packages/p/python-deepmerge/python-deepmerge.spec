#
# spec file for package python-deepmerge
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-deepmerge
Version:        1.1.0
Release:        0
License:        MIT
Summary:        A toolset to deeply merge python dictionaries
URL:            https://github.com/toumorokoshi/deepmerge
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/d/deepmerge/deepmerge-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm > 5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module vcver}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
Python module to deeply merge python dictionaries.

%prep
%setup -q -n deepmerge-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/deepmerge
%{python_sitelib}/deepmerge-%{version}.dist-info/

%changelog
