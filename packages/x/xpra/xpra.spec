#
# spec file for package xpra
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


%ifarch x86_64 ppc64 s390x aarch64 riscv64
%global with_pandoc 1
%endif
%bcond_with pandoc
# -----
# Comes from git tarball setup.py:
# setup.py build --verbose ...
%define xpra_ver 6.1
%define python_ver python311
%define python_short_ver 3.11
%define python_bin python3.11
# ----
%if 0%{?suse_version} >= 1550
%define ffmpeg_ver 6
%else
%define ffmpeg_ver 4
%endif

# ----
%global __requires_exclude ^typelib\\(GtkosxApplication\\)|typelib\\(GdkGLExt\\)|typelib\\(GtkGLExt\\).*$
Name:           xpra
Version:        6.1+git20240620.b8d2c4b5
Release:        0
Summary:        Remote display server for applications and desktops
License:        BSD-3-Clause AND GPL-2.0-or-later AND LGPL-3.0-or-later AND MIT
Group:          System/X11/Utilities
URL:            https://www.xpra.org/
Source0:        %{name}-%{version}.tar.gz
Source1:        xpra-icon.png
Source100:      xpra-rpmlintrc
# ----
BuildRequires:  ImageMagick
BuildRequires:  brotli
BuildRequires:  cups
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  ffmpeg-%{ffmpeg_ver}
BuildRequires:  ffmpeg-%{ffmpeg_ver}-libavcodec-devel
BuildRequires:  ffmpeg-%{ffmpeg_ver}-libavformat-devel
BuildRequires:  ffmpeg-%{ffmpeg_ver}-libavutil-devel
BuildRequires:  ffmpeg-%{ffmpeg_ver}-libswresample-devel
BuildRequires:  ffmpeg-%{ffmpeg_ver}-libswscale-devel
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
# ----
%if 0%{?suse_version} >= 1550
%define using_release "distribution-release"
BuildRequires:  distribution-release
%else
%define using_release "openSUSE-release"
BuildRequires:  openSUSE-release
%endif
# ----
BuildRequires:  pam-devel
%if %{with pandoc}
BuildRequires:  pandoc-cli
%endif
BuildRequires:  pkgconfig
BuildRequires:  %{python_ver}-Cython
BuildRequires:  %{python_ver}-devel
BuildRequires:  %{python_ver}-gobject-devel
BuildRequires:  %{python_ver}-pyxdg
BuildRequires:  %{python_ver}-setuptools
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libavcodec) >= 58
BuildRequires:  pkgconfig(libavformat) >= 58
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libswscale) >= 5
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libwebp) >= 0.4
BuildRequires:  pkgconfig(libxxhash)
# TW can do this, 15.4 can't ...
#BuildRequires:  pkgconfig(pam)
#BuildRequires:  pkgconfig(pam_misc)
BuildRequires:  pkgconfig(py3cairo)
BuildRequires:  procps-devel
BuildRequires:  qrencode-devel
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(vpx) >= 1.4.0
#BuildRequires:  pkgconfig(x264)
#BuildRequires:  pkgconfig(openh264)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  python-rpm-macros
Requires:       dbus-1-x11
Requires:       gstreamer-plugins-base
Requires:       gstreamer-plugins-good
Requires:       gstreamer-utils
%if 0%{?sle_version} && 0%{?sle_version} < 150300
Requires:       pulseaudio
%else
Requires:       pulseaudio-daemon
%endif
Requires:       pulseaudio-utils
Requires:       %{python_ver}-Pillow
Requires:       %{python_ver}-cairo
Requires:       %{python_ver}-dbus-python
Requires:       %{python_ver}-gobject
Requires:       %{python_ver}-gobject-Gdk
Requires:       %{python_ver}-gst
#Requires:       python3-lz4
#Requires:       python3-opencv
Requires:       %{python_ver}-pycups
Requires:       %{python_ver}-rencode
Requires:       shared-mime-info
Requires:       xf86-video-dummy
Requires:       xorg-x11-xauth
Requires(post): %fillup_prereq
Recommends:     lsb-release
Recommends:     pinentry
Recommends:     pulseaudio-module-x11
#Recommends:     python3-asn1crypto
#Recommends:     python3-cffi
Recommends:     %{python_ver}-cryptography
#Recommends:     python3-decorator
Recommends:     %{python_ver}-dnspython
#Recommends:     python3-idna
#Recommends:     python3-ipaddress
Recommends:     %{python_ver}-netifaces
Recommends:     %{python_ver}-opencv
Recommends:     %{python_ver}-opengl
Recommends:     %{python_ver}-opengl-accelerate
#Recommends:     python3-packaging
Recommends:     %{python_ver}-paramiko
#Recommends:     python3-pyasn1
#Recommends:     python3-pycparser
Recommends:     %{python_ver}-pyinotify
#Recommends:     python3-pynacl
#Recommends:     python3-pyparsing
Recommends:     %{python_ver}-pyxdg
#Recommends:     python3-setuptools
#Recommends:     python3-six
Recommends:     xdg-menu
# Overflow errors on 32-bit
ExcludeArch:    %ix86
%{?systemd_ordering}

