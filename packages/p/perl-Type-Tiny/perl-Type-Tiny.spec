#
# spec file for package perl-Type-Tiny
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Type-Tiny
Version:        1.010006
Release:        0
%define cpan_name Type-Tiny
Summary:        Tiny, yet Moo(se)-compatible type constraint
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Exporter::Tiny) >= 1.000000
Requires:       perl(Exporter::Tiny) >= 1.000000
Recommends:     perl(Devel::LexAlias) >= 0.05
Recommends:     perl(Devel::StackTrace)
Recommends:     perl(Ref::Util::XS) >= 0.100
Recommends:     perl(Regexp::Util) >= 0.003
Recommends:     perl(Sub::Util)
Recommends:     perl(Type::Tie)
Recommends:     perl(Type::Tiny::XS) >= 0.016
%{perl_requires}

%description
This documents the internals of the Type::Tiny class. Type::Tiny::Manual is
a better starting place if you're new.

Type::Tiny is a small class for creating Moose-like type constraint objects
which are compatible with Moo, Moose and Mouse.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING COPYRIGHT CREDITS doap.ttl examples NEWS README
%license LICENSE

%changelog
