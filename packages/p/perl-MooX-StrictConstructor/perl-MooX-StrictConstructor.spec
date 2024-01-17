#
# spec file for package perl-MooX-StrictConstructor
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-MooX-StrictConstructor
Version:        0.011
Release:        0
%define cpan_name MooX-StrictConstructor
Summary:        Make your Moo-based object constructors blow up on unknown attributes
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HARTZELL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(Moo) >= 1.001000
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(strictures) >= 1
Requires:       perl(Class::Method::Modifiers)
Requires:       perl(Moo) >= 1.001000
Requires:       perl(Moo::Role)
Requires:       perl(strictures) >= 1
%{perl_requires}

%description
Simply loading this module makes your constructors "strict". If your
constructor is called with an attribute init argument that your class does
not declare, then it dies. This is a great way to catch small typos.

Your application can use Carp::Always to generate stack traces on 'die'.
Previously all exceptions contained traces, but this could potentially leak
sensitive information, e.g.

    My::Sensitive::Class->new( password => $sensitive, extra_value => 'foo' );

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
%doc Changes
%license LICENSE

%changelog
