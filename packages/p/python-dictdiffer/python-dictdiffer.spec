#
# spec file for package python-dictdiffer
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-dictdiffer
Version:        0.8.1
Release:        0
Summary:        Dictdiffer is a library that helps you to diff and patch dictionaries
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/inveniosoftware/dictdiffer
Source:         https://files.pythonhosted.org/packages/source/d/dictdiffer/dictdiffer-%{version}.tar.gz
Patch0:         lower-reqs.diff
BuildRequires:  %{python_module pytest-runner >= 2.7}
BuildRequires:  %{python_module setuptools_scm >= 1.15.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-numpy >= 1.11.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mock >= 1.3.0}
BuildRequires:  %{python_module pytest >= 2.8.0}
# /SECTION
%python_subpackages

%description
Dictdiffer is a library that helps you to diff and patch dictionaries.

%prep
%setup -q -n dictdiffer-%{version}
%patch0 -p1
# Remove dependence on unnecessary pytest plugins
rm pytest.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS CHANGES README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
