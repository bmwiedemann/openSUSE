#
# spec file for package fbterm
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           fbterm
Summary:        A fast framebuffer-based terminal emulator
License:        GPL-2.0+
Group:          System/Console
Version:        1.7
Release:        0
Url:            http://code.google.com/p/fbterm/

Source:         https://fbterm.googlecode.com/files/%name-1.7.0.tar.gz
Patch1:         fbterm-gcc6-fixes.patch
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  gpm
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
%if 0%{?suse_version} > 1210
# Fix build for openSUSE 12.2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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


Authors:
--------
   dragchan <zgchan317@gmail.com>

%prep
%setup -q
%patch1 -p1

%build
autoreconf -fi
export CFLAGS="%optflags -fno-strict-aliasing"
%configure
make %{?_smp_mflags}

%install
%make_install
# disallow setuid bit for now...
chmod 0755 $RPM_BUILD_ROOT%{_bindir}/fbterm

%files
%defattr(-, root, root)
%doc README AUTHORS ChangeLog COPYING
%doc %{_mandir}/man1/*
%{_bindir}/*

%changelog
