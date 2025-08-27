#
# spec file for package octave-forge-image-acquisition
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define octpkg  image-acquisition
Name:           octave-forge-%{octpkg}
Version:        0.3.3
Release:        0
Summary:        Image Acquisition functions for Octave
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gnu-octave.github.io/packages/image-acquisition/
Source0:        https://github.com/Andy1978/octave-image-acquisition/releases/download/%{octpkg}-%{version}/%{octpkg}-%{version}.tar.gz
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  libv4l-devel
BuildRequires:  octave-devel >= 5.1.0
Requires:       octave-cli >= 5.1.0

%description
The Octave-forge Image Aquisition package provides functions to capture
images from connected devices. Currently only v4l2 is supported.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
%octave_pkg_src

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%global octskiptests imaqhwinfo|__imaq_handler__.cc-tst
echo "Skip tests requiring a camera device: %{octskiptests}"
%octave_pkg_test

%post
%octave --eval "pkg rebuild"

%postun
%octave --eval "pkg rebuild"

%files
%{octpackages_dir}/%{octpkg}-%{version}/
%{octlib_dir}/%{octpkg}-%{version}/

%changelog
