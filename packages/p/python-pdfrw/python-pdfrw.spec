#
# spec file for package python-pdfrw
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


# Tests require external files
%bcond_with     test
%{?sle15_python_module_pythons}
Name:           python-pdfrw
Version:        0.4
Release:        0
Summary:        PDF file reader/writer library
License:        MIT
Group:          Development/Libraries/Python
URL:            https://code.google.com/p/pdfrw/
Source:         https://files.pythonhosted.org/packages/source/p/pdfrw/pdfrw-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
pdfrw is a Python library and utility that reads and writes PDF files.

%prep
%setup -q -n pdfrw-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%pytest
%endif

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/pdfrw/
%{python_sitelib}/pdfrw-%{version}*-info

%changelog