%description
Xpra is "screen for X": it allows you to run X programs, usually on a remote
host, direct their display to your local machine, and then to disconnect from
these programs and reconnect from the same or another machine, without losing
any state. It gives you remote access to individual applications.

Xpra is "rootless" or "seamless": programs you run under it show up on your
desktop as regular programs, managed by your regular window manager.
Sessions can be accessed over SSH, or password protected over plain TCP sockets.
Xpra is usable over reasonably slow links and does its best to adapt to changing
network bandwidth constraints.

%prep

%setup -q
find -name '*.py' \
  -exec sed -i '1{\@^#!/usr/bin/env python@d}' {} +
find \( -name xpraforwarder \
  -o -name auth_dialog \
  -o -name xdg-open \
  -o -name xpra_signal_listener \) \
  -exec sed -i 's@#!%{_bindir}/env python3$@#!%{_bindir}/python3@' {} +
install -m0644 %{SOURCE1} -T fs/share/icons/xpra.png
# misc fixes for SUSE specific differences upstream
baselibexec=$(basename $(rpm -E '%{_libexecdir}'))
sed -e 's|__FILLUPDIR__|%{_fillupdir}|' \
  -e 's|__UNITDIR__|%{_unitdir}|' \
  -e 's|share/doc/xpra|share/doc/packages/xpra|' \
  -e "s|__LIBEXECDIR__|$baselibexec|" \
  -i setup.py

%build

### DEBUGGING
echo "ffmpeg_ver:    %ffmpeg_ver"
echo "sle_version:   %sle_version"
echo "suse_version:  %suse_version"
echo "using_release: %using_release"
#####

export CFLAGS="%{optflags}"
#%%if 0%%{?suse_version} <= 1500
export CFLAGS="$CFLAGS -Wno-error=deprecated-declarations"
#%%endif
%{python_bin} setup.py clean

### These don't appear available anymore:
#  --with-enc_ffmpeg \
#  --with-dec_avcodec2 \
#  --with-csc_swscale \
#####
### Not sure how to incorporate this from: Open H.264 Codec
#  --with-openh264 \
#####
%{python_bin} setup.py build \
  --verbose \
  --with-vpx \
  --with-webp \
  --with-Xdummy \
  --with-Xdummy_wrapper \
  --with-opengl \
  --with-service \
  --without-cuda_kernels \
  --without-nvenc \
%if !%{with pandoc}
  --without-docs \
%endif
  --without-nvfbc \
  --without-nvidia
#%%if %%{ffmpeg_ver} == 4
#  --without-nvfbc
#%%endif
#%%if %%{ffmpeg_ver} == 5
#  --without-nvfbc
#%%endif
#%%if %%{ffmpeg_ver} == 5
#  --without-nvfbc \
#  --without-strict
#%%endif

%install
%{python_bin} setup.py install \
  --skip-build \
  --root %{buildroot} \
  --prefix %{_prefix} \
  --with-service \
  --with-Xdummy \
  --with-Xdummy_wrapper \
  --without-nvidia \
%if !%{with pandoc}
  --without-docs \
%endif
  --verbose

rm -rf %{buildroot}%{_datadir}/xpra/cuda

%suse_update_desktop_file -r xpra Network RemoteAccess
%suse_update_desktop_file -r xpra-gui Network RemoteAccess
%suse_update_desktop_file -r xpra-launcher Network RemoteAccess

mkdir -pv %{buildroot}%{_sbindir}
ln -sf %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_pam_vendordir}
mv %{buildroot}%{_sysconfdir}/pam.d/xpra %{buildroot}%{_pam_vendordir}
%endif

%fdupes -s %{buildroot}

