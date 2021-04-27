#
# spec file for package deepin-feature-enable
#
# Copyright (c) 2021 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           deepin-feature-enable
Version:        1.0
Release:        0
Summary:        Deepin Features installer
License:        WTFPL
Group:          System/GUI/Other
Url:            https://github.com/linuxdeepin
Source0:        %{name}.in
Requires:       deepin-api-dbus
Requires:       deepin-api-polkit
Requires:       deepin-daemon-dbus
Requires:       deepin-daemon-polkit
Recommends:     deepin-file-manager-dbus
Recommends:     deepin-file-manager-polkit

%description
The tool will help your to enable all feature of deepin-api and deepin-daemon.
For Ensuring you openSUSE is in security, We remove all the dbus and policykit
features on deepin-api and deepin-daemon. 

If user dose not care about security issues, he can click "I agree" to install
this package. Or click "I disagree" to exit installation.

%prep

%build

%install
%suse_install_update_script %{SOURCE0}
install -d %{buildroot}%{_localstatedir}/adm/update-messages
touch %{buildroot}%{_localstatedir}/adm/update-messages/%{name}-%{version}-%{release}

%files
%defattr(-,root,root)
%{_localstatedir}/adm/update-scripts/*
%{_localstatedir}/adm/update-messages/*

%changelog

