#
# spec file for package mupen64plus
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


Name:           mupen64plus
Version:        2.5.9
Release:        0
Summary:        Plugin-Based Nintendo 64 Emulator
License:        GPL-2.0-or-later
URL:            https://mupen64plus.org
Source0:        https://github.com/%{name}/%{name}-core/releases/download/%{version}/%{name}-bundle-src-%{version}.tar.gz
Source1:        %{name}.rpmlintrc
Patch0:         %{name}-fix-cflags.patch
Patch1:         %{name}-use-system-font.patch
Patch2:         %{name}-binutils-2_29.patch
Patch3:         %{name}-libboost-1.85.patch
Patch4:         %{name}-ppc64le-aarch64.patch
Patch5:         don-t-put-globals-in-include-files.patch
BuildRequires:  binutils-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_system-devel
BuildRequires:  lirc-devel
BuildRequires:  nasm
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(zlib)
ExcludeArch:    s390x

%description
Mupen64Plus is a plugin-based N64 emulator which is capable of accurately
playing many games. It includes four MIPS R4300 CPU emulators, with dynamic
recompilers for 32-bit x86 and 64-bit amd64 systems.  It supports plugins for
audio, graphical rendering (RDP), the signal co-processor (RSP), and input.

%package -n lib%{name}2
Summary:        Shared Library Interface to the Mupen64plus Nintendo 64 Emulator
Requires:       dejavu

%description -n lib%{name}2
Mupen64Plus is a plugin-based N64 emulator which is capable of accurately
playing many games. It includes four MIPS R4300 CPU emulators, with dynamic
recompilers for 32-bit x86 and 64-bit amd64 systems.  It supports plugins for
audio, graphical rendering (RDP), the signal co-processor (RSP), and input.

This package contains the shared library interface for Mupen64plus frontends.

%package -n lib%{name}-devel
Summary:        Include Files for Mupen64plus Development
Requires:       lib%{name}2 = %{version}

%description -n lib%{name}-devel
This package contains all necessary include files to develop frontends against
the Mupen64plus shared library interface.

%package ui-console
Summary:        Command Line Frontend for the Mupen64plus Nintendo 64 Emulator
Requires:       %{name}-plugin-audio
Requires:       %{name}-plugin-input
Requires:       %{name}-plugin-rsp
Requires:       %{name}-plugin-video
Requires:       lib%{name}2 = %{version}

%description ui-console
Mupen64Plus is a plugin-based N64 emulator which is capable of accurately
playing many games.

This package contains a command line frontend.

%package plugin-audio-sdl
Summary:        SDL Audio Plugin for the Mupen64plus Nintendo 64 Emulator
Provides:       %{name}-plugin-audio

%description plugin-audio-sdl
This package contains the SDL audio plugin for the Mupen64plus Nintendo 64
Emulator.

%package plugin-input-sdl
Summary:        SDL Input Plugin for the Mupen64plus Nintendo 64 Emulator
Provides:       %{name}-plugin-input

%description plugin-input-sdl
This package contains the SDL input plugin for the Mupen64plus Nintendo 64
Emulator. It has LIRC Infrared remote control interface and Rumble Pak support.

%package plugin-rsp-hle
Summary:        RSP High-Level Emulation Plugin For the Mupen64plus Nintendo 64 Emulator
Provides:       %{name}-plugin-rsp

%description plugin-rsp-hle
This package contains the RSP High-Level emulation plugin for the Mupen64plus
Nintendo 64 Emulator.

%package plugin-video-rice
Summary:        Rice Video Plugin for the Mupen64plus Nintendo 64 Emulator
Provides:       %{name}-plugin-video

%description plugin-video-rice
This package contains the Rice Video Plugin for the Mupen64plus Nintendo 64
Emulator. It provides a high-level graphics emulation with support for
high-resolution texture support.

%package plugin-video-glide64mk2
Summary:        Glide64mk2 Video Plugin for the Mupen64plus Nintendo 64 Emulator
Provides:       %{name}-plugin-video

%description plugin-video-glide64mk2
This package contains the Glide64mk2 Video Plugin for the Mupen64plus
Nintendo 64 Emulator which provides high-level graphics emulation.

%prep
%autosetup -p1 -n %{name}-bundle-src-%{version}

%build
%make_build -C source/%{name}-core/projects/unix all \
    OPTFLAGS="%{optflags}" \
%ifnarch x86_64
    NO_ASM=1 \
%endif
%ifarch armv7hl
    VFP_HARD=1 \
%endif
    PIC=1 \
    PREFIX=%{_prefix} \
    SHAREDIR=%{_datadir}/%{name}2 \
    LIBDIR=%{_libdir} \
    LIRC=1 \
    V=1
%make_build -C source/%{name}-ui-console/projects/unix all \
    OPTFLAGS="%{optflags}" \
    PIC=1 \
    PIE=1 \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir} \
    SHAREDIR=%{_datadir}/%{name}2 \
    COREDIR=%{_libdir}/ \
    PLUGINDIR=%{_libdir}/%{name}2 \
    V=1
%make_build -C source/%{name}-audio-sdl/projects/unix all \
    OPTFLAGS="%{optflags}" \
    PIC=1 \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir} \
    PLUGINDIR=%{_libdir}/%{name}2 \
    V=1
%make_build -C source/%{name}-input-sdl/projects/unix all \
    OPTFLAGS="%{optflags}" \
    PIC=1 \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir} \
    SHAREDIR=%{_datadir}/%{name}2 \
    PLUGINDIR=%{_libdir}/%{name}2 \
    V=1
