#
# spec file for package cherrytree
#
# Copyright (c) 2022 SUSE LLC
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


Name:           cherrytree
Version:        0.99.52
Release:        0
Summary:        A hierarchical note taking application
License:        GPL-3.0-or-later AND LGPL-2.1-only
Group:          Productivity/Office/Other
URL:            https://www.giuspen.com/cherrytree/
Source0:        %{name}-%{version}.tar.xz
#PATCH-FIX-OPENSUSE cherrytree-set-git-version.patch malcolmlewis@opensuse.org -- Set git version in help about.
Patch0:         cherrytree-set-git-version.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  python3-lxml
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(fmt)
BuildRequires:  pkgconfig(gspell-1)
BuildRequires:  pkgconfig(gtkmm-3.0)
BuildRequires:  pkgconfig(gtksourceviewmm-3.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml++-2.6)
BuildRequires:  pkgconfig(spdlog) >= 1.5
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(uchardet)
BuildRequires:  pkgconfig(vte-2.91)
# For password-protected format
Recommends:     p7zip-full

%description
A hierarchical note taking application, featuring rich text and syntax
highlighting, storing all the data (including images) in a single xml
file with extension ".ctd".

%lang_package

%prep
%autosetup -p1

%build
#Disable build tests as this needs cpputest and static development files!
%cmake -DBUILD_TESTING=OFF -DCT_VERSION=%{version}
%cmake_build

%install
%cmake_install
# Remove old mime registration files
rm %{buildroot}%{_datadir}/mime-info/cherrytree.*
%suse_update_desktop_file -G "Hierarchical Notes Utility" cherrytree TextEditor
%find_lang %{name} %{?no_lang_C}
%fdupes -s %{buildroot}%{_datadir}

%files
%license license.txt
%doc changelog.txt
%{_bindir}/cherrytree
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/net.giuspen.cherrytree.metainfo.xml
%{_datadir}/applications/cherrytree.desktop
%{_datadir}/cherrytree/
%{_datadir}/icons/hicolor/scalable/apps/cherrytree.svg
%{_mandir}/man1/cherrytree.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
