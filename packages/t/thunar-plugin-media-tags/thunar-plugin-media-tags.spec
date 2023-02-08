#
# spec file for package thunar-plugin-media-tags
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


%define plugin_name thunar-media-tags-plugin

Name:           thunar-plugin-media-tags
URL:            https://docs.xfce.org/xfce/thunar/media-tags
Version:        0.4.0
Release:        0
Source0:        https://archive.xfce.org/src/thunar-plugins/thunar-media-tags-plugin/0.4/%{plugin_name}-%{version}.tar.bz2
Summary:        Thunar Plugin for Editing Media File Metadata and Renaming Based on Metadata
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
BuildRequires:  intltool
BuildRequires:  pkgconfig(glib-2.0) >= 2.50.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.0.0
BuildRequires:  pkgconfig(taglib) >= 1.4
BuildRequires:  pkgconfig(thunarx-3) >= 1.0.1
Requires:       thunar >= 1.7.0
Recommends:     %{name}-lang = %{version}
Provides:       %{plugin_name} = %{version}
Obsoletes:      %{plugin_name} < %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Thunar Media Tags Plugin enables editing media file metadata from within
the Thunar file properties dialog and allows for bulk renaming based on
metadata.

%lang_package

%prep
%setup -q -n %{plugin_name}-%{version}

%build
%configure --disable-static
make %{?_smp_mflags} V=1

%install
%make_install

rm -rf %{buildroot}%{_libdir}/thunarx-3/thunar-media-tags-plugin.la

# remove unsupported locales
rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{plugin_name} %{?no_lang_C}

%clean
rm -rf "%{buildroot}"

%files
%defattr(-,root,root)
%{_libdir}/thunarx-3/thunar-media-tags-plugin.so

%files lang -f %{plugin_name}.lang

%changelog
