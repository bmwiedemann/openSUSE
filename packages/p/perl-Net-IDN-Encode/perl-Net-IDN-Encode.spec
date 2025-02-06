#
# spec file for package perl-Net-IDN-Encode
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


%define cpan_name Net-IDN-Encode
Name:           perl-Net-IDN-Encode
Version:        2.500
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Internationalizing Domain Names in Applications (UTS #46)
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/C/CF/CFAERBER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
# PATCH-FIX-UPSTREAM https://rt.cpan.org/Public/Bug/Display.html?id=149108
Patch0:         use-uvchr_to_utf8_flags-instead-of-uvuni_to_utf8_fla.patch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build) >= 0.42
BuildRequires:  perl(Test::NoWarnings)
%{perl_requires}

%description
This module provides an easy-to-use interface for encoding and decoding
Internationalized Domain Names (IDNs).

IDNs use characters drawn from a large repertoire (Unicode), but IDNA
allows the non-ASCII characters to be represented using only the ASCII
characters already allowed in so-called host names today
(letter-digit-hyphen, '/[A-Z0-9-]/i').

Use this module if you just want to convert domain names (or email
addresses), using whatever IDNA standard is the best choice at the moment.

You should be familiar with Unicode support in perl, as this module expects
correctly encoded input. See perlunitut, perluniintro and perlunicode for
details.

%prep
%autosetup  -n %{cpan_name}-%{version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Build.PL --installdirs=vendor optimize="%{optflags}"
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README
%license LICENSE

%changelog
