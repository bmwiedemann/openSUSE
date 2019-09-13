#
# spec file for package perl-Term-UI
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


Name:           perl-Term-UI
Version:        0.46
Release:        0
%define cpan_name Term-UI
Summary:        Term::ReadLine UI made easy
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Term-UI/
Source0:        http://www.cpan.org/authors/id/B/BI/BINGOS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Locale::Maketext::Simple)
BuildRequires:  perl(Log::Message::Simple)
BuildRequires:  perl(Params::Check)
Requires:       perl(Locale::Maketext::Simple)
Requires:       perl(Log::Message::Simple)
Requires:       perl(Params::Check)
%{perl_requires}

%description
'Term::UI' is a transparent way of eliminating the overhead of having to
format a question and then validate the reply, informing the user if the
answer was not proper and re-issuing the question.

Simply give it the question you want to ask, optionally with choices the
user can pick from and a default and 'Term::UI' will DWYM.

For asking a yes or no question, there's even a shortcut.

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
%doc CHANGES README

%changelog
