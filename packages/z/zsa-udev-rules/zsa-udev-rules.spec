#
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


Name:           zsa-udev-rules
Version:        2.1.3+git13.623a50d
Release:        0
Summary:        udev rules to use ZSA tools from normal users
License:        MIT 
URL:            https://github.com/zsa/wally 
Source0:        https://raw.githubusercontent.com/zsa/wally/master/dist/linux64/50-oryx-legacy.rules 
Source1:        https://raw.githubusercontent.com/zsa/wally/master/dist/linux64/50-oryx.rules
Source2:        https://raw.githubusercontent.com/zsa/wally/master/dist/linux64/50-wally.rules
Source3:        https://raw.githubusercontent.com/zsa/wally/master/license.md
#
Provides:       ergodox-wally-udev-rules = %{version}-%{release}
Obsoletes:      ergodox-wally-udev-rules <= %{version}-%{release}
#
BuildRequires:  pkgconfig(udev)
BuildArch:      noarch
#
%description
udev rules to use ZSA tools from normal users.

%prep
cp %{SOURCE3} LICENSE

%build

%install
install -D -m 0644 -t %{buildroot}%{_udevrulesdir} ${RPM_SOURCE_DIR}/*.rules

%files
%license LICENSE
%{_udevrulesdir}/50-wally.rules
%{_udevrulesdir}/50-oryx.rules
%{_udevrulesdir}/50-oryx-legacy.rules

%changelog
