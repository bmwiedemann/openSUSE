#
# spec file for package xmp
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


Name:           xmp
Version:        4.1.0
Release:        0
Summary:        Extended Module Player for MOD/S3M/XM/IT/etc.
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Players
Url:            http://xmp.sf.net/

#Git-Clone:	git://git.code.sf.net/p/xmp/xmp-cli
Source:         http://downloads.sf.net/xmp/%name-%version.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"

%files
%defattr(-,root,root)
%dir %_sysconfdir/xmp/
%config %_sysconfdir/xmp/*.conf
%_bindir/xmp
%_mandir/man1/xmp.1*
%doc COPYING README

%changelog
