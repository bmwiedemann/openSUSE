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
Version:        0.8
Release:        0
Summary:        An editor combining the strengths of both vi(m) and sam
License:        ISC
Group:          Productivity/Text/Editors
URL:            https://github.com/martanne/vis
Source0:        https://github.com/martanne/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/martanne/vis-test/releases/download/v%{test_version}/vis-test-%{test_version}.tar.gz
# PATCH-FEATURE-UPSTREAM 675-nb-subproc-runner.patch gh#martanne/vis!675 mcepl@suse.com
# adds support for the non-blocking subprocess runner
Patch0:         675-nb-subproc-runner.patch
BuildRequires:  libselinux-devel
BuildRequires:  libtermkey-devel
BuildRequires:  lua-devel
BuildRequires:  lua-lpeg
BuildRequires:  ncurses-devel
BuildRequires:  tar
BuildRequires:  tre-devel
Requires:       lua
ExclusiveArch:  x86_64 %{ix86}
Suggests:       par_text

%description
Vis aims to be a modern, legacy free, simple yet efficient editor combining the strengths of both vi(m) and sam.

It extends vi's modal editing with built-in support for multiple cursors/selections and combines it with sam's structural regular expression based command language.

%prep
%autosetup -p1

tar -xC test/ --strip-components 1 -f %{SOURCE1}

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
