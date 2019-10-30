#
# spec file for package google-compute-engine
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define setup_version 20190801.0

Name:           google-compute-engine
Version:        20190801
Release:        0
Summary:        GCE Instance Initialization
License:        Apache-2.0
Group:          System/Daemons
Url:            https://github.com/GoogleCloudPlatform/compute-image-packages
Source0:        compute-image-packages-%{version}.tar.gz
Source7:        google-compute-engine-rpmlintrc
Source8:        baselibs.conf
Source9:        google-optimize-local-ssd.service
Source10:       google-set-multiqueue.service
Patch1:         gcei-hide-py-deps.patch
Patch2:         gcei-scripts-after-reg.patch
Patch3:         gcei-set-run_dir.patch
# see: https://github.com/GoogleCloudPlatform/compute-image-packages/issues/830
Patch4:         gcei-link-boost_regex.patch
# see: https://github.com/GoogleCloudPlatform/compute-image-packages/issues/831
Patch5:         gcei-normalize-python-version.patch
Patch6:         gcei_disableipv6.patch
# see: https://github.com/GoogleCloudPlatform/compute-image-packages/issues/862
Patch7:         gcei-waitlimit-dns.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Google Compute Engine instance code.

%package init
Summary:        GCE Instance Initialization
Group:          System/Daemons
Requires:       google-compute-engine-oslogin == %{version}
%if 0%{?suse_version} && 0%{?suse_version} > 1315
Requires:       python3-distro
Requires:       python3-setuptools
%else
Requires:       python-setuptools
%endif
Requires:       systemd
%{?systemd_requires}
%if 0%{?suse_version} && 0%{?suse_version} > 1315
BuildRequires:  python3-distro
BuildRequires:  python3-setuptools
%else
BuildRequires:  python-setuptools
%endif
BuildArch:      noarch
%if 0%{?suse_version} && 0%{?suse_version} <= 1315
# These packages were not released in SLE 15 and later, thus no conflict needed
Conflicts:      google-startup-scripts
Conflicts:      google-daemon
Conflicts:      gcimagebundle
%endif

%description init
Initialization code for Google Compute Engine instances.

%package oslogin
Summary:        OS Login Functionality for Google Compute Engine
Group:          System/Daemons

Requires:       pam
Requires(post): openssh
Requires(post): glibc
%if 0%{?suse_version} && 0%{?suse_version} <= 1315
BuildRequires:  boost-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  libcurl-devel
BuildRequires:  libjson-c-devel
BuildRequires:  make
BuildRequires:  pam-devel

%description oslogin
Libraries and scripts  to enable OS Login functionality for
Google Compute Engine. Modifies sshd, nsswitch, and sshd_pam configurations.


%prep
%setup -q -n compute-image-packages-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%if 0%{?suse_version} <= 1315
%patch4 -p1
%endif
%patch5 -p1
%patch6 -p1
%patch7
find -name "*.py" | xargs sed -i 'sm#!/usr/bin/pythonmm'
cp %{SOURCE9} google-optimize-local-ssd.service
cp %{SOURCE10} google-set-multiqueue.service

%build
cd packages/python-google-compute-engine
%if 0%{?suse_version} && 0%{?suse_version} > 1315
python3 setup.py build
%else
python setup.py build
%endif
cd ..
pushd google-compute-engine-oslogin
%if 0%{?suse_version} && 0%{?suse_version} > 1315
make %{?_smp_mflags}
%else
make %{?_smp_mflags} LIBS='-lcurl -ljson-c -lboost_regex'
%endif
popd

