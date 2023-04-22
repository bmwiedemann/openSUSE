#
# spec file for package python-cppy
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
Name:           python-cppy
Version:        1.2.1
Release:        0
Summary:        C++ headers for C extension development
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/nucleic/cppy
Source:         https://files.pythonhosted.org/packages/source/c/cppy/cppy-%{version}.tar.gz
Source99:       python-cppy-rpmlintrc
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 61.2}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module tomli}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
C++ headers for C extension development

%prep
%setup -q -n cppy-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/cppy
%{python_sitelib}/cppy-%{version}*-info

%changelog
