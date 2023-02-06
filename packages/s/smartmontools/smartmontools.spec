#
# spec file for package smartmontools
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           smartmontools
Version:        7.3
Release:        0
Source:         https://sourceforge.net/projects/smartmontools/files/smartmontools/%{version}/%{name}-%{version}.tar.gz
Source1:        https://sourceforge.net/projects/smartmontools/files/smartmontools/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        smartmontools.sysconfig
Source3:        %{name}-rpmlintrc
Source4:        %{name}.keyring
# SOURCE-FEATURE-OPENSUSE smartmontools.generate_smartd_opts.in sbrabec@suse.cz -- sysconfig support for systemd.
Source5:        %{name}.generate_smartd_opts.in
# SOURCE-FEATURE-SLE smartmontools-drivedb_h-update.sh bnc851276 sbrabec@suse.cz -- Supplementary script to update drivedb.h.
Source6:        smartmontools-drivedb_h-update.sh
# SOURCE-FEATURE-UPSTREAM smartmontools-drivedb.h bnc851276 sbrabec@suse.cz -- Update of drivedb.h. (Following line is handled by smartmontools-drivedb_h-update.sh.)
#Source7:        smartmontools-drivedb.h
Source8:        smartd_generate_opts.path
Source9:        smartd_generate_opts.service
# PATCH-FEATURE-OPENSUSE smartmontools-suse-default.patch sbrabec@suse.cz -- Define smart SUSE defaults.
Patch4:         smartmontools-suse-default.patch
# PATCH-FIX-OPENSUSE smartmontools-var-lock-subsys.patch sbrabec@suse.cz -- Do not use unsupported /var/lock/subsys.
Patch10:        smartmontools-var-lock-subsys.patch
Patch11:        harden_smartd.service.patch
Requires(pre):  %fillup_prereq
# Needed by generate_smartd_opt:
Requires(pre):  coreutils
URL:            https://www.smartmontools.org/
BuildRequires:  gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libcap-ng-devel
BuildRequires:  libselinux-devel
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
Summary:        Monitor for SMART devices
License:        GPL-2.0-or-later
Group:          Hardware/Other

%description
SMARTmontools controls and monitors storage devices using the
Self-Monitoring, Analysis, and Reporting Technology System (S.M.A.R.T.)
built into ATA, SATA and SCSI Hard Drives. This is used to check the
hard drive reliability and to predict drive failures. The suite
contains two utilities. The first, smartctl, is a command line utility
designed to perform simple S.M.A.R.T. tasks. The second, smartd, is a
daemon that periodically monitors the smart status and reports errors
to syslog. The package is compatible with the ATA/ATAPI-3 to -7
specification. The package is intended to incorporate as much "vendor
specific" and "reserved" information as possible about disk drives. The
commands man smartctl and man smartd will provide more information.

%prep
%setup -q
cp -a %{SOURCE2} %{SOURCE5} .
# Following line is handled by smartmontools-drivedb_h-update.sh.
#cp -a %{SOURCE7} drivedb.h.new
%patch4
%patch10 -p1
%patch11 -p1
#
# PATCH-FEATURE-OPENSUSE (sed on smartd.service.in) sbrabec@suse.cz -- Use generated smartd_opts (from SUSE sysconfig file). Systemd smartd.service cannot be smart enough to parse SUSE sysconfig file and generate smartd_opts on fly. And we do not want to launch shell just for it in every boot.
sed "s:/usr/local/etc/sysconfig/smartmontools:%{_localstatedir}/lib/smartmontools/smartd_opts:" <smartd.service.in >smartd.service.in.new
if cmp -s smartd.service.in smartd.service.in.new ; then
	echo "Failed to modify smartd.service.in"
	exit 1
fi
mv smartd.service.in.new smartd.service.in
#
# Check whether drivedb.h from the tarball is older than drivedb.h.new
# If yes, replace it. If not, fail.
# PACKAGERS: Don't delete this section. It prevents packaging of outdated smartmontools-drivedb.h.
if test -f drivedb.h.new ; then
	UPD_TIME=$(date -d "$(sed -n 's/^.*$Id: drivedb.h [0-9][0-9]* \([^ ]* [^ ]*\) .*$/\1/p' <drivedb.h.new)" +%s)
	PCK_TIME=$(date -d "$(sed -n 's/^.*$Id: drivedb.h [0-9][0-9]* \([^ ]* [^ ]*\) .*$/\1/p' <drivedb.h)" +%s)
	if test $UPD_TIME -lt $PCK_TIME ; then
		echo >&2 "Packaging error: Attached smartmontools-drivedb.h is older than the one from the release.
		  Please call \"bash ./smartmontools-drivedb_h-update.sh\" to fix it."
		exit 1
	fi
	mv drivedb.h.new drivedb.h
fi

