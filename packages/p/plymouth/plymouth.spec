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


%bcond_with x11_renderer
%bcond_with fedora_theme

%global git_version 20200418+14e91cc
%global so_version 5

Name:           plymouth
Version:        0.9.5+git%{git_version}
Release:        0
Summary:        Graphical Boot Animation and Logger
License:        GPL-2.0-or-later
Group:          System/Base
URL:            https://www.freedesktop.org/wiki/Software/Plymouth
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE plymouth-some-greenish-openSUSE-colors.patch bnc#886148 fcrozat@suse.com -- To use suse colors in tribar.
Patch0:         plymouth-some-greenish-openSUSE-colors.patch
# PATCH-FIX-OPENSUSE plymouth-manpages.patch bnc#871419 idoenmez@suse.de -- Fix man page installation
Patch1:         plymouth-manpages.patch
# PATCH-FIX-OPENSUSE plymouth-only_use_fb_for_cirrus_bochs.patch bnc#888590 fvogt@suse.com -- force fb for cirrus and bochs, force drm otherwise. replace removal of framebuffer driver and plymouth-ignore-cirrusdrm.patch with single patch.
Patch2:         plymouth-only_use_fb_for_cirrus_bochs.patch
# PATCH-FIX-OPENSUSE plymouth-disable-fedora-logo.patch qzhao@opensuse.org -- Disable the fedora logo reference which is not in openSUSE.
Patch3:         plymouth-disable-fedora-logo.patch
# PATCH-FIX-OPENSUSE plymouth-disable-fedora-bizcom-theme.patch qzhao@opensuse.org -- Disable to compile fedora related themes.
Patch4:         plymouth-disable-fedora-bizcom-theme.patch
# PATCH-FIX-OPENSUSE plymouth-ignore-serial-console.patch qzhao@opensuse.org bnc#1164123 -- Don't output in serial console for openQA need to take serial in the test, and yast-installation prgram has a feature to install system through it.
Patch5:         plymouth-ignore-serial-console.patch
# PATCH-FIX-UPSTREAM 0001-Add-label-ft-plugin.patch boo#959986 fvogt@suse.com -- add ability to output text in initrd needed for encryption.
Patch1000:      0001-Add-label-ft-plugin.patch
# PATCH-FIX-UPSTREAM 0002-Install-label-ft-plugin-into-initrd-if-available.patch boo#959986 fvogt@suse.com -- add ability to output text in initrd needed for encryption.
Patch1001:      0002-Install-label-ft-plugin-into-initrd-if-available.patch
# PATCH-FIX-UPSTREAM 0003-fix_null_deref.patch boo#959986 fvogt@suse.com -- add ability to output text in initrd needed for encryption.
Patch1002:      0003-fix_null_deref.patch
BuildRequires:  automake
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gcc
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  libxslt
BuildRequires:  pkgconfig
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
%if 0%{suse_version} >= 1550
# regenerate_initrd_post moved to rpm-config-SUSE:initrd.macros
BuildRequires:  rpm-config-SUSE >= 0.g11
%else
BuildRequires:  suse-module-tools
%endif
Recommends:     %{name}-lang
Requires:       %{name}-branding
Requires:       systemd >= 186
Requires(post): coreutils
Requires(post): plymouth-scripts = %{version}
Requires(postun): coreutils
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

%package -n libply-boot-client%{so_version}
Summary:        Plymouth core library
Group:          Development/Libraries/C and C++

%description -n libply-boot-client%{so_version}

This package contains the libply-boot-client library used by Plymouth.

%package -n libply-splash-core%{so_version}
Summary:        Plymouth core library
Group:          Development/Libraries/C and C++

%description -n libply-splash-core%{so_version}
This package contains the libply-splash-core library
used by graphical Plymouth splashes.

%package -n libply-splash-graphics%{so_version}
Summary:        Plymouth graphics libraries
Group:          Development/Libraries/C and C++
BuildRequires:  libpng-devel

%description -n libply-splash-graphics%{so_version}
This package contains the libply-splash-graphics library
used by graphical Plymouth splashes.

%package -n libply%{so_version}
Summary:        Plymouth core library
Group:          Development/Libraries/C and C++
Requires:       libply-boot-client%{so_version} = %{version}

%description -n libply%{so_version}
This package contains the libply library used by Plymouth.

