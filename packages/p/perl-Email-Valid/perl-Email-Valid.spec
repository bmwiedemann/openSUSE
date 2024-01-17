#
# spec file for package perl-Email-Valid
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


%define cpan_name Email-Valid
Name:           perl-Email-Valid
Version:        1.203
Release:        0
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Check validity of Internet email addresses
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
Patch0:         fix-test.patch
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::CaptureOutput)
BuildRequires:  perl(Mail::Address)
BuildRequires:  perl(Net::DNS)
BuildRequires:  perl(Net::Domain::TLD) >= 1.65
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(IO::CaptureOutput)
Requires:       perl(Mail::Address)
Requires:       perl(Net::DNS)
Requires:       perl(Net::Domain::TLD) >= 1.65
%{perl_requires}

%description
This module determines whether an email address is well-formed, and
optionally, whether a mail host exists for the domain.

Please note that there is no way to determine whether an address is
deliverable without attempting delivery (for details, see at
http://perldoc.perl.org/perlfaq9.html#How-do-I-check-a-valid-mail-address).

%prep
%autosetup  -n %{cpan_name}-%{version} -p1

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
%license LICENSE

%changelog
