#
# spec file for package gnuchess
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


Name:           gnuchess
Version:        6.2.8
Release:        0
Summary:        GNU Chess Program
License:        GPL-3.0-or-later
Group:          Amusements/Games/Board/Chess
URL:            https://www.gnu.org/software/chess/
Source0:        https://ftp.gnu.org/gnu/chess/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/chess/%{name}-%{version}.tar.gz.sig
# WARNING: Don't forget to re-generate book.dat manually before submit!
# Simply remove the source and build, updated book will be generated.
Source2:        book_1.02.pgn.bz2
Source3:        genbook.sh
Source4:        xgnuchess
Source5:        http://savannah.gnu.org/project/memberlist-gpgkeys.php?group=chess&download=1#/gnuchess.keyring
# PATCH-FIX-UPSTREAM txtJ07eHdR0m6.patch CVE-2021-30184 mcepl@suse.com
# https://lists.gnu.org/archive/html/bug-gnu-chess/2021-04/msg00000.html
# Patch from https://src.fedoraproject.org/rpms/gnuchess/c/bb2dd55d0daf.patch
Patch0:         txtJ07eHdR0m6.patch
BuildRequires:  expect
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  help2man
BuildRequires:  readline-devel
Requires(post): info
Requires(preun):info
Suggests:       xboard
Provides:       chess_backend
Provides:       gchess

%description
A worthy chess opponent that runs in text mode. Find an X11 interface
in the xboard package.

%prep
%autosetup -p1

%build
%configure
%make_build
sed -i 's/^Book[[:space:]]*=[[:space:]]*false/Book = true/;s/^OwnBook[[:space:]]=[[:space:]]*false/OwnBook = true/' src/gnuchess.ini
sh %{SOURCE3} %{SOURCE2}

%install
%make_install
# install xgnuchess
install -m 755 %{SOURCE4} %{buildroot}/%{_bindir}
%find_lang %{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%license COPYING
%{_bindir}/*
%{_mandir}/man*/*
%{_infodir}/gnuchess.info%{?ext_info}
%{_datadir}/gnuchess
%dir %{_datadir}/games/plugins
%dir %{_datadir}/games/plugins/logos
%{_datadir}/games/plugins/logos/%{name}.png
%dir %{_datadir}/games/plugins/xboard
%{_datadir}/games/plugins/xboard/%{name}.eng

%changelog
