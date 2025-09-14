#
# spec file for package octave-forge-tsa
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


%define octpkg  tsa
Name:           octave-forge-%{octpkg}
Version:        4.6.3
Release:        0
Summary:        Time Series Analysis Toolbox for Octave
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gnu-octave.github.io/packages/tsa/
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
BuildRequires:  octave-devel
Requires:       octave-cli >= 2.9.7
Requires:       octave-forge-nan >= 3.0.0
BuildArch:      noarch

%description
Stochastic concepts and maximum entropy methods for time series analysis.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
# src dirctory without any purpose, see https://savannah.gnu.org/bugs/index.php?57578
mv %{octpkg}-%{version}/src{,_disabled}
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

%changelog
