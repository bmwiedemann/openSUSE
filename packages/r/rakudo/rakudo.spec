#
# spec file for package rakudo
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           rakudo
Version:        2020.05.1
Release:        2.1
Summary:        Raku (formerly Perl 6) implemenation that runs on MoarVM
License:        Artistic-2.0
Group:          Development/Languages/Other
URL:            http://rakudo.org/
Source0:        rakudo-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  moarvm-devel >= 2020.05
BuildRequires:  nqp >= 2020.05
Provides:       perl6 = %{version}-%{release}
Requires:       moarvm >= 2020.05
Requires:       nqp >= 2020.05
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Rakudo, is an implementation of the Raku (formerly Perl 6)
specification that runs on the Moar virtual machine.

%prep
%setup -q

%build
perl Configure.pl --prefix="%{_prefix}"
make

%check
rm t/08-performance/99-misc.t
RAKUDO_SKIP_TIMING_TESTS=1 make test

%install
%make_install
mkdir -p "%{buildroot}/%{_datadir}/perl6/bin"
cp tools/install-dist.p6 "%{buildroot}/%{_datadir}/perl6/bin/install-perl6-dist"
chmod +x "%{buildroot}/%{_datadir}/perl6/bin/install-perl6-dist"
sed -i -e '1s:!/usr/bin/env :!/usr/bin/:' "%{buildroot}/%{_datadir}/perl6/bin"/*
rm "%{buildroot}/%{_bindir}/raku"
rm "%{buildroot}/%{_bindir}/raku-debug"
ln -s rakudo "%{buildroot}/%{_bindir}/raku"
ln -s rakudo-debug "%{buildroot}/%{_bindir}/raku-debug"
%fdupes %{buildroot}/%{_bindir}
%fdupes %{buildroot}/%{_datadir}/perl6/runtime

%files
%defattr(-,root,root)
%doc CREDITS
%license LICENSE
%{_bindir}/*
%{_datadir}/perl6

%changelog
