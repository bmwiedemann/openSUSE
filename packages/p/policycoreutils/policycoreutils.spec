#
# spec file for package policycoreutils
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


%{?sle15_python_module_pythons}
%if 0%{?suse_version} < 1600
# redefine python_for_executables from python macros to deprecate python36
%define python_for_executables python311
# cahu 2024-05-29: dirty hack to be able to pass python3.11 as python interpreter
# in an environment variable for < 1600 to build with python3.11;
# python_binary_for_executables is only defined in this specfile so can be just replaced
# when someone has found a more clever way
%define python_binary_for_executables python3.11
%else
%define python_binary_for_executables %{python_for_executables}
%endif

%define libaudit_ver     2.2
%define libsepol_ver     3.6
%define libsemanage_ver  3.6
%define libselinux_ver   3.6
%define setools_ver      4.1.1
Name:           policycoreutils
Version:        3.6
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
Source13:       newrole.pam
Source14:       https://github.com/SELinuxProject/selinux/releases/download/%{version}/selinux-gui-%{version}.tar.gz
Source15:       https://github.com/SELinuxProject/selinux/releases/download/%{version}/selinux-gui-%{version}.tar.gz.asc
Source16:       https://github.com/SELinuxProject/selinux/releases/download/%{version}/selinux-dbus-%{version}.tar.gz
Source17:       https://github.com/SELinuxProject/selinux/releases/download/%{version}/selinux-dbus-%{version}.tar.gz.asc
Source18:       policycoreutils-rpmlintrc
Patch0:         make_targets.patch
Patch2:         get_os_version.patch
Patch3:         run_init.pamd.patch
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
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{pythons}
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  xmlto
Recommends:     setools-console
Requires:       gawk
Requires:       libsepol2 >= %{libsepol_ver}
Requires:       rpm
Requires:       selinux-tools
Requires:       util-linux
Obsoletes:      policycoreutils-python <= 2.6
%define python_subpackage_only 1
%python_subpackages

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

%package -n python-%{name}
Summary:        SELinux policy core python3 interfaces
Group:          Productivity/Security
Requires:       %{name} = %{version}-%{release}
Requires:       %{python_for_executables}-selinux
Requires:       %{python_for_executables}-semanage >= %{libsepol_ver}
Requires:       %{python_for_executables}-setools >= %{setools_ver}
Requires:       %{python_for_executables}-setuptools
%if 0%{?suse_version} < 1600
Requires:       audit-libs-python3 >= %{libaudit_ver}
%else
Requires:       %{python_for_executables}-audit >= %{libaudit_ver}
%endif
Requires:       checkpolicy
Provides:       policycoreutils-python = %{version}-%{release}
Obsoletes:      policycoreutils-python < %{version}
Obsoletes:      python-policycoreutils < %{version}-%{release}
Provides:       python-policycoreutils = %{version}-%{release}
%if "%{python_flavor}" != "python3"
Obsoletes:      python3-policycoreutils < %{version}-%{release}
%endif
BuildArch:      noarch

%description -n python-%{name}
The python-policycoreutils package contains the interfaces that can be used
by python in an SELinux environment.

%package python-utils
Summary:        SELinux policy core python utilities
Group:          Productivity/Security
Requires:       %{python_for_executables}-%{name} = %{version}-%{release}
BuildArch:      noarch
Obsoletes:      policycoreutils-python

%description python-utils
The policycoreutils-python-utils package contains the management tools
use to manage an SELinux environment.

%package devel
Summary:        SELinux policy core policy devel utilities
Group:          Productivity/Security
Requires:       %{_bindir}/make
Requires:       %{python_for_executables}-%{name} = %{version}-%{release}
%if 0%{?sle_version} <= 150400
Requires:       python3-distro
%else
Requires:       %{python_for_executables}-distro
%endif
Recommends:     %{_sbindir}/ausearch
Recommends:     selinux-policy-devel
Conflicts:      %{name}-python <= 2.6

%description devel
The policycoreutils-devel package contains the management tools use to develop policy in an SELinux environment.

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

%package gui
Summary:        SELinux configuration GUI
Group:          Productivity/Security
Requires:       %{name}-dbus = %{version}
Requires:       %{python_for_executables}
Requires:       %{python_for_executables}-%{name} = %{version}
Requires:       %{python_for_executables}-gobject
Requires:       python-gtk
Requires:       selinux-policy
Requires:       setools-console
BuildArch:      noarch

