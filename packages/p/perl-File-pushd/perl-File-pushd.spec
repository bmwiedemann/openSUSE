#
# spec file for package perl-File-pushd
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-File-pushd
Version:        1.016
Release:        0
%define cpan_name File-pushd
Summary:        Change Directory Temporarily for a Limited Scope
License:        Apache-2.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/File-pushd/
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.96
%{perl_requires}

%description
File::pushd does a temporary 'chdir' that is easily and automatically
reverted, similar to 'pushd' in some Unix command shells. It works by
creating an object that caches the original working directory. When the
object is destroyed, the destructor calls 'chdir' to revert to the original
working directory. By storing the object in a lexical variable with a
limited scope, this happens automatically at the end of the scope.

This is very handy when working with temporary directories for tasks like
testing; a function is provided to streamline getting a temporary directory
from File::Temp.

For convenience, the object stringifies as the canonical form of the
absolute pathname of the directory entered.

*Warning*: if you create multiple 'pushd' objects in the same lexical
scope, their destruction order is not guaranteed and you might not wind up
in the directory you expect.

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
%doc Changes CONTRIBUTING.mkdn examples README Todo
%license LICENSE

%changelog
