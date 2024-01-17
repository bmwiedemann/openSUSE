#
# spec file for package perl-WWW-PAUSE-CleanUpHomeDir
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


Name:           perl-WWW-PAUSE-CleanUpHomeDir
Version:        1.001002
Release:        0
%define cpan_name WWW-PAUSE-CleanUpHomeDir
Summary:        the module to clean up old dists from your PAUSE home directory
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/WWW-PAUSE-CleanUpHomeDir/
Source:         http://www.cpan.org/authors/id/Z/ZO/ZOFFIX/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Class::Accessor::Grouped)
BuildRequires:  perl(Devel::TakeHashArgs)
BuildRequires:  perl(HTML::TokeParser::Simple)
BuildRequires:  perl(Sort::Versions)
BuildRequires:  perl(URI)
BuildRequires:  perl(WWW::Mechanize)
Requires:       perl(Class::Accessor::Grouped)
Requires:       perl(Devel::TakeHashArgs)
Requires:       perl(HTML::TokeParser::Simple)
Requires:       perl(Sort::Versions)
Requires:       perl(URI)
Requires:       perl(WWW::Mechanize)
%{perl_requires}

%description
The module provides means to clean up your PAUSE home directory from old
distributions with ability to undelete files if you so prefer.

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
%doc Changes examples LICENSE README README.md

%changelog
