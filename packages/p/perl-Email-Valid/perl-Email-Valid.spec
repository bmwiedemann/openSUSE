#
# spec file for package perl-Email-Valid
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-Email-Valid
Version:        1.202
Release:        0
%define cpan_name Email-Valid
Summary:        Check validity of Internet email addresses
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Email-Valid/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE README

%changelog
