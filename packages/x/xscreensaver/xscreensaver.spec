#
# spec file for package xscreensaver
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


Name:           xscreensaver
Version:        5.45
Release:        0
Summary:        A screen saver and locker for the X Window System
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Amusements/Toys/Screensavers
URL:            https://www.jwz.org/xscreensaver
Source:         https://www.jwz.org/xscreensaver/%{name}-%{version}.tar.gz
Source1:        xscreensaver.pamd
Source2:        xscreensaver-data.list
Source3:        xscreensaver-data-extra.list
#
Source4:        xscreensaver-desktops-generate.sh
# Do not show some rpmlint warnings.
Source99:       xscreensaver-rpmlintrc
#
Patch5:         xscreensaver-background.patch
Patch20:        xscreensaver-mansuffix.patch
Patch21:        xscreensaver-default-screensaver.patch
Patch24:        xscreensaver-slideshow-dri-detect.patch
Patch29:        xscreensaver-ignore-no-pwent-password.patch
Patch32:        xscreensaver-fireworkx-man.patch
# PATCH-FIX-OPENSUSE xscreensaver-webcollage-dictpath.patch seife+obs@b1-systems.com -- Add /var/lib/dict/words to search path for word dictionaries.
Patch42:        xscreensaver-webcollage-dictpath.patch
# PATCH-FEATURE-OPENSUSE xscreensaver-disable-upgrade-nagging.patch boo#890595 gber@opensuse.org -- Disable nagging messages about upgrading to a newer version.
Patch43:        xscreensaver-disable-upgrade-nagging-message.patch
# PATCH-FEATURE-OPENSUSE xscreensaver-bug-reports.patch bnc890595 sbrabec@suse.cz -- Ask reporters to upgrade before reporting bugs.
Patch45:        xscreensaver-bug-reports.patch
BuildRequires:  automake
BuildRequires:  bc
BuildRequires:  gdmflexiserver
BuildRequires:  gtkdoc
BuildRequires:  intltool
BuildRequires:  libgle-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libxslt-tools
BuildRequires:  pam-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(atk)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdk-pixbuf-xlib-2.0)
BuildRequires:  pkgconfig(gdk-x11-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gtk+-x11-2.0)
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(xxf86vm)
#
Requires:       %{name}-data
Requires:       /sbin/unix2_chkpwd
Requires:       desktop-data
Recommends:     %{name}-lang = %{version}
#
Suggests:       %{name}-data-extra
#
Provides:       xscreensaver-gnome = %{version}
Provides:       xscrns = %{version}
Obsoletes:      xscreensaver-gnome < %{version}
Obsoletes:      xscrns < %{version}

%description
The xscreensaver program waits until the keyboard and mouse have
been idle for a period of time, and then runs a graphics demo
chosen at random. It turns off as soon as there is any mouse or
keyboard activity. It can also lock the screen immediately, after a
longer idle period, or on demand.

The xscreensaver package consists of two parts: the screensaver and
the "driver" or "daemon", which detects idleness and does locking,
and the many graphics demos that are launched by xscreensaver.

Any X program that can draw on the root window can be used with
xscreensaver, regardless of how that program is written, what
language it is written in, or what libraries it uses. The
xscreensaver daemon takes care of detecting when the user is idle,
locking, and checking passwords and all the other book-keeping. All
the other programs need to do is draw.

The benefit that xscreensaver has over the combination of the xlock
and xautolock programs is the ease with which new graphic hacks can
be installed. You do not need to recompile (or even re-run) the
xscreensaver program to add a new display mode, you just change a
config file.

%package data
Summary:        Selection of screensavers from xscreensaver
Group:          Amusements/Toys/Screensavers
Recommends:     %{name}-lang = %{version}

%description data
The xscreensaver program waits until the keyboard and mouse have
been idle for a period of time, and then runs a graphics demo
chosen at random. It turns off as soon as there is any mouse or
keyboard activity. It can also lock the screen immediately, after a
longer idle period, or on demand.

This packages contains a selection of graphics demos.

