#
# spec file for package python-imreg
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
%define         skip_python2 1
Name:           python-imreg
Version:        2019.1.1
Release:        0
Summary:        FFT based image registration
License:        BSD-3-Clause
URL:            https://www.lfd.uci.edu/~gohlke/
Source:         https://files.pythonhosted.org/packages/source/i/imreg/imreg-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.11
Requires:       python-scipy >= 1.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module numpy >= 1.11}
BuildRequires:  %{python_module scipy >= 1.0}
# /SECTION
%python_subpackages

%description
Imreg is a Python library that implements an FFT-based technique for
translation, rotation and scale-invariant image registration.

%prep
%setup -q -n imreg-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
