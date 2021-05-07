#
# spec file for package selinux-policy
#
# Copyright (c) 2021 SUSE LLC
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


# There are almost no SUSE specific modifications available in the policy, so we utilize the
# ones used by redhat and include also the SUSE specific ones (see sed statement below)
%define distro redhat
%define ubac n
%define polyinstatiate n
%define monolithic n
%define BUILD_TARGETED 1
%define BUILD_MINIMUM 1
%define BUILD_MLS 1

%define POLICYCOREUTILSVER %(rpm -q --qf %%{version} policycoreutils)
%define CHECKPOLICYVER %POLICYCOREUTILSVER

Summary:        SELinux policy configuration
License:        GPL-2.0-or-later
Group:          System/Management
Name:           selinux-policy
Version:        20210419
Release:        0
Source:         fedora-policy-%{version}.tar.bz2
Source1:        selinux-policy-rpmlintrc

Source10:       modules-targeted-base.conf
Source11:       modules-targeted-contrib.conf
Source12:       modules-mls-base.conf
Source13:       modules-mls-contrib.conf
Source14:       modules-minimum-base.conf
Source15:       modules-minimum-contrib.conf
Source18:       modules-minimum-disable.lst

Source20:       booleans-targeted.conf
Source21:       booleans-mls.conf
Source22:       booleans-minimum.conf
Source23:       booleans.subs_dist

Source30:       setrans-targeted.conf
Source31:       setrans-mls.conf
Source32:       setrans-minimum.conf

Source40:       securetty_types-targeted
Source41:       securetty_types-mls
Source42:       securetty_types-minimum

Source50:       users-targeted
Source51:       users-mls
Source52:       users-minimum

Source60:       selinux-policy.conf

Source91:       Makefile.devel
Source92:       customizable_types
#Source93:       config.tgz
Source94:       file_contexts.subs_dist
Source95:       macros.selinux-policy
Source96:       update.sh

Source120:      packagekit.te
Source121:      packagekit.if
Source122:      packagekit.fc
Source123:      rtorrent.te
Source124:      rtorrent.if
Source125:      rtorrent.fc
Source126:      wicked.te
Source127:      wicked.if
Source128:      wicked.fc

Patch001:       fix_djbdns.patch
Patch002:       fix_dbus.patch
Patch003:       fix_gift.patch
Patch004:       fix_java.patch
Patch005:       fix_hadoop.patch
Patch006:       fix_thunderbird.patch
Patch007:       fix_postfix.patch
Patch008:       fix_nscd.patch
Patch009:       fix_sysnetwork.patch
Patch010:       fix_logging.patch
Patch011:       fix_xserver.patch
Patch012:       fix_miscfiles.patch
Patch013:       fix_init.patch
Patch014:       fix_locallogin.patch
Patch016:       fix_iptables.patch
Patch017:       fix_irqbalance.patch
Patch018:       fix_ntp.patch
Patch019:       fix_fwupd.patch
Patch020:       fix_firewalld.patch
Patch021:       fix_logrotate.patch
Patch022:       fix_selinuxutil.patch
Patch024:       fix_corecommand.patch
Patch025:       fix_snapper.patch
Patch026:       fix_systemd.patch
Patch027:       fix_unconfined.patch
Patch028:       fix_unconfineduser.patch
Patch029:       fix_chronyd.patch
Patch030:       fix_networkmanager.patch
Patch032:       fix_accountsd.patch
Patch033:       fix_automount.patch
Patch034:       fix_colord.patch
Patch035:       fix_mcelog.patch
Patch036:       fix_sslh.patch
Patch037:       fix_nagios.patch
Patch038:       fix_openvpn.patch
Patch039:       fix_cron.patch
Patch040:       fix_usermanage.patch
Patch041:       fix_smartmon.patch
Patch042:       fix_geoclue.patch
Patch044:       fix_authlogin.patch
Patch045:       fix_screen.patch
Patch046:       fix_unprivuser.patch
Patch047:       fix_rpm.patch
Patch048:       fix_apache.patch
Patch049:       fix_nis.patch
Patch050:       fix_libraries.patch
Patch051:       fix_dovecot.patch

