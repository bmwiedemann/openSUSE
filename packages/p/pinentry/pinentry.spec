#
# spec file for package pinentry
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


%define ncurses %(xxx="`readlink -f %{_includedir}/ncurses.h`"; echo $xxx)
%define nmajor  %(grep NCURSES_VERSION_MAJOR < %{_includedir}/ncurses.h)
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" != ""
%define nsuffix -%{flavor}
%endif

%bcond_without fltk

Name:           pinentry%{?nsuffix}
Version:        1.3.0
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
BuildRequires:  libassuan-devel >= 2.1.0
BuildRequires:  libgpg-error-devel >= 1.16
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
Provides:       pinentry-dialog
%if "%{flavor}" == "gui"
%if %{with fltk}
BuildRequires:  fltk-devel >= 1.3
%endif
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Test)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gcr-base-3)
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.12.0
BuildRequires:  pkgconfig(libsecret-1)
%ifnarch ppc
BuildRequires:  pkgconfig(efl)
%endif
%endif

%description
This is a collection of simple PIN or passphrase entry dialogs which
utilize the Assuan protocol as described by the Aegypten project.

%if "%{flavor}" == "gui"
%package -n pinentry-emacs
Summary:        Simple PIN or Passphrase Entry Dialog integrated into Emacs
Group:          Productivity/Other
Requires:       emacs
Requires:       pinentry
Provides:       pinentry-dialog
Provides:       pinentry-gui
Provides:       pinentry:%{_bindir}/pinentry-emacs

%description -n pinentry-emacs
A simple PIN or passphrase entry dialog utilize the Assuan protocol
as described by the Aegypten project, integrated into Emacs.

%package -n pinentry-efl
Summary:        Simple PIN or Passphrase Entry Dialog for EFL
Group:          Productivity/Other
Requires:       pinentry
Provides:       pinentry-dialog
Provides:       pinentry-gui
Provides:       pinentry:%{_bindir}/pinentry-efl

%description -n pinentry-efl
A simple PIN or passphrase entry dialog utilize the Assuan protocol
as described by the Aegypten project, using Enlightenment Foundation Libraries.

%package -n pinentry-gtk2
Summary:        Simple PIN or Passphrase Entry Dialog for GTK2
Group:          Productivity/Other
Requires:       pinentry
Provides:       pinentry-dialog
Provides:       pinentry-gui
Provides:       pinentry:%{_bindir}/pinentry-gtk-2

%description -n pinentry-gtk2
A simple PIN or passphrase entry dialog utilize the Assuan protocol
as described by the Aegypten project, using the GTK2 UI toolkit.

%package -n pinentry-gnome3
Summary:        Simple PIN or Passphrase Entry Dialog for GNOME
Group:          Productivity/Other
Requires:       pinentry
Provides:       pinentry-dialog
Provides:       pinentry-gui
Provides:       pinentry:%{_bindir}/pinentry-gnome3

%description -n pinentry-gnome3
A simple PIN or passphrase entry dialog utilize the Assuan protocol
as described by the Aegypten project, using GNOME libraries.

%if %{with fltk}
%package -n pinentry-fltk
Summary:        Collection of Simple PIN or Passphrase Entry Dialogs
Group:          Productivity/Other
Requires:       pinentry
Provides:       pinentry-dialog
Provides:       pinentry-gui
Provides:       pinentry:%{_bindir}/pinentry-fltk

%description -n pinentry-fltk
A simple PIN or passphrase entry dialog utilize the Assuan protocol
as described by the Aegypten project, using FLTK libraries.
%endif

%package -n pinentry-qt6
Summary:        Simple PIN or Passphrase Entry Dialog for QT5
Group:          Productivity/Other
Requires:       pinentry
Provides:       pinentry-dialog
Provides:       pinentry-gui
Provides:       pinentry-qt = %{version}
Obsoletes:      pinentry-qt <= 0.8.3
Provides:       pinentry-qt4 = %{version}-%{release}
Obsoletes:      pinentry-qt4 <= 0.9.7
Provides:       pinentry-qt5 = %{version}-%{release}
Obsoletes:      pinentry-qt5 <= 1.3.0

%description -n pinentry-qt6
A simple PIN or passphrase entry dialog utilize the Assuan protocol
as described by the Aegypten project, using the QT5 UI toolkit.
%endif

%prep
%autosetup -p1 -n pinentry-%{version}

%build
nmajor=$(sed -rn 's/^#define\s+NCURSES_VERSION_MAJOR\s+([0-9]+)/\1/p' %{_includedir}/ncurses.h)
CFLAGS="%{optflags} $(ncursesw${nmajor}-config --cflags)"
CXXFLAGS="%{optflags} $(ncursesw${nmajor}-config --cflags)"
LDFLAGS="$(ncursesw${nmajor}-config --libs)"
export CFLAGS CXXFLAGS LDFLAGS

%define _configure ../configure
%if "%{flavor}" == "gui"
# Regenerate moc's
# moc-qt6 qt/pinentrydialog.h > qt/pinentrydialog.moc
# moc-qt6 qt/pinentryconfirm.h > qt/pinentryconfirm.moc

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
%if %{with fltk}
	--enable-pinentry-fltk \
%else
        --disable-pinentry-fltk \
%endif
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
ln -s pinentry-qt %{buildroot}%{_bindir}/pinentry-qt6
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
%files -n pinentry-efl
%license COPYING
%attr(755,root,root) %{_bindir}/pinentry-efl
%endif

%files -n pinentry-emacs
%license COPYING
%attr(755,root,root) %{_bindir}/pinentry-emacs

%files -n pinentry-gtk2
%license COPYING
%attr(755,root,root) %{_bindir}/pinentry-gtk-2

%files -n pinentry-gnome3
%license COPYING
%attr(755,root,root) %{_bindir}/pinentry-gnome3

%if %{with fltk}
%files -n pinentry-fltk
%license COPYING
%attr(755,root,root) %{_bindir}/pinentry-fltk
%endif

%files -n pinentry-qt6
%license COPYING
%{_bindir}/pinentry-qt6
%{_bindir}/pinentry-qt5
%{_bindir}/pinentry-qt4
%attr(755,root,root) %{_bindir}/pinentry-qt
%{_datadir}/applications/org.gnupg.pinentry-qt.desktop
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
