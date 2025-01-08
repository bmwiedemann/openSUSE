#
# spec file for package octave-forge-vrml
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


%define octpkg  vrml
Name:           octave-forge-%{octpkg}
Version:        1.0.13
Release:        0
Summary:        3D graphics using VRML for Octave
License:        GPL-3.0-or-later
Group:          Productivity/Scientific/Math
URL:            https://gnu-octave.github.io/packages/vrml/
Source0:        https://downloads.sourceforge.net/project/octave/Octave%20Forge%20Packages/Individual%20Package%20Releases/%{octpkg}-%{version}.tar.gz
Patch0:         https://file.savannah.gnu.org/file/octave-9.patch?file_id=55689#/fix-octave9-line-continuation.patch
BuildRequires:  octave-devel
Requires:       octave-cli >= 2.9.7
Requires:       octave-forge-linear-algebra
Requires:       octave-forge-miscellaneous
Requires:       octave-forge-statistics
Requires:       octave-forge-struct
BuildArch:      noarch

%description
3D graphics using VRML.
This is part of Octave-Forge project.

%prep
%setup -c %{name}-%{version}
(cd vrml
%patch -P0 -p1
)
%octave_pkg_src

%build
%octave_pkg_build

%install
%octave_pkg_install
find %{buildroot} -iname \*.svnignore -ls -delete

%check
%octave_pkg_test

%post
%octave --eval "pkg rebuild"

%postun
%octave --eval "pkg rebuild"

%files
%{octpackages_dir}/%{octpkg}-%{version}

%changelog
