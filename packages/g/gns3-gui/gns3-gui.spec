#
# spec file for package gns3-gui
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


Name:           gns3-gui
Version:        2.2.52
Release:        0
Summary:        GNS3 graphical interface for the GNS3 server
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other
URL:            http://github.com/GNS3/%{name}
Source:         https://github.com/GNS3/gns3-gui/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  update-desktop-files
Requires:       python3-distro >= 1.6.0
Requires:       python3-jsonschema >= 4.17.3
Requires:       python3-psutil >= 5.9.4
Requires:       python3-qt5
Requires:       python3-sentry-sdk >= 1.17.0
Requires:       python3-truststore
Recommends:     gns3-server
Recommends:     libcap-progs
Recommends:     sudo
Recommends:     telnet
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  python3-distro >= 1.8.0
BuildRequires:  python3-jsonschema >= 4.17.3
BuildRequires:  python3-psutil >= 5.9.4
BuildRequires:  python3-pytest
BuildRequires:  python3-qt5
BuildRequires:  python3-sentry-sdk >= 1.17.0
BuildRequires:  xvfb-run
# /SECTION

%description
GNS3 is an excellent complementary tool to real labs for network engineers,
administrators and people wanting to study for certifications such as Cisco
CCNA, CCNP, CCIP and CCIE as well as Juniper JNCIA, JNCIS and JNCIE.

It can also be used to experiment features of Cisco IOS, Juniper JunOS or to
check configurations that need to be deployed later on real routers.

Thanks to VirtualBox integration, now even system engineers and administrators
can take advantage of GNS3 to study Redhat (RHCE, RHCT), Microsoft (MSCE,
MSCA), Novell (CLP) and many other vendor certifications.

%prep
%autosetup -p1
find . -type f -name "*\.py" -exec sed -i 's/^#!\/usr\/bin\/env python3/#!\/usr\/bin\/python3/' {} \;
find . -type f -name "*\.py" -exec sed -i 's/^#!\/usr\/bin\/env python/#!\/usr\/bin\/python3/' {} \;

# Relax strict requirements
sed -i -r 's/==/>=/g' requirements.txt
sed -i -r '/jsonschema/ s/,<.*$//' requirements.txt
sed -i -r '/sentry-sdk/ s/,<.*$//' requirements.txt
sed -i -r '/setuptools/d' requirements.txt
# It's required but missing
echo qt5 >> requirements.txt
# Disable update alerts
sed -i 's/"check_for_update": True,/"check_for_update": False,/' gns3/settings.py
# Disable anonymous data collection
sed -i 's/"send_stats": True,/"send_stats": False,/' gns3/settings.py

%build
%python3_pyproject_wheel

%install
%python3_pyproject_install

rm %{buildroot}/%{python3_sitelib}/gns3/static/.keep
#
find %{buildroot}/%{python3_sitelib}/gns3 -name "*.ui" -exec chmod -x {} \;
find %{buildroot}/%{python3_sitelib}/gns3  -type f -name "*\.py" -exec grep -Hl python3 {} \; | xargs chmod +x
find %{buildroot}/%{python3_sitelib}/gns3  -name "*.svg" -exec chmod -x {} \;
#
install -D -m0644 %{name}.appdata.xml %{buildroot}/%{_datadir}/appdata/gns3.appdata.xml
%suse_update_desktop_file gns3 System Emulator
%fdupes %{buildroot}%{python3_sitelib}
%fdupes %{buildroot}%{_datadir}/icons

%check
rm tests/test_main_window.py
xvfb-run python3 -m pytest -rs

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/gns3
%{python3_sitelib}/gns3
%{python3_sitelib}/gns3_gui-%{version}.dist-info
%{_datadir}/icons/hicolor/*
%{_datadir}/applications/gns3.desktop
%{_datadir}/mime/packages/gns3-gui.xml
%{_datadir}/appdata/gns3.appdata.xml

%changelog
