#
# spec file for package plymouth
#
# Copyright (c) 2020 SUSE LLC
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
%define plymouthdaemon_execdir %{_sbindir}
%define plymouthclient_execdir %{_bindir}
%define plymouth_libdir %{_libdir}
%define plymouth_initrd_file /boot/initrd-plymouth.img

Name:           plymouth
Version:        0.9.5+git20190908+3abfab2
Release:        0
Summary:        Graphical Boot Animation and Logger
License:        GPL-2.0-or-later
Group:          System/Base
URL:            http://www.freedesktop.org/wiki/Software/Plymouth
Source0:        %{name}-%{version}.tar.xz
Source1:        boot-duration
# PATCH-FIX-OPENSUSE plymouth-dracut-path.patch tittiatcoke@gmail.com -- Prefix is /usr/sbin and /usr/bin
Patch0:         plymouth-dracut-path.patch
# PATCH-FIX-OPENSUSE plymouth-some-greenish-openSUSE-colors.patch bnc#886148 fcrozat@suse.com -- To use suse colors in tribar.
Patch1:         plymouth-some-greenish-openSUSE-colors.patch
# PATCH-FIX-OPENSUSE plymouth-correct-runtime-dir.patch tittiatcoke@gmail.com -- Make sure the runtime directory is /run and not /var/run
Patch2:         plymouth-correct-runtime-dir.patch
# PATCH-FIX-UPSTREAM plymouth-manpages.patch bnc#871419 idoenmez@suse.de  -- Fix man page installation
Patch3:         plymouth-manpages.patch
# PATCH-FIX-OPENSUSE plymouth-avoid-umount-hanging-shutdown.patch bnc#1105688, bnc#1129386, bnc#1134660 qzhao@opensuse.org -- Drop grantpt() to avoid system failed to unmount /var during shutdown.
Patch4:         plymouth-avoid-umount-hanging-shutdown.patch
# PATCH-FIX-SLE plymouth-no-longer-modify-conf-to-drop-isopensuse-macro.patch qzhao@suse.com  jsc#SLE-11637 -- plymouth will use plymouthd.defaults instead of plymouth.conf to close the leap gap.
Patch5:         plymouth-no-longer-modify-conf-to-drop-isopensuse-macro.patch
# PATCH-FIX-UPSTREAM 0001-Add-label-ft-plugin.patch boo#959986 fvogt@suse.com -- add ability to output text in initrd needed for encryption.
Patch1000:      0001-Add-label-ft-plugin.patch
# PATCH-FIX-UPSTREAM 0002-Install-label-ft-plugin-into-initrd-if-available.patch boo#959986 fvogt@suse.com -- add ability to output text in initrd needed for encryption.
Patch1001:      0002-Install-label-ft-plugin-into-initrd-if-available.patch
# PATCH-FIX-UPSTREAM 0003-fix_null_deref.patch boo#959986 fvogt@suse.com -- add ability to output text in initrd needed for encryption.
Patch1002:      0003-fix_null_deref.patch
BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gcc
BuildRequires:  kernel-headers
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  module-init-tools
BuildRequires:  pkgconfig
BuildRequires:  suse-module-tools
# needed for systemd-tty-ask-password-agent
BuildRequires:  intltool
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libsystemd) >= 186
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(pango) >= 1.21.0
BuildRequires:  pkgconfig(systemd) >= 186
%if %{with x11_renderer}
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14.0
%endif
Recommends:     %{name}-lang
Requires:       %{name}-branding
Requires:       gnu-unifont-bitmap-fonts
Requires:       systemd >= 186
Requires(post): coreutils
Requires(post): plymouth-scripts = %{version}
Requires(postun): coreutils
Recommends:     plymouth-plugin-label-ft
Suggests:       plymouth-plugin-label
Provides:       bootsplash = 3.5
Obsoletes:      bootsplash < 3.5
Provides:       systemd-plymouth = 44-10.2
Obsoletes:      systemd-plymouth <= 44-10.1

%description
Plymouth provides an attractive graphical boot animation in
place of the text messages that normally get shown.  Text
messages are instead redirected to a log file for viewing
after boot.

%package -n libply-boot-client%{soversion}
Summary:        Plymouth core library
Group:          Development/Libraries/C and C++

%description -n libply-boot-client%{soversion}
This package contains the libply-boot-client library used by Plymouth.

%package -n libply-splash-core%{soversion}
Summary:        Plymouth core library
Group:          Development/Libraries/C and C++

%description -n libply-splash-core%{soversion}
This package contains the libply-splash-core library
used by graphical Plymouth splashes.

%package -n libply-splash-graphics%{soversion}
Summary:        Plymouth graphics libraries
Group:          Development/Libraries/C and C++
BuildRequires:  libpng-devel

%description -n libply-splash-graphics%{soversion}
This package contains the libply-splash-graphics library
used by graphical Plymouth splashes.

%package -n libply%{soversion}
Summary:        Plymouth core library
Group:          Development/Libraries/C and C++
Requires:       libply-boot-client%{soversion} = %{version}

