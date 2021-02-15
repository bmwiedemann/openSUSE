#
# spec file for package python-cmapfile
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
# NEP 29: TW python36-numpy -scipy and -tifffile are no more
%define skip_python36 1
%define packagename cmapfile
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-cmapfile
Version:        2020.1.1
Release:        0
Summary:        Write Chimera Map (CMAP) files
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://www.lfd.uci.edu/~gohlke/
Source:         https://github.com/cgohlke/cmapfile/archive/v%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module h5py >= 2.9}
BuildRequires:  %{python_module numpy >= 1.14.5}
BuildRequires:  %{python_module scipy >= 1.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tifffile >= 2019.1.1}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-h5py >= 2.9
Requires:       python-numpy >= 1.14.5
Requires:       python-oiffile >= 2020.1.1
Requires:       python-scipy >= 1.2
Requires:       python-tifffile >= 2019.1.1
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Create Chimera MAP files from various file formats containing volume data.

%prep
%setup -q -n %{packagename}-%{version}
# Fix warning wrong-file-end-of-line-encoding
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
