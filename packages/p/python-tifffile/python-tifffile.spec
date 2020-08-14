#
# spec file for package python-tifffile
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


%define packagename tifffile
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_with test
Name:           python-tifffile
Version:        2020.5.30
Release:        0
Summary:        Read and write TIFF(r) files
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://www.lfd.uci.edu/~gohlke/
Source:         https://github.com/cgohlke/tifffile/archive/v%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module numpy >= 1.11.3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module imagecodecs}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click
Requires:       python-numpy >= 1.11.3
Suggests:       python-matplotlib >= 2.2
Requires:       python-imagecodecs
BuildArch:      noarch
%python_subpackages

%description
Read and write TIFF(r) files. Read image and metadata from many
bio-scientific formats such as plain TIFF, BigTIFF, OME-TIFF, STK, LSM,
SGI, NIH, ImageJ, MicroManager, MD GEL, and FluoView files. Write numpy
arrays to TIFF, BigTIFF, and ImageJ hyperstack compatible files.

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

for p in lsm2bin ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
done

%python_expand %fdupes %{buildroot}%{$python_sitelib}
%prepare_alternative %{packagename}
%prepare_alternative lsm2bin

%post
%python_install_alternative %{packagename}
%python_install_alternative lsm2bin

%postun
%python_uninstall_alternative %{packagename}
%python_uninstall_alternative lsm2bin

%check
# Test need network connection.

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/tifffile
%python_alternative %{_bindir}/lsm2bin
%{python_sitelib}/*egg-info/
%{python_sitelib}/%{packagename}/

%changelog
