#
# spec file for package python-pilkit
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
%bcond_without test
Name:           python-pilkit
Version:        2.0
Release:        0
Summary:        A collection of utilities and processors for the Python Imaging Libary
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://github.com/matthewwithanm/pilkit/
Source:         https://files.pythonhosted.org/packages/source/p/pilkit/pilkit-%{version}.tar.gz
Patch0:         pil-fix-test.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module mock >= 1.0.1}
BuildRequires:  %{python_module nose >= 1.3.6}
BuildRequires:  %{python_module nose-progressive >= 1.5.1}
%endif
# /SECTION
%python_subpackages

%description
PILKit is a collection of utilities for working with PIL (the Python Imaging
Library).

One of its main features is a set of **processors** which expose a simple
interface for performing manipulations on PIL images.

%prep
%setup -q -n pilkit-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%license LICENSE
%doc AUTHORS README.rst
%{python_sitelib}/*

%changelog
