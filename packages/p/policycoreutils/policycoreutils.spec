#
# spec file for package policycoreutils
#
# Copyright (c) 2022 SUSE LLC
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


%define libaudit_ver     2.2
%define libsepol_ver     3.4
%define libsemanage_ver  3.4
%define libselinux_ver   3.4
%define setools_ver      4.1.1
Name:           policycoreutils
Version:        3.4
Release:        0
Summary:        SELinux policy core utilities
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            https://github.com/SELinuxProject/selinux
Source0:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        policycoreutils.keyring
Source3:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/selinux-python-%{version}.tar.gz
Source4:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/selinux-python-%{version}.tar.gz.asc
Source5:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/semodule-utils-%{version}.tar.gz
Source6:        https://github.com/SELinuxProject/selinux/releases/download/%{version}/semodule-utils-%{version}.tar.gz.asc
Source7:        system-config-selinux.png
Source8:        system-config-selinux.desktop
Source9:        system-config-selinux.pam
Source10:       system-config-selinux.console
Source11:       selinux-polgengui.desktop
Source12:       selinux-polgengui.console
Source13:       newrole.pam
Patch0:         make_targets.patch
Patch2:         get_os_version.patch
Patch3:         run_init.pamd.patch
Patch4:         chcat_handle_missing_translations.patch
BuildRequires:  audit-devel >= %{libaudit_ver}
BuildRequires:  bison
BuildRequires:  dbus-1-glib-devel
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gettext
BuildRequires:  hicolor-icon-theme
BuildRequires:  libbz2-devel
BuildRequires:  libcap-devel
BuildRequires:  libcap-ng-devel
BuildRequires:  libselinux-devel >= %{libselinux_ver}
BuildRequires:  libsemanage-devel >= %{libsemanage_ver}
BuildRequires:  libsepol-devel-static >= %{libsepol_ver}
BuildRequires:  pam-devel
# needed only for dir /usr/share/polkit-1 from policycoreutils-gui
BuildRequires:  polkit
BuildRequires:  python-rpm-macros
BuildRequires:  python3
BuildRequires:  python3-setools >= %{setools_ver}
BuildRequires:  update-desktop-files
BuildRequires:  xmlto
Requires:       gawk
Requires:       libsepol2 >= %{libsepol_ver}
Requires:       rpm
Requires:       selinux-tools
Requires:       util-linux

%description
policycoreutils contains the policy core utilities that are required
for basic operation of a SELinux system.  These utilities include
load_policy to load policies, setfiles to label filesystems, newrole
to switch roles, and run_init to run %{_initddir} scripts in the proper
context.

(Security-enhanced Linux is a feature of the kernel and some
utilities that implement mandatory access control policies, such as
Type Enforcement, Role-based Access Control and Multi-Level
Security.)

%lang_package

%package -n python3-%{name}
Summary:        SELinux policy core python3 interfaces
Group:          Productivity/Security
Requires:       %{name} = %{version}-%{release}
Requires:       checkpolicy
Requires:       python3-audit >= %{libaudit_ver}
Requires:       python3-selinux
Requires:       python3-semanage >= %{libsepol_ver}
Requires:       python3-setools >= %{setools_ver}
Requires:       python3-setuptools
Provides:       policycoreutils-python = %{version}-%{release}
Obsoletes:      policycoreutils-python < %{version}
BuildArch:      noarch

%description -n python3-%{name}
The python-policycoreutils package contains the interfaces that can be used
by python in an SELinux environment.

%package python-utils
Summary:        SELinux policy core python utilities
Group:          Productivity/Security
Requires:       python3-policycoreutils = %{version}-%{release}
BuildArch:      noarch
Obsoletes:      policycoreutils-python

%description python-utils
The policycoreutils-python-utils package contains the management tools
use to manage an SELinux environment.

%package devel
Summary:        SELinux policy core policy devel utilities
Group:          Productivity/Security
Requires:       %{_bindir}/make
Requires:       python3-%{name} = %{version}-%{release}
Recommends:     %{_sbindir}/ausearch
Conflicts:      %{name}-python <= 2.6

%description devel
The policycoreutils-devel package contains the management tools use to develop policy in an SELinux environment.

%package sandbox
Summary:        SELinux sandbox utilities
Group:          Productivity/Security
Requires:       python3-%{name} = %{version}
Requires:       xorg-x11-server-extra

%description sandbox
The sandbox package contains the scripts to create graphical sandboxes.

%package newrole
Summary:        The newrole application for RBAC/MLS
Group:          Productivity/Security
Requires:       %{name} = %{version}
# we need both, else permissions could be de-installed
# and verify failed
Requires:       permissions
Requires(post): permissions

