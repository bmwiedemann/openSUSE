#
# spec file for package perl-Data-Uniqid
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Data-Uniqid
Version:        0.12
Release:        0
%define cpan_name Data-Uniqid
Summary:        Perl extension for simple genrating of unique id's
License:        Artistic-1.0 or GPL-2.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Data-Uniqid/
Source:         http://www.cpan.org/authors/id/M/MW/MWX/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
%{perl_requires}

%description
Data::Uniqid provides three simple routines for generating unique ids.
These ids are coded with a Base62 systen to make them short and handy (e.g.
to use it as part of a URL).

  suinqid
    genrates a very short id valid only for the localhost and with a 
    liftime of 1 day
  
  uniqid
    generates a short id valid on the local host 

  luniqid 
    generates a long id valid everywhere and ever

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
