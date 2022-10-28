#
# spec file for package plymouth
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


# plymouth's X11 renderer adds many GTK3 packages to the build cycle,
# it is not used in the production environment.
%bcond_with x11_renderer

%global soversion 5

Name:           plymouth
Version:        22.02.122+94.4bd41a3
Release:        0
Summary:        Graphical Boot Animation and Logger
License:        GPL-2.0-or-later
Group:          System/Base
URL:            https://www.freedesktop.org/wiki/Software/Plymouth
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE plymouth-dracut-path.patch tittiatcoke@gmail.com -- Prefix is /usr/sbin and /usr/bin
Patch0:         plymouth-dracut-path.patch
# PATCH-FIX-OPENSUSE plymouth-some-greenish-openSUSE-colors.patch bnc#886148 fcrozat@suse.com -- To use suse colors in tribar.
Patch1:         plymouth-some-greenish-openSUSE-colors.patch
# PATCH-FIX-UPSTREAM plymouth-manpages.patch bnc#871419 idoenmez@suse.de -- Fix man page installation
Patch2:         plymouth-manpages.patch
# PATCH-FIX-OPENSUSE plymouth-disable-fedora-logo.patch qzhao@suse.com -- Disable the fedora logo reference which is not in openSUSE.
Patch3:         plymouth-disable-fedora-logo.patch
# PATCH-FIX-OPENSUSE plymouth-only_use_fb_for_cirrus_bochs.patch bnc#888590 boo#1172028 bsc#1181913 fvogt@suse.com -- Force fb for cirrus and bochs, force drm otherwise. replace removal of framebuffer driver and plymouth-ignore-cirrusdrm.patch with single patch.
Patch4:         plymouth-only_use_fb_for_cirrus_bochs.patch
# PATCH-FIX-OPENSUSE plymouth-keep-KillMode-none.patch bsc#1177082 bsc#1184087 boo#1182145 qzhao@suse.com -- Keep the plymouth-start.service KillMode=none.
Patch5:         plymouth-keep-KillMode-none.patch
# PATCH-FIX-OPENSUSE plymouth-install-label-library-and-font-file-to-initrd.patch boo#1183425 boo#1184309 qzhao@suse.com -- Pack label plugin and font into initram to ensure notice info could successfully show when partition encrypted.
Patch6:         plymouth-install-label-library-and-font-file-to-initrd.patch
# PATCH-FIX-OPENSUSE plymouth-quiet-dracut-build-info.patch bsc#1189613 qzhao@suse.com -- Hide unuseful output when re-generate initrd.
Patch7:         plymouth-quiet-dracut-build-info.patch
# PATCH-FIX-OPENSUSE plymouth-watermark-config.patch bsc#1189613 qzhao@suse.com -- Add two-step water mark config support.
Patch8:         plymouth-watermark-config.patch
# PATCH-FIX-OPENSUSE plymouth-log-on-default.patch bsc#1193736 qzhao@suse.com -- Enable plymouth log by default, help to resolve random appear problems.
Patch9:         plymouth-log-on-default.patch
# PATCH-FIX-OPENSUSE plymouth-screen-twice-scale-on-160DPI-higher.patch boo#1183425 boo#1184309 qzhao@suse.com -- When DPI > 160, screen will scale output twice.
Patch10:        plymouth-screen-twice-scale-on-160DPI-higher.patch
# PATCH-FIX-OPENSUSE plymouth-crash-avoid-on-keyboard-remove-input-handler.patch bsc#1193736 qzhao@suse.com -- Confirm keyboard handler list not NULL before release memory to avoid crash.
Patch11:        plymouth-crash-avoid-on-keyboard-remove-input-handler.patch
BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  pkgconfig
%if 0%{suse_version} >= 1550
# regenerate_initrd_post moved to rpm-config-SUSE:initrd.macros
BuildRequires:  rpm-config-SUSE >= 0.g11
%else
BuildRequires:  suse-module-tools
%endif
BuildRequires:  intltool
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libsystemd) >= 186
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango) >= 1.21.0
# needed for systemd-tty-ask-password-agent
BuildRequires:  pkgconfig(systemd) >= 186
%if %{with x11_renderer}
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14.0
%endif
Recommends:     %{name}-lang
Requires:       %{name}-branding
Requires:       systemd >= 186
Requires(post): coreutils
Requires(post): plymouth-scripts = %{version}
Requires(postun):coreutils
Suggests:       plymouth-plugin-label
Provides:       bootsplash = 3.5
Obsoletes:      bootsplash < 3.5
Provides:       systemd-plymouth = 44-10.2
Obsoletes:      systemd-plymouth <= 44-10.1

