#
# spec file for package perl-Email-Abstract
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Email-Abstract
Version:        3.008
Release:        0
%define cpan_name Email-Abstract
Summary:        unified interface to mail representations
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Email-Abstract/
Source:         http://www.cpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Email::Simple) >= 1.998
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
