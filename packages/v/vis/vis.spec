#
# spec file for package vis
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


Name:           vis
Version:        0.5+git.1590819266.c37f09e
Release:        0
Summary:        An editor combining the strengths of both vi(m) and sam
License:        ISC
Group:          Productivity/Text/Editors
URL:            https://github.com/martanne/vis
Source:         %{name}-%{version}.tar.xz
BuildRequires:  libtermkey-devel
BuildRequires:  lua-devel
BuildRequires:  lua-lpeg
BuildRequires:  ncurses-devel
BuildRequires:  tar
BuildRequires:  tre-devel
Requires:       lua
ExclusiveArch:  x86_64 %{ix86}

%description
Vis aims to be a modern, legacy free, simple yet efficient editor combining the strengths of both vi(m) and sam.

It extends vi's modal editing with built-in support for multiple cursors/selections and combines it with sam's structural regular expression based command language.

%prep
%autosetup

%build
# FIXME: you should use the %%configure macro
./configure --prefix="%{_prefix}"
%make_build debug

%install
%make_install

%check
# According to the debian/rules: 
# The vim tests harness is not solid, let's skip them for the moment.
# Upstream mentioned the possibility of phasing them out entirely.
make -C test/core
# No busted yet make -C test/lua
make -C test/vis

%files
%{_bindir}/vis*
%{_datadir}/vis
%{_mandir}/man1/*
%dir %{_datadir}/doc/vis
%{_datadir}/doc/vis/LICENSE
%{_datadir}/doc/vis/README.md

%changelog
