#
# spec file for package lmms
#
# Copyright (c) 2022 SUSE LLC
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


# The revision numbers for rpmalloc and qt5-x11embed come from accessing them via
# https://github.com/LMMS/lmms/tree/v%%{version}/src/3rdparty/qt5-x11embed and
# https://github.com/LMMS/lmms/tree/v1.2.1/src/3rdparty/rpmalloc/rpmalloc (two directories not a mistake)
%define rpmallocrev b5bdc18051bb74a22f0bde4bcc90b01cf590b496
%define qt5x11embedrev 022b39a1d496d72eb3e5b5188e5559f66afca957
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150300
%bcond_with  wine
%endif
%bcond_without  carla
%bcond_without  crippled_stk
Name:           lmms
Version:        1.2.2
Release:        0
Summary:        Linux MultiMedia Studio
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Midi
URL:            https://lmms.io/
Source0:        https://github.com/LMMS/lmms/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/mjansson/rpmalloc/archive/%{rpmallocrev}.tar.gz
Source2:        https://github.com/lukas-w/qt5-x11embed/archive/%{qt5x11embedrev}.tar.gz
%if %{with wine}
Source3:        lmms-warning
%endif
# PATCH-FIX-OPENSUSE Patch for providing proper return code in a function
Patch0:         lmms-1.2.0-return.patch
%if %{with crippled_stk}
# PATCH-FIX-OPENSUSE Some parts cannot be build because stk misses some files due to legal issues (bnc#761147)
Patch1:         lmms-1.2.0-crippled_stk.patch
%endif
# PATCH-FIX-UPSTREAM Fix plugin library search path, testing an upstream proposal
Patch2:         lmms-1.2.0-libdir.patch
Patch3:         lmms-rpmalloc-fpic.patch
# PATCH-FIX-UPSTREAM -- Fix build with recent carla releases
Patch4:         lmms-1.2.2-carla_defines.patch
BuildRequires:  bash-completion
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  filesystem
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libQt5Core-private-headers-devel
BuildRequires:  libQt5Gui-private-headers-devel
BuildRequires:  libQt5Widgets-private-headers-devel
BuildRequires:  libstk-devel
BuildRequires:  pkgconfig
BuildRequires:  sndio-devel
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3f) >= 3.0.0
BuildRequires:  pkgconfig(fluidsynth) >= 1.0.7
BuildRequires:  pkgconfig(gig)
BuildRequires:  pkgconfig(jack) >= 0.77
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(libmp3lame)
%else
BuildRequires:  libmp3lame-devel
%endif
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(portaudiocpp)
BuildRequires:  pkgconfig(samplerate) >= 0.1.8
BuildRequires:  pkgconfig(sdl)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  pkgconfig(sndfile) >= 1.0.11
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-util)
# SECTION Zynaddsubfx
BuildRequires:  fltk-devel
BuildRequires:  pkgconfig(mxml)
BuildRequires:  pkgconfig(ntk)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
# /SECTION
%if %{with carla}
# also needed (contains libcarla_standalone2 library)
# to enable internal Carla plugin host
BuildRequires:  carla
BuildRequires:  pkgconfig(carla-native-plugin)
%requires_eq    carla
%endif
%if %{with wine}
#Extra packages
BuildRequires:  gcc-c++-32bit
BuildRequires:  libstdc++-devel-32bit
BuildRequires:  wine
BuildRequires:  wine-devel
BuildRequires:  wine-devel-32bit
#!BuildIgnore:  sane-backends-32bit
%endif
ExclusiveArch:  x86_64

%description
LMMS is a free cross-platform music studio which allows you to produce music
with your computer. This includes the creation of melodies and beats, the
synthesis and mixing of sounds, and arranging of samples.
%if %{with wine}
You need to install lmms-vst for VST plugins

%package vst
Summary:        Wine dependent VST plugins
Group:          Productivity/Multimedia/Sound/Midi
Requires:       %{name} = %{version}
Requires:       wine
Obsoletes:      %{name} < 1.2.1

%description vst
LMMS is a free cross-platform music studio which allows you to produce music
with your computer. This includes the creation of melodies and beats, the
synthesis and mixing of sounds, and arranging of samples.
This package contains the wine dependent VST plugins
%endif

%package devel
Summary:        Headers to create LMMS plugins
Group:          Development/Libraries/C and C++

%description devel
Headers that provide access to the LMMS features. Install it if you plan to
create a LMMS plugin.

%prep
%autosetup -p1

