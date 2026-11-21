#
# spec file for package bluerig
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:            bluerig
Version:         1.0.2
Release:         0
Summary:         Terminal IDE, a continuation of cooledit
License:         GPL-3.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-or-later AND BSD-3-Clause AND MIT
URL:             https://github.com/blue-panels/bluerig
Source0:         %{url}/releases/download/bluerig-%{version}/bluerig-%{version}.tar.gz

BuildRequires:   check-devel
BuildRequires:   gcc
BuildRequires:   gettext
BuildRequires:   glib2-devel
BuildRequires:   json-glib-devel
BuildRequires:   gpm-devel
BuildRequires:   meson >= 0.61
BuildRequires:   pkgconfig
BuildRequires:   slang-devel
BuildRequires:   lua54-devel
BuildRequires:   libX11-devel

Recommends:      %{name}-lua%{?_isa} = %{version}-%{release}
Suggests:        libX11
Suggests:        aspell
Suggests:        hunspell
Suggests:        ctags

%description
bluerig is a terminal IDE that continues cooledit by Paul Sheer.  Its editor
has syntax highlighting, code folding, an undo history browser, keyboard
macros, a user menu, multiple windows, skins and editable key bindings, and
works with language servers for completion, documentation and diagnostics.

bluerig -D opens the project of a directory: its tree, its build with meson,
cmake or make, and its debugger, gdb or a debug adapter.  bluerig -G opens a
Git window on a work tree, and bluerig -Q runs the queries of a file in
PostgreSQL, by libpq, or in MongoDB, by mongosh.

Spell checking uses aspell or hunspell, whichever is installed; libpq and the
spell checker are loaded at run time.

%package lua
Summary:         Lua runtime and scripts for bluerig
Requires:        %{name}%{?_isa} = %{version}-%{release}

%description lua
The Lua runtime plugin that bluerig loads at run time, and the editor scripts
that come with it, such as inserting the date and time, sorting the
selection, formatting a paragraph, drawing a table or inserting the output of
a command.  Without this package bluerig runs, and the features written in Lua
are absent.

%prep
%autosetup -n %{name}-%{version}

%build
# The archive carries its version in .tarball-version.
%meson \
    -Dscreen=slang \
    -Db_pie=true \
    -Dplugins_dir=%{_libdir}/bluerig/plugins \
    -Druntime_plugins_dir=%{_libdir}/bluerig/runtime-plugins \
    -Dlua=enabled
%meson_build

%install
%meson_install
%find_lang %{name}
# The Lua documentation is listed as %%doc below, which puts it in place
# itself; what the install left behind would be packaged twice.
rm -rf %{buildroot}%{_datadir}/doc/%{name}

%check
%meson_test

%files -f %{name}.lang
%license COPYING
%doc README.md CHANGELOG.md
%doc doc/LUA_API_REFERENCE.md doc/LUA_PLUGINS.md doc/lua-api.json
%{_bindir}/bluerig
%{_bindir}/brg
# Owned here so that the directory does not depend on the lua subpackage.
%dir %{_datadir}/bluerig/
%{_datadir}/bluerig/charsets
%{_datadir}/bluerig/defaults.ini
%{_datadir}/bluerig/examples/
%{_datadir}/bluerig/help/
%{_datadir}/bluerig/query/
%{_datadir}/bluerig/skins/
%{_datadir}/bluerig/syntax/
%dir %{_sysconfdir}/bluerig/
%config(noreplace) %{_sysconfdir}/bluerig/*
%{_mandir}/man1/bluerig.1*
# The translated manuals.
%{_mandir}/*/man1/bluerig.1*
# Owned here so that the directory does not depend on the lua subpackage.
%dir %{_libdir}/bluerig/
# The editor plugins that are modules: the terminal, the viewer, the debugger.
%{_libdir}/bluerig/plugins/

%files lua
%{_libdir}/bluerig/runtime-plugins/
%{_datadir}/bluerig/lua/

%changelog
