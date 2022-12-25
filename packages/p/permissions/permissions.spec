#
# spec file for package permissions
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


%define VERSION_DATE 20221220

Name:           permissions
Version:        %{suse_version}_%{VERSION_DATE}
Release:        0
Summary:        SUSE Linux Default Permissions
# Maintained in github by the security team.
License:        GPL-2.0-or-later
Group:          Productivity/Security
URL:            http://github.com/openSUSE/permissions
Source:         permissions-%{VERSION_DATE}.tar.xz
Source1:        fix_version.sh
Source2:        permissions.rpmlintrc
BuildRequires:  gcc-c++
BuildRequires:  libcap-devel
BuildRequires:  libcap-progs
BuildRequires:  tclap
# test suite
BuildRequires:  python3-base
Requires:       chkstat
Requires:       permissions-config
Provides:       aaa_base:%{_datadir}/permissions

%prep
%autosetup -n permissions-%{VERSION_DATE}

%build
make %{?_smp_mflags} CXXFLAGS="%{optflags}"

%install
%make_install fillupdir=%{_fillupdir}

%check
# will fail on qemu with  unshare: unshare failed: Invalid argument
%if !0%{?qemu_user_space_build}
tests/regtest.py --skip-make > /dev/null
%endif

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
Requires(post): chkstat
#!BuildIgnore:  group(trusted)
Requires(pre):  group(trusted)
Obsoletes:      permissions-doc <= %{suse_version}_%{VERSION_DATE}
BuildArch:      noarch

%description config
The actual permissions configuration files, /usr/share/permissions/permission.*.

%files config
%defattr(644, root, root, 755)
%dir %{_datadir}/permissions
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
%{_bindir}/chkstat --system || :

%package -n chkstat
Summary:        SUSE Linux Default Permissions tool
Group:          Productivity/Security

%description -n chkstat
Tool to check and set file permissions.

%files -n chkstat
%{_bindir}/chkstat
%{_mandir}/man8/chkstat.8%{ext_man}

%package -n permissions-zypp-plugin
BuildArch:      noarch
Requires:       permissions = %{version}
Requires:       python3-zypp-plugin
Requires:       libzypp(plugin:commit) = 1
Summary:        A zypper commit plugin for calling chkstat
Group:          Productivity/Security

%description -n permissions-zypp-plugin
This package contains a plugin for zypper that calls `chkstat --system` after
new packages have been installed. This is helpful for maintaining custom
entries in /etc/permissions.local.

%files -n permissions-zypp-plugin
%dir /usr/lib/zypp
%dir /usr/lib/zypp/plugins
%dir /usr/lib/zypp/plugins/commit
/usr/lib/zypp/plugins/commit/permissions.py

%changelog
