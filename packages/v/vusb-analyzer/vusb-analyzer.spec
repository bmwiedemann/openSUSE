#
# spec file for package vusb-analyzer
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


Name:           vusb-analyzer
Version:        1.1
Release:        0
Summary:        A tool for viewing USB trace files from usbmon and other usb dump formats
License:        MIT
Group:          Development/Tools/Other
Url:            http://vusb-analyzer.sourceforge.net
Source:         http://downloads.sourceforge.net/vusb-analyzer/%{name}-%{version}.tar.gz
BuildRequires:  python-gtk
Requires:       python-gnomecanvas
Requires:       python-gtk
BuildArch:      noarch

%description
The Virtual USB Analyzer is a free and open source tool for visualizing
logs of USB packets, from hardware or software USB sniffer tools.  The
Virtual USB Analyzer is not itself a USB sniffer tool. It is just a user
interface for visualizing logs.

%prep
%setup -q

%build
sed -i "s|/usr/bin/env python|/usr/bin/python2|g" %{name}

%install
install -Dpm 0755 %{name} \
   %{buildroot}/%{_bindir}/%{name}
install -d %{buildroot}/%{python_sitelib}
cp -a VUsbTools %{buildroot}/%{python_sitelib}

%files
%{_bindir}/vusb-analyzer
%{python_sitelib}/VUsbTools

%changelog
