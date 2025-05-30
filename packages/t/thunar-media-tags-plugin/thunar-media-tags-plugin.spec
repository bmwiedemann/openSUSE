#
# spec file for package thunar-media-tags-plugin
#
# Copyright (c) 2025 SUSE LLC
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


Name:           thunar-media-tags-plugin
URL:            https://docs.xfce.org/xfce/thunar/media-tags
Version:        0.6.0
Release:        0
Source0:        https://archive.xfce.org/src/thunar-plugins/thunar-media-tags-plugin/0.6/%{name}-%{version}.tar.xz
Summary:        Thunar Plugin for Editing Media File Metadata and Renaming Based on Metadata
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
BuildRequires:  meson >= 0.56.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.18.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.18.0
BuildRequires:  pkgconfig(taglib) >= 1.4
BuildRequires:  pkgconfig(thunarx-3) >= 4.18.0
Requires:       thunar >= 4.18.0
Recommends:     %{name}-lang = %{version}
Provides:       thunar-plugin-media-tags = %{version}
Obsoletes:      thunar-plugin-media-tags < %{version}

%description
The Thunar Media Tags Plugin enables editing media file metadata from within
the Thunar file properties dialog and allows for bulk renaming based on
metadata.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

rm -rf %{buildroot}%{_libdir}/thunarx-3/thunar-media-tags-plugin.la

# remove unsupported locales
rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name} %{?no_lang_C}

%files
%{_libdir}/thunarx-3/thunar-media-tags-plugin.so

%files lang -f %{name}.lang

%changelog
