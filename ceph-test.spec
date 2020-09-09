#
# spec file for package ceph
#
# Copyright (C) 2004-2019 The Ceph Project Developers. See COPYING file
# at the top-level directory of this distribution and at
# https://github.com/ceph/ceph/blob/master/COPYING
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon.
#
# This file is under the GNU Lesser General Public License, version 2.1
#
# Please submit bugfixes or comments via http://tracker.ceph.com/
#

#################################################################################
# conditional build section
#
# please read http://rpm.org/user_doc/conditional_builds.html for explanation of
# bcond syntax!
#################################################################################
%bcond_with make_check
%bcond_with cmake_verbose_logging
%bcond_without ceph_test_package
%bcond_with minimal_debugging_information
%ifarch s390 s390x
%bcond_with tcmalloc
%else
%bcond_without tcmalloc
%endif
%if 0%{?fedora} || 0%{?rhel}
%bcond_without selinux
%if 0%{?rhel} >= 8
%bcond_with cephfs_java
%else
%bcond_without cephfs_java
%endif
%bcond_without amqp_endpoint
%bcond_without kafka_endpoint
%bcond_without lttng
%bcond_without libradosstriper
%bcond_without ocf
%global _remote_tarball_prefix https://download.ceph.com/tarballs/
%endif
%if 0%{?suse_version}
%bcond_with amqp_endpoint
%bcond_with cephfs_java
%bcond_with kafka_endpoint
%bcond_with libradosstriper
%ifarch x86_64 aarch64 ppc64le
%bcond_without lttng
%else
%bcond_with lttng
%endif
%bcond_with ocf
%bcond_with selinux
#Compat macro for _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
%global _fillupdir /var/adm/fillup-templates
%endif
%endif
%bcond_with seastar
%if 0%{?fedora} || 0%{?suse_version} >= 1500
# distros that ship cmd2 and/or colorama
%bcond_without cephfs_shell
%else
# distros that do _not_ ship cmd2/colorama
%bcond_with cephfs_shell
%endif
%if 0%{?fedora} || 0%{?suse_version} || 0%{?rhel} >= 8
%global weak_deps 1
%endif
%if %{with selinux}
# get selinux policy version
# Force 0.0.0 policy version for centos builds to avoid repository sync issues between rhel and centos
%if 0%{?centos}
%global _selinux_policy_version 0.0.0
%else
%{!?_selinux_policy_version: %global _selinux_policy_version 0.0.0}
%endif
%endif

%{!?_udevrulesdir: %global _udevrulesdir /lib/udev/rules.d}
%{!?tmpfiles_create: %global tmpfiles_create systemd-tmpfiles --create}
%{!?python3_pkgversion: %global python3_pkgversion 3}
%{!?python3_version_nodots: %global python3_version_nodots 3}
%{!?python3_version: %global python3_version 3}

# disable dwz which compresses the debuginfo
%global _find_debuginfo_dwz_opts %{nil}

#################################################################################
# main package definition
#################################################################################
Name: ceph-test
Version: 16.0.0.4863+g5d95d9d41d
Release: 0%{?dist}
%if 0%{?fedora} || 0%{?rhel}
Epoch: 2
%endif

# define _epoch_prefix macro which will expand to the empty string if epoch is
# undefined
%global _epoch_prefix %{?epoch:%{epoch}:}

Summary: Ceph benchmarks and test tools
License: LGPL-2.1 and LGPL-3.0 and CC-BY-SA-3.0 and GPL-2.0 and BSL-1.0 and BSD-3-Clause and MIT
%if 0%{?suse_version}
Group: System/Filesystems
%endif
URL: http://ceph.com/
Source0: %{?_remote_tarball_prefix}ceph-16.0.0-4863-g5d95d9d41d.tar.bz2
%if 0%{?suse_version}
Source96: checkin.sh
Source97: README-checkin.txt
Source98: README-ceph-test.txt
Source99: ceph-rpmlintrc
# _insert_obs_source_lines_here
ExclusiveArch: x86_64
%endif
#################################################################################
# dependencies that apply across all distro families
#################################################################################




