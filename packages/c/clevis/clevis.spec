#
# spec file for package clevis
#
# Copyright (c) 2023 SUSE LLC
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


Name:           clevis
Version:        19
Release:        0
Summary:        A pluggable framework for automated decryption
License:        GPL-3.0-or-later
URL:            https://github.com/latchset/clevis
Source0:        https://github.com/latchset/clevis/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0:         cryptsetup-path.patch
BuildRequires:  asciidoc
BuildRequires:  cryptsetup
BuildRequires:  curl
BuildRequires:  jq
BuildRequires:  keyutils
BuildRequires:  libpwquality-tools
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  socat
BuildRequires:  tpm2.0-tools >= 3.0.0
BuildRequires:  pkgconfig(audit) >= 2.7.8
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(dracut)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(jansson) >= 2.10
BuildRequires:  pkgconfig(jose) >= 8
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libcryptsetup) >= 2.0.2
BuildRequires:  pkgconfig(luksmeta) >= 8
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udisks2)
Requires:       curl
Requires:       jose >= 8
Requires:       tpm2.0-tools >= 3.0.0

%description
Clevis is a pluggable framework for automated decryption. It can be used to
provide automated decryption of data or even automated unlocking of LUKS
volumes.

%package luks
Summary:        LUKS integration for Clevis
Requires:       %{name} = %{version}
Requires:       cryptsetup
Requires:       libpwquality-tools
#Requires:       luksmeta >= 8

%description luks
LUKS integration for Clevis.

%package systemd
Summary:        Systemd integration for Clevis
Requires:       %{name}-luks = %{version}
Requires:       systemd

%description systemd
Automatically unlock LUKS devices in /etc/crypttab with Clevis.

%package dracut
Summary:        Dracut integration for Clevis
Requires:       %{name}-systemd = %{version}
Requires:       dracut

%description dracut
Automatically unlock LUKS devices in /etc/crypttab with Clevis at early boot.

%package udisks2
Summary:        UDisks2 integration for Clevis
Requires:       %{name}-luks = %{version}

%description udisks2
Automatically unlock LUKS devices in UDisks2 with Clevis.

%package bash-completion
Summary:        Bash completion for Clevis
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    packageand(%{name}:bash)

%description bash-completion
This package provides Bash completion for Clevis.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%pre systemd
%service_add_pre clevis-luks-askpass.path clevis-luks-askpass.service

%post systemd
%service_add_post clevis-luks-askpass.path clevis-luks-askpass.service

%preun systemd
%service_del_preun clevis-luks-askpass.path clevis-luks-askpass.service

%postun systemd
%service_del_postun clevis-luks-askpass.path clevis-luks-askpass.service

%post dracut
%{?regenerate_initrd_post}

%postun dracut
%{?regenerate_initrd_post}

%posttrans dracut
%{?regenerate_initrd_posttrans}

%files
%license COPYING
%{_bindir}/clevis
%{_bindir}/clevis-decrypt
%{_bindir}/clevis-decrypt-*
%{_bindir}/clevis-encrypt-*
%{_mandir}/man1/clevis.1%{?ext_man}
%{_mandir}/man1/clevis-decrypt.1%{?ext_man}
%{_mandir}/man1/clevis-encrypt-*.1%{?ext_man}

%files luks
%license COPYING
%{_bindir}/clevis-luks-*
%{_mandir}/man[17]/clevis-luks-*.[17]%{?ext_man}

%files systemd
%license COPYING
%{_libexecdir}/clevis-luks-askpass
%{_unitdir}/*

%files dracut
%license COPYING
%{_prefix}/lib/dracut/modules.d/**

%files udisks2
%license COPYING
%{_libexecdir}/clevis-luks-udisks2
%{_sysconfdir}/xdg/autostart/clevis-luks-udisks2.desktop

%files bash-completion
%license COPYING
%{_datadir}/bash-completion/completions/clevis

%changelog
