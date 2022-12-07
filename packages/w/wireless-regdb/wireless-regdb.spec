#
# spec file for package wireless-regdb
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


Name:           wireless-regdb
Version:        20221205
Release:        0
Summary:        802.11 regulatory domain database
License:        ISC
Group:          Hardware/Wifi
URL:            https://wireless.wiki.kernel.org/en/developers/regulatory/wireless-regdb
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch

%description
The 802.11 regulatory domain database is used by CRDA and provides allowed
frequency ranges for 802.11 wireless drivers.

%prep
%setup -q

%build

%install
%make_install FIRMWARE_PATH="%{_firmwaredir}"

%files
%license LICENSE
%doc README
%{_firmwaredir}/regulatory.db
%{_firmwaredir}/regulatory.db.p7s
%dir %{_prefix}/lib/crda
%{_prefix}/lib/crda/regulatory.bin
%dir %{_prefix}/lib/crda/pubkeys
%{_prefix}/lib/crda/pubkeys/*pem
%{_mandir}/man5/regulatory.db.5%{?ext_man}
%{_mandir}/man5/regulatory.bin.5%{?ext_man}

%changelog
