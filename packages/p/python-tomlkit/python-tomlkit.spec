#
# spec file for package python-tomlkit
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
%bcond_without python2
Name:           python-tomlkit
Version:        0.7.0
Release:        0
Summary:        Style preserving TOML library
License:        MIT
URL:            https://github.com/sdispater/tomlkit
Source:         https://files.pythonhosted.org/packages/source/t/tomlkit/tomlkit-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 5.3.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing >= 3.6}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-enum34
BuildRequires:  python-functools32
%endif
%ifpython2
Requires:       python-enum34
Requires:       python-functools32
%endif
%if %{python_version_nodots} < 35
Requires:       python-typing >= 3.6
%endif
%python_subpackages

%description
Style preserving TOML library

%prep
%setup -q -n tomlkit-%{version}

%build
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/tomlkit
%{python_sitelib}/tomlkit-%{version}-py*.egg-info

%changelog
