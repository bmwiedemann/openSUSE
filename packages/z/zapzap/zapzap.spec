#
# spec file for package zapzap
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


Name:           zapzap
Version:        5.3.1
Release:        0
Summary:        Whatsapp Desktop for Linux
License:        GPL-3.0-only+
URL:            https://github.com/zapzap-linux/zapzap
Source0:        https://github.com/zapzap-linux/zapzap/archive/refs/tags/%{version}.tar.gz
BuildRequires:  %{python_module PyQt6}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
Requires:       python3-PyQt6-WebEngine
Requires:       python3-PyQt6-sip
Requires:       python3-dbus-python
BuildArch:      noarch

%description
WhatsApp desktop application for Linux.

%prep
%autosetup -n %{name}-%{version}
sed -i "s|!/usr/bin/env python|!%{_bindir}/python3|" zapzap/services/dbus_notify.py

%build
%py3_build

%install
%py3_install
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/
cp -R share/applications/com.rtosta.zapzap.desktop %{buildroot}%{_datadir}/applications/com.rtosta.zapzap.desktop
cp -R share/icons/com.rtosta.zapzap.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/com.rtosta.zapzap.svg

%fdupes %{buildroot}%{python_sitelib}/%{name}/

chmod +x %{buildroot}/%{python_sitelib}/%{name}/services/dbus_notify.py

%check

%files
%license LICENSE
%doc README.md
%{python_sitelib}/%{name}-*.egg-info
%{python_sitelib}/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/com.rtosta.zapzap.desktop
%{_datadir}/icons/hicolor/scalable/apps/com.rtosta.zapzap.svg

%changelog
