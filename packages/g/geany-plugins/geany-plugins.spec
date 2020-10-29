#
# spec file for package geany-plugins
#
# Copyright (c) 2020 SUSE LLC
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


# FIXME: Files listed inside the conditional "%%if %%{gtk3_ready}" are enabled because they do build when compiled against gtk3.
# On next update, try enabling each of the disabled libs (in the %%else section) and check if they build with gtk3 or not. When all of them compile against gtk3, remove the macro and conditional.
%define gtk3_ready 1
Name:           geany-plugins
Version:        1.37
Release:        0
# FIXME: gendoc requires ctpl (http://ctpl.tuxfamily.org/)
Summary:        A collection of different plugins for Geany
License:        GPL-2.0-or-later AND GPL-3.0-or-later
Group:          Development/Tools/IDE
URL:            https://plugins.geany.org/geany-plugins/
Source:         http://plugins.geany.org/geany-plugins/%{name}-%{version}.tar.bz2

BuildRequires:  devhelp-devel
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libgeany0 >= 1.29
BuildRequires:  libgpgme-devel
BuildRequires:  libtool
BuildRequires:  libwnck2-devel
BuildRequires:  lua51-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
# We cannot use pygtk anymore, as it is Python 2-based.
# Unless geany-plugins switches to PyGObject, we cannot have Gnome
# plugins here.
# BuildRequires:  python-gtk-devel
BuildRequires:  vala
BuildRequires:  pkgconfig(enchant) >= 1.3
BuildRequires:  pkgconfig(geany) >= 1.26
BuildRequires:  pkgconfig(glib-2.0) >= 2.16
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtkspell3-3.0)
BuildRequires:  pkgconfig(libgit2) >= 0.21
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.27
# Disable this as we do not want to use this unsupported version of webkit.
# Leaving it in place to remind us to enable for newer versions if upstream ports it.
# See https://github.com/geany/geany-plugins/issues/655
#BuildRequires:  pkgconfig(webkit-1.0) >= 1.1.18
Requires:       geany >= 1.26
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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc NEWS README
%{_libdir}/libgeanypluginutils.so
%{_libdir}/libgeanypluginutils.so.*
# Explicitly list plugins, so we don't lose any by accident
%dir %{_libdir}/geany-plugins
%dir %{_libdir}/geany-plugins/geanylua
%{_docdir}/%{name}/
%{_datadir}/geany-plugins/

%if %{gtk3_ready}
# List of gtk3 compatible plugins
%{_libdir}/geany/addons.so
%{_libdir}/geany/autoclose.so
%{_libdir}/geany/automark.so
%{_libdir}/geany/codenav.so
%{_libdir}/geany/commander.so
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

%else
# These plugins are not compatible with gtk3
%{_libdir}/geany/debugger.so
%{_libdir}/geany/devhelp.so
%{_libdir}/geany/markdown.so
%{_libdir}/geany/multiterm.so
%{_libdir}/geany/scope.so
%{_libdir}/geany/webhelper.so

%dir %{_libdir}/geany/geanypy
%dir %{_libdir}/geany/geanypy/geany
%dir %{_datadir}/geany/geanypy
%dir %{_datadir}/geany/geanypy/plugins

%{_libdir}/geany/geanypy.so
%{_libdir}/geany/geanypy/geany/__init__.py
%{_libdir}/geany/geanypy/geany/__init__.pyc
%{_libdir}/geany/geanypy/geany/console.py
%{_libdir}/geany/geanypy/geany/console.pyc
%{_libdir}/geany/geanypy/geany/loader.py
%{_libdir}/geany/geanypy/geany/loader.pyc
%{_libdir}/geany/geanypy/geany/manager.py
%{_libdir}/geany/geanypy/geany/manager.pyc
%{_libdir}/geany/geanypy/geany/plugin.py
%{_libdir}/geany/geanypy/geany/plugin.pyc
%{_libdir}/geany/geanypy/geany/signalmanager.py
%{_libdir}/geany/geanypy/geany/signalmanager.pyc
%{_datadir}/geany/geanypy/plugins/console.py
%{_datadir}/geany/geanypy/plugins/demo.py
%{_datadir}/geany/geanypy/plugins/hello.py
%endif

%files lang -f %{name}.lang

%changelog
