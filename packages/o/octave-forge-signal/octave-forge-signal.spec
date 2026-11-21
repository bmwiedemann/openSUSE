#
# spec file for package octave-forge-signal
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


%define octpkg  signal
Name:           octave-forge-%{octpkg}
Version:        1.4.8
Release:        0
Summary:        Signal processing tools for Octave
License:        GPL-3.0-or-later AND LicenseRef-SUSE-Public-Domain
Group:          Productivity/Scientific/Math
URL:            https://gnu-octave.github.io/packages/%{octpkg}/
Source0:        https://github.com/gnu-octave/octave-%{octpkg}/releases/download/%{version}/%{octpkg}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  gnuplot
BuildRequires:  hdf5-devel
BuildRequires:  octave-devel
BuildRequires:  octave-forge-control >= 2.4.5
Requires:       octave-cli >= 3.8.0
Requires:       octave-forge-control >= 2.4.5

%description
Signal processing tools, including filtering, windowing and display functions.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
%octave_pkg_src

%build
%octave_pkg_build

%install
%octave_pkg_install

# Fix shebangs
sed -i '1s|#!/usr/bin/env octave|#!/usr/bin/octave|' %{buildroot}%{_datadir}/octave/packages/signal-%{version}/doc/mkdoccache.m
sed -i '1s|^#!/usr/bin/env python3|#!/usr/bin/python3|' %{buildroot}%{_datadir}/octave/packages/signal-%{version}/doc/mkfuncdocs.py
sed -i '1s|^#!/usr/bin/env python3|#!/usr/bin/python3|' %{buildroot}%{_datadir}/octave/packages/signal-%{version}/doc/mkqhcp.py

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
