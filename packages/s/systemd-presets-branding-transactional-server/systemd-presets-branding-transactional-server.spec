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
Source0:        50-transactional-server.preset
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-presets-common-SUSE
PreReq:         coreutils
# systemd-presets-common-SUSE provides
Requires(pre):  systemd-presets-common-SUSE
Requires(pre):  bash
Requires(post): bash
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Service presets for systemd for Transactional Server System Role.

%prep
%setup -q -T -c

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/%{generic_name}
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-preset
install -m644 %{SOURCE0}  %{buildroot}%{_prefix}/lib/systemd/system-preset/

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
fi

%posttrans
if [ -f /run/rpm-%{name}-preset-all ]; then
  # Enable all services, which were installed before systemd
  # Don't disable services, since this would disable the
  # complete network stack.
  systemctl preset-all --preset-mode=enable-only
fi
rm -f /run/rpm-%{name}-preset-all

%files
%defattr(-,root,root)
%{_prefix}/lib/%{generic_name}/
%{_prefix}/lib/systemd/system-preset/*

%changelog
