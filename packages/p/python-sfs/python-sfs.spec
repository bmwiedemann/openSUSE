#
# spec file for package python-sfs
#
# Copyright (c) 2021 SUSE LLC
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
%define         skip_python2 1
%define         skip_python36 1
Name:           python-sfs
Version:        0.5.0
Release:        0
Summary:        Sound Field Synthesis toolbox for Python
License:        MIT
URL:            https://github.com/sfstoolbox/
Source:         https://files.pythonhosted.org/packages/source/s/sfs/sfs-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-scipy
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
# /SECTION
%python_subpackages

%description
The Sound Field Synthesis Toolbox for Python gives you the
possibility to create numercial simulations of sound field
synthesis methods like wave field synthesis (WFS) or
near-field compensated higher order Ambisonics (NFC-HOA).

%prep
%setup -q -n sfs-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc NEWS.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
