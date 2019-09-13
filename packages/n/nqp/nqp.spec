#
# spec file for package nqp
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           nqp
Version:        2019.07
Release:        1.1
Summary:        Not Quite Perl
License:        Artistic-2.0
Group:          Development/Languages/Other
Url:            http://rakudo.org/
Source:         nqp-%{version}.tar.gz
BuildRequires:  moarvm-devel >= 2019.07
Requires:       moarvm >= 2019.07
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is "Not Quite Perl" -- a compiler for a subset of Perl 6 used
to implement a full Perl 6 compiler.

%prep
%setup -q

%build
perl Configure.pl --backends=moar --prefix=%{_usr} --with-moar=/usr/bin/moar
make

%check
make test

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CREDITS
%license LICENSE
%{_bindir}/*
%{_datadir}/nqp

%changelog
