#
# spec file for package forkbomb
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           forkbomb
Version:        1.4
Release:        0
Summary:        Controlled fork() bomber for testing heavy system load
License:        SUSE-Public-Domain
Group:          System/Benchmark
URL:            http://home.tiscali.cz:8080/~cz210552/forkbomb.html
Source:         http://home.tiscali.cz:8080/~cz210552/distfiles/%{name}-%{version}.tar.gz

%description
Classic Unix fork() bomber. Includes CPU hanger, memory allocator, memory
toucher and zombie dance team. You can test how will your computer behave under
heavy CPU, process, memory load. Linux 2.4 and FreeBSD 5.4 don't survive
classic forkbomb. Forkbomb is also useful as realloc() benchmark.

%prep
%setup -q

%build
make CFLAGS="%{optflags}" %{?_smp_mflags} %{name}

%install
install -Dpm 0755 %{name}   \
  %{buildroot}%{_bindir}/%{name}
install -Dpm 0444 %{name}.8 \
  %{buildroot}%{_mandir}/man8/%{name}.8

%files
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8%{ext_man}

%changelog
