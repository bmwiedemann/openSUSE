#
# spec file for package ppsspp
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define _lto_cflags %{nil}
Name:           ppsspp
Version:        1.18.1
Release:        0
Summary:        PlayStation Portable Emulator
License:        Apache-2.0 AND BSD-1-Clause AND BSL-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-2-Clause AND BSD-3-Clause AND (BSD-2-Clause OR GPL-2.0-or-later) AND (BSD-3-Clause OR GPL-2.0-only) AND CC0-1.0 AND GPL-2.0-or-later WITH Autoconf-exception-3.0 AND GPL-3.0-or-later WITH Bison-exception-2.2 AND Libpng AND ISC AND IJG AND Zlib AND MIT AND CC-BY-4.0 AND FTL
Group:          System/Emulators/Other
URL:            https://www.ppsspp.org
Source:         https://github.com/hrydgard/ppsspp/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0:         ppsspp-1.14.4-system-png.patch
BuildRequires:  Mesa-devel
BuildRequires:  cmake >= 3.6
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glslang-devel
# Does not build with FFmpeg 5.0 yet
# https://github.com/hrydgard/ppsspp/issues/15308
BuildRequires:  libavcodec-devel < 5
BuildRequires:  pkgconfig
BuildRequires:  snappy-devel
BuildRequires:  unzip
#Desktop icon deps
BuildRequires:  update-desktop-files
BuildRequires:  wayland-devel
#Qt deps:
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpostproc)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libzip)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-common
Requires(post): hicolor-icon-theme
Requires(postun): hicolor-icon-theme
# never built for PowerPC/Arm on 20200721
ExcludeArch:    aarch64 %{arm} ppc ppc64 ppc64le s390x

%description
PPSSPP is a PSP emulator written in C++, and translates PSP CPU instructions directly into optimized x86, x64 and ARM machine code, using JIT recompilers (dynarecs).

%package headless
Summary:        PPSSPP headless
Group:          System/Emulators/Other
Requires:       %{name}-common

%description headless
PPSSPP headless build

%package qt
Summary:        PPSSPP Qt backend
Group:          System/Emulators/Other
Requires:       %{name}-common

%description qt
PPSSPP build using the Qt framework

%package common
Summary:        PPSSPP assets
Group:          System/Emulators/Other
BuildArch:      noarch

%description common
Required assets for PPSSPP GUI and assorted configuration files

%prep
%autosetup -p1

echo "// This is a generated file.

const char *PPSSPP_GIT_VERSION = \"%{version}\";

// If you don't want this file to update/recompile, change to 1.
#define PPSSPP_GIT_VERSION_NO_UPDATE 1
" > git-version.cpp

%build
# Remove cmake4 error due to not setting
# min cmake version - sflees.de
export CMAKE_POLICY_VERSION_MINIMUM=3.5

mkdir build-headless build-qt build

cd build-headless
# FIXME: you should use the %%cmake macros
cmake  .. \
        -DUSE_SYSTEM_FFMPEG="ON" \
        -DHEADLESS="ON" \
        -DCMAKE_C_FLAGS="%{optflags}" \
        -DCMAKE_CXX_FLAGS="%{optflags}" \
        -DCMAKE_BUILD_TYPE="Release|RelWithDebugInfo" \
        -DCMAKE_SKIP_RPATH="YES" \
        -Wno-dev
%make_jobs

cd ../build-qt
# FIXME: you should use the %%cmake macros
cmake  .. \
        -DUSE_SYSTEM_FFMPEG="ON" \
        -DUSING_QT_UI="ON" \
        -DCMAKE_C_FLAGS="%{optflags}" \
        -DCMAKE_CXX_FLAGS="%{optflags}" \
        -DCMAKE_BUILD_TYPE="Release|RelWithDebugInfo" \
        -DCMAKE_SKIP_RPATH="YES" \
        -Wno-dev
%make_jobs

cd ../build
# FIXME: you should use the %%cmake macros
cmake  .. \
        -DUSE_SYSTEM_FFMPEG="ON" \
        -DCMAKE_C_FLAGS="%{optflags}" \
        -DCMAKE_CXX_FLAGS="%{optflags}" \
        -DCMAKE_BUILD_TYPE="Release|RelWithDebugInfo" \
        -DCMAKE_SKIP_RPATH="YES" \
        -Wno-dev

%make_jobs

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}

#setup wrapper(s)

##----------------####----------------####----------------####----------------##

touch %{buildroot}%{_sysconfdir}/%{name}/%{name}-headless.env

cat > %{buildroot}%{_bindir}/%{name}-headless << 'EOF'
#!/bin/sh

#Mark all sourced variables for export
set -a

#Do not edit this file!
#Use %{_sysconfdir}/%{name}/%{name}-headless.env to set environment variables
. %{_sysconfdir}/%{name}/%{name}-headless.env

exec %{_libexecdir}/%{name}/%{name}-headless "$@"

EOF

##----------------####----------------####----------------####----------------##

touch %{buildroot}%{_sysconfdir}/%{name}/%{name}-qt.env

cat > %{buildroot}%{_bindir}/%{name}-qt << 'EOF'
#!/bin/sh

#Mark all sourced variables for export
set -a

#Do not edit this file!
#Use %{_sysconfdir}/%{name}/%{name}-qt.env to set environment variables
. %{_sysconfdir}/%{name}/%{name}-qt.env

exec %{_libexecdir}/%{name}/%{name}-qt "$@"

EOF

##----------------####----------------####----------------####----------------##

touch %{buildroot}%{_sysconfdir}/%{name}/%{name}.env

cat > %{buildroot}%{_bindir}/%{name} << 'EOF'
#!/bin/sh

#Mark all sourced variables for export
set -a

#Do not edit this file!
#Use %{_sysconfdir}/%{name}/%{name}.env to set environment variables
. %{_sysconfdir}/%{name}/%{name}.env

exec %{_libexecdir}/%{name}/%{name} "$@"

EOF

##----------------####----------------####----------------####----------------##

#install files
install -m 755 -D build-headless/PPSSPPHeadless %{buildroot}%{_libexecdir}/%{name}/%{name}-headless

install -m 755 -D build-qt/PPSSPPQt %{buildroot}%{_libexecdir}/%{name}/%{name}-qt

install -m 755 -D build/PPSSPPSDL %{buildroot}%{_libexecdir}/%{name}/%{name}

mv assets %{buildroot}%{_libexecdir}/%{name}/
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -m 444 -D icons/icon.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg
%suse_update_desktop_file -c %{name} PPSSPP 'PSP Emulator' %{name} %{name} System Emulator
%suse_update_desktop_file -c %{name}-qt PPSSPPQt 'PSP Emulator' %{name}-qt %{name} System Emulator

%fdupes %{buildroot}

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files headless
%license LICENSE.TXT
%attr(755,root,root) %{_bindir}/%{name}-headless
%attr(755,root,root) %{_libexecdir}/%{name}/%{name}-headless

%files qt
%license LICENSE.TXT
%attr(755, root, root) %{_bindir}/%{name}-qt
%attr(755, root, root) %{_libexecdir}/%{name}/%{name}-qt
%{_datadir}/applications/%{name}-qt.desktop

%files common
%doc README.md
%license LICENSE.TXT
%{_libexecdir}/%{name}/assets
%{_datadir}/pixmaps/%{name}.svg

%config(noreplace) %{_sysconfdir}/%{name}

%files
%license LICENSE.TXT
%dir %{_libexecdir}/%{name}
%attr(755, root, root) %{_bindir}/%{name}
%attr(755, root, root) %{_libexecdir}/%{name}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
