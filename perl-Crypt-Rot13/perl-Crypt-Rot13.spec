#
# spec file for package perl-Crypt-Rot13 (Version 0.6)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild


Name:           perl-Crypt-Rot13
Version:        0.6
Release:        4
AutoReqProv:    on
Group:          Development/Libraries/Perl
License:        GPL-2.0+
Url:            http://search.cpan.org/dist/Crypt-Rot13/
Summary:        Rot13 (Caesar) encryption for perl
Source:         Crypt-Rot13-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildArch:      noarch

%description
This package provides ROT13 Algorithm (Caesar) as a Perl module.

%prep
%setup -n Crypt-Rot13-%{version} -q

%build
perl Makefile.PL OPTIMIZE="$RPM_OPT_FLAGS -Wall"
make %{?_smp_mflags}

%check
make test

%install
make DESTDIR=$RPM_BUILD_ROOT install_vendor
# remove .packlist file
%{__rm} -rf $RPM_BUILD_ROOT%perl_vendorarch
# remove perllocal.pod file
%{__rm} -rf $RPM_BUILD_ROOT%perl_archlib
#%perl_gen_filelist

%clean
rm -rf $RPM_BUILD_ROOT

#%files -f %{name}.files

%files
%defattr(-,root,root,-)
%doc COPYING Changes README
%doc %{_mandir}/man3/Crypt::Rot13.3pm*
%dir %{perl_vendorlib}/Crypt
%{perl_vendorlib}/Crypt/Rot13.pm

%changelog
