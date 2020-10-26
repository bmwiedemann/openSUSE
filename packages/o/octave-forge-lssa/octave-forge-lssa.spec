#
# spec file for package octave-forge-lssa
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


%define octpkg  lssa
Name:           octave-forge-%{octpkg}
Version:        0.1.4
Release:        0
Summary:        Least squares spectral analysis for Octave
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://octave.sourceforge.io/%{octpkg}/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  octave-devel
Requires:       octave-cli >= 3.6.0

%description
A package implementing tools to compute spectral decompositions of
irregularly-spaced time series.  Currently includes functions based off the
Lomb-Scargle periodogram and Adolf Mathias' implementation for R and C.
This is part of the Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
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
%{octpackages_dir}/%{octpkg}-%{version}
%{octlib_dir}/%{octpkg}-%{version}

%changelog
