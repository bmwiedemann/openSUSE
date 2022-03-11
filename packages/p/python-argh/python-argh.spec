#
# spec file for package python-argh
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-argh
Version:        0.26.2
Release:        0
Summary:        An argparse wrapper
License:        LGPL-3.0-or-later
URL:            https://github.com/neithere/argh/
Source:         https://files.pythonhosted.org/packages/source/a/argh/argh-%{version}.tar.gz
Patch0:         support-py39.patch
# https://github.com/neithere/argh/issues/152
Patch1:         python-argh-no_mock.patch
BuildRequires:  %{python_module iocapture}
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
%setup -q -n argh-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%{python_sitelib}/argh/
%{python_sitelib}/argh-%{version}-py*.egg-info

%changelog
