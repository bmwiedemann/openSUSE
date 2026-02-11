#
# spec file for package systemd-presets-branding-transactional-server
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define generic_name systemd-presets-branding

Name:           systemd-presets-branding-transactional-server
Version:        15.0
Release:        0
Summary:        Systemd presets for Transactional Server System Role
License:        MIT
Group:          System/Base
Source0:        transactional-server.preset
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-presets-common-SUSE-devel
Requires(pre):  coreutils
Requires(pre):  bash
Requires(post): bash
BuildArch:      noarch
%{?systemd_preset_requires}

%description
Service presets for systemd for Transactional Server System Role.

%prep
%autosetup -T -c

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/%{generic_name}
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-preset
install -Dm0644 %{SOURCE0}  %{buildroot}%{_prefix}/lib/systemd/system-preset/87-transactional-server.preset

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
