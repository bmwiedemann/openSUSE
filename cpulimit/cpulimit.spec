# vim: set sw=4 ts=4 et nu:
#
# spec file for package cpulimit
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


Name:           cpulimit
Version:        2.5
Release:        0
Summary:        Limit the CPU Usage of a Process
License:        GPL-2.0+
Group:          System/Monitoring
Url:            http://limitcpu.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/limitcpu/%{name}-%{version}.tar.gz
Patch0:         %{name}-2.2-do_not_forget_version.patch
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  make

%description
LimitCPU is a program to throttle the CPU cycles used by other applications.
LimitCPU will monitor a process and make sure its CPU usage stays at or
below a given percentage. This can be used to make sure your system
has plenty of CPU cycles available for other tasks. It can also be used
to keep laptops cool in the face of CPU-hungry processes and for limiting
virtual machines.

LimitCPU is the direct child of CPUlimit, a creation of Angelo Marletta,
which can be found at http://cpulimit.sourceforge.net

%prep
%setup -q
%patch0 -p1

%build
make %{?_smp_mflags} \
    CFLAGS="%{optflags}"

%install
%make_install PREFIX=%{buildroot}/%{_prefix}

%files
%doc LICENSE CHANGELOG README TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