%build
export CFLAGS="%{optflags} $(getconf LFS_CFLAGS) -fPIE"
export CXXFLAGS="%{optflags} -fPIE $(getconf LFS_CFLAGS)"
export LDFLAGS="-pie"
%configure\
	--docdir=%{_defaultdocdir}/%{name}\
	--with-selinux\
	--with-libsystemd\
	--with-systemdsystemunitdir=%{_unitdir}\
	--with-savestates \
	--with-attributelog \
	--with-nvme-devicescan

make %{?_smp_mflags} BUILD_INFO='"(SUSE RPM)"'
SERVICE=/usr/sbin/service
sed "s:@prefix@:%{_prefix}:g;s:@localstatedir@:%{_localstatedir}:g;s:@SERVICE@:$SERVICE:" <smartmontools.generate_smartd_opts.in >generate_smartd_opts

%install
%makeinstall
mkdir -p %{buildroot}%{_prefix}/lib/smartmontools
mkdir -p %{buildroot}%{_fillupdir}
cp smartmontools.sysconfig %{buildroot}%{_fillupdir}/sysconfig.smartmontools
mkdir -p %{buildroot}%{_localstatedir}/lib/smartmontools
touch %{buildroot}%{_localstatedir}/lib/smartmontools/smartd_opts
install generate_smartd_opts %{buildroot}%{_prefix}/lib/smartmontools/
cat >%{buildroot}%{_sysconfdir}/smart_drivedb.h <<EOF
/* smart_drivedb.h: Custom drive database. See also %{_datadir}/smartmontools/drivedb.h. */
EOF
cp smartd.service %{buildroot}/%{_unitdir}
cp %{SOURCE8} %{buildroot}/%{_unitdir}
cp %{SOURCE9} %{buildroot}/%{_unitdir}
ln -sf %{_sbindir}/service  %{buildroot}%{_sbindir}/rcsmartd
# INSTALL file is intended only for packagers.
rm %{buildroot}%{_defaultdocdir}/%{name}/INSTALL
# Create empty ghost files for files created by update-smart-drivedb.
touch %{buildroot}%{_datadir}/smartmontools/drivedb.h.{error,lastcheck,old}

# Check syntax of drivedb.h that may come from a later snapshot (code from update-smart-drivedb)
if ./smartctl -B drivedb.h -P showall >/dev/null; then :; else
  echo "drivedb.h.error: rejected by smartctl, probably no longer compatible" >&2
  exit 1
fi
# Intelligent drivedb.h update, part 0.
# Check that drivedb.h has well formed svn RELEASE. We will need it for the intelligent update.
DRIVEDB_H_RELEASE_CHECK="$(sed -n 's/^.*$Id: drivedb.h \([0-9][0-9]*\) .*$/\1/p' <%{buildroot}%{_datadir}/smartmontools/drivedb.h)"
# Fail if the file has broken release number.
test "$DRIVEDB_H_RELEASE_CHECK" -ge 0
# Fail if there is no default_branch= in update-smart-drivedb
grep -q "^default_branch=\"[^\"]*\"$" update-smart-drivedb

%pre
%service_add_pre smartd.service smartd_generate_opts.path smartd_generate_opts.service
# Intelligent drivedb.h update, part 1.
# Extract drivedb.h branch for installed version. We will need it in %%post.
if test -f %{_sbindir}/update-smart-drivedb ; then
    BRANCH=
    eval $(grep "^BRANCH=\"[^\"]*\"$" /usr/sbin/update-smart-drivedb)
    if test -n "$BRANCH" ; then
	echo -n "$BRANCH" >%{_datadir}/smartmontools/drivedb.h.branch.rpmtemp
    fi
fi
# Save installed drivedb.h. Maybe the sysadmin called update-smart-drivedb,
# and the installed drivedb.h may be even newer than the new packaged one.
if test -f %{_datadir}/smartmontools/drivedb.h ; then
    # Be on safe side, remove any potential drivedb.h.rpmsave.
    rm -f %{_datadir}/smartmontools/drivedb.h.rpmsave
    ln %{_datadir}/smartmontools/drivedb.h %{_datadir}/smartmontools/drivedb.h.rpmsave
fi