Patch100:       sedoctool.patch

URL:            https://github.com/fedora-selinux/selinux-policy.git
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  checkpolicy
BuildRequires:  gawk
BuildRequires:  libxml2-tools
BuildRequires:  m4
BuildRequires:  policycoreutils
BuildRequires:  policycoreutils-devel
BuildRequires:  python3
BuildRequires:  python3-policycoreutils
# we need selinuxenabled
Requires(pre):  policycoreutils >= %{POLICYCOREUTILSVER}
Requires(pre):  pam-config
Requires(post): pam-config
Requires(post): selinux-tools
Requires(post): /usr/bin/sha512sum
Recommends:     audit
Recommends:     selinux-tools
# for audit2allow
Recommends:     python3-policycoreutils
Recommends:     policycoreutils-python-utils
Recommends:     container-selinux
Recommends:     selinux-autorelabel

%define common_params DISTRO=%{distro} UBAC=%{ubac} DIRECT_INITRC=n MONOLITHIC=%{monolithic} MLS_CATS=1024 MCS_CATS=1024

%define makeCmds() \
%make_build %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 bare \
%make_build %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 conf \
cp -f selinux_config/booleans-%1.conf ./policy/booleans.conf \
cp -f selinux_config/users-%1 ./policy/users \
#cp -f selinux_config/modules-%1-base.conf  ./policy/modules.conf \

%define makeModulesConf() \
cp -f selinux_config/modules-%1-%2.conf  ./policy/modules-base.conf \
cp -f selinux_config/modules-%1-%2.conf  ./policy/modules.conf \
if [ %3 == "contrib" ];then \
        cp selinux_config/modules-%1-%3.conf ./policy/modules-contrib.conf; \
        cat selinux_config/modules-%1-%3.conf >> ./policy/modules.conf; \
fi; \

