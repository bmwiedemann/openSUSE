#
# spec file for package perl-Term-Size-Any
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Term-Size-Any
Version:        0.002
Release:        0
%define cpan_name Term-Size-Any
Summary:        Retrieve terminal size
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Term-Size-Any/
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::Hide)
BuildRequires:  perl(Module::Load::Conditional)
BuildRequires:  perl(Term::Size::Perl)
Requires:       perl(Devel::Hide)
Requires:       perl(Module::Load::Conditional)
Requires:       perl(Term::Size::Perl)
%{perl_requires}

%description
This is a unified interface to retrieve terminal size. It loads one module
of a list of known alternatives, each implementing some way to get the
desired terminal information. This loaded module will actually do the job
on behalf of 'Term::Size::Any'.

Thus, 'Term::Size::Any' depends on the availability of one of these
modules:

    Term::Size           (soon to be supported)
    Term::Size::Perl
    Term::Size::ReadKey  (soon to be supported)
    Term::Size::Win32

This release fallbacks to Term::Size::Win32 if running in Windows 32
systems. For other platforms, it uses the first of Term::Size::Perl,
Term::Size or Term::Size::ReadKey which loads successfully. (To be honest,
I disabled the fallback to Term::Size and Term::Size::ReadKey which are
buggy by now.)

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
