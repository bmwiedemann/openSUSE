#
# spec file for package pinentry
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


%define ncurses %(xxx="`readlink -f %{_includedir}/ncurses.h`"; echo $xxx)
%define nmajor  %(grep NCURSES_VERSION_MAJOR < %{_includedir}/ncurses.h)
%global flavor @BUILD_FLAVOR@%{nil}
Name:           pinentry
Version:        1.1.1
Release:        0
Summary:        Collection of Simple PIN or Passphrase Entry Dialogs
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            https://www.gnupg.org/aegypten/
Source:         https://www.gnupg.org/ftp/gcrypt/pinentry/pinentry-%{version}.tar.bz2
Source1:        https://www.gnupg.org/ftp/gcrypt/pinentry/pinentry-%{version}.tar.bz2.sig
# https://www.gnupg.org/signature_key.html
# https://incenp.org/srv/dgouttegattat.asc
Source2:        pinentry.keyring
Source3:        pinentry
Patch1:         pinentry-0.7.2-gtk+-2.4.diff
BuildRequires:  fltk-devel >= 1.3
BuildRequires:  libassuan-devel >= 2.1.0
BuildRequires:  libgpg-error-devel >= 1.16
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
%if "%{flavor}" == "gui"
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
%ifnarch ppc
BuildRequires:  pkgconfig(efl)
%endif
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gcr-base-3)
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.12.0
BuildRequires:  pkgconfig(libsecret-1)
%endif
Provides:       pinentry-dialog

%description
This is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the Aegypten project.

%if "%{flavor}" == "gui"
%package emacs
Summary:        Simple PIN or Passphrase Entry Dialog integrated into Emacs
Group:          Productivity/Other
Requires:       emacs
Requires:       pinentry
Provides:       pinentry-dialog
Provides:       pinentry-gui
Provides:       pinentry:%{_bindir}/pinentry-emacs

%description emacs
A simple PIN or passphrase entry dialog utilize the Assuan protocol
as described by the Aegypten project, integrated into Emacs.

%package efl
Summary:        Simple PIN or Passphrase Entry Dialog for EFL
Group:          Productivity/Other
Requires:       pinentry
Provides:       pinentry-dialog
Provides:       pinentry-gui
Provides:       pinentry:%{_bindir}/pinentry-efl

%description efl
A simple PIN or passphrase entry dialog utilize the Assuan protocol
as described by the Aegypten project, using Enlightenment Foundation Libraries.

%package gtk2
Summary:        Simple PIN or Passphrase Entry Dialog for GTK2
Group:          Productivity/Other
Requires:       pinentry
Provides:       pinentry-dialog
Provides:       pinentry-gui
Provides:       pinentry:%{_bindir}/pinentry-gtk-2

%description gtk2
A simple PIN or passphrase entry dialog utilize the Assuan protocol
as described by the Aegypten project, using the GTK2 UI toolkit.

%package gnome3
Summary:        Simple PIN or Passphrase Entry Dialog for GNOME
Group:          Productivity/Other
Requires:       pinentry
Provides:       pinentry-dialog
Provides:       pinentry-gui
Provides:       pinentry:%{_bindir}/pinentry-gnome3

%description gnome3
A simple PIN or passphrase entry dialog utilize the Assuan protocol
as described by the Aegypten project, using GNOME libraries.

%package fltk
Summary:        Collection of Simple PIN or Passphrase Entry Dialogs
Group:          Productivity/Other
Requires:       pinentry
Provides:       pinentry-dialog
Provides:       pinentry-gui
Provides:       pinentry:%{_bindir}/pinentry-fltk

%description fltk
A simple PIN or passphrase entry dialog utilize the Assuan protocol
as described by the Aegypten project, using FLTK libraries.

%package qt5
Summary:        Simple PIN or Passphrase Entry Dialog for QT5
Group:          Productivity/Other
Requires:       pinentry
Provides:       pinentry-dialog
Provides:       pinentry-gui
Provides:       pinentry-qt = %{version}
Obsoletes:      pinentry-qt <= 0.8.3
Provides:       pinentry-qt4 = %{version}-%{release}
Obsoletes:      pinentry-qt4 <= 0.9.7

%description qt5
A simple PIN or passphrase entry dialog utilize the Assuan protocol
as described by the Aegypten project, using the QT5 UI toolkit.
%endif

%prep
%setup -q
%patch1 -p1

%build
nmajor=$(sed -rn 's/^#define\s+NCURSES_VERSION_MAJOR\s+([0-9]+)/\1/p' %{_includedir}/ncurses.h)
CFLAGS="%{optflags} $(ncursesw${nmajor}-config --cflags)"
CXXFLAGS="%{optflags} -std=gnu++11 $(ncursesw${nmajor}-config --cflags)"
LDFLAGS="$(ncursesw${nmajor}-config --libs)"
export CFLAGS CXXFLAGS LDFLAGS

%define _configure ../configure
%if "%{flavor}" == "gui"
# Regenerate moc's
moc-qt5 qt/pinentrydialog.h > qt/pinentrydialog.moc
moc-qt5 qt/pinentryconfirm.h > qt/pinentryconfirm.moc

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
	--enable-pinentry-efl \
	--without-ncurses-include-dir
%make_build
# build text version without libsecret (bnc#934214)
cd ..
%else
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
	--disable-pinentry-efl \
	--without-ncurses-include-dir
%make_build
%endif

%install
%if "%{flavor}" == "gui"
cd gui
%make_install
cd ..

# backward compatibility symlinks
ln -s pinentry-qt %{buildroot}%{_bindir}/pinentry-qt5
ln -s pinentry-qt %{buildroot}%{_bindir}/pinentry-qt4
rm -rf %{buildroot}%{_infodir}
rm -rf %{buildroot}%{_bindir}/pinentry
%else
cd tui
%make_install
cd ..

# remove symlink
rm -rf %{buildroot}%{_bindir}/pinentry
install -p -m 755 -D %{SOURCE3} %{buildroot}%{_bindir}/pinentry

%post
%install_info --info-dir=.%{_infodir} .%{_infodir}/pinentry.info.gz

%postun
%install_info_delete --info-dir=.%{_infodir} .%{_infodir}/pinentry.info.gz
%endif

%if "%{flavor}" == "gui"

%ifnarch ppc
%files efl
%license COPYING
%attr(755,root,root) %{_bindir}/pinentry-efl
%endif

%files emacs
%license COPYING
%attr(755,root,root) %{_bindir}/pinentry-emacs

%files gtk2
%license COPYING
%attr(755,root,root) %{_bindir}/pinentry-gtk-2

%files gnome3
%license COPYING
%attr(755,root,root) %{_bindir}/pinentry-gnome3

%files fltk
%license COPYING
%attr(755,root,root) %{_bindir}/pinentry-fltk

%files qt5
%license COPYING
%{_bindir}/pinentry-qt5
%{_bindir}/pinentry-qt4
%attr(755,root,root) %{_bindir}/pinentry-qt
%else
%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_infodir}/pinentry*
%attr(755,root,root) %{_bindir}/pinentry
%attr(755,root,root) %{_bindir}/pinentry-tty
%attr(755,root,root) %{_bindir}/pinentry-curses

%endif

%changelog
