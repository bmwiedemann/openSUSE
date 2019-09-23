#
# spec file for package python-pyssim
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
Name:           python-pyssim
Version:        0.4
Release:        0
Summary:        Structured Similarity Image Metric (SSIM)
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/jterrace/pyssim
Source:         https://github.com/jterrace/pyssim/archive/v%{version}.tar.gz
Patch0:         Pillow-imports.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       python-numpy
Requires:       python-scipy
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module scipy}
# /SECTION
%python_subpackages

%description
Module for computing Structured Similarity Image Metric (SSIM) in Python.

%prep
%setup -q -n pyssim-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand # Tests extracted from .travis.yml
$python -m ssim test-images/test1-1.png test-images/test1-1.png | grep 1
$python -m ssim test-images/test1-1.png test-images/test1-2.png | grep 0.998
$python -m ssim test-images/test1-1.png "test-images/*" | grep -E " 1| 0.998| 0.672| 0.648" | wc -l | grep 4
$python -m ssim --cw --width 128 --height 128 test-images/test1-1.png test-images/test1-1.png | grep 1
$python -m ssim --cw --width 128 --height 128 test-images/test3-orig.jpg test-images/test3-rot.jpg | grep 0.938
}

%files %{python_files}
%license LICENSE.md
%doc README.md
%python3_only %{_bindir}/pyssim
%{python_sitelib}/*

%changelog
