#
# spec file for package perl-HTTP-Headers-ActionPack
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


Name:           perl-HTTP-Headers-ActionPack
Version:        0.09
Release:        0
%define cpan_name HTTP-Headers-ActionPack
Summary:        HTTP Action, Adventure and Excitement
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/HTTP-Headers-ActionPack/
Source0:        http://www.cpan.org/authors/id/D/DR/DROLSKY/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTTP::Date)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(HTTP::Headers::Util)
BuildRequires:  perl(HTTP::Request)
BuildRequires:  perl(HTTP::Response)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Fatal) >= 0.0003
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(URI::Escape)
BuildRequires:  perl(parent)
Requires:       perl(HTTP::Date)
Requires:       perl(HTTP::Headers::Util)
Requires:       perl(Module::Runtime)
Requires:       perl(Sub::Exporter)
Requires:       perl(Time::Piece)
Requires:       perl(URI::Escape)
Requires:       perl(parent)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  perl(Plack)
# MANUAL END

%description
This is a module to handle the inflation and deflation of complex HTTP
header types. In many cases header values are simple strings, but in some
cases they are complex values with a lot of information encoded in them.
The goal of this module is to make the parsing and analysis of these
headers as easy as calling 'inflate' on a compatible object (see below for
a list).

This top-level class is basically a Factory for creating instances of the
other classes in this module. It contains a number of convenience methods
to help make common cases easy to write.

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
%doc Changes LICENSE README README.md

%changelog
