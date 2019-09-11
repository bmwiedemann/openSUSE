#
# spec file for package pinentry
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define ncurses %(xxx="`readlink -f %{_includedir}/ncurses.h`"; echo $xxx)
%define nmajor  %(grep NCURSES_VERSION_MAJOR < %{_includedir}/ncurses.h)
Name:           pinentry
Version:        1.1.0
Release:        0
Summary:        Collection of Simple PIN or Passphrase Entry Dialogs
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            https://www.gnupg.org/aegypten/
Source:         ftp://ftp.gnupg.org/gcrypt/pinentry/%{name}-%{version}.tar.bz2
Source1:        ftp://ftp.gnupg.org/gcrypt/pinentry/%{name}-%{version}.tar.bz2.sig
Source2:        pinentry.keyring
Source3:        pinentry
Patch1:         pinentry-0.7.2-gtk+-2.4.diff
# PATCH-FIX-SUSE make it build with ncurses ABI 6
Patch7:         pinentry-ncurses6.diff
# PATCH-FIX-SUSE bsc#1141883 pinentry-qt crashes with QtCurve
Patch8:         pinentry-qt-Fix-use-of-dangling-pointer.patch
BuildRequires:  fltk-devel >= 1.3
BuildRequires:  libassuan-devel >= 2.1.0
BuildRequires:  libgpg-error-devel >= 1.16
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gcr-base-3)
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.4.0
BuildRequires:  pkgconfig(libsecret-1)
Requires(post): %{install_info_prereq}
Provides:       pinentry-dialog

%description
This is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the Aegypten project.

%package qt5
Summary:        Collection of Simple PIN or Passphrase Entry Dialogs
Group:          Productivity/Other
Requires:       pinentry
Provides:       pinentry-dialog
Provides:       pinentry-gui
Provides:       pinentry-qt = %{version}
Obsoletes:      pinentry-qt <= 0.8.3
Provides:       pinentry-qt4 = %{version}-%{release}
Obsoletes:      pinentry-qt4 <= 0.9.7

%description qt5
This is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the Aegypten project.

%package gtk2
Summary:        Collection of Simple PIN or Passphrase Entry Dialogs
Group:          Productivity/Other
Requires:       pinentry
Provides:       pinentry-dialog
Provides:       pinentry-gui
Provides:       pinentry:%{_bindir}/pinentry-gtk-2

%description gtk2
This is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the Aegypten project.

%package gnome3
Summary:        Collection of Simple PIN or Passphrase Entry Dialogs
Group:          Productivity/Other
Requires:       pinentry
Provides:       pinentry-dialog
Provides:       pinentry-gui
Provides:       pinentry:%{_bindir}/pinentry-gnome3

%description gnome3
This is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the Aegypten project.

%package emacs
Summary:        Collection of Simple PIN or Passphrase Entry Dialogs
Group:          Productivity/Other
Requires:       emacs
Requires:       pinentry
Provides:       pinentry-dialog
Provides:       pinentry-gui
Provides:       pinentry:%{_bindir}/pinentry-emacs

%description emacs
This is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the Aegypten project.

%package fltk
Summary:        Collection of Simple PIN or Passphrase Entry Dialogs
Group:          Productivity/Other
Requires:       pinentry
Provides:       pinentry-dialog
Provides:       pinentry-gui
Provides:       pinentry:%{_bindir}/pinentry-fltk

%description fltk
This package contains a simple PIN or passphrase entry dialog built
using the fltk GUI toolkit.

%prep
%setup -q
%patch1 -p1
%patch7
%patch8 -p1

%build
# Regenerate moc's
moc-qt5 qt/pinentrydialog.h > qt/pinentrydialog.moc
moc-qt5 qt/pinentryconfirm.h > qt/pinentryconfirm.moc
nmajor=$(sed -rn 's/^#define\s+NCURSES_VERSION_MAJOR\s+([0-9]+)/\1/p' %{_includedir}/ncurses.h)
CFLAGS="%{optflags} $(ncursesw${nmajor}-config --cflags)"
CXXFLAGS="%{optflags} -std=gnu++11 $(ncursesw${nmajor}-config --cflags)"
LDFLAGS="$(ncursesw${nmajor}-config --libs)"
export CFLAGS CXXFLAGS LDFLAGS

%define _configure ../configure
# build gui version with libsecret (bnc#934214)
mkdir gui
cd gui
%configure \
	--disable-pinentry-curses \
	--disable-pinentry-tty \
	--enable-libsecret \
	--enable-pinentry-qt \
	--enable-pinentry-gtk2 \
	--enable-pinentry-gnome3 \
	--enable-pinentry-emacs \
	--enable-inside-emacs \
	--enable-pinentry-fltk \
	--without-ncurses-include-dir
make %{?_smp_mflags}
# build text version without libsecret (bnc#934214)
cd ..
mkdir tui
cd tui
%configure \
	--enable-pinentry-curses \
	--enable-pinentry-tty \
	--disable-libsecret \
	--disable-pinentry-qt \
	--disable-pinentry-gtk2 \
	--disable-pinentry-gnome3 \
	--disable-pinentry-emacs \
	--disable-inside-emacs \
	--disable-pinentry-fltk \
	--without-ncurses-include-dir
make %{?_smp_mflags}

%install
cd tui
%make_install
cd ../gui
%make_install

# remove symlink
rm -rf %{buildroot}%{_bindir}/pinentry
# backward compatibility symlinks
ln -s pinentry-qt %{buildroot}%{_bindir}/pinentry-qt5
ln -s pinentry-qt %{buildroot}%{_bindir}/pinentry-qt4
cp %{SOURCE3} %{buildroot}%{_bindir}

%post
%install_info --info-dir=.%{_infodir} .%{_infodir}/pinentry.info.gz

%postun
%install_info_delete --info-dir=.%{_infodir} .%{_infodir}/pinentry.info.gz

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_infodir}/pinentry*
%attr(755,root,root) %{_bindir}/pinentry
%attr(755,root,root) %{_bindir}/pinentry-tty
%attr(755,root,root) %{_bindir}/pinentry-curses

%files qt5
%attr(755,root,root) %{_bindir}/pinentry-qt5
%attr(755,root,root) %{_bindir}/pinentry-qt4
%attr(755,root,root) %{_bindir}/pinentry-qt

%files gtk2
%attr(755,root,root) %{_bindir}/pinentry-gtk-2

%files gnome3
%attr(755,root,root) %{_bindir}/pinentry-gnome3

%files emacs
%attr(755,root,root) %{_bindir}/pinentry-emacs

%files fltk
%attr(755,root,root) %{_bindir}/pinentry-fltk

%changelog
