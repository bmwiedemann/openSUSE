#
# spec file for package x3270
#
# Copyright (c) 2025 SUSE LLC
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


%define _suffix ga10
%define _fullname suite3270-%{version}%{_suffix}
%define _x026ver 1.2
Name:           x3270
Version:        4.3
Release:        0
Summary:        A Family of IBM 3270 Terminal Emulators
License:        MIT
Group:          System/X11/Terminals
URL:            https://x3270.miraheze.org
#Git-Clone:     https://github.com/pmattes/x3270
Source0:        https://download.sourceforge.net/x3270/%{_fullname}-src.tgz
Source1:        https://download.sourceforge.net/x3270/x026-%{_x026ver}.tgz
Source2:        x3270.desktop
Patch0:         mknod.patch
Patch100:       usr_local_bin.patch
Patch102:       x026-offset.diff
# fix build with gcc 15
Patch103:       x3270-gcc15.patch
BuildRequires:  bdftopcf
BuildRequires:  fdupes
BuildRequires:  fontpackages-devel
BuildRequires:  freetype2
BuildRequires:  imake
BuildRequires:  mkfontdir
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  tcl-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)

%description
This package contains a family of IBM 3270 mainframe terminal
emulators:

* terminal emulators for interactive use x3270	X Window System
   c3270  curses based

* terminal emulators for scripted use s3270    see the x3270-script
   man page tcl3270  Tcl based

* printer emulator pr3287

* do not miss the punch card puncher emulator x026

x3270 is an IBM 3270 terminal emulator for the X Window System.  x3270
runs over a telnet connection (with or without TN3270E) and emulates
either an IBM 3279 (color) or 3278 (monochrome).  It supports APL2
characters, IND$FILE file transfer, NVT mode, a pop-up keypad for
3270-specific keys, alternative keymaps, 3287 printer sessions, and a
scrollbar and has extensive debugging and scripting facilities.

x3270a is a script that computes the correct font sizes for
higher-resolution displays, then runs x3270.
(x3270 handles scaling of visual elements automatically,
but it cannot adjust the font sizes by itself.)

b3270 is a generic back-end for 3270 emulators.
It implements the 3270 protocol and host input/output,
and communicates with a front end application using a simple XML-based protocol.

c3270 is the curses-based version of x3270.  It runs on any dumb
terminal (an xterm or a console, for example), and supports (almost)
all of the x3270 features.  c3270 scripts are compatible with x3270
scripts, and the subset of command line options and resource
definitions are also compatible.

s3270 is a scripting-only version of x3270.  This program is intended
primarily for writing "screen-scraping" applications, for example a CGI
back-end script that retrieves database information from a mainframe.

tcl3270 is a Tcl-based 3270 scripting engine.  It lets you write Tcl
scripts that manipulate 3270 sessions, and is quite a bit easier to set
up and use than s3270.

pr3287 is the printer companion for the above tools, and allows printer
output from a 3270 session to be directed to a Unix printer queue.

x026 is a fun toy which emulates an x026 puncher.

%prep
# the source-packages all extract to corresponding subdirectories.
# they are all expanded below a 'all3270' directory.  this directory
# will also hold the common config.cache
# -q uietly -c reate -name all3270
# -a fter changing into all3270, expand sources
%setup -q -n suite3270-%{version} -a1
%patch -P 0
%patch -P 100
%patch -P 102
%patch -P 103

find . -name ".gitignore" -delete

%build
export CFLAGS="%{optflags}"
export LIBX3270DIR=%{_sysconfdir}/x3270
%configure \
  --disable-windows \
  --disable-windows-lib \
  --enable-lib \
  --enable-unix \
  --enable-ssl \
  --x-includes=%{_includedir} \
  --x-libraries=%{_libdir} \
  --with-all-xinstall \
  --with-iconv \
  --with-fontdir=%{_miscfontsdir}
# There is broken generated makefile
sed -i -e 's:$(FALLBACKS_:$(FALLBACKS):g' x3270/Makefile
%make_build LIBX3270DIR=${LIBX3270DIR} unix CC="gcc %{optflags}"
# the IBM 026 keypunch emulator
cd x026-%{_x026ver}
    xmkmf
    %make_build
