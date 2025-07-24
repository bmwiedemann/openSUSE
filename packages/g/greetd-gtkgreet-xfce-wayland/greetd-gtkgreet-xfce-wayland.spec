#
# spec file for package openSUSE-repos
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
Name:           greetd-gtkgreet-xfce-wayland
Version:        1.0
Release:        1%{?dist}
Summary:        Greetd config using gtkgreet and XFCE Wayland session
License:        MIT
Group:          System/X11/Displaymanagers
Source0:        config.toml
Source1:        environments
BuildRequires:  greetd
Requires:       cage
Requires:       greetd
Requires:       gtkgreet
# We need to provide our own /etc/greetd/config.toml
Conflicts:      greetd-branding-upstream
# openSUSE way has also it's own entry in greetd/config
# but doens't provide greetd-branding
Conflicts:      openSUSEway 
Provides:       greetd-branding = %{version}
BuildArch:      noarch

%description
This package configures greetd to use gtkgreet in the Cage Wayland compositor,
and provides a session environment that launches XFCE in Wayland mode.

%prep

%build

%install
# Create config directory
mkdir -p %{buildroot}%{_sysconfdir}/greetd

install -D -m 0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/greetd/config.toml
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/greetd/environments

%files
%config(noreplace) %{_sysconfdir}/greetd/environments
%config(noreplace) %{_sysconfdir}/greetd/config.toml

%changelog
