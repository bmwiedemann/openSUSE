#
# spec file for package vis
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


%define test_version 0.5
Name:           vis
Version:        0.9
Release:        0
Summary:        An editor combining the strengths of both vi(m) and sam
License:        ISC
Group:          Productivity/Text/Editors
URL:            https://sr.ht/~martanne/vis/
Source0:        https://git.sr.ht/~martanne/vis/archive/v%{version}.tar.gz
Source1:        https://git.sr.ht/~martanne/vis-test/archive/v%{test_version}.tar.gz
# PATCH-FIX-UPSTREAM vis-test-builtin_strncpy-bounds.patch mcepl@suse.com
# patch from https://git.sr.ht/~martanne/vis-test/commit/efafa3c17826
Patch0:         vis-test-builtin_strncpy-bounds.patch
BuildRequires:  libselinux-devel
BuildRequires:  libtermkey-devel
BuildRequires:  lua-devel
BuildRequires:  lua-lpeg
BuildRequires:  ncurses-devel
BuildRequires:  tar
BuildRequires:  tre-devel
Requires:       lua
Suggests:       par_text
ExclusiveArch:  x86_64 %{ix86}
Suggests:       par_text

%description
Vis aims to be a modern, legacy free, simple yet efficient editor combining the strengths of both vi(m) and sam.

It extends vi's modal editing with built-in support for multiple cursors/selections and combines it with sam's structural regular expression based command language.

%prep
%setup -q -n %{name}-v%{version}

tar -xC test/ --strip-components 1 -f %{SOURCE1}

%patch -p1 -P 0

%build
export CFLAGS="%{optflags} -fcommon"
%configure
%make_build debug

%install
%make_install

%check
# According to the debian/rules:
# The vim tests harness is not solid, let's skip them for the moment.
# Upstream mentioned the possibility of phasing them out entirely.
%make_build -C test/core
# No busted yet make -C test/lua
%make_build -C test/vis

%files
%{_bindir}/vis*
%{_datadir}/vis
%{_mandir}/man1/*
%dir %{_datadir}/doc/vis
%{_datadir}/doc/vis/LICENSE
%{_datadir}/doc/vis/README.md

%changelog