%description
Plymouth provides an attractive graphical boot animation in
place of the text messages that normally get shown. Text
messages are instead redirected to a log file for viewing
after boot.
%lang_package

%package -n libply%{soversion}
Summary:        Plymouth core library
Group:          System/Libraries

%description -n libply%{soversion}
This package contains the libply library used by Plymouth.

%package -n libply-boot-client%{soversion}
Summary:        Plymouth core library
Group:          System/Libraries

%description -n libply-boot-client%{soversion}
This package contains the libply-boot-client library used by Plymouth.

%package -n libply-splash-core%{soversion}
Summary:        Plymouth core library
Group:          System/Libraries

%description -n libply-splash-core%{soversion}
This package contains the libply-splash-core library
used by graphical Plymouth splashes.

%package -n libply-splash-graphics%{soversion}
Summary:        Plymouth graphics libraries
Group:          System/Libraries
BuildRequires:  libpng-devel

%description -n libply-splash-graphics%{soversion}
This package contains the libply-splash-graphics library
used by graphical Plymouth splashes.

%package branding-upstream
Summary:        Default configuration file and branding from the Plymouth upstream
Group:          System/Base
Provides:       %{name}-branding = %{version}
Conflicts:      %{name}-branding
BuildArch:      noarch

%description branding-upstream
This package contains the /usr/share/plymouthd.defaults which contains the basic
settings and branding from the upstream.

%package devel
Summary:        Libraries and headers for writing Plymouth splash plugins
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
%if %{with x11_renderer}
Requires:       %{name}-x11-renderer = %{version}
%endif
Requires:       libply%{soversion} = %{version}
Requires:       libply-boot-client%{soversion} = %{version}
Requires:       libply-splash-core%{soversion} = %{version}
Requires:       libply-splash-graphics%{soversion} = %{version}
Requires:       pkgconfig

%description devel
This package contains the libply and libplybootsplash libraries
and headers needed to develop 3rd party splash plugins for Plymouth.

%package dracut
Summary:        Plymouth related utilities for dracut
Group:          System/Base
Requires:       %{name} = %{version}
Supplements:    (plymouth and dracut)
BuildArch:      noarch

%description dracut
This package contains utilities that integrate dracut with Plymouth

%package x11-renderer
Summary:        Plymouth X11 renderer
Group:          System/Base
Requires:       %{name} = %{version}

%description x11-renderer
This package provides the X11 renderer which allows to test plymouth
behavior on environments with a valid DISPLAY.

%package scripts
Summary:        Plymouth related scripts
Group:          System/Base
Requires:       awk
Requires:       dracut
Requires:       grep
Requires:       sed
Requires(pre):  %{name} = %{version}
BuildArch:      noarch

%description scripts
This package contains scripts that help integrate Plymouth with
the system.

%package plugin-label
Summary:        Plymouth label plugin
Group:          System/Base
Requires:       libply-splash-graphics%{soversion} = %{version}

%description plugin-label
This package contains the label control plugin for
Plymouth. It provides the ability to render text on
graphical boot splashes using pango and cairo.

%package plugin-label-ft
Summary:        Plymouth FreeType label plugin
Group:          System/Base
Requires:       fontconfig
Requires:       libply-splash-graphics%{soversion} = %{version}

%description plugin-label-ft
This package contains the label control plugin for
Plymouth. It provides the ability to render text on
graphical boot splashes using FreeType

%package plugin-fade-throbber
Summary:        Plymouth "Fade-Throbber" plugin
Group:          System/Base
Requires:       libply%{soversion} = %{version}
Requires:       libply-splash-core%{soversion} = %{version}
Requires:       libply-splash-graphics%{soversion} = %{version}

%description plugin-fade-throbber
This package contains the "Fade-In" boot splash plugin for
Plymouth. It features a centered image that fades in and out
while other images pulsate around during system boot up.

%package plugin-space-flares
Summary:        Plymouth "space-flares" plugin
Group:          System/Base
Requires:       %{name}-plugin-label = %{version}
Requires:       libply%{soversion} = %{version}
Requires:       libply-splash-core%{soversion} = %{version}
Requires:       libply-splash-graphics%{soversion} = %{version}

