#
# spec file for package sblim-sfcb
#
# Copyright (c) 2023 SUSE LLC
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


%if 0%{?suse_version} > 1140 || 0%{?fedora_version} > 14
%define has_systemd 1
%else
%define has_systemd 0
%endif

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Small Footprint CIM Broker
License:        EPL-1.0
Group:          System/Management

Name:           sblim-sfcb
Version:        1.4.9
Release:        0
%define srcversion 1.4.9
URL:            http://sblim.sf.net/
Source0:        %{name}-%{srcversion}.tar.bz2
Source1:        autoconfiscate.sh
%if 0%{?suse_version}
Source2:        sblim-sfcb.init
%endif
Source4:        sfcb-pam.conf
Source5:        %{name}-rpmlintrc
Source6:        susefirewall.conf
Source7:        README.conf
Source8:        gen_ssl_certs.sh

# SUSE build service
Patch1:         0001-Makefile.am-Honor-build-environment.patch
Patch2:         0002-providerMgr-add-prototypes.patch
Patch3:         0003-Enable-broker.LogMessage-and-broker.trace.patch
Patch4:         0004-Check-for-existance-of-autoconfiscate.sh-before-call.patch

# fixes local build
Patch5:         0005-Define-YYPARSE_PARAM-early-for-cimXmlOps-and-cimXmlP.patch
Patch6:         0006-Don-t-crash-if-class-repo-is-not-initialized.patch
Patch7:         0007-Increase-max-trace-msg-len-to-4096.patch
Patch8:         0008-Properly-shut-down-if-provider-crashed.patch

# functionality fixes
Patch9:         0009-Improvide-error-message-if-ClassProvider-for-root-in.patch
Patch10:        0010-Enable-authentication-by-default.patch

Patch12:        0012-Configurable-local-socket-group-permission-for-daemo.patch
Patch13:        0013-Fix-bashisms-in-scripts.patch
# bsc#942628 lookupProviders() null pointer dereference
Patch14:        0014-Fix-lookupProviders-null-pointer-dereference.patch
Patch15:        0015-Define-UINT16_MAX.patch
Patch16:        0016-Externalize-strncpy_kind.patch
Patch17:        0017-Add-braces-around-else.patch
Patch18:        0018-Adapt-to-bison-3.x-replace-YYPARSE_PARAM.patch
Patch19:        0019-Fix-uninitialized-value-reported-by-valgrind.patch
Patch20:        0020-link-certificate-if-missing.patch
Patch21:        0021-revert-upstream-mistake.patch
Patch22:        0022-Fix-crash-caused-by-NULL-content_type.patch
# bsc#906070 - add custom names as alias
Patch23:        0023-Alias-sblim-sfcb-service-to-sfcb-and-sfcbd.patch
# SLE10's curl is too old
Patch24:        0024-CURLOPT_POSTREDIR-might-not-be-defined.patch
# bsc#1092281 - certificates shouldn't be generated during installation.
Patch25:        0025-Generates-certificates-during-service-start.patch
Patch26:        0026-fix-build-dependencies-for-sfcbinst2mof.patch
Patch27:        0027-Makefile.am-add-autoconfiscate.sh-to-dist.patch
Patch28:        0028-allow-requests-with-Content-Type-set-to-text-xml.patch
Patch29:        no_tlsv1_config.patch
Patch30:        harden_sblim-sfcb.service.patch

Provides:       cim-server
Provides:       cimserver
BuildRequires:  cmpi-devel
BuildRequires:  curl
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  openssl
BuildRequires:  sblim-sfcCommon-devel
%if 0%{?suse_version} >= 1030
BuildRequires:  libcurl-devel
%else
BuildRequires:  curl-devel
%endif
BuildRequires:  cim-schema
BuildRequires:  libtool
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  sblim-sfcc-devel
BuildRequires:  zlib-devel
%if 0%{?rhel_version} == 0 && 0%{?centos_version} == 0
BuildRequires:  openslp-devel
%endif
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  unzip
%if 0%{?suse_version} >= 1140
%if 0%{?has_systemd} == 0
Requires:       sysvinit-tools
%endif
%endif
%if 0%{?has_systemd}
BuildRequires:  pkgconfig(systemd)
%{?systemd_ordering}
# for /usr/sbin/service
Requires(pre):  aaa_base
%endif

