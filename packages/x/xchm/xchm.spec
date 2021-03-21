#
# spec file for package xchm
#
# Copyright (c) 2021 SUSE LLC
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


Name:           xchm
Version:        1.32
Release:        0
Summary:        A wxWidgets CHM document viewer
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://github.com/rzvncj/xCHM/
Source:         https://github.com/rzvncj/xCHM/releases/download/%version/%name-%version.tar.gz
BuildRequires:  automake
BuildRequires:  chmlib-devel
BuildRequires:  gcc-c++
BuildRequires:  wxWidgets-devel >= 3.0

%description
xCHM is a GUI frontend for CHMLIB, written with wxGTK. It is able to
display the topics tree, work with displayed pages history, print the
current page, work with bookmarks, change fonts and fast search
through all the pages of the loaded .chm document.

%lang_package

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install
%find_lang xchm

%files
%_bindir/xchm
%_datadir/applications/*
%_datadir/icons/*
%_datadir/metainfo/
%_mandir/man1/*
%license COPYING

%files lang -f xchm.lang

%changelog
