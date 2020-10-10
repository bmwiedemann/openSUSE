#
# spec file for package hwdata
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


Name:           hwdata
Version:        0.340
Release:        0
Summary:        Hardware identification and configuration data
License:        GPL-2.0-or-later
URL:            https://github.com/vcrhonek/hwdata
Source:         https://github.com/vcrhonek/hwdata/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Provides:       pciutils-ids = 20200529
Obsoletes:      pciutils-ids < 20200529
BuildArch:      noarch

%description
hwdata contains various hardware identification and configuration data,
such as the pci.ids and usb.ids databases.

%prep
%setup -q

%build
%configure
# nothing to build

%install
%make_install

# create symlink for smooth transition from pciutils-ids package
ln -s %{_datadir}/hwdata/pci.ids \
  %{buildroot}%{_datadir}/pci.ids

# not needed at all
rm -rf %{buildroot}/%{_libdir}/modprobe.d

%files
%license LICENSE COPYING
%dir %{_datadir}/%{name}
%{_datadir}/hwdata/iab.txt
%{_datadir}/hwdata/oui.txt
%{_datadir}/hwdata/pci.ids
%{_datadir}/hwdata/pnp.ids
%{_datadir}/hwdata/usb.ids
%{_datadir}/pci.ids

%changelog
