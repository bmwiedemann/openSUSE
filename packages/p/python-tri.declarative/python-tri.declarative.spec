#
# spec file for package python-tri.declarative
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
%define skip_python2 1
Name:           python-tri.declarative
Version:        3.1.0
Release:        0
License:        BSD-3-Clause
Summary:        Python class decorators in the style of Django model classes
Url:            https://github.com/TriOptima/tri.declarative
Group:          Development/Languages/Python
Source:         https://github.com/TriOptima/tri.declarative/archive/%{version}.tar.gz#/tri.declarative-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
# Tests are incomptaible with pytest 5
# https://github.com/TriOptima/tri.declarative/issues/9
BuildRequires:  %{python_module pytest < 5}
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
%pytest

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
