#
# spec file
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


%define octpkg  stk
Name:           octave-forge-%{octpkg}
Version:        2.8.0
Release:        0
Summary:        Small Octave Toolbox for Kriging
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gnu-octave.github.io/packages/%{octpkg}/
Source0:        https://github.com/stk-kriging/stk/releases/download/%{version}/stk-%{version}-octpkg.tar.gz#/%{octpkg}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  octave-devel >= 4.0.1
Requires:       octave-cli >= 4.0.1

%description
The STK is a (not so) Small Toolbox for Kriging. Its primary focus
in on the interpolation/regression technique known as kriging, which
is very closely related to Splines and Radial Basis Functions, and can be
interpreted as a non-parametric Bayesian method using a Gaussian Process
(GP) prior. The STK also provides tools for the sequential and
non-sequential design of experiments. Even though it is, currently, mostly
geared towards the Design and Analysis of Computer Experiments (DACE), the
STK can be useful for other applications areas (such as Geostatistics,
Machine Learning, Non-parametric Regression, etc.).
This is part of Octave-Forge project.

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
