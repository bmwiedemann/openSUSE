#
# spec file for package octave-forge-ltfat
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


%define octpkg  ltfat
Name:           octave-forge-%{octpkg}
Version:        2.6.0
Release:        0
Summary:        The Large Time-Frequency Analysis Toolbox for Octave
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gnu-octave.github.io/packages/ltfat/
Source0:        https://github.com/ltfat/ltfat/releases/download/v%{version}/ltfat-%{version}-of.tar.gz
# PATCH-FIX-UPSTREAM ltfat-fix-jar-bin-path.patch badshah400@gmail.com --  Remove extraneous Windows path for jar, upstream commit 8bf70b2
Patch0:         ltfat-fix-jar-bin-path.patch
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  fftw3-threads-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  java-devel >= 1.8
BuildRequires:  lapack-devel
BuildRequires:  octave-devel
BuildRequires:  portaudio-devel
Requires:       octave-cli >= 3.8.0

%description
The Large Time/Frequency Analysis Toolbox (LTFAT) is a Matlab/Octave toolbox
for working with time-frequency analysis, wavelets and signal processing.
It is intended both as an educational and a computational tool. The toolbox
provides a large number of linear transforms including Gabor and wavelet
transforms along with routines for constructing windows (filter prototypes)
and routines for manipulating coefficients.
This is part of the Octave-Forge project.

%prep
%autosetup -p1 -c %{name}-%{version}

# REMOVE PREBUILT JAR
find ./ -name "*.jar" -delete -print

# Building with Octave 10 requires C++17, https://github.com/ltfat/ltfat/issues/203
sed -i -e 's/gnu++11/gnu++17/' ltfat/oct/Makefile_unix

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
pushd ./ltfat/inst/blockproc/java/
%make_build
popd
%octave_pkg_src

%octave_pkg_build

%install
%octave_pkg_install
%fdupes %{buildroot}%{octpackages_dir}/%{octpkg}-%{version}

sed -Ei '1{\@#!/usr/bin/env python@d}' %{buildroot}%{octpackages_dir}/%{octpkg}-%{version}/private/test_ltfatarghelper.py

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
