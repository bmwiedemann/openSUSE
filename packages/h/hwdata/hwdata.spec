#
# spec file for package hwdata
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


Name:           hwdata
Version:        0.383
Release:        0
Summary:        Hardware identification and configuration data
License:        GPL-2.0-or-later
URL:            https://github.com/vcrhonek/hwdata
Source0:        https://github.com/vcrhonek/hwdata/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        merge-pciids.pl
Requires(post): coreutils
Requires(post): perl
Conflicts:      pciutils-ids
Provides:       pciutils-ids = 20200529
Obsoletes:      pciutils-ids < 20200529
BuildArch:      noarch

%description
hwdata contains various hardware identification and configuration data,
such as the pci.ids and usb.ids databases.

%prep
%autosetup

%build
%configure
# nothing to build

%install
%make_install

# create symlink for smooth transition from pciutils-ids package
mkdir %{buildroot}%{_datadir}/pci.ids.d
ln -s %{_datadir}/hwdata/pci.ids \
  %{buildroot}%{_datadir}/pci.ids.d/pci.ids.dist

install -Dpm 0755 %{SOURCE1} \
  %{buildroot}%{_bindir}/merge-pciids
install -Dpm 0644 /dev/null \
  %{buildroot}%{_datadir}/pci.ids

# not needed at all
rm -rf %{buildroot}/%{_libdir}/modprobe.d

%post
if [ -x %{_bindir}/merge-pciids -a -x %{_bindir}/perl ]; then
  %{_bindir}/merge-pciids
else
  # This should only happen in autobuild
  echo "WARNING: merge-pciids or perl not found"
  cp -p %{_datadir}/pci.ids.d/pci.ids.dist %{_datadir}/pci.ids
fi

%files
%license LICENSE COPYING
%{_bindir}/merge-pciids
%{_datadir}/pkgconfig/hwdata.pc
%dir %{_datadir}/%{name}
%{_datadir}/hwdata/iab.txt
%{_datadir}/hwdata/oui.txt
%{_datadir}/hwdata/pci.ids
%{_datadir}/hwdata/pnp.ids
%{_datadir}/hwdata/usb.ids
%dir %{_datadir}/pci.ids.d
%{_datadir}/pci.ids.d/pci.ids.dist
%ghost %{_datadir}/pci.ids

%changelog
