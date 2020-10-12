#
# spec file for package fbterm
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


Name:           fbterm
Version:        1.8
Release:        0
Summary:        A fast framebuffer-based terminal emulator
License:        GPL-2.0-or-later
Group:          System/Console
URL:            https://github.com/sfzhi/fbterm

Source:         https://github.com/sfzhi/fbterm/archive/%version.tar.gz
Patch1:         fbterm-gcc6-fixes.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gpm
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)

%description
FbTerm is a fast terminal emulator for linux with frame buffer device.
Features include:
  
  * mostly as fast as terminal of linux kernel while accelerated scrolling
    is enabled on framebuffer device
  * select font with fontconfig and draw text with freetype2, same as
    Qt/Gtk+ based GUI apps
  * dynamicly create/destroy up to 10 windows initially running default shell
  * record scrollback history for every window
  * auto-detect current locale and convert text encoding, support double
    width scripts like Chinese, Japanese etc
  * switch between configurable additional text encodings with hot keys
    on the fly
  * copy/past selected text between windows with mouse when gpm server is
    running
  * change the orientation of screen display, a.k.a. screen rotation
  * lightweight input method framework with client-server architecture

%prep
%autosetup -p1

%build
autoreconf -fi
export CFLAGS="%optflags -fno-strict-aliasing"
%configure
%make_build

%install
%make_install
# disallow setuid bit for now...
chmod 0755 %{buildroot}/%{_bindir}/fbterm

%files
%doc README AUTHORS ChangeLog COPYING
%doc %{_mandir}/man1/*
%{_bindir}/*

%changelog
