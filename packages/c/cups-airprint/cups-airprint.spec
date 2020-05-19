#
# spec file for package cups-airprint
#
# Copyright (c) 2020 SUSE LLC
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


Name:           cups-airprint
Version:        1.1
Release:        0
Summary:        AirPrint for CUPS printers
License:        MIT
Group:          Hardware/Printing
URL:            https://github.com/tjfontaine/airprint-generate
Source0:        https://raw.githubusercontent.com/tjfontaine/airprint-generate/master/airprint-generate.py
Source10:       apple.types
Source11:       local.convs
Source20:       airprint-generate.py.8
Source21:       CREDITS.txt
Source22:       README.SUSE
Source23:       LICENSE.txt
Patch0:         airprint-generate.patch
Patch1:         python3.patch
Patch2:         pdf-support.patch
BuildRequires:  python3-pycups
Requires:       avahi
# cups-airprint will not work reasonably well with traditional CUPS <= 1.5.4
# that has neither built-in DNS-SD/Avahi support nor the urftopdf filter
# so that in practice a modern CUPS >= 1.6 is required:
Requires:       cups >= 1.6
# cups-filters >= 1.0.25 provides the urftopdf filter to convert the URF format
# which (at least some) iOS apps send when printing via AirPrint:
Requires:       cups-filters >= 1.0.25
Requires:       python3-pycups
Requires:       python3-xml
BuildArch:      noarch

%description
Tools for setting up AirPrint for CUPS printers on openSUSE.

AirPrint is an Apple technology that helps you create full-quality printed
output from iOS or OS X devices without the need to download or install
drivers.

Some printers support AirPrint natively; for those you don't need CUPS
AirPrint support. For any other printer, if it can be printed to via CUPS
on openSUSE, this package provides the additional tools and configuration
files needed to add CUPS AirPrint support for basic printing tasks from
iOS or OS X devices. For limitations see the "caveats" section in:
  %{_docdir}/%{name}/README.SUSE

Some post-install configuration changes have to be performed manually to make
AirPrint work; please follow the instructions in:
  %{_docdir}/%{name}/README.SUSE

%prep
%setup -q -c -T
cp %{SOURCE0} %{SOURCE10} %{SOURCE11} .
cp %{SOURCE21} %{SOURCE22} %{SOURCE23} .
%patch0
%patch1 -p1
%patch2 -p1

%build

%install
mkdir -p %{buildroot}%{_sbindir}
install airprint-generate.py %{buildroot}%{_sbindir}

mkdir -p %{buildroot}%{_datadir}/cups/mime
install -m 644 apple.types local.convs %{buildroot}%{_datadir}/cups/mime

mkdir -p %{buildroot}%{_mandir}/man8
install -m 644 %{SOURCE20} %{buildroot}/%{_mandir}/man8

%check
python3 airprint-generate.py -h

%files
%{_sbindir}/airprint-generate.py
%dir %{_datadir}/cups/
%dir %{_datadir}/cups/mime
%{_datadir}/cups/mime/apple.types
%{_datadir}/cups/mime/local.convs
%license LICENSE.txt
%doc CREDITS.txt README.SUSE
%{_mandir}/man8/airprint-generate.py.8%{?ext_man}

%changelog
