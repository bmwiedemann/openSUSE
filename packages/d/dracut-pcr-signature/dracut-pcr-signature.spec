#
# spec file for package dracut-pcr-signature
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


Name:           dracut-pcr-signature
Version:        0.6+0
Release:        0
Summary:        Dracut module to import PCR signatures
License:        GPL-2.0-or-later
URL:            https://github.com/aplanas/dracut-pcr-signature
Source:         %{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
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
mkdir -p %{buildroot}%{_prefix}/lib/dracut/modules.d/50pcr-signature
for i in module-setup.sh boot-efi-generator.sh pcr-signature.sh pcr-signature.service; do
    cp "$i" %{buildroot}%{_prefix}/lib/dracut/modules.d/50pcr-signature
done

%post
%{?regenerate_initrd_post}

%posttrans
%{?regenerate_initrd_posttrans}

%postun
%{?regenerate_initrd_post}

%files
%license LICENSE
%doc README.md
%dir %{_prefix}/lib/dracut
%dir %{_prefix}/lib/dracut/modules.d
%{_prefix}/lib/dracut/modules.d/50pcr-signature

%changelog
