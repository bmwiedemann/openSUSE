#
# spec file for package xorg-x11-server
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define pci_ids_dir %{_datadir}/X11/xorg_pci_ids
# now built separately in xwayland pkg with more recent sources (boo#1182677)
%define have_wayland 0

%define build_suid_wrapper 1

%if 0%{?build_suid_wrapper:1}
    %if 0%{?suse_version} >= 1550
      %define suid_wrapper_dir %{_bindir}
    %else
      %define build_suid_wrapper 0
    %endif
%endif

Name:           xorg-x11-server
Version:        21.1.4
Release:        0
URL:            http://xorg.freedesktop.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Summary:        X
# Source URL: http://xorg.freedesktop.org/archive/individual/xserver/
License:        MIT
Group:          System/X11/Servers/XF86_4
Source0:        xorg-server-%{version}.tar.xz
Source1:        sysconfig.displaymanager.template
Source2:        README.updates
Source3:        xorgcfg.tar.bz2
Source4:        xorg-backtrace
Source5:        50-extensions.conf
Source6:        modesetting.ids
Source7:        xkb-tmpfiles.conf
# RPM Macros to be installed. The ABI Versions will be injected by configure.
Source90:       xorg-x11-server.macros.in
# Source91 and Source99 are used to ensure proper ABI provides.
Source91:       xorg-server-provides
Source92:       pre_checkin.sh

BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(bigreqsproto) >= 1.1.0
BuildRequires:  pkgconfig(compositeproto)
BuildRequires:  pkgconfig(damageproto) >= 1.1
BuildRequires:  pkgconfig(dbus-1) >= 1.0
BuildRequires:  pkgconfig(dri) >= 7.8.0
BuildRequires:  pkgconfig(dri2proto)
BuildRequires:  pkgconfig(dri3proto)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy) >= 1.1
%if 0%{?have_wayland} == 1
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
%endif
BuildRequires:  pkgconfig(fixesproto) >= 4.1
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(fontenc)
BuildRequires:  pkgconfig(fontsproto)
BuildRequires:  pkgconfig(fontutil)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(inputproto) >= 1.9.99.902
BuildRequires:  pkgconfig(kbproto) >= 1.0.3
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxcvt)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(pciaccess) >= 0.8.0
BuildRequires:  pkgconfig(pixman-1) >= 0.24
BuildRequires:  pkgconfig(presentproto)
BuildRequires:  pkgconfig(randrproto) >= 1.5.0
BuildRequires:  pkgconfig(renderproto) >= 0.11
BuildRequires:  pkgconfig(resourceproto)
BuildRequires:  pkgconfig(scrnsaverproto)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xcb-renderutil)
BuildRequires:  pkgconfig(xcmiscproto) >= 1.2.0
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xext) >= 1.0.99.4
BuildRequires:  pkgconfig(xextproto) >= 7.1.99
BuildRequires:  pkgconfig(xf86dgaproto)
BuildRequires:  pkgconfig(xf86driproto)
BuildRequires:  pkgconfig(xf86vidmodeproto)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xfont2)
BuildRequires:  pkgconfig(xi) >= 1.2.99.1
BuildRequires:  pkgconfig(xineramaproto)
BuildRequires:  pkgconfig(xkbcomp)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xorg-macros)
BuildRequires:  pkgconfig(xp)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xprintutil)
BuildRequires:  pkgconfig(xproto) >= 7.0.31
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xres)
BuildRequires:  pkgconfig(xshmfence)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xtrans) >= 1.3.1
BuildRequires:  pkgconfig(xtst) >= 1.0.99.2
BuildRequires:  pkgconfig(xv)
### udev support (broken on openSUSE 11.2, see also bnc #589997)
%if 0%{?suse_version} >= 1130
BuildRequires:  pkgconfig(libudev) >= 143
%endif

Requires(pre):  %fillup_prereq
Requires:       pkgconfig
Requires:       xkbcomp
Recommends:     xorg-x11-fonts-core
Requires:       libpixman-1-0 >= 0.24
%(cat %{SOURCE91})
Requires:       Mesa
%if 0%{?suse_version} >= 1315
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif
Provides:       xorg-x11-server-glx
Obsoletes:      xorg-x11-server-glx

