#
# spec file for package rakudo
#
# Copyright (c) 2019 SUSE LLC
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
Version:        2019.11
Release:        2.1
Summary:        Perl 6 implemenation that runs on MoarVM
License:        Artistic-2.0
Group:          Development/Languages/Other
URL:            http://rakudo.org/
Source0:        rakudo-%{version}.tar.gz
Patch0:         rakudo-buildroot-fix.diff
BuildRequires:  fdupes
BuildRequires:  moarvm-devel >= 2019.11
BuildRequires:  nqp >= 2019.11
Provides:       perl6 = %{version}-%{release}
Requires:       moarvm >= 2019.11
Requires:       nqp >= 2019.11
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Rakudo Perl 6, or just Rakudo, is an implementation of the Perl 6 
specification that runs on the Moar virtual machine.

%prep
%setup -q
%patch0 -p1

%build
perl Configure.pl --prefix="%{_prefix}"
make

%ifnarch armv6l armv6hl
# See armv6 issue: https://github.com/rakudo/rakudo/issues/2513
%check
RAKUDO_SKIP_TIMING_TESTS=1 make test
%endif

%install
%make_install
mkdir -p "%{buildroot}/%{_datadir}/perl6/bin"
cp tools/install-dist.p6 "%{buildroot}/%{_datadir}/perl6/bin/install-perl6-dist"
chmod +x "%{buildroot}/%{_datadir}/perl6/bin/install-perl6-dist"
rm "%{buildroot}/%{_bindir}/raku"
rm "%{buildroot}/%{_bindir}/raku-debug"
ln -s "rakudo %{buildroot}/%{_bindir}/raku"
ln -s "rakudo-debug %{buildroot}/%{_bindir}/raku-debug"
%fdupes %{buildroot}/%{_bindir}
%fdupes %{buildroot}/%{_datadir}/perl6/runtime

%files
%defattr(-,root,root)
%doc CREDITS
%license LICENSE
%{_bindir}/*
%{_datadir}/perl6

%changelog
