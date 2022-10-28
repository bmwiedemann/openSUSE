#
# spec file for package nfoview
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


Name:           nfoview
Version:        1.29
Release:        0
Summary:        Simple Viewer for NFO Files
License:        GPL-3.0-or-later
Group:          Productivity/Text/Utilities
URL:            https://otsaloma.io/nfoview/
Source:         https://github.com/otsaloma/nfoview/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gettext
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Recommends:     terminus-font
BuildArch:      noarch

%description
NFO Viewer is a simple viewer for NFO files, which are "ASCII" art in
the CP437 codepage. The advantages of using NFO Viewer instead of a text
editor are preset font and encoding settings, automatic window size and
clickable hyperlinks.

%lang_package

%prep
%autosetup -p1

%build
%make_build

%install
%make_install PREFIX=/usr
%suse_update_desktop_file -r io.otsaloma.nfoview Office Viewer
%find_lang %{name}

%files
%doc AUTHORS.md NEWS.md README.md
%license COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/metainfo/io.otsaloma.nfoview.appdata.xml
%{_datadir}/applications/io.otsaloma.nfoview.desktop
%{_datadir}/icons/hicolor/*/apps/io.otsaloma.nfoview*.svg
%{_mandir}/man?/*
%{python3_sitelib}/%{name}
%{python3_sitelib}/*.egg-info

%files lang -f %{name}.lang

%changelog