Provides:       glamor = %{version}
Provides:       glamor-egl = %{version}
Obsoletes:      glamor < %{version}
Obsoletes:      glamor < 7.6_%{version}
Obsoletes:      glamor-egl < %{version}
Obsoletes:      glamor-egl < 7.6_%{version}

Provides:       xf86-video-modesetting = %{version}
Obsoletes:      xf86-video-modesetting < %{version}
Obsoletes:      xf86-video-modesetting < 7.6_%{version}

%if 0%{?suse_version} >= 1500
Provides:       xf86-video-ast
Obsoletes:      xf86-video-ast
Provides:       xf86-video-cirrus
Obsoletes:      xf86-video-cirrus
%endif

Provides:       xorg-x11-server = 7.6_%{version}
Obsoletes:      xorg-x11-server < 7.6_%{version}
# get rid of meta packages still requiring/recommending obsolete
# drivers packages (boo#1121525)
%if 0%{?suse_version} >= 1500
Provides:       xorg-x11-driver-input = 7.6_1
Obsoletes:      xorg-x11-driver-input < 7.6_1
Provides:       xorg-x11-driver-video = 7.6_1
Obsoletes:      xorg-x11-driver-video < 7.6_1
%endif

 # Remove (also from depending driver(s)) when updating X11_ABI_VIDEODRV by updating the server package - NOTE: also remove from xorg-x11-server.macros.in !
Provides:       X11_ABI_HAS_DPMS_GET_CAPABILITIES

Requires:       xkeyboard-config

# Install it by default; otherwise we run into too much package build failures
# when Xvfb is being used for testing ...
# Unfortunately we need a requires here due to OBS not installing 'recommended'
# packages :-(
Requires:       xorg-x11-server-Xvfb

# PATCH-FEATURE-OPENSUSE n_xorg-x11-server-rpmmacros.patch dimstar@opensuse.org -- Provide RPM macros to require correct ABI Versions.
Patch1:         N_default-module-path.diff
Patch2:         N_zap_warning_xserver.diff
Patch3:         N_driver-autoconfig.diff
Patch4:         N_fix_fglrx_screendepth_issue.patch
Patch5:         n_raise_default_clients.patch
Patch6:         N_fix-dpi-values.diff
Patch7:         N_Install-Avoid-failure-on-wrapper-installation.patch
Patch8:         u_xorg-wrapper-Drop-supplemental-group-IDs.patch
Patch9:         u_xorg-wrapper-build-Build-position-independent-code.patch
Patch10:        u_xorg-wrapper-Xserver-Options-Whitelist-Filter.patch
Patch11:        n_xorg-wrapper-rename-Xorg.patch
Patch12:        n_xorg-wrapper-anybody.patch
Patch100:       u_01-Improved-ConfineToShape.patch
Patch101:       u_02-DIX-ConfineTo-Don-t-bother-about-the-bounding-box-when-grabbing-a-shaped-window.patch
# PATCH-FIX-UPSTREAM u_x86emu-include-order.patch schwab@suse.de -- Change include order to avoid conflict with system header, remove duplicate definitions

Patch104:       u_xorg-server-xdmcp.patch

Patch117:       xorg-x11-server-byte-order.patch

Patch160:       u_vesa-Add-VBEDPMSGetCapabilities-VBEDPMSGet.patch

Patch208:       u_Panning-Set-panning-state-in-xf86RandR12ScreenSetSize.patch
Patch209:       u_pci-primary-Fix-up-primary-PCI-device-detection-for-the-platfrom-bus.patch
Patch210:       u_os-connections-Check-for-stale-FDs.patch

Patch215:       u_Use-better-fallbacks-to-generate-cookies-if-arc4rand.patch

Patch1000:      n_xserver-optimus-autoconfig-hack.patch

Patch1162:      b_cache-xkbcomp-output-for-fast-start-up.patch
Patch1211:      b_0001-Prevent-XSync-Alarms-from-senslessly-calling-CheckTr.patch
Patch1222:      b_sync-fix.patch

Patch1401:      u_randr-Do-not-crash-if-slave-screen-does-not-have-pro.patch

Patch1503:      u_xfree86-Do-not-claim-pci-slots-if-fb-slot-is-already.patch

Patch1900:      u_no-lto-for-tests.patch

Patch1910:      u_modesetting-Fix-dirty-updates-for-sw-rotation.patch

