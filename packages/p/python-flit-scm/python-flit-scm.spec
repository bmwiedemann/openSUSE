#
# spec file for package python-flit-scm
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
Name:           python-flit-scm
Version:        1.7.0
Release:        0
Summary:        PEP 518 build backend using setuptools_scm and flit
License:        MIT
URL:            https://gitlab.com/WillDaSilva/flit_scm
Source:         https://files.pythonhosted.org/packages/source/f/flit_scm/flit_scm-%{version}.tar.gz
BuildRequires:  %{python_module flit-core >= 3.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm >= 6.4}
BuildRequires:  %{python_module tomli if %python-version < 3.11}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-flit-core >= 3.5
Requires:       python-setuptools_scm >= 6.4
Provides:       python-flit-scm = %{version}-%{release}
BuildArch:      noarch
%if 0%{python_version_nodots} < 311
Requires:       python-tomli
%endif
%python_subpackages

%description
A PEP 518 build backend that uses setuptools_scm to generate a version file
from your version control system, then flit to build the package.

%prep
%setup -q -n flit_scm-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
# there are no tests

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/flit_scm
%{python_sitelib}/flit_scm-%{version}*-info

%changelog
