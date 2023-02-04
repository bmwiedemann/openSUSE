#
# spec file for package snapper
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


# Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

# Location for PAM module
%if 0%{?suse_version} >= 1550
%define pam_security_dir %{_libdir}/security
%else
%define pam_security_dir /%{_lib}/security
%endif

# Optionally build with test coverage reporting
%bcond_with coverage

Name:           snapper
Version:        0.10.4
Release:        0
Summary:        Tool for filesystem snapshot management
License:        GPL-2.0-only
Group:          System/Packages
URL:            http://snapper.io/
Source:         snapper-%{version}.tar.bz2
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
BuildRequires:  libboost_test-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  libacl-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  e2fsprogs-devel
BuildRequires:  ncurses-devel
%if 0%{?suse_version}
BuildRequires:  libbtrfs-devel
%endif
%if 0%{?suse_version} > 1310
BuildRequires:  libmount-devel >= 2.24
%endif
%if 0%{?fedora_version} >= 23
BuildRequires:  pkgconfig
BuildRequires:  systemd
%else
BuildRequires:  pkg-config
%endif
%if 0%{?fedora_version} >= 24 || 0%{?centos_version} >= 800
BuildRequires:	glibc-langpack-de
BuildRequires:	glibc-langpack-fr
BuildRequires:	glibc-langpack-en
%else
BuildRequires:  glibc-locale
%endif
%if ! 0%{?mandriva_version}
%if 0%{?fedora_version} >= 23
BuildRequires:  dbus-devel
BuildRequires:  docbook-style-xsl
%else
BuildRequires:  dbus-1-devel
BuildRequires:  docbook-xsl-stylesheets
%endif
BuildRequires:  libxslt
%else
BuildRequires:  docbook-dtd45-xml
BuildRequires:  docbook-xsl
BuildRequires:  libdbus-1-devel
BuildRequires:  xsltproc
%endif
%if 0%{?suse_version}
BuildRequires:  libzypp(plugin:commit)
%endif
BuildRequires:  pam-devel
%if 0%{?fedora_version} || 0%{?rhel_version} || 0%{?centos_version} || 0%{?scientificlinux_version}
BuildRequires:  json-c-devel
%else
BuildRequires:  libjson-c-devel
%endif
BuildRequires:  zlib-devel
%if %{with coverage}
BuildRequires:  lcov
%endif
Requires:       diffutils
Requires:       libsnapper6 = %version
Requires:       systemd
%if 0%{?suse_version}
Recommends:     logrotate snapper-zypp-plugin
Supplements:    btrfsprogs
%endif

%description
This package contains snapper, a tool for filesystem snapshot management.

%prep
%setup -q

%build
%if %{with coverage}
# optimized code may confuse the coverage measurement, turn it off
# -fPIC is mysteriously needed on Fedora.
export CFLAGS="-g3 -fPIC"
export CXXFLAGS="-g3 -fPIC"
%else
export CFLAGS="%{optflags} -DNDEBUG"
export CXXFLAGS="%{optflags} -DNDEBUG"
%endif

autoreconf -fvi
%configure \
	--docdir="%{_defaultdocdir}/snapper"					\
%if %{with coverage}
	--enable-coverage \
%endif
	--with-pam-security="%{pam_security_dir}"				\
%if 0%{?suse_version} <= 1310
	--disable-rollback							\
%endif
%if 0%{?suse_version} <= 1310
	--disable-btrfs-quota							\
%endif
	--disable-silent-rules --disable-ext4
make %{?_smp_mflags}

