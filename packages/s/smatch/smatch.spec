#
# spec file for package smatch
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


Name:           smatch
Version:        1.72+20220506
Release:        0
Summary:        Static analysis tool for C
License:        GPL-2.0-only
Group:          Development/Tools/Building
URL:            http://smatch.sf.net
Source:         %{name}-%{version}.tar.xz
Patch0:         Makefile-allow-CFLAGS-to-be-redefined.patch
Patch1:         Makefile-use-CFLAGS-when-linking.patch
Patch2:         check_free-declare-is_percent_p_print-before-use.patch
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  sqlite3-devel
BuildRequires:  xz

%description
Smatch is a static analysis tool for C. Most of the checks are for the linux
kernel. Please write checks for your project. It's fun and easy!

%prep
%autosetup -p1

%build
make %{?_smp_mflags} V=1 CFLAGS="%{optflags} -Wno-unused-result -Wno-abi" \
	INSTALL_PREFIX=%{_prefix} \
	LIBDIR=%{_libdir} \
	PKGCONFIGDIR=%{_datadir}/pkgconfig \
	smatch

%install
install -d %{buildroot}/%{_bindir} %{buildroot}/%{_datadir}/%{name}
install -t %{buildroot}/%{_bindir} smatch
cp -ar smatch_data smatch_scripts %{buildroot}/%{_datadir}/%{name}/

# empty files
rm -f %{buildroot}/%{_datadir}/%{name}/smatch_data/db/fixup_smatch_generic.sh
rm -f %{buildroot}/%{_datadir}/%{name}/smatch_data/kernel.allocation_funcs.remove

%files
%defattr(-,root,root)
%license LICENSE
%doc Documentation/smatch*
%{_bindir}/smatch
%{_datadir}/%{name}

%changelog
