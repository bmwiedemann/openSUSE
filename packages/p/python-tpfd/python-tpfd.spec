#
# spec file for package python-tpfd
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
Name:           python-tpfd
Version:        0.2.4
Release:        0
Summary:        Text Parsing Function Dispatcher
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/erinxocon/tpfd
Source:         https://github.com/erinxocon/tpfd/archive/v%{version}.tar.gz#/tpfd-%{version}.tar.gz
Patch0:         drop-test-data-installation.patch
BuildRequires:  %{python_module parse}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-parse
BuildArch:      noarch
%python_subpackages

%description
TPFD (Text Parsing Function Dispatcher) is an easy way to parse strings and execute
functions depending on their contents.

Inspired by Flask and using Parse under the hood, TPFD allows you to decorate functions
with grammar rules and if a pattern that matches one of your grammar rules is found,
the function will be run with a set of keyword arguments you've specified passed to it!
Great for parsing logs and executing macros on what it finds!

%prep
%setup -q -n tpfd-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
cd test
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python test_parse.py
}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
