#
# spec file for package systemd-presets-common-SUSE
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


Name:           systemd-presets-common-SUSE
Version:        15
Release:        0
Summary:        Systemd default presets for SUSE distributions
License:        GPL-2.0-or-later
Group:          System/Base
Source0:        default-SUSE.preset
Source2:        99-default-disable.preset
Source3:        branding-preset-states
Source4:        default-SUSE-user.preset
Source5:        macros.systemd-preset
BuildRequires:  pkgconfig(systemd)
#!BuildIgnore:  systemd-presets-branding
PreReq:         coreutils
Supplements:    systemd
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

Requires(pre):  bash
Requires(post): bash

%{load:%{SOURCE5}}
%define generic_name %{__preset_generic_name}

%description
Default presets for systemd on SUSE based distributions.

%package devel
Summary:        Devel package for systemd presets
Group:          System/Base
Requires:       systemd-presets-common-SUSE

%description devel
This package provides the needed files to build preset
packages

%prep
%setup -q -T -c

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/%{generic_name}
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-preset
mkdir -p %{buildroot}%{_prefix}/lib/systemd/user-preset
# everything that must be enabled to have a working system.
# shared across all brands
install -m644 %{SOURCE0}  %{buildroot}%{_prefix}/lib/systemd/system-preset/95-default-SUSE.preset
install -m644 %{SOURCE2}  %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -m755 %{SOURCE3}  %{buildroot}%{_prefix}/lib/%{generic_name}/
install -m644 %{SOURCE4}  %{buildroot}%{_prefix}/lib/systemd/user-preset/95-default-SUSE.preset

install -Dm0644 %{SOURCE5} %{buildroot}%{_rpmmacrodir}/macros.systemd-preset

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
%{_prefix}/lib/%{generic_name}/
%{_prefix}/lib/systemd/system-preset/*
%{_prefix}/lib/systemd/user-preset/*

%files devel
%{_rpmmacrodir}/macros.systemd-preset

%changelog
