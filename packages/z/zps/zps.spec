#
# spec file for package zps
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


Name:           zps
Version:        1.2.8
Release:        0
Summary:        Utility for listing and reaping zombie processes
License:        GPL-3.0-only
Group:          System/Monitoring
URL:            https://github.com/orhun/zps
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.sig
Source2:        %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz.sha512
BuildRequires:  c_compiler

%description
zps aims to list the running processes at a particular time with stats and indicate
the zombie processes on this list. It can also reap these zombie processes automatically
if `--reap` argument is provided. There's also `--lreap` argument for reaping zombie
processes after listing.

%prep
%setup -q

%build
%make_build

%install
# They should have used a more convenient flag/variable
export TARGET=%{buildroot}
%make_install
install -Dm644 man/%{name}.1 -t %{buildroot}%{_mandir}/man1/
# Makefile sets wrong permissions for the desktop applicaation entry
install -Dm644 .application/%{name}.desktop -t %{buildroot}%{_datadir}/applications/

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1%{?ext_man}
%license LICENSE
%doc README.md README_KO.md

%changelog
