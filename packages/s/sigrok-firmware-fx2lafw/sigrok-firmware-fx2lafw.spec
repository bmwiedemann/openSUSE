#
# spec file for package sigrok-firmware-fx2lafw
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


Summary:        Firmware for Logic Analyzers based on the Cypress EZ-USB FX2(LP) Chip
License:        GPL-2.0+
Group:          Hardware/Other

Name:           sigrok-firmware-fx2lafw
Version:        0.1.6
Release:        0
BuildArch:      noarch
Url:            http://sigrok.org
Source0:        http://sigrok.org/download/source/sigrok-firmware-fx2lafw/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  sdcc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
fx2lafw is a free/libre/open-source firmware for logic analyzers based on
the Cypress EZ-USB FX2(LP) chip.

%prep
%setup -q

%build
%configure
make

%install
%make_install

%files
%defattr(-,root,root,-)
%doc NEWS README COPYING COPYING.LESSER
%_datadir/sigrok-firmware

%changelog
