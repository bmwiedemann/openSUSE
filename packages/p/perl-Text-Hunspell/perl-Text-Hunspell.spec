#
# spec file for package perl-Text-Hunspell
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Text-Hunspell
Name:           perl-Text-Hunspell
Version:        2.16
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Perl interface to the Hunspell library
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CO/COSIMO/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Alien::Hunspell) >= 0.04
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.52
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  gcc-c++
BuildRequires:  hunspell-devel
# MANUAL END

%description
This module provides a Perl interface to the *Hunspell* library. This
module is to meet the need of looking up many words, one at a time, in a
single session, such as spell-checking a document in memory.

The example code describes the interface on http://hunspell.sf.net

%prep
%autosetup  -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes examples perlobject.map README
%license LICENSE

%changelog
