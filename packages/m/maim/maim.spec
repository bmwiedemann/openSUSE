#
# spec file for package maim
#
# Copyright (c) 2024 SUSE LLC
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


# See also http://en.opensuse.org/openSUSE:Specfile_guidelines
Name:           maim
Version:        5.8.0
Release:        0
Summary:        Flexible screenshotting utility
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://github.com/naelstrof/maim
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.7
BuildRequires:  gcc-c++
BuildRequires:  gengetopt
BuildRequires:  glm-devel
BuildRequires:  pkgconfig
BuildRequires:  slop-devel >= 7
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(zlib)
%if 0%{?suse_version} > 1600
# We must use the C++17 standard if we're using ICU >= 75
Patch0:         use_cxx17_standard.patch
%endif

%description
maim (Make Image) is a utility that takes screenshots of the desktop
using EGL. It is meant to overcome shortcomings of the "scrot"
utility and performs better in several ways.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
