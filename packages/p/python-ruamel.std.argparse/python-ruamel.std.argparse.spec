#
# spec file for package python-ruamel.std.argparse
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
Name:           python-ruamel.std.argparse
Version:        0.8.1
Release:        0
License:        MIT
Summary:        Enhancements to argparse
Url:            https://bitbucket.org/ruamel/std.argparse
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/r/ruamel.std.argparse/ruamel.std.argparse-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
%ifpython3
Requires:       python-ruamel.base
%endif
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
