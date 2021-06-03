#
# spec file for package xiphos
#
# Copyright (c) 2021 SUSE LLC
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


Name:           xiphos
Version:        4.2.1.7
Release:        0
Summary:        GNOME-based Bible research tool
License:        GPL-2.0-only
Group:          Productivity/Scientific/Other
URL:            http://xiphos.org/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}.desktop
# PATCH-FIX-OPENSUSE find_biblesync.patch mcepl@suse.com
# Allow working with ancient cmake 3.10 on SLE/Leap 15.
Patch1:         find_biblesync.patch
Patch2:         xiphos-glib.patch
BuildRequires:  appstream-glib
BuildRequires:  cmake
# BuildRequires:  docbook-utils-minimal
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gnome-doc-utils-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  pkgconfig
BuildRequires:  python3-lxml
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  zip
BuildRequires:  pkgconfig(biblesync) >= 1.2.0
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-unix-print-2.0)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libgtkhtml-4.0)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.8
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(sword) >= 1.8.1
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(yelp-xsl)
Requires:       sword
Recommends:     %{name}-lang
Recommends:     sword-bible
Recommends:     sword-commentary
Provides:       sword-frontend

%description
Bible Study Software for the Linux community. Lookup and search Bible texts and
commentaries. Xiphos uses modules and libraries from the SWORD Project.
Display multiple translations in the interlinear window. Search for passages in
any translation by word, phrase, or regular expression. Install this package
if you want to browse the Bible translations and reference works distributed
by Crosswire Bible Society through the SWORD Project.

%lang_package

%prep
%setup -q
echo %{version} >cmake/source_version.txt
%if 0%{?suse_version} < 1550
%patch1 -p1
%endif
%patch2 -p1

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
export PYTHON="%{_bindir}/python3"
%cmake -DGTKHTML=ON
make %{?_smp_mflags}

%install
%cmake_install
%if 0%{?suse_version} < 1550
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file -n %{buildroot}%{_datadir}/applications/%{name}.desktop
%else
%suse_update_desktop_file %{name} Education Spirituality
%endif
# package docs with macro
rm -frv %{buildroot}/%{_datadir}/doc/%{name}
install -D -m644 -t %{buildroot}%{_mandir}/man1/ build/desktop/xiphos*.1
%fdupes -s %{buildroot}/%{_datadir}
%find_lang %{name}

%if 0%{?suse_version} < 1330
%post
%icon_theme_cache_post

%postun
%icon_theme_cache_postun
%endif

%files
%license COPYING
%doc README.md RELEASE-NOTES doc/Xiphos.ogg AUTHORS ChangeLog
%dir %{_datadir}/%{name}
%{_bindir}/xiphos*
%{_datadir}/xiphos/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/appdata
%{_datadir}/appdata/xiphos.appdata.xml
%{_mandir}/man1/*

%files lang -f %{name}.lang

%changelog