Requires: ceph-common
Requires: xmlstarlet
Requires: jq
Requires: socat
Requires(post):	binutils
%if 0%{with cephfs_java}
BuildRequires:	java-devel
BuildRequires:	sharutils
%endif
%if 0%{with selinux}
BuildRequires:	checkpolicy
BuildRequires:	selinux-policy-devel
%endif
BuildRequires:	gperf
BuildRequires:  cmake > 3.5
BuildRequires:	cryptsetup
BuildRequires:	fuse-devel
%if 0%{with seastar}
BuildRequires:	gcc-toolset-9-gcc-c++ >= 9.2.1-2.3
%else
BuildRequires:	gcc-c++
%endif
BuildRequires:	gdbm
%if 0%{with tcmalloc}
%if 0%{?fedora} || 0%{?rhel}
BuildRequires:	gperftools-devel >= 2.6.1
%endif
%if 0%{?suse_version}
BuildRequires:	gperftools-devel >= 2.4
%endif
%endif
BuildRequires:	leveldb-devel > 1.2
BuildRequires:	libaio-devel
BuildRequires:	libblkid-devel >= 2.17
BuildRequires:	libcurl-devel
BuildRequires:	libcap-ng-devel
BuildRequires:	pkgconfig(libudev)
BuildRequires:	libnl3-devel
BuildRequires:	liboath-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	make
BuildRequires:	ncurses-devel
BuildRequires:	parted
BuildRequires:	patch
BuildRequires:	perl
BuildRequires:	pkgconfig
BuildRequires:  procps
BuildRequires:	python%{python3_pkgversion}
BuildRequires:	python%{python3_pkgversion}-devel
BuildRequires:	snappy-devel
BuildRequires:	sudo
BuildRequires:	pkgconfig(udev)
BuildRequires:	util-linux
BuildRequires:	valgrind-devel
BuildRequires:	which
BuildRequires:	xfsprogs
BuildRequires:	xfsprogs-devel
BuildRequires:	xmlstarlet
BuildRequires:	yasm
%if 0%{with amqp_endpoint}
BuildRequires:  librabbitmq-devel
%endif
%if 0%{with kafka_endpoint}
BuildRequires:  librdkafka-devel
%endif
%if 0%{with make_check}
BuildRequires:  jq
BuildRequires:	libuuid-devel
BuildRequires:	python%{python3_pkgversion}-bcrypt
BuildRequires:	python%{python3_pkgversion}-nose
BuildRequires:	python%{python3_pkgversion}-pecan
BuildRequires:	python%{python3_pkgversion}-requests
BuildRequires:	python%{python3_pkgversion}-dateutil
BuildRequires:	python%{python3_pkgversion}-virtualenv
BuildRequires:	python%{python3_pkgversion}-coverage
BuildRequires:	python%{python3_pkgversion}-pyOpenSSL
BuildRequires:	socat
%endif
%if 0%{with seastar}
BuildRequires:  c-ares-devel
BuildRequires:  gnutls-devel
BuildRequires:  hwloc-devel
BuildRequires:  libpciaccess-devel
BuildRequires:  lksctp-tools-devel
BuildRequires:  protobuf-devel
BuildRequires:  ragel
BuildRequires:  systemtap-sdt-devel
BuildRequires:  yaml-cpp-devel
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  fmt-devel
BuildRequires:  libubsan
BuildRequires:  libasan
BuildRequires:  libatomic
%if 0%{with seastar}
BuildRequires:  gcc-toolset-9-annobin
BuildRequires:  gcc-toolset-9-libubsan-devel
BuildRequires:  gcc-toolset-9-libasan-devel
BuildRequires:  gcc-toolset-9-libatomic-devel
%endif
%endif
%endif
#################################################################################
# distro-conditional dependencies
#################################################################################
%if 0%{?suse_version}
BuildRequires:  pkgconfig(systemd)
BuildRequires:	systemd-rpm-macros
%{?systemd_requires}
PreReq:		%fillup_prereq
BuildRequires:	fdupes
BuildRequires:	net-tools
BuildRequires:	libbz2-devel
BuildRequires:	mozilla-nss-devel
BuildRequires:	keyutils-devel
BuildRequires:  libopenssl-devel
BuildRequires:  lsb-release
BuildRequires:  openldap2-devel
#BuildRequires:  krb5
#BuildRequires:  krb5-devel
BuildRequires:  cunit-devel
BuildRequires:	python%{python3_pkgversion}-setuptools
BuildRequires:	python%{python3_pkgversion}-Cython
BuildRequires:	python%{python3_pkgversion}-PrettyTable
BuildRequires:	python%{python3_pkgversion}-Sphinx
BuildRequires:  rdma-core-devel
BuildRequires:	liblz4-devel >= 1.7
# for prometheus-alerts
BuildRequires:  golang-github-prometheus-prometheus
%endif
%if 0%{?fedora} || 0%{?rhel}

BuildRequires:  boost-random
BuildRequires:	nss-devel
BuildRequires:	keyutils-libs-devel
BuildRequires:	libibverbs-devel
BuildRequires:  librdmacm-devel
BuildRequires:  openldap-devel
#BuildRequires:  krb5-devel
BuildRequires:  openssl-devel
BuildRequires:  CUnit-devel
BuildRequires:  redhat-lsb-core
BuildRequires:	python%{python3_pkgversion}-devel
BuildRequires:	python%{python3_pkgversion}-setuptools
BuildRequires:	python%{python3_pkgversion}-Cython
BuildRequires:	python%{python3_pkgversion}-prettytable
BuildRequires:	python%{python3_pkgversion}-sphinx
BuildRequires:	lz4-devel >= 1.7
%endif
# distro-conditional make check dependencies
%if 0%{with make_check}
%if 0%{?fedora} || 0%{?rhel}
BuildRequires:	libtool-ltdl-devel
BuildRequires:	xmlsec1
BuildRequires:	xmlsec1-devel
%ifarch x86_64
BuildRequires:	xmlsec1-nss
%endif
BuildRequires:	xmlsec1-openssl
BuildRequires:	xmlsec1-openssl-devel
BuildRequires:	python%{python3_pkgversion}-cherrypy
BuildRequires:	python%{python3_pkgversion}-jwt
BuildRequires:	python%{python3_pkgversion}-routes
BuildRequires:	python%{python3_pkgversion}-scipy
BuildRequires:	python%{python3_pkgversion}-werkzeug
BuildRequires:	python%{python3_pkgversion}-pyOpenSSL
%endif
%if 0%{?suse_version}
BuildRequires:	libxmlsec1-1
BuildRequires:	libxmlsec1-nss1
BuildRequires:	libxmlsec1-openssl1
BuildRequires:	python%{python3_pkgversion}-CherryPy
BuildRequires:	python%{python3_pkgversion}-PyJWT
BuildRequires:	python%{python3_pkgversion}-Routes
BuildRequires:	python%{python3_pkgversion}-Werkzeug
BuildRequires:	python%{python3_pkgversion}-numpy-devel
BuildRequires:	xmlsec1-devel
BuildRequires:	xmlsec1-openssl-devel
%endif
%endif
# lttng and babeltrace for rbd-replay-prep
%if %{with lttng}
%if 0%{?fedora} || 0%{?rhel}
BuildRequires:	lttng-ust-devel
BuildRequires:	libbabeltrace-devel
%endif
%if 0%{?suse_version}
BuildRequires:	lttng-ust-devel
BuildRequires:  babeltrace-devel
%endif
%endif
%if 0%{?suse_version}
BuildRequires:	libexpat-devel
%endif
%if 0%{?rhel} || 0%{?fedora}
BuildRequires:	expat-devel
%endif
#hardened-cc1
%if 0%{?fedora} || 0%{?rhel}
BuildRequires:  redhat-rpm-config
%endif
%if 0%{with seastar}
%if 0%{?fedora} || 0%{?rhel}
BuildRequires:  cryptopp-devel
BuildRequires:  numactl-devel
BuildRequires:  protobuf-compiler
%endif
%if 0%{?suse_version}
BuildRequires:  libcryptopp-devel
BuildRequires:  libnuma-devel
%endif
%endif
%if 0%{?rhel} >= 8
BuildRequires:  /usr/bin/pathfix.py
%endif

