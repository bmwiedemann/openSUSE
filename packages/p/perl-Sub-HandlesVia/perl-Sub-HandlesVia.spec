#
# spec file for package perl-Sub-HandlesVia
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


Name:           perl-Sub-HandlesVia
Version:        0.016
Release:        0
%define cpan_name Sub-HandlesVia
Summary:        Alternative handles_via implementation
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(Eval::TypeTiny)
BuildRequires:  perl(Exporter::Shiny)
BuildRequires:  perl(List::Util) >= 1.54
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Type::Params) >= 1.004000
BuildRequires:  perl(Types::Standard)
Requires:       perl(Class::Method::Modifiers)
Requires:       perl(Class::Tiny)
Requires:       perl(Eval::TypeTiny)
Requires:       perl(Exporter::Shiny)
Requires:       perl(List::Util) >= 1.54
Requires:       perl(Role::Tiny)
Requires:       perl(Type::Params) >= 1.004000
Requires:       perl(Types::Standard)
Recommends:     perl(Sub::Util)
%{perl_requires}

%description
If you've used Moose's native attribute traits, or MooX::HandlesVia before,
you should have a fairly good idea what this does.

Why re-invent the wheel? Well, this is an implementation that should work
okay with Moo, Moose, Mouse, and any other OO toolkit you throw at it. One
ring to rule them all, so to speak.

Also, unlike MooX::HandlesVia, it honours type constraints, plus it doesn't
have the limitation that it can't mutate non-reference values.

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
%doc Changes COPYRIGHT CREDITS doap.ttl README
%license LICENSE

%changelog
