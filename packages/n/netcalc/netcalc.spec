#
# spec file for package netcalc
#
# Copyright (c) 2021 SUSE LLC
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


Name:           netcalc
Version:        2.1.6
Release:        0
Summary:        IP subnet calculator
License:        BSD-3-Clause
URL:            https://github.com/troglobit/netcalc
Source:         https://github.com/troglobit/netcalc/releases/download/v%{version}/%{name}-%{version}.tar.gz
# for tests
BuildRequires:  bats

%description
netcalc is an IP network calculator that can calcuate host IP ranges, subnet
masks, and split networks. It is a clone of sipcalc and uses the output format
of ipcalc.

%prep
%setup -q

%build
%configure \
	--docdir=%{_docdir}/%{name} \
	--disable-ipcalc-symlink
%make_build

%install
%make_install
# installed vial %%license macro
rm -v %{buildroot}/%{_docdir}/netcalc/LICENSE

%check
%make_build check

%files
%license LICENSE
%doc ChangeLog.md AUTHORS README.md TODO
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_bindir}/%{name}

%changelog
