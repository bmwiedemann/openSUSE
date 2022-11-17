#
# spec file for package zutty
#
# Copyright (c) 2022 SUSE LLC
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


Name:           zutty
Version:        0.13
Release:        0
Summary:        Terminal program with GLES renderer and low latency
License:        GPL-3.0-or-later
Group:          System/X11/Terminals

URL:            https://tomscii.sig7.se/zutty/
#Git-Clone:     https://github.com/tomscii/zutty
#Git-Clone:     https://github.com/tomscii/zutty.wiki
Source:         https://github.com/tomscii/zutty/archive/refs/tags/%version.tar.gz#/zutty-%version.tar.gz
Source3:        FAQ.md
# Note: Tumbleweed contains waf, but Leap does not (yet), so we use python3 and add waf to the sources.
BuildRequires:  Mesa-libEGL-devel
BuildRequires:  Mesa-libGLESv3-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  libXmu-devel
BuildRequires:  pkg-config
BuildRequires:  python3

%description
An X terminal emulator rendering through OpenGL ES shaders.
It has good input latency and VTxxx emulation over most other
terminals, ranging second after xterm (as of 2022).
It uses FreeType, but does not support fontconfig, thus won't find
fonts by their usual names. (See FAQ for details.)

%prep
%autosetup
cp -a "%_sourcedir/FAQ.md" .

%build
CXXFLAGS="%{?optflags}" LDFLAGS="%{?build_ldflags}" ./waf configure --prefix="%_prefix" --no-werror
./waf

%install
./waf install --destdir=%{buildroot}

%files
%{_bindir}/zutty
%doc FAQ.md
%license LICENSE

%changelog