Patch1920:      u_xf86-Accept-devices-with-the-hyperv_drm-driver.patch
Patch1921:      u_xf86-Accept-devices-with-the-kernels-ofdrm-driver.patch

Patch1930:      u_xfree86-activate-GPU-screens-on-autobind.patch

Patch1940:      U_xephyr-Don-t-check-for-SeatId-anymore.patch

Patch1960:      u_sync-pci-ids-with-Mesa.patch

Patch1204412:   U_xkb-proof-GetCountedString-against-request-length-at.patch
Patch1204416:   U_xkb-fix-some-possible-memleaks-in-XkbGetKbdByName.patch

Patch1205874:   U_0001-Xtest-disallow-GenericEvents-in-XTestSwapFakeInput.patch
Patch1205875:   U_0002-Xi-return-an-error-from-XI-property-changes-if-verif.patch
Patch1205876:   U_0003-Xi-avoid-integer-truncation-in-length-check-of-ProcX.patch
Patch1205877:   U_0004-Xi-disallow-passive-grabs-with-a-detail-255.patch
Patch1205878:   U_0005-Xext-free-the-screen-saver-resource-when-replacing-i.patch
Patch1205879:   U_0006-Xext-free-the-XvRTVideoNotify-when-turning-off-from-.patch
Patch1206017:   U_0007-xkb-reset-the-radio_groups-pointer-to-NULL-after-fre.patch

%description
This package contains the X.Org Server.

%package extra
Summary:        Additional Xservers Xephyr, Xnest)
Group:          System/X11/Servers/XF86_4
Requires:       Mesa
Requires:       xkbcomp
Requires:       xkeyboard-config
Recommends:     xorg-x11-fonts-core
Provides:       xorg-x11-Xnest
Obsoletes:      xorg-x11-Xnest

%description extra
This package contains additional Xservers (Xephyr, Xnest).

%package Xvfb
Summary:        Virtual Xserver Xvfb
Group:          System/X11/Servers/XF86_4
Requires:       Mesa
Requires:       xkbcomp
# Xvfb requires keyboard files as well (bnc#797124)
Requires:       xkeyboard-config
Recommends:     xorg-x11-fonts-core
Provides:       xorg-x11-Xvfb
Provides:       xorg-x11-server:/usr/bin/Xvfb
Obsoletes:      xorg-x11-Xvfb

%description Xvfb
This package contains the virtual Xserver Xvfb.

%if 0%{?have_wayland} == 1
%package wayland
Summary:        Xwayland Xserver
Group:          System/X11/Servers/XF86_4
Requires:       xkbcomp
Requires:       xkeyboard-config
Recommends:     xorg-x11-fonts-core

%description wayland
This package contains the Xserver running on the Wayland Display Server.
%endif

%if 0%{?build_suid_wrapper} == 1
%package wrapper
Summary:        Xserver SUID Wrapper
Group:          System/X11/Servers/XF86_4
PreReq:         permissions
Requires:       xorg-x11-server == %{version}

%description wrapper
This package contains an SUID wrapper for the Xserver.
%endif

%package sdk
Summary:        X
Group:          System/Libraries
Requires:       autoconf
Requires:       automake
Requires:       c_compiler
Requires:       libtool
Requires:       xorg-x11-server
Requires:       pkgconfig(fontconfig)
Requires:       pkgconfig(fontenc)
Requires:       pkgconfig(freetype2)
Requires:       pkgconfig(ice)
Requires:       pkgconfig(libdrm)
Requires:       pkgconfig(libevdev)
Requires:       pkgconfig(libudev)
Requires:       pkgconfig(mtdev)
Requires:       pkgconfig(sm)
Requires:       pkgconfig(x11)
Requires:       pkgconfig(xau)
Requires:       pkgconfig(xdmcp)
Requires:       pkgconfig(xext)
Requires:       pkgconfig(xfixes)
Requires:       pkgconfig(xkbfile)
Requires:       pkgconfig(xmu)
Requires:       pkgconfig(xorg-macros)
Requires:       pkgconfig(xp)
Requires:       pkgconfig(xpm)
Requires:       pkgconfig(xprintutil)
Requires:       pkgconfig(xrender)
Requires:       pkgconfig(xt)
Requires:       pkgconfig(xtrans)
Requires:       pkgconfig(xv)
Provides:       xorg-x11-sdk
Obsoletes:      xorg-x11-sdk
Provides:       glamor-devel = %{version}
Obsoletes:      glamor-devel < %{version}
Obsoletes:      glamor-devel < 7.6_%{version}
Provides:       xorg-x11-server-sdk = 7.6_%{version}
Obsoletes:      xorg-x11-server-sdk < 7.6_%{version}

