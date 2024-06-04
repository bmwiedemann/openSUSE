#
# spec file for package dracut-pcr-signature
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


Name:           dracut-pcr-signature
Version:        0.4+0
Release:        0
Summary:        Dracut module to import PCR signatures
License:        GPL-2.0-or-later
URL:            https://github.com/aplanas/dracut-pcr-signature
Source:         %{name}-%{version}.tar.xz
BuildRequires:  rpm-config-SUSE
BuildRequires:  pkgconfig(dracut)
BuildArch:      noarch

%description
Dracut module to import PCR signatures.  This will make possible the
prediction of the initrd (and cmdline) hashes, as will not require the
update of the initrd to introduce the JSON and PEM files required to
unlock the LUKS2 device via systemd-cryptsetup.

%prep
%setup -q

%build

%install
mkdir -p %buildroot/usr/lib/dracut/modules.d/50pcr-signature
cp module-setup.sh %buildroot/usr/lib/dracut/modules.d/50pcr-signature
cp pcr-signature.sh %buildroot/usr/lib/dracut/modules.d/50pcr-signature
cp pcr-signature.conf %buildroot/usr/lib/dracut/modules.d/50pcr-signature

%post
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%postun
%{?regenerate_initrd_post}

%files
%license LICENSE
%doc README.md
%dir /usr/lib/dracut
%dir /usr/lib/dracut/modules.d
/usr/lib/dracut/modules.d/50pcr-signature

%changelog
