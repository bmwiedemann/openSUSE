#
# Copyright (c) 2024 SUSE LLC
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


Name:           pulsar-udev-rules
Version:        0.0.2+git0.c123022
Release:        0
Summary:        Udev rules to access Pulsar devices from normal user accounts
License:        MIT
URL:            https://bbb.pulsar.gg/
Source0:        %{name}-%{version}.tar.gz
#
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(systemd)
BuildArch:      noarch
#
%description
udev rules to use pulsar tools from normal users.

%prep
%autosetup

%build

%install
install -D -m 0644 -t %{buildroot}%{_udevrulesdir} 70-pulsar.rules

%files
%doc README.md
%{_udevrulesdir}/70-pulsar.rules

%changelog
