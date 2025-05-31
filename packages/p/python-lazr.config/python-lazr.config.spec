#
# spec file for package python-lazr.config
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
Name:           python-lazr.config
Version:        3.0
Release:        0
Summary:        Create configuration schemas, and process and validate configurations
License:        LGPL-3.0-only
URL:            https://launchpad.net/lazr.config
Source:         https://files.pythonhosted.org/packages/source/l/lazr.config/lazr.config-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lazr.delegates
Requires:       python-zope.interface
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module lazr.delegates}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module zope.interface}
# /SECTION
%python_subpackages

%description
Create configuration schemas, and process and validate configurations.

%prep
%setup -q -n lazr.config-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# use pytest, reported to lazr-users@lists.launchpad.net on 2020-06-03
cat << EOF > pytest.ini
[pytest]
doctest_optionflags = ELLIPSIS NORMALIZE_WHITESPACE
EOF
# test_not_stackable fails otherwise (with nose it did not run at all)
# needs to be investigated more
export PYTEST_ADDOPTS="--doctest-glob='*.rst' --import-mode=importlib"
%pytest

%files %{python_files}
%doc README.rst
%license COPYING.txt
%dir %{python_sitelib}/lazr
%{python_sitelib}/lazr/config
%{python_sitelib}/lazr[._]config-%{version}*-info
%{python_sitelib}/lazr[._]config-%{version}*-nspkg.pth

%changelog