cd ..

%install
export LIBX3270DIR=%{_sysconfdir}/x3270
# create the default directory structure in the build root
mkdir --parents %{buildroot}{%{_bindir},%{_mandir}/{man1,man5}}
make DESTDIR=%{buildroot} LIBX3270DIR=${LIBX3270DIR} install
make DESTDIR=%{buildroot} LIBX3270DIR=${LIBX3270DIR} install.man
# the IBM 026 keypunch emulator
cd x026-%{_x026ver}
    make DESTDIR=%{buildroot} install install.man
cd ..
# move site config files to the standard locations
mkdir -p %{buildroot}%{_libexecdir}/x3270
# this is a per-site, not a per-machine config file
chmod 644 %{buildroot}%{_sysconfdir}/x3270/ibm_hosts
# set permissions correct
chmod ugo-x %{buildroot}%{_mandir}/man{1,5}/*
# make install does a mkfontdir, that creates a fonts.dir we don't
# want in the package.  remove that:
rm %{buildroot}%{_miscfontsdir}/fonts.dir

# copy the docs
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -pr --parents x3270/{Examples,html} %{buildroot}%{_docdir}/%{name}
cp -pr --parents b3270/html %{buildroot}%{_docdir}/%{name}
cp -pr --parents c3270/html %{buildroot}%{_docdir}/%{name}
cp -pr --parents pr3287/html %{buildroot}%{_docdir}/%{name}
cp -pr --parents s3270/{Examples,html} %{buildroot}%{_docdir}/%{name}
cp -pr --parents tcl3270/{Examples,html} %{buildroot}%{_docdir}/%{name}
# create symlinks in documentation
%fdupes -s %{buildroot}/%{_docdir}

install -D -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/x3270.desktop
%suse_update_desktop_file x3270

%post
%desktop_database_post
%reconfigure_fonts_post

%postun
%desktop_database_postun
%reconfigure_fonts_postun

%posttrans
%reconfigure_fonts_posttrans

%files
%defattr(-,root,root,755)
# common files
%dir %{_sysconfdir}/x3270
%dir %{_docdir}/%{name}
%dir %{_docdir}/%{name}/*
%config(noreplace) %{_sysconfdir}/x3270/ibm_hosts
%{_mandir}/man5/ibm_hosts.5%{?ext_man}
%{_mandir}/man1/x3270if.1%{?ext_man}
%{_bindir}/x3270if
# x3270
%{_bindir}/x3270
%{_bindir}/x3270a
%{_bindir}/prtodir
%dir %{_miscfontsdir}
%{_miscfontsdir}/*
%{_mandir}/man1/x3270.1%{?ext_man}
%doc %{_docdir}/%{name}/x3270/Examples
%doc %{_docdir}/%{name}/x3270/html
%{_datadir}/applications/x3270.desktop
# b3270
%{_bindir}/b3270
%{_mandir}/man1/b3270.1%{?ext_man}
%doc %{_docdir}/%{name}/b3270/html
# c3270
%{_bindir}/c3270
%{_mandir}/man1/c3270.1%{?ext_man}
%doc %{_docdir}/%{name}/c3270/html
# pr3287
%{_bindir}/pr3287
%{_mandir}/man1/pr3287.1%{?ext_man}
%doc %{_docdir}/%{name}/pr3287/html
# s3270
%{_bindir}/s3270
%{_mandir}/man1/s3270.1%{?ext_man}
%doc %{_docdir}/%{name}/s3270/Examples
%doc %{_docdir}/%{name}/s3270/html
# tcl3270
%{_bindir}/tcl3270
%{_mandir}/man1/tcl3270.1%{?ext_man}
%doc %{_docdir}/%{name}/tcl3270/Examples
%doc %{_docdir}/%{name}/tcl3270/html
# x026
%{_bindir}/x026
%{_mandir}/man1/x026.1x%{ext_man}

%changelog
