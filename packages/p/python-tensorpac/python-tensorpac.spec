#
# spec file for package python-tensorpac
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
Name:           python-tensorpac
Version:        0.6.2
Release:        0
Summary:        Tensor-based phase-Amplitude coupling package
License:        BSD-3-Clause
URL:            https://etiennecmb.github.io/tensorpac/
Source:         https://files.pythonhosted.org/packages/source/t/tensorpac/tensorpac-%{version}.tar.gz
BuildRequires:  %{python_module joblib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-joblib
Requires:       python-numpy >= 1.12
Requires:       python-scipy
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module joblib}
BuildRequires:  %{python_module numpy >= 1.12}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
# /SECTION
%python_subpackages

%description
Tensorpac is an Python toolbox for computing Phase-Amplitude Coupling
(PAC) using tensors and parallel computing.

%prep
%setup -q -n tensorpac-%{version}
chmod a-x LICENSE README.rst

%build
%python_build

%install
%python_install
%python_expand chmod a-x %{buildroot}%{$python_sitelib}/*egg-info/*
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests missing and no recent tags to download from github. See:
# https://github.com/EtienneCmb/tensorpac/issues/4
# https://github.com/EtienneCmb/tensorpac/pull/5
# %%check
# %%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
