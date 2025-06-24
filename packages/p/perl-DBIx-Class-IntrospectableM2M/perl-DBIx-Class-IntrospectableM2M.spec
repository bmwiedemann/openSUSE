#
# spec file for package perl-DBIx-Class-IntrospectableM2M
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name DBIx-Class-IntrospectableM2M
Name:           perl-DBIx-Class-IntrospectableM2M
Version:        0.1.2
Release:        0
# 0.001002 -> normalize -> 0.1.2
%define cpan_version 0.001002
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Introspect many-to-many relationships
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IL/ILMARI/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(DBIx::Class)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
Requires:       perl(DBIx::Class)
Provides:       perl(DBIx::Class::IntrospectableM2M) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Because the many-to-many relationships are not real relationships, they can
not be introspected with DBIx::Class. Many-to-many relationships are
actually just a collection of convenience methods installed to bridge two
relationships. This DBIx::Class component can be used to store all relevant
information about these non-relationships so they can later be introspected
and examined.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install;/use lib q[.];\nuse inc::Module::Install;/' Makefile.PL
# MANUAL END

%build
PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
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
