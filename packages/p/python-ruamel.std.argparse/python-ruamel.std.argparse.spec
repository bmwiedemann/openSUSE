#
# spec file for package python-ruamel.std.argparse
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-ruamel.std.argparse
Version:        0.8.3
Release:        0
Summary:        Enhancements to argparse
License:        MIT
Group:          Development/Languages/Python
URL:            https://sourceforge.net/p/ruamel-std-argparse
Source:         https://files.pythonhosted.org/packages/source/r/ruamel.std.argparse/ruamel.std.argparse-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ruamel.base
%ifpython2
Requires:       python2-ruamel.std.pathlib
%endif
BuildArch:      noarch

%python_subpackages

%description
Enhancements to argparse providing extra actions, subparser aliases,
smart formatter, and a decorator based wrapper.

%prep
%setup -q -n ruamel.std.argparse-%{version}

%build
%python_build

%install
export RUAMEL_NO_PIP_INSTALL_CHECK=1
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