%description
This package contains Ceph benchmarks and test tools.

#################################################################################
# subpackages
#################################################################################
%if 0%{?suse_version}
%endif
%if 0%{with selinux}
%endif
%if 0%{?fedora} || 0%{?rhel}
%if 0%{with tcmalloc}
%endif
%endif
%if 0%{?weak_deps}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?weak_deps}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{with libradosstriper}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?weak_deps}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%if 0%{?weak_deps}
%endif
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel} >= 8
%endif
%if 0%{?suse_version}
%endif
%if 0%{?weak_deps}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?rhel} || 0%{?fedora}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{with selinux}
%endif
%if 0%{?rhel} || 0%{?fedora}
%endif
%if %{with ocf}
%if 0%{?suse_version}
%endif
%endif
%if 0%{?suse_version}
%endif
%if 0%{with seastar}
%if 0%{?suse_version}
%endif
%endif
%if 0%{?suse_version}
%endif
%if 0%{?rhel} || 0%{?fedora}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{with libradosstriper}
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?rhel} || 0%{?fedora}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?rhel} || 0%{?fedora}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel} >= 8
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{with cephfs_shell}
%endif
%if 0%{with ceph_test_package}
%if 0%{?suse_version}
%endif
%endif
%if 0%{with cephfs_java}
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%endif
%if 0%{?suse_version}
%endif
%if 0%{with selinux}
%if 0%{?suse_version}
%endif
%endif
%if 0%{?suse_version}
%endif
%prep
%autosetup -p1 -n ceph-16.0.0-4863-g5d95d9d41d

%build
# LTO can be enabled as soon as the following GCC bug is fixed:
# https://gcc.gnu.org/bugzilla/show_bug.cgi?id=48200
%define _lto_cflags %{nil}

%if 0%{with seastar}
. /opt/rh/gcc-toolset-9/enable
%endif

%if 0%{with cephfs_java}
# Find jni.h
for i in /usr/{lib64,lib}/jvm/java/include{,/linux}; do
    [ -d $i ] && java_inc="$java_inc -I$i"
done
%endif

%if 0%{?suse_version}
# the following setting fixed an OOM condition we once encountered in the OBS
RPM_OPT_FLAGS="$RPM_OPT_FLAGS --param ggc-min-expand=20 --param ggc-min-heapsize=32768"
%endif
%if %{with minimal_debugging_information}
RPM_OPT_FLAGS="$(echo $RPM_OPT_FLAGS | sed -e 's/^-g /-g1 /g' -e 's/ -g / -g1 /g' -e 's/ -g$/ -g1/g')"
%endif

export CPPFLAGS="$java_inc"
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS="$RPM_LD_FLAGS"
test "$RPM_LD_FLAGS" && echo "RPM_LD_FLAGS == $RPM_LD_FLAGS" || echo "RPM_LD_FLAGS is empty"

%if 0%{with seastar}
# seastar uses longjmp() to implement coroutine. and this annoys longjmp_chk()
export CXXFLAGS=$(echo $RPM_OPT_FLAGS | sed -e 's/-Wp,-D_FORTIFY_SOURCE=2//g')
%endif

# Parallel build settings ...
CEPH_MFLAGS_JOBS="%{?_smp_mflags}"
CEPH_SMP_NCPUS=$(echo "$CEPH_MFLAGS_JOBS" | sed 's/-j//')
%if 0%{?__isa_bits} == 32
# 32-bit builds can use 3G memory max, which is not enough even for -j2
CEPH_SMP_NCPUS="1"
%endif
# do not eat all memory
echo "Available memory:"
free -h
echo "System limits:"
ulimit -a
if test -n "$CEPH_SMP_NCPUS" -a "$CEPH_SMP_NCPUS" -gt 1 ; then
    mem_per_process=2500
    max_mem=$(LANG=C free -m | sed -n "s|^Mem: *\([0-9]*\).*$|\1|p")
    max_jobs="$(($max_mem / $mem_per_process))"
    test "$CEPH_SMP_NCPUS" -gt "$max_jobs" && CEPH_SMP_NCPUS="$max_jobs" && echo "Warning: Reducing build parallelism to -j$max_jobs because of memory limits"
    test "$CEPH_SMP_NCPUS" -le 0 && CEPH_SMP_NCPUS="1" && echo "Warning: Not using parallel build at all because of memory limits"
fi
export CEPH_SMP_NCPUS
export CEPH_MFLAGS_JOBS="-j$CEPH_SMP_NCPUS"

env | sort

mkdir build
cd build
CMAKE=cmake
${CMAKE} .. \
    -DCMAKE_INSTALL_PREFIX=%{_prefix} \
    -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
    -DCMAKE_INSTALL_LIBEXECDIR=%{_libexecdir} \
    -DCMAKE_INSTALL_LOCALSTATEDIR=%{_localstatedir} \
    -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} \
    -DCMAKE_INSTALL_MANDIR=%{_mandir} \
    -DCMAKE_INSTALL_DOCDIR=%{_docdir}/ceph \
    -DCMAKE_INSTALL_INCLUDEDIR=%{_includedir} \
    -DCMAKE_INSTALL_SYSTEMD_SERVICEDIR=%{_unitdir} \
    -DWITH_MANPAGE=ON \
    -DWITH_PYTHON3=%{python3_version} \
    -DWITH_MGR_DASHBOARD_FRONTEND=OFF \
