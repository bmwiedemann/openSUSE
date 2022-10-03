#
# spec file for package rakudo
#
# Copyright (c) 2022 SUSE LLC
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
Version:        2022.07
Release:        2.1
Summary:        Raku (formerly Perl 6) implemenation that runs on MoarVM
License:        Artistic-2.0
Group:          Development/Languages/Other
URL:            https://rakudo.org/
Source0:        rakudo-%{version}.tar.gz
Patch0:         rakudo-test-log.diff
Patch1:         rakudo-fix-module-installation.diff
%if !0%{?rhel_version}
BuildRequires:  fdupes
%endif
BuildRequires:  moarvm-devel >= 2022.07
BuildRequires:  nqp >= 2022.07
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(IPC::Cmd)
BuildRequires:  perl(YAML::Tiny)
Provides:       perl6 = %{version}-%{release}
Requires:       moarvm >= 2022.07
Requires:       nqp >= 2022.07
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%ifarch s390x
BuildRequires:  libffi-devel
%endif

%description
The most mature, production-ready implementation of the Raku language.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
perl Configure.pl --prefix="%{_prefix}"
VERBOSE_BUILD=1 make

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
%if !0%{?rhel_version}
%fdupes %{buildroot}/%{_bindir}
%fdupes %{buildroot}/%{_datadir}/perl6/runtime
%endif

%files
%defattr(-,root,root)
%doc CREDITS
%license LICENSE
%{_bindir}/*
%{_datadir}/perl6

%changelog
