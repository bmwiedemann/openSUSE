#
# spec file for package setconf
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


Name:           setconf
Version:        0.7.7
Release:        0
Summary:        Utility to easily change settings in configuration files
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://setconf.roboticoverlords.org
Source:         https://setconf.roboticoverlords.org/%{name}-%{version}.tar.xz
BuildArch:      noarch

%description
setconf is a small utility that can be used for changing settings in
configuration textfiles.

%prep
%autosetup
gzip -d %{name}.1.gz

%build
# Nothing to build.

%install
# fix E: env-script-interpreter
sed -i 's|/usr/bin/env python|/usr/bin/python3|g' %{name}.py

install -Dpm 0755 %{name}.py %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.?%{?ext_man}

%changelog
