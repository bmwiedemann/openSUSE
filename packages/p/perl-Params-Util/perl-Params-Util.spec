#
# spec file for package perl-Params-Util
#
# Copyright (c) 2020 SUSE LLC
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


Name:           perl-Params-Util
Version:        1.101
Release:        0
%define cpan_name Params-Util
Summary:        Simple, compact and correct param-checking functions
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(Test::LeakTrace)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(XSLoader) >= 0.22
BuildRequires:  perl(parent)
Requires:       perl(XSLoader) >= 0.22
%{perl_requires}

%description
'Params::Util' provides a basic set of importable functions that makes
checking parameters a hell of a lot easier

While they can be (and are) used in other contexts, the main point behind
this module is that the functions *both* Do What You Mean, and Do The Right
Thing, so they are most useful when you are getting params passed into your
code from someone and/or somewhere else and you can't really trust the
quality.

Thus, 'Params::Util' is of most use at the edges of your API, where params
and data are coming in from outside your code.

The functions provided by 'Params::Util' check in the most strictly correct
manner known, are documented as thoroughly as possible so their exact
behaviour is clear, and heavily tested so make sure they are not fooled by
weird data and Really Bad Things.

To use, simply load the module providing the functions you want to use as
arguments (as shown in the SYNOPSIS).

To aid in maintainability, 'Params::Util' will *never* export by default.

You must explicitly name the functions you want to export, or use the
':ALL' param to just have it export everything (although this is not
recommended if you have any _FOO functions yourself with which future
additions to 'Params::Util' may clash)

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -path "*/t/*" ! -name "*.pl" ! -path "*/bin/*" ! -path "*/script/*" ! -name "configure" -print0 | xargs -0 chmod 644

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README.md
%license ARTISTIC-1.0 GPL-1 LICENSE

%changelog
