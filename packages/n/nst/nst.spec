#
# spec file for package nst
#
# Copyright (c) 2024 SUSE LLC
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


%define commit 56dd2cb

Name:           nst
Version:        1.0
Release:        0
Summary:        C++ port of suckless.org st (simple-terminal) emulator
License:        MIT
Group:          System/X11/Terminals
URL:            https://github.com/gerstner-hub/nst
Source0:        nst-1.0+git%{commit}.tar.xz
Source1:        nst_config.cxx
Source2:        nst_config.hxx
Patch0:         usr_etc_lookup.patch

BuildRequires:  asciidoc
BuildRequires:  gcc-c++
BuildRequires:  libXft-devel
BuildRequires:  libcosmos-devel
BuildRequires:  libxpp-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
BuildRequires:  scons
BuildRequires:  tclap

%description
The not (so) simple terminal emulator. It is a C++ port of st, the simple
terminal emulator for X that sucks less. Apart from a modernized code base
nst offers builtin scrollback buffer support, enhanced smart selection
features and the possibility to process the terminal buffer history in
external tools for searching.

%prep
%setup -q -n nst-1.0+git%{commit}
%autopatch -p1
# copy compile time configuration from package sources into source tree
cp %{SOURCE1} src
cp %{SOURCE2} src

%build
scons libtype=shared use-system-pkgs=1

%install
scons install instroot=%{buildroot}/usr use-system-pkgs=1

%files
%license LICENSE
%doc README.md
%{_bindir}/nst*
%{_distconfdir}/nst.conf
%{_datadir}/applications/%{name}.desktop
%{_datadir}/terminfo/n/nst*
%{_mandir}/man1/nst*
%{_mandir}/man5/nst*

%changelog
