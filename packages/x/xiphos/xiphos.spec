#
# spec file for package xiphos
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           xiphos
Version:        4.1.0
Release:        0
Summary:        GNOME-based Bible research tool
License:        GPL-2.0
Group:          Productivity/Scientific/Other
Url:            http://xiphos.org/
Source0:        https://github.com/crosswire/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.desktop
BuildRequires:  docbook-utils-minimal
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gnome-doc-utils-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  scrollkeeper
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(biblesync) >= 1.1.2
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-unix-print-2.0)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libgsf-1) >= 1.14
BuildRequires:  pkgconfig(libgtkhtml-4.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sword) >= 1.7.3
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
Requires:       sword
Recommends:     sword-bible
Recommends:     sword-commentary
Provides:       sword-frontend
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
./waf configure \
	--prefix=%{_prefix} \
	--enable-webkit2 \
	--gtk=3
./waf build

%install
./waf install --destdir=%{buildroot}
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file -n %{buildroot}%{_datadir}/applications/%{name}.desktop
# package docs with macro
rm -frv %{buildroot}/%{_datadir}/doc/%{name}
install -Dm644 xiphos.1 %{buildroot}%{_mandir}/man1/xiphos.1
install -Dm644 xiphos-nav.1 %{buildroot}%{_mandir}/man1/xiphos-nav.1
%fdupes -s %{buildroot}/%{_datadir}
%find_lang %{name}

%post
%icon_theme_cache_post

%postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc COPYING README.md RELEASE-NOTES Xiphos.ogg
%dir %{_datadir}/%{name}
%{_bindir}/xiphos*
%{_datadir}/xiphos/*
%{_datadir}/icons/hicolor/scalable/apps/*
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/appdata
%{_datadir}/appdata/xiphos.appdata.xml
%{_mandir}/man1/*
%dir %{_datadir}/omf

%files lang -f %{name}.lang
%defattr(-, root, root)

%changelog
