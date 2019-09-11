#
# spec file for package clinfo
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015, Martin Hauke <mardnh@gmx.de>
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


Name:           clinfo
Version:        2.2.18.04.06
Release:        0
Summary:        Utility that reports status information for all installed OpenCL ICDs
License:        SUSE-Public-Domain
Group:          Productivity/Other
Url:            https://github.com/Oblomov/clinfo/
Source:         https://github.com/Oblomov/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  opencl-headers
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(OpenCL)

%description
A simple OpenCL application that enumerates all possible platform and
device properties. Inspired by AMD's program of the same name, it is
coded in pure C99 and it tries to output all possible information,
including that provided by platform-specific extensions, and not to
crash on platform-unsupported properties (e.g. 1.2 properties on 1.1
platforms).

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}

%install
export PREFIX="%{buildroot}/%{_prefix}" MANDIR="%{buildroot}/%{_mandir}"
%make_install

%files
%doc README.md
%license LICENSE
%{_bindir}/clinfo
%{_mandir}/man1/clinfo.1%{ext_man}

%changelog
