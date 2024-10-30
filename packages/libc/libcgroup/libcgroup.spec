#
# spec file for package libcgroup
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

%define lname	libcgroup3
Name:           libcgroup
Version:        3.1.0
Release:        0
Summary:        Tools and libraries to control and monitor control groups
License:        LGPL-2.1-only
Url:            https://github.com/libcgroup/libcgroup
Source:         https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source2:        libcgroup.keyring
Source3:        sysconfig.cgred
Source4:        cgrules.service
Source5:        cgconfig.service
Source6:        %{name}-rpmlintrc
Source7:        system-group-cgroup.conf
Source99:       baselibs.conf
Patch0:         cgroup-directory.patch
Patch1:         Syntax-fixes-for-man-pages.patch
Patch2:         pam_cgroup-Revert-broken-cache-usage.patch
Patch3:         template-doc.patch
Patch4:         oldfashion_init.patch
Patch5:         groups.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  permissions
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(pam)
BuildRequires:  pkgconfig(pkgconf)
BuildRequires:  pkgconfig(pkg-config)
BuildRequires:  sysuser-tools
%if ! %{defined _pam_moduledir}
%define _pam_moduledir /%{_lib}/security
%endif
%define add_optflags(a:f:t:p:w:W:d:g:O:A:C:D:E:H:i:M:n:P:U:u:l:s:X:B:I:L:b:V:m:x:c:S:E:o:v:) \
%global optflags %{optflags} %{**}

%description
Control groups infrastructure. The tools and library help manipulate, control,
administrate and monitor control groups and the associated controllers.

%package -n %{lname}
Summary:        Control groups management library
%description -n %{lname}

The shared library libcgroup 3.1.0 its self.

%package devel
Summary:        Control groups management tools devel package
Requires:       %{lname} = %{version}-%{release}

%description devel
This package contains the headers needed to build against
the libcgroup library in its ABI version 3 form.

%package tools
Summary:        Control groups management tools
# Added for openSUSE 12.3 to aid the solver.
Provides:       libcgroup1:%{_bindir}/cgexec
Provides:       group(cgred)
Requires(pre):  permissions
Recommends:     %{name}-pam
%sysusers_requires

%description tools
NOTE - this release is not guaranteed to be backward compatible with previous releases!

Libcgroup v3.1.0 adds systemd support to the libcgroup library.  Users can now create
systemd scopes via the libcgroup C APIs, command line tools, and (experimental) Python
bindings.  These scopes can be "delegated" (or not), which is systemd parlance for a
cgroup hierarchy that is being managed by another entity.  Systemd will not modify
settings or processes within a delegated hierarchy.

Note that libcgroup v3.1.0 is still capable of modifying cgroups and processes anywhere
in the cgroup hierarchy, including the root cgroup and its children (which are owned
by systemd).  Modifying cgroups and processes owned by systemd is a violation of the
cgroup single-writer rule, and systemd reserves the right to undo any changes made by
other processes.  The libcgroup team strongly discourages modifying systemd-managed
cgroups - especially on production systems - but it can be useful during prototyping
and on experimental systems.

The initial release of the cgroups implementation was in Linux 2.6.24.  Over time,
various cgroup controllers have been added to  allow  the  management  of  various
types of resources.  However, the development of these controllers was largely
uncoordinated, with the result that many inconsistencies arose between controllers and
management of the cgroup hierarchies became rather complex.

%package pam
Summary:        A Pluggable Authentication Module for libcgroup
Provides:       libcgroup-tools:%{_pam_moduledir}/pam_cgroup.so
Requires:       pam

%description pam
Linux-PAM module, which allows administrators to classify the user's login
processes to pre-configured control group.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4
%patch -P5

%build
%add_optflags -D_GNU_SOURCE
%configure \
    --disable-silent-rules \
    --enable-cgred-socket=/run/cgred.socket \
    --enable-opaque-hierarchy="name=systemd" \
    --enable-pam-module-dir=%_pam_moduledir
%make_build

%install
%make_install DESTDIR=%{buildroot}
%sysusers_generate_pre %{S:7} cgred system-group-cgroup.conf
chmod u-s %{buildroot}%{_bindir}/cgexec
mkdir -p %{buildroot}%{_datadir}/permissions/permissions.d
mkdir -p %{buildroot}%{_sysconfdir}/cgconfig.d
mkdir -p %{buildroot}%{_sysusersdir}
pushd samples/config/
    install -m 644 cgconfig.conf     %{buildroot}%{_sysconfdir}
    install -m 644 cgrules.conf      %{buildroot}%{_sysconfdir}
    install -m 644 cgsnapshot_*.conf %{buildroot}%{_sysconfdir}
popd
mkdir -p %{buildroot}%{_unitdir}
    install -m 644 %{S:4} %{buildroot}%{_unitdir}/
    install -m 644 %{S:5} %{buildroot}%{_unitdir}/
    install -m 644 %{S:7} %{buildroot}%{_sysusersdir}/
find %{buildroot} -type f -a \( -name "*.la" -o -name "*.a" \) -delete -print
chmod u-s %{buildroot}/%{_bindir}/cgexec

(cat > %{buildroot}%{_datadir}/permissions/permissions.d/libcgroup)<<-'EOF'
	%{_bindir}/cgexec			root:cgred	2755
EOF

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%preun tools
%service_del_preun cgconfig.service
%service_del_preun cgrules.service

%postun tools
%service_del_postun cgconfig.service
%service_del_postun cgrules.service

%pre tools -f cgred.pre
%service_add_pre cgconfig.service
%service_add_pre cgrules.service

%post tools
%service_add_post cgconfig.service
%service_add_post cgrules.service
%set_permissions %{_bindir}/cgexec

%verifyscript tools
%verify_permissions -e %{_bindir}/cgexec

%files -n %{lname}
%license COPYING
%{_libdir}/libcgroup.so.*

%files tools
%license COPYING
%doc README
%doc README_daemon
%doc README_systemd
%config %{_sysconfdir}/*.conf
%dir %{_sysconfdir}/cgconfig.d
%dir %{_datadir}/permissions/permissions.d/
%{_datadir}/permissions/permissions.d/libcgroup
%{_unitdir}/*.service
%{_bindir}/cg[^e]*
%attr(2755,root,cgred) %{_bindir}/cgexec
%{_sbindir}/cg*
%{_bindir}/ls*
%{_bindir}/libcgroup_systemd_idle_thread
%{_mandir}/man[158]/*
%{_sysusersdir}/system-group-cgroup.conf

%files pam
%license COPYING
%{_pam_moduledir}/pam_cgroup.so

%files devel
%defattr(-,root,root)
%{_libdir}/libcgroup.so
%{_includedir}/libcgroup.h
%dir %{_includedir}/libcgroup
%{_includedir}/libcgroup/*.h
%{_libdir}/pkgconfig/libcgroup.pc

%changelog
