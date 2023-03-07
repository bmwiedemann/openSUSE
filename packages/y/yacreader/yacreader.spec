#
# spec file for package yacreader
#
# Copyright (c) 2019 Xu Zhao (i@xuzhao.net).
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
%define unarr_version 569ffdb
%define p7zip_version 16.02
Name:            yacreader
Version:         9.11.0
Release:         0
Summary:         The best way for reading your comics
License:         GPL-3.0-or-later
Group:           Productivity/Graphics/Viewers
Url:             https://www.yacreader.org
Source0:         https://github.com/YACReader/yacreader/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:         unarr-%{unarr_version}.zip
# Source URL: https://sourceforge.net/projects/p7zip/files/p7zip/16.02/p7zip_16.02_src_all.tar.bz2/download
Source2:         p7zip_%{p7zip_version}_src_all.tar.bz2
Patch1:          0001-fix-unarr.patch
BuildRequires:   unzip
BuildRequires:   libqt5-linguist
BuildRequires:   libqt5-qtbase-devel
BuildRequires:   libqt5-qtmultimedia-devel
BuildRequires:   libqt5-qtscript-devel
BuildRequires:   libqt5-qtdeclarative-devel
BuildRequires:   libqt5-qtsvg-devel
BuildRequires:   libQt5Sql5-sqlite
BuildRequires:   libQt5QuickControls2-devel
BuildRequires:   libpoppler-qt5-devel
BuildRequires:   glu-devel
BuildRequires:   desktop-file-utils
BuildRequires:   update-desktop-files
BuildRequires:   fdupes
BuildRequires:   mozilla-nss
BuildRequires:   hicolor-icon-theme
Requires:        hicolor-icon-theme

%description
A cross platform comic reader and library manager.

%prep
%setup -q -a 1 -a 2
mv unarr-%{unarr_version} compressed_archive/unarr/unarr-master
%patch1 -p1
mv p7zip_%{p7zip_version} compressed_archive/libp7zip

%build
qmake-qt5
make %{?_smp_mflags}

%install
INSTALL_ROOT=%{buildroot} %make_install
rm %{buildroot}/%{_datadir}/applications/*.desktop
%suse_update_desktop_file -i YACReader
%suse_update_desktop_file -i YACReaderLibrary
%fdupes %{buildroot}

%files
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/yacreader
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/doc/yacreader
/usr/lib/systemd/user/yacreaderlibraryserver.service

%changelog
