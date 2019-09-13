#
# spec file for package perl-Array-Unique
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


Name:           perl-Array-Unique
Version:        0.08
Release:        0
%define         cpan_name Array-Unique
Summary:        Tie-able array that allows only unique values
License:        GPL-2.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Array-Unique/
#Source:         http://www.cpan.org/authors/id/S/SZ/SZABGAB/Array-Unique-%%{version}.tar.gz
Source:         %{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More) >= 0.47
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%{perl_requires}

%description
This package lets you create an array which will allow only one occurrence
of any value.

In other words no matter how many times you put in 42 it will keep only the
first occurrence and the rest will be dropped.

You use the module via tie and once you tied your array to this module it
will behave correctly.

Uniqueness is checked with the 'eq' operator so among other things it is
case sensitive.

As a side effect the module does not allow undef as a value in the array.

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

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.files
%defattr(644,root,root,755)
%doc Changes README

%changelog
