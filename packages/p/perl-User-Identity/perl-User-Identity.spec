#
# spec file for package perl-User-Identity
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define cpan_name User-Identity
Name:           perl-User-Identity
Version:        4.0.0
Release:        0
# 4.00 -> normalize -> 4.0.0
%define cpan_version 4.00
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Collect information about a user
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MARKOV/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Hash::Ordered) >= 0.14
BuildRequires:  perl(Log::Report) >= 1.420
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(Test::Pod) >= 1
Requires:       perl(Hash::Ordered) >= 0.14
Requires:       perl(Log::Report) >= 1.420
Provides:       perl(Mail::Identity) = %{version}
Provides:       perl(User::Identity) = %{version}
Provides:       perl(User::Identity::Archive) = %{version}
Provides:       perl(User::Identity::Archive::Plain) = %{version}
Provides:       perl(User::Identity::Collection) = %{version}
Provides:       perl(User::Identity::Collection::Emails) = %{version}
Provides:       perl(User::Identity::Collection::Locations) = %{version}
Provides:       perl(User::Identity::Collection::Systems) = %{version}
Provides:       perl(User::Identity::Collection::Users) = %{version}
Provides:       perl(User::Identity::Item) = %{version}
Provides:       perl(User::Identity::Location) = %{version}
Provides:       perl(User::Identity::System) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
The 'User-Identity' distribution is created to maintain a set of
informational objects which are related to one user. The 'User::Identity'
module tries to be smart providing defaults, conversions and often required
combinations.

*Be aware:* This module versions 4.0 and up is not fully compatible with
older releases: mainly the exception handling has changed. When you need to
upgrade, please read at https://github.com/markov2/perl5-Mail-Box/wiki/.
*Version 3 is still maintained* and may see new releases as well.

The identities are not implementing any kind of storage, and can therefore
be created by any simple or complex Perl program. This way, it is more
flexible than an XML file to store the data. For instance, you can decide
to store the data with Data::Dumper, Storable, DBI, AddressBook or
whatever. Extension to simplify this task are still to be developed.

If you need more kinds of user information, then please contact the module
author.

Extends "DESCRIPTION" in User::Identity::Item.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
%doc ChangeLog README.md

%changelog
