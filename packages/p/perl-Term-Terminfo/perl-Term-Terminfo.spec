#
# spec file for package perl-Term-Terminfo
#
# Copyright (c) 2025 SUSE LLC
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


Name:           perl-Term-Terminfo
Version:        0.09
Release:        0
%define cpan_name Term-Terminfo
Summary:        Access the terminfo database
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PEVANS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(ExtUtils::CChecker) >= 0.02
BuildRequires:  perl(Module::Build) >= 0.400400
BuildRequires:  perl(Module::Build::Using::PkgConfig)
BuildRequires:  perl(Test::More) >= 0.88
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  ncurses-devel
# MANUAL END

%description
Objects in this class provide access to _terminfo_ database entires.

This database provides information about a terminal, in three separate sets
of capabilities. Flag capabilities indicate the presence of a particular
ability, feature, or bug simply by their presence. Number capabilities give
the size, count or other numeric detail of some feature of the terminal.
String capabilities are usually control strings that the terminal will
recognise, or send.

Capabilities each have two names; a short name called the capname, and a
longer name called the varname. This class provides two sets of methods,
one that works on capnames, one that work on varnames.

This module optionally uses _unibilium_ to access the terminfo(5) database,
if it is available at compile-time. If not, it will use _<term.h>_ and
_-lcurses_. For more detail, see the SEE ALSO section below.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Build.PL installdirs=vendor optimize="%{optflags}"
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
