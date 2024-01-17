#
# spec file for package perl-Devel-StackTrace-AsHTML
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


Name:           perl-Devel-StackTrace-AsHTML
Version:        0.15
Release:        0
%define cpan_name Devel-StackTrace-AsHTML
Summary:        Displays stack trace in HTML
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Devel-StackTrace-AsHTML/
Source0:        http://www.cpan.org/authors/id/M/MI/MIYAGAWA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Devel::StackTrace)
%{perl_requires}

%description
Devel::StackTrace::AsHTML adds 'as_html' method to Devel::StackTrace which
displays the stack trace in beautiful HTML, with code snippet context and
function parameters. If you call it on an instance of
Devel::StackTrace::WithLexicals, you even get to see the lexical variables
of each stack frame.

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
