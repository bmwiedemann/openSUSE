#
# spec file for package apparmor
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2011-2024 Christian Boltz
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


%if 0%{?suse_version} >= 1550
%define sbindir %_sbindir
%define apparmor_bin_prefix /usr/lib/apparmor
%else
%define sbindir /sbin
%define apparmor_bin_prefix /lib/apparmor
%endif

%if 0%{?suse_version} <= 1500
# _pamdir isn't defined in 15.x
%define _pamdir /%{_lib}/security
%endif

# warning - confusing syntax ahead ;-)
# bcond_with means "disable"
# bcond_without means "enable"
%bcond_with tomcat
%bcond_without pam
%bcond_without apache
%bcond_without perl
%bcond_without python3
%bcond_without ruby

%if 0%{?suse_version} <= 1550
# enable precompiled profile cache on <= 15.x
%bcond_without precompiled_cache
%else
# don't build precompiled profile cache on Tumbleweed as long as it's purely validated based on timestamps (boo#1205659)
%bcond_with precompiled_cache
%endif

%define CATALINA_HOME /usr/share/tomcat6
%define JAR_FILE changeHatValve.jar

%define tarversion v4.0.1
%define pyeggversion 4.0.1

Name:           apparmor
Version:        4.0.1
Release:        0
Summary:        AppArmor userlevel parser utility
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://gitlab.com/apparmor/apparmor/
Source0:        https://gitlab.com/apparmor/apparmor/-/archive/%{tarversion}/apparmor-%{tarversion}.tar.gz
# from https://gitlab.com/apparmor/apparmor/-/wikis/%{version}_Signatures
Source1:        apparmor-%{tarversion}.tar.gz.asc
Source2:        %{name}.keyring

Source6:        baselibs.conf
Source7:        apparmor-rpmlintrc

# enable caching of profiles (= massive performance speedup when loading profiles)
# and set cache-loc in parser.conf and apparmor.service accordingly
Patch1:         apparmor-enable-profile-cache.diff

# bug 906858 - confine lessopen.sh (submitted upstream 2014-12-21)
Patch4:         apparmor-lessopen-profile.patch

# make <apache2.d> include in apache extra profile optional to make openQA happy (boo#1178527)
Patch6:         apache-extra-profile-include-if-exists.diff

# add path for precompiled cache (only done/applied if precompiled_cache is enabled)
Patch7:         apparmor-enable-precompiled-cache.diff

# fix redefinition of _ in tools (merged upstream 2024-04-22 https://gitlab.com/apparmor/apparmor/-/merge_requests/1218)
Patch10:        tools-fix-redefinition.diff

# make test-aa-notify a bit more relaxed to allow different argparse wording on Leap 15.5 (merged upstream 2024-05-06 (4.0 and master) https://gitlab.com/apparmor/apparmor/-/merge_requests/1226)
Patch11:        test-aa-notify.diff

# Fix aa-remove-unknown for 'unconfined' profiles (merged upstream 2024-05-28 in 4.0 and master https://gitlab.com/apparmor/apparmor/-/merge_requests/1240)
Patch12:        aa-remove-unknown-fix-unconfined.diff

# Fix aa-teardown for 'unconfined' profiles (submitted upstream 2024-05-28 https://gitlab.com/apparmor/apparmor/-/merge_requests/1242)
Patch13:        teardown-unconfined.diff

# Relax handling of mount rules in utils to avoid errors when parsing valid profiles (both patches taken from upstream 4.0 branch 2024-05-28)
Patch14:        utils-relax-mount-rules.diff
Patch15:        utils-relax-mount-rules-2.diff

# Fix QtWebEngineProcess path in plasmashell profile (merged upstream 2024-06-04 in 4.0 and master - https://gitlab.com/apparmor/apparmor/-/merge_requests/1248)
Patch16:        plasmashell.diff

# latest sddm uses yet another path for xauth (submitted upstream 2024-06-04 https://gitlab.com/apparmor/apparmor/-/merge_requests/1249)
Patch17:        sddm-xauth.diff

# utils MountRule: add support for quoted paths and empty source (master merged upstream 2024-06-11, 4.0 branch submitted upstream 2024-06-11 https://gitlab.com/apparmor/apparmor/-/merge_requests/1259)
Patch18:        logprof-mount-empty-source.diff

#  samba-dcerpcd: allow to execute rpcd_witness (submitted upstream 2024-06-08 https://gitlab.com/apparmor/apparmor/-/merge_requests/1256, packaged patch adjusted to match the packaged samba-rpcd profile)
Patch19:        sampa-rpcd-witness.diff

PreReq:         sed
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  dejagnu
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  iproute2
BuildRequires:  libtool
BuildRequires:  pcre-devel
BuildRequires:  pkg-config
BuildRequires:  python3
BuildRequires:  swig
BuildRequires:  perl(Locale::gettext)

%if %{with python3}
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-notify2
BuildRequires:  python3-psutil
BuildRequires:  python3-setuptools
%endif

%if %{with ruby}
BuildRequires:  ruby-devel
%endif

%if %{with apache}
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
%endif

