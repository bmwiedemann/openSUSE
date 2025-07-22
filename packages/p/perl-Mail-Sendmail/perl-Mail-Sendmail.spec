#
# spec file for package perl-Mail-Sendmail
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


%define cpan_name Mail-Sendmail
Name:           perl-Mail-Sendmail
Version:        0.820.0
Release:        0
# 0.82 -> normalize -> 0.820.0
%define cpan_version 0.82
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Simple platform independent mailer
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Sys::Hostname::Long)
BuildRequires:  perl(parent)
Requires:       perl(Sys::Hostname::Long)
Requires:       perl(parent)
Provides:       perl(Mail::Sendmail) = 0.800.0
%undefine       __perllib_provides
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  findutils
BuildRequires:  make
# MANUAL END

%description
Simple platform independent e-mail from your perl script. Only requires
Perl 5 and a network connection.

Mail::Sendmail takes a hash with the message to send and sends it to your
mail server. It is intended to be very easy to setup and use. See also
"FEATURES" below, and as usual, read this documentation.

There is also a FAQ (see "NOTES").

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -path "*/scripts/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
# bsc#1017667 -- Disabled tests sending email when building
# make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes README Todo
%license LICENSE

%changelog
