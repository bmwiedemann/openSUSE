#
# spec file for package wdiff
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2026 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           wdiff
Version:        1.2.3
Release:        0
Summary:        Display Word Differences Between Text Files
License:        GPL-3.0-or-later
Group:          Productivity/Text/Utilities
URL:            https://www.gnu.org/software/wdiff/
Source0:        https://ftp.gnu.org/gnu/wdiff/wdiff-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/wdiff/wdiff-%{version}.tar.gz.sig
# https://blog.josefsson.org/about/
# ed25519 2019-03-20 [SC] Simon Josefsson <simon@josefsson.org>
# B1D2 BD13 75BE CB78 4CF4  F8C4 D73C F638 C53C 06BE
# https://josefsson.org/key-20190320.txt
Source2:        %{name}.keyring
BuildRequires:  help2man
BuildRequires:  makeinfo
BuildRequires:  pkgconfig(tinfo)

%description
wdiff compares two files and finds which words have been deleted or
added to old_file to get new_file. A word is considered to be anything
between whitespace.

%lang_package

%prep
%autosetup -p1

%build
%configure \
  --enable-experimental="mdiff wdiff2 unify"
%make_build

%install
%make_install
%find_lang %{name}

%check
%make_build check

%files
%license COPYING
%doc BACKLOG ChangeLog NEWS README* THANKS TODO ABOUT-NLS AUTHORS
%{_bindir}/mdiff
%{_bindir}/unify
%{_bindir}/wdiff
%{_bindir}/wdiff2
%{_infodir}/wdiff.info%{?ext_info}
%{_mandir}/man1/mdiff.1%{?ext_man}
%{_mandir}/man1/unify.1%{?ext_man}
%{_mandir}/man1/wdiff.1%{?ext_man}
%{_mandir}/man1/wdiff2.1%{?ext_man}

%files lang -f %{name}.lang
%license COPYING

%changelog
