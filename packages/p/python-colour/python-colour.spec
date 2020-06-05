#
# spec file for package python-colour
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
Name:           python-colour
Version:        0.1.5
Release:        0
Summary:        Python module to convert between color representations (RGB, HSL, web)
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/vaab/colour
Source0:        https://files.pythonhosted.org/packages/source/c/colour/colour-%{version}.tar.gz
BuildRequires:  %{python_module d2to1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python module to convert between color representations:
  * RGB, HSL, 6-digit hex, 3-digit hex, human color
  * One object (Color) or several single purpose functions
    (rgb2hex, hsl2rgb, ...)
  * Web format which uses the smallest representation between
    6-digit (e.g. #fa3b2c), 3-digit (e.g. #fbb), fully spelled
    color (e.g. white), following W3C color naming for compatible
    CSS or HTML color specifications
  * Color scale generation choosing N color gradients
  * It's possible to pick colors to identify objects of the
    application being developed

%prep
%setup -q -n colour-%{version}
rm -rf colour.egg-info

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest --doctest-modules

%files %{python_files}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python_sitelib}/*

%changelog