%description plugin-space-flares
This package contains the "space-flares" boot splash plugin for
Plymouth. It features a corner image with animated flares.

%package plugin-two-step
Summary:        Plymouth "two-step" plugin
Group:          System/Base
Requires:       libply%{soversion} = %{version}
Requires:       libply-splash-core%{soversion} = %{version}
Requires:       libply-splash-graphics%{soversion} = %{version}
Requires:       plymouth-plugin-label = %{version}

%description plugin-two-step
This package contains the "two-step" boot splash plugin for
Plymouth. It features a two phased boot process that starts with
a progressing animation synced to boot time and finishes with a
short, fast one-shot animation.

%package plugin-script
Summary:        Plymouth "script" plugin
Group:          System/Base
Requires:       libply%{soversion} = %{version}
Requires:       libply-splash-core%{soversion} = %{version}
Requires:       libply-splash-graphics%{soversion} = %{version}

%description plugin-script
This package contains the "script" boot splash plugin for
Plymouth. It features an extensible, scriptable boot splash
language that simplifies the process of designing custom
boot splash themes.

%package plugin-tribar
Summary:        Plymouth "script" plugin
Group:          System/Base
Requires:       libply%{soversion} = %{version}
Requires:       libply-splash-core%{soversion} = %{version}
Requires:       libply-splash-graphics%{soversion} = %{version}

%description plugin-tribar
This package contains the "tribar" boot splash plugin for
Plymouth. It features an extensible, scriptable boot splash
language that simplifies the process of designing custom
boot splash themes.

%package theme-fade-in
Summary:        Plymouth "Fade-In" theme
Group:          System/Base
Requires:       %{name}-plugin-fade-throbber = %{version}
Requires:       plymouth-plugin-label = %{version}
Requires(post): %{name}-scripts
BuildArch:      noarch

%description theme-fade-in
This package contains the "Fade-In" boot splash theme for
Plymouth. It features a centered logo that fades in and out
while stars twinkle around the logo during system boot up.

%package theme-spinfinity
Summary:        Plymouth "Spinfinity" theme
Group:          System/Base
Requires(post): %{name}-scripts
Requires(pre):  %{name}
BuildArch:      noarch

%description theme-spinfinity
This package contains the "Spinfinity" boot splash theme for
Plymouth. It features a centered logo and animated spinner that
spins in the shape of an infinity sign.

%package theme-spinner
Summary:        Plymouth "Spinner" theme
Group:          System/Base
Requires:       %{name}-plugin-two-step = %{version}
Requires(post): %{name}-scripts
BuildArch:      noarch

%description theme-spinner
This package contains the "spinner" boot splash theme for
Plymouth.

%package theme-solar
Summary:        Plymouth "Solar" theme
Group:          System/Base
Requires:       %{name}-plugin-space-flares = %{version}
Requires(post): %{name}-scripts
BuildArch:      noarch

%description theme-solar
This package contains the "Solar" boot splash theme for
Plymouth. It features a blue flamed sun with animated solar flares.

%package theme-tribar
Summary:        Plymouth "Tribar" theme
Group:          System/Base
Requires:       %{name}-plugin-tribar = %{version}
Requires(post): %{name}-scripts
BuildArch:      noarch

%description theme-tribar
This package contains the "Tribar" boot splash theme for
Plymouth

%package theme-script
Summary:        Plymouth "Script" theme
Group:          System/Base
Requires:       %{name}-plugin-script = %{version}
Requires(post): %{name}-scripts
BuildArch:      noarch

%description theme-script
This package contains the "script" boot splash theme for
Plymouth. It is a simple example theme the uses the "script"
plugin.

%package theme-bgrt
Summary:        Plymouth "bgrt" theme
# Uses images from spinner theme
Group:          System/Base
Requires:       %{name}-plugin-two-step = %{version}
Requires:       %{name}-theme-spinner = %{version}
Requires(post): %{name}-scripts
BuildArch:      noarch

%description theme-bgrt
This package contains the "bgrt" boot splash theme for
Plymouth.

%prep
%setup -q
%autopatch -p1
autoreconf -ivf

%build
%configure \
           --enable-systemd-integration                          \
           --enable-tracing                                      \
           --disable-silent-rules                                \
           --disable-static                                      \
           --disable-upstart-monitoring                          \
           --disable-tests                                       \
