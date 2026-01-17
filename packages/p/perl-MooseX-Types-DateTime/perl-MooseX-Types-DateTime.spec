#
# spec file for package perl-MooseX-Types-DateTime
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


%define cpan_name MooseX-Types-DateTime
Name:           perl-MooseX-Types-DateTime
Version:        0.140.0
Release:        0
# 0.14 -> normalize -> 0.140.0
%define cpan_version 0.14
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        DateTime related constraints and coercions for Moose
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DateTime) >= 0.430.200
BuildRequires:  perl(DateTime::Duration) >= 0.430.200
BuildRequires:  perl(DateTime::Locale) >= 0.400.100
BuildRequires:  perl(DateTime::TimeZone) >= 0.950
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Build::Tiny) >= 0.34
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Moose) >= 0.410
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Types) >= 0.300
BuildRequires:  perl(MooseX::Types::Moose) >= 0.300
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(namespace::clean) >= 0.190
BuildRequires:  perl(ok)
Requires:       perl(DateTime) >= 0.430.200
Requires:       perl(DateTime::Duration) >= 0.430.200
Requires:       perl(DateTime::Locale) >= 0.400.100
Requires:       perl(DateTime::TimeZone) >= 0.950
Requires:       perl(Moose) >= 0.410
Requires:       perl(MooseX::Types) >= 0.300
Requires:       perl(MooseX::Types::Moose) >= 0.300
Requires:       perl(namespace::clean) >= 0.190
Provides:       perl(MooseX::Types::DateTime) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module packages several Moose::Util::TypeConstraints with coercions,
designed to work with the DateTime suite of objects.

Namespaced Example:

    use MooseX::Types::DateTime;

    has time_zone => (
        isa => 'DateTime::TimeZone',
        is => "rw",
        coerce => 1,
    );

    Class->new( time_zone => "Africa/Timbuktu" );

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

%build
perl Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING README
%license LICENCE

%changelog