%pre
getent group xpra >/dev/null || groupadd -r xpra
mkdir -p %{_rundir}/%{name} || exit 1
%service_add_pre %{name}.service
%service_add_pre %{name}.socket
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/lib; save any old .rpmsave
for i in pam.d/xpra ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/lib, restore just created .rpmsave
for i in pam.d/xpra ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%post
%service_add_post %{name}.service
%service_add_post %{name}.socket
%fillup_only %{name}
%tmpfiles_create %{_tmpfilesdir}/xpra.conf

%preun
%service_del_preun %{name}.service
%service_del_preun %{name}.socket

%postun
%service_del_postun %{name}.service
%service_del_postun %{name}.socket

%files
%doc docs/README.md docs/CHANGELOG.md
%if %{with pandoc}
%doc %{_defaultdocdir}/xpra
%endif
%license COPYING
%dir %{_datadir}/xpra
%dir %{_sysconfdir}/xpra
%dir %{_sysconfdir}/xpra/conf.d
%dir %{_sysconfdir}/xpra/content-categories
%dir %{_sysconfdir}/xpra/content-parent
%dir %{_sysconfdir}/xpra/content-type
%dir %{_sysconfdir}/xpra/http-headers
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/xpra
%else
%dir %{_sysconfdir}/pam.d
%config(noreplace) %{_sysconfdir}/pam.d/xpra
%endif
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/xpra.conf
%config(noreplace) %{_sysconfdir}/xpra/*.conf
%config(noreplace) %{_sysconfdir}/xpra/conf.d/*.conf
%config(noreplace) %{_sysconfdir}/xpra/content-categories/*.conf
%config(noreplace) %{_sysconfdir}/xpra/content-parent/*.conf
%config(noreplace) %{_sysconfdir}/xpra/content-type/*.conf
%config(noreplace) %{_sysconfdir}/xpra/http-headers/*.txt
%config(noreplace) %{_sysconfdir}/X11/xorg.conf.d/90-xpra-virtual.conf
%{_fillupdir}/sysconfig.%{name}
%{_bindir}/run_scaled
%{_bindir}/xpra
%{_bindir}/xpra_Xdummy
%{_bindir}/xpra_launcher
%{_udevrulesdir}/71-xpra-virtual-pointer.rules
%dir %{_libexecdir}/xpra
%{_libexecdir}/xpra/auth_dialog
%{_libexecdir}/xpra/gnome-open
%{_libexecdir}/xpra/gvfs-open
%{_libexecdir}/xpra/xdg-open
%{_libexecdir}/xpra/xpra_signal_listener
%{_libexecdir}/xpra/xpra_udev_product_version
%{_sbindir}/rc%{name}
### Leap 15.[5,6] need to use >= Python3.10, so these have to be called out directly.
#%%{python3_sitearch}/xpra
%{_libdir}/%{python_bin}/site-packages/%{name}
#%%{python3_sitearch}/%%{name}-%%{xpra_ver}-py%%{python3_version}.egg-info
%{_libdir}/%{python_bin}/site-packages/%{name}-%{xpra_ver}-py%{python_short_ver}.egg-info
#####
%{_datadir}/applications/xpra-gui.desktop
%{_datadir}/applications/xpra-launcher.desktop
%{_datadir}/applications/xpra-shadow.desktop
%{_datadir}/applications/xpra.desktop
%{_datadir}/metainfo/xpra.appdata.xml
%{_datadir}/pixmaps/xpra-mdns.png
%{_datadir}/pixmaps/xpra-shadow.png
%{_datadir}/pixmaps/xpra.png
%{_datadir}/mime/packages/application-x-xpraconfig.xml
%{_datadir}/xpra/autostart.desktop
%{_datadir}/xpra/bell.wav
%{_datadir}/xpra/css
%{_datadir}/xpra/icons
%{_datadir}/xpra/images
%{_prefix}/lib/cups/backend/xpraforwarder
%{_mandir}/man1/run_scaled.1%{?ext_man}
%{_mandir}/man1/xpra.1%{?ext_man}
%{_mandir}/man1/xpra_launcher.1%{?ext_man}
%{_sysusersdir}/xpra.conf
%{_tmpfilesdir}/xpra.conf
%{_unitdir}/xpra.service
%{_unitdir}/xpra.socket
%ghost %dir %{_rundir}/xpra
%ghost %dir %{_rundir}/xpra/proxy

%changelog