%install
cd packages/python-google-compute-engine
%if 0%{?suse_version} && 0%{?suse_version} > 1315
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%else
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
%endif
cd ..
mkdir -p %{buildroot}%{_bindir}
cp google-compute-engine/src/usr/bin/* %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sbindir}
# Init
mkdir -p %{buildroot}%{_unitdir}
cp ../google-optimize-local-ssd.service %{buildroot}%{_unitdir}
cp ../google-set-multiqueue.service %{buildroot}%{_unitdir}
cp google-compute-engine/src/lib/systemd/system/*.service %{buildroot}%{_unitdir}
for srv_name in %{buildroot}%{_unitdir}/*.service; do rc_name=$(basename -s '.service' $srv_name); ln -s service %{buildroot}%{_sbindir}/rc$rc_name; done
# Sysconfig
mkdir -p %{buildroot}%{_sysconfdir}/sysctl.d
cp google-compute-engine/src/etc/sysctl.d/11-gce-network-security.conf %{buildroot}%{_sysconfdir}/sysctl.d
# udev
mkdir -p %{buildroot}/usr/lib/udev/rules.d
cp google-compute-engine/src/lib/udev/rules.d/* %{buildroot}/usr/lib/udev/rules.d
# syslog
mkdir -p %{buildroot}/%{_sysconfdir}/rsyslog.d
cp google-compute-engine/src/etc/rsyslog.d/* %{buildroot}/%{_sysconfdir}/rsyslog.d
# oslogin
pushd google-compute-engine-oslogin
make install DESTDIR=%{buildroot} LIBDIR=/%{_libdir} PAMDIR=/%{_lib}/security
popd
# kernel module blacklist
mkdir -p %{buildroot}/%{_sysconfdir}/modprobe.d
cp google-compute-engine/src/etc/modprobe.d/gce-blacklist.conf  %{buildroot}/%{_sysconfdir}/modprobe.d/

%pre init
    if [ -f /usr/lib/systemd/system/google-ip-forwarding-daemon.service ]; then
        systemctl stop --no-block google-ip-forwarding-daemon
        systemctl disable google-ip-forwarding-daemon.service
    fi
    if [ -f /usr/lib/systemd/system/google-network-setup.service ]; then
        systemctl stop --no-block google-network-setup
        systemctl disable google-network-setup.service
    fi
    %service_add_pre google-accounts-daemon.service google-clock-skew-daemon.service google-instance-setup.service google-network-daemon.service google-optimize-local-ssd.service google-set-multiqueue.service google-shutdown-scripts.service google-startup-scripts.service

%post init
    %service_add_post google-accounts-daemon.service google-clock-skew-daemon.service google-instance-setup.service google-network-daemon.service google-optimize-local-ssd.service google-set-multiqueue.service google-shutdown-scripts.service google-startup-scripts.service
    if [ "$1" == "2" ] && ! [ -e /.buildenv ]; then
        # "$1" == "2" means the package is being upgraded
        # ./buildenv is only present during package builds
        systemctl enable google-network-daemon.service
        systemctl start google-network-daemon.service
    fi

%post oslogin 
/sbin/ldconfig

%preun init
    %service_del_preun -f google-accounts-daemon.service google-clock-skew-daemon.service google-instance-setup.service google-network-daemon.service google-optimize-local-ssd.service google-set-multiqueue.service google-shutdown-scripts.service google-startup-scripts.service

%postun init
    %service_del_postun -f google-accounts-daemon.service google-clock-skew-daemon.service google-instance-setup.service google-network-daemon.service google-optimize-local-ssd.service google-set-multiqueue.service google-shutdown-scripts.service google-startup-scripts.service

%postun oslogin 
/sbin/ldconfig

%files init
%defattr(0644,root,root,0755)
%doc CONTRIB.md README.md
%license LICENSE 
%if 0%{?suse_version} && 0%{?suse_version} > 1315
%dir %{python3_sitelib}/google_compute_engine
%dir %{python3_sitelib}/google_compute_engine-%{setup_version}-py%{py3_ver}.egg-info
%else
%dir %{python_sitelib}/google_compute_engine
%dir %{python_sitelib}/google_compute_engine-%{setup_version}-py%{py_ver}.egg-info
%endif
%exclude %{_bindir}/google_oslogin_control
%exclude %{_bindir}/google_authorized_keys
%exclude %{_bindir}/google_oslogin_nss_cache
%attr(0755,root,root) %{_bindir}/*
%if 0%{?suse_version} && 0%{?suse_version} > 1315
%{_sbindir}/*
%else
%attr(0755,root,root) %{_sbindir}/*
%endif
%if 0%{?suse_version} && 0%{?suse_version} > 1315
%{python3_sitelib}/google_compute_engine/*
%else
%{python_sitelib}/google_compute_engine/*
%endif
%if 0%{?suse_version} && 0%{?suse_version} > 1315
%{python3_sitelib}/google_compute_engine-%{setup_version}-py%{py3_ver}.egg-info/*
%else
%{python_sitelib}/google_compute_engine-%{setup_version}-py%{py_ver}.egg-info/*
%endif
%{_unitdir}/*.service
%config %{_sysconfdir}/sysctl.d/*
%dir /usr/lib/systemd
%dir /usr/lib/udev
%dir /usr/lib/udev/rules.d
/usr/lib/udev/rules.d/*
%dir %{_sysconfdir}/rsyslog.d
%dir %{_sysconfdir}/modprobe.d
%config %{_sysconfdir}/rsyslog.d/*
%config %{_sysconfdir}/modprobe.d/gce-blacklist.conf

%files oslogin
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/google_oslogin_control
%attr(0755,root,root) %{_bindir}/google_authorized_keys
%attr(0755,root,root) %{_bindir}/google_oslogin_nss_cache
/%{_mandir}/man8/*
/%{_lib}/security/*
/%{_libdir}/libnss*

%changelog
