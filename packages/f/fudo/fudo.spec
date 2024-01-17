#
# spec file for package fudo
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


Name:           fudo
Version:        0
Release:        0
Summary:        Fake sudo
License:        MIT
Source:         30-fudo-machinectl-shell.rules
Source1:        fudo.sh
Source2:        50-machinectl-shell-run-env.rules
BuildRequires:  polkit
Requires:       polkit
Requires:       systemd-container

%description
Fake sudo leveraging machinctl shell and polkit to be able to
execute commands as root

- just a few lines of shell and js
- no setuid program
- no hard to understand config file

%package policy-noauth-wheel
Summary:        fudo policy no authentication for wheel group
Requires:       group(wheel)
Conflicts:      fudo-policy
Provides:       fudo-policy

%description policy-noauth-wheel
Members of the wheel group do not need to authenticate when using
fudo

%package policy-selfauth-wheel
Summary:        fudo policy wheel group members use own password
Requires:       group(wheel)
Conflicts:      fudo-policy
Provides:       fudo-policy

%description policy-selfauth-wheel
Members of the wheel group use their own password to authenticate
as root

%prep
%setup -q -c -T

%build

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_datadir}/polkit-1/rules.d/30-fudo-machinectl-shell.rules
install -D -m 644 %{SOURCE1} %{buildroot}%{_prefix}%{_sysconfdir}/profile.d/fudo.sh
install -D -m 644 %{SOURCE2} %{buildroot}%{_docdir}/50-machinectl-shell-run-env.rules
echo 'polkit._fudo_noauth_group = "wheel";' > %{buildroot}%{_datadir}/polkit-1/rules.d/31-fudo-machinectl-shell-noauth-wheel.rules
echo 'polkit._fudo_selfauth_group = "wheel";' > %{buildroot}%{_datadir}/polkit-1/rules.d/31-fudo-machinectl-shell-selfauth-wheel.rules

%files
%{_docdir}/50-machinectl-shell-run-env.rules
%{_datadir}/polkit-1/rules.d/30-fudo-machinectl-shell.rules
%{_prefix}%{_sysconfdir}/profile.d/fudo.sh

%files policy-noauth-wheel
%{_datadir}/polkit-1/rules.d/31-fudo-machinectl-shell-noauth-wheel.rules

%files policy-selfauth-wheel
%{_datadir}/polkit-1/rules.d/31-fudo-machinectl-shell-selfauth-wheel.rules

%changelog
