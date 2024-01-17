#
# spec file for package xmp
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


Name:           xmp
Version:        4.2.0
Release:        0
Summary:        Extended Module Player for MOD/S3M/XM/IT/etc.
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            http://xmp.sf.net/

#Git-Clone:	https://github.com/libxmp/xmp-cli
Source:         https://github.com/libxmp/xmp-cli/releases/download/xmp-%version/xmp-%version.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa) >= 1
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libxmp) >= 4.4

%description
The Extended Module Player is a command-line mod player for Unix-like
systems that plays over 90 mainstream and obscure module formats from
Amiga, Atari, Acorn, Apple IIgs, C64, and PC, including Protracker
(MOD), Scream Tracker 3 (S3M), Fast Tracker II (XM), and Impulse
Tracker (IT) files.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%dir %_sysconfdir/xmp/
%config %_sysconfdir/xmp/*.conf
%_bindir/xmp
%_mandir/man1/xmp.1*
%doc COPYING README

%changelog
