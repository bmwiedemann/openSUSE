# vim: set sw=4 ts=4 et nu:
#
# spec file for package cpulimit
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


Name:           cpulimit
Version:        2.8
Release:        0
Summary:        Limit the CPU Usage of a Process
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            http://limitcpu.sourceforge.net/
Source0:        https://downloads.sourceforge.net/limitcpu/%{name}-%{version}.tar.gz
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
%make_build \
    CFLAGS="%{optflags}"

%install
%make_install PREFIX=%{buildroot}/%{_prefix}

%files
%license LICENSE
%doc CHANGELOG README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