%if %{without x11_renderer}
           --disable-gtk                                         \
%endif
           --with-release-file=%{_sysconfdir}/os-release         \
           --with-boot-tty=/dev/tty7                             \
           --with-shutdown-tty=/dev/tty7                         \
           --with-background-start-color-stop=0x1A3D1F           \
           --with-background-end-color-stop=0x4EA65C             \
           --with-background-color=0x3391cd                      \
           --runstatedir=/run                                    \
           --without-rhgb-compat-link                            \
           --without-system-root-install

make %{?_smp_mflags}

%install
%make_install

# *.la are files generated during compilation, useless for final user.
find %{buildroot} -type f -name "*.la" -delete

# Glow isn't quite ready for primetime
rm -rf %{buildroot}%{_datadir}/plymouth/themes/glow/

# We will nolonger ship plymouthd.conf, Plymouthd will read /usr/share/plymouth/plymouthd.defaults if /etc/plymouth/plymouthd.conf doesn't exist(jsc#SLE-11637).
rm -f %{buildroot}%{_sysconfdir}/plymouth/plymouthd.conf

# Move logrotate files from user specific directory /etc/logrotate.d to vendor specific directory /usr/etc/logrotate.d.
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d
mv %{buildroot}%{_sysconfdir}/logrotate.d/bootlog %{buildroot}%{_distconfdir}/logrotate.d/bootlog
%endif

# Split lang to seperate package.
%find_lang %{name}

%post
%{?regenerate_initrd_post}

%postun
%{?regenerate_initrd_post}
%if 0%{?suse_version} > 1500
%service_del_postun_without_restart
%else
%systemd_postun
%endif
if [ $1 -eq 0 ]; then
    rm -f %{_libdir}/plymouth/default.so
    rm -f /boot/initrd-plymouth.img
fi

%posttrans
%{?regenerate_initrd_posttrans}

%if 0%{?suse_version} > 1500
%ldconfig_scriptlets -n libply-boot-client%{soversion}
%ldconfig_scriptlets -n libply-splash-core%{soversion}
%ldconfig_scriptlets -n libply-splash-graphics%{soversion}
%ldconfig_scriptlets -n libply%{soversion}
%else
%post -n libply-boot-client%{soversion} -p /sbin/ldconfig
%postun -n libply-boot-client%{soversion} -p /sbin/ldconfig
%post -n libply-splash-core%{soversion} -p /sbin/ldconfig
%postun -n libply-splash-core%{soversion} -p /sbin/ldconfig
%post -n libply-splash-graphics%{soversion} -p /sbin/ldconfig
%postun -n libply-splash-graphics%{soversion} -p /sbin/ldconfig
%post -n libply%{soversion} -p /sbin/ldconfig
%postun -n libply%{soversion} -p /sbin/ldconfig
%endif

%post theme-spinfinity
if [ $1 -eq 1 ]; then
  set -x
  export LIB=%{_libdir}
  OTHEME="$(%{_sbindir}/plymouth-set-default-theme)"
  if [ "$OTHEME" = "text" ]; then
     if [ ! -e /.buildenv ]; then
       %{_sbindir}/plymouth-set-default-theme -R spinfinity
     else
       %{_sbindir}/plymouth-set-default-theme spinfinity
     fi
  fi
fi

%postun theme-spinfinity
if [ $1 -eq 0 ]; then
    export LIB=%{_libdir}
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" = "spinfinity" ]; then
        %{_sbindir}/plymouth-set-default-theme -R --reset
    fi
fi

%post theme-fade-in
if [ $1 -eq 1 ]; then
  set -x
  export LIB=%{_libdir}
  OTHEME="$(%{_sbindir}/plymouth-set-default-theme)"
  if [ "$OTHEME" = "text" ]; then
     if [ ! -e /.buildenv ]; then
       %{_sbindir}/plymouth-set-default-theme -R fade-in
     else
       %{_sbindir}/plymouth-set-default-theme fade-in
     fi
  fi
fi

%postun theme-fade-in
if [ $1 -eq 0 ]; then
    export LIB=%{_libdir}
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" = "fade-in" ]; then
        %{_sbindir}/plymouth-set-default-theme -R --reset
    fi
fi

