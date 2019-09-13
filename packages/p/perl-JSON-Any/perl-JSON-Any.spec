#
# spec file for package perl-JSON-Any
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


Name:           perl-JSON-Any
Version:        1.39
Release:        0
%define cpan_name JSON-Any
Summary:        (DEPRECATED) Wrapper Class for the various JSON classes
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/JSON-Any/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::Warnings) >= 0.009
BuildRequires:  perl(Test::Without::Module)
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

This will check in that order, and will never attempt to load the JSON::XS
manpage, the JSON.pm/JSON manpage, or the JSON::DWIW manpage. This can also
be set via the '$ENV{JSON_ANY_ORDER}' environment variable.

the JSON::Syck manpage has been deprecated by its author, but in the
attempt to still stay relevant as a "Compatibility Layer" JSON::Any still
supports it. This support however has been made optional starting with
JSON::Any 1.19. In deference to a bug request starting with JSON 1.20, the
JSON::Syck manpage and other deprecated modules will still be installed,
but only as a last resort and will now include a warning.

    use JSON::Any qw(Syck XS JSON);

or

    $ENV{JSON_ANY_ORDER} = 'Syck XS JSON';

At install time, JSON::Any will attempt to install the JSON::PP manpage as
a reasonable fallback if you do not appear have *any* backends installed on
your system.

WARNING: If you call JSON::Any with an empty list

    use JSON::Any ();

It will skip the JSON package detection routines and will die loudly that
it couldn't find a package.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes CONTRIBUTING LICENSE README

%changelog