%description sdk
This package contains the X.Org Server SDK.

%package source
Summary:        Source code of X.Org server
Group:          Development/Sources

%description source
This package contains patched sources of X.Org Server.

%prep
%setup -q -n xorg-server-%{version} -a3
# Early verification if the ABI Defines are correct. Let's not waste build cycles if the Provides are wrong at the end.
sh %{SOURCE92} --verify . %{SOURCE91}

%if 0%{?suse_version} < 1315
%patch1
%endif
%patch2 -p1
%patch3 -p0
%patch4 -p0
%patch5 -p1
%patch6 -p0
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
#
%patch100 -p1
#%patch101 -p1
%patch104 -p1
%patch117 -p1
%patch160 -p1
%patch208 -p1
%patch209 -p1
### not applicable anymore
#%patch210 -p1
%patch215 -p1
### apparently supersed by upstream
###  commit 078277e4d92f05a90c4715d61b89b9d9d38d68ea
###  Author: Dave Airlie <airlied@redhat.com>
###  Date:   Fri Aug 17 09:49:24 2012 +1000
###
###    xf86: autobind GPUs to the screen
#%patch1000 -p1

### disabled for now
#%patch1162 -p1
### disabled for now
#%patch1211 -p1
### patch222 might not be applicable anymore
#%patch1222 -p1
%patch1401 -p1
%patch1503 -p1
%patch1900 -p1
%patch1910 -p1
%patch1920 -p1
%patch1921 -p1
%patch1930 -p1
%patch1940 -p1
%patch1960 -p1
%patch1204412 -p1
%patch1204416 -p1
%patch1205874 -p1
%patch1205875 -p1
%patch1205876 -p1
%patch1205877 -p1
%patch1205878 -p1
%patch1205879 -p1
%patch1206017 -p1

%build
# We have some -z now related errors during X default startup (boo#1197994):
# - when loading modesetting: gbm_bo_get_plane_count
# - when loading fbdev: fbdevHWSave
# - when loading vesa: VBESetModeParameters
# this is directly visible on startup, so easy to test later on.
export SUSE_ZNOW=0

%global _lto_cflags %{?_lto_cflags} -ffat-lto-objects
test -e source-file-list || \
    find -L . -type f \! -name '*.orig' \! -path ./source-file-list > \
    source-file-list

autoreconf -fi
%if 0%{?pci_ids_dir:1}
export PCI_TXT_IDS_DIR=%{pci_ids_dir}
%endif
%configure CFLAGS="%{optflags} -fno-strict-aliasing" \
            --enable-xf86vidmode \
            --enable-xdmcp \
            --enable-xdm-auth-1 \
            --enable-dri \
            --enable-dri2 \
            --enable-dri3 \
            --enable-glamor \
            --enable-xnest \
            --enable-kdrive \
            --enable-kdrive-evdev \
            --enable-xephyr \
            --disable-xfake \
            --disable-xfbdev \
            --enable-record \
            --enable-xcsecurity \
            --enable-systemd-logind \
            --with-sha1=libcrypto \
            --disable-linux-acpi \
            --disable-linux-apm \
            --enable-xorg \
%if 0%{?suse_version} > 1120
            --enable-config-udev \
%endif
%if 0%{?have_wayland} == 1
            --enable-xwayland \
%else
            --disable-xwayland \
%endif
%if 0%{?build_suid_wrapper} == 1
            --enable-suid-wrapper \
            --libexecdir=%{suid_wrapper_dir} \
