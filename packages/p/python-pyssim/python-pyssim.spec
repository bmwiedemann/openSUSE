#
# spec file for package python-pyssim
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-pyssim
Version:        0.7
Release:        0
Summary:        Structured Similarity Image Metric (SSIM)
License:        MIT
URL:            https://github.com/jterrace/pyssim
Source:         https://files.pythonhosted.org/packages/source/p/pyssim/pyssim-%{version}.tar.gz
Patch0:         Pillow-imports.patch
# PATCH-FIX-UPSTREAM Use PyWavelets rather than scipy.signal gh#jterrace/pyssim#49
Patch1:         use-pywavelets.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       python-PyWavelets
Requires:       python-numpy
Requires:       python-scipy
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module PyWavelets}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module scipy}
# /SECTION
%python_subpackages

%description
Module for computing Structured Similarity Image Metric (SSIM) in Python.

%prep
%autosetup -p1 -n pyssim-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pyssim
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand # Tests extracted from .travis.yml
$python -m ssim test-images/test1-1.png test-images/test1-1.png | grep 1
$python -m ssim test-images/test1-1.png test-images/test1-2.png | grep 0.998
$python -m ssim test-images/test1-1.png "test-images/*" | grep -E " 1| 0.998| 0.672| 0.648" | wc -l | grep 4
$python -m ssim --cw --width 128 --height 128 test-images/test1-1.png test-images/test1-1.png | grep 1
$python -m ssim --cw --width 128 --height 128 test-images/test3-orig.jpg test-images/test3-rot.jpg | grep 0.938
}

%post
%python_install_alternative pyssim

%postun
%python_uninstall_alternative pyssim

%files %{python_files}
%license LICENSE.md
%doc README.md
%python_alternative %{_bindir}/pyssim
%{python_sitelib}/ssim
%{python_sitelib}/pyssim-%{version}.dist-info

%changelog
