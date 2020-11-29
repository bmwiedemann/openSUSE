#
# spec file for package python-oiffile
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


%define packagename oiffile
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-oiffile
Version:        2020.9.18
Release:        0
Summary:        Read Olympus(r) image files (OIF and OIB)
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://www.lfd.uci.edu/~gohlke/
Source:         https://github.com/cgohlke/oiffile/archive/v%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module numpy >= 1.15}
BuildRequires:  %{python_module tifffile >= 2020.6.3}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.15
Requires:       python-tifffile >= 2020.6.3
BuildArch:      noarch
%python_subpackages

%description
Oiffile is a Python library to read image and metadata from Olympus Image
Format files. OIF is the native file format of the Olympus FluoView(tm) 
software for confocal microscopy.

%prep
%setup -q -n %{packagename}-%{version}
# Fix warning: wrong end-of-line encoding
sed -i 's/\r//g' README.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# No test provided

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*egg-info/
%{python_sitelib}/%{packagename}/

%changelog
