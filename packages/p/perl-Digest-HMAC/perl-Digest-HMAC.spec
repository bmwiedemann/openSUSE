#
# spec file for package perl-Digest-HMAC
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


Name:           perl-Digest-HMAC
%define cpan_name Digest-HMAC
Summary:        Keyed-Hashing for Message Authentication
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Version:        1.03
Release:        0
Url:            http://search.cpan.org/dist/Digest-HMAC/
Source:         http://www.cpan.org/authors/id/G/GA/GAAS/Digest-HMAC-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Digest::MD5) >= 2
BuildRequires:  perl(Digest::SHA1) >= 1
Requires:       perl(Digest::MD5) >= 2
Requires:       perl(Digest::SHA1) >= 1

%description
HMAC is used for message integrity checks between two parties that share a
secret key, and works in combination with some other Digest algorithm,
usually MD5 or SHA-1. The HMAC mechanism is described in RFC 2104.

HMAC follow the common 'Digest::' interface, but the constructor takes the
secret key and the name of some other simple 'Digest::' as argument.

Authors:
--------
    Graham Barr <gbarr@ti.com>
    Gisle Aas <gisle@aas.no>

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
### since 11.4 perl_process_packlist
### removes .packlist, perllocal.pod files
%if 0%{?suse_version} > 1130
%perl_process_packlist
%else
# do not perl_process_packlist
# remove .packlist file
%{__rm} -rf $RPM_BUILD_ROOT%perl_vendorarch
# remove perllocal.pod file
%{__rm} -f $RPM_BUILD_ROOT%perl_archlib/perllocal.pod
%endif
%perl_gen_filelist

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files -f %{name}.files
%defattr(-,root,root,-)
%doc Changes README

%changelog
