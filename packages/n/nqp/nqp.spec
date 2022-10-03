#
# spec file for package nqp
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


Name:           nqp
Version:        2022.07
Release:        1.1
Summary:        Not Quite Perl
License:        Artistic-2.0
Group:          Development/Languages/Other
URL:            https://github.com/Raku/nqp
Source:         nqp-%{version}.tar.gz
BuildRequires:  moarvm-devel >= 2022.07
Requires:       moarvm >= 2022.07
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%ifarch s390x
BuildRequires:  libffi-devel
%endif
BuildRequires:  perl
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(IPC::Cmd)

%description
This is "Not Quite Perl" -- a lightweight Raku-like environment for virtual
machines. The key feature of NQP is that it's designed to be a very small
environment (as compared with, say, raku or Rakudo) and is focused on being
a high-level way to create compilers and libraries for virtual machines like
MoarVM, the JVM, and others.

Unlike a full-fledged implementation of Raku, NQP strives to have as small a
runtime footprint as it can, while still providing a Raku object model and
regular expression engine for the virtual machine.

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
