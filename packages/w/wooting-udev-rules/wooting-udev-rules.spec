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


Name:           wooting-udev-rules
Version:        0.0.4
Release:        0
Summary:        Udev rules to use Wooting from normal users
License:        MIT
URL:            https://wooting.io
#
# based on https://github.com/KyleGospo/wooting-udev-rules
# plus the generic rule from
# https://help.wooting.io/article/147-configuring-device-access-for-wootility-under-linux-udev-rules
#
Source1:        70-wooting.rules
#
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(systemd)
BuildArch:      noarch
#
%description
udev rules to use Wooting tools from normal users.

%prep

%build

%install
install -D -m 0644 -t %{buildroot}%{_udevrulesdir} ${RPM_SOURCE_DIR}/70-wooting.rules

%files
%{_udevrulesdir}/70-wooting.rules

%changelog
