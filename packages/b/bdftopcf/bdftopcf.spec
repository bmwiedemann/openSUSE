#
# spec file for package bdftopcf
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           bdftopcf
Version:        1.1
Release:        0
Summary:        Font compiler for the X server and font server
License:        MIT
Group:          System/X11/Utilities
Url:            http://xorg.freedesktop.org/
Source0:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
Source1:        http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2.sig
Source2:        %{name}.keyring
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xfont)
BuildRequires:  pkgconfig(xorg-macros) >= 1.8

%description
bdftopcf is a font compiler for the X server and font server. Fonts
in Portable Compiled Format can be read by any architecture, although
the file is structured to allow one particular architecture to read
them directly without reformatting. This allows fast reading on the
appropriate machine, but the files are still portable (but read more
slowly) on other machines.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} V=1

%install
%make_install

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%{_bindir}/bdftopcf
%{_mandir}/man1/bdftopcf.1%{?ext_man}

%changelog
