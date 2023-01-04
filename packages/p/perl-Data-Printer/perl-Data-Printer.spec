#
# spec file for package perl-Data-Printer
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


%define cpan_name Data-Printer
Name:           perl-Data-Printer
Version:        1.001000
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Colored & full-featured pretty print of Perl data structures and objects
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/G/GA/GARU/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(version) >= 0.77
Requires:       perl(version) >= 0.77
%{perl_requires}

%description
The ever-popular Data::Dumper is a fantastic tool, meant to stringify data
structures in a way they are suitable for being "eval"'ed back in. The
thing is, a lot of people keep using it (and similar ones, like Data::Dump)
to print data structures and objects on screen for inspection and
debugging, and while you _can_ use those modules for that, it doesn't mean
you _should_.

This is where Data::Printer comes in. It is meant to do one thing and one
thing only:

_format Perl variables and objects to be inspected by a human_

If you want to serialize/store/restore Perl data structures, this module
will NOT help you. Try Storable, Data::Dumper, JSON, or whatever. CPAN is
full of such solutions!

Whenever you type 'use Data::Printer' or 'use DDP', we export two functions
to your namespace:

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
%doc Changes CONTRIBUTING.md examples README.md

%changelog
