#
# spec file for package perl-MooseX-Types-DateTime
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-MooseX-Types-DateTime
Version:        0.13
Release:        0
%define cpan_name MooseX-Types-DateTime
Summary:        L<DateTime> related constraints and coercions for Moose
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/MooseX-Types-DateTime/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DateTime) >= 0.4302
BuildRequires:  perl(DateTime::Duration) >= 0.4302
BuildRequires:  perl(DateTime::Locale) >= 0.400100
BuildRequires:  perl(DateTime::TimeZone) >= 0.95
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(Moose) >= 0.41
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Types) >= 0.30
BuildRequires:  perl(MooseX::Types::Moose) >= 0.30
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(namespace::clean) >= 0.19
BuildRequires:  perl(ok)
Requires:       perl(DateTime) >= 0.4302
Requires:       perl(DateTime::Duration) >= 0.4302
Requires:       perl(DateTime::Locale) >= 0.400100
Requires:       perl(DateTime::TimeZone) >= 0.95
Requires:       perl(Moose) >= 0.41
Requires:       perl(MooseX::Types) >= 0.30
Requires:       perl(MooseX::Types::Moose) >= 0.30
Requires:       perl(namespace::clean) >= 0.19
%{perl_requires}

%description
This module packages several the Moose::Util::TypeConstraints manpage with
coercions, designed to work with the the DateTime manpage suite of objects.

Namespaced Example:

    use MooseX::Types::DateTime;

    has time_zone => (
        isa => 'DateTime::TimeZone',
        is => "rw",
        coerce => 1,
    );

    Class->new( time_zone => "Africa/Timbuktu" );

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING LICENCE README

%changelog
