#
# spec file for package python-docopt
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-docopt
Version:        0.6.2
Release:        0
Summary:        Pythonic argument parser
License:        MIT
Group:          Development/Languages/Python
URL:            http://docopt.org
Source:         https://files.pythonhosted.org/packages/source/d/docopt/docopt-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
docopt creates command-line interfaces.

This way one does not need to write repeatable parser-code,
and instead can write only the help message.

%prep
%setup -q -n docopt-%{version}

# Fix wrong-script-interpreter
sed -i "s|#! %{_bindir}/env python||" examples/git/git.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE-MIT
%doc README.rst
%doc examples/
%{python_sitelib}/*

%changelog