%if %{with tomcat}
BuildRequires:  ant
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  tomcat6
%endif

%package parser
Summary:        AppArmor userlevel parser utility
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
Conflicts:      apparmor-utils < 3.0
Obsoletes:      libimnxcert < 2.9
Obsoletes:      subdomain-leaf-cert < 2.9
Obsoletes:      subdomain-parser < 2.9
Obsoletes:      subdomain-parser-common < 2.9
Obsoletes:      subdomain-parser-demo < 2.9
Obsoletes:      subdomain_parser < 2.9
Provides:       libimnxcert = %{version}
Provides:       subdomain-leaf-cert = %{version}
Provides:       subdomain-parser = %{version}
Provides:       subdomain-parser-common = %{version}
Provides:       subdomain-parser-demo = %{version}
Provides:       subdomain_parser = %{version}
Provides:       apparmor-parser(CAP_SYSLOG)
BuildRequires:  systemd-rpm-macros
%{?systemd_ordering}

%description parser
The AppArmor Parser is a userlevel program that is used to load in
program profiles to the AppArmor Security kernel module.

This package is part of a suite of tools that used to be named
SubDomain.

%package docs
Summary:        AppArmor Documentation package
License:        GPL-2.0-or-later
Group:          Documentation/Other
BuildArch:      noarch

%description docs
This package contains documentation for AppArmor.

This package is part of a suite of tools that used to be named
SubDomain.

%if %{with apache}

%package -n apache2-mod_apparmor
Summary:        AppArmor module for apache2
License:        GPL-2.0-or-later
Group:          Productivity/Security

%description -n apache2-mod_apparmor
apache2-modapparmor adds support to apache2 to provide AppArmor
confinement to individual cgi scripts handled by apache modules like
mod_php and mod_perl.

This package is part of a suite of tools that used to be named
SubDomain.

The documentation is in the apparmor-admin_en package.

%endif

%if %{with perl}

%package -n perl-apparmor
Summary:        Perl interface for libapparmor functions
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          Development/Libraries/Perl
Requires:       libapparmor1 = %{version}
Requires:       perl = %{perl_version}
Provides:       perl-libapparmor = %{version}
Obsoletes:      perl-libapparmor < 2.5

%description -n perl-apparmor
This package provides the perl interface to AppArmor. It is used for perl
applications interfacing with AppArmor.

%endif

%if %{with python3}

%package -n python3-apparmor
Summary:        Python 3 interface for libapparmor functions
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          Development/Libraries/Python
Requires:       libapparmor1 = %{version}
Requires:       python3
Requires:       python(abi) = %{py3_ver}

%description -n python3-apparmor
This package provides the python interface to AppArmor. It is used for python
applications interfacing with AppArmor.

%endif

%if %{with ruby}

%package -n ruby-apparmor
Summary:        Ruby interface for libapparmor functions
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          Development/Languages/Ruby
Requires:       libapparmor1 = %{version}
Requires:       ruby = %(rpm -q --qf '%%{version}' ruby)
Provides:       ruby-libapparmor = %{version}
Obsoletes:      ruby-libapparmor < 2.5

%description -n ruby-apparmor
This package provides the ruby interface to AppArmor. It is used for ruby
applications interfacing with AppArmor.

%endif

%package abstractions
Summary:        AppArmor abstractions and directory structure
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          Productivity/Security
Requires:       apparmor-parser(CAP_SYSLOG)
BuildArch:      noarch

%description abstractions
AppArmor abstractions (common parts used in various profiles) and
the /etc/apparmor.d/ directory structure.

AppArmor is a file and network mandatory access control mechanism.
AppArmor confines processes to the resources allowed by the systems
administrator and can constrain the scope of potential security
vulnerabilities.

This package is part of a suite of tools that used to be named
SubDomain.

%package profiles
Summary:        AppArmor profiles that are loaded into the apparmor kernel module
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          Productivity/Security
Requires:       apparmor-abstractions >= %{version}
Requires:       apparmor-parser(CAP_SYSLOG)
Obsoletes:      subdomain-profiles < 2.9
Provides:       subdomain-profiles = %{version}
BuildArch:      noarch

%description profiles
Base profiles. AppArmor is a file and network mandatory access control
mechanism. AppArmor confines processes to the resources allowed by the
systems administrator and can constrain the scope of potential security
vulnerabilities.

This package is part of a suite of tools that used to be named
SubDomain.

%package utils
Summary:        AppArmor User-Level Utilities Useful for Creating AppArmor Profiles
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          Productivity/Security
Requires:       apparmor-parser
Requires:       libapparmor1 = %{version}
Requires:       python3-apparmor = %{version}
Requires:       python3-base
Requires:       python3-notify2
Requires:       python3-psutil
# aa-unconfined needs ss
Recommends:     iproute2
BuildArch:      noarch

%description utils
This package provides the aa-logprof, aa-genprof, aa-autodep,
aa-enforce, and aa-complain tools to assist with profile authoring.
Besides it provides the aa-unconfined server information tool.
It is part of a suite of tools that used to be named SubDomain.

%if %{with tomcat}

