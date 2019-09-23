#
# spec file for package python-audiomate
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-audiomate
Version:        3.0.0
Release:        0
Summary:        A library for working with audio datasets
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/ynop/audiomate
Source0:        https://files.pythonhosted.org/packages/source/a/audiomate/audiomate-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module audioread >= 2.1.0}
BuildRequires:  %{python_module beautifulsoup4 >= 4.6.0}
BuildRequires:  %{python_module h5py >= 2.7.1}
BuildRequires:  %{python_module librosa >= 0.6.0}
BuildRequires:  %{python_module lxml >= 4.1.1}
BuildRequires:  %{python_module networkx >= 2.0}
BuildRequires:  %{python_module numpy >= 1.14.0}
BuildRequires:  %{python_module pytest >= 3.3.0}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module requests >= 2.18.4}
BuildRequires:  %{python_module requests-mock >= 1.4.0}
BuildRequires:  %{python_module scipy >= 1.1.0}
# /SECTION
Requires:       python-audioread >= 2.1.0
Requires:       python-beautifulsoup4 >= 4.6.0
Requires:       python-h5py >= 2.7.1
Requires:       python-librosa >= 0.6.0
Requires:       python-lxml >= 4.1.1
Requires:       python-networkx >= 2.0
Requires:       python-numpy >= 1.14.0
Requires:       python-requests >= 2.18.4
Requires:       python-scipy >= 1.1.0
BuildArch:      noarch

%python_subpackages

%description
Audiomate is a library providing datastructures for accessing/loading
audio datasets.

%prep
%setup -q -n audiomate-%{version}

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
