#
# spec file for package python-hammett
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
Name:           python-hammett
Version:        0.5.0
Release:        0
Summary:        hammett is a fast python test runner
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/boxed/hammett
Source0:        https://files.pythonhosted.org/packages/source/h/hammett/hammett-%{version}.tar.gz
Source1:        tests.tar.bz2
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-astunparse
Requires:       python-colorama
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module astunparse}
BuildRequires:  %{python_module colorama}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
hammett is a fast python test runner

%prep
%setup -q -n hammett-%{version} -a1

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
