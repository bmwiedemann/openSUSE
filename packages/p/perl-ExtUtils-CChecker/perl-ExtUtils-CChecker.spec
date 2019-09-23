#
# spec file for package perl-ExtUtils-CChecker
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


Name:           perl-ExtUtils-CChecker
Version:        0.10
Release:        0
%define cpan_name ExtUtils-CChecker
Summary:        Configure-Time Utilities for Using C Headers,
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/ExtUtils-CChecker/
Source0:        http://www.cpan.org/authors/id/P/PE/PEVANS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::CBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::Fatal)
Requires:       perl(ExtUtils::CBuilder)
%{perl_requires}

%description
Often Perl modules are written to wrap functionality found in existing C
headers, libraries, or to use OS-specific features. It is useful in the
_Build.PL_ or _Makefile.PL_ file to check for the existance of these
requirements before attempting to actually build the module.

Objects in this class provide an extension around the ExtUtils::CBuilder
manpage to simplify the creation of a _.c_ file, compiling, linking and
running it, to test if a certain feature is present.

It may also be necessary to search for the correct library to link against,
or for the right include directories to find header files in. This class
also provides assistance here.

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
%doc Changes LICENSE README

%changelog
