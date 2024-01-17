#
# spec file for package perl-Exporter-Lite
#
# Copyright (c) 2022 SUSE LLC
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


%define cpan_name Exporter-Lite
Name:           perl-Exporter-Lite
Version:        0.09
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Lightweight exporting of functions and variables
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Exporter::Lite is an alternative to Exporter, intended to provide a
lightweight subset of the most commonly-used functionality. It supports
'import()', '@EXPORT' and '@EXPORT_OK' and not a whole lot else.

Exporter::Lite simply exports its import() function into your namespace.
This might be called a "mix-in" or a "role".

When 'Exporter::Lite' was written, if you wanted to use 'Exporter' you had
to write something like this:

 use Exporter;
 our @ISA = qw/ Exporter /;

'Exporter::Lite' saved you from writing that second line. But since before
2010 you've been able to write:

 use Exporter qw/ import /;

Which imports the 'import' function into your namespace from 'Exporter'. As
a result, I would recommend that you use 'Exporter' now, as it's a core
module (shipped with Perl).

To make sure you get a version of 'Exporter' that supports the above usage,
specify a minimum version when you 'use' it:

 use Exporter 5.57 qw/ import /;

%prep
%autosetup  -n %{cpan_name}-%{version}

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

%changelog
