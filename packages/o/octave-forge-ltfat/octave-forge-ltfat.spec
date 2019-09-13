#
# spec file for package octave-forge-ltfat
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define octpkg  ltfat
Name:           octave-forge-%{octpkg}
Version:        2.3.1
Release:        0
Summary:        The Large Time-Frequency Analysis Toolbox for Octave
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
Url:            http://octave.sourceforge.net
Source0:        http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
BuildRequires:  blas-devel
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  fftw3-threads-devel
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  java-devel
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
%setup -q -c %{name}-%{version}
%octave_pkg_src

%build
%octave_pkg_build

%install
%octave_pkg_install
%fdupes %{buildroot}%{octpackages_dir}/%{octpkg}-%{version}

%check
%octave_pkg_test

%post
%octave --eval "pkg rebuild"

%postun
%octave --eval "pkg rebuild"

%files
%defattr(-,root,root)
%{octpackages_dir}/%{octpkg}-%{version}
%{octlib_dir}/%{octpkg}-%{version}

%changelog