%install
%make_install
rm -f "%{buildroot}/%{_libdir}"/*.la "%{buildroot}/%{pam_security_dir}/pam_snapper.la"
rm -f %{buildroot}/etc/cron.hourly/suse.de-snapper
rm -f %{buildroot}/etc/cron.daily/suse.de-snapper

%if 0%{?suse_version}
install -D -m 644 data/sysconfig.snapper "%{buildroot}%{_fillupdir}/sysconfig.snapper"
%else
install -D -m 644 data/sysconfig.snapper "%{buildroot}/etc/sysconfig/snapper"
%endif

# move logrotate files from /etc/logrotate.d to /usr/etc/logrotate.d
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d
mv %{buildroot}/%{_sysconfdir}/logrotate.d/snapper %{buildroot}%{_distconfdir}/logrotate.d
%endif

%{find_lang} snapper

%check
make %{?_smp_mflags} check VERBOSE=1

%pre
%if 0%{?suse_version}
%service_add_pre snapper-boot.service snapper-boot.timer snapper-cleanup.service snapper-cleanup.timer snapper-timeline.service snapper-timeline.timer snapperd.service
%endif
%if 0%{?suse_version} > 1500
# Migration from /etc/logrotate.d to /usr/etc/logrotate.d
test -f /etc/logrotate.d/snapper.rpmsave && mv -v /etc/logrotate.d/snapper.rpmsave /etc/logrotate.d/snapper.rpmsave.old ||:
%endif

%post
%if 0%{?suse_version}
# special hack, since the macros were added much later than
# the systemd timer
if [ -f /etc/cron.hourly/suse.de-snapper ]; then
 systemctl preset snapper-timeline.timer || :
 systemctl is-enabled -q snapper-timeline.timer && systemctl start snapper-timeline.timer || :
fi
if [ -f /etc/cron.daily/suse.de-snapper ]; then
 systemctl preset snapper-cleanup.timer || :
 systemctl is-enabled -q snapper-cleanup.timer && systemctl start snapper-cleanup.timer || :
fi
%service_add_post snapper-boot.service snapper-boot.timer snapper-cleanup.service snapper-cleanup.timer snapper-timeline.service snapper-timeline.timer snapperd.service
%endif

%if 0%{?suse_version} > 1500
%posttrans
# Migration from /etc/logrotate.d to /usr/etc/logrotate.d
test -f /etc/logrotate.d/snapper.rpmsave && mv -v /etc/logrotate.d/snapper.rpmsave /etc/logrotate.d/snapper ||:
%endif

%preun
%if 0%{?suse_version}
%service_del_preun snapper-boot.service snapper-boot.timer snapper-cleanup.service snapper-cleanup.timer snapper-timeline.service snapper-timeline.timer snapperd.service
%endif

%postun
%if 0%{?suse_version}
%service_del_postun snapper-boot.service snapper-boot.timer snapper-cleanup.service snapper-cleanup.timer snapper-timeline.service snapper-timeline.timer snapperd.service
%endif

%files -f snapper.lang
%defattr(-,root,root)
%{_bindir}/snapper
%{_sbindir}/snapperd
%if 0%{?suse_version} > 1310
%{_sbindir}/mksubvolume
%endif
%dir %{_prefix}/lib/snapper
%{_prefix}/lib/snapper/*-helper
%{_mandir}/*/snapper.8*
%{_mandir}/*/snapperd.8*
%{_mandir}/*/snapper-configs.5*
%if 0%{?suse_version} > 1310
%doc %{_mandir}/*/mksubvolume.8*
%endif
%if 0%{?suse_version} > 1500
%{_distconfdir}/logrotate.d/snapper
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/snapper
%endif
%{_unitdir}/snapper*.*
%if 0%{?suse_version} <= 1500
%dir %{_datadir}/dbus-1/system.d
%endif
%{_datadir}/dbus-1/system.d/org.opensuse.Snapper.conf
%{_datadir}/dbus-1/system-services/org.opensuse.Snapper.service
%{_datadir}/bash-completion/completions/snapper

%package -n libsnapper6
Summary:        Library for filesystem snapshot management
Group:          System/Libraries
Requires:       util-linux
%if 0%{?suse_version}
PreReq:         %fillup_prereq
%endif
# expands to Obsoletes: libsnapper1 libsnapper2 libsnapper3...
Obsoletes:      %(echo `seq -s " " -f "libsnapper%.f" $((6 - 1))`)

%description -n libsnapper6
This package contains libsnapper, a library for filesystem snapshot management.

%files -n libsnapper6
%license %{_defaultdocdir}/snapper/COPYING
%doc %dir %{_defaultdocdir}/snapper
%doc %{_defaultdocdir}/snapper/AUTHORS
%{_libdir}/libsnapper.so.*
%dir %{_sysconfdir}/snapper
%dir %{_sysconfdir}/snapper/configs
%dir %{_datadir}/snapper
%dir %{_datadir}/snapper/config-templates
%{_datadir}/snapper/config-templates/default
%dir %{_datadir}/snapper/filters
%{_datadir}/snapper/filters/*.txt
%if 0%{?suse_version}
%{_fillupdir}/sysconfig.snapper
%else
%config(noreplace) %{_sysconfdir}/sysconfig/snapper
%endif

%pre -n libsnapper6
# Migration from /etc/snapper to /usr/share/snapper
for i in config-templates/default filters/base.txt filters/lvm.txt filters/x11.txt ; do
    test -f /etc/snapper/${i}.rpmsave && mv -v /etc/snapper/${i}.rpmsave /etc/snapper/${i}.rpmsave.old ||:
done

%posttrans -n libsnapper6
# Migration from /etc/snapper to /usr/share/snapper
for i in config-templates/default filters/base.txt filters/lvm.txt filters/x11.txt ; do
    test -f /etc/snapper/${i}.rpmsave && mv -v /etc/snapper/${i}.rpmsave /etc/snapper/${i} ||:
done

%post -n libsnapper6
/sbin/ldconfig
%if 0%{?suse_version}
%{fillup_only -n snapper}
%endif

%postun -n libsnapper6 -p /sbin/ldconfig

%package -n libsnapper-devel
%if 0%{?suse_version} > 1325
Requires:       libboost_headers-devel
%else
Requires:       boost-devel
%endif
Requires:       gcc-c++
Requires:	    libacl-devel
Requires:       libsnapper6 = %version
Requires:       libstdc++-devel
Requires:       libxml2-devel
%if 0%{?suse_version}
Requires:       libbtrfs-devel
%endif
%if 0%{?suse_version} > 1310
Requires:       libmount-devel >= 2.24
%endif
Summary:        Header files and documentation for libsnapper
Group:          Development/Languages/C and C++

%description -n libsnapper-devel
This package contains header files and documentation for developing with
libsnapper.

%files -n libsnapper-devel
%{_libdir}/libsnapper.so
%{_includedir}/snapper

%package -n snapper-zypp-plugin
Requires:       libzypp(plugin:commit) = 1
Requires:       snapper = %version
Summary:        A zypp commit plugin for calling snapper
Group:          System/Packages

%description -n snapper-zypp-plugin
This package contains a plugin for zypp that makes filesystem snapshots with
snapper during commits.

%files -n snapper-zypp-plugin
%{_datadir}/snapper/zypp-plugin.conf
/usr/lib/zypp/plugins/commit/snapper-zypp-plugin
%doc %{_mandir}/*/snapper-zypp-plugin.8*
%doc %{_mandir}/*/snapper-zypp-plugin.conf.5*

%pre -n snapper-zypp-plugin
# Migration from /etc/snapper to /usr/share/snapper
for i in zypp-plugin.conf ; do
    test -f /etc/snapper/${i}.rpmsave && mv -v /etc/snapper/${i}.rpmsave /etc/snapper/${i}.rpmsave.old ||:
done

%posttrans -n snapper-zypp-plugin
# Migration from /etc/snapper to /usr/share/snapper
for i in zypp-plugin.conf ; do
    test -f /etc/snapper/${i}.rpmsave && mv -v /etc/snapper/${i}.rpmsave /etc/snapper/${i} ||:
done

%package -n pam_snapper
Requires:       pam
Requires:       snapper = %version
Summary:        PAM module for calling snapper
Group:          System/Packages

%description -n pam_snapper
A PAM module for calling snapper during user login and logout.

%files -n pam_snapper
/%{pam_security_dir}/pam_snapper.so
%dir /usr/lib/pam_snapper
/usr/lib/pam_snapper/*.sh
%doc %{_mandir}/*/pam_snapper.8*

%package testsuite
Summary:        Integration tests for snapper
Group:          System/Packages

%description testsuite
Tests to be run in a scratch machine to test that snapper operates as expected.

%files testsuite
%dir %{_libdir}/snapper
%dir %{_libdir}/snapper/testsuite
%{_libdir}/snapper/testsuite/*

%changelog
