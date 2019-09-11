#
# spec file for package octave-forge-parallel
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define octpkg  parallel
Name:           octave-forge-%{octpkg}
Version:        3.1.3
Release:        0
Summary:        Parallel Computing for Octave
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://octave.sourceforge.net
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE octave-forge-parallel-build-with-octave5.patch badshah400@gmail.com -- fix building against octave >= 5; patch taken from upstream mercurial commits
Patch0:         octave-forge-parallel-build-with-octave5.patch
BuildRequires:  gcc-c++
BuildRequires:  gnutls-devel >= 3.4.0
BuildRequires:  hdf5-devel
BuildRequires:  octave-devel
BuildRequires:  pkgconfig
BuildRequires:  zlib-devel
Requires:       octave-cli >= 3.8.0
Requires:       octave-forge-struct >= 1.0.12
# SECTION FOR PATCH0
BuildRequires:  autoconf
BuildRequires:  automake
# /SECTION

%description
Parallel execution package.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
pushd %{octpkg}-%{version}
%patch0 -p1
cd src && ./bootstrap
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
%{octpackages_dir}/%{octpkg}-%{version}
%{octlib_dir}/%{octpkg}-%{version}

%changelog
