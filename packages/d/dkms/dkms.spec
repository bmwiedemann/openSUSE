#
# spec file for package dkms
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


Name:           dkms
Version:        3.1.3
Release:        0
Summary:        Dynamic Kernel Module Support Framework
License:        GPL-2.0-only
Group:          System/Kernel
URL:            https://github.com/dell/dkms
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source100:      %{name}.rpmlintrc
# PATCH-FIX-OPENSUSE fix-weak-modules_dkms_in.patch boo#1194723
Patch1:         fix-weak-modules_dkms_in.patch
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

%package bash-completion
Summary:        Bash completion for %{name}
BuildRequires:  bash-completion
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash command line completion support for %{name}.

%package zsh-completion
Summary:        Zsh completion for %{name}
BuildRequires:  zsh
Requires:       %{name} = %{version}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
Zsh command line completion support for %{name}.

%prep
%setup -q
%autopatch -p1 1

%build

%install
# Note: the makefile changed and has the following gotchas:
# 1. Defined variables should not contain buildroot, the given
#    paths are concatenated with DESTDIR (which has buildroot) by
#    the makefile
# 2. BASHDIR, ETC and VAR are not settable
%make_install install-redhat \
  SBIN=%{_sbindir} \
  MAN=%{_mandir}/man8 \
  LIBDIR=%{_libexecdir}/%{name} \
  KCONF=%{_sysconfdir}/kernel \
  KINSTALL=%{_prefix}/lib/kernel/install.d

# systemd
install -p -m 644 -D dkms.service %{buildroot}%{_unitdir}/dkms.service

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
%{_tmpfilesdir}/dkms.conf
%{_mandir}/man8/dkms.8%{ext_man}
%{_unitdir}/dkms.service
# these dirs are for plugins - owned by other packages
%dir %{_prefix}/lib/kernel/
%dir %{_prefix}/lib/kernel/install.d

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%files zsh-completion
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_%{name}

%changelog
