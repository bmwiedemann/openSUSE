#
# spec file for package python-genfire
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


%define packagename genfire
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-genfire
Version:        1.1.11
Release:        0
Summary:        GENeralized Fourier Iterative REconstruction
License:        GPL-3.0-only
URL:            https://github.com/genfire-em/GENFIRE-Python
Source:         https://files.pythonhosted.org/packages/1e/e3/bb80c9e9f9b0255f70b230baf05609122a317945fa623eee8aba8f9ec8ec/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module Pillow >= 4.1.1}
BuildRequires:  %{python_module PyQt5 >= 5.5.0}
BuildRequires:  %{python_module matplotlib >= 2.0.2}
BuildRequires:  %{python_module numpy >= 1.12.1}
BuildRequires:  %{python_module pyFFTW}
BuildRequires:  %{python_module pyparsing >= 2.2.0}
BuildRequires:  %{python_module scipy >= 0.19.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  fdupes
Requires:       python-Pillow >= 4.1.1
Requires:       python-PyQt5 >= 5.5.0
Requires:       python-numpy >= 1.12.1
Requires:       python-pyFFTW
Requires:       python-pyparsing >= 2.2.0
Requires:       python-scipy >= 0.19.0
Requires:       python-setuptools
Requires:       python-six >= 1.10.0
BuildArch:      noarch
%python_subpackages

%description
GENeralized Fourier Iterative REconstruction (GENFIRE)
is a python package for 3D reconstruction from arbitrarily
oriented projection images

%prep
%setup -q -n %{packagename}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# No test given

%files %{python_files}
%doc README.md
%python3_only %{_bindir}/genfire
%{python_sitelib}/*

%changelog
