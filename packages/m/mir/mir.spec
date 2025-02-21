#
# spec file for package mir
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) Shawn W Dunn <sfalken@opensuse.org>
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


# Disable lto
%global _lto_cflags %{nil}

# Disable ctest run
# The take a long time and are generally broken in the build environment
%bcond_with run_tests

# Set globals for easier future maintenance
%global commonlibsover 11
%global mircoresover 2
%global mirplatformsover 30
%global lomirisover 5
%global miralsover 7
%global mirserversover 62
%global mirwaylandsover 5
%global mirserverplatformsover 22
%global mirevdevsover 10

Name:           mir
Version:        2.19.3
Release:        0
Summary:        Libraries for building Wayland shells
License:        (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://mir-server.io
Source:         https://github.com/canonical/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM 0001-Fix-include-paths.patch
Patch0:         0001-Fix-include-paths.patch
# PATCH-FIX-OPENSUSE 0002-remove-use-of-env-to-call-bash.patch
Patch1:         0002-remove-use-of-env-to-call-bash.patch
# PATCH-FIX-UPSTREAM 0003-workaround-for-LXQt-panel.patch sfalken@opensuse.org (gh#canonical/mir#3761)
Patch2:         0003-workaround-for-LXQt-panel.patch
# PATCH-FIX-UPSTREAM 0004-check-buffer-size.patch sfalken@opensuse.org (gh#canonical/mir#3761)
Patch3:         0004-check-buffer-size.patch
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gcovr
BuildRequires:  git-core
BuildRequires:  gnu-free-fonts
BuildRequires:  graphviz
BuildRequires:  lcov
BuildRequires:  libatomic1
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libxslt-tools
BuildRequires:  python3
BuildRequires:  python3-Pillow
BuildRequires:  systemtap-sdt-devel
BuildRequires:  valgrind

BuildRequires:  cmake(GTest) >= 1.8.0
BuildRequires:  cmake(glm)
BuildRequires:  cmake(glog)
BuildRequires:  cmake(yaml-cpp)

BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm) >= 9.0.0
BuildRequires:  pkgconfig(gflags)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtest) >= 1.8.0
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libxml++-2.6)
BuildRequires:  pkgconfig(lttng-ust)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(umockdev-1.0) >= 0.6
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-eglstream)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlcs)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)

%description
A set of libraries for building Wayland based shells.

%package devel
Summary:        Development files for Mir
Requires:       %{name}-test-libs-static = %{version}
Requires:       libmircommon%{commonlibsover} = %{version}
Requires:       libmiroil%{lomirisover} = %{version}
Requires:       libmirserver%{mirserversover} = %{version}
Requires:       libmirserverplatform%{mirserverplatformsover} = %{version}
Requires:       libmirevdev%{mirevdevsover} = %{version}

%description devel
This package provides the development files to create compositors built on Mir

%package private-devel
Summary:        Development files for Mir exposing private internals
Requires:       %{name}-devel = %{version}

%description private-devel
This package provides extra development files to create compositors built on
Mir that need acces to private internal interfaces

%package -n libmircommon%{commonlibsover}
Summary:        Mir server library
License:        LGPL-2.1-only OR LGPL-3.0-only

%description -n libmircommon%{commonlibsover}
Component library of the Mir compositing stack

%package -n libmircore%{mircoresover}
Summary:        Mir core library
License:        LGPL-2.1-only OR LGPL-3.0-only

%description -n libmircore%{mircoresover}
Component library of the Mir compositing stack

%package -n libmirplatform%{mirplatformsover}
Summary:        Mir platform library
License:        LGPL-2.1-only OR LGPL-3.0-only

%description -n libmirplatform%{mirplatformsover}
Component library of the Mir compositing stack

%package -n libmiroil%{lomirisover}
Summary:        Lomiri compatibility libraries for Mir
License:        LGPL-2.1-only OR LGPL-3.0-only

%description -n libmiroil%{lomirisover}
This package provides the libraries for Lomiri to use Mir as a Wayland compositor

%package -n libmiral%{miralsover}
Summary:        Mir Abstraction Layer library
License:        LGPL-2.1-only OR LGPL-3.0-only

%description -n libmiral%{miralsover}
Component library of the Mir compositing stack

%package -n libmirserver%{mirserversover}
Summary:        Mir server library
License:        GPL-2.0-only OR GPL-3.0-only
Requires:       libmirserverplatform%{mirserverplatformsover}
Requires:       libmirevdev%{mirevdevsover}

%description -n libmirserver%{mirserversover}
Component library of the Mir compositing stack

%package -n libmirwayland%{mirwaylandsover}
Summary:        Mir Wayland library
License:        LGPL-2.1-only OR LGPL-3.0-only

%description -n libmirwayland%{mirwaylandsover}
Component library of the Mir compositing stack

%package -n libmirserverplatform%{mirserverplatformsover}
Summary:        Mir Server Platform Library
License:        LGPL-2.1-only OR LGPL-3.0-only

%description -n libmirserverplatform%{mirserverplatformsover}
Component library of the Mir server platform

%package -n libmirevdev%{mirevdevsover}
Summary:        Evdev support for Mir
License:        LGPL-2.1-only OR LGPL-3.0-only

%description -n libmirevdev%{mirevdevsover}
evdev support library for the Mir server platform

%package test-tools
Summary:        Testing tools for Mir
License:        GPL-2.0-only OR GPL-3.0-only
Requires:       libmirserver%{mirserversover} = %{version}
Requires:       wlcs
Recommends:     %{name}-demos
Recommends:     glmark2
Recommends:     xwayland

