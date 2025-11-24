#
# spec file for package android-file-transfer-linux
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           android-file-transfer-linux
Summary:        Android file fransfer for Linux
Version:        4.5
Release:        0
URL:            https://github.com/whoozle/android-file-transfer-linux
Source0:        %{name}-%{version}.tar.gz
License:        LGPL-2.1-only
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  readline-devel
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6NetworkAuth)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Widgets)
BuildRequires:  pkgconfig(fuse3)
BuildRequires:  pkgconfig(libcrypto)

%description
Android File Transfer for Linux — a MTP client with minimalist UI

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_libdir}/libmtp-ng-static.a

%files
%doc FAQ.md
%license LICENSE
%{_bindir}/aft-mtp-cli
%{_bindir}/aft-mtp-mount
%{_bindir}/android-file-transfer
%{_datadir}/metainfo/android-file-transfer.appdata.xml
%{_datadir}/applications/android-file-transfer.desktop
%{_datadir}/icons/hicolor/*/apps/android-file-transfer.png

%changelog
