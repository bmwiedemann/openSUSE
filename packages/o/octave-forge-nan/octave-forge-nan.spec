#
# spec file for package octave-forge-nan
#
# Copyright (c) 2019 SUSE LLC
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


%define octpkg  nan
Name:           octave-forge-%{octpkg}
Version:        3.4.3
Release:        0
Summary:        A statistics and machine learning toolbox
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://octave.sourceforge.io
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
Patch0:         fix_missing_return.patch
BuildRequires:  libsvm-devel
BuildRequires:  octave-devel >= 3.8.0
Requires:       octave-cli >= 3.8.0

%description
A statistics and machine learning toolbox for data with and w/o missing values.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
pushd %{octpkg}-%{version}
%patch0 -p1
popd
sed -i 's/-lblas/-l%{octave_blas}/g' %{octpkg}-%{version}/src/Makefile.in
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
%defattr(-,root,root)
%{octpackages_dir}/%{octpkg}-%{version}
%{octlib_dir}/%{octpkg}-%{version}

%changelog
