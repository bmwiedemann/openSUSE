#
# spec file for package python-argh
#
# Copyright (c) 2024 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-argh
Version:        0.31.2
Release:        0
Summary:        An argparse wrapper
License:        LGPL-3.0-or-later
URL:            https://github.com/neithere/argh/
Source:         https://files.pythonhosted.org/packages/source/a/argh/argh-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This Python module provides a wrapper for argparse with support for hierarchical
commands that can be bound to modules or classes.

Features that argh adds to argparse:

* mark a function as a CLI command and specify its arguments before the parser
  is instantiated;
* nested commands made easy: no messing with subparsers (though they are of
  course used under the hood);
* infer agrument type from the default value;
* infer command name from function name;
* add an alias root command help for the --help argument;
* enable passing unwrapped arguments to certain functions instead of a
  argparse.Namespace object.

Argh is fully compatible with argparse. argh-agnostic and argh-aware code
can be mixed. Keep in mind that argh.dispatch does some extra
work that a custom dispatcher may not do.

%prep
%autosetup -p1 -n argh-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# do not run test_integration, which requires dropped iocapture
rm tests/test_integration.py
%pytest -v

%files %{python_files}
%doc README.rst
%{python_sitelib}/argh/
%{python_sitelib}/argh-%{version}.dist-info

%changelog
