#
# spec file for package octave-forge-image-acquisition
#
# Copyright (c) 2023 SUSE LLC
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
Version:        0.2.2
Release:        0
Summary:        Image Acquisition functions for Octave
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            http://octave.sourceforge.net
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM image-acquisition-error-state.patch badshah400@gmail.com -- Fix build failure against octave >= 6 by dropping use of error_state (https://savannah.gnu.org/bugs/index.php?63136)
Patch0:         image-acquisition-error-state.patch
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  libv4l-devel
BuildRequires:  octave-devel
Requires:       octave-cli >= 3.8.0

%description
The Octave-forge Image Aquisition package provides functions to capture
images from connected devices. Currently only v4l2 is supported.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
pushd %{octpkg}-%{version}
%autopatch -p1
popd
%octave_pkg_src

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_test

%post
%octave --eval "pkg rebuild"

%postun
%octave --eval "pkg rebuild"

%files
%{octpackages_dir}/%{octpkg}-%{version}/
%{octlib_dir}/%{octpkg}-%{version}/

%changelog
