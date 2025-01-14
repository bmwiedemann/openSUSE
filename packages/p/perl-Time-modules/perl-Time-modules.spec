#
# spec file for package perl-Time-modules
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


Name:           perl-Time-modules
Version:        2013.0912
Release:        0
Summary:        Various Perl time modules
License:        SUSE-Permissive
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/MUIR/Time-modules-2013.0912
Source:         https://www.cpan.org/modules/by-module/Time/Time-modules-%{version}.tar.gz
Patch0:         fixtest.patch
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}
# MANUAL
BuildRequires:  timezone

%description
Perl modules providing various time functions.

%prep
%autosetup -p1 -n Time-modules-%{version}

%build
perl Makefile.PL
make %{?_smp_mflags}

%check
#cd ~/rpmbuild/BUILD/Time-modules-2013.0912/ && PERL5LIB=lib perl t/datetime.t | tee /tmp/datetime.out ; exit 1
make %{?_smp_mflags} test

%install
make DESTDIR=%{buildroot} install_vendor
%perl_process_packlist

%files
%doc CHANGELOG README
%{_mandir}/man?/*
%{perl_vendorlib}/Time/
%{perl_vendorarch}/auto/Time-modules/

%changelog
