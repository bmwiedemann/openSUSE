#
# spec file for package qimgv
#
# Copyright (c) 2021 SUSE LLC
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


Name:           qimgv
Version:        1.0.2
Release:        0
Summary:        Qt5 image viewer
License:        GPL-3.0-only
URL:            https://github.com/easymodo/qimgv
Source0:        https://github.com/easymodo/qimgv/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE qimgv-PIE.patch # aloisio@gmx.com add PIE flags
Patch1:         qimgv-PIE.patch
# PATCH-FIX-OPENSUSE qimgv-includepath.patch # aloisio@gmx.com use correct path for opencv includes
Patch2:         qimgv-includepath.patch
# PATCH-FIX-OPENSUSE qimgv-no_return_in_nonvoid.patch # aloisio@gmx.com pacify rpmlint
Patch6:         qimgv-no_return_in_nonvoid.patch
BuildRequires:  cmake >= 3.13
%if 0%{?suse_version} > 1500
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc9-c++
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  opencv-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.12
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(mpv) >= 1.22.0
Requires:       mpv >= 0.32.0

%description
Qt5 image viewer with webm support.

%prep
%autosetup -p1

%build
export CXX=g++
test -x "$(type -p g++-9)" && export CXX=g++-9
%cmake
%make_jobs

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_libdir}/%{name}
%{_libdir}/%{name}/player_mpv.so

%changelog
