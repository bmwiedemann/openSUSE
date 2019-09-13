#
# spec file for package python-ExifRead
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
Name:           python-ExifRead
Version:        2.1.2
Release:        0
Summary:        Module to read Exif metadata from TIFF and JPEG files
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/ExifRead/%{version}
Source:         https://files.pythonhosted.org/packages/source/E/ExifRead/ExifRead-2.1.2.tar.gz
Source1:        https://github.com/ianare/exif-samples/archive/master.tar.gz#/exif-samples-master.tar.gz
Patch0:         https://patch-diff.githubusercontent.com/raw/ianare/exif-py/pull/58.patch#/merged_pr_58.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A Python module to extract Exif metadata from TIFF and JPEG files.

%prep
%setup -q -n ExifRead-%{version} -a1
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
find exif-samples-master -name "*.tiff" -o -name "*.jpg" -exec $python %{buildroot}%{_bindir}/EXIF.py {} \;
find exif-samples-master -name "*.tiff" -o -name "*.jpg" -exec $python %{buildroot}%{_bindir}/EXIF.py -dc {} \;
}

%files %{python_files}
%license LICENSE.txt
%doc README.rst ChangeLog.rst
%{python_sitelib}/exifread/
%{python_sitelib}/ExifRead-%{version}-py*.egg-info
%python3_only %{_bindir}/EXIF.py

%changelog
