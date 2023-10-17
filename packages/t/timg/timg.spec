#
# spec file for package timg
#
# Copyright (c) 2023 SUSE LLC
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


Name:           timg
Version:        1.5.2
Release:        0
Summary:        Terminal image viewer
License:        GPL-2.0-only
URL:            https://github.com/hzeller/timg
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(GraphicsMagick++)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libdeflate)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libsixel)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libturbojpeg)
BuildRequires:  pkgconfig(stb)

%description
A user-friendly terminal image viewer that uses graphic capabilities of
terminals (Sixel, Kitty or iterm2), or 24-Bit color capabilities and unicode
character blocks if these are not available.

%prep
%autosetup

%build
%cmake  \
    -DWITH_QOI_IMAGE=OFF \
    -DTIMG_VERSION_FROM_GIT=OFF
%{nil}
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
