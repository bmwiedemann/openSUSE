#
# spec file for package yacreader
#
# Copyright (c) 2026 mantarimay
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2019 Xu Zhao (i@xuzhao.net).
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


%define gitlink https://github.com/YACReader/yacreader
Name:           yacreader
Version:        9.16.3
Release:        0
Summary:        The best way for reading your comics
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://www.yacreader.com
Source0:        %{gitlink}/releases/download/%{version}/%{name}-%{version}-src.tar.xz
Source1:        unarr.tar.zst
BuildRequires:  fdupes
BuildRequires:  glu-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpoppler-qt6-devel
BuildRequires:  mozilla-nss
BuildRequires:  qt6-base-devel
BuildRequires:  qt6-declarative-devel
BuildRequires:  qt6-linguist-devel
BuildRequires:  qt6-multimedia-devel
BuildRequires:  qt6-qml-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qt6-quickcontrols2-devel
BuildRequires:  qt6-sql-devel
BuildRequires:  qt6-svg-devel
BuildRequires:  zstd

%description
A cross platform comic reader and library manager.

%prep
%setup -q -a 1
mv unarr compressed_archive/unarr/unarr-master
# fix build unarr
sed -i '/Ppmd7Dec.c\\/a\ \t\t$$PWD/unarr-master/lzmasdk/Ppmd7aDec.c\\' \
   compressed_archive/unarr/unarr.pro

%build
qmake6
make %{?_smp_mflags}

%install
INSTALL_ROOT=%{buildroot} %make_install
rm %{buildroot}/usr/share/doc/yacreader/CHANGELOG.md
%fdupes %{buildroot}

%files
%doc README.md CHANGELOG.md
%license COPYING.txt
%{_bindir}/YACReader
%{_bindir}/YACReaderLibrary
%{_bindir}/YACReaderLibraryServer
%{_mandir}/man1/*
%{_datadir}/yacreader
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*
%{_userunitdir}/yacreaderlibraryserver.service

%changelog
