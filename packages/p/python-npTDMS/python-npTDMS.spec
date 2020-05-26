#
# spec file for package python-npTDMS
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
Name:           python-npTDMS
Version:        0.18.1
Release:        0
Summary:        Python module for reading TDMS files produced by LabView
License:        LGPL-3.0-only
URL:            https://github.com/adamreeve/npTDMS
Source:         https://github.com/adamreeve/npTDMS/archive/%{version}.tar.gz#/npTDMS-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module numpy}
# /SECTION
%python_subpackages

%description
NumPy based module for reading TDMS files produced by LabView.

%prep
%setup -q -n npTDMS-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/tdmsinfo
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -B -m unittest discover -s nptdms -p "*_test.py"

%post
%python_install_alternative tdmsinfo

%postun
%python_uninstall_alternative tdmsinfo

%files %{python_files}
%doc README.rst
%license COPYING COPYING.LESSER
%python_alternative %{_bindir}/tdmsinfo
%{python_sitelib}/*

%changelog
