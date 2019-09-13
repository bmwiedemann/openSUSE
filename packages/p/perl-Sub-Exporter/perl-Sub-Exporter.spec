#
# spec file for package perl-Sub-Exporter
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


Name:           perl-Sub-Exporter
Version:        0.987
Release:        0
%define cpan_name Sub-Exporter
Summary:        a sophisticated exporter for custom-built routines
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Sub-Exporter/
Source:         http://www.cpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Data::OptList) >= 0.100
BuildRequires:  perl(Params::Util) >= 0.14
BuildRequires:  perl(Sub::Install) >= 0.92
BuildRequires:  perl(Test::More) >= 0.96

Requires:       perl(Data::OptList) >= 0.100
Requires:       perl(Params::Util) >= 0.14
Requires:       perl(Sub::Install) >= 0.92
%{perl_requires}

%description
*ACHTUNG!* If you're not familiar with Exporter or exporting, read the
Sub::Exporter::Tutorial manpage first!

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
%doc Changes LICENSE README

%changelog
