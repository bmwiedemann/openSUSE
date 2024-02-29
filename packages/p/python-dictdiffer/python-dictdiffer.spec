#
# spec file for package python-dictdiffer
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


Name:           python-dictdiffer
Version:        0.9.0
Release:        0
Summary:        Dictdiffer is a library that helps you to diff and patch dictionaries
License:        MIT
URL:            https://github.com/inveniosoftware/dictdiffer
Source:         https://files.pythonhosted.org/packages/source/d/dictdiffer/dictdiffer-%{version}.tar.gz
Patch0:         lower-reqs.diff
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm >= 1.15.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-numpy >= 1.11.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 2.8.0}
# /SECTION
%python_subpackages

%description
Dictdiffer is a library that helps you to diff and patch dictionaries.

%prep
%autosetup -p1 -n dictdiffer-%{version}
# Remove dependence on unnecessary pytest plugins
rm pytest.ini
# https://github.com/inveniosoftware/dictdiffer/issues/167
sed -i '/pytest-runner/d' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS CHANGES README.rst
%license LICENSE
%{python_sitelib}/dictdiffer
%{python_sitelib}/dictdiffer-%{version}.dist-info

%changelog