%package -n tomcat_apparmor
Summary:        Tomcat 6 plugin for AppArmor change_hat
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          System/Libraries
Requires:       libapparmor1 = %{version}
Requires:       tomcat6

%description -n tomcat_apparmor
tomcat_apparmor - is a plugin for Apache Tomcat version 6 that
provides support for AppArmor change_hat for creating AppArmor
containers that are bound to discrete elements of processing within the
Tomcat servlet container. The AppArmor containers, or "hats", can be
created for individual URL processing or per servlet.

%endif

%if %{with pam}

%package -n pam_apparmor
Summary:        PAM module for AppArmor change_hat
License:        GPL-2.0-only AND LGPL-2.1-or-later
Group:          Productivity/Security
BuildRequires:  pam-devel
PreReq:         pam
PreReq:         pam-config
Requires:       pam
Requires:       pam-config

%description -n pam_apparmor
The pam_apparmor module provides the means for any PAM applications
that call pam_open_session() to automatically perform an AppArmor
change_hat operation in order to switch to a user-specific security
policy.

%endif

%description
The AppArmor Parser is a userlevel program that is used to load in
program profiles to the AppArmor Security kernel module.

This package is part of a suite of tools that used to be named
SubDomain.

%lang_package -n apparmor-utils
%lang_package -n apparmor-parser

%prep
%setup -q -n %{name}-%{tarversion}

# very loose profile that doesn't even match the apache2 binary path in openSUSE. Move it away instead of confusing people (boo#872984)
mv -v profiles/apparmor.d/usr.lib.apache2.mpm-prefork.apache2 profiles/apparmor/profiles/extras/

%patch -P 1
%patch -P 4
%patch -P 6
%if %{with precompiled_cache}
%patch -P 7
%endif
%patch -P 10 -p1
%patch -P 11 -p1
%patch -P 12 -p1
%patch -P 13 -p1
%patch -P 14 -p1
%patch -P 15 -p1
%patch -P 16 -p1
%patch -P 17 -p1
%patch -P 18 -p1
%patch -P 19 -p1

%build
export SUSE_ASNEEDED=0

# libapparmor:
(
  cd ./libraries/libapparmor
  sh ./autogen.sh && \
  %configure \
%if %{with perl}
  --with-perl \
%endif
%if %{with python3}
  --with-python \
%else
  --without-python \
%endif
%if %{with ruby}
  --with-ruby \
%else
  --without-ruby \
%endif

  make
)

# Utilities:
make -C utils

# binutils
make -C binutils

# parser:
make -C parser V=1

# Apache mod_apparmor:
%if %{with apache}
  make -C changehat/mod_apparmor
%endif

# PAM AppArmor:
%if %{with pam}
  make -C changehat/pam_apparmor
%endif

# Profiles:
make -C profiles

%if %{with tomcat}
  make -C changehat/tomcat_apparmor/tomcat_5_5 CATALINA_HOME=%{CATALINA_HOME}
%endif

# pre-build profile cache
# note that -L only works with an absolute path, therefore prefix it with $(pwd)
%if %{with precompiled_cache}
parser/apparmor_parser --config-file $(pwd)/parser/parser.conf --write-cache -QT  -L $(pwd)/profiles/cache -I profiles/apparmor.d/ profiles/apparmor.d/
%endif

# create filelist of previously (up to 3.1.x) shipped local/* files
# (adding them as %ghost prevents modified files from being moved to *.rpmsave)
for oldlocal in \
    bin.ping lsb_release nvidia_modprobe php-fpm samba-bgqd samba-dcerpcd samba-rpcd samba-rpcd-classic samba-rpcd-spoolss sbin.klogd sbin.syslogd sbin.syslog-ng \
    usr.bin.lessopen.sh usr.lib.dovecot.anvil usr.lib.dovecot.auth usr.lib.dovecot.config usr.lib.dovecot.deliver usr.lib.dovecot.dict usr.lib.dovecot.director \
    usr.lib.dovecot.doveadm-server usr.lib.dovecot.dovecot-auth usr.lib.dovecot.dovecot-lda usr.lib.dovecot.imap usr.lib.dovecot.imap-login usr.lib.dovecot.lmtp \
    usr.lib.dovecot.log usr.lib.dovecot.managesieve usr.lib.dovecot.managesieve-login usr.lib.dovecot.pop3 usr.lib.dovecot.pop3-login usr.lib.dovecot.replicator \
    usr.lib.dovecot.script-login usr.lib.dovecot.ssl-params usr.lib.dovecot.stats usr.sbin.apache2 usr.sbin.avahi-daemon usr.sbin.dnsmasq usr.sbin.dovecot \
    usr.sbin.identd usr.sbin.mdnsd usr.sbin.nmbd usr.sbin.nscd usr.sbin.ntpd usr.sbin.smbd usr.sbin.smbd-shares usr.sbin.smbldap-useradd  usr.sbin.traceroute \
    usr.sbin.winbindd zgrep
do
    echo "%ghost %config %attr(0644,root,root) /etc/apparmor.d/local/$oldlocal"
done > oldlocal.files

