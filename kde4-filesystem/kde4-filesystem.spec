#
# spec file for package kde4-filesystem
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           kde4-filesystem
Url:            http://www.kde.org
Version:        4.14
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        KDE4 Directory Layout
License:        LGPL-2.1+
Group:          System/Fhs
Source0:        macros.kde4
Source1:        COPYING
Source99:       kde4-filesystem-rpmlintrc
Obsoletes:      akonadi-google              < 4.9.0
Obsoletes:      extragear-libs    < 4.1
Obsoletes:      kbattleship       < 4.7
Obsoletes:      kde4-fsview                 < 4.0
Obsoletes:      kde4-kbackgammon            < 4.0
Obsoletes:      kde4-kghostview             < 4.0
Obsoletes:      kde4-khexeditor             < 4.0
Obsoletes:      kde4-kmilo        < 4.1
Obsoletes:      kde4-kmobiletools < 4.1
Obsoletes:      kde4-knewsticker        < 4.2
Obsoletes:      kde4-korn         < 4.1
Obsoletes:      kde4-kpercentage  < 4.1
Obsoletes:      kde4-kpilot       < 4.1
Obsoletes:      kde4-kregexpeditor          < 4.0
Obsoletes:      kde4-ktnef              < 4.2
Obsoletes:      kde4-kworldclock  < 4.1
Obsoletes:      kde4-kxsldbg                < 4.0
Obsoletes:      kde4-noatun                 < 4.0
Obsoletes:      kde4-quanta                 < 4.0
Obsoletes:      kde4-secpolicy    < 4.1
Obsoletes:      kde4-style-phase        < 4.2
Obsoletes:      kdeaccessibility4 < 4.7
Obsoletes:      kdeaccessibility4-kicker    < 4.0
Obsoletes:      kdeaddons4                  < 4.0
Obsoletes:      kdeaddons4-kicker           < 4.0
Obsoletes:      kdeaddons4-knewsticker      < 4.0
Obsoletes:      kdeaddons4-konqueror        < 4.0
Obsoletes:      kdeaddons4-renamedlgplugins < 4.0
Obsoletes:      kdeadmin4         < 4.7
Obsoletes:      kdeartwork4       < 4.7
Obsoletes:      kdeartwork4-kwin        < 4.2
Obsoletes:      kdeartwork4-kworldclock < 4.2
Obsoletes:      kdeedu4           < 4.7
Obsoletes:      kdeedu4-noarch    < 4.7
Obsoletes:      kdegames4         < 4.7
Obsoletes:      kdemultimedia4    < 4.7
Obsoletes:      kdemultimedia4-thumbnailers < 4.9.0
Obsoletes:      kdenetwork4       < 4.7
Obsoletes:      kdepim4-wizards   < 4.8
Obsoletes:      kdesdk4           < 4.7
Obsoletes:      kdesdk4-kdeaccounts < 4.9.0
Obsoletes:      kdetoys4          < 4.7
Obsoletes:      kdetoys4-kicker             < 4.0
Obsoletes:      kdeutils4         < 4.7
Obsoletes:      klines            < 4.7
Obsoletes:      kmtrace-devel     < 4.7
Obsoletes:      kpilot < 4.4
Obsoletes:      ktron             < 4.7
Obsoletes:      ktuberling        < 4.7
Obsoletes:      kwikdisk          < 4.8
Obsoletes:      libkscan4         < 4.1
Obsoletes:      nepomuk-virtuoso-converter  < 4.9.0
Obsoletes:      phonon-backend-xine
Obsoletes:      plasma-addons-akonadi < 4.9.0
Obsoletes:      polkit-kde-kcmmodules-1 < 4.11.0

#
# keep in sync with macros.kde4
# TODO: can we include macros.kde4 directly to define it?
%define _kde_config_dir /usr/share/kde4/config

%description
This package installs the KDE directory structure.

%prep

%build

%install
install -D -m644 %{SOURCE0} %{buildroot}%{_sysconfdir}/rpm/macros.kde4
install -D -m644 %{SOURCE1} %{buildroot}%{_docdir}/kde4-filesystem/COPYING
mkdir -p %{buildroot}/%{_kde_config_dir}
mkdir -p %{buildroot}%{_datadir}/applications/kde4
for size in scalable 128x128 64x64 48x48 32x32 22x22 16x16; do
for type in actions apps devices filesystems mimetypes places status; do
  for theme in crystalsvg oxygen hicolor locolor; do
    mkdir -p %{buildroot}%{_datadir}/icons/$theme/$size/$type
  done
done
done
mkdir -p %{buildroot}%{_datadir}/icons/oxygen/scalable/apps/small/{16x16,32x32}
mkdir -p %{buildroot}%{_datadir}/icons/oxygen/scalable/status/small/{16x16,22x22,48x48}
mkdir -p %{buildroot}%{_datadir}/kde4/services/phononbackends
mkdir -p %{buildroot}%{_datadir}/kde4/services/ServiceMenus
mkdir -p %{buildroot}%{_datadir}/kde4/apps
mkdir -p %{buildroot}%{_datadir}/kde4/apps/color-schemes
mkdir -p %{buildroot}%{_datadir}/kde4/apps/khtml/kpartplugins
mkdir -p %{buildroot}%{_datadir}/kde4/apps/konqsidebartng/virtual_folders/services
mkdir -p %{buildroot}%{_datadir}/kde4/config.kcfg
mkdir -p %{buildroot}%{_includedir}/KDE
mkdir -p %{buildroot}%{_libdir}/kde4
mkdir -p %{buildroot}%{_libdir}/kde4/libexec
mkdir -p %{buildroot}%{_libdir}/kde4/plugins
for lang in `find /usr/share/locale/* -maxdepth 0 -type d -printf "%f\n"`; do mkdir -p %{buildroot}%{_datadir}/doc/kde/HTML/$lang; done

%files
%defattr(-,root,root)
%{_sysconfdir}/rpm/macros.kde4
%{_kde_config_dir}
%{_datadir}/kde4
%{_datadir}/applications/kde4
%{_datadir}/doc/kde
%{_datadir}/icons/*
%{_datadir}/kde4/services/phononbackends
%dir %{_docdir}/kde4-filesystem
%{_docdir}/kde4-filesystem/COPYING
%{_includedir}/KDE
%{_libdir}/kde4

%changelog
