#
# spec file for package deskflow
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define         qt6ver 6.7.0
%define         appid org.deskflow.deskflow
Name:           deskflow
Version:        1.25.0
Release:        0
Summary:        Share a single keyboard and mouse between multiple computers
License:        GPL-2.0-only AND MIT AND SUSE-GPL-2.0-with-openssl-exception AND LGPL-2.1-only
URL:            https://github.com/deskflow/deskflow
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         disable-updater.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.24
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(CLI11)
BuildRequires:  pkgconfig(Qt6Core) >= %{qt6ver}
BuildRequires:  pkgconfig(Qt6DBus) >= %{qt6ver}
BuildRequires:  pkgconfig(Qt6Linguist) >= %{qt6ver}
BuildRequires:  pkgconfig(Qt6Network) >= %{qt6ver}
BuildRequires:  pkgconfig(Qt6Test) >= %{qt6ver}
BuildRequires:  pkgconfig(Qt6Widgets) >= %{qt6ver}
BuildRequires:  pkgconfig(Qt6Xml) >= %{qt6ver}
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmock)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libcrypto) >= 3.0.0
BuildRequires:  pkgconfig(libei-1.0) >= 1.3.0
BuildRequires:  pkgconfig(libportal) >= 0.8.0
BuildRequires:  pkgconfig(pugixml)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(tomlplusplus)
BuildRequires:  pkgconfig(valgrind)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xtst)

%description
Deskflow is a free and open source keyboard and mouse sharing app. Use the
keyboard, mouse, or trackpad of one computer to control nearby computers, and
work seamlessly between them. It's like a software KVM (but without the video).
TLS encryption is enabled by default. Wayland is supported. Clipboard sharing
is supported.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
%{summary}.


%prep
%autosetup -p1

%build
%cmake \
  -DBUILD_DOCS=ON \
  -DBUILD_GUI=ON \
  -DBUILD_INSTALLER=OFF \
  -DBUILD_TESTS=ON \
  -DBUILD_UNIFIED=OFF
%cmake_build

%install
%cmake_install
install -Dm0644 ./deploy/linux/%{appid}.desktop %{buildroot}%{_datadir}/applications/%{appid}.desktop
install -Dm0644 ./deploy/linux/%{appid}.metainfo.xml %{buildroot}%{_datadir}/metainfo/%{appid}.metainfo.xml
install -Dm0644 ./deploy/linux/%{appid}.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/%{appid}.png
%fdupes %{buildroot}%{_docdir}

%check
./build/bin/legacytests

%files
%license LICENSE LICENSE_EXCEPTION
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-core
%{_datadir}/%{name}
%{_datadir}/applications/%{appid}.desktop
%{_datadir}/icons/hicolor/512x512/apps/%{appid}.png
%{_datadir}/metainfo/%{appid}.metainfo.xml

%files doc
%{_docdir}/%{name}/html

%changelog
