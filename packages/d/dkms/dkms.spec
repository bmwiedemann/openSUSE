#
# spec file for package dkms
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


Name:           dkms
Version:        3.0.11
Release:        0
Summary:        Dynamic Kernel Module Support Framework
License:        GPL-2.0-only
Group:          System/Kernel
URL:            https://github.com/dell/dkms
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source3:        dkms.default
Source100:      %{name}.rpmlintrc
# PATCH-FIX-OPENSUSE fix-kernel-postinst_d.patch boo#1194723
Patch1:         fix-kernel-postinst_d.patch
# PATCH-FIX-OPENSUSE fix-weak-modules_dkms_in.patch boo#1194723
Patch2:         fix-weak-modules_dkms_in.patch
BuildRequires:  make
BuildRequires:  pkgconfig(systemd)
Requires:       bash > 1.99
Requires:       cpio
Requires:       findutils
Requires:       gawk
Requires:       gcc
Requires:       grep
Requires:       gzip
Requires:       kernel-syms
Requires:       make
Requires:       mktemp
Requires:       modutils
Requires:       sed
Requires:       tar
Requires:       zstd
Recommends:     openssl
BuildArch:      noarch
%systemd_requires

%description
This package contains the framework for the Dynamic
Kernel Module Support (DKMS) method for installing
module RPMS as originally developed by Dell.

%prep
%setup -q
%autopatch -p1 1 2

%build

%install
%make_install \
  SBIN=%{buildroot}%{_sbindir} \
  VAR=%{buildroot}%{_localstatedir}/lib/%{name} \
  MAN=%{buildroot}%{_mandir}/man8 \
  ETC=%{buildroot}%{_sysconfdir}/%{name} \
  BASHDIR=%{buildroot}%{_datadir}/bash-completion/completions \
  LIBDIR=%{buildroot}%{_libexecdir}/%{name}

install -p -m 755 -D kernel_install.d_dkms \
    %{buildroot}%{_prefix}/lib/kernel/install.d/40-%{name}.install

# Required due to changes in kernel-install
mv %{buildroot}%{_sysconfdir}/kernel/install.d/%{name} \
   %{buildroot}%{_sysconfdir}/kernel/install.d/40-%{name}.install

# systemd
install -p -m 644 -D dkms.service %{buildroot}%{_unitdir}/dkms.service

install -m 644 -D %{SOURCE3} %{buildroot}%{_sysconfdir}/default/dkms
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcdkms

sed -i \
    -e 's:# tmp_location="/tmp":tmp_location="%{_localstatedir}/tmp/dkms":' \
    %{buildroot}%{_sysconfdir}/dkms/framework.conf
sed -i \
    -e 's/# modprobe_on_install="true"/modprobe_on_install="true"/g' \
    %{buildroot}%{_sysconfdir}/%{name}/framework.conf

# Install /usr/lib/tmpfiles.d/dkms.conf
mkdir -p %{buildroot}%{_tmpfilesdir}
cat > %{buildroot}%{_tmpfilesdir}/dkms.conf <<EOF
# See tmpfiles.d(5) for details
d %{_localstatedir}/tmp/dkms 0700 root root -
EOF

%pre
%service_add_pre dkms.service
exit 0

%post
%tmpfiles_create %{_tmpfilesdir}/dkms.conf
# enable on initial install
%service_add_post dkms.service
exit 0

%postun
%service_del_postun dkms.service
exit 0

%preun
# remove on uninstall
%service_del_preun dkms.service
exit 0

%files
%doc README.md
%license COPYING
%config(noreplace) %{_sysconfdir}/%{name}
%{_sbindir}/%{name}
%{_sbindir}/rcdkms
%{_prefix}/lib/kernel/install.d/40-%{name}.install
%{_localstatedir}/lib/%{name}
%{_libexecdir}/%{name}
%{_tmpfilesdir}/dkms.conf
%{_mandir}/man8/dkms.8%{ext_man}
%{_sysconfdir}/kernel/postinst.d/%{name}
%{_sysconfdir}/kernel/prerm.d/%{name}
%{_sysconfdir}/kernel/install.d/40-%{name}.install
%{_datadir}/bash-completion/completions/%{name}
%{_unitdir}/dkms.service
%config %{_sysconfdir}/default/dkms
# these dirs are for plugins - owned by other packages
%dir %{_sysconfdir}/kernel
%dir %{_sysconfdir}/kernel/postinst.d
%dir %{_sysconfdir}/kernel/install.d
%dir %{_sysconfdir}/kernel/prerm.d
%dir %{_prefix}/lib/kernel/
%dir %{_prefix}/lib/kernel/install.d

%changelog
