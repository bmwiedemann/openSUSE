#
# spec file for package freshplayerplugin
#
# Copyright (c) 2021 SUSE LLC
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


%bcond_with restricted
Name:           freshplayerplugin
Version:        0.3.11
Release:        0
Summary:        PPAPI2NPAPI compatibility layer
License:        MIT
Group:          Productivity/Networking/Web/Browsers
URL:            https://github.com/i-rinat/freshplayerplugin
Source:         https://github.com/i-rinat/freshplayerplugin/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE freshplayerplugin-drop-angle.patch bsc#937244 i@marguerite.su
Patch0:         freshplayerplugin-drop-angle.patch
# PATCH-FIX-UPSTREAM freshplayerplugin-fix-no-hwdec.patch -- Fix compilation with no hardware acceleration.
Patch1:         freshplayerplugin-fix-no-hwdec.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  ragel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libevent_pthreads)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(pangoft2)
BuildRequires:  pkgconfig(soxr)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
Supplements:    (browser(npapi) and flash-player-ppapi)
Conflicts:      flash-player
%if 0%{with restricted}
# Hardware accelerated decoding.
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(vdpau)
Requires:       flash-player-ppapi
Provides:       flash-plugin
%else
Recommends:     flash-player-ppapi
%endif
%ifarch armv6l || armv6hl
BuildRequires:  Mesa-libEGL-devel
BuildRequires:  Mesa-libEGL1
BuildRequires:  Mesa-libGLESv1_CM-devel
BuildRequires:  Mesa-libGLESv1_CM1
BuildRequires:  Mesa-libGLESv2-2
BuildRequires:  Mesa-libGLESv2-devel
%endif

%description
The main goal of this project is to get PPAPI (Pepper) Flash player
working in Firefox. This wrapper implements some kind of adapter
which will look like browser to PPAPI plugin and look like NPAPI
plugin for browser.

%prep
%autosetup -p1

# Enable hardware accelerated decoding for PMBS.
%if %{with restricted}
sed -i 's|^\(enable_hwdec = \)0|\11|' data/freshwrapper.conf.example
%endif

%build
%cmake \
  -DMOZPLUGIN_INSTALL_DIR=%{_libdir}/browser-plugins \
%if %{with restricted}
  -DWITH_HWDEC=1  \
%else
  -DWITH_HWDEC=0  \
%endif
  -DWITH_GLES2=ON
%make_build

%install
%cmake_install
install -Dpm 0644 data/freshwrapper.conf.example \
  %{buildroot}%{_sysconfdir}/freshwrapper.conf

%post
/sbin/ldconfig
# A tweak for Plasma 5.
if [ ! -f "%{_bindir}/plasmashell" ]; then
    sed -i 's|^\(quirk_plasma5_screensaver = \)0$|\11|' %{_sysconfdir}/freshwrapper.conf
fi

%postun -p /sbin/ldconfig

%files
%license COPYING LICENSE
%doc ChangeLog README.md
%config %{_sysconfdir}/freshwrapper.conf
%{_libdir}/browser-plugins/libfreshwrapper-flashplayer.so

%changelog