%if 0%{without ceph_test_package}
    -DWITH_TESTS=OFF \
%endif
%if 0%{with cephfs_java}
    -DWITH_CEPHFS_JAVA=ON \
%endif
%if 0%{with selinux}
    -DWITH_SELINUX=ON \
%endif
%if %{with lttng}
    -DWITH_LTTNG=ON \
    -DWITH_BABELTRACE=ON \
%else
    -DWITH_LTTNG=OFF \
    -DWITH_BABELTRACE=OFF \
%endif
    $CEPH_EXTRA_CMAKE_ARGS \
%if 0%{with ocf}
    -DWITH_OCF=ON \
%endif
%ifarch aarch64 armv7hl mips mipsel ppc ppc64 ppc64le %{ix86} x86_64
    -DWITH_BOOST_CONTEXT=ON \
%else
    -DWITH_BOOST_CONTEXT=OFF \
%endif
%if 0%{with cephfs_shell}
    -DWITH_CEPHFS_SHELL=ON \
%endif
%if 0%{with libradosstriper}
    -DWITH_LIBRADOSSTRIPER=ON \
%else
    -DWITH_LIBRADOSSTRIPER=OFF \
%endif
%if 0%{with amqp_endpoint}
    -DWITH_RADOSGW_AMQP_ENDPOINT=ON \
%else
    -DWITH_RADOSGW_AMQP_ENDPOINT=OFF \
%endif
%if 0%{with kafka_endpoint}
    -DWITH_RADOSGW_KAFKA_ENDPOINT=ON \
%else
    -DWITH_RADOSGW_KAFKA_ENDPOINT=OFF \
%endif
%if 0%{with cmake_verbose_logging}
    -DCMAKE_VERBOSE_MAKEFILE=ON \
%endif
    -DBOOST_J=$CEPH_SMP_NCPUS \
    -DWITH_GRAFANA=ON

%if %{with cmake_verbose_logging}
cat ./CMakeFiles/CMakeOutput.log
cat ./CMakeFiles/CMakeError.log
%endif

make "$CEPH_MFLAGS_JOBS"


%if 0%{with make_check}
%check
# run in-tree unittests
cd build
ctest "$CEPH_MFLAGS_JOBS"
%endif


%install
pushd build
make DESTDIR=%{buildroot} install
# we have dropped sysvinit bits
rm -f %{buildroot}/%{_sysconfdir}/init.d/ceph
popd

%if 0%{with seastar}
# package crimson-osd with the name of ceph-osd
install -m 0755 %{buildroot}%{_bindir}/crimson-osd %{buildroot}%{_bindir}/ceph-osd
%endif

install -m 0644 -D src/etc-rbdmap %{buildroot}%{_sysconfdir}/ceph/rbdmap
%if 0%{?fedora} || 0%{?rhel}
install -m 0644 -D etc/sysconfig/ceph %{buildroot}%{_sysconfdir}/sysconfig/ceph
%endif
%if 0%{?suse_version}
install -m 0644 -D etc/sysconfig/ceph %{buildroot}%{_fillupdir}/sysconfig.%{name}
%endif
install -m 0644 -D systemd/ceph.tmpfiles.d %{buildroot}%{_tmpfilesdir}/ceph-common.conf
install -m 0644 -D systemd/50-ceph.preset %{buildroot}%{_presetdir}/50-ceph.preset
mkdir -p %{buildroot}%{_sbindir}
install -m 0644 -D src/logrotate.conf %{buildroot}%{_sysconfdir}/logrotate.d/ceph
chmod 0644 %{buildroot}%{_docdir}/ceph/sample.ceph.conf
install -m 0644 -D COPYING %{buildroot}%{_docdir}/ceph/COPYING
install -m 0644 -D etc/sysctl/90-ceph-osd.conf %{buildroot}%{_sysctldir}/90-ceph-osd.conf
install -m 0755 -D src/tools/rbd_nbd/rbd-nbd_quiesce %{buildroot}%{_libexecdir}/rbd-nbd/rbd-nbd_quiesce

install -m 0755 src/cephadm/cephadm %{buildroot}%{_sbindir}/cephadm
mkdir -p %{buildroot}%{_sharedstatedir}/cephadm
chmod 0700 %{buildroot}%{_sharedstatedir}/cephadm
mkdir -p %{buildroot}%{_sharedstatedir}/cephadm/.ssh
chmod 0700 %{buildroot}%{_sharedstatedir}/cephadm/.ssh
touch %{buildroot}%{_sharedstatedir}/cephadm/.ssh/authorized_keys
chmod 0600 %{buildroot}%{_sharedstatedir}/cephadm/.ssh/authorized_keys

# firewall templates and /sbin/mount.ceph symlink
%if 0%{?suse_version}
mkdir -p %{buildroot}/sbin
ln -sf %{_sbindir}/mount.ceph %{buildroot}/sbin/mount.ceph
%endif

# udev rules
install -m 0644 -D udev/50-rbd.rules %{buildroot}%{_udevrulesdir}/50-rbd.rules

# sudoers.d
install -m 0600 -D sudoers.d/ceph-osd-smartctl %{buildroot}%{_sysconfdir}/sudoers.d/ceph-osd-smartctl
install -m 0600 -D sudoers.d/cephadm %{buildroot}%{_sysconfdir}/sudoers.d/cephadm

