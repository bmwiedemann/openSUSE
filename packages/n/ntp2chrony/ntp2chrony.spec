#
# spec file for package ntp2chrony
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ntp2chrony
Version:        0.3+git20190605.f616151
Release:        0
Summary:        Utility to convert ntpd configuration files to chrony
License:        MIT
Group:          Productivity/Networking/Other
Url:            https://github.com/mlichvar/ntp2chrony
Source:         ntp2chrony-%{version}.tar.xz
Source1:        README.packaging.txt
Patch:          python3.patch
BuildArch:      noarch

%description
A script that converts the ntpd configuration file to a chrony configuration
file. Since both tools are not feature identical, not everything can
be converted. Such configuration options will be ignored.

%prep
%setup -q
%patch -p0

%build

%install
mkdir -p %{buildroot}%{_sbindir}
install -m 755 ntp2chrony/ntp2chrony.py %{buildroot}%{_sbindir}/ntp2chrony

%files
%license COPYRIGHT
%{_sbindir}/ntp2chrony

%changelog
