#
# spec file for package rpcs3
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


Name:           rpcs3
Version:        0.0.26~git20230210
Release:        0
Summary:        PS3 emulator/debugger
License:        GPL-2.0-only
URL:            https://rpcs3.net
Source0:        %{name}-%{version}.tar.xz
Source1:        intel-ittapi.tar.xz
Patch1:         fix-test-files.patch
BuildRequires:  gcc-c++ >= 9
BuildRequires:  cmake(x86-64) >= 3.14.1
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libedit)
BuildRequires:  pkgconfig(libevdev)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(yaml-cpp)
BuildRequires:  pkgconfig(zlib)

#graphics backend dependencies:
#-------------------------------------------------
##opengl:
BuildRequires:  pkgconfig(glew) >= 1.13.0
BuildRequires:  pkgconfig(glu)

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
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.15.2
BuildRequires:  libqt5-qtbase-private-headers-devel >= 5.15.2
BuildRequires:  pkgconfig(Qt5Core) >= 5.15.2
BuildRequires:  pkgconfig(Qt5DBus) >= 5.15.2
BuildRequires:  pkgconfig(Qt5Multimedia) >= 5.15.2
BuildRequires:  pkgconfig(Qt5MultimediaWidgets) >= 5.15.2
BuildRequires:  pkgconfig(Qt5Network) >= 5.15.2
BuildRequires:  pkgconfig(Qt5Qml) >= 5.15.2
BuildRequires:  pkgconfig(Qt5Svg)  >= 5.15.2
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.15.2

Requires(post): hicolor-icon-theme
Requires(post): update-desktop-files
Requires(postun):hicolor-icon-theme
Requires(postun):update-desktop-files
ExclusiveArch:  x86_64

%description
An open-source PlayStation 3 emulator/debugger written in C++.

%prep
%setup -q -a 1
%patch1 -p 1

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
sed -i -e 's:FATAL_ERROR:WARNING:g' llvm/lib/ExecutionEngine/IntelJITEvents/CMakeLists.txt

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
        -DSKIP_PRECOMPILE_HEADERS="ON" \
        -DUSE_PRECOMPILED_HEADERS="OFF" \
        -DUSE_SYSTEM_CURL="ON" \
        -DUSE_SYSTEM_FFMPEG="ON" \
        -DUSE_SYSTEM_LIBPNG="ON" \
        -DUSE_SYSTEM_ZLIB="ON" \
        -DUSE_NATIVE_INSTRUCTIONS="OFF" \
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
