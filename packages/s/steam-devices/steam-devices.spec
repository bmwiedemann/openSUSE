#
# spec file for package steam-devices
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


Name:           steam-devices
Version:        20251018+git.4d7e6c1
Release:        0
Summary:        Device support for Steam-related hardware
License:        MIT
Group:          Hardware/Joystick
URL:            https://github.com/ValveSoftware/steam-devices/
Source0:        %{name}-%{version}.tar.xz
Source1:        51-these-are-not-joysticks-rm.rules
Supplements:    steam
Obsoletes:      steam-controller <= 1.0.0.78
Obsoletes:      steam-vr <= 1.0.0.78
Provides:       steam-controller = 1.0.0.78
Provides:       steam-vr = 1.0.0.78

%description
The Steam Controller features dual trackpads, HD haptic feedback, dual-stage
triggers, back grip buttons, and fully-customizable control schemes.
Make sure that all users, which should have access to the steam-controller,
are in the "games" group. Steam VR is a full-featured, 360° room-scale
virtual reality experience.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_udevrulesdir}
install -Dm0644 60-steam-input.rules %{buildroot}%{_udevrulesdir}/60-steam-input.rules
install -Dm0644 60-steam-vr.rules %{buildroot}%{_udevrulesdir}/60-steam-vr.rules
install -Dm0644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/51-these-are-not-joysticks-rm.rules

%post

%files
%license LICENSE
%{_udevrulesdir}/51-these-are-not-joysticks-rm.rules
%{_udevrulesdir}/60-steam-input.rules
%{_udevrulesdir}/60-steam-vr.rules

%changelog
