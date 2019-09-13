#
# spec file for package perl-Encode-HanExtra
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Encode-HanExtra
PreReq:         /usr/bin/enc2xs
Version:        0.23
Release:        0
Url:            http://search.cpan.org/~autrijus/Encode-HanExtra-0.23/
Source0:        http://search.cpan.org/CPAN/authors/id/A/AU/AUDREYT/Encode-HanExtra-0.23.tar.gz
Patch1:         HanExtra-include-sort.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Extra sets of Chinese encodings
License:        MIT
Group:          Development/Libraries/Perl
%{perl_requires}
BuildRequires:  perl
BuildRequires:  perl-macros

%description
Perl 5.7.3 and later ships with an adequate set of Chinese encodings,
including the most used CP950, CP936 (also known as GBK), Big5,
Big5-HKSCS, EUC-CN, HZ, and ISO-IR-165.

However, the numbers of Chinese encodings are staggering, and a
complete coverage will easily increase the size of perl distribution by
several megabytes; hence, this CPAN module tries to provide the rest of
them.

%prep
%setup -q -n Encode-HanExtra-%{version}
%patch1 -p1

%build
sed -i -e 's/use inc::Module::Install;/use lib q[.];\nuse inc::Module::Install;/' Makefile.PL
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL
make %{?_smp_mflags}

%install
install -d $RPM_BUILD_ROOT/%{perl_archlib}
make DESTDIR=$RPM_BUILD_ROOT install_vendor
%perl_process_packlist

%post
enc2xs -C >/dev/null 2>&1

%postun
if [ $1 = 0 ]; then
    enc2xs -C >/dev/null 2>&1
fi

%clean 

%files 
%defattr(-,root,root)
%doc Changes MANIFEST README*
%{_mandir}/man3/*.3pm.gz
%{perl_vendorarch}/Encode/
%{perl_vendorarch}/auto/Encode/

%changelog
