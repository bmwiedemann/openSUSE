#
# spec file for package systemd-presets-branding-openSUSE
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


%define generic_name systemd-presets-branding

Name:           %{generic_name}-openSUSE
Version:        12.2
Release:        0
Summary:        Systemd default presets for openSUSE
License:        GPL-2.0-or-later
Group:          System/Base
Source1:        default-openSUSE.preset
# FIXME: why systemd is required ?
BuildRequires:  pkgconfig(systemd)
#!BuildIgnore:  systemd-presets-branding
Requires(pre):  coreutils
BuildRequires:  systemd-presets-common-SUSE-devel
Provides:       %{generic_name} = %{version}
Supplements:    (systemd and branding-openSUSE)
Conflicts:      %{generic_name}
BuildArch:      noarch
Requires(pre):  bash
Requires(post): bash
%{?systemd_preset_requires}

%description
Default presets for systemd on openSUSE distribution.

These are the openSUSE specific presets. The default
presets needed for all SUSE based distributions can be
found in systemd-presets-common-SUSE.

%prep
%autosetup -T -c

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/%{generic_name}
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-preset
# everything that must be enabled to have a working system.
# everything that must be enabled only in openSUSE
install -m644 %{SOURCE1}  %{buildroot}%{_prefix}/lib/systemd/system-preset/90-default-openSUSE.preset

%pre
%systemd_preset_pre

%post
%systemd_preset_post

%posttrans
%systemd_preset_posttrans

%files
%defattr(-,root,root)
%{_prefix}/lib/%{generic_name}/
%{_prefix}/lib/systemd/system-preset/*

%changelog
