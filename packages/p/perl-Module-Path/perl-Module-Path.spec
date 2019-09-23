#
# spec file for package perl-Module-Path
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


Name:           perl-Module-Path
Version:        0.19
Release:        0
%define cpan_name Module-Path
Summary:        get the full path to a locally installed module
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Module-Path/
Source:         http://www.cpan.org/authors/id/N/NE/NEILB/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Devel::FindPerl)
BuildRequires:  perl(Test::More) >= 0.88
%{perl_requires}

%description
This module provides a single function, 'module_path()', which takes a
module name and finds the first directory in your '@INC' path where the
module is installed locally. It returns the full path to that file,
resolving any symlinks. It is portable and only depends on core modules.

It works by looking in all the directories in '@INC' for an appropriately
named file:

I wrote this module because I couldn't find an alternative which dealt with
the points listed above, and didn't pull in what seemed like too many
dependencies to me.

The distribution for 'Module::Path' includes the 'mpath' script, which lets
you get the path for a module from the command-line:

 % mpath Module::Path

The 'module_path()' function will also cope if the module name includes
'.pm'; this means you can pass a partial path, such as used as the keys in
'%INC':

  module_path('Test/More.pm') eq $INC{'Test/More.pm'}

The above is the basis for one of the tests.

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
%doc Changes LICENSE README TODO.md

%changelog
