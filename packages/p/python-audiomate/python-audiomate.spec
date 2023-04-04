#
# spec file for package python-audiomate
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
%define         skip_python2 1
%define         skip_python36 1
# python-numba is not available for python 3.11 yet
%define         skip_python311 1
Name:           python-audiomate
Version:        6.0.0
Release:        0
Summary:        A library for working with audio datasets
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ynop/audiomate
Source0:        https://files.pythonhosted.org/packages/source/a/audiomate/audiomate-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PGet >= 0.5.0
Requires:       python-audioread >= 2.1.8
Requires:       python-h5py >= 2.10.0
Requires:       python-intervaltree >= 3.0.2
Requires:       python-librosa >= 0.7.2
Requires:       python-networkx >= 2.4
Requires:       python-numba >= 0.49.1
Requires:       python-numpy >= 1.18.1
Requires:       python-requests >= 2.23.0
Requires:       python-scipy >= 1.4.1
Requires:       python-sox >= 1.3.7
BuildArch:      noarch
%python_subpackages

%description
Audiomate is a library providing datastructures for accessing/loading
audio datasets.

%prep
%setup -q -n audiomate-%{version}
sed -i "s/'pytest-runner'//" setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Test files not present
# They would be too big
# %%check
# echo "" > tests/__init__.py
# %%{python_expand export PYTHONPATH=%%{buildroot}%%{$python_sitelib}
# py.test-%%{$python_bin_suffix} .}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
