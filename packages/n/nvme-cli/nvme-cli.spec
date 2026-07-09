#
# spec file for package nvme-cli
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%bcond_without check

Name:           nvme-cli
Version:        3.0~b.3
Release:        0
Summary:        NVM Express user space tools
License:        GPL-2.0-only
Group:          Hardware/Other
URL:            https://github.com/linux-nvme/nvme-cli/
Source0:        nvme-cli-%{version}.tar.gz
BuildRequires:  asciidoc
BuildRequires:  dbus-1-devel
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  keyutils-devel
BuildRequires:  libjson-c-devel
BuildRequires:  libjson-c-devel
BuildRequires:  libkmod-devel
BuildRequires:  meson
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel
BuildRequires:  swig
BuildRequires:  systemd-rpm-macros
BuildRequires:  xmlto
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(libudev)

# nvme-cli API for NBFT support.
Provides:       nvmeof-boot-support = 0.1

%systemd_ordering

%description
NVM Express (NVMe) is a direct attached storage interface. The
nvme-cli package contains core management tools with minimal
dependencies.

%package -n     nvme-cli-regress-script
Summary:        A small script to test the nvme binary for regressions
Group:          Hardware/Other
Requires:       nvme-cli
BuildArch:      noarch

%description -n nvme-cli-regress-script
A small shell script to test the nvme binary for regressions. It requires an
NVMe device for testing purposes. Do NOT use in a production environment.

%package bash-completion
Summary:        NVM Express user space tools bash completion
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (nvme-cli and bash-completion)
BuildArch:      noarch

%description bash-completion
Optional dependency offering bash completion for NVM Express user space tools

%package zsh-completion
Summary:        NVM Express user space tools zsh completion
Group:          System/Shells
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (nvme-cli and zsh)
BuildArch:      noarch

%description zsh-completion
Optional dependency offering zsh completion for NVM Express user space tools

%package -n     libnvme3-1
Summary:        Linux-native nvme device management library
License:        LGPL-2.1-or-later

%description -n libnvme3-1
Provides library functions for accessing and managing NVMe devices on a Linux
system.

%package -n     libnvme3-devel
Summary:        Development files for libnvme
License:        LGPL-2.1-or-later
Requires:       libnvme3-1 = %{version}

%description -n libnvme3-devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     python3-libnvme3
Summary:        Python binding for %{name}
License:        LGPL-2.1-or-later
Requires:       libnvme3-1 = %{version}

%description -n python3-libnvme3
Provides library functions for accessing and managing NVMe devices on a Linux
system.

Python binding part.

%prep
%autosetup -p1

%build
export KBUILD_BUILD_TIMESTAMP=@${SOURCE_DATE_EPOCH:-$(date +%s)}
%meson \
    -Dudevrulesdir=%{_udevrulesdir} \
    -Ddracutrulesdir=%{_sysconfdir}/dracut/dracut.conf.d \
    -Dsystemddir=%{_unitdir} \
    -Ddocs=man \
    -Ddocs-build=true \
    -Dsystemctl=%{_bindir}/systemctl \
    -Dversion-tag=%{version}
%meson_build

%if %{with check}
%check
%meson_test
%endif

%install
%meson_install
install -m 644 -D /dev/null %{buildroot}%{_sysconfdir}/nvme/hostnqn
install -m 644 -D /dev/null %{buildroot}%{_sysconfdir}/nvme/hostid
install -m 644 -D /dev/null %{buildroot}%{_sysconfdir}/nvme/discovery.conf
rm %{buildroot}%{_sysconfdir}/dracut/dracut.conf.d/70-nvmf-autoconnect.conf

# for subpackage nvme-cli-regress-script:
install -m 744 -D scripts/regress %{buildroot}%{_sbindir}/nvme-regress

%if 0%{?suse_version} < 1600
mkdir -p %{buildroot}%{_sbindir}
pushd %{buildroot}%{_sbindir}
ln -s service rcnvmefc-boot-connections
ln -s service rcnvmf-autoconnect
ln -s service rcnvmf-connect
ln -s service rcnvmf-connect-nbft
popd
%endif

