#
# spec file for package zcfan
#
# Copyright (c) 2024 SUSE LLC
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


Name:           zcfan
Version:        1.4.0
Release:        0
Summary:        Zero-configuration fan control daemon for ThinkPads
License:        MIT
URL:            https://github.com/cdown/zcfan
Source:         https://github.com/cdown/zcfan/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         move_executable_to_sbin.patch
%if 0%{?suse_version} < 1550
BuildRequires:  gcc11
%else
BuildRequires:  gcc >= 11
%endif
BuildRequires:  make
Conflicts:      thinkfan

%description
Zero-configuration fan control daemon for ThinkPads with watchdog
support and automatic temperature- and time-based hysteresis (no
bouncing between fan levels).

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1550
export CC=gcc-11
%endif
%make_build CFLAGS="%{optflags} -fPIE" LDFLAGS="%{optflags} -pie"

%install
%make_install prefix=%{_prefix}

%pre
%service_add_pre zcfan.service

%post
%service_add_post zcfan.service

%preun
%service_del_preun zcfan.service

%postun
%service_del_postun zcfan.service

%files
%license LICENSE
%doc README.md
%{_sbindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_unitdir}/%{name}.service

%changelog