%post
# First prepare sysconfig.
%{fillup_only}
# Up to Leap 42.3 and SLE 15 SP3 Maintenance Update there was a "Command" meta comment in the sysconfig file.
# It is not needed any more, but fillup does not delete it. Do it explicitly. (bsc#1195785, bsc#1196103)
sed -i '\@^##[[:space:]]*Command:[[:space:]]*/usr/lib/smartmontools/generate_smartd_opts$@d' /etc/sysconfig/smartmontools
# Then generate initial %%{_localstatedir}/lib/smartmontools/smartd_opts needed by smartd.service.
SMARTD_SKIP_INIT=1 %{_prefix}/lib/smartmontools/generate_smartd_opts
# No start by default here.. belongs to -presets packages
%service_add_post smartd.service smartd_generate_opts.path smartd_generate_opts.service
# Intelligent drivedb.h update, part 2.
# Now we have the old system drivedb.h.rpmsave and the new packaged drivedb.h.
if test -f %{_datadir}/smartmontools/drivedb.h.rpmsave ; then
    # Compare their release numbers.
    DRIVEDB_H_RELEASE_RPM="$(sed -n 's/^.*$Id: drivedb.h \([0-9][0-9]*\) .*$/\1/p' <%{_datadir}/smartmontools/drivedb.h)"
    DRIVEDB_H_RELEASE_SAVED="$(sed -n 's/^.*$Id: drivedb.h \([0-9][0-9]*\) .*$/\1/p' <%{_datadir}/smartmontools/drivedb.h.rpmsave)"
    # Note: The SAVED release number may be broken. The test syntax must cover it and replace old file.
    if test "$DRIVEDB_H_RELEASE_RPM" -lt "${DRIVEDB_H_RELEASE_SAVED:-0}" ; then
	# If it is an update to the new branch, always replace the database.
	# Extract drivedb.h branch for the new version to default_branch.
	eval $(grep "^default_branch=\"[^\"]*\"$" /usr/sbin/update-smart-drivedb)
	OLD_BRANCH=
	if test -f %{_datadir}/smartmontools/drivedb.h.branch.rpmtemp ; then
	    OLD_BRANCH=$(<%{_datadir}/smartmontools/drivedb.h.branch.rpmtemp)
	fi
	if test "$default_branch" = "$OLD_BRANCH" ; then
	    # It is safe to keep later version of installed database.
	    mv %{_datadir}/smartmontools/drivedb.h.rpmsave %{_datadir}/smartmontools/drivedb.h
	else
	    # Saved file needs to be replaced.
	    rm %{_datadir}/smartmontools/drivedb.h.rpmsave
	    # We returned to the vanilla packages, remove files created by update-smart-drivedb.
	    rm -f %{_datadir}/smartmontools/drivedb.h.{error,lastcheck,old}
	    echo >&2 "%{name} updated to a version that requires new branch of drivedb.h"
	    echo >&2 "Replacing your custom drivedb.h."
	    echo >&2 "You may need to call update-smart-drivedb."
	fi
    else
	# Saved file is older or equal, or saved file has broken release number.
	rm %{_datadir}/smartmontools/drivedb.h.rpmsave
	# We returned to the vanilla packages, remove files created by update-smart-drivedb.
	rm -f %{_datadir}/smartmontools/drivedb.h.{error,lastcheck,old}
    fi
fi
rm -f %{_datadir}/smartmontools/drivedb.h.branch.rpmtemp
# Before Leap 15 / SLE 15, there was a incorrect configuration of self tests (bsc#1073918).
# Perform a fix of this nonsense, even if the noreplace configuration file was edited.
if grep -q -F -- '-s S/../.././03 -s L/../(01|02|03|04|05|06|07)/7/01' %{_sysconfdir}/smartd.conf ; then
	sed -i 's:-s S/\.\./\.\./\./03 -s L/\.\./(01|02|03|04|05|06|07)/7/01:-s (S/../.././03|L/../(01|02|03|04|05|06|07)/7/01):g' %{_sysconfdir}/smartd.conf
fi

%preun
%service_del_preun smartd.service smartd_generate_opts.path smartd_generate_opts.service

%postun
%service_del_postun smartd.service smartd_generate_opts.path smartd_generate_opts.service
# Clean all attrlogs and state files.
if test "$1" = 0 ; then
    rm -rf %{_localstatedir}/lib/smartmontools
fi

%files
%defattr(-, root, root)
%doc %{_docdir}/%{name}
%dir %{_datadir}/smartmontools
%verify(not md5 size mtime) %{_datadir}/smartmontools/drivedb.h
%ghost %{_datadir}/smartmontools/drivedb.h.error
%ghost %{_datadir}/smartmontools/drivedb.h.lastcheck
%ghost %{_datadir}/smartmontools/drivedb.h.old
%doc %{_mandir}/man*/*
%dir %{_localstatedir}/lib/smartmontools
%ghost %{_localstatedir}/lib/smartmontools/smartd_opts
%{_prefix}/lib/smartmontools
%{_unitdir}/*
%{_sbindir}/*
%config(noreplace) %{_sysconfdir}/smart_drivedb.h
%config(noreplace) %{_sysconfdir}/smartd.conf
%config(noreplace) %{_sysconfdir}/smartd_warning.sh
%config %dir %{_sysconfdir}/smartd_warning.d
%{_fillupdir}/sysconfig.*

%changelog
