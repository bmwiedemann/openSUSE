#
# spec file for package python-Glymur
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
%define         skip_python2 1
Name:           python-Glymur
Version:        0.8.19
Release:        0
Summary:        Tools for accessing JPEG2000 files
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/quintusdias/glymur
Source:         https://files.pythonhosted.org/packages/source/G/Glymur/Glymur-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  procps
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.7.1
Recommends:     python-lxml
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module numpy >= 1.7.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scikit-image}
# /SECTION
%python_subpackages

%description
Python interface to the OpenJPEG library

%prep
%setup -q -n Glymur-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
touch tests/data/__init__.py
%pytest

%files %{python_files}
%doc README.md CHANGES.txt
%license LICENSE.txt
%python3_only %{_bindir}/jp2dump
%{python_sitelib}/*

%changelog
