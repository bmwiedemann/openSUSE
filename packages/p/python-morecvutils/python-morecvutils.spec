#
# spec file for package python-morecvutils
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
%define         skip_python2 1
Name:           python-morecvutils
Version:        1.0.2
Release:        0
Summary:        Computer Vision utilities
License:        MIT
URL:            https://github.com/scivision/morecvutils
Source:         https://github.com/scivision/morecvutils/archive/v%{version}.tar.gz#/morecvutils-%{version}.tar.gz
BuildRequires:  %{python_module pip >= 10}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       ffmpeg
Requires:       gstreamer-plugins-good
Requires:       python-imageio
Requires:       python-imageio-ffmpeg
Requires:       python-numpy
Requires:       python-opencv
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module coveralls}
BuildRequires:  %{python_module imageio-ffmpeg}
BuildRequires:  %{python_module imageio}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module opencv}
BuildRequires:  %{python_module pytest}
BuildRequires:  ffmpeg
BuildRequires:  gstreamer-plugins-good
# /SECTION
%python_subpackages

%description
Computer Vision utilities, Cohen-Sutherland line clipping,
OpenCV plot helpers for Optical Flow and Blob Analysis,
and AVI codec helpers.

%prep
%setup -q -n morecvutils-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Don't put demos in bindir
rm %{buildroot}%{_bindir}/Demo*
rm %{buildroot}%{_bindir}/OpticalFlow_Python_vs_Matlab.py 

%check
# test uses AVC/AAC file
%pytest -k "not test_avi"

%files %{python_files}
%doc README.md
%doc Demo*
%doc OpticalFlow_Python_vs_Matlab.py
%license LICENSE.txt
%{python_sitelib}/*

%changelog
