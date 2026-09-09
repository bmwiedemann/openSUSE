#
# spec file for package octave-forge-tisean
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define octpkg  tisean
Name:           octave-forge-%{octpkg}
Version:        0.2.4
Release:        0
Summary:        Nonlinear Time Series Analysis
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gnu-octave.github.io/packages/tisean/
Source0:        https://downloads.sourceforge.net/project/octave/Octave%20Forge%20Packages/Individual%20Package%20Releases/%{octpkg}-%{version}.tar.gz
Patch1:         0001-Fix-const-correctness-invalid-used-of-non-const-fort.patch
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  octave-devel
Requires:       octave-cli >= 4.0.0
Requires:       octave-forge-signal >= 1.3.0

%description
TISEAN stands for TIme SEries ANalysis.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
pushd %{octpkg}-%{version}
%autopatch -p1
# Fix missing namespace
find src/ -iname \*.cc -exec sed -i -e 's@set_warning_state\s*(@octave::\0@g' '{}' \;
popd
%octave_pkg_src

%build
# autoconf compiler detection is broken, force it
export CXX="g++ -std=gnu++17"
%octave_pkg_build

%install
%octave_pkg_install

%check
# See https://savannah.gnu.org/bugs/index.php?56541
%global octskiptests %{octskiptests}|ikeda|lyap_spec
echo "Skip tests requiring using chaotic ikeda time series: %{octskiptests}"
%octave_pkg_test

%post
%octave --eval "pkg rebuild"

%postun
%octave --eval "pkg rebuild"

%files
%{octpackages_dir}/%{octpkg}-%{version}
%{octlib_dir}/%{octpkg}-%{version}

%changelog