%description newrole
RBAC/MLS policy machines require newrole as a way of changing the role
or level of a logged-in user.

%if 0%{?suse_version} < 1500
%package gui
Summary:        SELinux configuration GUI
Group:          Productivity/Security
Requires:       python
Requires:       python-gnome
Requires:       python-gtk
Requires:       python3-%{name} = %{version}
Requires:       selinux-policy
Requires:       setools-console

%description gui
system-config-selinux is a utility for managing the SELinux environment.
%endif

%prep
%setup -q -a3 -a5
setools_python_pwd="$PWD/selinux-python-%{version}"
semodule_utils_pwd="$PWD/semodule-utils-%{version}"
%patch0 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
mv ${setools_python_pwd}/audit2allow ${setools_python_pwd}/chcat ${setools_python_pwd}/semanage ${setools_python_pwd}/sepolgen ${setools_python_pwd}/sepolicy .
mv ${semodule_utils_pwd}/semodule_expand ${semodule_utils_pwd}/semodule_link ${semodule_utils_pwd}/semodule_package .

%build
export PYTHON="python3" LIBDIR="%{_libdir}" CFLAGS="%{optflags} -fPIE" LDFLAGS="-pie -Wl,-z,relro"
make %{?_smp_mflags} LIBEXECDIR="%{_libexecdir}"
(cd selinux-python-%{version}/po && make)

%install
export PYTHON="python3"
mkdir -p %{buildroot}%{_localstatedir}/lib/selinux
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}/sbin
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_sysconfdir}/security/console.apps
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_pam_vendordir}
%else
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
%endif
make LSPP_PRIV=y DESTDIR=%{buildroot} install LIBEXECDIR=%{_libexecdir}
%if 0%{?suse_version} > 1500
cp -f %{SOURCE13} %{buildroot}%{_pam_vendordir}/newrole
rm %{buildroot}%{_sysconfdir}/pam.d/newrole
mv %{buildroot}%{_sysconfdir}/pam.d/run_init %{buildroot}%{_pam_vendordir}/run_init
%else
cp -f %{SOURCE13} %{buildroot}%{_sysconfdir}/pam.d/newrole
%endif
install -D -m 644 %{SOURCE12} %{buildroot}%{_datadir}/pixmaps/system-config-selinux.png
%if 0%{?suse_version} < 1500
install -m 644 %{SOURCE13} %{buildroot}%{_sysconfdir}/pam.d/system-config-selinux
install -m 644 %{SOURCE13} %{buildroot}%{_sysconfdir}/pam.d/selinux-polgengui
%endif
install -m 644 %{SOURCE10} %{buildroot}%{_sysconfdir}/security/console.apps/system-config-selinux
install -m 644 %{SOURCE12} %{buildroot}%{_sysconfdir}/security/console.apps/selinux-polgengui
rm -f %{buildroot}%{_mandir}/ru/man8/genhomedircon.8.gz
ln -sf consolehelper %{buildroot}%{_bindir}/system-config-selinux
ln -sf consolehelper %{buildroot}%{_bindir}/selinux-polgengui
mkdir -p %{buildroot}%{_libexecdir}/selinux/hll/
mkdir -p %{buildroot}%{_localstatedir}/lib/sepolgen
cp %{python3_sitearch}/setools/perm_map %{buildroot}%{_localstatedir}/lib/sepolgen
%suse_update_desktop_file -i system-config-selinux System Security Settings
%suse_update_desktop_file -i selinux-polgengui System Security Settings
(cd selinux-python-%{version}/po && make DESTDIR=%{buildroot} install)
%find_lang %{name}
%find_lang selinux-python
%fdupes -s %{buildroot}%{_datadir}

%if 0%{?suse_version} >= 1500
rm %{buildroot}%{_sysconfdir}/security/console.apps/selinux-polgengui \
   %{buildroot}%{_sysconfdir}/security/console.apps/system-config-selinux \
   %{buildroot}%{_bindir}/selinux-polgengui \
   %{buildroot}%{_bindir}/system-config-selinux \
   %{buildroot}%{_datadir}/applications/selinux-polgengui.desktop \
   %{buildroot}%{_datadir}/applications/system-config-selinux.desktop \
   %{buildroot}%{_datadir}/pixmaps/system-config-selinux.png
%endif

