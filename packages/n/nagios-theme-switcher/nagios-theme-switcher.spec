#
# spec file for package nagios-theme-switcher
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2014 by Lars Vogdt
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


Name:           nagios-theme-switcher
Version:        1.4
Release:        0
Summary:        Simple Theme Switcher for Nagios Webfrontend
License:        BSD-3-Clause
Group:          System/Monitoring
Url:            http://en.opensuse.org/nagios-theme-switcher
Source0:        switch-nagios-theme
Source1:        switch-nagios-theme.8
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%define         theme_dir /usr/share/nagios-themes

%description
This package contains a simple script with configures Nagios to use
a theme below /usr/share/nagios.

%prep
#

%build
#

%install
mkdir -p %{buildroot}/%{_sbindir}
mkdir -p %{buildroot}/%{theme_dir}
install -d -m0700 %{buildroot}/%{theme_dir}/backups
install -m755 %{SOURCE0} %{buildroot}/%{_sbindir}/switch-nagios-theme
install -Dm644 %{SOURCE1} %{buildroot}/%{_mandir}/man8/switch-nagios-theme.8

%files
%defattr(-, root, root)
%{_sbindir}/switch-nagios-theme
%dir %{theme_dir}
%dir %{theme_dir}/backups
%{_mandir}/man8/switch-nagios-theme.8*

%changelog
