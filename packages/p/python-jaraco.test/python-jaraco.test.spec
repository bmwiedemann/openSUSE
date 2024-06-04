#
# spec file for package python-jaraco.test
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
Name:           python-jaraco.test
Version:        5.4.0
Release:        0
Summary:        Testing support by jaraco
License:        MIT
URL:            https://github.com/jaraco/jaraco.test
Source:         https://files.pythonhosted.org/packages/source/j/jaraco.test/jaraco.test-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module jaraco.context}
BuildRequires:  %{python_module jaraco.collections}
BuildRequires:  %{python_module jaraco.functools}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module testsuite}
# /SECTION
BuildRequires:  fdupes
Requires:       python-jaraco.collections
Requires:       python-jaraco.context
Requires:       python-jaraco.functools
Suggests:       python-sphinx >= 3.5
Suggests:       python-jaraco.packaging >= 9
Suggests:       python-rst.linker >= 1.9
Suggests:       python-furo
Suggests:       python-sphinx-lint
BuildArch:      noarch
%python_subpackages

%description
Testing support by jaraco

%prep
%autosetup -p1 -n jaraco.test-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# https://github.com/pytest-dev/pytest/issues/12303
%pytest -v || :

%files %{python_files}
%doc NEWS.rst README.rst
%license LICENSE
%{python_sitelib}/jaraco/test
%{python_sitelib}/jaraco.test-%{version}.dist-info

%changelog