%description -n libply%{soversion}
This package contains the libply library used by Plymouth.

%package branding-upstream
Summary:        default configuration file and branding from the Plymouth upstream.
Group:          System/Base
Provides:       %{name}-branding = %{version}-%{release}.
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
Supplements:    packageand(plymouth:dracut)

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
Requires:       coreutils
Requires:       cpio
Requires:       dracut
Requires:       findutils
Requires:       gzip
Requires(pre):  %{name} = %{version}

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
graphical boot splashes using FreeTyoe

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

%package plugin-throbgress
Summary:        Plymouth "Throbgress" plugin
Group:          System/Base
Requires:       %{name}-plugin-label = %{version}
Requires:       libply%{soversion} = %{version}
Requires:       libply-splash-core%{soversion} = %{version}
Requires:       libply-splash-graphics%{soversion} = %{version}

%description plugin-throbgress
This package contains the "throbgress" boot splash plugin for
Plymouth. It features a centered logo and animated spinner that
spins repeatedly while a progress bar advances at the bottom of
the screen.

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
Requires:       %{name}-plugin-throbgress = %{version}
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

# replace builddate with patch0date
sed -i "s/__DATE__/\"$(stat -c %%y %{_sourcedir}/%{name}.changes)\"/" src/main.c

%build
%configure \
           --enable-systemd-integration                          \
           --enable-tracing                                      \
           --disable-silent-rules                                \
           --disable-static                                      \
           --disable-upstart-monitoring                          \
           --disable-tests                                       \
           --disable-libkms                                      \
%if %{without x11_renderer}
           --disable-gtk                                         \
%endif
           --with-release-file=%{_sysconfdir}/os-release         \
           --with-boot-tty=/dev/tty7                             \
           --with-shutdown-tty=/dev/tty1                         \
           --with-background-start-color-stop=0x1A3D1F           \
           --with-background-end-color-stop=0x4EA65C             \
           --with-background-color=0x3391cd                      \
           --without-rhgb-compat-link                            \
           --without-system-root-install                         

make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}/%{_bindir}/rhgb-client

#Link the plymouth client binary also to /bin until the move to /usr is completed
mkdir %{buildroot}/bin
(cd %{buildroot}/bin; ln -s ..%{_bindir}/plymouth)

# Glow isn't quite ready for primetime
rm -rf %{buildroot}%{_datadir}/plymouth/glow/
rm -rf %{buildroot}%{_datadir}/plymouth/themes/glow/
rm -f %{buildroot}%{_libdir}/plymouth/glow.so

find %{buildroot} -type f -name "*.la" -delete -print

mkdir -p %{buildroot}%{_localstatedir}/lib/plymouth
mkdir -p %{buildroot}/run/plymouth
mkdir -p %{buildroot}%{_localstatedir}/log
touch %{buildroot}%{_localstatedir}/log/boot.log
touch %{buildroot}%{_localstatedir}/spool/plymouth/boot.log
cp $RPM_SOURCE_DIR/boot-duration %{buildroot}%{_datadir}/plymouth/default-boot-duration
cp $RPM_SOURCE_DIR/boot-duration %{buildroot}%{_localstatedir}/lib/plymouth

# We will nolonger ship plymouthd.conf, Plymouthd will read /usr/share/plymouth/plymouthd.defaults if /etc/plymouth/plymouthd.conf doesn't exist(jsc#SLE-11637).
rm -f  %{buildroot}%{_sysconfdir}/plymouth/plymouthd.conf
rm -f  %{buildroot}%{_datadir}/plymouth/plymouthd.conf

%post
%{?regenerate_initrd_post}
if [ ! -e /.buildenv ]; then
   [ -f %{_localstatedir}/lib/plymouth/boot-duration ] || cp -f %{_datadir}/plymouth/default-boot-duration %{_localstatedir}/lib/plymouth/boot-duration
fi
[ -x /bin/systemctl ] && /bin/systemctl daemon-reload >/dev/null 2>&1 || :

%postun
%{?regenerate_initrd_post}
if [ $1 -eq 0 ]; then
    rm -f %{_libdir}/plymouth/default.so
    rm -f /boot/initrd-plymouth.img
    [ -x /bin/systemctl ] && /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi

%posttrans
%{?regenerate_initrd_posttrans}

