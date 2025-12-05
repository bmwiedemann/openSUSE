#
# spec file for package sway-xkb-layout-generator
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           sway-xkb-layout-generator
Version:        0.0.1+git20251204.58fbdcb
Release:        0
Summary:        A xkb layout generator script for Sway based on localectl
License:        MIT
URL:            https://github.com/FilippoBonazziSUSE/sway-xkb-layout-generator
BuildArch:      noarch
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.rpmlintrc
# For /etc/vconsole.conf
Requires:       udev
Requires:       grep
# For localectl
Requires:       systemd

%description
Generate a Sway keyboard configuration block with the xkb_* options
corresponding to the XKB* variables found in /etc/vconsole.conf.

%prep
%autosetup

%build

%install
install -D -p -m 755 -t %{buildroot}%{_libexecdir} %{name}

%files
%license LICENSE
%doc README.md
%{_libexecdir}/sway-xkb-layout-generator

%changelog