%description gui
system-config-selinux is a utility for managing the SELinux environment.

%package dbus
Summary:        SELinux policy core DBUS api
Group:          Productivity/Security
Requires:       %{python_for_executables}-%{name} = %{version}
Requires:       %{python_for_executables}-gobject
Requires:       polkit
BuildArch:      noarch

%description dbus
The policycoreutils-dbus package contains the management DBUS API use to manage
an SELinux environment.

%prep
%setup -q -a3 -a5 -a14 -a16
setools_python_pwd="$PWD/selinux-python-%{version}"
semodule_utils_pwd="$PWD/semodule-utils-%{version}"
%patch -P0 -p1
%patch -P2 -p1
%patch -P3 -p1
mv ${setools_python_pwd}/audit2allow ${setools_python_pwd}/chcat ${setools_python_pwd}/semanage ${setools_python_pwd}/sepolgen ${setools_python_pwd}/sepolicy .
mv ${semodule_utils_pwd}/semodule_expand ${semodule_utils_pwd}/semodule_link ${semodule_utils_pwd}/semodule_package .

%build
export PYTHON="%{python_binary_for_executables}" LIBDIR="%{_libdir}" CFLAGS="%{optflags} -fPIE" LDFLAGS="-pie -Wl,-z,relro"
make %{?_smp_mflags} LIBEXECDIR="%{_libexecdir}"
(cd selinux-python-%{version}/po && make)

%install
mkdir -p %{buildroot}%{_localstatedir}/lib/selinux
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
# Do not create legacy /sbin folder on newer systems
%if 0%{?suse_version} <= 1500
mkdir -p %{buildroot}/sbin
%endif
mkdir -p %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_mandir}/man8
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_pam_vendordir}
%else
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
%endif

# Set the SBINDIR to the openSUSE one (/usb/sbin)
%python_expand make PYTHON=$python LSPP_PRIV=y DESTDIR=%{buildroot} SBINDIR=%{_sbindir} install LIBEXECDIR=%{_libexecdir}
export PYTHON="%{python_binary_for_executables}"
%if 0%{?suse_version} > 1500
cp -f %{SOURCE13} %{buildroot}%{_pam_vendordir}/newrole
rm %{buildroot}%{_sysconfdir}/pam.d/newrole
mv %{buildroot}%{_sysconfdir}/pam.d/run_init %{buildroot}%{_pam_vendordir}/run_init
%else
cp -f %{SOURCE13} %{buildroot}%{_sysconfdir}/pam.d/newrole
%endif

# Dbus
(cd selinux-dbus-%{version} && make DESTDIR=%{buildroot} install)
# Move dbus configuration file to /usr/share
mkdir -p %{buildroot}%{_datadir}/dbus-1/system.d
mv %{buildroot}%{_sysconfdir}/dbus-1/system.d/org.selinux.conf %{buildroot}%{_datadir}/dbus-1/system.d/org.selinux.conf

# GUI apps
(cd selinux-gui-%{version} && make DESTDIR=%{buildroot} install)
%if 0%{?suse_version} > 1500
install -m 644 %{SOURCE13} %{buildroot}%{_pam_vendordir}/selinux-polgengui
install -m 644 %{SOURCE13} %{buildroot}%{_pam_vendordir}/system-config-selinux
%else
install -m 644 %{SOURCE13} %{buildroot}%{_sysconfdir}/pam.d/selinux-polgengui
install -m 644 %{SOURCE13} %{buildroot}%{_sysconfdir}/pam.d/system-config-selinux
%endif
%suse_update_desktop_file -i system-config-selinux System Security Settings
%suse_update_desktop_file -i selinux-polgengui System Security Settings
%suse_update_desktop_file -i sepolicy System Security Settings

# Add compatibility symlinks from /usr/sbin to /sbin on Leap
%if 0%{?suse_version} <= 1500
for f in `ls -1 %{buildroot}%{_sbindir}`
do
ln -rs "%{buildroot}%{_sbindir}/$f" "%{buildroot}/sbin/$f"
done
%endif

mkdir -p %{buildroot}%{_libexecdir}/selinux/hll/
mkdir -p %{buildroot}%{_localstatedir}/lib/sepolgen

(cd selinux-python-%{version}/po && make DESTDIR=%{buildroot} install)
%find_lang %{name}
%find_lang selinux-python
%find_lang selinux-gui
%fdupes -s %{buildroot}%{_datadir}

