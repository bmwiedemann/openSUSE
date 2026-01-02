#
# spec file for package systemd-presets-branding-Aeon
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


%define generic_name systemd-presets-branding

Name:           systemd-presets-branding-Aeon
Version:        20231005
Release:        0
Summary:        Systemd default presets for openSUSE Aeon
License:        MIT
Group:          System/Base
Source0:        50-default-Aeon.preset
Source1:        50-default-Aeon-user.preset
BuildRequires:  systemd-presets-branding-openSUSE
BuildRequires:  systemd-presets-common-SUSE-devel
BuildRequires:  pkgconfig(systemd)
#!BuildIgnore:  systemd-presets-branding
Requires(pre):  coreutils
# systemd-presets-common-SUSE provides
Supplements:    (systemd and branding-MicroOS)
Conflicts:      systemd-presets-branding
Provides:       systemd-presets-branding = %{version}
Obsoletes:      systemd-presets-branding-CAASP < 15.1
Obsoletes:      systemd-presets-branding-MicroOS < 20231005
BuildArch:      noarch
%{?systemd_preset_requires}

%description
Default presets for systemd on openSUSE Aeon

%prep
%setup -q -T -c

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-preset
mkdir -p %{buildroot}%{_prefix}/lib/systemd/user-preset

install -m644 %{SOURCE0}  %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -m644 %{SOURCE1}  %{buildroot}%{_prefix}/lib/systemd/user-preset/
# Copy default presets and script
install -m644 %{_prefix}/lib/systemd/system-preset/90-default-openSUSE.preset %{buildroot}%{_prefix}/lib/systemd/system-preset/

%pre
%systemd_preset_pre
%systemd_user_preset_pre

%post
%systemd_preset_post
%systemd_user_preset_post

%posttrans
%systemd_preset_posttrans
%systemd_user_preset_posttrans

%files
%defattr(-,root,root)
%{_prefix}/lib/systemd/system-preset/*
%{_prefix}/lib/systemd/user-preset/50-default-Aeon-user.preset

%changelog