%package data-extra
Summary:        Selection of screensavers from xscreensaver
Group:          Amusements/Toys/Screensavers
Recommends:     %{name}-data
Recommends:     %{name}-lang = %{version}

%description data-extra
The xscreensaver program waits until the keyboard and mouse have
been idle for a period of time, and then runs a graphics demo
chosen at random. It turns off as soon as there is any mouse or
keyboard activity. It can also lock the screen immediately, after a
longer idle period, or on demand.

This packages contains additional graphics demos.

%lang_package

%prep
%setup -q
%patch5
%patch20
%patch21
# FIXME: Test, whether this patch is still needed:
%patch24 -p1
%patch29
%patch32
%patch42
%patch43 -p1
%patch45 -p1
# KDE, GNOME and MATE have there own screensavers:
echo 'NotShowIn=KDE;GNOME;MATE;' >> driver/screensaver-properties.desktop.in
cp -f %{SOURCE4} xscreensaver-desktops-generate
chmod a+x xscreensaver-desktops-generate

%build
# Fix man pages header:
find hacks -name '*.man' -print0 | xargs -0 sed -ie 's/TH XScreenSaver 1/TH XScreenSaver 6/'
# Modify hack list to fit our needs:
sed -re '
  s/^([[:space:]]*(rorschach|greynetic|noseguy|deco|moire|spiral|laser|sierpinski|flag|sphere|mountain|triangle|worm|xlyap|cynosure|bsod|t3d|wander"Wander|critical|phosphor|blaster|nerverot|"SpeedMine"|poluominoes|fluidballs|barcode|bubbles))/-\1/;
  s/^-([[:space:]]*(juggle))/\1/;
  s/^@GL_KLUDGE@([[:space:]]*GL:[[:space:]]*(sproingies|"Molecule \(lumpy\)"|circuit|atunnel|glmatrix|stairs|pulsar|starwars|"GLText|boxed|"GLForestFire"|sballs|cubenetic|queens|endgame))/-\1/;
  s/^-([[:space:]]*GL:[[:space:]]*(fireflies))/\1/;
  /.*vidwhacker -stdin -stdout/D;
  ' driver/XScreenSaver.ad.in > driver/XScreenSaver.ad.in.tmp && mv -f driver/XScreenSaver.ad.in.tmp driver/XScreenSaver.ad.in
intltoolize --copy --force
sed -i "s|@install_sh@|../install-sh -c|" po/Makefile.in.in
chmod +x install-sh
autoreconf -fi
#lie to configure so the default C standard is used
export ac_cv_gcc_accepts_std=no
# Disable direct PAM use and shadow (both needs suid).
%configure \
  --with-hackdir=%{_libdir}/xscreensaver             \
  --with-x-app-defaults=%{_datadir}/X11/app-defaults \
  --with-configdir=%{_sysconfdir}/xscreensaver       \
  --without-kerberos                                 \
  --with-passwd-helper=/sbin/unix2_chkpwd            \
  --with-gl                                          \
  --with-gle                                         \
  --with-pixbuf                                      \
  --with-jpeg                                        \
  --with-xshm-ext                                    \
  --with-xdbe-ext                                    \
  --without-pam                                      \
  --without-shadow                                   \
  --with-login-manager=%{_bindir}/gdmflexiserver     \
  --with-image-directory=%{_datadir}/wallpapers      \
  --enable-locking                                   \
  --with-login-manager
%make_build all

%install
rm -f hacks/config/vidwhacker.xml
mkdir -p %{buildroot}/tmp/bin/
make install_prefix=%{buildroot} \
  KDEDIR=/tmp                    \
  DESTDIR=%{buildroot}           \
  datadir=%{_datadir}            \
  install
rm -r %{buildroot}/tmp/
#
# Remove obsolete SUID bit.
chmod 0755 %{buildroot}%{_bindir}/xscreensaver
#
# PAM config.
install -Dm 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/xscreensaver
#
# Language files.
%find_lang %{name}
#
# Desktop files.
%suse_update_desktop_file -G "Screensaver properties" xscreensaver-properties DesktopSettings
#
# Generate .desktop files for mate-screensaver usage.
mkdir -p %{buildroot}%{_datadir}/applications/screensavers/
./xscreensaver-desktops-generate %{buildroot}%{_sysconfdir}/xscreensaver/ %{buildroot}%{_datadir}/applications/screensavers/
# Remove duplicate of a file from mate-screensaver.
rm -f %{buildroot}%{_datadir}/applications/screensavers/popsquares.desktop
#
# List files for screensavers in data and data-extra subpackages.
rm -f %{name}-data.lst %{name}-data-extra.lst
for hack in $(grep -v '#' %{SOURCE2}); do
    [ -f %{buildroot}%{_mandir}/man6/$hack.6* ] && echo "%doc %{_mandir}/man6/$hack.6*" >> %{name}-data.lst
    [ -f %{buildroot}%{_sysconfdir}/xscreensaver/$hack.xml ] && echo "%config %{_sysconfdir}/xscreensaver/$hack.xml" >> %{name}-data.lst
    [ -f %{buildroot}%{_datadir}/applications/screensavers/$hack.desktop ] && echo "%{_datadir}/applications/screensavers/$hack.desktop" >> %{name}-data.lst
    echo "%{_libdir}/xscreensaver/$hack" >> %{name}-data.lst
done
for hack in $(grep -v '#' %{SOURCE3}); do
    [ -f %{buildroot}%{_mandir}/man6/$hack.6* ] && echo "%doc %{_mandir}/man6/$hack.6*" >> %{name}-data-extra.lst
    [ -f %{buildroot}%{_sysconfdir}/xscreensaver/$hack.xml ] && echo "%config %{_sysconfdir}/xscreensaver/$hack.xml" >> %{name}-data-extra.lst
    [ -f %{buildroot}%{_datadir}/applications/screensavers/$hack.desktop ] && echo "%{_datadir}/applications/screensavers/$hack.desktop" >> %{name}-data-extra.lst
    echo "%{_libdir}/xscreensaver/$hack" >> %{name}-data-extra.lst
done

%files
%doc README
%{_bindir}/xscreensaver
%{_bindir}/xscreensaver-command
%{_bindir}/xscreensaver-demo
%{_bindir}/xscreensaver-gl-helper
%{_bindir}/xscreensaver-systemd
%{_datadir}/applications/xscreensaver-properties.desktop
%{_datadir}/pixmaps/xscreensaver.xpm
%dir %{_datadir}/xscreensaver
%{_datadir}/xscreensaver/ui
%dir %{_prefix}/lib/X11/app-defaults
%{_prefix}/lib/X11/app-defaults/XScreenSaver
%{_mandir}/man1/xscreensaver.*
%{_mandir}/man1/xscreensaver-command.*
%{_mandir}/man1/xscreensaver-demo.*
%{_mandir}/man6/xscreensaver-gl-helper.*
%{_mandir}/man1/xscreensaver-systemd.*
%config %{_sysconfdir}/pam.d/xscreensaver
%dir %{_sysconfdir}/xscreensaver/
%config %{_sysconfdir}/xscreensaver/README

%files lang -f %{name}.lang

%files data -f %{name}-data.lst
%dir %{_libdir}/xscreensaver/
%dir %{_sysconfdir}/xscreensaver/
%dir %{_datadir}/applications/screensavers/

%files data-extra -f %{name}-data-extra.lst
%dir %{_libdir}/xscreensaver/
%dir %{_sysconfdir}/xscreensaver/
%dir %{_datadir}/applications/screensavers/
# Screensavers using those utilities are in this package.
%{_bindir}/xscreensaver-getimage
%{_bindir}/xscreensaver-getimage-file
%{_bindir}/xscreensaver-getimage-video
%{_bindir}/xscreensaver-text
%{_mandir}/man1/xscreensaver-getimage.*
%{_mandir}/man1/xscreensaver-getimage-file.*
%{_mandir}/man1/xscreensaver-getimage-video.*
%{_mandir}/man1/xscreensaver-text.*

%changelog
