#
# spec file for package python-jaraco.itertools
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
Name:           python-jaraco.itertools
Version:        6.4.1
Release:        0
Summary:        Tools to work with iterables
License:        MIT
URL:            https://github.com/jaraco/jaraco.itertools
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco.itertools/jaraco.itertools-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module inflect}
BuildRequires:  %{python_module more-itertools >= 4.0.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 56}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-inflect
Requires:       python-more-itertools >= 4.0.0
BuildArch:      noarch
%python_subpackages

%description
jaraco.itertools Tools for working with iterables.
Complements itertools and more_itertools.

%prep
%setup -q -n jaraco.itertools-%{version}
rm -r jaraco.itertools.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest --doctest-modules

%files %{python_files}
%license LICENSE
%doc docs/*.rst README.rst NEWS.rst
%dir %{python_sitelib}/jaraco
%{python_sitelib}/jaraco[_.]itertools-%{version}.dist-info
%{python_sitelib}/jaraco/itertools.py*
%pycache_only %dir %{python_sitelib}/jaraco/__pycache__
%pycache_only %{python_sitelib}/jaraco/__pycache__/itertools*.py*

%changelog
