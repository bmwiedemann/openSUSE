#
# spec file for package perl-String-Truncate
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-String-Truncate
Version:        1.100602
Release:        0
%define cpan_name String-Truncate
Summary:        a module for when strings are too long to be displayed in...
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/String-Truncate/
Source:         http://www.cpan.org/authors/id/R/RJ/RJBS/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Sub::Exporter) >= 0.953
BuildRequires:  perl(Sub::Exporter::Util)
BuildRequires:  perl(Sub::Install) >= 0.03
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Sub::Exporter) >= 0.953
Requires:       perl(Sub::Exporter::Util)
Requires:       perl(Sub::Install) >= 0.03
%{perl_requires}

%description
a module for when strings are too long to be displayed in...

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