# 1. Manually compress man pages using '-n' to remove distinct timestamps/headers
find %{buildroot}%{_mandir} -type f -name '*.[1-9]' -exec gzip -n -9 {} +

# 2. Run fdupes on the entire buildroot to catch the identical .gz files
%fdupes -s %{buildroot}

%define services nvmefc-boot-connections.service nvmf-autoconnect.service nvmf-connect.target nvmf-connect-nbft.service

%pre
%service_add_pre %{services} nvmf-connect@.service

%post
if  [ ! -e /.buildenv ] && [ ! -e /image/config.xml ]; then
    if [ ! -s %{_sysconfdir}/nvme/hostnqn ]; then
	%{_bindir}/echo "Generating host NQN."
	%{_sbindir}/nvme gen-hostnqn > %{_sysconfdir}/nvme/hostnqn
    fi

    if [ ! -s %{_sysconfdir}/nvme/hostid ]; then
	sed -nr 's/.*:uuid:(.*?)$/\1/p' %{_sysconfdir}/nvme/hostnqn > %{_sysconfdir}/nvme/hostid
    fi
else
    %{_bindir}/echo "Build environment detected, not generating host NQN."
fi
%service_add_post %{services} nvmf-connect@.service

%preun
%service_del_preun %{services}

%postun
%service_del_postun %{services}

%posttrans
if [ -f /sys/class/fc/fc_udev_device/nvme_discovery ]; then
	%{_bindir}/echo add > /sys/class/fc/fc_udev_device/nvme_discovery
fi

%pre -n nvme-cli-bash-completion
if [ -d %{_datadir}/bash-completion/completions/nvme ]; then
    rm -r %{_datadir}/bash-completion/completions/nvme;
fi

%post -n libnvme3-1 -p /sbin/ldconfig

%postun -n libnvme3-1 -p /sbin/ldconfig

%files
%license LICENSE
%doc README.md
%{_sbindir}/nvme
%if 0%{?suse_version} < 1600
%{_sbindir}/rcnvmefc-boot-connections
%{_sbindir}/rcnvmf-autoconnect
%{_sbindir}/rcnvmf-connect
%{_sbindir}/rcnvmf-connect-nbft
%endif
%{_mandir}/man1/nvme*.1*%{?ext_man}
%{_udevrulesdir}/65-persistent-net-nbft.rules
%{_udevrulesdir}/70-nvmf-keys.rules
%{_udevrulesdir}/70-nvmf-autoconnect.rules
%{_udevrulesdir}/70-nvmf-registry.rules
%{_udevrulesdir}/71-nvmf-hpe.rules
%{_udevrulesdir}/71-nvmf-netapp.rules
%{_udevrulesdir}/71-nvmf-vastdata.rules
%{_unitdir}/nvmefc-boot-connections.service
%{_unitdir}/nvmf-autoconnect.service
%{_unitdir}/nvmf-connect-nbft.service
%{_unitdir}/nvmf-connect.target
%{_unitdir}/nvmf-connect@.service
%dir %{_prefix}/lib/NetworkManager
%dir %{_prefix}/lib/NetworkManager/dispatcher.d
%{_prefix}/lib/NetworkManager/dispatcher.d/80-nvmf-connect-nbft.sh
%dir %{_sysconfdir}/nvme/
%ghost %{_sysconfdir}/nvme/hostnqn
%ghost %{_sysconfdir}/nvme/hostid
%ghost %{_sysconfdir}/nvme/discovery.conf

%files -n nvme-cli-regress-script
%{_sbindir}/nvme-regress

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/nvme

%files zsh-completion
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_nvme

%files -n libnvme3-1
%license LICENSE
%doc README.md
%{_libdir}/libnvme3.so.1
%{_libdir}/libnvme3.so.1.*

%files -n libnvme3-devel
%doc README.md
%{_includedir}/libnvme3/
%{_libdir}/libnvme3.so
%{_libdir}/pkgconfig/libnvme3.pc
%{_mandir}/man2/*.2*%{?ext_man}

%files -n python3-libnvme3
%{python3_sitearch}/libnvme3/

%changelog
