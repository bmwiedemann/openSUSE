#
# spec file for package perl-Cavil-Matcher
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Cavil-Matcher
Name:           perl-Cavil-Matcher
Version:        1.0.0
Release:        0
# 1.00 -> normalize -> 1.0.0
%define cpan_version 1.00
License:        GPL-1.0-or-later
Summary:        Next-generation license pattern matcher for Cavil
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        Cavil-Matcher-1.00.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Cpanel::JSON::XS) >= 4.90
BuildRequires:  perl(ExtUtils::MakeMaker) >= 7.12
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More) >= 0.98
Requires:       perl(Cpanel::JSON::XS) >= 4.90
Provides:       perl(Cavil::Matcher) = %{version}
Provides:       perl(Cavil::Matcher::Hash)
Provides:       perl(Cavil::Matcher::Index)
Provides:       perl(Cavil::Matcher::Manifest)
%undefine       __perllib_provides
Recommends:     perl(Spooky::Patterns::XS)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  gcc-c++
# MANUAL END

%description
'Cavil::Matcher' turns source files into license and keyword matches for at
https://github.com/openSUSE/cavil. It keeps the proven token-hash
prefix-tree algorithm of its predecessor, Spooky::Patterns::XS, but stores
the compiled patterns as immutable, memory-mapped *segments* described by a
small *manifest*, so that adding or removing a pattern never rebuilds the
whole cache and index workers share one physical copy of the data per host.

The tokenizer and hashing are a frozen C++ core, bit-for-bit compatible
with the previous engine; the segment lifecycle is pure Perl (see
Cavil::Matcher::Index and Cavil::Matcher::Manifest). For the design and
rationale see _docs/Architecture.md_.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc Changes docs README.md
%license COPYING

%changelog
