#
# spec file for package kchmviewer
#
# Copyright (c) 2023 SUSE LLC
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


Name:           kchmviewer
Version:        8.0
Release:        0
Summary:        KDE CHM and ePub Viewer
License:        GPL-3.0-only
Group:          Productivity/Office/Other
URL:            https://www.kchmviewer.net/
Source:         https://github.com/gyunaev/kchmviewer/archive/refs/tags/RELEASE_8_0.tar.gz
# PATCH-FIX-UPSTREAM git 9ac73e7ad15de08aab6b1198115be2eb44da7afe
Patch0:         url-scheme.patch
# PATCH-FIX-UPSTREAM git 99a6d94bdfce9c4578cce82707e71863a71d1453
Patch1:         qtwebengine-1-linkClicked.patch
# PATCH-FIX-UPSTREAM git 99a6d94bdfce9c4578cce82707e71863a71d1453
Patch2:         qtwebengine-2-createWindow.patch
# PATCH-FIX-UPSTREAM git 99a6d94bdfce9c4578cce82707e71863a71d1453
Patch3:         qtwebengine-3-synchronize-url.patch
# PATCH-FIX-UPSTREAM git a4a3984465cb635822953350c571950ae726b539
Patch4:         no-webkit.patch
# PATCH-FIX-OPENSUSE
Patch5:         InitialPreference-greater-than-okular.patch
# PATCH-FIX-OPENSUSE https://github.com/gyunaev/kchmviewer/pull/17
Patch6:         rename-desktop-file.patch
# PATCH-FIX-UPSTREAM - kchmviewer-adding-support-for-old-single-pass-gcc-linker.patch - https://github.com/gyunaev/kchmviewer/commit/e3b09edbbae17ad19661a7514afe5a9d84ca0ffa
Patch7:         kchmviewer-adding-support-for-old-single-pass-gcc-linker.patch
BuildRequires:  chmlib-devel
BuildRequires:  libQt5Core-devel
BuildRequires:  libQt5DBus-devel
BuildRequires:  libQt5Widgets-devel
BuildRequires:  libQt5Xml-devel
BuildRequires:  libqt5-qtbase-common-devel
BuildRequires:  libqt5-qtwebengine-devel
BuildRequires:  libzip-devel

%description
This is a viewer for ebooks and documentation in CHM (Microsoft Compiled HTML) and ePub formats.
It supports complex searching for large books and has various viewing features.

%prep
%autosetup -p1 -n kchmviewer-RELEASE_8_0

%build
%qmake5
%make_jobs

%install
mkdir -p %{buildroot}%{_bindir}
install -pm755 bin/kchmviewer %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/applications
install -pm644 packages/net.kchmviewer.kchmviewer.desktop %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps
install -pm644 packages/kchmviewer.png %{buildroot}%{_datadir}/pixmaps

%files
%license COPYING
%doc ChangeLog FAQ README
%{_bindir}/kchmviewer
%{_datadir}/applications/net.kchmviewer.kchmviewer.desktop
%{_datadir}/pixmaps/kchmviewer.*

%changelog
