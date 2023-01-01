#
# spec file for package xorg-x11-driver-input
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


Name:           xorg-x11-driver-input
Version:        7.6_1
Release:        0
Summary:        Compatibility metapackage for X.Org input drivers
License:        MIT
Group:          System/X11/Servers/XF86_4
URL:            https://xorg.freedesktop.org/
Source0:        README.meta
## Requires of packages that we split away from xorg-x11-driver-input
Requires:       xf86-input-evdev
## no longer supported on sle12 (FATE#316785)
Recommends:     xf86-input-joystick
Recommends:     xf86-input-mouse
## Most drivers can replaced by xf86-input-libinput today. Only keep
## the ones with lower priority or very specific device matching rules.
%if 0%{?suse_version} >= 1330 || (0%{?is_opensuse} && 0%{?sle_version} >= 120200)
Requires:       xf86-input-libinput
%else
Requires:       xf86-input-synaptics
%endif
## only built on x86/x64
Recommends:     xf86-input-vmmouse
Requires:       xf86-input-void
Requires:       xf86-input-wacom
## End Requires of packages that we split away from xorg-x11-driver-input
Provides:       %{name}-devel = %{version}
Obsoletes:      %{name}-devel < %{version}
BuildArch:      noarch
ExcludeArch:    s390 s390x

%description
This package is a compatibility metapackage. It used to contain the
X.Org input drivers.

%prep
%setup -c -T
cp %{SOURCE0} .

%build

%install

%files
%doc README.meta

%changelog