%package devel
Summary:        Libraries and headers for writing Plymouth splash plugins
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
%if %{with x11_renderer}
Requires:       %{name}-x11-renderer = %{version}
%endif
Requires:       libply%{so_version} = %{version}
Requires:       libply-boot-client%{so_version} = %{version}
Requires:       libply-splash-core%{so_version} = %{version}
Requires:       libply-splash-graphics%{so_version} = %{version}
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
Requires:       libply-splash-graphics%{so_version} = %{version}

%description plugin-label
This package contains the label control plugin for
Plymouth. It provides the ability to render text on
graphical boot splashes using pango and cairo.

%package plugin-label-ft
Summary:        Plymouth FreeType label plugin
Group:          System/Base
Requires:       fontconfig
Requires:       libply-splash-graphics%{so_version} = %{version}

%description plugin-label-ft
This package contains the label control plugin for
Plymouth. It provides the ability to render text on
graphical boot splashes using FreeType

%package plugin-script
Summary:        Plymouth "script" plugin
Group:          System/Base
Requires:       libply%{so_version} = %{version}
Requires:       libply-splash-core%{so_version} = %{version}
Requires:       libply-splash-graphics%{so_version} = %{version}

%description plugin-script
This package contains the "script" boot splash plugin for
Plymouth. It features an extensible, scriptable boot splash
language that simplifies the process of designing custom
boot splash themes.

%package plugin-tribar
Summary:        Plymouth "script" plugin
Group:          System/Base
Requires:       libply%{so_version} = %{version}
Requires:       libply-splash-core%{so_version} = %{version}
Requires:       libply-splash-graphics%{so_version} = %{version}

%description plugin-tribar
This package contains the "tribar" boot splash plugin for
Plymouth. It features an extensible, scriptable boot splash
language that simplifies the process of designing custom
boot splash themes.

%package plugin-two-step
Summary:        Plymouth "two-step" plugin
Group:          System/Base
Requires:       libply%{so_version} = %{version}
Requires:       libply-splash-core%{so_version} = %{version}
Requires:       libply-splash-graphics%{so_version} = %{version}
Requires:       plymouth-plugin-label = %{version}

%description plugin-two-step
This package contains the "two-step" boot splash plugin for
Plymouth. It features a two phased boot process that starts with
a progressing animation synced to boot time and finishes with a
short, fast one-shot animation.

%package theme-bgrt
Summary:        Plymouth "bgrt" theme
Group:          System/Base
Requires:       %{name}-plugin-two-step = %{version}
Requires:       %{name}-theme-spinner = %{version}
Requires(post): %{name}-scripts
BuildArch:      noarch

%description theme-bgrt
This package contains the "bgrt" boot splash theme for
Plymouth. 

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

%package theme-spinfinity
Summary:        Plymouth "Spinfinity" theme
Group:          System/Base
Requires:       %{name}-plugin-two-step = %{version}
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

%package theme-tribar
Summary:        Plymouth "Tribar" theme
Group:          System/Base
Requires:       %{name}-plugin-tribar = %{version}
Requires(post): %{name}-scripts
BuildArch:      noarch

%description theme-tribar
This package contains the "Tribar" boot splash theme for
Plymouth

%if %{with x11_renderer}
%package x11-renderer
Summary:        Plymouth X11 renderer
Group:          System/Base
Requires:       %{name} = %{version}

%description x11-renderer
This package provides the X11 renderer which allows to test Plymouth
behavior on environments with a valid DISPLAY.
%endif

%if %{with fedora_theme}
%package plugin-fade-throbber
Summary:        Plymouth "Fade-Throbber" plugin
Group:          System/Base
Requires:       libply%{so_version} = %{version}
Requires:       libply-splash-core%{so_version} = %{version}
Requires:       libply-splash-graphics%{so_version} = %{version}

%description plugin-fade-throbber
This package contains the "Fade-In" boot splash plugin for
Plymouth. It features a centered image that fades in and out
while other images pulsate around during system boot up.

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

%package theme-glow
Summary:        Plymouth "glow" theme
Group:          System/Base
Requires:       %{name}-plugin-tribar = %{version}
Requires(post): %{name}-scripts
BuildArch:      noarch

%description theme-glow
This package contains the "glow" boot splash theme for
Plymouth

%package plugin-space-flares
Summary:        Plymouth "space-flares" plugin
Group:          System/Base
Requires:       %{name}-plugin-label = %{version}
Requires:       libply%{so_version} = %{version}
Requires:       libply-splash-core%{so_version} = %{version}
Requires:       libply-splash-graphics%{so_version} = %{version}

