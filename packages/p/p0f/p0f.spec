#
# spec file for package p0f
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2016, Martin Hauke <mardnh@gmx.de>
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


Name:           p0f
Version:        3.09b
Release:        0
Summary:        A versatile passive OS fingerprinting tool
License:        LGPL-2.1-only
Group:          Productivity/Networking/Diagnostic
URL:            http://lcamtuf.coredump.cx/p0f3/
Source:         http://lcamtuf.coredump.cx/p0f3/releases/%{name}-%{version}.tgz
Patch0:         p0f-set-fingerprint-file.diff
Patch1:         p0f-fix-gcc14.patch
BuildRequires:  libpcap-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
P0f is a tool that utilizes an array of sophisticated, purely passive traffic
fingerprinting mechanisms to identify the players behind any incidental TCP/IP
communications (often as little as a single normal SYN) without interfering in
any way.

%prep
%autosetup -p1

%build
make # %{?_smp_mflags}
cd tools && make # %{?_smp_mflags}

%install
install -Dpm 0755 p0f %{buildroot}%{_bindir}/p0f
install -Dpm 0755 tools/p0f-client %{buildroot}%{_bindir}/p0f-client
install -Dpm 0755 tools/p0f-sendsyn %{buildroot}%{_bindir}/p0f-sendsyn
install -Dpm 0755 tools/p0f-sendsyn6 %{buildroot}%{_bindir}/p0f-sendsyn6
install -Dpm 0644 p0f.fp %{buildroot}/%{_sysconfdir}/p0f3/p0f.fp

%files
%defattr(-,root,root)
%doc docs/{ChangeLog,COPYING,existential-notes.txt,extra-sigs.txt,README,TODO}
%{_bindir}/p0f
%{_bindir}/p0f-client
%{_bindir}/p0f-sendsyn
%{_bindir}/p0f-sendsyn6
%dir %{_sysconfdir}/p0f3/
%config %{_sysconfdir}/p0f3/p0f.fp

%changelog
