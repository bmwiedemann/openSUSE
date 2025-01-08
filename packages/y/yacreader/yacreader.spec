#
# spec file for package yacreader
#
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


%define p7zip_version 16.02
%define srcext        tar.zst
Name:           yacreader
Version:        9.15.0
Release:        0
Summary:        The best way for reading your comics
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://www.yacreader.com
Source0:        yacreader-%{version}.%{srcext}
Source1:        unarr.%{srcext}
# Source URL: https://sourceforge.net/projects/p7zip/files/p7zip/16.02/p7zip_16.02_src_all.tar.bz2/download
Source2:        p7zip_%{p7zip_version}_src_all.tar.bz2
Patch1:         0001-fix-unarr.patch
BuildRequires:  desktop-file-utils
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
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  zstd
Requires:       hicolor-icon-theme

%description
A cross platform comic reader and library manager.

%prep
%setup -q -a 1 -a 2
mv unarr compressed_archive/unarr/unarr-master
%patch -P 1 -p1
mv p7zip_%{p7zip_version} compressed_archive/libp7zip

%build
qmake6
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