%description plugin-space-flares
This package contains the "space-flares" boot splash plugin for
Plymouth. It features a corner image with animated flares.

%package theme-solar
Summary:        Plymouth "Solar" theme
Group:          System/Base
Requires:       %{name}-plugin-space-flares = %{version}
Requires(post): %{name}-scripts
BuildArch:      noarch

%description theme-solar
This package contains the "Solar" boot splash theme for
Plymouth. It features a blue flamed sun with animated solar flares.
%endif

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
           --with-release-file=%{_sysconfdir}/os-release         \
           --with-boot-tty=/dev/tty7                             \
           --with-shutdown-tty=/dev/tty1                         \
           --with-background-start-color-stop=0x1A3D1F           \
           --with-background-end-color-stop=0x4EA65C             \
           --with-background-color=0x3391cd                      \
           --without-rhgb-compat-link                            \
           --without-logo                                        \
           --without-system-root-install                         \
%if %{without x11_renderer}
           --disable-gtk
%endif

make %{?_smp_mflags}

%install
%make_install

# Create necessary directories:
mkdir -p %{buildroot}%{_localstatedir}/lib/plymouth
mkdir -p %{buildroot}/run/plymouth
mkdir -p %{buildroot}%{_localstatedir}/log

# Copy upstream's default config file to system and change release settings:
cp %{buildroot}/%{_datadir}/plymouth/plymouthd.defaults %{buildroot}/%{_sysconfdir}/plymouth/plymouthd.conf

%if 0%{?is_opensuse}
sed -i -e 's/spinner/bgrt/g' %{buildroot}/%{_sysconfdir}/plymouth/plymouthd.conf
%else
sed -i -e 's/spinner/SLE/g' %{buildroot}/%{_sysconfdir}/plymouth/plymouthd.conf
%endif

# Link the plymouth client binary to /bin to fit display and emergency service requirement:
mkdir %{buildroot}/bin
(cd %{buildroot}/bin; ln -s ..%{_bindir}/plymouth)

# Create boot-duration file for recording boot info:
touch %{buildroot}%{_datadir}/plymouth/default-boot-duration
touch %{buildroot}%{_localstatedir}/lib/plymouth

# Remove temp files which produced during the compilation:
find $RPM_BUILD_ROOT -name '*.la' -delete

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

%post   -n libply-boot-client%{so_version} -p /sbin/ldconfig
%postun -n libply-boot-client%{so_version} -p /sbin/ldconfig
%post   -n libply-splash-core%{so_version} -p /sbin/ldconfig
%postun -n libply-splash-core%{so_version} -p /sbin/ldconfig
%post   -n libply-splash-graphics%{so_version} -p /sbin/ldconfig
%postun -n libply-splash-graphics%{so_version} -p /sbin/ldconfig
%post   -n libply%{so_version} -p /sbin/ldconfig
%postun -n libply%{so_version} -p /sbin/ldconfig

%postun theme-bgrt
if [ $1 -eq 0 ]; then
    export LIB=%{_libdir}
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" = "bgrt" ]; then
        %{_sbindir}/plymouth-set-default-theme -R --reset
    fi
fi

%postun theme-script
if [ $1 -eq 0 ]; then
    export LIB=%{_libdir}
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" = "script" ]; then
        %{_sbindir}/plymouth-set-default-theme -R --reset
    fi
fi

%postun theme-spinfinity
if [ $1 -eq 0 ]; then
    export LIB=%{_libdir}
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" = "spinfinity" ]; then
        %{_sbindir}/plymouth-set-default-theme -R --reset
    fi
fi

%postun theme-spinner
if [ $1 -eq 0 ]; then
    export LIB=%{_libdir}
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" = "spinner" ]; then
        %{_sbindir}/plymouth-set-default-theme -R --reset
    fi
fi

%postun theme-tribar
if [ $1 -eq 0 ]; then
    export LIB=%{_libdir}
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" = "tribar" ]; then
        %{_sbindir}/plymouth-set-default-theme -R --reset
    fi
fi

%if %{with fedora_theme}
%postun theme-fade-in
if [ $1 -eq 0 ]; then
    export LIB=%{_libdir}
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" = "fade-in" ]; then
        %{_sbindir}/plymouth-set-default-theme -R --reset
    fi
