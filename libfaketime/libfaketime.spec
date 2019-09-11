#
# spec file for package libfaketime
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


Name:           libfaketime
Version:        0.9.7
Release:        0
Summary:        FakeTime Preload Library
License:        GPL-2.0-only
Group:          System/Libraries
Url:            https://github.com/wolfcw/libfaketime
Source:         https://github.com/wolfcw/libfaketime/archive/v%{version}.tar.gz
# https://github.com/wolfcw/libfaketime/pull/161 (rebased to 0.9.7)
Patch0:         161.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
report faked system time to programs without having to change the system-wide time

%prep
%setup -q
%patch0 -p1

%build
make %{?_smp_mflags} PREFIX=%{_prefix} LIBDIRNAME=/%{_lib}/%{name}

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIRNAME=/%{_lib}/%{name}
rm %{buildroot}%{_datadir}/doc/faketime/*

%files
%defattr(-,root,root)
%doc NEWS README
%license COPYING
%{_bindir}/faketime
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libfaketime.so.1
%{_libdir}/%{name}/libfaketimeMT.so.1
%{_mandir}/man1/faketime.1*

%changelog
