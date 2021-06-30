#
# spec file for package perl-Email-Abstract
#
# Copyright (c) 2021 SUSE LLC
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


%define cpan_name Email-Abstract
Name:           perl-Email-Abstract
Version:        3.009
Release:        0
Summary:        Unified interface to mail representations
License:        Artistic-1.0 OR GPL-1.0-or-later
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Email::Simple) >= 1.998
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.78
BuildRequires:  perl(MRO::Compat)
BuildRequires:  perl(Module::Pluggable) >= 1.5
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Email::Simple) >= 1.998
Requires:       perl(MRO::Compat)
Requires:       perl(Module::Pluggable) >= 1.5
%{perl_requires}

%description
'Email::Abstract' provides module writers with the ability to write simple,
representation-independent mail handling code. For instance, in the cases
of 'Mail::Thread' or 'Mail::ListDetector', a key part of the code involves
reading the headers from a mail object. Where previously one would either
have to specify the mail class required, or to build a new object from
scratch, 'Email::Abstract' can be used to perform certain simple operations
on an object regardless of its underlying representation.

'Email::Abstract' currently supports 'Mail::Internet', 'MIME::Entity',
'Mail::Message', 'Email::Simple', 'Email::MIME', and 'Courriel'. Other
representations are encouraged to create their own 'Email::Abstract::*'
class by copying 'Email::Abstract::EmailSimple'. All modules installed
under the 'Email::Abstract' hierarchy will be automatically picked up and
used.

%prep
%autosetup  -n %{cpan_name}-%{version}

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
