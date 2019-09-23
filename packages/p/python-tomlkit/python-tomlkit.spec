#
# spec file for package python-tomlkit
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-tomlkit
Version:        0.5.3
Release:        0
Summary:        Style preserving TOML library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/sdispater/tomlkit
Source:         https://files.pythonhosted.org/packages/source/t/tomlkit/tomlkit-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing >= 3.6}
BuildRequires:  fdupes
BuildRequires:  python-enum34
BuildRequires:  python-functools32
BuildRequires:  python-rpm-macros
BuildArch:      noarch
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
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
