#
# spec file for package sigrok-firmware-fx2lafw
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


Summary:        Firmware for Logic Analyzers based on the Cypress EZ-USB FX2(LP) Chip
License:        GPL-2.0-or-later
Group:          Hardware/Other
Name:           sigrok-firmware-fx2lafw
Version:        0.1.7+git20240203.0f2d324
Release:        0
URL:            https://sigrok.org

# osb service had problems creating the tarball, I used this workaround:
# git archive --format=tar.gz --prefix=sigrok-firmware-fx2lafw-0.1.7+git20240203.0f2d324
#  -o ../sigrok-firmware-fx2lafw-0.1.7+git20240203.0f2d324.tar.gz master

Source0:        https://sigrok.org/download/source/sigrok-firmware-fx2lafw/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  sdcc >= 3.4.0
BuildArch:      noarch

%description
fx2lafw is a free/libre/open-source firmware for logic analyzers based on
the Cypress EZ-USB FX2(LP) chip.

%prep
%setup -q

%build
sh autogen.sh
%configure
make

%install
%make_install

%files
%license COPYING COPYING.LESSER
%doc NEWS README
%_datadir/sigrok-firmware

%changelog
