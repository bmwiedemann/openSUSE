#
# spec file for package perl-Devel-StackTrace-AsHTML
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cpan_name Devel-StackTrace-AsHTML
Name:           perl-Devel-StackTrace-AsHTML
Version:        0.150.0
Release:        0
# 0.15 -> normalize -> 0.150.0
%define cpan_version 0.15
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Displays stack trace in HTML
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
Source100:      README.md
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::StackTrace)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Devel::StackTrace)
Provides:       perl(Devel::StackTrace::AsHTML) = %{version}
%undefine       __perllib_provides
%{perl_requires}

%description
Devel::StackTrace::AsHTML adds 'as_html' method to Devel::StackTrace which
displays the stack trace in beautiful HTML, with code snippet context and
function parameters. If you call it on an instance of
Devel::StackTrace::WithLexicals, you even get to see the lexical variables
of each stack frame.

%prep
%autosetup -n %{cpan_name}-%{cpan_version} -p1

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
