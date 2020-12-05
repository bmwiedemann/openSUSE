#
# spec file for package perl-User-Identity
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


Name:           perl-User-Identity
Version:        1.00
Release:        0
%define cpan_name User-Identity
Summary:        Maintain info about a physical person
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
The 'User-Identity' distribution is created to maintain a set of
informational objects which are related to one user. The 'User::Identity'
module tries to be smart providing defaults, conversions and often required
combinations.

The identities are not implementing any kind of storage, and can therefore
be created by any simple or complex Perl program. This way, it is more
flexible than an XML file to store the data. For instance, you can decide
to store the data with Data::Dumper, Storable, DBI, AddressBook or
whatever. Extension to simplify this task are still to be developed.

If you need more kinds of user information, then please contact the module
author.

Extends "DESCRIPTION" in User::Identity::Item.

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
%doc ChangeLog README README.md

%changelog
