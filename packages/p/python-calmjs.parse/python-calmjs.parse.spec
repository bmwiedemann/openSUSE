#
# spec file for package python-calmjs.parse
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-calmjs.parse
Version:        1.2.1
Release:        0
Summary:        Various parsers for ECMA standards
License:        MIT
URL:            https://github.com/calmjs/calmjs.parse
Source:         https://github.com/calmjs/calmjs.parse/archive/%{version}.tar.gz
BuildRequires:  %{python_module ply >= 3.6}
BuildRequires:  %{python_module pytest}
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
%python_build

%install
%python_install
%python_expand rm -r %{buildroot}%{$python_sitelib}/calmjs/parse/testing
%python_expand rm -r %{buildroot}%{$python_sitelib}/calmjs/parse/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst CHANGES.rst
%license LICENSE
%{python_sitelib}/*

%changelog
