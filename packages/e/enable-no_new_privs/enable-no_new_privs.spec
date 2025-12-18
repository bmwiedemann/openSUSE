#
# spec file for package enable-no_new_privs
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

Name:           enable-no_new_privs
Version:        1.0
Release:        0
Summary:        System configuration to enforce NoNewPrivs by default
License:        BSD-2-Clause
Source1:        LICENSE
Source2:        README
Source3:        10-enable-NoNewPrivs.conf
# Rebuild initrd since the systemd.conf changes end there
BuildRequires:  suse-module-tools
BuildRequires:  systemd-presets-common-SUSE-devel
Requires:       account-utils >= 1.0
Requires:       polkit >= 126-4.1
Requires:       run0-wrappers >= 0.4
Requires:       shadow >= 4.18.0-2.1
Requires(post): account-utils
Obsoletes:      disable-setuid
Conflicts:      cron
Conflicts:      cronie
BuildArch:      noarch

%description
This package provides the configuration files and dependencies
necessary to enforce the no_new_privs kernel flag system-wide.
When enabled, this flag prevents processes from granting privileges
that were not already held by their parent. Consequently, setuid and
setgid binaries will no longer function to elevate permissions.

%prep

%build
cp %{SOURCE1} .
cp %{SOURCE2} .

%install
# no-setuid config for systemd
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system.conf.d
install -m 644 %{SOURCE3} %{buildroot}%{_prefix}/lib/systemd/system.conf.d/

%post
%{?regenerate_initrd_post}

%postun
%{?regenerate_initrd_post}

%posttrans
%{systemd_preset_posttrans}
%{?regenerate_initrd_posttrans}

%files
%license LICENSE
%doc README
%dir %{_prefix}/lib/systemd/system.conf.d
%{_prefix}/lib/systemd/system.conf.d/10-enable-NoNewPrivs.conf

%changelog
