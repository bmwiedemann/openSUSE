#
# spec file for package numad
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           numad
Url:            http://git.fedorahosted.org/git/numad.git
Summary:        Userspace daemon that automatically binds workloads to NUMA nodes
License:        LGPL-2.1
Group:          System/Daemons
Version:        0.5.20130522
Release:        0
Source0:        numad-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Patch1:         mainline-sysfs-paths.patch
Patch2:         numad-sbindir.patch
Patch3:         numad-opensuse-init.patch
Patch4:         numad-versioning.patch
Patch5:         numad-rpm-opt-flags.patch
Patch6:         numad-opensuse-systemd.patch
Patch7:         numad-systemd-simple-type.patch

%if 0%{?suse_version} > 1140
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%define has_systemd 1
%endif

%description
numad is a userspace daemon that monitors NUMA usage and resource usage
and attempts to configure workloads using cpusets to use a subset of
CPUs and memory nodes to maximise the number local memory access for
best performance. Alternatively, it can be used to give hints as to how
workloads should be manually bound to CPUs and memory nodes. This daemon
is primarily intended for scenarios where there are multiple processes
each which fit within a NUMA node. Examples of such configurations are
virtual machine instances where each VM is smaller than a NUMA node
or running multiple JVMs where each instance fits within a NUMA node.
If the workload is one process that spans two or more nodes such as
a large database server or a single JVM instance then numad is likely
to regress performance.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1

%build
make OPT_CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
%makeinstall prefix=$RPM_BUILD_ROOT%{_prefix} install
gzip $RPM_BUILD_ROOT%{_mandir}/man8/numad.8
%{__install} -D -m 644 numad.conf $RPM_BUILD_ROOT/etc/numad.conf
%if 0%{?has_systemd}
install -D -m 0644 numad.service %{buildroot}%{_unitdir}/numad.service
ln -sf ../../usr/sbin/service $RPM_BUILD_ROOT/usr/sbin/rcnumad
%endif
%if 0%{suse_version} < 1230
%{__install} -d $RPM_BUILD_ROOT%{_sysconfdir}/init.d
%{__install} -m 744 numad.init $RPM_BUILD_ROOT%{_sysconfdir}/init.d/numad
ln -sf ../../etc/init.d/numad $RPM_BUILD_ROOT/usr/sbin/rcnumad
%endif

%files
%defattr(-,root,root)
%{_sbindir}/numad
%{_sbindir}/rcnumad
%{_mandir}/man8/numad.8.gz
%config /etc/numad.conf
%if 0%{?has_systemd}
%{_unitdir}/numad.service
%endif
%if 0%{suse_version} < 1230
%config /etc/init.d/numad
%endif

%pre
%if 0%{?has_systemd}
%service_add_pre numad.service
%endif

%preun
%if 0%{?has_systemd}
%service_del_preun numad.service
%else
%stop_on_removal numad
%endif

%post
%if 0%{?has_systemd}
%service_add_post numad.service
%endif

%postun
%if 0%{?has_systemd}
%service_del_postun numad.service
%else
%restart_on_update numad
%insserv_cleanup
%endif

%changelog
