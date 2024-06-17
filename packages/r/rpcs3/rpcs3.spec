#
# spec file for package rpcs3
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


Name:           rpcs3
Version:        0.0.32~git20240530
Release:        0
Summary:        PS3 emulator/debugger
License:        GPL-2.0-only
URL:            https://rpcs3.net
Source0:        %{name}-%{version}.tar.xz
Source1:        intel-ittapi.tar.xz
Patch1:         fix-test-files.patch
Patch2:         fix-toolbar-color.patch
BuildRequires:  gcc-c++
BuildRequires:  (llvm-devel >= 16 with llvm-devel <= 18)
BuildRequires:  cmake(x86-64) >= 3.14.1
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  pkgconfig(zlib)

#graphics backend dependencies:
#-------------------------------------------------
##opengl:
BuildRequires:  pkgconfig(glew) >= 1.13.0
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(sdl2)

##vulkan:
BuildRequires:  pkgconfig(vulkan) >= 1.1.126
#-------------------------------------------------

#audio backend dependencies:
#-------------------------------------------------
##alsa:
BuildRequires:  pkgconfig(alsa)

##pulseaudio:
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libpulse-simple)

##openal:
BuildRequires:  pkgconfig(openal)

##faudio:
BuildRequires:  pkgconfig(sdl2)
#-------------------------------------------------

#ffmpeg dependencies
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)

#qt dependencies
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  qt6-base-private-devel
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6DBus)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6MultimediaWidgets)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Qml)
BuildRequires:  pkgconfig(Qt6Svg)
BuildRequires:  pkgconfig(Qt6Widgets)

ExclusiveArch:  x86_64

Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun): hicolor-icon-theme
Requires(postun): update-desktop-files

# Xbox One/Series controller wireless driver
Recommends:     xpadneo

%description
An open-source PlayStation 3 emulator/debugger written in C++.

%prep
%autosetup -p1 -a 1

#Generate Version Strings
GIT_VERSION=$(echo %{version} | sed 's|.*git|git~|g')

echo "// This is a generated file.

#define RPCS3_GIT_VERSION \"$GIT_VERSION\"
#define RPCS3_GIT_BRANCH \"master\"
#define RPCS3_GIT_FULL_BRANCH \"RPCS3/rpcs3/master\"

// If you don't want this file to update/recompile, change to 1.

#define RPCS3_GIT_VERSION_NO_UPDATE 1
" > %{name}/git-version.h

%build

## llvm intel-ittapi workarounds

# Work around git revision issues
#sed -i -e 's:FATAL_ERROR:WARNING:g' llvm/lib/ExecutionEngine/IntelJITEvents/CMakeLists.txt

# Fix paths
mv intel-ittapi ittapi && mkdir intel-ittapi && mv ittapi intel-ittapi/
export ITTAPI_DIR="$(pwd)/intel-ittapi"

mkdir ../%{name}_build
cd ../%{name}_build
# FIXME: you should use the %%cmake macros
%__cmake ../%{name}-%{version} \
        -DITTAPI_SOURCE_DIR="${ITTAPI_DIR}" \
        -DUSE_PCH=OFF \
        -DENABLE_PCH=OFF \
        -DSKIP_PRECOMPILE_HEADERS=ON \
        -DUSE_PRECOMPILED_HEADERS=OFF \
        -DUSE_SYSTEM_CURL=ON \
        -DUSE_SYSTEM_FFMPEG=ON \
        -DUSE_SYSTEM_LIBPNG=ON \
        -DUSE_SYSTEM_LIBUSB=ON \
        -DUSE_SYSTEM_SDL=ON \
        -DUSE_SYSTEM_ZLIB=ON \
        -DUSE_NATIVE_INSTRUCTIONS=OFF \
        -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
        -DCMAKE_INSTALL_LIBEXEC="%{_libexecdir}" \
        -DCMAKE_BUILD_TYPE="Release" \
        -DCMAKE_SKIP_RPATH="YES"

%make_jobs

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%install
cd ../%{name}_build
%make_install

%files
%doc README.md
%license LICENSE

%attr(755, root, root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/%{name}
%{_datadir}/metainfo/%{name}.metainfo.xml

%changelog