pushd src/3rdparty
rm -r qt5-x11embed
tar -xf %{SOURCE2} && mv qt5-x11embed-%{qt5x11embedrev} qt5-x11embed
pushd qt5-x11embed
rm -r 3rdparty/ECM
ln -s %{_datadir}/ECM 3rdparty/ECM
popd
cd rpmalloc && rm -r rpmalloc && tar -xf %{SOURCE1} && mv rpmalloc-%{rpmallocrev} rpmalloc
popd

%build
export PATHBU=$PATH
%if %{with wine}
# Remove -m64 from CFLAGS, it causes VST build failure.
export CFLAGS="-O2 -g -fmessage-length=0 -D_FORTIFY_SOURCE=2 -fstack-protector -funwind-tables -fasynchronous-unwind-tables"
%define optflags $CFLAGS
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150300
#Add workaround for boo#1179734 to create the missing libwine.so symlink
export WINELIB=$(find %{_libdir} -name libwine.so.?)
export WINELIB32=$(find %{_prefix}/lib -name libwine.so.?)
export WINELINK=$(echo $WINELIB | cut -d . -f 1,2)
if ! test -e ${WINELINK}
then
mkdir -p $HOME/%{_lib}/wine
mkdir -p $HOME/lib/wine
pushd $HOME/%{_lib}/wine
ln -sf ${WINELIB} libwine.so
cd ../../lib/wine
ln -sf ${WINELIB32} libwine.so
export PATH="$PATH:$HOME/%{_lib}/:$HOME/lib"
popd
fi
%endif
%endif

export CFLAGS="$CFLAGS -fPIC"

# https://docs.lmms.io/user-manual/getting-started/troubleshooting?q=midi+keyboards#i-compiled-lmms-with-vst-support-but-it-doesnt-work-at-all
export CFLAGS="$CFLAGS -fno-omit-frame-pointer"
export CXXFLAGS="%optflags -fno-omit-frame-pointer"

%cmake \
%if %{with wine}
  -DCMAKE_CXX_FLAGS:STRING="$CXXFLAGS -D__WIDL_objidl_generated_name_0000000C=""" \
%else
  -DWANT_VST_NOWINE:BOOL=ON \
%endif
  -DWANT_QT5=ON \
  -DCMAKE_SHARED_LINKER_FLAGS="" \
  -DCMAKE_EXE_LINKER_FLAGS:STRING="$LDFLAGS -pie" \
%if !%{with carla}
  -DWANT_CARLA:BOOL=OFF \
%endif
  -Wno-dev

export PATH=$PATHBU
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150300
sed -i 's/\/wine\/libwinecrt0.a//' plugins/vst_base/CMakeFiles/vstbase.dir/build.make
sed -i 's/libwinecrt0.a\/wine\///' plugins/vst_base/CMakeFiles/vstbase.dir/build.make
%endif

%cmake_build

%install
%cmake_install

mkdir -p '%{buildroot}%{_defaultdocdir}/lmms/'

# remove unneeded static helper library from install
rm %{buildroot}%{_libdir}/libqx11embedcontainer.a

# workaround: copy bash completion manually into install dir because it fails during cmake install
mkdir -p %{buildroot}/%{_datadir}/bash-completion/completions
cp %{_builddir}/lmms*/doc/bash-completion/lmms %{buildroot}%{_datadir}/bash-completion/completions/lmms

%fdupes -s %{buildroot}/%{_datadir}

%if %{with wine}
mkdir -p %{buildroot}%{_localstatedir}/adm/update-messages/
# Install lmms-warning
cp %{SOURCE3}  %{buildroot}%{_localstatedir}/adm/update-messages/
%endif

%files
%doc doc/AUTHORS README.md INSTALL.txt
%license LICENSE.txt
%{_bindir}/lmms
%{_mandir}/man1/lmms.1%{?ext_man}
%{_libdir}/lmms/
%{_datadir}/lmms/
%{_datadir}/applications/lmms.desktop
%{_datadir}/icons/hicolor/*
%{_datadir}/mime/packages/lmms.xml
%{_datadir}/bash-completion/completions/lmms

%if %{with wine}
%{_localstatedir}/adm/update-messages/%{name}-warning
%exclude %{_libdir}/lmms/RemoteVstPlugin
%exclude %{_libdir}/lmms/RemoteVstPlugin.exe.so
%exclude %{_libdir}/lmms/libvsteffect.so

%post
cat %{_localstatedir}/adm/update-messages/%{name}-warning

%files vst
%{_libdir}/lmms/RemoteVstPlugin
%{_libdir}/lmms/RemoteVstPlugin.exe.so
%{_libdir}/lmms/libvsteffect.so
%endif

%files devel
%defattr(0644,root,root,0755)
%{_includedir}/lmms/

%changelog
