#
# spec file for package setconf
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           setconf
Version:        0.7.5
Release:        0
Summary:        Utility to easily change settings in configuration files
License:        GPL-2.0+
Group:          Development/Tools/Building
Url:            http://setconf.roboticoverlords.org/
Source:         http://setconf.roboticoverlords.org/%{name}-%{version}.tar.xz
# UPSTREAM: https://github.com/xyproto/setconf/pull/10
Patch0:         copying-fsf.patch
Requires:       python
BuildArch:      noarch

%description
setconf is a small utility that can be used for changing settings in
configuration textfiles.

%prep
%setup -q
%patch0 -p1
gzip -d %{name}.1.gz

%build
# Nothing to build.

%install
install -Dpm 0755 %{name}.py %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc COPYING
%{_bindir}/%{name}
%{_mandir}/man?/%{name}.?%{?ext_man}

%changelog
