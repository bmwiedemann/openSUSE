#
# spec file for package python-calmjs.parse
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-calmjs.parse
Version:        1.3.3
Release:        0
Summary:        Various parsers for ECMA standards
License:        MIT
URL:            https://github.com/calmjs/calmjs.parse
Source:         https://github.com/calmjs/calmjs.parse/archive/%{version}.tar.gz
BuildRequires:  %{python_module ply >= 3.6}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ply >= 3.6
Requires:       python-setuptools
BuildArch:      noarch
%python_subpackages

%description
A collection of parsers and helper libraries for understanding
ECMAScript; a near feature complete fork of slimit.

%prep
%setup -q -n calmjs.parse-%{version}

%build
export LANG=en_US.UTF-8
%python_build
%python_expand PYTHONPATH=build/lib $python -m calmjs.parse.parsers.optimize

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pyunittest -v calmjs.parse.tests.make_suite

%files %{python_files}
%doc README.rst CHANGES.rst
%license LICENSE
%{python_sitelib}/calmjs*

%changelog
