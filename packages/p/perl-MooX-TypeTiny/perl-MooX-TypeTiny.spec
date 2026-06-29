#
# spec file for package perl-MooX-TypeTiny
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


%define cpan_name MooX-TypeTiny
Name:           perl-MooX-TypeTiny
Version:        0.2.3
Release:        0
# 0.002003 -> normalize -> 0.2.3
%define cpan_version 0.002003
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Optimized type checks for Moo + Type::Tiny
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/%{cpan_name}-%{cpan_version}.tar.gz
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Moo) >= 2.004
BuildRequires:  perl(Test::Fatal) >= 0.003
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Type::Tiny) >= 1.008
Requires:       perl(Moo) >= 2.004
Requires:       perl(Type::Tiny) >= 1.008
Provides:       perl(MooX::TypeTiny) = %{version}
Provides:       perl(MooX::TypeTiny::Role::GenerateAccessor)
%undefine       __perllib_provides
%{perl_requires}

%description
This module optimizes Moo type checks when used with Type::Tiny to perform
better. It will automatically apply to isa checks and coercions that use
Type::Tiny. Non-Type::Tiny isa checks will work as normal.

This is done by inlining the type check in a more optimal manner that is
specific to Type::Tiny rather than the general mechanism Moo usually uses.

With this module, setters with type checks should be as fast as an
equivalent check in Moose.

It is hoped that eventually this type inlining will be done automatically,
making this module unnecessary.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

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
%doc Changes README
%license LICENSE

%changelog
