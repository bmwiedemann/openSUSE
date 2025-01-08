#
# spec file for package perl-IRI
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name IRI
Name:           perl-IRI
Version:        0.13.0
Release:        0
# 0.013 -> normalize -> 0.13.0
%define cpan_version 0.013
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Internationalized Resource Identifiers
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GW/GWILLIAMS/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:  perl(Moo)
BuildRequires:  perl(MooX::HandlesVia)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(Type::Tiny) >= 0.008
BuildRequires:  perl(URI)
Requires:       perl(Moo)
Requires:       perl(MooX::HandlesVia)
Requires:       perl(Type::Tiny) >= 0.008
Provides:       perl(IRI) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The IRI module provides an object representation for Internationalized
Resource Identifiers (IRIs) as defined by at
http://www.ietf.org/rfc/rfc3987.txt and supports their parsing,
serializing, and base resolution.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README

%changelog
