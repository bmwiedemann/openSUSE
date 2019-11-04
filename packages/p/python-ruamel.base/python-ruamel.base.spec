#
# spec file for package python-ruamel.base
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
Name:           python-ruamel.base
Version:        1.0.0+post1
Release:        0
Summary:        Shared ruamel routines
License:        MIT
URL:            https://bitbucket.org/ruamel/base
Source:         https://files.pythonhosted.org/packages/source/r/ruamel.base/ruamel.base-1.0.0.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This is a common package for the "ruamel" namespace.

%prep
%setup -q -n ruamel.base-1.0.0
rm -rf *.egg-info
# https://bitbucket.org/ruamel/base/issues/1
sed -i '/sys.exit/d' setup.py
# Use normal namespaces with a __init__.py, so it is easier to
# managed the ordereddict and yaml packages which also include .so files
sed -i '/namespace_packages=/d' setup.py

%build
%python_build

%install
export RUAMEL_NO_PIP_INSTALL_CHECK=1
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/ruamel
%{python_sitelib}/ruamel.base-1.0.0-py%{python_version}.egg-info

%changelog