Requires:       curl
%if 0%{?suse_version} < 1120
# unneeded explicit lib dependency
Requires:       zlib
%endif
Requires:       openssl
Requires:       pam
# Added NWP - dependency on cim-schema instead of inbuilt schema
Requires:       cim-schema
PreReq:         /usr/sbin/groupadd
PreReq:         /usr/sbin/groupmod
PreReq:         cmpi-provider-register

%description
Small Footprint CIM Broker (sfcb) is a CIM server conforming to the CIM
Operations over HTTP protocol. It is robust, with low resource
consumption and therefore specifically suited for embedded and resource
constrained environments. sfcb supports providers written against the
Common Manageability Programming Interface (CMPI).

%prep
%setup -q -n %{name}-%{srcversion}

# remove autogenerated file
rm cimXmlParserProcessed.c

cp %{S:1} .
cp %{S:7} .
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1

export PATCH_GET=0

%build
autoreconf -f -i
if test -d mofc; then cd mofc && autoreconf -f -i; cd ..; fi
#%%configure --enable-debug --enable-ssl --enable-pam --enable-ipv6 CIMSCHEMA_SOURCE=%{SOURCE1} CIMSCHEMA_MOF=cimv216.mof CIMSCHEMA_SUBDIRS=y
mkdir -p m4
%if 0%{?rhel_version} == 0 && 0%{?centos_version} == 0
WITH_SLP=--enable-slp
%else
WITH_SLP=
%endif
export SFCB_DIR=`pwd`
export SYSTEMDDIR=%{_unitdir}
%if 0%{?suse_version}
%if 0%{?suse_version} <= 1040
# SLE 10 fails on -fgnu89-inline
export CFLAGS="%optflags"
%else
export CFLAGS="%optflags -fgnu89-inline -fcommon"
%endif
%endif
%configure --enable-debug --enable-ssl --enable-pam --enable-ipv6 \
            --enable-uds $WITH_SLP \
	    --enable-large_volume_support \
	    --enable-optimized-enumeration \
	    --enable-cim-rs \
            --enable-relax-mofsyntax
echo "exit 0" > getSchema.sh
make

