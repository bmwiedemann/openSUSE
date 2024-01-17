#
# spec file for package perl-IO-SessionData
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


Name:           perl-IO-SessionData
Version:        1.03
Release:        0
%define cpan_name IO-SessionData
Summary:        Supporting module for SOAP::Lite
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/IO-SessionData/
Source:         http://www.cpan.org/authors/id/P/PH/PHRED/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires: perl(IO::SessionData)
#BuildRequires: perl(IO::SessionSet)
%{perl_requires}

%description
supporting module for SOAP::Lite

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
%doc Changes README

%changelog