%if 0%{?suse_version} < 1600
%python311_fix_shebang
# cahu 2024-05-29: the python3_fix_shebang_path macro does not exist in <1600 so far and the
# python311_fix_shebang macro in <1600 does not fix /usr/sbin so dirty hack:
# please replace this with python3_fix_shebang_path when python-rpm-macros get updated in <1600
sed -i '1s@#!.*python.*@#!%{_bindir}/%{python_binary_for_executables}@' %{buildroot}/sbin/semanage
%else
%python3_fix_shebang
%endif

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
# Compatibility symlinks from /usr/sbin to /sbin on Leap
%if 0%{?suse_version} <= 1500
/sbin/fixfiles
/sbin/genhomedircon
/sbin/load_policy
/sbin/open_init_pty
/sbin/restorecon
/sbin/restorecon_xattr
/sbin/run_init
/sbin/semodule
/sbin/sestatus
/sbin/setfiles
/sbin/setsebool
%endif
# PAM
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
%{_mandir}/man5/selinux_config.5%{?ext_man}
%{_mandir}/man5/sestatus.conf.5%{?ext_man}
%{_mandir}/man1/secon.1%{?ext_man}
%{_datadir}/bash-completion/completions/setsebool

%files %{python_files policycoreutils}
%{python_sitelib}/sepolicy
%{python_sitelib}/sepolgen
%{python_sitelib}/sepolicy-%{version}.dist-info
%{python_sitelib}/seobject.py

%files lang -f %{name}.lang

%files python-utils -f selinux-python.lang
%{_bindir}/audit2allow
%{_bindir}/audit2why
%{_bindir}/chcat
%{_sbindir}/semanage
# Compatibility symlinks from /usr/sbin to /sbin on Leap
%if 0%{?suse_version} <= 1500
/sbin/semanage
%endif
%{_mandir}/man1/audit2allow.1%{?ext_man}
%{_mandir}/man1/audit2why.1%{?ext_man}
%{_mandir}/man8/chcat.8%{?ext_man}
%{_mandir}/man8/semanage*.8%{?ext_man}
%{_datadir}/bash-completion/completions/semanage
%dir %{_localstatedir}/lib/selinux

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
%dir %{_localstatedir}/lib/sepolgen
%{_localstatedir}/lib/sepolgen/perm_map
%{_datadir}/bash-completion/completions/sepolicy

%files newrole
%verify(not mode) %attr(4755,root,root) %{_bindir}/newrole
%{_mandir}/man1/newrole.1%{?ext_man}
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/newrole
%else
%config(noreplace) %{_sysconfdir}/pam.d/newrole
%endif

%files gui -f selinux-gui.lang
%{_bindir}/system-config-selinux
%{_bindir}/selinux-polgengui
%{_datadir}/applications/system-config-selinux.desktop
%{_datadir}/applications/selinux-polgengui.desktop
%{_datadir}/applications/sepolicy.desktop
%{_datadir}/icons/hicolor/24x24/apps/system-config-selinux.png
%{_datadir}/icons/hicolor/16x16/apps/sepolicy.png
%{_datadir}/icons/hicolor/22x22/apps/sepolicy.png
%{_datadir}/icons/hicolor/256x256/apps/sepolicy.png
%{_datadir}/icons/hicolor/32x32/apps/sepolicy.png
%{_datadir}/icons/hicolor/48x48/apps/sepolicy.png
%{_datadir}/pixmaps/sepolicy.png
%{_datadir}/pixmaps/system-config-selinux.png
%dir %{_datadir}/system-config-selinux
%{_datadir}/system-config-selinux/system-config-selinux.png
%{_datadir}/system-config-selinux/*Page.py
%{_datadir}/system-config-selinux/system-config-selinux.py
%{_datadir}/system-config-selinux/*.ui
%{_mandir}/man8/selinux-polgengui.8%{?ext_man}
%{_mandir}/man8/system-config-selinux.8%{?ext_man}
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/system-config-selinux
%{_pam_vendordir}/selinux-polgengui
%else
%config(noreplace) %{_sysconfdir}/pam.d/system-config-selinux
%config(noreplace) %{_sysconfdir}/pam.d/selinux-polgengui
%endif

%files dbus
%{_datadir}/dbus-1/system.d/org.selinux.conf
%{_datadir}/dbus-1/system-services/org.selinux.service
%{_datadir}/polkit-1/actions/org.selinux.policy
%{_datadir}/polkit-1/actions/org.selinux.config.policy
%{_datadir}/system-config-selinux/selinux_server.py

%changelog
