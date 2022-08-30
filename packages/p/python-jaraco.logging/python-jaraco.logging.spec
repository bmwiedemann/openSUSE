#
# spec file for package python-jaraco.logging
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


Name:           python-jaraco.logging
Version:        3.1.2
Release:        0
Summary:        Tools to work with logging
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jaraco/jaraco.logging
Source0:        https://files.pythonhosted.org/packages/source/j/jaraco.logging/jaraco.logging-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 56}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tempora}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-tempora
BuildArch:      noarch
%python_subpackages

%description
jaraco.logging Tools for working with logging.

%prep
%setup -q -n jaraco.logging-%{version}
rm -rf jaraco.logging.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
#  work around for gh#pytest-dev/pytest#3396 until gh#pytest-dev/pytest#10088 lands in a pytest release
touch jaraco/__init__.py
cp -r %{python3_sitelib}/jaraco/* jaraco/
%pytest --doctest-modules

%files %{python_files}
%license LICENSE
%doc docs/*.rst README.rst CHANGES.rst
%{python_sitelib}/jaraco.logging-%{version}*-info
%{python_sitelib}/jaraco/logging.py*
%dir %{python_sitelib}/jaraco
%pycache_only %dir %{python_sitelib}/jaraco/__pycache__
%pycache_only %{python_sitelib}/jaraco/__pycache__/logging*.py*

%changelog
