#
# spec file for package pgn-extract
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2010 Packman Team <packman@links2linux.de>
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


Name:           pgn-extract
Version:        24.09
%define mver    24-09
Release:        0
Summary:        A CLI program for manipulating PGN files
License:        GPL-3.0-or-later
Group:          Amusements/Games/Board/Chess
URL:            https://www.cs.kent.ac.uk/people/staff/djb/pgn-extract/
Source0:        https://www.cs.kent.ac.uk/~djb/pgn-extract/pgn-extract-%{mver}.tgz
Source100:      %{name}.changes
# PATCH-FIX-OPENSUSE pgn-extract-set_eco.pgn_path.patch
Patch0:         pgn-extract-set_eco.pgn_path.patch
# PATCH-FIX-OPENSUSE pgn-extract-no-buildtime.patch
Patch1:         pgn-extract-no-buildtime.patch

%description
This is a command-line program for manipulating chess games recorded
in the Portable Game Notation (PGN).
Extracted games may be written out either including or excluding
comments, NAGs, variations, move numbers, tags and/or results.
Games may be given ECO classifications derived from the accompanying
file %{_datadir}/%{name}/eco.pgn, or a customised version provided
by the user.

For a full description of pgn-extract's functionality see
%{_docdir}/%{name}/help.html.

%prep
%autosetup -p1 -n %{name}

%build
CFLAGS="%{optflags}" make

%install
# install the binary
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
# install the default eco.pgn file
install -D -m 0644 eco.pgn %{buildroot}%{_datadir}/%{name}/eco.pgn

%files
%license COPYING
%doc help.html
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
