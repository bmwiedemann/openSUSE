#
# spec file for package python-lfdfiles
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


%define skip_python2 1
%define skip_python36 1
%define packagename lfdfiles
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-lfdfiles
Version:        2020.9.18
Release:        0
Summary:        Laboratory for Fluorescence Dynamics (LFD) file formats
License:        BSD-3-Clause
URL:            https://www.lfd.uci.edu/~gohlke/
Source:         https://github.com/cgohlke/lfdfiles/archive/v%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module czifile >= 2019.7.2}
BuildRequires:  %{python_module matplotlib >= 3.2.0}
BuildRequires:  %{python_module netpbmfile >= 2020.9.18}
BuildRequires:  %{python_module numpy >= 1.15}
BuildRequires:  %{python_module oiffile >= 2020.9.18}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tifffile >= 2020.9.3}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
Requires:       python-czifile >= 2019.7.2
Requires:       python-matplotlib >= 3.2.0
Requires:       python-netpbmfile >= 2020.9.18
Requires:       python-numpy >= 1.15
Requires:       python-oiffile >= 2020.9.18
Requires:       python-tifffile >= 2020.9.3
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
Lfdfiles is a Python library and console script for reading, writing,
converting, and viewing many of the proprietary file formats used to store
experimental data at the Laboratory for Fluorescence Dynamics.

%prep
%setup -q -n %{packagename}-%{version}
# Fix warning: wrong end-of-line encoding
sed -i 's/\r//g' README.rst

%build
%python_build

%install
%python_install
for p in %{packagename} ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done

%python_expand %fdupes %{buildroot}%{$python_sitearch}
%prepare_alternative %{packagename}

%post
%python_install_alternative %{packagename}

%postun
%python_uninstall_alternative %{packagename}

%check
# Test not provided

%files %{python_files}
%license LICENSE
%doc README.rst
%python_alternative %{_bindir}/%{packagename}
%{python_sitearch}/*egg-info
%{python_sitearch}/%{packagename}/

%changelog
