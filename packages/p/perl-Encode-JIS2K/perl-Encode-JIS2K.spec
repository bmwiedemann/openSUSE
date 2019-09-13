#
# spec file for package perl-Encode-JIS2K
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define cpan_name Encode-JIS2K
Name:           perl-Encode-JIS2K
Version:        0.03
Release:        0
Summary:        JIS X 0212 (aka JIS 2000) Encodings
License:        Artistic-1.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/pod/Encode::JIS2K
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/%{cpan_name}-%{version}.tar.gz
Patch0:         perl-Encode-JIS2K.patch
BuildRequires:  perl
BuildRequires:  perl-macros
Requires:       %{_bindir}/enc2xs
%{perl_requires}

%description
This module implements encodings that covers JIS X 0213 charset (AKA
JIS 2000, hence the module name).

%define __find_provides %{_prefix}/lib/rpm/find-provides
%define __find_requires %{_prefix}/lib/rpm/find-requires

%prep
%setup -q -n Encode-JIS2K-%{version}
%patch0 -p1

%build
CFLAGS="%{optflags}" perl Makefile.PL
make %{?_smp_mflags}

%install
install -d %{buildroot}/%{perl_archlib}
make DESTDIR=%{buildroot} install_vendor
%perl_process_packlist

%post
enc2xs -C > /dev/null 2>&1

%postun
if [ $1 = 0 ]; then
    enc2xs -C > /dev/null 2>&1
fi

%files
%doc Changes MANIFEST README*
%{_mandir}/man3/*.3pm.gz
%{perl_vendorarch}/Encode/
%{perl_vendorarch}/auto/Encode/

%changelog
