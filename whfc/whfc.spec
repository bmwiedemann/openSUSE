#
# spec file for package whfc
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           whfc
BuildRequires:  unzip
Version:        1.2.3
Release:        0
Url:            http://www.uli-eckhardt.de/whfc/
Summary:        A client for the network fax server HylaFAX 4.x under Microsoft Windows(r)
License:        GPL-2.0+
Group:          Hardware/Fax
Source:         http://www.uli-eckhardt.de/whfc/download/%{name}-%{version}_src.zip
Source1:        http://www.uli-eckhardt.de/whfc/download/%{name}-%{version}_setup.exe
Source20:       http://www.uli-eckhardt.de/whfc/copy.shtml
Source21:       http://www.uli-eckhardt.de/whfc/download/whfc-docu-1.2.1.zip
Source30:       README.SUSE
Source31:       systemsettings.png
Source32:       usersettings.png
Source40:       install_de.html
Source41:       install_en.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
WHFC is a client for the network fax server HylaFAX 4.x under Microsoft
Windows(r) 95/98 and NT/2000.

Authors:
--------
    Ulrich Eckhardt <whfc at gmx de>

%prep

%build
install -m 0644 -p %{SOURCE20} %{SOURCE21} %{SOURCE30} %{SOURCE31} %{SOURCE32} %{SOURCE40} %{SOURCE41} ${RPM_BUILD_DIR}
unzip -d docu whfc-docu-1.2.1.zip

%install
mkdir -p \
	${RPM_BUILD_ROOT}/%{_datadir}/%{name}
install -m 0644 -p %{SOURCE1} ${RPM_BUILD_ROOT}/%{_datadir}/whfc
find docu -type f -print0 | xargs -0 chmod a-x

%files
%defattr(-,root,root)
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/whfc-1.2.3_setup.exe
%doc README.SUSE copy.shtml docu install_*.html systemsettings.png usersettings.png

%changelog
