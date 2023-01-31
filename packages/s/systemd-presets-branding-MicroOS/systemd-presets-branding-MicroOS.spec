#
# spec file for package systemd-presets-branding-MicroOS
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


%define generic_name systemd-presets-branding

Name:           systemd-presets-branding-MicroOS
Version:        20230130
Release:        0
Summary:        Systemd default presets for openSUSE MicroOS
License:        MIT
Group:          System/Base
Source0:        50-default-MicroOS.preset
Source1:        50-default-MicroOS-user.preset
BuildRequires:  systemd-presets-branding-openSUSE
BuildRequires:  pkgconfig(systemd)
#!BuildIgnore:  systemd-presets-branding
Requires:       systemd-presets-common-SUSE
PreReq:         coreutils
# systemd-presets-common-SUSE provides
Requires(pre):  systemd-presets-common-SUSE
Supplements:    packageand(systemd:branding-MicroOS)
Conflicts:      systemd-presets-branding
Provides:       systemd-presets-branding = %{version}
Obsoletes:      systemd-presets-branding-CAASP < 15.1
BuildArch:      noarch

%description
Default presets for systemd on openSUSE MicroOS

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
# On initial installation, branding-preset-states does not yet exist,
# which is why we also check for the file to be present/executable
if [ $1 -gt 1 -a -x %{_prefix}/lib/%{generic_name}/branding-preset-states ] ; then
        #
        # Save the old state so we can detect which package have its
        # default changed later.
        #
        # Note: the old version of the script is used here.
        #
        %{_prefix}/lib/%{generic_name}/branding-preset-states save
        %{_prefix}/lib/%{generic_name}/branding-preset-states save user
elif [ $1 -eq 1 ]; then
  touch /run/rpm-%{name}-preset-all
fi

%post
if [ $1 -gt 1 ] ; then
        #
        # Now that the updated presets are installed, find the ones
        # that have been changed and apply "systemct preset" on them.
        #
        %{_prefix}/lib/%{generic_name}/branding-preset-states apply-changes
        %{_prefix}/lib/%{generic_name}/branding-preset-states apply-changes user
fi

%posttrans
if [ -f /run/rpm-%{name}-preset-all ]; then
  # Enable all services, which were installed before systemd
  # Don't disable services, since this would disable the
  # complete network stack.
  systemctl preset-all --preset-mode=enable-only
  systemctl preset-all --preset-mode=enable-only --global
fi
rm -f /run/rpm-%{name}-preset-all

%files
%defattr(-,root,root)
%{_prefix}/lib/systemd/system-preset/*
%{_prefix}/lib/systemd/user-preset/50-default-MicroOS-user.preset

%changelog
