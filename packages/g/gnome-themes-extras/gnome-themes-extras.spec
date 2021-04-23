#
# spec file for package gnome-themes-extras
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gnome-themes-extras
Version:        2.22.0
Release:        0
Summary:        Additional GNOME Themes
License:        GPL-2.0-only AND GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            http://www.gnome.org/
Source:         http://download.gnome.org/sources/gnome-themes-extras/2.22/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM 0001-Fix-to-http-bugzilla.gnome.org-show_bug.cgi-id-52832.patch bgo#528322 michal@sawicz.net -- Fix Darklooks's gtkrc tooltip definitions (fixed upstream but not released since 2008.04)
Patch0:         0001-Fix-to-http-bugzilla.gnome.org-show_bug.cgi-id-52832.patch
BuildRequires:  fdupes
BuildRequires:  glib2-devel
# FIXME: Should be a part of gtk2-engines-devel, which is not yet splitted:
BuildRequires:  gtk2-devel
BuildRequires:  gtk2-engines-devel
BuildRequires:  icon-naming-utils
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  translation-update-upstream
Requires:       gnome-themes
Enhances:       gnome-themes
BuildArch:      noarch

%description
This package contains several extra GNOME themes.

%prep
%setup -q
%patch0 -p1
translation-update-upstream

%build
autoreconf -f -i
%configure
make %{?_smp_mflags}

%install
%make_install
mkdir -p %{buildroot}%{_docdir}/%{name}
find -name AUTHORS -o -name "COPYING*" -o -name "README*" -o -name TODO -o -name "ChangeLog*" -o -name MAINTAINERS -o -name "*NEWS*" |
    while read ; do
	mkdir -p %{buildroot}%{_docdir}/%{name}/${REPLY%/*}
	cp -a $REPLY %{buildroot}%{_docdir}/%{name}/$REPLY
    done
rm -r %{buildroot}%{_docdir}/%{name}/po
# COPYING README TODO are 1 byte long
rm %{buildroot}%{_docdir}/%{name}/{COPYING,README,TODO}
# NOTE: There is no real use of these locales just now:
%find_lang %{name}
%fdupes %{buildroot}%{_datadir}
%{icon_theme_cache_create_ghost Foxtrot}
%{icon_theme_cache_create_ghost Gion}
%{icon_theme_cache_create_ghost Neu}
%{icon_theme_cache_create_ghost gnome-alternative}

%post
%icon_theme_cache_post Foxtrot
%icon_theme_cache_post Gion
%icon_theme_cache_post Neu
%icon_theme_cache_post gnome-alternative

# No need for %%icon_theme_cache_postun in %postun since the themes won't exist anymore

%files -f %{name}.lang
%doc %{_docdir}/%{name}
%ghost %{_datadir}/icons/*/icon-theme.cache
%{_datadir}/icons/Foxtrot/
%{_datadir}/icons/Gion/
%{_datadir}/icons/Neu/
%{_datadir}/icons/gnome-alternative/
%{_datadir}/themes/Darklooks/
%{_datadir}/themes/Unity/

%changelog
