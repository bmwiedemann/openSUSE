#
# spec file for package python-tri.declarative
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
%define skip_python2 1
Name:           python-tri.declarative
Version:        5.3.0
Release:        0
Summary:        Python class decorators in the style of Django model classes
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/TriOptima/tri.declarative
Source:         https://github.com/TriOptima/tri.declarative/archive/%{version}.tar.gz#/tri.declarative-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 4.0}
BuildRequires:  %{python_module tri.struct >= 3.0.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-tri.struct >= 3.0.0
BuildArch:      noarch

%python_subpackages

%description
tri.declarative contains class decorators to define classes with
subclass semantics in the style of django Model classes.

%prep
%setup -q -n tri.declarative-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_namespace_missing_call_target - pytest5 incompatible usage
#   https://github.com/TriOptima/tri.declarative/issues/9
%pytest -k 'not test_namespace_missing_call_target'

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
