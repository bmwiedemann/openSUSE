#
# spec file for package perl-Email-MIME
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Email-MIME
Version:        1.946
Release:        0
%define cpan_name Email-MIME
Summary:        Easy Mime Message Handling
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Email-MIME/
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Email::Address::XS)
BuildRequires:  perl(Email::MIME::ContentType) >= 1.022
BuildRequires:  perl(Email::MIME::Encodings) >= 1.314
BuildRequires:  perl(Email::MessageID)
BuildRequires:  perl(Email::Simple) >= 2.212
BuildRequires:  perl(Email::Simple::Creator)
BuildRequires:  perl(Email::Simple::Header)
BuildRequires:  perl(MIME::Types) >= 1.13
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(parent)
Requires:       perl(Email::Address::XS)
Requires:       perl(Email::MIME::ContentType) >= 1.022
Requires:       perl(Email::MIME::Encodings) >= 1.314
Requires:       perl(Email::MessageID)
Requires:       perl(Email::Simple) >= 2.212
Requires:       perl(Email::Simple::Creator)
Requires:       perl(Email::Simple::Header)
Requires:       perl(MIME::Types) >= 1.13
Requires:       perl(Module::Runtime)
Requires:       perl(parent)
%{perl_requires}

%description
This is an extension of the Email::Simple module, to handle MIME encoded
messages. It takes a message as a string, splits it up into its constituent
parts, and allows you access to various parts of the message. Headers are
decoded from MIME encoding.

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
%license LICENSE

%changelog
