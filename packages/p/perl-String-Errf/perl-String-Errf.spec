#
# spec file for package perl-String-Errf
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


Name:           perl-String-Errf
Version:        0.008
Release:        0
%define cpan_name String-Errf
Summary:        Simple Sprintf-Like Dialect
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/String-Errf/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Date::Format)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(String::Formatter) >= 0.102081
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Time::Piece)
BuildRequires:  perl(autodie)
BuildRequires:  perl(parent)
Requires:       perl(Params::Util)
Requires:       perl(String::Formatter) >= 0.102081
Requires:       perl(Sub::Exporter)
Requires:       perl(Time::Piece)
Requires:       perl(parent)
%{perl_requires}

%description
String::Errf provides 'errf', a simple string formatter that works
something like 'sprintf'. It is implemented using String::Formatter and
Sub::Exporter. Their documentation may be useful in understanding or
extending String::Errf. The 'errf' subroutine is only available when
imported. Calling String::Errf::errf will not do what you want.

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