%post -n libply-boot-client%{soversion} -p /sbin/ldconfig
%postun -n libply-boot-client%{soversion} -p /sbin/ldconfig
%post -n libply-splash-core%{soversion} -p /sbin/ldconfig
%postun -n libply-splash-core%{soversion} -p /sbin/ldconfig
%post -n libply-splash-graphics%{soversion} -p /sbin/ldconfig
%postun -n libply-splash-graphics%{soversion} -p /sbin/ldconfig
%post -n libply%{soversion} -p /sbin/ldconfig
%postun -n libply%{soversion} -p /sbin/ldconfig
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
%license COPYING
%doc AUTHORS NEWS README
%dir %{_datadir}/plymouth
%dir %{_datadir}/plymouth/themes
%dir %{_datadir}/plymouth/themes/details
%dir %{_datadir}/plymouth/themes/text
%dir %{_localstatedir}/lib/plymouth
%dir %{_libdir}/plymouth
%dir %{_libdir}/plymouth/renderers
%dir %{_sysconfdir}/plymouth
%ghost %{_sysconfdir}/plymouth/plymouthd.conf
%{plymouthdaemon_execdir}/plymouthd
%{plymouthclient_execdir}/plymouth
/bin/plymouth
%{_libdir}/plymouth/details.so
%{_libdir}/plymouth/text.so
%{_libdir}/plymouth/renderers/drm*
%{_libdir}/plymouth/renderers/frame-buffer*
%{_datadir}/plymouth/default-boot-duration
%{_datadir}/plymouth/themes/details/details.plymouth
%{_datadir}/plymouth/themes/text/text.plymouth
%{_datadir}/plymouth/bizcom.png
%ghost /run/plymouth
%{_localstatedir}/spool/plymouth
%{_mandir}/man?/*
%ghost %{_localstatedir}/lib/plymouth/boot-duration
%{_unitdir}/*
%ghost %{_localstatedir}/log/boot.log
/usr/share/locale/

%files branding-upstream
%{_datadir}/plymouth/plymouthd.defaults

%files dracut
%{_libexecdir}/plymouth/plymouth-populate-initrd
%{_libexecdir}/plymouth/plymouth-generate-initrd

%files devel
%{plymouth_libdir}/libply.so
%{plymouth_libdir}/libply-splash-core.so
%{_libdir}/libply-boot-client.so
%{_libdir}/libply-splash-graphics.so
%{_libdir}/pkgconfig/ply-splash-core.pc
%{_libdir}/pkgconfig/ply-splash-graphics.pc
%{_libdir}/pkgconfig/ply-boot-client.pc
%{_includedir}/plymouth-1

%files -n libply-boot-client%{soversion}
%{_libdir}/libply-boot-client.so.%{soversion}*

%files -n libply-splash-core%{soversion}
%{plymouth_libdir}/libply-splash-core.so.%{soversion}*

%files -n libply-splash-graphics%{soversion}
%{_libdir}/libply-splash-graphics.so.%{soversion}*

%files -n libply%{soversion}
%{plymouth_libdir}/libply.so.%{soversion}*

%files scripts
%dir %{_libexecdir}/plymouth
%{_sbindir}/plymouth-set-default-theme
%{_libexecdir}/plymouth/plymouth-update-initrd

%if %{with x11_renderer}
%files x11-renderer
%{_libdir}/plymouth/renderers/x11*
%endif

%files plugin-label
%{_libdir}/plymouth/label.so

%files plugin-label-ft
%{_libdir}/plymouth/label-ft.so

%files plugin-fade-throbber
%{_libdir}/plymouth/fade-throbber.so

%files theme-fade-in
%dir %{_datadir}/plymouth/themes/fade-in
%{_datadir}/plymouth/themes/fade-in/bullet.png
%{_datadir}/plymouth/themes/fade-in/entry.png
%{_datadir}/plymouth/themes/fade-in/lock.png
%{_datadir}/plymouth/themes/fade-in/star.png
%{_datadir}/plymouth/themes/fade-in/fade-in.plymouth

%files plugin-throbgress
%{_libdir}/plymouth/throbgress.so

%files theme-spinfinity
%dir %{_datadir}/plymouth/themes/spinfinity
%{_datadir}/plymouth/themes/spinfinity/box.png
%{_datadir}/plymouth/themes/spinfinity/bullet.png
%{_datadir}/plymouth/themes/spinfinity/entry.png
%{_datadir}/plymouth/themes/spinfinity/lock.png
%{_datadir}/plymouth/themes/spinfinity/throbber-[0-3][0-9].png
%{_datadir}/plymouth/themes/spinfinity/spinfinity.plymouth

%files plugin-space-flares
%{_libdir}/plymouth/space-flares.so

%files theme-spinner
%dir %{_datadir}/plymouth/themes/spinner
%{_datadir}/plymouth/themes/spinner/*.*

%files theme-solar
%dir %{_datadir}/plymouth/themes/solar
%{_datadir}/plymouth/themes/solar/*.png
%{_datadir}/plymouth/themes/solar/solar.plymouth

%files theme-tribar
%dir %{_datadir}/plymouth/themes/tribar
%{_datadir}/plymouth/themes/tribar/*.*

%files plugin-two-step
%{_libdir}/plymouth/two-step.so

%files plugin-tribar
%{_libdir}/plymouth/tribar.so

%files plugin-script
%{_libdir}/plymouth/script.so

%files theme-script
%dir %{_datadir}/plymouth/themes/script/
%{_datadir}/plymouth/themes/script/*.png
%{_datadir}/plymouth/themes/script/script.script
%{_datadir}/plymouth/themes/script/script.plymouth

%files theme-bgrt
%dir %{_datadir}/plymouth/themes/bgrt
%{_datadir}/plymouth/themes/bgrt/*.*

%changelog
