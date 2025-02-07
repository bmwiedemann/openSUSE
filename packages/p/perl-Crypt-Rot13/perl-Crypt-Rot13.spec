#
# spec file for package perl-Crypt-Rot13
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Crypt-Rot13
Name:           perl-Crypt-Rot13
Version:        0.600.0
Release:        0
# 0.6 -> normalize -> 0.600.0
%define cpan_version 0.6
#Upstream:  This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You should have received a copy of the GNU General Public License along with this program; if not, write to the Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
License:        GPL-2.0-or-later
Summary:        Simple, reversible encryption
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        Crypt-Rot13-0.6.tar.bz2
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
rot13 is a simple encryption in which ASCII letters are rotated 13 places
(see below). This module provides an array object with methods to encrypt
its string elements by rotating ASCII letters n places down the alphabet.

Think of it this way: all of the letters of the alphabet are arranged in a
circle like the numbers of a clock. Also like a clock, you have a hand
pointing at one of the letters: a. Crypt::Rot13 turns the hand clockwise n
times through 'b', 'c', 'd', etc, and back again to 'a', 26 turns later.

Crypt::Rot13 turns this hand for every letter of every string it contains a
given number of times, the default of which is 13, or exactly half the
number of letters in the alphabet.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README rot13.perl
%license COPYING

%changelog
