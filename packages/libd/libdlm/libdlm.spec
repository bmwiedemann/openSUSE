#
# spec file for package libdlm
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%if 0%{?suse_version}
%define _libexecdir %{_libdir}
%endif
%if 0%{?fedora_version} || 0%{?centos_version} || 0%{?rhel_version}
%define pkg_group System Environment/Daemons
%else
%define pkg_group Productivity/Clustering/HA
%endif

Name:           libdlm
Summary:        Application interface to the kernel's distributed lock manager
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          Productivity/Clustering/HA
Version:        4.3.0
Release:        0
URL:            https://pagure.io/dlm/
Source:         https://pagure.io/dlm/archive/dlm-%{version}/dlm-dlm-%{version}.tar.gz

##################
#upstream patch
# n/a

# suse special patch
Patch1001:      0001-makefile-for-diff-arch.patch
Patch1002:      0002-remove-sd-notify.patch
Patch1003:      0003-bnc#874705-nodes-without-quorum.patch
Patch1004:      0004-man-dlm.conf-add-note-that-the-file-is-not-creat.patch

##################

BuildRequires:  fdupes
BuildRequires:  glib2-devel
BuildRequires:  pkgconfig(corosync) >= 3.1.0
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  pkgconfig(pacemaker)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
Recommends:     dlm-kmp

%description
Libraries and tools that allow applications, particularly filesystems
like OCFS2, to interface with the in-kernel distributed lock manager.

%package -n     libdlm3
Summary:        Application interface to the kernel's distributed lock manager
# libdlm2 (openSUSE 11.2) also contained libdlm*.so.3
License:        GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
Obsoletes:      libdlm2 < 2.99
Conflicts:      libdlm2 < 2.99

%description -n libdlm3
Libraries and tools that allow applications, particularly filesystems
like OCFS2, to interface with the in-kernel distributed lock manager.

%package        devel
Summary:        Development files for the kernel's distributed lock manager
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libdlm3 = %{version}

%description devel
Libraries and tools that allow applications, particularly filesystems
like OCFS2, to interface with the in-kernel distributed lock manager.

%prep
%autosetup -p1 -n dlm-dlm-%{version}

%build
echo "V_%version { global: *; };" >dlm.ver
export CFLAGS="%optflags"
export LDFLAGS="-Wl,--version-script=$PWD/dlm.ver"
make all UDEVDIR="%{_udevrulesdir}"
###########################################################

%install
###########################################################
%make_install UDEVDIR="%{_udevrulesdir}"
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/packages/libdlm-%{version}

install -Dm 0644 init/dlm.service $RPM_BUILD_ROOT%{_unitdir}/dlm.service
install -Dm 0644 init/dlm.sysconfig $RPM_BUILD_ROOT%{_fillupdir}/sysconfig.dlm
%fdupes %{buildroot}/%{_prefix}

###########################################################

%post
%fillup_only -n dlm
%{?udev_rules_update}
%service_add_post dlm.service

%preun
%service_del_preun dlm.service

%pre
%service_add_pre dlm.service

%postun
%service_del_postun dlm.service

%post   -n libdlm3 -p /sbin/ldconfig
%postun -n libdlm3 -p /sbin/ldconfig

%files
%dir %{_datadir}/doc/packages/libdlm-%{version}
%{_udevrulesdir}/51-dlm.rules
%{_sbindir}/dlm_controld
%{_sbindir}/dlm_stonith
%{_sbindir}/dlm_tool
%{_datadir}/man/man8/*.gz
%{_datadir}/man/man3/*.gz
%{_datadir}/man/man5/*.gz
%{_datadir}/doc/packages/libdlm-%{version}
%{_unitdir}/dlm.service
%{_fillupdir}/sysconfig.dlm

%files -n libdlm3
%{_libdir}/libdlm.so.*
%{_libdir}/libdlm_lt.so.*
%{_libdir}/libdlmcontrol.so.*

%files devel
%{_libdir}/libdlm*.so
%{_libdir}/pkgconfig/libdlm.pc
%{_libdir}/pkgconfig/libdlm_lt.pc
%{_libdir}/pkgconfig/libdlmcontrol.pc
%{_includedir}/libdlm.h
%{_includedir}/libdlmcontrol.h

%changelog