%check
make check -C libraries/libapparmor
make check -C parser
make check -C binutils

# some tests depend on kernel LSM (e.g. access /proc/PID/attr/apparmor/current)
if grep -q apparmor /sys/kernel/security/lsm; then
	# profiles make check fails for the utils (they expect
	# /sbin/apparmor_parser to exist), therefore only do parser-based check
	make -C profiles check-parser

%if %{with precompiled_cache}
	# test for a few files that should exist in the cache
	test -f profiles/cache/*/bin.ping
	test -f profiles/cache/*/.features
%endif

	# run checks in utils except linting -- https://gitlab.com/apparmor/apparmor/-/issues/121
	make check -o check_lint -C utils
else
	# clear grep status to avoid flagging check failure
	true
fi

%install
# libapparmor: swig bindings only, libapparmor is packaged via libapparmor.spec
%makeinstall -C libraries/libapparmor/swig

# utilities
%makeinstall -C utils
test ! -x %{buildroot}/%{_bindir}/aa-easyprof && chmod +x %{buildroot}/%{_bindir}/aa-easyprof # https://bugs.launchpad.net/apparmor/+bug/1366568
mkdir -p %{buildroot}%{_localstatedir}/log/apparmor

# binutils
%makeinstall -C binutils
( cd %{buildroot}/%{_sbindir} && ln -s %{_bindir}/aa-exec exec )

%makeinstall -C profiles

