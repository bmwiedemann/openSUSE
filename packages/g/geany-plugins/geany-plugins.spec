#
# spec file for package geany-plugins
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


Name:           geany-plugins
Version:        2.0
Release:        0
# FIXME: gendoc requires ctpl (http://ctpl.tuxfamily.org/)
Summary:        A collection of different plugins for Geany
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Development/Tools/IDE
URL:            https://plugins.geany.org/geany-plugins/
Source:         http://plugins.geany.org/geany-plugins/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM db2698cc869274aef353ba7af23d70921d944166.patch -- projectorganizer: fix invalid string comparison
Patch1:         https://github.com/geany/geany-plugins/commit/db2698cc869274aef353ba7af23d70921d944166.patch
# PATCH-FIX-UPSTREAM 644550babb52013d2625a3f8e789bbe94a335b6f.patch -- projectorganizer: Use g_pattern_spec_match_string() instead  of g_pattern_match_string()
Patch2:         https://github.com/geany/geany-plugins/commit/644550babb52013d2625a3f8e789bbe94a335b6f.patch
# PATCH-FIX-UPSTREAM geany-plugins-2.0-gcc15.patch -- Fix build with gcc 15
Patch3:         geany-plugins-2.0-gcc15.patch

BuildRequires:  devhelp-devel
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libgeany0 >= 2.0
BuildRequires:  libgpgme-devel
BuildRequires:  libtool
BuildRequires:  lua51-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  vala
BuildRequires:  pkgconfig(enchant) >= 1.3
BuildRequires:  pkgconfig(geany) >= 1.26
BuildRequires:  pkgconfig(glib-2.0) >= 2.16
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(libgit2) >= 0.21
BuildRequires:  pkgconfig(libsoup-2.4) >= 2.4.0
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.27
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       geany >= 2.0
Requires:       lua
Enhances:       geany

%description
Geany-Plugins is a collection of different plugins for Geany,
a lightweight IDE.

%lang_package

%prep
%autosetup -p1

%build
%configure \
	--docdir=%{_docdir}/%{name} \
	%{nil}
%make_build

%install
%make_install
install -d -m755 %{buildroot}%{python_sitearch}

find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -size 0 -delete
%fdupes %{buildroot}%{_docdir}/%{name}
%find_lang %{name}

%ldconfig_scriptlets

%files
%doc NEWS README
%{_libdir}/libgeanypluginutils.so
%{_libdir}/libgeanypluginutils.so.*
# Explicitly list plugins, so we don't lose any by accident
%dir %{_libdir}/geany-plugins
%dir %{_libdir}/geany-plugins/geanylua
%{_docdir}/%{name}/
%{_datadir}/geany-plugins/
%{_libdir}/geany/addons.so
%{_libdir}/geany/autoclose.so
%{_libdir}/geany/automark.so
%{_libdir}/geany/codenav.so
%{_libdir}/geany/commander.so
%{_libdir}/geany/debugger.so
%{_libdir}/geany/defineformat.so
%{_libdir}/geany/geanyctags.so
%{_libdir}/geany/geanyextrasel.so
%{_libdir}/geany/geanyinsertnum.so
%{_libdir}/geany/lipsum.so
%{_libdir}/geany/geanylua.so
%{_libdir}/geany-plugins/geanylua/libgeanylua.so
%{_libdir}/geany/geanyminiscript.so
%{_libdir}/geany/geanypg.so
%{_libdir}/geany/sendmail.so
%{_libdir}/geany/geanyvc.so
%{_libdir}/geany/geniuspaste.so
%{_libdir}/geany/git-changebar.so
%{_libdir}/geany/lineoperations.so
%{_libdir}/geany/markdown.so
%{_libdir}/geany/overview.so
%{_libdir}/geany/pairtaghighlighter.so
%{_libdir}/geany/pohelper.so
%{_libdir}/geany/pretty-printer.so
%{_libdir}/geany/projectorganizer.so
%{_libdir}/geany/scope.so
%{_libdir}/geany/shiftcolumn.so
%{_libdir}/geany/spellcheck.so
%{_libdir}/geany/tableconvert.so
%{_libdir}/geany/treebrowser.so
%{_libdir}/geany/updatechecker.so
%{_libdir}/geany/xmlsnippets.so
%{_libdir}/geany/latex.so
%{_libdir}/geany/geanymacro.so
%{_libdir}/geany/geanynumberedbookmarks.so
%{_libdir}/geany/geanyprj.so
%{_libdir}/geany/geanydoc.so
%{_libdir}/geany/keyrecord.so
%{_libdir}/geany/vimode.so
%{_libdir}/geany/workbench.so
%{_libdir}/geany/webhelper.so

%files lang -f %{name}.lang

%changelog
