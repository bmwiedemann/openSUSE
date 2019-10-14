#
# spec file for package ledmon
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


Name:           ledmon
Version:        0.92
Release:        0
Summary:        Enclosure LED Utilities
License:        GPL-2.0-only
Group:          Hardware/Other
Url:            https://github.com/intel/ledmon/
Source0:        https://github.com/intel/ledmon/archive/v%{version}.tar.gz
BuildRequires:  libsgutils-devel
BuildRequires:  libudev-devel
Provides:       sgpio:/sbin/ledmon
Provides:       sgpio:/{%{_bindir}}/ledctl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The ledctl application and ledmon daemon are part of Intel(R) LED
ControlUtilities. They help to enable LED management for software RAID
solutions.

%prep
%setup -q

%build
make -j1 CXFLAGS="%{optflags} -lsgutils2 -std=c99"

%install
%make_install

%files
%defattr(-,root,root)
%doc README COPYING
%{_sbindir}/ledmon
%{_sbindir}/ledctl
%{_mandir}/man5/ledmon.conf.5%{ext_man}
%{_mandir}/man8/ledctl.8%{ext_man}
%{_mandir}/man8/ledmon.8%{ext_man}

%changelog
