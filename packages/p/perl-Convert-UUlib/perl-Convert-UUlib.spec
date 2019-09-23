#
# spec file for package perl-Convert-UUlib
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


%define cpan_name Convert-UUlib
Name:           perl-Convert-UUlib
Version:        1.5
Release:        0
Summary:        Perl interface to the uulib library
License:        GPL-1.0-or-later OR Artistic-1.0
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/pod/Convert::UUlib
Source:         https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/%{cpan_name}-%{version}.tar.gz
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Canary::Stability)
Provides:       p_conulb
Obsoletes:      p_conulb
%{perl_requires}

%description
A Perl interface to the uulib library

%prep
%setup -q -n %{cpan_name}-%{version}
# ---------------------------------------------------------------------------

%build
perl Makefile.PL
make %{?_smp_mflags}

%check
make %{?_smp_mflags} test
# ---------------------------------------------------------------------------

%install
make DESTDIR=%{buildroot} install_vendor
%perl_process_packlist

%files
%dir %{perl_vendorarch}/Convert
%{perl_vendorarch}/Convert/UUlib.pm
%dir %{perl_vendorarch}/auto/Convert
%{perl_vendorarch}/auto/Convert/UUlib
%{_mandir}/man3/Convert::UUlib.3pm.gz
%license COPYING COPYING.Artistic COPYING.GNU
%doc Changes MANIFEST README example-decoder doc

%changelog