%endif
            --with-log-dir="/var/log" \
            --with-os-name="openSUSE" \
            --with-os-vendor="SUSE LINUX" \
            --with-fontrootdir="/usr/share/fonts" \
            --with-xkb-path="/usr/share/X11/xkb" \
            --with-xkb-output="/var/lib/xkb/compiled" \
            --with-default-font-path="/usr/share/fonts/misc:unscaled,\
/usr/share/fonts/Type1/,/usr/share/fonts/100dpi:unscaled,\
%if 0%{?suse_version} > 1210
/usr/share/fonts/75dpi:unscaled,/usr/share/fonts/ghostscript/,\
%else
/usr/share/fonts/75dpi:unscaled,/usr/share/fonts/URW/,\
%endif
/usr/share/fonts/cyrillic:unscaled,\
/usr/share/fonts/misc/sgi:unscaled,\
/usr/share/fonts/truetype/,built-ins"
make %{?_smp_mflags} V=1
make -C hw/kdrive %{?_smp_mflags}

%install
%make_install
make -C hw/kdrive install DESTDIR=%{buildroot}
# remove .la files
find %{buildroot}%{_libdir}/xorg/modules/ -name "*.la" | \
  xargs rm
install -m 644 hw/xfree86/parser/{xf86Parser.h,xf86Optrec.h} \
  %{buildroot}%{_includedir}/xorg
# bnc #632737
chmod u-s %{buildroot}%{_bindir}/Xorg
%if 0%{?pci_ids_dir:1}
%__mkdir_p %{buildroot}%{pci_ids_dir}
install -m 644 %{S:6} %{buildroot}%{pci_ids_dir}
%endif
%if 0%{?build_suid_wrapper} == 1
mv %{buildroot}%{_bindir}/Xorg \
   %{buildroot}%{_bindir}/Xorg.bin
mv %{buildroot}%{_bindir}/Xorg.sh \
   %{buildroot}%{_bindir}/Xorg
%endif
ln -snf Xorg %{buildroot}%{_bindir}/X
%if 0%{?suse_version} > 1120
%{__install} -m 644 %{S:5} %{buildroot}%{_datadir}/X11/xorg.conf.d
%endif
%if 0%{?suse_version} < 1315
mkdir -p %{buildroot}%{_libdir}/xorg/modules/updates/{fonts,input,linux,drivers,multimedia,extensions}
install -m 644 $RPM_SOURCE_DIR/README.updates %{buildroot}%{_libdir}/xorg/modules/updates
%endif
# FATE#325524
mkdir -p %{buildroot}%{_datadir}/factory/%{_localstatedir}/lib/xkb/compiled
mv %{buildroot}%{_localstatedir}/lib/xkb/compiled/README.compiled %{buildroot}%{_datadir}/factory/%{_localstatedir}/lib/xkb/compiled/
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 644 %{S:7} %{buildroot}%{_tmpfilesdir}/xkb.conf
mkdir -p %{buildroot}%{_fillupdir}
install -m 644 %_sourcedir/sysconfig.displaymanager.template \
  %{buildroot}%{_fillupdir}/sysconfig.displaymanager-%{name}
install -m 755 $RPM_SOURCE_DIR/xorg-backtrace %{buildroot}%{_bindir}/xorg-backtrace
cp %{S:90} .
./config.status --file xorg-x11-server.macros
install -D xorg-x11-server.macros %{buildroot}/usr/lib/rpm/macros.d/macros.xorg-server
%if 0%{?suse_version} >= 1315
mkdir -p %{buildroot}%{_libdir}/xorg/modules/extensions/xorg
mv  %{buildroot}%{_libdir}/xorg/modules/extensions/libglx.so \
    %{buildroot}%{_libdir}/xorg/modules/extensions/xorg/xorg-libglx.so
ln -snf %{_sysconfdir}/alternatives/libglx.so %{buildroot}%{_libdir}/xorg/modules/extensions/libglx.so
%endif

mkdir -p %{buildroot}/usr/src/xserver
xargs cp --parents --target-directory=%{buildroot}/usr/src/xserver < source-file-list
# unneeded python2 script; simply remove it (boo#1179591)
rm -f %{buildroot}/usr/src/xserver/config/fdi2iclass.py

