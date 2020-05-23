#
# spec file for package octave-forge-general
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


%define octpkg  general
Name:           octave-forge-%{octpkg}
Version:        2.1.1
Release:        0
Summary:        General tools for Octave
License:        GPL-3.0-or-later AND BSD-3-Clause
Group:          Productivity/Scientific/Math
URL:            https://octave.sourceforge.io
Source0:        https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  hdf5-devel
BuildRequires:  octave-devel
Requires:       octave-cli >= 4.0.0

%description
General tools for Octave.
This is part of Octave-Forge project.

%prep
%setup -q -c %{name}-%{version}
%octave_pkg_src

# COPY METAINFO FILE TO TOPLEVEL DIR FOR MANUAL INSTALLATION LATER
find ./ -name "*.metainfo.xml" -exec cp '{}' ./ \;

%build
%octave_pkg_build

%install
%octave_pkg_install
mkdir -p %{buildroot}%{_datadir}/metainfo
install -m 644 octave-general.metainfo.xml %{buildroot}%{_datadir}/metainfo/

%check
%octave_pkg_test

%post
%octave --eval "pkg rebuild"

%postun
%octave --eval "pkg rebuild"

%files
%{octpackages_dir}/%{octpkg}-%{version}
%{octlib_dir}/%{octpkg}-%{version}
%{_datadir}/metainfo/*.metainfo.xml

%changelog
