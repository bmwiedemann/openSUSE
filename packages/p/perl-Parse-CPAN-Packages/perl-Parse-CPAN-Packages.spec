#
# spec file for package perl-Parse-CPAN-Packages
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


Name:           perl-Parse-CPAN-Packages
Version:        2.40
Release:        0
%define cpan_name Parse-CPAN-Packages
Summary:        Parse 02packages.details.txt.gz
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Parse-CPAN-Packages/
Source:         http://www.cpan.org/authors/id/M/MI/MITHALDU/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Archive::Peek)
BuildRequires:  perl(CPAN::DistnameInfo)
BuildRequires:  perl(Compress::Zlib)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(Moo)
BuildRequires:  perl(PPI)
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(Test::InDistDir)
BuildRequires:  perl(Type::Utils)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(version)
Requires:       perl(Archive::Peek)
Requires:       perl(CPAN::DistnameInfo)
Requires:       perl(Compress::Zlib)
Requires:       perl(File::Slurp)
Requires:       perl(Moo)
Requires:       perl(PPI)
Requires:       perl(Path::Class)
Requires:       perl(Test::InDistDir)
Requires:       perl(Type::Utils)
Requires:       perl(Types::Standard)
Requires:       perl(version)
%{perl_requires}

%description
The Comprehensive Perl Archive Network (CPAN) is a very useful collection
of Perl code. It has several indices of the files that it hosts, including
a file named "02packages.details.txt.gz" in the "modules" directory. This
file contains lots of useful information and this module provides a simple
interface to the data contained within.

In a future release the Parse::CPAN::Packages::Package manpage and the
Parse::CPAN::Packages::Distribution manpage might have more information.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

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
%doc CHANGES README

%changelog
