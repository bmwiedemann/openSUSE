#
# spec file for package perl-Sub-Identify
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


Name:           perl-Sub-Identify
Version:        0.14
Release:        0
%define cpan_name Sub-Identify
Summary:        Retrieve names of code references
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Sub-Identify/
Source0:        https://cpan.metacpan.org/authors/id/R/RG/RGARCIA/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
'Sub::Identify' allows you to retrieve the real name of code references.

It provides six functions, all of them taking a code reference.

'sub_name' returns the name of the code reference passed as an argument (or
'__ANON__' if it's an anonymous code reference), 'stash_name' returns its
package, and 'sub_fullname' returns the concatenation of the two.

'get_code_info' returns a list of two elements, the package and the
subroutine name (in case of you want both and are worried by the speed.)

In case of subroutine aliasing, those functions always return the original
name.

'get_code_location' returns a two-element list containing the file name and
the line number where the subroutine has been defined.

'is_sub_constant' returns a boolean value indicating whether the subroutine
is a constant or not.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README.mdown TODO.mdown

%changelog
