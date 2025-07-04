#
# spec file for package gramps
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2010 Dominique Leuenberger, Amsterdam, Netherlands.
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


%global __requires_exclude typelib\\(GtkosxApplication\\)|typelib\\(Gtkspell\\)|typelib\\(GConf\\)
%define pythons python3
Name:           gramps
Version:        6.0.1
Release:        0
Summary:        Genealogical Research Software
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            http://www.gramps-project.org/
Source:         https://github.com/gramps-project/gramps/archive/v%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE gramps-no-translations-check.patch boo#941490 dimstar@opensuse.org -- Do not warn on missing translations
Patch0:         gramps-no-translations-check.patch
BuildRequires:  fdupes
# Needed for typelib() - Requires.
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  python-rpm-macros
BuildRequires:  python3
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
# We need the %%mime_database_* macros
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
Requires:       python3-bsddb3
Requires:       python3-cairo
Requires:       python3-gobject >= 3.12.0
Requires:       python3-gobject-Gdk
Requires:       python3-orjson
Requires:       xdg-utils
Recommends:     ghostscript
Recommends:     graphviz
Recommends:     python3-Pillow
Recommends:     python3-PyICU
# python3-fontconfig is required for the Genealogical Symbols option; currently no package available
#Recommends:     python3-fontconfig
Suggests:       python3-networkx
Suggests:       python3-pygraphviz
Suggests:       python3-numpy
Suggests:       typelib-1_0-GooCanvas-2_0
BuildArch:      noarch

%description
Gramps gives you the ability to record the many details of an
individual's life as well as the complex relationships between
various people, places and events. All of your research is kept
organized, searchable and as precise as you need it to be.

%lang_package

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
# fix resource-path containing buildroot information
echo -n %{_datadir} > %{buildroot}%{python3_sitelib}/gramps/gen/utils/resource-path
# We package those files as package docs...
rm -r %{buildroot}%{_datadir}/doc/%{name}/
%suse_update_desktop_file -r %{buildroot}%{_datadir}/applications/org.gramps_project.Gramps.desktop Office Database
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}
%fdupes %{buildroot}%{python3_sitelib}/%{name}/

%post
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun

%files
%license COPYING
%doc AUTHORS FAQ NEWS README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%dir %{_datadir}/metainfo
%{_datadir}/applications/org.gramps_project.Gramps.desktop
%{_datadir}/icons/hicolor/*/*/
%{_datadir}/metainfo/org.gramps_project.Gramps.metainfo.xml
%{_datadir}/mime/packages/org.gramps_project.Gramps.xml
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}.dist-info
%{_mandir}/man1/%{name}.1%{?ext_man}
# We can't really move the localized manpages to the lang package, since they'd
# create a conflict between the lang subpackage and bundles
%lang(cs) %{_mandir}/cs/man1/%{name}.*
%lang(fr) %{_mandir}/fr/man1/%{name}.*
%lang(nl) %{_mandir}/nl/man1/%{name}.*
%lang(pl) %{_mandir}/pl/man1/%{name}.*
%lang(sv) %{_mandir}/sv/man1/%{name}.*
%lang(pt_BR) %{_mandir}/pt_BR/man1/%{name}.*
# man doesn't provide those directories, so we have to own them
%lang(cs) %dir %{_mandir}/cs
%lang(cs) %dir %{_mandir}/cs/man1
%lang(nl) %dir %{_mandir}/nl
%lang(nl) %dir %{_mandir}/nl/man1
%lang(pl) %dir %{_mandir}/pl
%lang(pl) %dir %{_mandir}/pl/man1
%lang(sv) %dir %{_mandir}/sv
%lang(sv) %dir %{_mandir}/sv/man1
%lang(pt_BR) %dir %{_mandir}/pt_BR
%lang(pt_BR) %dir %{_mandir}/pt_BR/man1

%files lang -f %{name}.lang

%changelog
