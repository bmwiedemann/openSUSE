#
# spec file for package python-ExifRead
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
Name:           python-ExifRead
Version:        2.3.1
Release:        0
Summary:        Module to read Exif metadata from TIFF and JPEG files
License:        BSD-3-Clause
URL:            https://pypi.python.org/pypi/ExifRead/%{version}
Source:         https://files.pythonhosted.org/packages/source/E/ExifRead/ExifRead-%{version}.tar.gz
Source1:        https://github.com/ianare/exif-samples/archive/master.tar.gz#/exif-samples-master.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
A Python module to extract Exif metadata from TIFF and JPEG files.

%prep
%setup -q -n ExifRead-%{version} -a1

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/EXIF.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
find exif-samples-master -name "*.tiff" -o -name "*.jpg" -exec $python %{buildroot}%{_bindir}/EXIF.py-%{python_bin_suffix} {} \;
find exif-samples-master -name "*.tiff" -o -name "*.jpg" -exec $python %{buildroot}%{_bindir}/EXIF.py-%{python_bin_suffix} -dc {} \;
}

%post
%python_install_alternative EXIF.py

%postun
%python_uninstall_alternative EXIF.py

%files %{python_files}
%license LICENSE.txt
%doc README.rst ChangeLog.rst
%{python_sitelib}/exifread/
%{python_sitelib}/ExifRead-%{version}-py*.egg-info
%python_alternative %{_bindir}/EXIF.py

%changelog
