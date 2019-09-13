#
# spec file for package perl-Crypt-Blowfish
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


%bcond_with opt

Name:           perl-Crypt-Blowfish
Version:        2.14
Release:        0
%define cpan_name Crypt-Blowfish
Summary:        Perl Blowfish encryption module
License:        BSD-3-Clause
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Crypt-Blowfish/
Source:         http://www.cpan.org/authors/id/D/DP/DPARIS/%{cpan_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%if %{with opt}
BuildRequires:  perl(Crypt::CBC)
%endif
%if 0%{?suse_version} > 1010
Recommends:     perl(Crypt::CBC)
%endif
%{perl_requires}

%description
Blowfish is capable of strong encryption and can use key sizes up to 56
bytes (a 448 bit key). You're encouraged to take advantage of the full key
size to ensure the strongest encryption possible from this module.

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
%doc Changes COPYRIGHT README

%changelog
