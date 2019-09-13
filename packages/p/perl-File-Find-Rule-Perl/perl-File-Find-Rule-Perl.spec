#
# spec file for package perl-File-Find-Rule-Perl
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


Name:           perl-File-Find-Rule-Perl
Version:        1.15
Release:        0
%define cpan_name File-Find-Rule-Perl
Summary:        Common rules for searching for Perl things
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/File-Find-Rule-Perl/
Source0:        http://www.cpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Find::Rule) >= 0.20
BuildRequires:  perl(Params::Util) >= 0.38
BuildRequires:  perl(Parse::CPAN::Meta) >= 1.38
Requires:       perl(File::Find::Rule) >= 0.20
Requires:       perl(Params::Util) >= 0.38
Requires:       perl(Parse::CPAN::Meta) >= 1.38
%{perl_requires}

%description
I write a lot of things that muck with Perl files. And it always annoyed me
that finding "perl files" requires a moderately complex the
File::Find::Rule manpage pattern.

*File::Find::Rule::Perl* provides methods for finding various types
Perl-related files, or replicating search queries run on a distribution in
various parts of the CPAN ecosystem.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
# MANUAL no testing (broken within build env)
#%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes

%changelog
