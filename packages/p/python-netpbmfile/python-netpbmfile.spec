#
# spec file for package python-netpbmfile
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
%define packagename netpbmfile
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-netpbmfile
Version:        2020.10.18
Release:        0
Summary:        Read and write image files in the Netpbm format
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://www.lfd.uci.edu/~gohlke/
Source:         https://github.com/cgohlke/netpbmfile/archive/v%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module matplotlib >= 3.2}
BuildRequires:  %{python_module numpy >= 1.15}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-matplotlib >= 3.2
Requires:       python-numpy >= 1.15
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Netpbmfile is a Python library to read and write image files in the Netpbm
format.

%prep
%setup -q -n %{packagename}-%{version}
# Fix warning: wrong end-of-line encoding
sed -i 's/\r//' README.rst

%build
%python_build

%install
%python_install
for p in %{packagename} ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done

%python_expand %fdupes %{buildroot}%{$python_sitelib}
%prepare_alternative %{packagename}

%post
%python_install_alternative %{packagename}

%postun
%python_uninstall_alternative %{packagename}

%check
# Test not provided

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/%{packagename}
%{python_sitelib}/*egg-info/
%{python_sitelib}/%{packagename}/

%changelog