%post
%tmpfiles_create xkb.conf
%{fillup_only -an displaymanager}
# Move SaX2 generated xorg.conf file to xorg.conf.sle11
#
# Only in very rare cases a static X configuration is still
# required on sle12. And, in some cases the migration from a
# static sle11 X configuration to a static sle12 X configuration
# is not possible at all, e.g. some video and input drivers
# are no longer available on sle12. In short, trying to migrate
# will result in more harm than benefit.
if [ -f etc/X11/xorg.conf -a ! -f etc/X11/xorg.conf.sle11 ]; then
  echo "xorg.conf exists and xorg.conf.sle11 does not"
  if grep -q "SaX generated X11 config file" etc/X11/xorg.conf; then
    echo "move SaX generated xorg.conf to xorg.conf.sle11"
    mv etc/X11/xorg.conf etc/X11/xorg.conf.sle11
    # remove dangling link (bnc#879360, comment#15)
    rm -f etc/X11/XF86Config
    # prevent %postun of NVIDIA/fglrx driver packages from restoring xorg.conf
    # backup or running sax2 as fallback to create a new xorg.conf (bcn#877315)
    rm -f etc/X11/xorg.conf.nvidia-post \
          etc/X11/xorg.conf.fglrx-post
    chmod -x usr/sbin/sax2
  fi
fi
%if 0%{?suse_version} >= 1315
%_sbindir/update-alternatives \
    --force --install %{_libdir}/xorg/modules/extensions/libglx.so libglx.so %{_libdir}/xorg/modules/extensions/xorg/xorg-libglx.so 50
%endif
exit 0

%if 0%{?suse_version} >= 1315
%postun
if [ "$1" = 0 ] ; then
   "%_sbindir/update-alternatives" --remove libglx.so %{_libdir}/xorg/modules/extensions/xorg/xorg-libglx.so
fi
%endif

%if 0%{?build_suid_wrapper} == 1
%post wrapper
%set_permissions %{suid_wrapper_dir}/Xorg.wrap

%verifyscript wrapper
%verify_permissions -e %{suid_wrapper_dir}/Xorg.wrap
%endif

%files
%defattr(-,root,root)
%if 0%{?suse_version} > 1120
%if 0%{?pci_ids_dir:1}
%dir %{pci_ids_dir}
%{pci_ids_dir}/modesetting.ids
%endif
%dir %{_datadir}/X11/xorg.conf.d
%{_datadir}/X11/xorg.conf.d/*.conf
%endif
%{_tmpfilesdir}/xkb.conf
%dir %{_localstatedir}/lib/xkb
%dir %{_localstatedir}/lib/xkb/compiled
%dir %{_libdir}/xorg
%{_libdir}/xorg/protocol.txt
%{_mandir}/man1/*
%exclude %{_mandir}/man1/Xephyr.1*
%exclude %{_mandir}/man1/Xnest.1*
%dir %{_datadir}/factory
%dir %{_datadir}/factory/var
%dir %{_datadir}/factory/var/lib
%dir %{_datadir}/factory/var/lib/xkb
%dir %{_datadir}/factory/var/lib/xkb/compiled
%{_datadir}/factory/%{_localstatedir}/lib/xkb/compiled/README.compiled
%{_bindir}/Xorg
%if 0%{?build_suid_wrapper} == 1
%{_bindir}/Xorg.bin
%endif
%{_bindir}/X

%{_bindir}/gtf
%{_libdir}/xorg/modules/
%{_mandir}/man4/*
%{_mandir}/man5/*
%{_fillupdir}/sysconfig.displaymanager-%{name}
%if 0%{?suse_version} >= 1315
%ghost %{_sysconfdir}/alternatives/libglx.so
%endif
%{_bindir}/xorg-backtrace

%if 0%{?have_wayland} == 1
%files wayland
%{_bindir}/Xwayland
%endif

%if 0%{?build_suid_wrapper} == 1
%files wrapper
%defattr(-,root,root)
%attr(4755,root,root) %{suid_wrapper_dir}/Xorg.wrap
%endif

%files extra
%defattr(-,root,root)
%{_bindir}/Xephyr
%{_bindir}/Xnest
%{_mandir}/man1/Xephyr.1*
%{_mandir}/man1/Xnest.1*

%files Xvfb
%defattr(-,root,root)
%{_bindir}/Xvfb

%files sdk
%defattr(-,root,root)
%{_includedir}/xorg/
%{_libdir}/pkgconfig/*.pc
%{_datadir}/aclocal/*.m4
/usr/lib/rpm/macros.d/macros.xorg-server

%files source
%defattr(-,root,root)
/usr/src/xserver

%changelog
