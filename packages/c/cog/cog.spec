#
# spec file for package cog
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

Name:           cog
Version:        0.18.1
Release:        0
Summary:        WPE launcher and webapp container
License:        MIT
Group:          Productivity/Networking/Web/Browsers
URL:            https://github.com/Igalia/cog
Source:         %{name}-%{version}.tar.xz
Patch0:         cog-fix-include-dirs.patch
Patch1:         cog-fix-load-backend-fdo-lib.patch

BuildRequires: meson
BuildRequires: ninja
BuildRequires: pkg-config
BuildRequires: cmake
BuildRequires: pkgconfig(wpe-webkit-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(wpe-1.0)
BuildRequires: pkgconfig(manette-0.2)
BuildRequires: pkgconfig(wpebackend-fdo-1.0)
BuildRequires: pkgconfig(epoxy)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libinput)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(egl)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-egl)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-protocols)
BuildRequires: pkgconfig(wayland-cursor)
BuildRequires: pkgconfig(gbm)

%description
Cog is a small single “window” launcher for the WebKit WPE port. It is small,
provides no user interface, and is suitable to be used as a Web application
container. The “window” may be fullscreen depending on the WPE backend
being used.

%package -n cogctl
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++

%description -n cogctl
Cog is a small single “window” launcher for the WebKit WPE port. It is small,
provides no user interface, and is suitable to be used as a Web application
container. The “window” may be fullscreen depending on the WPE backend
being used.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       cog = %{version}

%description devel
Cog is a small single “window” launcher for the WebKit WPE port. It is small,
provides no user interface, and is suitable to be used as a Web application
container. The “window” may be fullscreen depending on the WPE backend
being used.

%prep
%autosetup -p1

%build
%meson \
  -Dplatforms='drm, wayland, headless' \
  -Dwpe_api=2.0 \
%meson_build

%install
%meson_install

%ldconfig_scriptlets

%files
%{_bindir}/cog
%{_libdir}/libcogcore.so.*
%dir %{_libdir}/cog
%{_libdir}/cog/modules
%{_mandir}/man1/cog*
%license COPYING
%doc NEWS

%files -n cogctl
%{_bindir}/cogctl

%files devel
%{_includedir}/cog
%{_libdir}/libcogcore.so
%{_libdir}/pkgconfig/cogcore.pc

%changelog