fi

%postun theme-glow
if [ $1 -eq 0 ]; then
    export LIB=%{_libdir}
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" = "glow" ]; then
        %{_sbindir}/plymouth-set-default-theme -R --reset
    fi
fi

%postun theme-solar
if [ $1 -eq 0 ]; then
    export LIB=%{_libdir}
    if [ "$(%{_sbindir}/plymouth-set-default-theme)" = "solar" ]; then
        %{_sbindir}/plymouth-set-default-theme -R --reset
    fi
fi
%endif

%files
%dir %{_datadir}/plymouth
%dir %{_datadir}/plymouth/themes
%dir %{_datadir}/plymouth/themes/details
%dir %{_datadir}/plymouth/themes/text
%dir %{_localstatedir}/lib/plymouth
%dir %{_libdir}/plymouth
%dir %{_libdir}/plymouth/renderers
%dir %{_sysconfdir}/plymouth
/bin/plymouth
%{_bindir}/plymouth
%{_sbindir}/plymouthd
%config(noreplace) %{_sysconfdir}/plymouth/plymouthd.conf
%config(noreplace) %{_sysconfdir}/logrotate.d/bootlog
%{_libdir}/plymouth/details.so
%{_libdir}/plymouth/text.so
%{_libdir}/plymouth/renderers/drm*
%{_libdir}/plymouth/renderers/frame-buffer*
%{_datadir}/plymouth/default-boot-duration
%{_datadir}/plymouth/themes/details/details.plymouth
%{_datadir}/plymouth/themes/text/text.plymouth
%{_datadir}/plymouth/plymouthd.defaults
%{_localstatedir}/spool/plymouth
%{_unitdir}/*
%ghost /run/plymouth
%ghost %{_localstatedir}/lib/plymouth/boot-duration
%ghost %{_localstatedir}/log/boot.log
%{_mandir}/man?/*
%doc AUTHORS NEWS README
%license COPYING
/usr/share/locale/

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

%files -n libply-boot-client%{so_version}
%{_libdir}/libply-boot-client.so.%{so_version}*

%files -n libply-splash-core%{so_version}
%{_libdir}/libply-splash-core.so.%{so_version}*

%files -n libply-splash-graphics%{so_version}
%{_libdir}/libply-splash-graphics.so.%{so_version}*

%files -n libply%{so_version}
%{_libdir}/libply.so.%{so_version}*

%files scripts
%dir %{_libexecdir}/plymouth
%{_sbindir}/plymouth-set-default-theme
%{_libexecdir}/plymouth/plymouth-update-initrd

%files plugin-label
%{_libdir}/plymouth/label.so

%files plugin-label-ft
%{_libdir}/plymouth/label-ft.so

%files plugin-script
%{_libdir}/plymouth/script.so

%files plugin-tribar
%{_libdir}/plymouth/tribar.so

%files plugin-two-step
%{_libdir}/plymouth/two-step.so

%files theme-bgrt
%dir %{_datadir}/plymouth/themes/bgrt
%{_datadir}/plymouth/themes/bgrt/*

%files theme-script
%dir %{_datadir}/plymouth/themes/script/
%{_datadir}/plymouth/themes/script/*

%files theme-spinfinity
%dir %{_datadir}/plymouth/themes/spinfinity
%{_datadir}/plymouth/themes/spinfinity/*

%files theme-spinner
%dir %{_datadir}/plymouth/themes/spinner
%{_datadir}/plymouth/themes/spinner/*

%files theme-tribar
%dir %{_datadir}/plymouth/themes/tribar
%{_datadir}/plymouth/themes/tribar/*

%if %{with x11_renderer}
%files x11-renderer
%{_libdir}/plymouth/renderers/x11*
%endif

%if %{with fedora_theme}
%files plugin-fade-throbber
%{_libdir}/plymouth/fade-throbber.so

%files theme-fade-in
%dir %{_datadir}/plymouth/themes/fade-in
%{_datadir}/plymouth/themes/fade-in/*

%files theme-glow
%dir %{_datadir}/plymouth/themes/glow
%{_datadir}/plymouth/themes/glow/*

%files plugin-space-flares
%{_libdir}/plymouth/space-flares.so

%files theme-solar
%dir %{_datadir}/plymouth/themes/solar
%{_datadir}/plymouth/themes/solar/*
%endif

%changelog