%post theme-solar
if [ $1 -eq 1 ]; then
  set -x
  export LIB=%{_libdir}
  OTHEME="$(%{_sbindir}/plymouth-set-default-theme)"
  if [ "$OTHEME" = "text" ]; then
     if [ ! -e /.buildenv ]; then
       %{_sbindir}/plymouth-set-default-theme -R solar
     else
       %{_sbindir}/plymouth-set-default-theme solar
     fi
  fi
fi

%postun theme-solar
if [ $1 -eq 0 ]; then
    export LIB=%{_libdir}
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" = "solar" ]; then
        %{_sbindir}/plymouth-set-default-theme -R --reset
    fi
fi

%files
%dir %{_sysconfdir}/plymouth
%ghost %{_sysconfdir}/plymouth/plymouthd.conf
%dir %{_datadir}/plymouth
%dir %{_datadir}/plymouth/themes
%dir %{_datadir}/plymouth/themes/details
%dir %{_datadir}/plymouth/themes/text
%dir %{_sharedstatedir}/plymouth
%dir %{_libdir}/plymouth
%dir %{_libdir}/plymouth/renderers
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/bootlog
%else
%{_sysconfdir}/logrotate.d/bootlog
%endif
%{_bindir}/plymouth
%{_sbindir}/plymouthd
%{_libdir}/plymouth/details.so
%{_libdir}/plymouth/text.so
%{_libdir}/plymouth/renderers/drm*
%{_libdir}/plymouth/renderers/frame-buffer*
%{_datadir}/plymouth/themes/details/details.plymouth
%{_datadir}/plymouth/themes/text/text.plymouth
%{_datadir}/plymouth/bizcom.png
%ghost /run/plymouth
%{_localstatedir}/spool/plymouth
%{_mandir}/man?/*
%ghost %{_localstatedir}/lib/plymouth/boot-duration
%{_unitdir}/*
%ghost %{_localstatedir}/log/boot.log
%{_libexecdir}/plymouth/plymouthd-fd-escrow
%doc AUTHORS NEWS README.md ply_header.svg
%license COPYING

%files lang -f %{name}.lang

%files branding-upstream
%{_datadir}/plymouth/plymouthd.defaults

%files dracut
%{_libexecdir}/plymouth/plymouth-populate-initrd
%{_libexecdir}/plymouth/plymouth-generate-initrd

%files devel
%{_libdir}/libply.so
%{_libdir}/libply-splash-core.so
%{_libdir}/libply-boot-client.so
%{_libdir}/libply-splash-graphics.so
%{_libdir}/pkgconfig/ply-splash-core.pc
%{_libdir}/pkgconfig/ply-splash-graphics.pc
%{_libdir}/pkgconfig/ply-boot-client.pc
%{_includedir}/plymouth-1

%files -n libply%{soversion}
%{_libdir}/libply.so*

%files -n libply-boot-client%{soversion}
%{_libdir}/libply-boot-client.so*

%files -n libply-splash-core%{soversion}
%{_libdir}/libply-splash-core.so*

%files -n libply-splash-graphics%{soversion}
%{_libdir}/libply-splash-graphics.so*

%files scripts
%dir %{_libexecdir}/plymouth
%{_libexecdir}/plymouth/plymouth-update-initrd
%{_sbindir}/plymouth-set-default-theme

%if %{with x11_renderer}
%files x11-renderer
%{_libdir}/plymouth/renderers/x11*
%endif

%files plugin-fade-throbber
%{_libdir}/plymouth/fade-throbber.so

%files plugin-label
%{_libdir}/plymouth/label-pango.so

%files plugin-label-ft
%{_libdir}/plymouth/label-freetype.so

%files plugin-script
%{_libdir}/plymouth/script.so

%files plugin-space-flares
%{_libdir}/plymouth/space-flares.so

%files plugin-tribar
%{_libdir}/plymouth/tribar.so

%files plugin-two-step
%{_libdir}/plymouth/two-step.so

%files theme-bgrt
%{_datadir}/plymouth/themes/bgrt

%files theme-fade-in
%{_datadir}/plymouth/themes/fade-in

%files theme-spinfinity
%{_datadir}/plymouth/themes/spinfinity

%files theme-script
%{_datadir}/plymouth/themes/script

%files theme-spinner
%{_datadir}/plymouth/themes/spinner

%files theme-solar
%{_datadir}/plymouth/themes/solar

%files theme-tribar
%{_datadir}/plymouth/themes/tribar

%changelog