%if 0%{?rhel} >= 8
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_bindir}/*
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_sbindir}/*
%endif

#set up placeholder directories
mkdir -p %{buildroot}%{_sysconfdir}/ceph
mkdir -p %{buildroot}%{_localstatedir}/run/ceph
mkdir -p %{buildroot}%{_localstatedir}/log/ceph
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/tmp
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/mon
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/osd
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/mds
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/mgr
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/crash
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/crash/posted
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/radosgw
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/bootstrap-osd
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/bootstrap-mds
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/bootstrap-rgw
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/bootstrap-mgr
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/bootstrap-rbd
mkdir -p %{buildroot}%{_localstatedir}/lib/ceph/bootstrap-rbd-mirror

# prometheus alerts
install -m 644 -D monitoring/prometheus/alerts/ceph_default_alerts.yml %{buildroot}/etc/prometheus/ceph/ceph_default_alerts.yml

%if 0%{?suse_version}
# create __pycache__ directories and their contents
%py3_compile %{buildroot}%{python3_sitelib}
# hardlink duplicate files under /usr to save space
%fdupes %{buildroot}%{_prefix}
%endif

%if 0%{?rhel} == 8
%py_byte_compile %{__python3} %{buildroot}%{python3_sitelib}
%endif

rm -rf %{buildroot}%{_bindir}/ceph-crash
rm -rf %{buildroot}%{_bindir}/crushtool
rm -rf %{buildroot}%{_bindir}/monmaptool
rm -rf %{buildroot}%{_bindir}/osdmaptool
rm -rf %{buildroot}%{_bindir}/ceph-kvstore-tool
rm -rf %{buildroot}%{_bindir}/ceph-run
rm -rf %{buildroot}%{_bindir}/ceph-dencoder
rm -rf %{buildroot}%{_bindir}/cephfs-data-scan
rm -rf %{buildroot}%{_bindir}/cephfs-journal-tool
rm -rf %{buildroot}%{_bindir}/cephfs-table-tool
rm -rf %{buildroot}%{_presetdir}/50-ceph.preset
rm -rf %{buildroot}%{_sbindir}/ceph-create-keys
rm -rf %{buildroot}%{_libexecdir}/ceph/ceph_common.sh
rm -rf %{buildroot}%{_libdir}/rados-classes/*
rm -rf %{buildroot}%{_libdir}/ceph/erasure-code/libec_*.so*
rm -rf %{buildroot}%{_libdir}/ceph/compressor/libceph_*.so*
rm -rf %{buildroot}%{_unitdir}/ceph-crash.service
rm -rf %{buildroot}%{_libdir}/ceph/crypto/libceph_*.so*
rm -rf %{buildroot}%{_libdir}/libos_tp.so*
rm -rf %{buildroot}%{_libdir}/libosd_tp.so*
rm -rf %{buildroot}%{_sysconfdir}/logrotate.d/ceph
rm -rf %{buildroot}%{_sysconfdir}/sysconfig/ceph
rm -rf %{buildroot}%{_fillupdir}/sysconfig.*
rm -rf %{buildroot}%{_unitdir}/ceph.target
rm -rf %{buildroot}%{python3_sitelib}/ceph_volume/*
rm -rf %{buildroot}%{python3_sitelib}/ceph_volume-*
rm -rf %{buildroot}%{python3_sitelib}/ceph_lvm*
rm -rf %{buildroot}%{python3_sitelib}/ceph_volume_lvm*
rm -rf %{buildroot}%{_mandir}/man8/ceph-deploy.8*
rm -rf %{buildroot}%{_mandir}/man8/ceph-create-keys.8*
rm -rf %{buildroot}%{_mandir}/man8/ceph-run.8*
rm -rf %{buildroot}%{_mandir}/man8/crushtool.8*
rm -rf %{buildroot}%{_mandir}/man8/osdmaptool.8*
rm -rf %{buildroot}%{_mandir}/man8/monmaptool.8*
rm -rf %{buildroot}%{_mandir}/man8/ceph-kvstore-tool.8*
rm -rf %{buildroot}%{_sbindir}/cephadm
rm -rf %{buildroot}%{_mandir}/man8/cephadm.8*
rm -rf %{buildroot}%{_sysconfdir}/sudoers.d/cephadm
rm -rf %{buildroot}%{_sharedstatedir}/cephadm/.ssh/authorized_keys
rm -rf %{buildroot}%doc
rm -rf %{buildroot}%{_docdir}/ceph/sample.ceph.conf
rm -rf %{buildroot}%license
rm -rf %{buildroot}%{_docdir}/ceph/COPYING
rm -rf %{buildroot}%{_bindir}/ceph
rm -rf %{buildroot}%{_bindir}/ceph-authtool
rm -rf %{buildroot}%{_bindir}/ceph-conf
rm -rf %{buildroot}%{_bindir}/ceph-rbdnamer
rm -rf %{buildroot}%{_bindir}/ceph-syn
rm -rf %{buildroot}%{_bindir}/rados
rm -rf %{buildroot}%{_bindir}/radosgw-admin
rm -rf %{buildroot}%{_bindir}/rbd
rm -rf %{buildroot}%{_bindir}/rbd-replay
rm -rf %{buildroot}%{_bindir}/rbd-replay-many
rm -rf %{buildroot}%{_bindir}/rbdmap
rm -rf %{buildroot}%{_sbindir}/mount.ceph
rm -rf %{buildroot}/sbin/mount.ceph
rm -rf %{buildroot}%{_bindir}/rbd-replay-prep
rm -rf %{buildroot}%{_bindir}/ceph-post-file
rm -rf %{buildroot}%{_tmpfilesdir}/ceph-common.conf
rm -rf %{buildroot}%{_mandir}/man8/ceph-authtool.8*
rm -rf %{buildroot}%{_mandir}/man8/ceph-conf.8*
rm -rf %{buildroot}%{_mandir}/man8/ceph-dencoder.8*
rm -rf %{buildroot}%{_mandir}/man8/ceph-diff-sorted.8*
rm -rf %{buildroot}%{_mandir}/man8/ceph-rbdnamer.8*
rm -rf %{buildroot}%{_mandir}/man8/ceph-syn.8*
rm -rf %{buildroot}%{_mandir}/man8/ceph-post-file.8*
rm -rf %{buildroot}%{_mandir}/man8/ceph.8*
rm -rf %{buildroot}%{_mandir}/man8/mount.ceph.8*
rm -rf %{buildroot}%{_mandir}/man8/rados.8*
rm -rf %{buildroot}%{_mandir}/man8/radosgw-admin.8*
rm -rf %{buildroot}%{_mandir}/man8/rbd.8*
rm -rf %{buildroot}%{_mandir}/man8/rbdmap.8*
rm -rf %{buildroot}%{_mandir}/man8/rbd-replay.8*
rm -rf %{buildroot}%{_mandir}/man8/rbd-replay-many.8*
rm -rf %{buildroot}%{_mandir}/man8/rbd-replay-prep.8*
rm -rf %{buildroot}%{_mandir}/man8/rgw-orphan-list.8*
rm -rf %{buildroot}%{_datadir}/ceph/known_hosts_drop.ceph.com
rm -rf %{buildroot}%{_datadir}/ceph/id_rsa_drop.ceph.com
rm -rf %{buildroot}%{_datadir}/ceph/id_rsa_drop.ceph.com.pub
rm -rf %{buildroot}%{_sysconfdir}/bash_completion.d/ceph
rm -rf %{buildroot}%{_sysconfdir}/bash_completion.d/rados
rm -rf %{buildroot}%{_sysconfdir}/bash_completion.d/rbd
rm -rf %{buildroot}%{_sysconfdir}/bash_completion.d/radosgw-admin
rm -rf %{buildroot}%{_sysconfdir}/ceph/rbdmap
rm -rf %{buildroot}%{_unitdir}/rbdmap.service
rm -rf %{buildroot}%{_udevrulesdir}/50-rbd.rules
rm -rf %{buildroot}%{_bindir}/ceph-mds
rm -rf %{buildroot}%{_mandir}/man8/ceph-mds.8*
rm -rf %{buildroot}%{_unitdir}/ceph-mds@.service
rm -rf %{buildroot}%{_unitdir}/ceph-mds.target
rm -rf %{buildroot}%{_bindir}/ceph-mgr
rm -rf %{buildroot}%{_datadir}/ceph/mgr/mgr_module.*
rm -rf %{buildroot}%{_datadir}/ceph/mgr/mgr_util.*
rm -rf %{buildroot}%{_unitdir}/ceph-mgr@.service
rm -rf %{buildroot}%{_unitdir}/ceph-mgr.target
rm -rf %{buildroot}%{_datadir}/ceph/mgr/dashboard
rm -rf %{buildroot}%{_datadir}/ceph/mgr/diskprediction_local
rm -rf %{buildroot}%{_datadir}/ceph/mgr/alerts
rm -rf %{buildroot}%{_datadir}/ceph/mgr/balancer
rm -rf %{buildroot}%{_datadir}/ceph/mgr/crash
rm -rf %{buildroot}%{_datadir}/ceph/mgr/devicehealth
rm -rf %{buildroot}%{_datadir}/ceph/mgr/influx
rm -rf %{buildroot}%{_datadir}/ceph/mgr/insights
rm -rf %{buildroot}%{_datadir}/ceph/mgr/iostat
rm -rf %{buildroot}%{_datadir}/ceph/mgr/localpool
rm -rf %{buildroot}%{_datadir}/ceph/mgr/mds_autoscaler
rm -rf %{buildroot}%{_datadir}/ceph/mgr/orchestrator
rm -rf %{buildroot}%{_datadir}/ceph/mgr/osd_perf_query
rm -rf %{buildroot}%{_datadir}/ceph/mgr/pg_autoscaler
rm -rf %{buildroot}%{_datadir}/ceph/mgr/progress
rm -rf %{buildroot}%{_datadir}/ceph/mgr/prometheus
rm -rf %{buildroot}%{_datadir}/ceph/mgr/rbd_support
rm -rf %{buildroot}%{_datadir}/ceph/mgr/restful
rm -rf %{buildroot}%{_datadir}/ceph/mgr/selftest
rm -rf %{buildroot}%{_datadir}/ceph/mgr/snap_schedule
rm -rf %{buildroot}%{_datadir}/ceph/mgr/status
rm -rf %{buildroot}%{_datadir}/ceph/mgr/telegraf
rm -rf %{buildroot}%{_datadir}/ceph/mgr/telemetry
rm -rf %{buildroot}%{_datadir}/ceph/mgr/test_orchestrator
rm -rf %{buildroot}%{_datadir}/ceph/mgr/volumes
rm -rf %{buildroot}%{_datadir}/ceph/mgr/zabbix
rm -rf %{buildroot}%{_datadir}/ceph/mgr/rook
rm -rf %{buildroot}%{_datadir}/ceph/mgr/k8sevents
rm -rf %{buildroot}%{_datadir}/ceph/mgr/cephadm
rm -rf %{buildroot}%{_bindir}/ceph-mon
rm -rf %{buildroot}%{_bindir}/ceph-monstore-tool
rm -rf %{buildroot}%{_mandir}/man8/ceph-mon.8*
rm -rf %{buildroot}%{_unitdir}/ceph-mon@.service
rm -rf %{buildroot}%{_unitdir}/ceph-mon.target
rm -rf %{buildroot}%{_bindir}/ceph-fuse
rm -rf %{buildroot}%{_mandir}/man8/ceph-fuse.8*
rm -rf %{buildroot}%{_sbindir}/mount.fuse.ceph
rm -rf %{buildroot}%{_unitdir}/ceph-fuse@.service
rm -rf %{buildroot}%{_unitdir}/ceph-fuse.target
rm -rf %{buildroot}%{_bindir}/rbd-fuse
rm -rf %{buildroot}%{_mandir}/man8/rbd-fuse.8*
rm -rf %{buildroot}%{_bindir}/rbd-mirror
rm -rf %{buildroot}%{_mandir}/man8/rbd-mirror.8*
rm -rf %{buildroot}%{_unitdir}/ceph-rbd-mirror@.service
rm -rf %{buildroot}%{_unitdir}/ceph-rbd-mirror.target
rm -rf %{buildroot}%{_bindir}/ceph-immutable-object-cache
rm -rf %{buildroot}%{_mandir}/man8/ceph-immutable-object-cache.8*
rm -rf %{buildroot}%{_unitdir}/ceph-immutable-object-cache@.service
rm -rf %{buildroot}%{_unitdir}/ceph-immutable-object-cache.target
rm -rf %{buildroot}%{_bindir}/rbd-nbd
rm -rf %{buildroot}%{_mandir}/man8/rbd-nbd.8*
rm -rf %{buildroot}%{_libexecdir}/rbd-nbd/rbd-nbd_quiesce
rm -rf %{buildroot}%{_bindir}/ceph-diff-sorted
rm -rf %{buildroot}%{_bindir}/radosgw
rm -rf %{buildroot}%{_bindir}/radosgw-token
rm -rf %{buildroot}%{_bindir}/radosgw-es
rm -rf %{buildroot}%{_bindir}/radosgw-object-expirer
rm -rf %{buildroot}%{_bindir}/rgw-orphan-list
rm -rf %{buildroot}%{_libdir}/libradosgw.so*
rm -rf %{buildroot}%{_mandir}/man8/radosgw.8*
rm -rf %{buildroot}%{_unitdir}/ceph-radosgw@.service
rm -rf %{buildroot}%{_unitdir}/ceph-radosgw.target
rm -rf %{buildroot}%{_bindir}/ceph-clsinfo
rm -rf %{buildroot}%{_bindir}/ceph-bluestore-tool
rm -rf %{buildroot}%{_bindir}/ceph-erasure-code-tool
rm -rf %{buildroot}%{_bindir}/ceph-objectstore-tool
rm -rf %{buildroot}%{_bindir}/ceph-osdomap-tool
rm -rf %{buildroot}%{_bindir}/ceph-osd
rm -rf %{buildroot}%{_libexecdir}/ceph/ceph-osd-prestart.sh
rm -rf %{buildroot}%{_sbindir}/ceph-volume
rm -rf %{buildroot}%{_sbindir}/ceph-volume-systemd
rm -rf %{buildroot}%{_mandir}/man8/ceph-clsinfo.8*
rm -rf %{buildroot}%{_mandir}/man8/ceph-osd.8*
rm -rf %{buildroot}%{_mandir}/man8/ceph-bluestore-tool.8*
rm -rf %{buildroot}%{_mandir}/man8/ceph-volume.8*
rm -rf %{buildroot}%{_mandir}/man8/ceph-volume-systemd.8*
rm -rf %{buildroot}%{_unitdir}/ceph-osd@.service
rm -rf %{buildroot}%{_unitdir}/ceph-osd.target
rm -rf %{buildroot}%{_unitdir}/ceph-volume@.service
rm -rf %{buildroot}%{_sysctldir}/90-ceph-osd.conf
rm -rf %{buildroot}%{_sysconfdir}/sudoers.d/ceph-osd-smartctl
rm -rf %{buildroot}%{_bindir}/crimson-osd
rm -rf %{buildroot}%{_prefix}/lib/ocf/resource.d/ceph/rbd
rm -rf %{buildroot}%{_libdir}/librados.so.*
rm -rf %{buildroot}%{_libdir}/ceph/libceph-common.so.*
rm -rf %{buildroot}%{_libdir}/librados_tp.so.*
rm -rf %{buildroot}%{_includedir}/rados/librados.h
rm -rf %{buildroot}%{_includedir}/rados/rados_types.h
rm -rf %{buildroot}%{_libdir}/librados.so
rm -rf %{buildroot}%{_libdir}/librados_tp.so
rm -rf %{buildroot}%{_bindir}/librados-config
rm -rf %{buildroot}%{_mandir}/man8/librados-config.8*
rm -rf %{buildroot}%{_includedir}/rados/buffer.h
rm -rf %{buildroot}%{_includedir}/rados/buffer_fwd.h
rm -rf %{buildroot}%{_includedir}/rados/crc32c.h
rm -rf %{buildroot}%{_includedir}/rados/inline_memory.h
rm -rf %{buildroot}%{_includedir}/rados/librados.hpp
rm -rf %{buildroot}%{_includedir}/rados/librados_fwd.hpp
rm -rf %{buildroot}%{_includedir}/rados/page.h
rm -rf %{buildroot}%{_includedir}/rados/rados_types.hpp
rm -rf %{buildroot}%{python3_sitearch}/rados.cpython*.so
rm -rf %{buildroot}%{python3_sitearch}/rados-*.egg-info
rm -rf %{buildroot}%{_libdir}/libradosstriper.so.*
rm -rf %{buildroot}%{_includedir}/radosstriper/libradosstriper.h
rm -rf %{buildroot}%{_includedir}/radosstriper/libradosstriper.hpp
rm -rf %{buildroot}%{_libdir}/libradosstriper.so
rm -rf %{buildroot}%{_libdir}/librbd.so.*
rm -rf %{buildroot}%{_libdir}/librbd_tp.so.*
rm -rf %{buildroot}%{_libdir}/ceph/librbd/libceph_*.so*
rm -rf %{buildroot}%{_includedir}/rbd/librbd.h
rm -rf %{buildroot}%{_includedir}/rbd/librbd.hpp
rm -rf %{buildroot}%{_includedir}/rbd/features.h
rm -rf %{buildroot}%{_libdir}/librbd.so
rm -rf %{buildroot}%{_libdir}/librbd_tp.so
rm -rf %{buildroot}%{_libdir}/librgw.so.*
rm -rf %{buildroot}%{_libdir}/librgw_op_tp.so.*
rm -rf %{buildroot}%{_libdir}/librgw_rados_tp.so.*
rm -rf %{buildroot}%{_includedir}/rados/librgw.h
rm -rf %{buildroot}%{_includedir}/rados/rgw_file.h
rm -rf %{buildroot}%{_libdir}/librgw.so
rm -rf %{buildroot}%{_libdir}/librgw_op_tp.so
rm -rf %{buildroot}%{_libdir}/librgw_rados_tp.so
rm -rf %{buildroot}%{python3_sitearch}/rgw.cpython*.so
rm -rf %{buildroot}%{python3_sitearch}/rgw-*.egg-info
rm -rf %{buildroot}%{python3_sitearch}/rbd.cpython*.so
rm -rf %{buildroot}%{python3_sitearch}/rbd-*.egg-info
rm -rf %{buildroot}%{_libdir}/libcephfs.so.*
rm -rf %{buildroot}%{_includedir}/cephfs/libcephfs.h
rm -rf %{buildroot}%{_includedir}/cephfs/ceph_ll_client.h
rm -rf %{buildroot}%{_includedir}/cephfs/metrics/Types.h
rm -rf %{buildroot}%{_libdir}/libcephfs.so
rm -rf %{buildroot}%{python3_sitearch}/cephfs.cpython*.so
rm -rf %{buildroot}%{python3_sitearch}/cephfs-*.egg-info
rm -rf %{buildroot}%{python3_sitelib}/ceph_volume_client.py
rm -rf %{buildroot}%{python3_sitelib}/__pycache__/ceph_volume_client.cpython*.py*
rm -rf %{buildroot}%{python3_sitelib}/ceph_argparse.py
rm -rf %{buildroot}%{python3_sitelib}/__pycache__/ceph_argparse.cpython*.py*
rm -rf %{buildroot}%{python3_sitelib}/ceph_daemon.py
rm -rf %{buildroot}%{python3_sitelib}/__pycache__/ceph_daemon.cpython*.py*
rm -rf %{buildroot}%{python3_sitelib}/ceph
rm -rf %{buildroot}%{python3_sitelib}/ceph-*.egg-info
rm -rf %{buildroot}%{python3_sitelib}/cephfs_shell-*.egg-info
rm -rf %{buildroot}%{_bindir}/cephfs-shell
rm -rf %{buildroot}%{_libdir}/libcephfs_jni.so.*
rm -rf %{buildroot}%{_libdir}/libcephfs_jni.so
rm -rf %{buildroot}%{_javadir}/libcephfs.jar
rm -rf %{buildroot}%{_javadir}/libcephfs-test.jar
rm -rf %{buildroot}%{_includedir}/rados/objclass.h
rm -rf %{buildroot}%{_datadir}/selinux/packages/ceph.pp
rm -rf %{buildroot}%{_datadir}/selinux/devel/include/contrib/ceph.if
rm -rf %{buildroot}%{_mandir}/man8/ceph_selinux.8*
rm -rf %{buildroot}%{_sysconfdir}/grafana/dashboards/ceph-dashboard/*
rm -rf %{buildroot}%doc
rm -rf %{buildroot}monitoring/grafana/dashboards/README
rm -rf %{buildroot}%doc
rm -rf %{buildroot}monitoring/grafana/README.md
rm -rf %{buildroot}%{_sysconfdir}/prometheus/ceph/ceph_default_alerts.yml

dirs=`find %{buildroot} -type d -empty`
while [[ -n $dirs ]]; do
  for d in $dirs; do
    rm -rf $d
  done
dirs=`find %{buildroot} -type d -empty`
done

%clean
rm -rf %{buildroot}

#################################################################################
# files and systemd scriptlets
#################################################################################
%files

%if %{with lttng}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if ! 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if %{with lttng}
%endif
%if 0%{?rhel} || 0%{?fedora}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?sysctl_apply}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?fedora} || 0%{?rhel}
%endif
%if 0%{with seastar}
%endif
%if %{with ocf}
%endif
%if %{with lttng}
%endif
%if %{with lttng}
%endif
%if 0%{with libradosstriper}
%endif
%if %{with lttng}
%endif
%if %{with lttng}
%endif
%if %{with lttng}
%endif
%if %{with lttng}
%endif
%if 0%{with cephfs_shell}
%endif
%if 0%{with ceph_test_package}
%files -n ceph-test
%{_bindir}/ceph-client-debug
%{_bindir}/ceph_bench_log
%{_bindir}/ceph_kvstorebench
%{_bindir}/ceph_multi_stress_watch
%{_bindir}/ceph_erasure_code_benchmark
%{_bindir}/ceph_omapbench
%{_bindir}/ceph_objectstore_bench
%{_bindir}/ceph_perf_objectstore
%{_bindir}/ceph_perf_local
%{_bindir}/ceph_perf_msgr_client
%{_bindir}/ceph_perf_msgr_server
%{_bindir}/ceph_psim
%{_bindir}/ceph_radosacl
%{_bindir}/ceph_rgw_jsonparser
%{_bindir}/ceph_rgw_multiparser
%{_bindir}/ceph_scratchtool
%{_bindir}/ceph_scratchtoolpp
%{_bindir}/ceph_test_*
%{_bindir}/ceph-coverage
%{_bindir}/ceph-debugpack
%{_bindir}/ceph-dedup-tool
%{_mandir}/man8/ceph-debugpack.8*
%dir %{_libdir}/ceph
%{_libdir}/ceph/ceph-monstore-update-crush.sh
%endif

%if 0%{with cephfs_java}
%endif
%if 0%{with selinux}
%endif
%if 0%{?suse_version}
%endif
%if 0%{?suse_version}
%endif
%changelog
