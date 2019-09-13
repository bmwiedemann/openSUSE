#
# spec file for package qimgv
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


Name:           qimgv
Version:        0.8.2
Release:        0
Summary:        Qt5 image viewer
License:        GPL-3.0-only
Group:          Productivity/Graphics/Viewers
URL:            https://github.com/easymodo/qimgv
Source0:        https://github.com/easymodo/qimgv/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE qimgv-nosharedlib.patch # aloisio@gmx.com build helper library statically
Patch0:         qimgv-nosharedlib.patch
BuildRequires:  cmake
%if 0%{?suse_version} > 1500
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc8-c++
%endif
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.9
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.9
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(mpv) >= 1.22.0

%description
Qt5 image viewer with webm support.

%prep
%autosetup -p1

%build
export CXX=g++
test -x "$(type -p g++-8)" && export CXX=g++-8
%cmake
make %{?_smp_mflags}

%install
%cmake_install

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