%description test-tools
This package provides tools for testing Mir

%package demos
Summary:        Demonstration applications using Mir
License:        GPL-2.0-only OR GPL-3.0-only
Requires:       bash
Requires:       gnu-free-fonts
Requires:       hicolor-icon-theme
Requires:       inotify-tools
Requires:       libmirserver%{mirserversover} = %{version}
Requires:       xkeyboard-config
Requires:       xwayland

%description demos
This package provides applications for demonstrating the capabilities of the
Mir display server

%package test-libs-static
Summary:        Testing framework library for Mir
License:        GPL-2.0-only OR GPL-3.0-only
Requires:       %{name}-devel = %{version}

%description test-libs-static
This package provides the static library for building Mir unit and integration
tests

%prep
%autosetup -S git_am

# Drop -Werror
sed -e "s/-Werror//g" -i CMakeLists.txt

%build
%cmake -DMIR_USE_PRECOMPILED_HEADERS=OFF \
       -DCMAKE_INSTALL_LIBEXECDIR="usr/libexec/mir" \
       -DMIR_PLATFORM="gbm-kms;x11;wayland;eglstream-kms"

%cmake_build

%install
%cmake_install

%check
%if %{with run_tests}
( %ctest ) || :
%endif

desktop-file-validate %{buildroot}%{_datadir}/applications/miral-shell.desktop

%ldconfig_scriptlets -n libmircommon%{commonlibsover}
%ldconfig_scriptlets -n libmircore%{mircoresover}
%ldconfig_scriptlets -n libmirplatform%{mirplatformsover}
%ldconfig_scriptlets -n libmiroil%{lomirisover}
%ldconfig_scriptlets -n libmiral%{miralsover}
%ldconfig_scriptlets -n libmirserver%{mirserversover}
%ldconfig_scriptlets -n libmirwayland%{mirwaylandsover}
%ldconfig_scriptlets -n libmirserverplatform%{mirserverplatformsover}
%ldconfig_scriptlets -n libmirevdev%{mirevdevsover}

%files devel
%license COPYING.*
%{_bindir}/mir_wayland_generator
%{_libdir}/libmir*.so
%{_libdir}/pkgconfig/mir*.pc
%exclude %{_libdir}/pkgconfig/mir*internal.pc
%{_includedir}/mir*/
%exclude %{_includedir}/mir*internal/

%files private-devel
%license COPYING.*
%{_libdir}/pkgconfig/mir*internal.pc
%{_includedir}/mir*internal/

%files -n libmircommon%{commonlibsover}
%license COPYING.LGPL*
%doc README.md
%dir %{_libdir}/mir
%{_libdir}/libmircommon.so.%{commonlibsover}
%{_libdir}/mir/miral*.so

%files -n libmircore%{mircoresover}
%{_libdir}/libmircore.so.%{mircoresover}

%files -n libmirplatform%{mirplatformsover}
%{_libdir}/libmirplatform.so.%{mirplatformsover}

%files -n libmiroil%{lomirisover}
%{_libdir}/libmiroil.so.%{lomirisover}

%files -n libmiral%{miralsover}
%{_libdir}/libmiral.so.%{miralsover}

%files -n libmirserver%{mirserversover}
%license COPYING.GPL*
%doc README.md
%{_libdir}/libmirserver.so.%{mirserversover}

%files -n libmirwayland%{mirwaylandsover}
%{_libdir}/libmirwayland.so.%{mirwaylandsover}

%files -n libmirserverplatform%{mirserverplatformsover}
%license COPYING.GPL*
%doc README.md
%dir %{_libdir}/mir/server-platform
%{_libdir}/mir/server-platform/graphics-eglstream-kms.so.%{mirserverplatformsover}
%{_libdir}/mir/server-platform/graphics-gbm-kms.so.%{mirserverplatformsover}
%{_libdir}/mir/server-platform/graphics-wayland.so.%{mirserverplatformsover}
%{_libdir}/mir/server-platform/renderer-egl-generic.so.%{mirserverplatformsover}
%{_libdir}/mir/server-platform/server-virtual.so.%{mirserverplatformsover}
%{_libdir}/mir/server-platform/server-x11.so.%{mirserverplatformsover}

%files -n libmirevdev%{mirevdevsover}
%license COPYING.GPL*
%doc README.md
%{_libdir}/mir/server-platform/input-evdev.so.%{mirevdevsover}

%files test-tools
%license COPYING.GPL*
%dir %{_libdir}/mir
%dir %{_libdir}/mir/tools
%dir %{_libdir}/mir/server-platform
%{_bindir}/mir-*test*
%{_bindir}/mir_*test*
%{_libdir}/mir/tools/libmirserverlttng.so
%{_libdir}/mir/server-platform/graphics-dummy.so
%{_libdir}/mir/server-platform/input-stub.so

%files test-libs-static
%license COPYING.GPL*
%{_libdir}/libmir-test-assist.a

%files demos
%license COPYING.GPL*
%doc README.md
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/scalable
%dir %{_datadir}/icons/hicolor/scalable/apps
%{_bindir}/mir_demo_*
%{_bindir}/mir-x11-kiosk*
%{_bindir}/miral-*
%{_datadir}/applications/miral-shell.desktop
%{_datadir}/icons/hicolor/scalable/apps/spiral-logo.svg

%changelog
