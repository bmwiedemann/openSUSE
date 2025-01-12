#
# spec file for package perl-Domain-PublicSuffix
#
# Copyright (c) 2024 SUSE LLC
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


%define cpan_name Domain-PublicSuffix
Name:           perl-Domain-PublicSuffix
Version:        0.210.0
Release:        0
# 0.21 -> normalize -> 0.210.0
%define cpan_version 0.21
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Parse a domain down to root
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NM/NMELNICK/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor::Fast)
BuildRequires:  perl(Net::IDN::Encode) >= 2.401
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Class::Accessor::Fast)
Requires:       perl(Net::IDN::Encode) >= 2.401
Requires:       perl(Test::More) >= 0.88
Provides:       perl(Domain::PublicSuffix) = %{version}
Provides:       perl(Domain::PublicSuffix::Default) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module utilizes the "effective_tld_names.dat" provided by Mozilla as a
way to effectively reduce a fully qualified domain name down to the
absolute root. The Mozilla PublicSuffix file is an open source, fully
documented format that shows absolute root TLDs, primarily for Mozilla's
browser products to be able to determine how far a cookie's security
boundaries go.

This module will attempt to search etc directories in
/usr/share/publicsuffix, /usr, /usr/local, and /opt/local for the
effective_tld_names.dat file. If a file is not found, a default file is
loaded from Domain::PublicSuffix::Default, which is current at the time of
the module's release. You can override the data file path by giving the
new() method a 'data_file' argument.

When creating a new PublicSuffix object, the module will load the data file
as specified, and use the internal structure to parse each domain sent to
the get_root_domain method. To re-parse the file, you must destroy and
create a new object, or execute the _parse_data_file method directly,
though that is not recommended.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version}

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes README README.md util
%license LICENSE

%changelog
