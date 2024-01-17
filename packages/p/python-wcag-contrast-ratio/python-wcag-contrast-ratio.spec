#
# spec file for package python-wcag-contrast-ratio
#
# Copyright (c) 2023 SUSE LLC
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
%{?sle15_python_module_pythons}
Name:           python-wcag-contrast-ratio
Version:        0.9
Release:        0
Summary:        A library for computing contrast ratios, as required by WCAG 20
License:        MIT
URL:            https://github.com/gsnedders/wcag-contrast-ratio
Source:         https://files.pythonhosted.org/packages/source/w/wcag-contrast-ratio/wcag-contrast-ratio-%{version}.tar.gz
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A library for computing contrast ratios, as required by WCAG 2.0

%prep
%setup -q -n wcag-contrast-ratio-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest test.py

%files %{python_files}
%doc README.rst
%{python_sitelib}/*

%changelog
