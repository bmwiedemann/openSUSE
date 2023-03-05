#
# spec file for package yast2-x11
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


Name:           yast2-x11
Version:        4.6.0
Release:        0
Summary:        YaST2 - X11 support
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-x11/
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  xorg-x11-libX11-devel
BuildRequires:  xorg-x11-libXmu-devel
BuildRequires:  yast2-devtools >= 3.1.10
Requires:       systemd
Requires:       yast2-theme >= 4.1.7
Supplements:    (yast2-installation and xorg-x11-server)
Obsoletes:      sax2-tools <= 8.1

%description
This package contains the programs and files for YaST2 X11 support.

%prep
%setup -q

%build
%yast_build

%install
%yast_install

%files
%license COPYING
%{yast_ybindir}/active_window
%{yast_ybindir}/testX
%{yast_ybindir}/set_videomode
%{yast_ybindir}/xftdpi
%{_sbindir}/xkbctrl
%{_sysconfdir}/icewm
%{_mandir}/man1/xkbctrl.1*

%changelog
