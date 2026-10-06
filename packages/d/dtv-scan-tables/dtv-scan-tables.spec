#
# spec file for package dtv-scan-tables
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        20260625
Release:        0
Summary:        Scan files for digital TV applications v3
License:        GPL-2.0-or-later AND LGPL-2.1-only
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

%description v5
Scan data needed for some scanning applications from dvb package and maybe
others. This package contains v5 of the files.

%prep
%setup -q

%build
# dvb-format-convert (v4l-utils 1.32) cannot express the DVB-S2 second
# generation inner code rates (1/4, 25/36, 77/90, ...) or the APSK/64
# modulation the scan tables now carry: it writes the entry with an empty
# field and then fails the whole build.  Such tables are left out of the
# legacy v3 output rather than shipped with blank FEC and modulation; the
# v5 tables are a plain copy of upstream and stay complete.
mkdir -p dvbv3/atsc dvbv3/dvb-c dvbv3/dvb-s dvbv3/dvb-t
for f in atsc/* dvb-c/* dvb-s/* dvb-t/*; do
	dvb-format-convert -IDVBV5 -OCHANNEL "$f" "dvbv3/$f" || rm -f "dvbv3/$f"
done
%make_build dvbv5

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
