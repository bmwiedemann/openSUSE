#
# spec file for package qemacs
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


Name:           qemacs
Version:        0.3.3
Release:        0
Summary:        An editor similar to Emacs
License:        LGPL-2.1-or-later
Group:          Productivity/Editors/Other
URL:            https://bellard.org/qemacs/
Source0:        https://bellard.org/qemacs/qemacs-%{version}.tar.gz
Patch0:         qemacs.patch
Patch1:         qemacs-lib64.patch
Patch2:         initcall.patch
Patch3:         qemacs-libpng.patch
# PATCH-FIX-UPSTREAM pngtoico-libpng15.patch -- pgajdos@suse.com; build with libpng15; sent today to fabrice.bellard@free.fr
# build against libpng14 should not be affected, otherwise please let me know
Patch4:         qemacs-libpng15.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xv)

%description
Full screen editor with an Emacs look and feel with common Emacs features
like multi-buffer, multi-window, command mode, universal argument,
keyboard macros, config file with C like syntax, minibuffer with
completion and history. Additional features:

* UTF-8 support, including bidirectional editing respecting the
  Unicode bidi algorithm.

* WYSIWYG HTML/XML/CSS2 mode graphical editing. Supports Lynx-like
  rendering on VT100 terminals.

* A WYSIWYG DocBook mode based on XML/CSS2 renderer.

* C mode: coloring with immediate update. Emacs like auto-indent.

* Shell mode: colorized VT100 emulation so that shells work as
  expected. Compile mode with next/prev error.

* Input methods for most languages, including Chinese (input methods
  come from the Yudit editor).

* Hexadecimal editing mode with insertion and block commands. Unicode
  hexa editing of UTF-8 files also supported.

* X11 support and support for multiple proportional fonts at the same
  time (as XEmacs). X Input methods supported. Xft extension
  supported for anti aliased font display.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .lib64
%patch2
%patch3
%patch4 -p1

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
./configure \
	--prefix="%{_prefix}" \
	%{_target_platform}
make STRIP=:

%install
%make_install -e
chmod 644 %{buildroot}/%{_mandir}/man1/*

%files
%license COPYING
%doc Changelog README TODO qe-doc.html config.eg
%doc tests/
%{_bindir}/*
%{_datadir}/qe/
%{_mandir}/man1/*

%changelog
