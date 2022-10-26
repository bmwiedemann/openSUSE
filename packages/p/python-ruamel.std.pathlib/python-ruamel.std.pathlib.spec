#
# spec file for package python-ruamel.std.pathlib
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


Name:           python-ruamel.std.pathlib
Version:        0.9.2
Release:        0
Summary:        Improvements over the standard pathlib module and pathlib2 package
License:        MIT
Group:          Development/Languages/Python
URL:            https://sourceforge.net/projects/ruamel-std-pathlib/
Source:         https://files.pythonhosted.org/packages/source/r/ruamel.std.pathlib/ruamel.std.pathlib-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ruamel.base >= 1.0.0+post1
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
%{python_expand touch %{buildroot}%{$python_sitelib}/ruamel/std/__init__.py
%fdupes %{buildroot}%{$python_sitelib}
}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
