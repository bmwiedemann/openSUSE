#
# spec file for package solo
#
# Copyright (c) 2019 Matthias Bach <marix@marix.org>.
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


Name:           solo
Version:        2.3.0
Release:        0
Summary:        Support for the Solo and Solo Tap security keys
License:        Apache-2.0 or MIT
Group:          Hardware/Other
Url:            https://solokeys.com
Source:         https://github.com/solokeys/solo/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        solo-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Miscellaneous tools and helpers to work with the Solo and Solo Tap security keys.

The Solo and Solo Tap are FIDO2 security keys with USB and, in the case of the Solo Tap, NFC support.

%package udev
Summary:        Udev rules for Solo and Solo Tap security keys
Group:          System/Kernel
Requires:       udev
BuildArch:      noarch

%description udev
This package contains the udev rule file for the Solo and Solo Tap security keys.
These are required if local non-root users are supposed to be able to use the keys.

%prep
%setup -q

%build

%install
install -Dm 644 udev/70-%{name}keys-access.rules %{buildroot}%{_udevrulesdir}/70-%{name}keys-access.rules

%files udev
%defattr(0644,root,root,-)
%license LICENSE LICENSE-APACHE LICENSE-MIT
%dir %{_udevrulesdir}
%{_udevrulesdir}/70-%{name}keys-access.rules

%changelog

