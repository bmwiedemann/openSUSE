#
# spec file for package python-jaraco.context
#
# Copyright (c) 2022 SUSE LLC
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
%define skip_python2 1
Name:           python-jaraco.context
Version:        4.1.1
Release:        0
Summary:        Tools to work with functools
License:        MIT
URL:            https://github.com/jaraco/jaraco.context
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco.context/jaraco.context-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module toml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
jaraco.functools Tools for working with functools.
Additional functools in the spirit of stdlib’s functools.

%prep
%setup -q -n jaraco.context-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc docs/*.rst README.rst CHANGES.rst
%{python_sitelib}/jaraco.context-%{version}*-info
%dir %{python_sitelib}/jaraco
%{python_sitelib}/jaraco/context.py*
%dir %{python_sitelib}/jaraco/__pycache__
%pycache_only %{python_sitelib}/jaraco/__pycache__/context*.py*

%changelog
