#
# spec file for package perl-Text-Kakasi
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


%define cpan_name Text-Kakasi
Name:           perl-Text-Kakasi
Version:        2.04
Release:        0
#Upstream:  (C) 1998, 1999, 2000 NOKUBI Takatsugu <knok@daionet.gr.jp> (C) 2003 Dan Kogai <dankogai@dan.co.jp> There is no warranty for this free software. Anyone can modify and/or redistribute this module under GNU GENERAL PUBLIC LICENSE. See COPYING file that is included in the archive for more details.
License:        GPL-2.0-or-later
Summary:        Perl frontend to kakasi
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  glibc-devel
BuildRequires:  kakasi-devel
BuildRequires:  kakasi-dict
Requires:       kakasi >= 2.3.4
# MANUAL END

%description
This module provides interface to kakasi (kanji kana simple inverter).
kakasi is a set of programs and libraries which does what Japanese input
methods do in reverse order. You feed Japanese and kakasi converts it to
phonetic representation thereof. kakasi can also be used to tokenizing
Japanese text. To find more about kakasi, see http://kakasi.namazu.org/ .

Text::Kakasi now features both functional and object-oriented APIs.
functional APIs are 100% compatible with ver. 1.05. But to take advantage
of "Perl 5.8 Features", you should use OOP APIs instead.

See Text::Kakasi::JP for the Japanese version of this document.

%prep
%autosetup -n %{cpan_name}-%{version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc ChangeLog.1 Changes README README.jp
%license COPYING

%changelog
