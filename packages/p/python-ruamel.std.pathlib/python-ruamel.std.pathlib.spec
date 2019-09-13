#
# spec file for package python-ruamel.std.pathlib
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-ruamel.std.pathlib
Version:        0.6.4
Release:        0
License:        MIT
Summary:        Improvements over the standard pathlib module and pathlib2 package
Url:            https://bitbucket.org/ruamel/std.pathlib
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/r/ruamel.std.pathlib/ruamel.std.pathlib-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-ruamel.base >= 1.0.0+post1
%ifpython2
Requires:       python-pathlib2
%endif
BuildArch:      noarch

%python_subpackages

%description
Improvements over the standard pathlib module and pathlib2 package.

%prep
%setup -q -n ruamel.std.pathlib-%{version}
sed -i '/keywords=/d' setup.py

%build
%python_build

%install
export RUAMEL_NO_PIP_INSTALL_CHECK=1
%python_install
# This makes this package the owner of the Python 2 namespace ruamel.std
touch %{buildroot}%{python2_sitelib}/ruamel/std/__init__.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
