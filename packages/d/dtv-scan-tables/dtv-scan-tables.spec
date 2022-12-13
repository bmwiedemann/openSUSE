#
# spec file for package dtv-scan-tables
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


Name:           dtv-scan-tables
Version:        20221125
Release:        0
Summary:        Scan files for digital TV applications v3
License:        GPL-2.0-or-later AND LGPL-2.1-only
Group:          Hardware/TV
URL:            https://linuxtv.org/
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  dvb-utils
BuildRequires:  fdupes
BuildArch:      noarch

%description
Scan data needed for some scanning applications from dvb package and maybe
others. This package contains v3 of the files.

%package v5
Summary:        Scan files for digital TV applications v5
Group:          Hardware/TV

%description v5
Scan data needed for some scanning applications from dvb package and maybe
others. This package contains v5 of the files.

%prep
%setup -q

%build
%make_build dvbv3 dvbv5

%install
%make_install DVBV3DIR=dvb DATADIR=%{buildroot}/%{_datadir} install_v3

%fdupes -s %{buildroot}/%{_datadir}/dvb/
%fdupes -s %{buildroot}/%{_datadir}/dvbv5/

%files
%license COPYING COPYING.LGPL
%{_datadir}/dvb

%files v5
%license COPYING COPYING.LGPL
%{_datadir}/dvbv5

%changelog