%if %{with precompiled_cache}
install -d -m 755 %{buildroot}/usr/share/apparmor/cache
echo -e "\n\n    *** WARNING: precompiling cache is known to fail under 'osc build' - use 'osc build --vm-type kvm' instead or skip building the precompiled cache with 'osc build --without precompiled_cache' ***\n\n"
# ensure cache files are newer than (text) profiles by sleeping a few seconds, and using cp -r which updates the timestamps
sleep 2
cp -r profiles/cache/* %{buildroot}/usr/share/apparmor/cache
test -f %{buildroot}/usr/share/apparmor/cache/*/.features
test -f %{buildroot}/usr/share/apparmor/cache/*/bin.ping
%endif

%makeinstall SBINDIR="%{buildroot}%{sbindir}" APPARMOR_BIN_PREFIX="%{buildroot}%{apparmor_bin_prefix}" -C parser
# default cache dir (starting with 2.13) is /etc/apparmor.d/cache.d - also not the best location
# Use /var/cache/apparmor and make /etc/apparmor.d/cache.d a symlink to it
mkdir -p %{buildroot}%{_localstatedir}/cache/apparmor
( cd %{buildroot}/%{_sysconfdir}/apparmor.d/ && ln -s ../../%{_localstatedir}/cache/apparmor cache.d )

%if %{with apache}
  %makeinstall -C changehat/mod_apparmor
%endif

%if %{with pam}
  %makeinstall -C changehat/pam_apparmor SECDIR=%{buildroot}%{_pamdir}
%endif

%if %{with tomcat}
  mkdir -p %{buildroot}/%{CATALINA_HOME}
  %makeinstall -C changehat/tomcat_apparmor/tomcat_5_5 CATALINA_HOME=%{buildroot}/%{CATALINA_HOME}
%endif

find %{buildroot} -name .packlist -exec rm -vf {} \;
find %{buildroot} -name perllocal.pod -exec rm -vf {} \;

# Re-create the links to the old names, but only for tools and manpages that had it for historic reasons[tm].
# Tools and manpages added in >= 2.9 won't get symlinks without aa- prefix
for file in %{buildroot}%{_prefix}/{sbin,share/man/man[0-9]}/aa-*; do
    d=$(dirname $file)
    f=$(basename $file)
    case "${f#aa-}" in
        audit    | autodep    | complain    | decode | disable                  | enforce    | exec    | genprof    | logprof    | notify   | status   | unconfined  | \
        audit.8* | autodep.8* | complain.8*          | disable.8* | easyprof.8* | enforce.8* | exec.1* | genprof.8* | logprof.8* | notify.8 | status.8 | unconfined.8* )
            if [ "${f#aa-}" != "$f" ]; then
                ln -s $f $d/${f#aa-}
            fi
        ;;
    esac
done

mv -f %{buildroot}%{_mandir}/man8/{status.8,apparmor_status.8}
mv -f %{buildroot}%{_mandir}/man8/{notify.8,apparmor_notify.8}
rm -f %{buildroot}%{_mandir}/man8/decode.8

for pkg in apparmor-utils apparmor-parser aa-binutils; do
    %find_lang $pkg
done

# remove *.la files
rm -fv %{buildroot}%{_libdir}/libapparmor.la

%files docs
%defattr(-,root,root)
%doc parser/*.[1-9].html
%doc utils/vim/apparmor.vim.5.html
%doc common/apparmor.css
#doc parser/techdoc.pdf
# apparmor.vim is included in the vim package. Ideally it should be in a -devel package, but that's overmuch for one file
%dir %{_datadir}/apparmor
%{_datadir}/apparmor/apparmor.vim

%files parser
%defattr(-,root,root)
%license parser/COPYING.GPL
%doc parser/README
%{sbindir}/apparmor_parser
%{_bindir}/aa-enabled
%{_bindir}/aa-exec
%{_bindir}/aa-features-abi
%{_sbindir}/aa-load
%{_sbindir}/aa-status
%{_sbindir}/apparmor_status
%{_sbindir}/status
%{_sbindir}/aa-teardown
%{_sbindir}/exec
%dir %attr(-, root, root) %{_sysconfdir}/apparmor
%dir %{_sysconfdir}/apparmor.d
%{_sysconfdir}/apparmor.d/cache.d
%{sbindir}/rcapparmor
%{_unitdir}/apparmor.service
%config(noreplace) %{_sysconfdir}/apparmor/parser.conf
%{_localstatedir}/cache/apparmor
%dir %attr(-, root, root) %{apparmor_bin_prefix}
%{apparmor_bin_prefix}/rc.apparmor.functions
%{apparmor_bin_prefix}/apparmor.systemd
%{apparmor_bin_prefix}/profile-load
%doc %{_mandir}/man1/aa-enabled.1.gz
%doc %{_mandir}/man1/aa-exec.1.gz
%doc %{_mandir}/man1/aa-features-abi.1.gz
%doc %{_mandir}/man1/exec.1.gz
%doc %{_mandir}/man5/apparmor.d.5.gz
%doc %{_mandir}/man5/apparmor.vim.5.gz
%doc %{_mandir}/man7/apparmor.7.gz
%doc %{_mandir}/man7/apparmor_xattrs.7.gz
%doc %{_mandir}/man8/aa-status.8.gz
%doc %{_mandir}/man8/aa-teardown.8.gz
%doc %{_mandir}/man8/apparmor_parser.8.gz
%doc %{_mandir}/man8/apparmor_status.8.gz

%pre parser
%service_add_pre apparmor.service

%files parser-lang -f apparmor-parser.lang -f aa-binutils.lang
%defattr(-,root,root)

%files abstractions
%defattr(644,root,root,755)
%dir %{_sysconfdir}/apparmor.d/
%dir %{_sysconfdir}/apparmor.d/abi
%config(noreplace) %{_sysconfdir}/apparmor.d/abi/3.0
%config(noreplace) %{_sysconfdir}/apparmor.d/abi/4.0
%config(noreplace) %{_sysconfdir}/apparmor.d/abi/kernel-5.4-outoftree-network
%config(noreplace) %{_sysconfdir}/apparmor.d/abi/kernel-5.4-vanilla
%dir %{_sysconfdir}/apparmor.d/abstractions
%config(noreplace) %{_sysconfdir}/apparmor.d/abstractions/*
%dir %{_sysconfdir}/apparmor.d/disable
%dir %{_sysconfdir}/apparmor.d/local
%dir %{_sysconfdir}/apparmor.d/tunables
%config(noreplace) %{_sysconfdir}/apparmor.d/tunables/*

%files profiles -f oldlocal.files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/apparmor.d/apache2.d
%config(noreplace) %{_sysconfdir}/apparmor.d/bin.*
%config(noreplace) %{_sysconfdir}/apparmor.d/sbin.*
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.*

%config(noreplace) %{_sysconfdir}/apparmor.d/1password
%config(noreplace) %{_sysconfdir}/apparmor.d/Discord
%config(noreplace) %{_sysconfdir}/apparmor.d/MongoDB_Compass
%config(noreplace) %{_sysconfdir}/apparmor.d/QtWebEngineProcess
%config(noreplace) %{_sysconfdir}/apparmor.d/brave
%config(noreplace) %{_sysconfdir}/apparmor.d/buildah
%config(noreplace) %{_sysconfdir}/apparmor.d/busybox
%config(noreplace) %{_sysconfdir}/apparmor.d/cam
%config(noreplace) %{_sysconfdir}/apparmor.d/ch-checkns
%config(noreplace) %{_sysconfdir}/apparmor.d/ch-run
%config(noreplace) %{_sysconfdir}/apparmor.d/chrome
%config(noreplace) %{_sysconfdir}/apparmor.d/code
# exclude crun, podman and runc profiles until the updated container engines (including updated profile with "signal peer=runc") has arrived
#config(noreplace) %{_sysconfdir}/apparmor.d/crun
%exclude %{_sysconfdir}/apparmor.d/crun
%exclude %{_sysconfdir}/apparmor.d/podman
%exclude %{_sysconfdir}/apparmor.d/runc
%config(noreplace) %{_sysconfdir}/apparmor.d/devhelp
%config(noreplace) %{_sysconfdir}/apparmor.d/element-desktop
%config(noreplace) %{_sysconfdir}/apparmor.d/epiphany
%config(noreplace) %{_sysconfdir}/apparmor.d/evolution
%config(noreplace) %{_sysconfdir}/apparmor.d/firefox
%config(noreplace) %{_sysconfdir}/apparmor.d/flatpak
%config(noreplace) %{_sysconfdir}/apparmor.d/foliate
%config(noreplace) %{_sysconfdir}/apparmor.d/geary
%config(noreplace) %{_sysconfdir}/apparmor.d/github-desktop
%config(noreplace) %{_sysconfdir}/apparmor.d/goldendict
%config(noreplace) %{_sysconfdir}/apparmor.d/ipa_verify
%config(noreplace) %{_sysconfdir}/apparmor.d/kchmviewer
%config(noreplace) %{_sysconfdir}/apparmor.d/keybase
%config(noreplace) %{_sysconfdir}/apparmor.d/lc-compliance
%config(noreplace) %{_sysconfdir}/apparmor.d/libcamerify
%config(noreplace) %{_sysconfdir}/apparmor.d/linux-sandbox
%config(noreplace) %{_sysconfdir}/apparmor.d/loupe
%config(noreplace) %{_sysconfdir}/apparmor.d/lsb_release
%config(noreplace) %{_sysconfdir}/apparmor.d/lxc-attach
%config(noreplace) %{_sysconfdir}/apparmor.d/lxc-create
%config(noreplace) %{_sysconfdir}/apparmor.d/lxc-destroy
%config(noreplace) %{_sysconfdir}/apparmor.d/lxc-execute
%config(noreplace) %{_sysconfdir}/apparmor.d/lxc-stop
%config(noreplace) %{_sysconfdir}/apparmor.d/lxc-unshare
%config(noreplace) %{_sysconfdir}/apparmor.d/lxc-usernsexec
%config(noreplace) %{_sysconfdir}/apparmor.d/mmdebstrap
%config(noreplace) %{_sysconfdir}/apparmor.d/msedge
%config(noreplace) %{_sysconfdir}/apparmor.d/nautilus
%config(noreplace) %{_sysconfdir}/apparmor.d/notepadqq
%config(noreplace) %{_sysconfdir}/apparmor.d/nvidia_modprobe
%config(noreplace) %{_sysconfdir}/apparmor.d/obsidian
%config(noreplace) %{_sysconfdir}/apparmor.d/opam
%config(noreplace) %{_sysconfdir}/apparmor.d/opera
%config(noreplace) %{_sysconfdir}/apparmor.d/pageedit
%config(noreplace) %{_sysconfdir}/apparmor.d/plasmashell
%config(noreplace) %{_sysconfdir}/apparmor.d/php-fpm
%config(noreplace) %{_sysconfdir}/apparmor.d/polypane
%config(noreplace) %{_sysconfdir}/apparmor.d/privacybrowser
%config(noreplace) %{_sysconfdir}/apparmor.d/qcam
%config(noreplace) %{_sysconfdir}/apparmor.d/qmapshack
%config(noreplace) %{_sysconfdir}/apparmor.d/qutebrowser
%config(noreplace) %{_sysconfdir}/apparmor.d/rootlesskit
%config(noreplace) %{_sysconfdir}/apparmor.d/rpm
%config(noreplace) %{_sysconfdir}/apparmor.d/rssguard
#config(noreplace) %{_sysconfdir}/apparmor.d/runc
%config(noreplace) %{_sysconfdir}/apparmor.d/samba-bgqd
%config(noreplace) %{_sysconfdir}/apparmor.d/samba-dcerpcd
%config(noreplace) %{_sysconfdir}/apparmor.d/samba-rpcd
%config(noreplace) %{_sysconfdir}/apparmor.d/samba-rpcd-*
%config(noreplace) %{_sysconfdir}/apparmor.d/sbuild
%config(noreplace) %{_sysconfdir}/apparmor.d/sbuild-abort
%config(noreplace) %{_sysconfdir}/apparmor.d/sbuild-adduser
%config(noreplace) %{_sysconfdir}/apparmor.d/sbuild-apt
%config(noreplace) %{_sysconfdir}/apparmor.d/sbuild-checkpackages
%config(noreplace) %{_sysconfdir}/apparmor.d/sbuild-clean
%config(noreplace) %{_sysconfdir}/apparmor.d/sbuild-createchroot
%config(noreplace) %{_sysconfdir}/apparmor.d/sbuild-destroychroot
%config(noreplace) %{_sysconfdir}/apparmor.d/sbuild-distupgrade
%config(noreplace) %{_sysconfdir}/apparmor.d/sbuild-hold
%config(noreplace) %{_sysconfdir}/apparmor.d/sbuild-shell
%config(noreplace) %{_sysconfdir}/apparmor.d/sbuild-unhold
%config(noreplace) %{_sysconfdir}/apparmor.d/sbuild-update
%config(noreplace) %{_sysconfdir}/apparmor.d/sbuild-upgrade
%config(noreplace) %{_sysconfdir}/apparmor.d/scide
%config(noreplace) %{_sysconfdir}/apparmor.d/signal-desktop
%config(noreplace) %{_sysconfdir}/apparmor.d/slack
%config(noreplace) %{_sysconfdir}/apparmor.d/slirp4netns
%config(noreplace) %{_sysconfdir}/apparmor.d/steam
%config(noreplace) %{_sysconfdir}/apparmor.d/stress-ng
%config(noreplace) %{_sysconfdir}/apparmor.d/surfshark
%config(noreplace) %{_sysconfdir}/apparmor.d/systemd-coredump
%config(noreplace) %{_sysconfdir}/apparmor.d/thunderbird
%config(noreplace) %{_sysconfdir}/apparmor.d/toybox
%config(noreplace) %{_sysconfdir}/apparmor.d/transmission
%config(noreplace) %{_sysconfdir}/apparmor.d/trinity
%config(noreplace) %{_sysconfdir}/apparmor.d/tup
%config(noreplace) %{_sysconfdir}/apparmor.d/tuxedo-control-center
%config(noreplace) %{_sysconfdir}/apparmor.d/unix-chkpwd
%config(noreplace) %{_sysconfdir}/apparmor.d/unprivileged_userns
%config(noreplace) %{_sysconfdir}/apparmor.d/userbindmount
%config(noreplace) %{_sysconfdir}/apparmor.d/uwsgi-core
%config(noreplace) %{_sysconfdir}/apparmor.d/vdens
%config(noreplace) %{_sysconfdir}/apparmor.d/virtiofsd
%config(noreplace) %{_sysconfdir}/apparmor.d/vivaldi-bin
%config(noreplace) %{_sysconfdir}/apparmor.d/vpnns
%config(noreplace) %{_sysconfdir}/apparmor.d/wpcom
%config(noreplace) %{_sysconfdir}/apparmor.d/zgrep

%config(noreplace) %{_sysconfdir}/apparmor.d/apache2.d/phpsysinfo
%config(noreplace) %{_sysconfdir}/apparmor.d/local/README
%dir /usr/share/apparmor/
%if %{with precompiled_cache}
/usr/share/apparmor/cache/
%endif
/usr/share/apparmor/extra-profiles/

%files utils
%defattr(-,root,root)
%dir %{_sysconfdir}/apparmor
%config(noreplace) %{_sysconfdir}/apparmor/easyprof.conf
%config(noreplace) %{_sysconfdir}/apparmor/logprof.conf
%config(noreplace) %{_sysconfdir}/apparmor/notify.conf
%config(noreplace) %{_sysconfdir}/apparmor/severity.db
%{_sbindir}/aa-audit
%{_sbindir}/aa-autodep
%{_sbindir}/aa-cleanprof
%{_sbindir}/aa-complain
%{_sbindir}/aa-decode
%{_sbindir}/aa-disable
%{_sbindir}/aa-enforce
%{_sbindir}/aa-genprof
%{_sbindir}/aa-logprof
%{_sbindir}/aa-mergeprof
%{_sbindir}/aa-notify
%{_sbindir}/aa-remove-unknown
%{_sbindir}/aa-unconfined
%{_sbindir}/audit
%{_sbindir}/autodep
%{_sbindir}/complain
%{_sbindir}/decode
%{_sbindir}/disable
%{_sbindir}/enforce
%{_sbindir}/genprof
%{_sbindir}/logprof
%{_sbindir}/notify
%{_sbindir}/unconfined
%{_bindir}/aa-easyprof
%dir %{_datadir}/apparmor
%{_datadir}/apparmor/easyprof/
%dir %{_localstatedir}/log/apparmor
%doc %{_mandir}/man5/logprof.conf.5.gz
%doc %{_mandir}/man8/apparmor_notify.8.gz
%doc %{_mandir}/man8/aa-audit.8.gz
%doc %{_mandir}/man8/aa-autodep.8.gz
%doc %{_mandir}/man8/aa-cleanprof.8.gz
%doc %{_mandir}/man8/aa-complain.8.gz
%doc %{_mandir}/man8/aa-decode.8.gz
%doc %{_mandir}/man8/aa-disable.8.gz
%doc %{_mandir}/man8/aa-easyprof.8.gz
%doc %{_mandir}/man8/aa-enforce.8.gz
%doc %{_mandir}/man8/aa-genprof.8.gz
%doc %{_mandir}/man8/aa-logprof.8.gz
%doc %{_mandir}/man8/aa-mergeprof.8.gz
%doc %{_mandir}/man8/aa-notify.8.gz
%doc %{_mandir}/man8/aa-remove-unknown.8.gz
%doc %{_mandir}/man8/aa-unconfined.8.gz
%doc %{_mandir}/man8/audit.8.gz
%doc %{_mandir}/man8/autodep.8.gz
%doc %{_mandir}/man8/complain.8.gz
%doc %{_mandir}/man8/disable.8.gz
%doc %{_mandir}/man8/easyprof.8.gz
%doc %{_mandir}/man8/enforce.8.gz
%doc %{_mandir}/man8/genprof.8.gz
%doc %{_mandir}/man8/logprof.8.gz
%doc %{_mandir}/man8/unconfined.8.gz
%doc utils/*.[0-9].html
%doc common/apparmor.css

%files utils-lang -f apparmor-utils.lang

%if %{with perl}
%files -n perl-apparmor
%defattr(-,root,root)
%{perl_vendorarch}/auto/LibAppArmor/
%{perl_vendorarch}/LibAppArmor.pm
%endif

%if %{with python3}

%files -n python3-apparmor
%defattr(-,root,root)
%{python3_sitearch}/LibAppArmor-%{pyeggversion}-py*.egg-info
%dir %{python3_sitearch}/LibAppArmor
%dir %{python3_sitearch}/LibAppArmor/__pycache__
%{python3_sitearch}/LibAppArmor/_LibAppArmor.cpython-*.so
%{python3_sitearch}/LibAppArmor/__pycache__/__init__.cpython-*.pyc
%{python3_sitearch}/LibAppArmor/__pycache__/LibAppArmor.cpython-*.pyc
%{python3_sitearch}/LibAppArmor/__init__.py
%{python3_sitearch}/LibAppArmor/LibAppArmor.py
%{python3_sitelib}/apparmor/
%{python3_sitelib}/apparmor-%{pyeggversion}-py*.egg-info
%endif

%if %{with ruby}

%files -n ruby-apparmor
%defattr(-,root,root)
%{rb_sitearchdir}/LibAppArmor.so
%endif

%if %{with pam}

%files -n pam_apparmor
%defattr(444,root,root,755)
%attr(555,root,root) %{_pamdir}/pam_apparmor.so
%doc changehat/pam_apparmor/README
%endif

%if %{with tomcat}

%files -n tomcat_apparmor
%defattr(-,root,root)
%{CATALINA_HOME}/lib/%{JAR_FILE}
%{_libdir}/libJNI*
%doc %attr(0644,root,root) changehat/tomcat_apparmor/tomcat_5_5/README.tomcat_apparmor
%endif

%if %{with apache}

%files -n apache2-mod_apparmor
%defattr(-,root,root)
%{apache_libexecdir}/mod_apparmor.so
%doc %{_mandir}/man8/mod_apparmor.8.gz
%endif

%post parser
%service_add_post apparmor.service

%preun parser
%service_del_preun apparmor.service

%postun parser
# bnc#853019 aka boo#853019 is still a thing, but in the meantime apparmor.service has ExecStop=/bin/true (= do nothing),
# which means that 'systemctl restart apparmor' is safe now
%service_del_postun apparmor.service

%posttrans abstractions
# workaround for bnc#904620#c8 / lp#1392042
rm -f /var/cache/apparmor/* 2>/dev/null
#restart_on_update apparmor - but non-broken (bnc#853019)
systemctl is-active -q apparmor && systemctl reload apparmor ||:

%post profiles
# delete old cache (location up to 2.12)
rm -f /var/lib/apparmor/cache/* 2>/dev/null

# cleanup old, unchanged local/* files
for oldlocal in \
    bin.ping lsb_release nvidia_modprobe php-fpm samba-bgqd samba-dcerpcd samba-rpcd samba-rpcd-classic samba-rpcd-spoolss sbin.klogd sbin.syslogd sbin.syslog-ng \
    usr.bin.lessopen.sh usr.lib.dovecot.anvil usr.lib.dovecot.auth usr.lib.dovecot.config usr.lib.dovecot.deliver usr.lib.dovecot.dict usr.lib.dovecot.director \
    usr.lib.dovecot.doveadm-server usr.lib.dovecot.dovecot-auth usr.lib.dovecot.dovecot-lda usr.lib.dovecot.imap usr.lib.dovecot.imap-login usr.lib.dovecot.lmtp \
    usr.lib.dovecot.log usr.lib.dovecot.managesieve usr.lib.dovecot.managesieve-login usr.lib.dovecot.pop3 usr.lib.dovecot.pop3-login usr.lib.dovecot.replicator \
    usr.lib.dovecot.script-login usr.lib.dovecot.ssl-params usr.lib.dovecot.stats usr.sbin.apache2 usr.sbin.avahi-daemon usr.sbin.dnsmasq usr.sbin.dovecot \
    usr.sbin.identd usr.sbin.mdnsd usr.sbin.nmbd usr.sbin.nscd usr.sbin.ntpd usr.sbin.smbd usr.sbin.smbd-shares usr.sbin.smbldap-useradd  usr.sbin.traceroute \
    usr.sbin.winbindd zgrep
do
    if [ -f "/etc/apparmor.d/local/$oldlocal" ] && [ "$(cat /etc/apparmor.d/local/$oldlocal)" = "# Site-specific additions and overrides for '$oldlocal'" ] ; then
        rm "/etc/apparmor.d/local/$oldlocal" || :
    fi
done

%posttrans profiles
# workaround for bnc#904620#c8 / lp#1392042
rm -f /var/cache/apparmor/* 2>/dev/null
#restart_on_update apparmor - but non-broken (bnc#853019)
systemctl is-active -q apparmor && systemctl reload apparmor ||:

%if %{with tomcat}
%post -n tomcat_apparmor -p /sbin/ldconfig

%postun -n tomcat_apparmor -p /sbin/ldconfig
%endif

%if %{with pam}
%post -n pam_apparmor
if [ $1 -eq 1 ]; then
        pam-config --add --apparmor || :
fi

%postun -n pam_apparmor
if [ $1 -eq 0 ]; then
        pam-config --delete --apparmor || :
fi
%endif

%changelog
