#
# spec file for package perl-Net-SMTP-SSL
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


Name:           perl-Net-SMTP-SSL
Version:        1.04
Release:        0
%define cpan_name Net-SMTP-SSL
Summary:        SSL support for Net::SMTP
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Net-SMTP-SSL/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IO::Socket::SSL)
Requires:       perl(IO::Socket::SSL)
%{perl_requires}

%description
Implements the same API as Net::SMTP, but uses IO::Socket::SSL for its
network operations. Due to the nature of 'Net::SMTP''s 'new' method, it is
not overridden to make use of a default port for the SMTPS service. Perhaps
future versions will be smart like that. Port '465' is usually what you
want, and it's not a pain to specify that.

For interface documentation, please see Net::SMTP.

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
%doc Changes README

%changelog
