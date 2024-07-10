#
# spec file for package libfaketime
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


Name:           libfaketime
Version:        0.9.10
Release:        0
Summary:        FakeTime Preload Library
License:        GPL-2.0-only
Group:          System/Libraries
URL:            https://github.com/wolfcw/libfaketime
Source:         https://github.com/wolfcw/libfaketime/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
report faked system time to programs without having to change the system-wide time

%prep
%setup -q

%build
make %{?_smp_mflags} PREFIX=%{_prefix} LIBDIRNAME=/%{_lib}/%{name}

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} LIBDIRNAME=/%{_lib}/%{name}
rm %{buildroot}%{_datadir}/doc/faketime/*

%files
%doc NEWS README
%license COPYING
%{_bindir}/faketime
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libfaketime.so.1
%{_libdir}/%{name}/libfaketimeMT.so.1
%{_mandir}/man1/faketime.1%{?ext_man}

%changelog
