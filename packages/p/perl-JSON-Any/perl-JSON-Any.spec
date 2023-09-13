#
# spec file for package perl-JSON-Any
#
# Copyright (c) 2023 SUSE LLC
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


%define cpan_name JSON-Any
Name:           perl-JSON-Any
Version:        1.400.0
Release:        0
%define cpan_version 1.40
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        (DEPRECATED) Wrapper Class for the various JSON classes
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.120620
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Warnings) >= 0.009
BuildRequires:  perl(Test::Without::Module)
Provides:       perl(JSON::Any) = 1.400.0
%define         __perllib_provides /bin/true
%{perl_requires}

%description
This module tries to provide a coherent API to bring together the various
JSON modules currently on CPAN. This module will allow you to code to any
JSON API and have it work regardless of which JSON module is actually
installed.

    use JSON::Any;

    my $j = JSON::Any->new;

    $json = $j->objToJson({foo=>'bar', baz=>'quux'});
    $obj = $j->jsonToObj($json);

or

    $json = $j->encode({foo=>'bar', baz=>'quux'});
    $obj = $j->decode($json);

or

    $json = $j->Dump({foo=>'bar', baz=>'quux'});
    $obj = $j->Load($json);

or

    $json = $j->to_json({foo=>'bar', baz=>'quux'});
    $obj = $j->from_json($json);

or without creating an object:

    $json = JSON::Any->objToJson({foo=>'bar', baz=>'quux'});
    $obj = JSON::Any->jsonToObj($json);

On load, JSON::Any will find a valid JSON module in your @INC by looking
for them in this order:

    Cpanel::JSON::XS
    JSON::XS
    JSON::PP
    JSON
    JSON::DWIW

And loading the first one it finds.

You may change the order by specifying it on the 'use JSON::Any' line:

    use JSON::Any qw(DWIW XS CPANEL JSON PP);

Specifying an order that is missing modules will prevent those module from
being used:

    use JSON::Any qw(CPANEL PP); # same as JSON::MaybeXS

This will check in that order, and will never attempt to load JSON::XS,
JSON.pm/JSON, or JSON::DWIW. This can also be set via the
'$ENV{JSON_ANY_ORDER}' environment variable.

JSON::Syck has been deprecated by its author, but in the attempt to still
stay relevant as a "Compatibility Layer" JSON::Any still supports it. This
support however has been made optional starting with JSON::Any 1.19. In
deference to a bug request starting with JSON.pm 1.20, JSON::Syck and other
deprecated modules will still be installed, but only as a last resort and
will now include a warning.

    use JSON::Any qw(Syck XS JSON);

or

    $ENV{JSON_ANY_ORDER} = 'Syck XS JSON';

At install time, JSON::Any will attempt to install JSON::PP as a reasonable
fallback if you do not appear have *any* backends installed on your system.

WARNING: If you call JSON::Any with an empty list

    use JSON::Any ();

It will skip the JSON package detection routines and will die loudly that
it couldn't find a package.

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
%doc Changes CONTRIBUTING README
%license LICENCE

%changelog