mv %{buildroot}/sbin/* %{buildroot}/usr/sbin/

%if 0%{?suse_version} > 1500
%pre
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in pam.d/run_init ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%pre newrole
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in pam.d/newrole ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/etc, restore just created .rpmsave
for i in pam.d/run_init ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done

%posttrans newrole
# Migration to /usr/etc, restore just created .rpmsave
for i in pam.d/newrole ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%post newrole
%set_permissions %{_bindir}/newrole

%verifyscript newrole
%verify_permissions -e %{_bindir}/newrole

%files
%{_bindir}/semodule_expand
%{_bindir}/semodule_link
%{_bindir}/semodule_package
%{_bindir}/semodule_unpackage
%{_sbindir}/restorecon
%{_sbindir}/setfiles
%{_sbindir}/restorecon_xattr
%{_sbindir}/fixfiles
%{_sbindir}/load_policy
%dir %{_libexecdir}/selinux
%dir %{_libexecdir}/selinux/hll
%{_libexecdir}/selinux/hll/pp
%{_sbindir}/genhomedircon
%{_sbindir}/setsebool
%{_sbindir}/semodule
%{_sbindir}/sestatus
%{_bindir}/sestatus
%{_sbindir}/run_init
%{_sbindir}/open_init_pty
%{_bindir}/secon
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/run_init
%else
%config(noreplace) %{_sysconfdir}/pam.d/run_init
%endif
%config(noreplace) %{_sysconfdir}/sestatus.conf
%{_mandir}/man8/fixfiles.8%{?ext_man}
%{_mandir}/man8/genhomedircon.8%{?ext_man}
%{_mandir}/man8/load_policy.8%{?ext_man}
%{_mandir}/man8/open_init_pty.8%{?ext_man}
%{_mandir}/man8/restorecon.8%{?ext_man}
%{_mandir}/man8/restorecon_xattr.8%{?ext_man}
%{_mandir}/man8/run_init.8%{?ext_man}
%{_mandir}/man8/semodule.8%{?ext_man}
%{_mandir}/man8/semodule_expand.8%{?ext_man}
%{_mandir}/man8/semodule_link.8%{?ext_man}
%{_mandir}/man8/semodule_package.8%{?ext_man}
%{_mandir}/man8/semodule_unpackage.8%{?ext_man}
%{_mandir}/man8/sestatus.8%{?ext_man}
%{_mandir}/man8/setfiles.8%{?ext_man}
%{_mandir}/man8/setsebool.8%{?ext_man}
%{_mandir}/ru/man8/fixfiles.8%{?ext_man}
%{_mandir}/ru/man8/genhomedircon.8%{?ext_man}
%{_mandir}/ru/man8/load_policy.8%{?ext_man}
%{_mandir}/ru/man8/open_init_pty.8%{?ext_man}
%{_mandir}/ru/man8/restorecon.8%{?ext_man}
%{_mandir}/ru/man8/restorecon_xattr.8%{?ext_man}
%{_mandir}/ru/man8/run_init.8%{?ext_man}
%{_mandir}/ru/man8/semodule.8%{?ext_man}
%{_mandir}/ru/man8/semodule_expand.8%{?ext_man}
%{_mandir}/ru/man8/semodule_link.8%{?ext_man}
%{_mandir}/ru/man8/semodule_package.8%{?ext_man}
%{_mandir}/ru/man8/semodule_unpackage.8%{?ext_man}
%{_mandir}/ru/man8/sestatus.8%{?ext_man}
%{_mandir}/ru/man8/setfiles.8%{?ext_man}
%{_mandir}/ru/man8/setsebool.8%{?ext_man}
%{_mandir}/man5/selinux_config.5%{?ext_man}
%{_mandir}/man5/sestatus.conf.5%{?ext_man}
%{_mandir}/ru/man5/selinux_config.5%{?ext_man}
%{_mandir}/ru/man5/sestatus.conf.5%{?ext_man}
%{_mandir}/man1/secon.1%{?ext_man}
%{_mandir}/ru/man1/secon.1%{?ext_man}
%{_datadir}/bash-completion/completions/setsebool

%files -n python3-%{name}
%{python3_sitelib}/*
%dir %{_localstatedir}/lib/selinux

%files lang -f %{name}.lang

%files python-utils -f selinux-python.lang
%{_bindir}/audit2allow
%{_bindir}/audit2why
%{_bindir}/chcat
%{_sbindir}/semanage
%{_mandir}/man1/audit2allow.1%{?ext_man}
%{_mandir}/ru/man1/audit2allow.1%{?ext_man}
%{_mandir}/man1/audit2why.1%{?ext_man}
%{_mandir}/ru/man1/audit2why.1%{?ext_man}
%{_mandir}/man8/chcat.8%{?ext_man}
%{_mandir}/ru/man8/chcat.8%{?ext_man}
%{_mandir}/man8/semanage*.8%{?ext_man}
%{_mandir}/ru/man8/semanage*.8%{?ext_man}
%{_datadir}/bash-completion/completions/semanage

%files devel
%{_bindir}/sepolgen
%{_bindir}/sepolgen-ifgen
%{_bindir}/sepolgen-ifgen-attr-helper
%{_bindir}/sepolicy
%{_mandir}/man8/sepolicy-booleans.8%{?ext_man}
%{_mandir}/man8/sepolicy-communicate.8%{?ext_man}
%{_mandir}/man8/sepolicy-generate.8%{?ext_man}
%{_mandir}/man8/sepolicy-gui.8%{?ext_man}
%{_mandir}/man8/sepolicy-interface.8%{?ext_man}
%{_mandir}/man8/sepolicy-manpage.8%{?ext_man}
%{_mandir}/man8/sepolicy-network.8%{?ext_man}
%{_mandir}/man8/sepolicy-transition.8%{?ext_man}
%{_mandir}/man8/sepolicy.8%{?ext_man}
%{_mandir}/man8/sepolgen.8%{?ext_man}
%{_mandir}/ru/man8/sepolicy-booleans.8%{?ext_man}
%{_mandir}/ru/man8/sepolicy-communicate.8%{?ext_man}
%{_mandir}/ru/man8/sepolicy-generate.8%{?ext_man}
%{_mandir}/ru/man8/sepolicy-gui.8%{?ext_man}
%{_mandir}/ru/man8/sepolicy-interface.8%{?ext_man}
%{_mandir}/ru/man8/sepolicy-manpage.8%{?ext_man}
%{_mandir}/ru/man8/sepolicy-network.8%{?ext_man}
%{_mandir}/ru/man8/sepolicy-transition.8%{?ext_man}
%{_mandir}/ru/man8/sepolicy.8%{?ext_man}
%{_mandir}/ru/man8/sepolgen.8%{?ext_man}
%dir %{_localstatedir}/lib/sepolgen
%{_localstatedir}/lib/sepolgen/perm_map
%{_datadir}/bash-completion/completions/sepolicy

%files newrole
%verify(not mode) %attr(4755,root,root) %{_bindir}/newrole
%{_mandir}/man1/newrole.1%{?ext_man}
%{_mandir}/ru/man1/newrole.1%{?ext_man}
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/newrole
%else
%config(noreplace) %{_sysconfdir}/pam.d/newrole
%endif

%if 0%{?suse_version} < 1500
%files gui
%{_bindir}/system-config-selinux
%{_bindir}/selinux-polgengui
%{_datadir}/applications/system-config-selinux.desktop
%{_datadir}/system-config-selinux/system-config-selinux.desktop
%{_datadir}/applications/selinux-polgengui.desktop
%{_datadir}/applications/sepolicy.desktop
%{_datadir}/system-config-selinux/selinux-polgengui.desktop
%{_datadir}/system-config-selinux/sepolicy.desktop
%{_datadir}/icons/hicolor/24x24/apps/system-config-selinux.png
%{_datadir}/icons/hicolor/16x16/apps/sepolicy.png
%{_datadir}/icons/hicolor/22x22/apps/sepolicy.png
%{_datadir}/icons/hicolor/256x256/apps/sepolicy.png
%{_datadir}/icons/hicolor/32x32/apps/sepolicy.png
%{_datadir}/icons/hicolor/48x48/apps/sepolicy.png
%{_datadir}/pixmaps/sepolicy.png
%{_datadir}/pixmaps/system-config-selinux.png
%{_datadir}/polkit-1/actions/org.selinux.config.policy
%{_datadir}/polkit-1/actions/org.selinux.policy
%dir %{_datadir}/system-config-selinux
%{_datadir}/system-config-selinux/system-config-selinux.png
%{_datadir}/system-config-selinux/*.py*
%{_datadir}/system-config-selinux/*.glade
%{_mandir}/man8/selinux-polgengui.8%{?ext_man}
%{_mandir}/man8/system-config-selinux.8%{?ext_man}
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.selinux.conf
%config(noreplace) %{_sysconfdir}/pam.d/system-config-selinux
%config(noreplace) %{_sysconfdir}/pam.d/selinux-polgengui
%dir %{_sysconfdir}/security/console.apps
%config(noreplace) %{_sysconfdir}/security/console.apps/selinux-polgengui
%config(noreplace) %{_sysconfdir}/security/console.apps/system-config-selinux
%endif

%changelog
