#
# spec file for package octave-forge-level-set
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


%define octpkg  level-set
Name:           octave-forge-%{octpkg}
Version:        0.3.1
Release:        0
Summary:        Level-Set functions for Octave
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gnu-octave.github.io/packages/level-set/
Source0:        %{octpkg}-%{version}.tar.xz
Patch0:         https://file.savannah.gnu.org/file/octave9.patch?file_id=55685#/fix_octave9_compat.patch
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  octave-devel
BuildRequires:  octave-forge-parallel
Requires:       octave-cli >= 4.0.0
Requires:       octave-forge-parallel

%description
Routines for calculating the time-evolution of the level-set equation
and extracting geometric information from the level-set function.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
%patch -p1 -P0 -d %{octpkg}-%{version}
(cd %{octpkg}-%{version}/src; aclocal; autoreconf -f )
%octave_pkg_src

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%global octskiptests ls_sign_colourmap
echo "Skip tests requiring graphical toolkit: %{octskiptests}"
%octave_pkg_test

%post
%octave --eval "pkg rebuild"

%postun
%octave --eval "pkg rebuild"

%files
%{octpackages_dir}/%{octpkg}-%{version}
%{octlib_dir}/%{octpkg}-%{version}

%changelog
