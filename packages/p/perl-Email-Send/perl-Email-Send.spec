#
# spec file for package perl-Email-Send
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


%define cpan_name Email-Send
Name:           perl-Email-Send
Version:        2.202.0
Release:        0
# 2.202 -> normalize -> 2.202.0
%define cpan_version 2.202
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Simply Sending Email
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Email::Abstract)
BuildRequires:  perl(Email::Address) >= 1.80
BuildRequires:  perl(Email::Simple) >= 1.92
BuildRequires:  perl(MIME::Entity)
BuildRequires:  perl(Mail::Internet)
BuildRequires:  perl(Module::Pluggable) >= 2.97
BuildRequires:  perl(Return::Value)
Requires:       perl(Email::Abstract)
Requires:       perl(Email::Address) >= 1.80
Requires:       perl(Email::Simple) >= 1.92
Requires:       perl(Module::Pluggable) >= 2.97
Requires:       perl(Return::Value)
Provides:       perl(Email::Send) = %{version}
Provides:       perl(Email::Send::NNTP) = %{version}
Provides:       perl(Email::Send::Qmail) = %{version}
Provides:       perl(Email::Send::SMTP) = %{version}
Provides:       perl(Email::Send::Sendmail) = %{version}
Provides:       perl(Email::Send::Test) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
This module provides a very simple, very clean, very specific interface to
multiple Email mailers. The goal of this software is to be small and
simple, easy to use, and easy to extend.

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
%doc Changes README.md util
%license LICENSE

%changelog