%make_build -C source/%{name}-rsp-hle/projects/unix all \
    OPTFLAGS="%{optflags}" \
    PIC=1 \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir} \
    PLUGINDIR=%{_libdir}/%{name}2 \
    V=1
%make_build -C source/%{name}-video-rice/projects/unix all \
%ifnarch x86_64
    OPTFLAGS="%{optflags}" \
    NO_ASM=1 \
%else
    OPTFLAGS="%{optflags} -msse" \
%endif
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir} \
    SHAREDIR=%{_datadir}/%{name}2 \
    PLUGINDIR=%{_libdir}/%{name}2 \
    PIC=1 \
    V=1
%make_build -C source/%{name}-video-glide64mk2/projects/unix all \
%ifnarch x86_64
    OPTFLAGS="%{optflags} -DNOSSE" \
    NO_ASM=1 \
%else
    OPTFLAGS="%{optflags} -mmmx -msse" \
%endif
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir} \
    SHAREDIR=%{_datadir}/%{name}2 \
    PLUGINDIR=%{_libdir}/%{name}2 \
    PIC=1 \
    V=1

%install
make -C source/%{name}-core/projects/unix install \
    OPTFLAGS="%{optflags}" \
%ifnarch x86_64
    NO_ASM=1 \
%endif
    DESTDIR=%{buildroot} \
    PREFIX=%{_prefix} \
    SHAREDIR=%{_datadir}/%{name}2 \
    LIBDIR=%{_libdir} \
    LIRC=1 \
    INSTALL_STRIP_FLAG= \
    V=1
(
    cd %{buildroot}%{_libdir}
    ln -s lib%{name}.so.2.0.0 lib%{name}.so
)
make -C source/%{name}-ui-console/projects/unix install \
    DESTDIR=%{buildroot} \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir} \
    SHAREDIR=%{_datadir}/%{name}2 \
    COREDIR=%{_libdir}/ \
    PLUGINDIR=%{_libdir}/%{name}2 \
    INSTALL_STRIP_FLAG= \
    V=1
rm %{buildroot}%{_datadir}/%{name}2/font.ttf
make -C source/%{name}-audio-sdl/projects/unix install \
    DESTDIR=%{buildroot} \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir} \
    PLUGINDIR=%{_libdir}/%{name}2 \
    INSTALL_STRIP_FLAG= \
    V=1
make -C source/%{name}-input-sdl/projects/unix install \
    DESTDIR=%{buildroot} \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir} \
    SHAREDIR=%{_datadir}/%{name}2 \
    PLUGINDIR=%{_libdir}/%{name}2 \
    INSTALL_STRIP_FLAG= \
    V=1
make -C source/%{name}-rsp-hle/projects/unix install \
    DESTDIR=%{buildroot} \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir} \
    PLUGINDIR=%{_libdir}/%{name}2 \
    INSTALL_STRIP_FLAG= \
    V=1
make -C source/%{name}-video-rice/projects/unix install \
    DESTDIR=%{buildroot} \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir} \
    SHAREDIR=%{_datadir}/%{name}2 \
    PLUGINDIR=%{_libdir}/%{name}2 \
    INSTALL_STRIP_FLAG= \
    V=1
make -C source/%{name}-video-glide64mk2/projects/unix install \
    DESTDIR=%{buildroot} \
    PREFIX=%{_prefix} \
    LIBDIR=%{_libdir} \
    SHAREDIR=%{_datadir}/%{name}2 \
    PLUGINDIR=%{_libdir}/%{name}2 \
    INSTALL_STRIP_FLAG= \
    V=1

%post -n lib%{name}2 -p /sbin/ldconfig
%postun -n lib%{name}2 -p /sbin/ldconfig

%files -n lib%{name}2
%license source/%{name}-core/LICENSES
%doc source/%{name}-core/{README,RELEASE}
%dir %{_datadir}/%{name}2
%dir %{_libdir}/%{name}2
%attr(0755,root,root) %{_libdir}/lib%{name}.so.*
%{_datadir}/%{name}2/{%{name}.ini,mupencheat.txt}

%files -n lib%{name}-devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so

%files ui-console
%license source/%{name}-ui-console/LICENSES
%doc source/%{name}-ui-console/{README,RELEASE}
%{_mandir}/man?/%{name}.?%{?ext_man}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.{png,svg}

%files plugin-audio-sdl
%doc source/%{name}-audio-sdl/{LICENSES,RELEASE}
%{_libdir}/%{name}2/%{name}-audio-sdl.so

%files plugin-input-sdl
%license source/%{name}-input-sdl/LICENSES
%doc source/%{name}-input-sdl/{AUTHORS,COPYING,README.md,RELEASE}
%{_datadir}/%{name}2/InputAutoCfg.ini
%{_libdir}/%{name}2/%{name}-input-sdl.so

%files plugin-rsp-hle
%license source/%{name}-rsp-hle/LICENSES
%doc source/%{name}-rsp-hle/RELEASE
%{_libdir}/%{name}2/%{name}-rsp-hle.so

%files plugin-video-rice
%license source/%{name}-video-rice/LICENSES
%doc source/%{name}-video-rice/{README,RELEASE}
%{_datadir}/%{name}2/RiceVideoLinux.ini
%{_libdir}/%{name}2/%{name}-video-rice.so

%files plugin-video-glide64mk2
%license source/%{name}-video-glide64mk2/doc/{fxt1-license,gpl-license}
%{_datadir}/%{name}2/Glide64mk2.ini
%{_libdir}/%{name}2/%{name}-video-glide64mk2.so

%changelog
