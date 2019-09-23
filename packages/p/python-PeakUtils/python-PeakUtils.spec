#
# spec file for package python-PeakUtils
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
Name:           python-PeakUtils
Version:        1.3.2
Release:        0
Summary:        Peak detection utilities for 1D data
License:        MIT
Group:          Development/Languages/Python
URL:            https://bitbucket.org/lucashnegri/peakutils
Source:         https://files.pythonhosted.org/packages/source/P/PeakUtils/PeakUtils-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy
Requires:       python-scipy
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module scipy}
# /SECTION
%python_subpackages

%description
This package provides utilities related to the detection of peaks on
1D data. Includes functions to estimate baselines, finding the
indexes of peaks in the data and performing Gaussian fitting or
centroid computation to further increase the resolution of the peak
detection.

%prep
%setup -q -n PeakUtils-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand $python -m unittest discover

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/peakutils
%{python_sitelib}/PeakUtils-%{version}-*.egg-info

%changelog
