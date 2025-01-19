#
# spec file for package swayimg
#
# Copyright (c) 2025 mantarimay
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


%bcond_with test
Name:           swayimg
Version:        3.7
Release:        0
Summary:        Image viewer for Sway/Wayland
License:        MIT
URL:            https://github.com/artemsen/swayimg
Source:         https://github.com/artemsen/swayimg/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  giflib-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.60.0
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
%if 0%{?suse_version} > 1600
BuildRequires:  pkgconfig(OpenEXR) >= 3.1
BuildRequires:  pkgconfig(libjxl)
%endif
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libsixel)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpdemux)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(xkbcommon)

%description
Swayimg is a lightweight image viewer for Wayland display servers.

In a Sway compatible mode, the viewer creates an "overlay" above
the currently active window, which gives the illusion that you are
opening the image directly in a terminal window.

%prep
%autosetup

%build
%meson \
%if 0%{?suse_version} < 1600
  -Dexr=disabled \
  -Djxl=disabled \
%endif
%if %{with test}
  -Dtests=enabled \
%endif
  -Dversion=%{version}
%meson_build

%install
%meson_install

%if %{with test}
%check
%meson_test
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/swayimg
%dir %{_datadir}/swayimg
%{_datadir}/swayimg/swayimgrc
%{_datadir}/applications/swayimg.desktop
%{_datadir}/bash-completion/completions/swayimg
%{_datadir}/icons/hicolor/*/apps/swayimg.png
%{_mandir}/man1/swayimg.1%{?ext_man}
%{_mandir}/man5/swayimgrc.5%{?ext_man}
%{_datadir}/zsh/site-functions/_swayimg

%changelog
