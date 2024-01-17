#
# spec file for package utmp-cli
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


Name:           utmp-cli
Version:        1.063
Release:        0
Summary:        Command to read temperature from USB thermometer
License:        MIT
Group:          Hardware/Other
URL:            https://usbtemp.com/
Source:         https://github.com/usbtemp/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
Read temperature from usbtemp.com USB thermometer and DS9097E compatible 1-wire
adapter with one DS18B20 digital probe attached through command line interface.

%prep
%setup -q

%build
%make_build

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
cp utmp-cli $RPM_BUILD_ROOT/%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/utmp-cli

%changelog

