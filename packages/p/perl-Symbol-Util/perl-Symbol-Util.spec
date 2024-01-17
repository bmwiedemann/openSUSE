#
# spec file for package perl-Symbol-Util
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Symbol-Util
Version:        0.0203
Release:        0
%define cpan_name Symbol-Util
Summary:        Additional utils for Perl symbols manipulation
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Symbol-Util/
Source:         http://www.cpan.org/authors/id/D/DE/DEXTER/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
#BuildRequires: perl(File::Slurp)
#BuildRequires: perl(Readonly)
#BuildRequires: perl(Symbol::Util)
#BuildRequires: perl(Test::CheckChanges)
#BuildRequires: perl(Test::Distribution)
#BuildRequires: perl(Test::Kwalitee)
#BuildRequires: perl(Test::Perl::Critic)
#BuildRequires: perl(Test::Signature)
#BuildRequires: perl(Test::Spelling)
%{perl_requires}

%description
This module provides a set of additional functions useful for Perl symbols
manipulation.

All Perl symbols from the same package are organized as a stash. Each
symbol (glob) contains one or more of following slots: 'SCALAR', 'ARRAY',
'HASH', 'CODE', 'IO', 'FORMAT'. These slots are also accessible as standard
variables or bare words.

The Perl symbols table is directly accessible with typeglob prefix but it
can be difficult to read and problematic if strict mode is used. Also the
access to stash, glob and one of its slot have different syntax notation.

'stash' and 'fetch_glob' functions gets stash or glob without need to use
'no strict 'refs''.

'delete_glob' function allows to delete specific slot of symbol name
without deleting others.

'delete_sub' removes the symbol from class API. This symbol won't be
available as an object method.

'export_glob' function exports a glob to the target package.

'export_package' works like the Exporter manpage module and allows to
export symbols from one package to other.

'unexport_package' allows to delete previously exported symbols.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes examples LICENSE README xt

%changelog
