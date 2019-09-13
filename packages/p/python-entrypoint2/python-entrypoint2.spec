#
# spec file for package python-entrypoint2
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-entrypoint2
Version:        0.0.6
Release:        0
Summary:        Command-line interface for python modules
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ponty/entrypoint2
Source:         https://files.pythonhosted.org/packages/source/e/entrypoint2/entrypoint2-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-decorator
BuildArch:      noarch
%python_subpackages

%description
entrypoint2 is a command-line interface for python modules, forked
off entrypoint.

%prep
%setup -q -n entrypoint2-%{version}
# argparse is py2.6 or older
sed -i -e '/argparse/d' requirements.txt

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