%define installCmds() \
%make_build %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 base.pp \
%make_build %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 validate modules \
make %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 DESTDIR=%{buildroot} install \
make %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 DESTDIR=%{buildroot} install-appconfig \
make %common_params UNK_PERMS=%3 NAME=%1 TYPE=%2 DESTDIR=%{buildroot} SEMODULE="%{_sbindir}/semodule -p %{buildroot} -X 100 " load \
%{__mkdir} -p %{buildroot}%{_sysconfdir}/selinux/%1/logins \
touch %{buildroot}%{_sysconfdir}/selinux/%1/contexts/files/file_contexts.subs \
install -m0644 selinux_config/securetty_types-%1 %{buildroot}%{_sysconfdir}/selinux/%1/contexts/securetty_types \
install -m0644 selinux_config/file_contexts.subs_dist %{buildroot}%{_sysconfdir}/selinux/%1/contexts/files \
install -m0644 selinux_config/setrans-%1.conf %{buildroot}%{_sysconfdir}/selinux/%1/setrans.conf \
install -m0644 selinux_config/customizable_types %{buildroot}%{_sysconfdir}/selinux/%1/contexts/customizable_types \
touch %{buildroot}%{_sysconfdir}/selinux/%1/contexts/files/file_contexts.bin \
touch %{buildroot}%{_sysconfdir}/selinux/%1/contexts/files/file_contexts.local \
touch %{buildroot}%{_sysconfdir}/selinux/%1/contexts/files/file_contexts.local.bin \
cp %{SOURCE23} %{buildroot}%{_sysconfdir}/selinux/%1 \
rm -f %{buildroot}%{_datadir}/selinux/%1/*pp*  \
%{_bindir}/sha512sum %{buildroot}%{_sysconfdir}/selinux/%1/policy/policy.* | cut -d' ' -f 1 > %{buildroot}%{_sysconfdir}/selinux/%1/.policy.sha512; \
rm -rf %{buildroot}%{_sysconfdir}/selinux/%1/contexts/netfilter_contexts  \
rm -rf %{buildroot}%{_sysconfdir}/selinux/%1/modules/active/policy.kern \
rm -f %{buildroot}%{_sharedstatedir}/selinux/%1/active/*.linked \
%nil

%define fileList() \
%defattr(-,root,root) \
%dir %{_sysconfdir}/selinux/%1 \
%config(noreplace) %{_sysconfdir}/selinux/%1/setrans.conf \
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/selinux/%1/seusers \
%dir %{_sysconfdir}/selinux/%1/logins \
%dir %{_sharedstatedir}/selinux/%1/active \
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%1/semanage.read.LOCK \
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%1/semanage.trans.LOCK \
%dir %attr(700,root,root) %{_sharedstatedir}/selinux/%1/active/modules \
%dir %{_sharedstatedir}/selinux/%1/active/modules/100 \
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%1/active/modules/100/base \
%dir %{_sysconfdir}/selinux/%1/policy/ \
%verify(not md5 size mtime) %{_sysconfdir}/selinux/%1/policy/policy.* \
%{_sysconfdir}/selinux/%1/.policy.sha512 \
%dir %{_sysconfdir}/selinux/%1/contexts \
%config %{_sysconfdir}/selinux/%1/contexts/customizable_types \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/securetty_types \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/dbus_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/x_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/default_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/virtual_domain_context \
%config %{_sysconfdir}/selinux/%1/contexts/virtual_image_context \
%config %{_sysconfdir}/selinux/%1/contexts/lxc_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/systemd_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/sepgsql_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/openssh_contexts \
%config %{_sysconfdir}/selinux/%1/contexts/snapperd_contexts \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/default_type \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/failsafe_context \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/initrc_context \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/removable_context \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/userhelper_context \
%dir %{_sysconfdir}/selinux/%1/contexts/files \
%verify(not md5 size mtime) %{_sysconfdir}/selinux/%1/contexts/files/file_contexts \
%ghost %{_sysconfdir}/selinux/%1/contexts/files/file_contexts.bin \
%verify(not md5 size mtime) %{_sysconfdir}/selinux/%1/contexts/files/file_contexts.homedirs \
%ghost %{_sysconfdir}/selinux/%1/contexts/files/file_contexts.homedirs.bin \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/files/file_contexts.local \
%ghost %{_sysconfdir}/selinux/%1/contexts/files/file_contexts.local.bin \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/files/file_contexts.subs \
%{_sysconfdir}/selinux/%1/contexts/files/file_contexts.subs_dist \
%{_sysconfdir}/selinux/%1/booleans.subs_dist \
%config %{_sysconfdir}/selinux/%1/contexts/files/media \
%dir %{_sysconfdir}/selinux/%1/contexts/users \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/users/root \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/users/guest_u \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/users/xguest_u \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/users/user_u \
%config(noreplace) %{_sysconfdir}/selinux/%1/contexts/users/staff_u \
%dir %{_datadir}/selinux/%1 \
%{_datadir}/selinux/%1/base.lst \
%{_datadir}/selinux/%1/modules-base.lst \
%{_datadir}/selinux/%1/modules-contrib.lst \
%{_datadir}/selinux/%1/nonbasemodules.lst \
%dir %{_sharedstatedir}/selinux/%1 \
%{_sharedstatedir}/selinux/%1/active/commit_num \
%{_sharedstatedir}/selinux/%1/active/users_extra \
%{_sharedstatedir}/selinux/%1/active/homedir_template \
%{_sharedstatedir}/selinux/%1/active/seusers \
%{_sharedstatedir}/selinux/%1/active/file_contexts \
%{_sharedstatedir}/selinux/%1/active/policy.kern \
%ghost %{_sharedstatedir}/selinux/%1/active/policy.linked \
%ghost %{_sharedstatedir}/selinux/%1/active/seusers.linked \
%ghost %{_sharedstatedir}/selinux/%1/active/users_extra.linked \
%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%1/active/file_contexts.homedirs \
%nil

%define relabel() \
. %{_sysconfdir}/selinux/config; \
FILE_CONTEXT=%{_sysconfdir}/selinux/%1/contexts/files/file_contexts; \
if selinuxenabled; then \
  if [ $? = 0  -a "${SELINUXTYPE}" = %1 -a -f ${FILE_CONTEXT}.pre ]; then \
    %{_sbindir}/fixfiles -C ${FILE_CONTEXT}.pre restore 2> /dev/null; \
    rm -f ${FILE_CONTEXT}.pre; \
  fi; \
  if /sbin/restorecon -e /run/media -R /root /var/log /var/run %{_sysconfdir}/passwd* %{_sysconfdir}/group* %{_sysconfdir}/*shadow* 2> /dev/null;then \
    continue; \
  fi; \
fi;

%define preInstall() \
if [ $1 -ne 1 ] && [ -s %{_sysconfdir}/selinux/config ]; then \
     . %{_sysconfdir}/selinux/config; \
     FILE_CONTEXT=%{_sysconfdir}/selinux/%1/contexts/files/file_contexts; \
     if [ "${SELINUXTYPE}" = %1 -a -f ${FILE_CONTEXT} ]; then \
        [ -f ${FILE_CONTEXT}.pre ] || cp -f ${FILE_CONTEXT} ${FILE_CONTEXT}.pre; \
     fi; \
     touch %{_sysconfdir}/selinux/%1/.rebuild; \
     if [ -e %{_sysconfdir}/selinux/%1/.policy.sha512 ]; then \
        POLICY_FILE=`ls %{_sysconfdir}/selinux/%1/policy/policy.* | sort | head -1` \
        sha512=`sha512sum $POLICY_FILE | cut -d ' ' -f 1`; \
        checksha512=`cat %{_sysconfdir}/selinux/%1/.policy.sha512`; \
        if [ "$sha512" == "$checksha512" ] ; then \
                rm %{_sysconfdir}/selinux/%1/.rebuild; \
        fi; \
   fi; \
fi;

%define postInstall() \
. %{_sysconfdir}/selinux/config; \
if [ -e %{_sysconfdir}/selinux/%%2/.rebuild ]; then \
  rm %{_sysconfdir}/selinux/%%2/.rebuild; \
  /usr/sbin/semodule -B -n -s %%2; \
fi; \
if [ -n "${TRANSACTIONAL_UPDATE}" ]; then \
  touch /etc/selinux/.autorelabel \
else    \
  if [ "${SELINUXTYPE}" = "%2" ]; then \
    if selinuxenabled; then \
      load_policy; \
    else \
      # probably a first install of the policy \
      true; \
    fi; \
  fi; \
  if selinuxenabled; then \
    if [ %1 -eq 1 ]; then \
      /sbin/restorecon -R /root /var/log /run /etc/passwd* /etc/group* /etc/*shadow* 2> /dev/null; \
    else \
      %relabel %2 \
    fi; \
  else \
    # run fixfiles on next boot \
    touch /.autorelabel \
  fi; \
fi;

%define modulesList() \
awk '$1 !~ "/^#/" && $2 == "=" && $3 == "module" { printf "%%s ", $1 }' ./policy/modules-base.conf > %{buildroot}%{_datadir}/selinux/%1/modules-base.lst \
awk '$1 !~ "/^#/" && $2 == "=" && $3 == "base" { printf "%%s ", $1 }' ./policy/modules-base.conf > %{buildroot}%{_datadir}/selinux/%1/base.lst \
if [ -e ./policy/modules-contrib.conf ];then \
        awk '$1 !~ "/^#/" && $2 == "=" && $3 == "module" { printf "%%s ", $1 }' ./policy/modules-contrib.conf > %{buildroot}%{_datadir}/selinux/%1/modules-contrib.lst; \
fi;

%define nonBaseModulesList() \
contrib_modules=`cat %{buildroot}%{_datadir}/selinux/%1/modules-contrib.lst` \
base_modules=`cat %{buildroot}%{_datadir}/selinux/%1/modules-base.lst` \
for i in $contrib_modules $base_modules; do \
    if [ $i != "sandbox" ];then \
        echo "%verify(not md5 size mtime) %{_sharedstatedir}/selinux/%1/active/modules/100/$i" >> %{buildroot}%{_datadir}/selinux/%1/nonbasemodules.lst \
    fi; \
done;

%description
SELinux Reference Policy. A complete SELinux policy that can be used
as the system policy for a variety of systems and used as the basis for
creating other policies.

%files
%defattr(-,root,root,-)
%doc COPYING
%dir %{_datadir}/selinux
%dir %{_datadir}/selinux/packages
%dir %{_sysconfdir}/selinux
%ghost %config(noreplace) %{_sysconfdir}/selinux/config
%{_tmpfilesdir}/selinux-policy.conf
%{_rpmconfigdir}/macros.d/macros.selinux-policy

%package sandbox
Summary:        SELinux policy sandbox
Group:          System/Management
Requires(pre): selinux-policy-targeted = %{version}-%{release}

%description sandbox
SELinux sandbox policy used for the policycoreutils-sandbox package

%files sandbox
%verify(not md5 size mtime) %{_datadir}/selinux/packages/sandbox.pp

%post sandbox
rm -f %{_sysconfdir}/selinux/*/modules/active/modules/sandbox.pp.disabled 2>/dev/null
rm -f %{_sharedstatedir}/selinux/*/active/modules/disabled/sandbox 2>/dev/null
%{_sbindir}/semodule -n -X 100 -i %{_datadir}/selinux/packages/sandbox.pp
if %{_sbindir}/selinuxenabled ; then
    %{_sbindir}/load_policy
fi;
exit 0

%preun sandbox
if [ $1 -eq 0 ] ; then
    %{_sbindir}/semodule -n -d sandbox 2>/dev/null
    if %{_sbindir}/selinuxenabled ; then
        %{_sbindir}/load_policy
    fi;
fi;
exit 0

%prep
%setup -n fedora-policy-%{version}
%patch001 -p1
%patch002 -p1
%patch003 -p1
%patch004 -p1
%patch005 -p1
%patch006 -p1
%patch007 -p1
%patch008 -p1
%patch009 -p1
%patch010 -p1
%patch011 -p1
%patch012 -p1
%patch013 -p1
%patch014 -p1
%patch016 -p1
%patch017 -p1
%patch018 -p1
%patch019 -p1
%patch020 -p1
%patch021 -p1
%patch022 -p1
%patch024 -p1
%patch025 -p1
%patch026 -p1
%patch027 -p1
%patch028 -p1
%patch029 -p1
%patch030 -p1
#% patch031 -p1
%patch032 -p1
%patch033 -p1
%patch034 -p1
%patch035 -p1
%patch036 -p1
%patch037 -p1
%patch038 -p1
%patch039 -p1
%patch040 -p1
%patch041 -p1
%patch042 -p1
#% patch043 -p1
%patch044 -p1
%patch045 -p1
%patch046 -p1
%patch047 -p1
%patch048 -p1
%patch049 -p1
%patch050 -p1
%patch051 -p1

%patch100 -p1
find . -type f -exec sed -i -e "s/distro_suse/distro_redhat/" \{\} \;

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/selinux
touch %{buildroot}%{_sysconfdir}/selinux/config
mkdir -p %{buildroot}%{_tmpfilesdir}
cp %{SOURCE60} %{buildroot}%{_tmpfilesdir}

# Adjust and install RPM macro file
mkdir -p %{buildroot}%{_rpmconfigdir}/macros.d
install -m 644 %{SOURCE95} %{buildroot}%{_rpmconfigdir}/macros.d/
sed -i 's|SELINUXPOLICYVERSION|%{version}-%{release}|' %{buildroot}%{_rpmconfigdir}/macros.d/macros.selinux-policy
sed -i 's|SELINUXSTOREPATH|%{_sharedstatedir}/selinux|' %{buildroot}%{_rpmconfigdir}/macros.d/macros.selinux-policy

# Always create policy module package directories
mkdir -p %{buildroot}%{_datadir}/selinux/{targeted,mls,minimum,modules}/
mkdir -p %{buildroot}%{_sharedstatedir}/selinux/{targeted,mls,minimum,modules}/

mkdir -p %{buildroot}%{_datadir}/selinux/packages

mkdir selinux_config
for i in %{SOURCE10} %{SOURCE11} %{SOURCE12} %{SOURCE13} %{SOURCE14} %{SOURCE15} %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE30} %{SOURCE31} %{SOURCE32} %{SOURCE40} %{SOURCE41} %{SOURCE42} %{SOURCE50} %{SOURCE51} %{SOURCE52} %{SOURCE91} %{SOURCE92} %{SOURCE94};do
 cp $i selinux_config
done

for i in %{SOURCE120} %{SOURCE121} %{SOURCE122} %{SOURCE123} %{SOURCE124} %{SOURCE125} %{SOURCE126} %{SOURCE127} %{SOURCE128}; do
 cp $i policy/modules/contrib
done

make clean
%if %{BUILD_TARGETED}
%makeCmds targeted mcs allow
%makeModulesConf targeted base contrib
%installCmds targeted mcs allow
# recreate sandbox.pp
rm -rf %{buildroot}%{_sharedstatedir}/selinux/targeted/active/modules/100/sandbox
%make_build %common_params UNK_PERMS=allow NAME=targeted TYPE=mcs sandbox.pp
mv sandbox.pp %{buildroot}%{_datadir}/selinux/packages/sandbox.pp
%modulesList targeted
%nonBaseModulesList targeted
%endif

%if %{BUILD_MINIMUM}
%makeCmds minimum mcs allow
%makeModulesConf targeted base contrib
%installCmds minimum mcs allow
install -m0644 %{SOURCE18} %{buildroot}%{_datadir}/selinux/minimum/modules-minimum-disable.lst
# Sandbox is only targeted
rm -f %{buildroot}%{_sysconfdir}/selinux/minimum/modules/active/modules/sandbox.pp
rm -rf %{buildroot}%{_sharedstatedir}/selinux/minimum/active/modules/100/sandbox
%modulesList minimum
%nonBaseModulesList minimum
%endif

%if %{BUILD_MLS}
%makeCmds mls mls deny
%makeModulesConf mls base contrib
%installCmds mls mls deny
%modulesList mls
%nonBaseModulesList mls
%endif

# Install devel
mkdir -p %{buildroot}%{_mandir}
cp -R  man/* %{buildroot}%{_mandir}
make %common_params UNK_PERMS=allow NAME=targeted TYPE=mcs DESTDIR=%{buildroot} PKGNAME=%{name} install-docs
make %common_params UNK_PERMS=allow NAME=targeted TYPE=mcs DESTDIR=%{buildroot} PKGNAME=%{name} install-headers
mkdir %{buildroot}%{_datadir}/selinux/devel/
mv %{buildroot}%{_datadir}/selinux/targeted/include %{buildroot}%{_datadir}/selinux/devel/include
install -m 644 selinux_config/Makefile.devel %{buildroot}%{_datadir}/selinux/devel/Makefile
install -m 644 doc/example.* %{buildroot}%{_datadir}/selinux/devel/
install -m 644 doc/policy.* %{buildroot}%{_datadir}/selinux/devel/
%{_bindir}/sepolicy manpage -a -p %{buildroot}%{_datadir}/man/man8/ -w -r %{buildroot}
mkdir %{buildroot}%{_datadir}/selinux/devel/html
mv %{buildroot}%{_datadir}/man/man8/*.html %{buildroot}%{_datadir}/selinux/devel/html
mv %{buildroot}%{_datadir}/man/man8/style.css %{buildroot}%{_datadir}/selinux/devel/html

%post
if [ ! -s %{_sysconfdir}/selinux/config ]; then
    # new install, use old sysconfig file if that exists,
    # else create new one.
    if [ -f  %{_sysconfdir}/sysconfig/selinux-policy ]; then
	mv %{_sysconfdir}/sysconfig/selinux-policy %{_sysconfdir}/selinux/config
    else
	echo "
# This file controls the state of SELinux on the system.
# SELinux can be completly disabled with the \"selinux=0\" kernel
# commandline option.
#
# SELINUX= can take one of these three values:
#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
SELINUX=permissive
# SELINUXTYPE= can take one of these three values:
#     targeted - Targeted processes are protected,
#     minimum - Modification of targeted policy. Only selected processes are protected.
#     mls - Multi Level Security protection.
SELINUXTYPE=targeted

" > %{_sysconfdir}/selinux/config
    fi
    ln -sf ../selinux/config %{_sysconfdir}/sysconfig/selinux-policy
    %{_sbindir}/restorecon %{_sysconfdir}/selinux/config 2> /dev/null || :
fi
%tmpfiles_create %_tmpfilesdir/selinux-policy.conf
if [ $1 -eq 1 ]; then
  pam-config -a --selinux
fi
exit 0

%define post_un() \
# disable selinux if we uninstall a policy and it's the used one \
if [ $1 -eq 0 ]; then \
  if [ -s %{_sysconfdir}/selinux/config ]; then \
      source %{_sysconfdir}/selinux/config &> /dev/null || true \
  fi \
  if [ "$SELINUXTYPE" = "$2" ]; then \
    %{_sbindir}/setenforce 0 2> /dev/null \
    if [ -s %{_sysconfdir}/selinux/config ]; then \
      sed -i 's/^SELINUX=.*/SELINUX=permissive/g' %{_sysconfdir}/selinux/config \
    fi \
  fi \
  pam-config -d --selinux \
fi \
exit 0

