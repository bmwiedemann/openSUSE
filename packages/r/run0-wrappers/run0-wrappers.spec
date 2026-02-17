#
# spec file for package run0-wrappers
#
# Copyright (c) 2025 SUSE LLC
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

Name:           run0-wrappers
Version:        0.4+git20260203.bbbfcf8
Release:        0
Summary:        Configs and scripts to simulate some sudo and su behavior with run0
License:        BSD-2-Clause
URL:            https://github.com/thkukuk/run0-wrappers
Source:         %{name}-%{version}.tar.xz
Source1:        run0-wrappers.tmpfiles
BuildRequires:  docbook5-xsl-stylesheets
BuildRequires:  meson
Requires:       systemd >= 257
Conflicts:      pkexec
Provides:       pkexec = %{version}
Conflicts:      sudo
Conflicts:      sudo-plugin-python
Conflicts:      sudo-policy-wheel-auth-self
Provides:       sudo = %{version}

%description
This package contains polkit rules and wrapper scripts for pkexec, su
and sudo to simulate their behavior with run0.
The run0 polkit rule tries to be compatible with the
sudo-policy-auth-wheel-self RPM as far as possible. Supported are
"nopasswd" and self authentication if an user is in the wheel group.

%package -n run0-policy-wheel-auth-self
Summary:        Users in the wheel group can authenticate as admin
Requires:       %{name} = %{version}
Requires:       group(wheel)
BuildArch:      noarch

%description -n run0-policy-wheel-auth-self
run0 authentication policy that allows users in the wheel group to
authenticate as root with their own password.

%prep
%autosetup

%build
%meson --sysconfdir=%{_prefix}/etc -Dpkexec-compat=true -Dsudo-compat=true
%meson_build
sed -i -e 's|"wheel";|"";|g' polkit/50-run0-sudo.rules

%install
%meson_install
install -Dm0644 %{SOURCE1} %{buildroot}%{_tmpfilesdir}/run0-wrappers.conf
echo 'polkit._run0_admin_group = "wheel";' > %{buildroot}%{_datadir}/polkit-1/rules.d/51-run0-admin-group.rules

%files
%license LICENSE
%{_bindir}/nnpenabled
%{_bindir}/run0-pkexec
%{_bindir}/pkexec
%{_bindir}/run0-su
%{_bindir}/run0-sudo
%{_bindir}/sudo
%{_prefix}%{_sysconfdir}/profile.d/run0-wrappers.sh
%attr(0555, root, root) %dir %{_datadir}/polkit-1/rules.d
%{_datadir}/polkit-1/rules.d/50-run0-sudo.rules
%{_tmpfilesdir}/run0-wrappers.conf
%{_mandir}/man1/run0-pkexec.1%{?ext_man}
%{_mandir}/man1/pkexec.1%{?ext_man}
%{_mandir}/man1/run0-su.1%{?ext_man}
%{_mandir}/man1/run0-sudo.1%{?ext_man}
%{_mandir}/man1/sudo.1%{?ext_man}
%{_mandir}/man5/sudo.conf.5%{?ext_man}

%files -n run0-policy-wheel-auth-self
%{_datadir}/polkit-1/rules.d/51-run0-admin-group.rules

%changelog
