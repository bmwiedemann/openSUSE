#
# spec file for package android-udev-rules
#
# Copyright (c) 2023 SUSE LLC
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


Name:           android-udev-rules
Version:        20230104
Release:        0
Summary:        Android udev rules list aimed to be the most comprehensive on the net
License:        GPL-3.0-or-later
Group:          Hardware/Mobile
URL:            https://github.com/M0Rf30/android-udev-rules
Source0:        https://github.com/M0Rf30/android-udev-rules/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  sysuser-shadow
BuildRequires:  sysuser-tools
Recommends:     android-tools
Provides:       android-tools-udev = %{version}
Obsoletes:      android-tools-udev < %{version}
BuildArch:      noarch
%sysusers_requires

%description
These rules refer to 'Run Apps on a Hardware Device - Android Studio'
and include many suggestions from the Archlinux and Github Communities.

%prep
%autosetup -p1

%build
%sysusers_generate_pre android-udev.conf adbusers android-udev.conf

%install
install -D -m 0644 -t %{buildroot}%{_sysusersdir} android-udev.conf
install -D -m 0644 -t %{buildroot}%{_udevrulesdir} 51-android.rules

%pre -f adbusers.pre

%post
%udev_rules_update

%postun
%udev_rules_update

%files
%license LICENSE
%doc README.md
%{_sysusersdir}/android-udev.conf
%{_udevrulesdir}/51-android.rules

%changelog
