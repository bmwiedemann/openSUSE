#
# spec file for package perl-Mail-Sender
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


Name:           perl-Mail-Sender
Version:        0.903
Release:        0
%define cpan_name Mail-Sender
Summary:        (DEPRECATED) module for sending mails with attachments through an SMTP server
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Mail-Sender/
Source0:        http://www.cpan.org/authors/id/C/CA/CAPOEIRAB/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
Recommends:     perl(Authen::NTLM)
Recommends:     perl(Digest::HMAC_MD5)
Recommends:     perl(IO::Socket::SSL)
Recommends:     perl(Mozilla::CA)
Recommends:     perl(Net::SSLeay)
%{perl_requires}

%description
Mail::Sender is deprecated. Email::Sender is the go-to choice when you need
to send Email from Perl. Go there, be happy!

Mail::Sender provides an object-oriented interface to sending mails. It
directly connects to the mail server using IO::Socket.

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
