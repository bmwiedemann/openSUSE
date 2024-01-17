#
# spec file for package dynamips
#
# Copyright (c) 2023 SUSE LLC
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


Name:           dynamips
Version:        0.2.23
Release:        0
Summary:        Cisco router Emulator
License:        GPL-2.0-or-later
Group:          System/Emulators/Other
URL:            https://www.gns3.net
Source:         https://github.com/GNS3/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         define-s390x-arch.patch
BuildRequires:  cmake
BuildRequires:  libelf-devel
BuildRequires:  libpcap-devel
%ifarch x86_64
%if %{undefined fedora}
BuildRequires:  glibc-32bit
BuildRequires:  glibc-devel-32bit
%endif
%endif

%description
Cisco Router Emulator supported by GNS3 Community

Dynamips emulates Cisco 7200/3600/3725/3745/2691 Routers on a traditional PC.
You can use dynamips to create labs. It uses IOS Images (which are not part
of this package). Of course, this emulator cannot replace a real router. It is
simply a complementary tool to real labs for administrators of Cisco networks
or people wanting to pass their CCNA/CCNP/CCIE exams.

%prep
%setup -q
%patch1 -p1

%build
%cmake \
%ifarch x86_64
	-DYNAMIPS_ARCH=amd64 \
%endif
..
%make_jobs

%install
%cmake_install

%files
%{_bindir}/%{name}
%{_bindir}/nvram_export
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/nvram_export.1%{?ext_man}
%{_mandir}/man7/hypervisor_mode.7%{?ext_man}
%{_datadir}/doc/%{name}

%changelog