%postun
if [ $1 = 0 ]; then
     %{_sbindir}/setenforce 0 2> /dev/null
     if [ -s %{_sysconfdir}/selinux/config ]; then
          sed -i 's/^SELINUX=.*/SELINUX=permissive/g' %{_sysconfdir}/selinux/config
     fi
fi
exit 0

%package devel
Summary:        SELinux policy devel
Group:          System/Management
Requires(pre):  selinux-policy = %{version}-%{release}
Requires:       /usr/bin/make
Requires:       checkpolicy >= %{CHECKPOLICYVER}
Requires:       m4

%description devel
SELinux policy development and man page package

%files devel
%defattr(-,root,root,-)
%doc %{_datadir}/man/ru/man8/*
%doc %{_datadir}/man/man8/*
%dir %{_datadir}/selinux/devel
%dir %{_datadir}/selinux/devel/html/
%doc %{_datadir}/selinux/devel/html/*
%dir %{_datadir}/selinux/devel/include
%{_datadir}/selinux/devel/include/*
%{_datadir}/selinux/devel/Makefile
%{_datadir}/selinux/devel/example.*

%package doc
Summary:        SELinux policy documentation
Group:          System/Management
Requires(pre):  selinux-policy = %{version}-%{release}
Requires:       /usr/bin/xdg-open

%description doc
SELinux policy documentation package

%files doc
%defattr(-,root,root,-)
%doc %{_datadir}/doc/%{name}
%{_datadir}/selinux/devel/policy.*

%if %{BUILD_TARGETED}
%package targeted
Summary:        SELinux targeted base policy
Group:          System/Management
Provides:       selinux-policy-base = %{version}-%{release}
Requires(pre):  coreutils
Requires(pre):  selinux-policy = %{version}-%{release}
Requires:       selinux-policy = %{version}-%{release}

%description targeted
SELinux Reference policy targeted base module.

%pre targeted
%preInstall targeted

%post targeted
%postInstall $1 targeted
exit 0

%postun targeted
%post_un $1 targeted

%files targeted -f %{buildroot}%{_datadir}/selinux/targeted/nonbasemodules.lst
%config(noreplace) %{_sysconfdir}/selinux/targeted/contexts/users/unconfined_u
%config(noreplace) %{_sysconfdir}/selinux/targeted/contexts/users/sysadm_u
%fileList targeted
%endif

%if %{BUILD_MINIMUM}
%package minimum
Summary:        SELinux minimum base policy
Group:          System/Management
Provides:       selinux-policy-base = %{version}-%{release}
Requires(post): policycoreutils >= %{POLICYCOREUTILSVER}
Requires(post): policycoreutils-python-utils >= %{POLICYCOREUTILSVER}
Requires(pre):  coreutils
Requires(pre):  /usr/bin/awk
Requires(pre):  selinux-policy = %{version}-%{release}
Requires:       selinux-policy = %{version}-%{release}

%description minimum
SELinux Reference policy minimum base module.

%pre minimum
%preInstall minimum
if [ $1 -ne 1 ]; then
    %{_sbindir}/semodule -s minimum --list-modules=full | awk '{ if ($4 != "disabled") print $2; }' > %{_datadir}/selinux/minimum/instmodules.lst
fi

%post minimum
contribpackages=`cat %{_datadir}/selinux/minimum/modules-contrib.lst`
basepackages=`cat %{_datadir}/selinux/minimum/modules-base.lst`
mkdir -p %{_sharedstatedir}/selinux/minimum/active/modules/disabled 2>/dev/null
if [ $1 -eq 1 ]; then
    for p in $contribpackages; do
	touch %{_sharedstatedir}/selinux/minimum/active/modules/disabled/$p
    done
    for p in $basepackages snapper dbus kerberos nscd rpm rtkit; do
	rm -f %{_sharedstatedir}/selinux/minimum/active/modules/disabled/$p
    done
    %{_sbindir}/semanage import -S minimum -f - << __eof
login -m  -s unconfined_u -r s0-s0:c0.c1023 __default__
login -m  -s unconfined_u -r s0-s0:c0.c1023 root
__eof
    /sbin/restorecon -R /root /var/log /var/run 2> /dev/null
    %{_sbindir}/semodule -B -s minimum
else
    instpackages=`cat %{_datadir}/selinux/minimum/instmodules.lst`
    for p in $contribpackages; do
	touch %{_sharedstatedir}/selinux/minimum/active/modules/disabled/$p
    done
    for p in $instpackages snapper dbus kerberos nscd rtkit; do
	rm -f %{_sharedstatedir}/selinux/minimum/active/modules/disabled/$p
    done
    %{_sbindir}/semodule -B -s minimum
    %relabel minimum
fi
exit 0

%postun minimum
%post_un $1 minimum

%files minimum -f %{buildroot}%{_datadir}/selinux/minimum/nonbasemodules.lst
%config(noreplace) %{_sysconfdir}/selinux/minimum/contexts/users/unconfined_u
%config(noreplace) %{_sysconfdir}/selinux/minimum/contexts/users/sysadm_u
%{_datadir}/selinux/minimum/modules-minimum-disable.lst
%fileList minimum
%endif

%if %{BUILD_MLS}
%package mls
Summary:        SELinux mls base policy
Group:          System/Management
Provides:       selinux-policy-base = %{version}-%{release}
Requires:       policycoreutils-newrole >= %{POLICYCOREUTILSVER}
Requires:       setransd
Requires(pre):  policycoreutils >= %{POLICYCOREUTILSVER}
Requires(pre):  coreutils
Requires(pre):  selinux-policy = %{version}-%{release}
Requires:       selinux-policy = %{version}-%{release}

%description mls
SELinux Reference policy mls base module.

%pre mls
%preInstall mls

%post mls
%postInstall $1 mls

%postun mls
%post_un $1 mls

%files mls -f %{buildroot}%{_datadir}/selinux/mls/nonbasemodules.lst
%config(noreplace) %{_sysconfdir}/selinux/mls/contexts/users/unconfined_u
%fileList mls
%endif

%changelog
