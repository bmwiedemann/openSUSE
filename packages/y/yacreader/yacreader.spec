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
Version:        10.0.0
Release:        0
Summary:        The best way for reading your comics
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://www.yacreader.com
Source0:        %{gitlink}/releases/download/%{version}/%{name}-%{version}-src.tar.xz
BuildRequires:  fdupes
BuildRequires:  glu-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpoppler-qt6-devel
BuildRequires:  mozilla-nss
BuildRequires:  qt6-base-devel
BuildRequires:  qt6-base-private-devel
BuildRequires:  qt6-declarative-devel
BuildRequires:  qt6-linguist-devel
BuildRequires:  qt6-multimedia-devel
BuildRequires:  qt6-shadertools-devel
BuildRequires:  qt6-texttospeech-devel
BuildRequires:  qt6-qml-devel
BuildRequires:  qt6-qt5compat-devel
BuildRequires:  qt6-quickcontrols2-devel
BuildRequires:  qt6-sql-devel
BuildRequires:  qt6-svg-devel
BuildRequires:  libarchive-devel
BuildRequires:  zstd
Requires:       kf6-kimageformats

%description
A cross platform comic reader and library manager.

%prep
%autosetup
sed -i \
 's|DESTINATION ${CMAKE_INSTALL_LIBDIR}/systemd/user|DESTINATION lib/systemd/user|' \
 YACReaderLibraryServer/CMakeLists.txt

%build
%cmake	-DBUILD_TESTS=OFF \
        -DBUILD_SERVER_STANDALONE=OFF \
        -DCMAKE_SKIP_RPATH=ON \
        -DDECOMPRESSION_BACKEND=libarchive
%make_build

%install
%cmake_install
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
