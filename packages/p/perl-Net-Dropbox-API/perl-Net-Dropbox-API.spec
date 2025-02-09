#
# spec file for package perl-Net-Dropbox-API
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


%define cpan_name Net-Dropbox-API
Name:           perl-Net-Dropbox-API
Version:        1.900.0
Release:        0
# 1.9 -> normalize -> 1.900.0
%define cpan_version 1.9
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Dropbox API interface
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NO/NORBU/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::Random)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.36
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(JSON)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Net::OAuth)
BuildRequires:  perl(URI)
BuildRequires:  perl(common::sense)
Requires:       perl(Data::Random)
Requires:       perl(HTTP::Request::Common)
Requires:       perl(JSON)
Requires:       perl(LWP::UserAgent)
Requires:       perl(Mouse)
Requires:       perl(Net::OAuth)
Requires:       perl(URI)
Requires:       perl(common::sense)
Provides:       perl(Net::Dropbox::API) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
A dropbox API interface

%prep
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

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
%doc Changes examples ignore.txt README

%changelog
