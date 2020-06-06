#
# spec file for package tilde
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


Name:           tilde
Version:        1.1.2
Release:        0
Summary:        A text editor for the terminal
License:        GPL-3.0-only
Group:          Productivity/Text/Editors
URL:            https://os.ghalkes.nl/t3/libt3widget.html

#Git-Clone:	https://github.com/gphalkes/tilde
Source:         https://os.ghalkes.nl/dist/%name-%version.tar.bz2
Source2:        https://os.ghalkes.nl/dist/%name-%version.tar.bz2.sig
Source3:        %name.keyring
BuildRequires:  c++_compiler
BuildRequires:  gettext-devel
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  libunistring-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libt3config) >= 1.0.0
BuildRequires:  pkgconfig(libt3highlight) >= 0.4.0
BuildRequires:  pkgconfig(libt3widget) >= 1.2.0
BuildRequires:  pkgconfig(libtranscript) >= 0.2.0

%description
Tilde is a text editor for the console/terminal, which provides an
interface for people accustomed to GUI environments such as
GNOME, KDE and Windows. For example, the short-cut to copy the
current selection is Control-C, and to paste the previously copied
text the short-cut Control-V can be used. As another example, the
File menu can be accessed by pressing Alt-F.

%prep
%autosetup -p1

%build
%configure CC=gcc CXX=g++ LIBTOOL=libtool --docdir="%_docdir/%name"
make %{?_smp_mflags}

%install
%make_install

%files
%_bindir/tilde
%_docdir/%name/
%_datadir/%name/
%_mandir/man1/tilde.1*
%license COPYING

%changelog
