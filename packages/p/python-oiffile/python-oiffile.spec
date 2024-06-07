#
# spec file for package python-oiffile
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-oiffile
Version:        2024.5.24
Release:        0
Summary:        Read Olympus(r) image files (OIF and OIB)
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://www.lfd.uci.edu/~gohlke/
# SourceRepository: https://github.com/cgohlke/oiffile
Source:         https://github.com/cgohlke/oiffile/archive/v%{version}.tar.gz#/oiffile-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module numpy >= 1.22}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tifffile >= 2021.11.2}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.22
Requires:       python-tifffile >= 2021.11.2
BuildArch:      noarch
%python_subpackages

%description
Oiffile is a Python library to read image and metadata from Olympus Image
Format files. OIF is the native file format of the Olympus FluoView(tm)
software for confocal microscopy.

%prep
%setup -q -n oiffile-%{version}
# Fix warning: wrong end-of-line encoding
sed -i 's/\r//g' README.rst

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# No test provided

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/oiffile
%{python_sitelib}/oiffile-%{version}.dist-info

%changelog