%install
export SYSTEMDDIR=$RPM_BUILD_ROOT/%{_unitdir}
%if 0%{?has_systemd}
mkdir -p $RPM_BUILD_ROOT/%{_unitdir}
%endif
# SLE10 'make install' does not create /etc/sfcb
%if 0%{?suse_version} == 1010
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/sfcb
%endif
make install DESTDIR=$RPM_BUILD_ROOT
make postinstall DESTDIR=$RPM_BUILD_ROOT
# comment out - NWP - removing schema pkg
#make DESTDIR=$RPM_BUILD_ROOT install-cimschema
# remove docs from wrong dir.  They are handled by %doc macro in files list
rm -r $RPM_BUILD_ROOT/usr/share/doc
# remove cmpi-devel
rm -rf $RPM_BUILD_ROOT/usr/include/cmpi
# remove unused libtool files
rm -f $RPM_BUILD_ROOT/%{_libdir}/*a
# make the cmpi directory that sfcb will own - for SuSE Autobuild checks of rpm directory ownership
mkdir $RPM_BUILD_ROOT/%{_libdir}/cmpi
%if 0%{?has_systemd}
# remove the default-installed sfcb init script
rm -f $RPM_BUILD_ROOT/etc/init.d/sfcb
# create /usr/sbin/rcsblim-sfcb, esp. for cmpi-provider-register
# create /usr/sbin/rcsfcb for compatibility with SLE11 upgrades in cmpi-provider-register, just in case... DO NOT REMOVE!
# see bugs: 1041885, 874811
ln -sf %{_sbindir}/service $RPM_BUILD_ROOT%{_sbindir}/rcsfcb
ln -sf %{_sbindir}/service $RPM_BUILD_ROOT%{_sbindir}/rcsblim-sfcb
%else
%if 0%{?suse_version}
# override the default-installed sfcb init script - use the one from Source2
# due to /etc/SuSE-release not available in autobuild, so won't install
# correct init script
install %SOURCE2 $RPM_BUILD_ROOT/etc/init.d/sfcb
ln -s /etc/init.d/sfcb $RPM_BUILD_ROOT/usr/sbin/rcsfcb
%endif
%endif
# Added NWP 5/14/08 - transition to using cim-schema rpm instead of internal-built schema
ln -sf /usr/share/mof/cim-current $RPM_BUILD_ROOT/%{_datadir}/sfcb/CIM
install -m 0644 %SOURCE4 $RPM_BUILD_ROOT/etc/pam.d/sfcb
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_pam_vendordir}
mv $RPM_BUILD_ROOT/etc/pam.d/sfcb $RPM_BUILD_ROOT/%{_pam_vendordir}
%endif
install -m 0755 %SOURCE8 %{buildroot}%{_datadir}/sfcb/gen_ssl_certs.sh
rm $RPM_BUILD_ROOT%{_libdir}/sfcb/*.la
%if 0%{?suse_version} <= 1500
# firewall service definition
mkdir -p $RPM_BUILD_ROOT/etc/sysconfig/SuSEfirewall2.d/services
install -m 0644 %SOURCE6 $RPM_BUILD_ROOT/etc/sysconfig/SuSEfirewall2.d/services/sblim-sfcb
%endif
echo "%defattr(-,root,root)" > _pkg_list
# Added NWP 5/14/08 - moved from 'files schema'
echo "%dir %{_datadir}/sfcb/" >> _pkg_list
find $RPM_BUILD_ROOT/%{_datadir}/sfcb -type f | grep -v $RPM_BUILD_ROOT/%{_datadir}/sfcb/CIM >> _pkg_list
# Added next line - NWP - declaring link to CIM as part of pkg
echo "%{_datadir}/sfcb/CIM" >> _pkg_list
# end add NWP
sed s?$RPM_BUILD_ROOT??g _pkg_list > _pkg_list_2
mv -f _pkg_list_2 _pkg_list
echo "%dir %{_libdir}/cmpi/" >> _pkg_list
echo "%dir %{_sysconfdir}/sfcb/" >> _pkg_list
echo "%dir %{_libdir}/sfcb" >> _pkg_list
echo "%config(noreplace) %{_sysconfdir}/sfcb/sfcb.cfg" >> _pkg_list
%if 0%{?suse_version} > 1500
echo "%config %{_pam_vendordir}/sfcb" >> _pkg_list
%else
echo "%config %{_sysconfdir}/pam.d/sfcb" >> _pkg_list
%endif
%if 0%{?suse_version} <= 1500
echo "%config %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services/sblim-sfcb" >> _pkg_list
%endif
echo "%doc README COPYING AUTHORS" >> _pkg_list
echo "%doc README.conf" >> _pkg_list
echo "%doc %{_datadir}/man/man1/*" >> _pkg_list
%if 0%{?has_systemd}
echo "%{_unitdir}/sblim-sfcb.service" >> _pkg_list
%else
echo "%{_sysconfdir}/init.d/sfcb" >> _pkg_list
%endif
echo "%{_localstatedir}/lib/sfcb" >> _pkg_list
echo "%{_bindir}/*" >> _pkg_list
echo "%{_sbindir}/*" >> _pkg_list
echo "%{_libdir}/sfcb/*.so*" >> _pkg_list
echo "%{_datadir}/sfcb/gen_ssl_certs.sh" >> _pkg_list
echo =======================================
cat _pkg_list

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/groupadd -r sfcb >/dev/null 2>&1 || :
/usr/sbin/groupmod -A root sfcb >/dev/null 2>&1 || :
# cleanup up schema directory (bnc#590196)
if [ -d %{_datadir}/sfcb/CIM -a \( \! -L /usr/share/sfcb/CIM \) ]
then
  rm -rf %{_datadir}/sfcb/CIM
fi

# follow http://en.opensuse.org/openSUSE:Systemd_packaging_guidelines
%if 0%{?has_systemd}
%service_add_pre sblim-sfcb.service
%endif

%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/lib; save any old .rpmsave
for i in pam.d/sfcb ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/lib, restore just created .rpmsave
for i in pam.d/sfcb ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%post
%if 0%{?has_systemd}
%service_add_post sblim-sfcb.service
%else
#removed NWP, placed into init script for first service startup
#%{_datadir}/sfcb/genSslCert.sh %{_sysconfdir}/sfcb
%if 0%{?suse_version}
%{fillup_and_insserv -f sfcb}
%endif
%endif
if test $1 -eq 1 ; then
   sfcbrepos -f 2> /dev/null || :
fi
# else we do it in postun instead.
/sbin/ldconfig
exit 0

%preun
%if 0%{?has_systemd}
%service_del_preun sblim-sfcb.service
%else
%stop_on_removal sfcb
%endif

%postun
/sbin/ldconfig
if test $1 -ge 1 ; then
   sfcbrepos -f 2> /dev/null || :
fi
%if 0%{?has_systemd}
%service_del_postun sblim-sfcb.service
%else
%restart_on_update sfcb
%insserv_cleanup
%endif

%files -f _pkg_list

%changelog
