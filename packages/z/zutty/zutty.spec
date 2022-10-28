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
Summary:        A high-end terminal for low-end systems

License:        GPL-3.0-or-later+
Group:          System/X11/Terminals
URL:            https://github.com/tomscii/zutty/archive/refs/tags/%version.tar.gz#zutty-%version.tar.gz
Source0:        %{name}-%{version}.tar.gz
# Note: Tumbleweed contains waf, but Leap does not (yet), so we use python3 and add waf to the sources.
BuildRequires:  gcc-c++ python3 pkg-config Mesa-libEGL-devel Mesa-libGLESv3-devel libXmu-devel freetype2-devel


%description
An X terminal emulator rendering through OpenGL ES Compute Shaders. It focuses on low-latency rendering and compatibility with commonly found terminal protocols.


%prep
%setup -q

%build
CXXFLAGS="%{?optflags}" LDFLAGS="%{?build_ldflags}" ./waf configure --prefix=/usr --no-werror
./waf

%install
./waf install --destdir=%{buildroot}

%files
%{_bindir}/zutty

%license LICENSE

%changelog
