#
# spec file for package oils-for-unix
#
# Copyright (c) 2025 SUSE LLC
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


Name:           oils-for-unix
Version:        0.27.0
Release:        0
Summary:        A bash compatible shell and a new modern shell
License:        Apache-2.0 AND CNRI-Python-GPL-Compatible
URL:            https://oils.pub
Source:         %{url}/download/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  ninja

%description
oils-for-unix contains two different shells: a POSIX and bash compatible shell called OSH,
and a modern Python-like shell called YSH.

%prep
%autosetup

%build
%{_configure} \
	--prefix=%{_prefix} \
	--exec-prefix=%{_exec_prefix} \
	--bindir=%{_bindir} \
	--sbindir=%{_sbindir} \
	--sysconfdir=%{_sysconfdir} \
	--datadir=%{_datadir} \
	--includedir=%{_includedir} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libexecdir} \
	--localstatedir=%{_localstatedir} \
	--sharedstatedir=%{_sharedstatedir} \
	--mandir=%{_mandir} \
	--infodir=%{_infodir}
_build/oils.sh

%install
DESTDIR=%{buildroot} ./install

%files
%license LICENSE.txt
%doc README-native.txt
%{_bindir}/oils-for-unix
%{_bindir}/osh
%{_bindir}/ysh
%{_mandir}/man1/osh.1%{?ext_man}

%changelog
