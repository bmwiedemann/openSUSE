#
# spec file for package permissions
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


Name:           permissions
Version:        1699_20250120
Release:        0
Summary:        SUSE Linux Default Permissions
# Maintained in github by the security team.
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            http://github.com/openSUSE/permissions
Source:         permissions-%{version}.tar.xz
Source2:        permissions.rpmlintrc
BuildRequires:  gcc-c++
BuildRequires:  libacl-devel
BuildRequires:  libcap-devel
BuildRequires:  libcap-progs
BuildRequires:  meson
BuildRequires:  python-rpm-macros
BuildRequires:  tclap
# test suite
BuildRequires:  python3-base
BuildRequires:  acl
BuildRequires:  system-user-bin
BuildRequires:  system-user-nobody
Requires:       permctl
Requires:       permissions-config
Provides:       aaa_base:%{_datadir}/permissions

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
# Fix shebang in scripts: Remove dependency on /usr/bin/python3,
# making scripts to depends on the real python3 binary, not the link.
# (bsc#1212476)
for f in %{buildroot}/usr/lib/zypp/plugins/commit/*
do
  [ -f $f ] && sed -i "1s@#\!.*python.*@#\!$(realpath %__python3)@" $f
done

%check
# will fail on qemu with  unshare: unshare failed: Invalid argument
#%%if !0%{?qemu_user_space_build}
#%tests/regtest.py --skip-build %_vpath_builddir >/dev/null
#%%endif

%description
File and directory permission settings depending on the local security
settings. The local security setting ("easy", "secure", or "paranoid") can be
configured in /etc/sysconfig/security.

This package does not contain files, it just requires the necessary packages.

%files

%package config
Summary:        SUSE Linux Default Permissions config files
Group:          Productivity/Security
Requires(post): %fillup_prereq
Requires(post): permctl
#!BuildIgnore:  group(trusted)
Requires(pre):  group(trusted)
Obsoletes:      permissions-doc <= %{version}
BuildArch:      noarch

%description config
The actual permissions configuration files, /usr/share/permissions/permission.*.

%files config
%defattr(644, root, root, 755)
%dir %{_datadir}/permissions
%dir %{_datadir}/permissions/permissions.d
%{_datadir}/permissions/permissions
%{_datadir}/permissions/permissions.easy
%{_datadir}/permissions/permissions.secure
%{_datadir}/permissions/permissions.paranoid
%{_datadir}/permissions/variables.conf
%config(noreplace) %{_sysconfdir}/permissions.local
%{_fillupdir}/sysconfig.security
%{_mandir}/man5/permissions.5%{ext_man}

%post config
%{fillup_only -n security}
# apply all potentially changed permissions
%{_bindir}/permctl --system || :

%package -n permctl
Summary:        SUSE Linux Default Permissions tool
Group:          Productivity/Security
Provides:       chkstat = %version-%release
Obsoletes:      chkstat < %version-%release

%description -n permctl
Tool to check and set file permissions.

%files -n permctl
%{_bindir}/chkstat
%{_bindir}/permctl
%{_mandir}/man8/permctl.8%{ext_man}
%{_rpmconfigdir}/macros.d/macros.*

%package -n permissions-zypp-plugin
BuildArch:      noarch
Requires:       permissions = %{version}
Requires:       python3-zypp-plugin
Requires:       libzypp(plugin:commit) = 1
Summary:        A zypper commit plugin for calling permctl
Group:          Productivity/Security

%description -n permissions-zypp-plugin
This package contains a plugin for zypper that calls `permctl --system` after
new packages have been installed. This is helpful for maintaining custom
entries in /etc/permissions.local.

%files -n permissions-zypp-plugin
%dir /usr/lib/zypp
%dir /usr/lib/zypp/plugins
%dir /usr/lib/zypp/plugins/commit
/usr/lib/zypp/plugins/commit/permissions.py

%changelog
