#
# spec file for package perl-Any-URI-Escape
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


%define cpan_name Any-URI-Escape
Name:           perl-Any-URI-Escape
Version:        0.10.0
Release:        0
# 0.01 -> normalize -> 0.10.0
%define cpan_version 0.01
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Load URI::Escape::XS preferentially over URI::Escape
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PH/PHRED/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(URI::Escape)
Requires:       perl(URI::Escape)
Provides:       perl(Any::URI::Escape) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
URI::Escape is great, but URI::Escape::XS is faster. This module loads
URI::Escape::XS and imports the two most common methods if XS is installed.

The insides of this module aren't completely shaken out yet, so patches
welcome.

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

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
