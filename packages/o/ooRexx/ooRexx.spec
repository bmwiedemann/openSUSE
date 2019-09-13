#
# spec file for package ooRexx
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


%if 0%{?_unknownos}
%define _unknownos 0
%endif

# Red Hat
%if 0%{?_redhat}
# Currently RH does not define these like Fedora does, but they might in the future.
# So we define them using the contents of the release file.
%define build_distro rhel
%if %(if grep -q "release 5.5" /etc/redhat-release; then echo 1; else echo 0; fi;)
%define build_version 55
%endif
%if %(if grep -q "release 5.6" /etc/redhat-release; then echo 1; else echo 0; fi;)
%define build_version 56
%endif
%if %(if grep -q "release 6.0" /etc/redhat-release; then echo 1; else echo 0; fi;)
%define build_version 60
%endif
%if %(if grep -q "release 6.1" /etc/redhat-release; then echo 1; else echo 0; fi;)
%define build_version 61
%endif
%if %(if grep -q "release 6.2" /etc/redhat-release; then echo 1; else echo 0; fi;)
%define build_version 62
%endif
%define _osdistname %{build_distro}%{build_version}
%define _unknownos 0
%endif

# SuSE
%if 0%{?suse_version}
%define build_distro %(grep -q "openSUSE" /etc/SuSE-release && echo opensuse || echo sles)
%define build_version %{suse_version}
%define _osdistname %{build_distro}%{build_version}
%define _unknownos 0
%endif

# This is the default
%if 0%{?_unknownos}
%define build_distro unknown
%define build_version 0
%define _osdistname %{build_distro}%{build_version}
%endif

#******************************************************************************
# The base spec tags
#******************************************************************************

Name:           ooRexx
Prefix:         /usr
Version:        4.2.0
Release:        0
Summary:        Open Object Rexx
License:        CPL-1.0
Group:          Development/Languages/Other
Url:            http://www.oorexx.org/
Source:         %{name}-%{version}.tar.bz2
Source1:        %{name}-rpmlintrc
# If we don't include the following option we get bogus dependencies generated
AutoReq:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  coreutils
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  procps
BuildRequires:  subversion
BuildRequires:	psmisc
Requires(post):   /usr/sbin/update-alternatives
Requires(postun): /usr/sbin/update-alternatives

%if 0%{?suse_version} > 1230

# SLE12 does not have xalan-c anymore!
%if %{suse_version} != 1315    
BuildRequires:  xalan-c
%endif
%{?systemd_requires}
%endif

Patch0:         set_default_rexx_path.patch
Patch1:         systemd-fixes.patch
# PATCH-FIX-UPSTREAM marguerite@opensuse.org - cannot convert 'bool' to 'RexxPackageObject' in return
Patch2:         ooRexx-4.2.0-gcc6.patch
# PATCH-FIX-UPSTREAM marguerite@opensuse.org - chdir before chroot and setgroups before setuid
Patch3:         ooRexx-chdir-setgroups.patch

# Specify the libtool library version
# The order of these looks wrong, but that is how it comes out!
%define orx_libversion 4.0.6

%package devel
Summary:        Open Object Rexx development files
Group:          Development/Languages/Other
Requires:       %{name}, glibc-devel 

#******************************************************************************
%description
#******************************************************************************
Open Object Rexx is an object-oriented scripting language. The language
is designed for both beginners and experienced Rexx programmers. It is
easy to learn and use, and provides an excellent vehicle to enter the
world of object-oriented programming without much effort.

It extends the procedural way of Rexx programming with object-oriented
features that allow you to gradually change your programming style as
you learn more about objects.

For more information on ooRexx, visit http://www.oorexx.org/
For more information on Rexx, visit http://www.rexxla.org/

#******************************************************************************
%description devel
This package contains headers and files needed for developing extensions for
Open Object Rexx.

#******************************************************************************
%prep
#******************************************************************************
%setup -q

%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1

#******************************************************************************
%build
#******************************************************************************

autoreconf -vfi

%if 0%{?suse_version}
echo "SUSE_VERSION=%{suse_version}"
%endif
# to avoid segmentation fault
export CFLAGS="$CFLAGS -fpermissive `echo $RPM_OPT_FLAGS | sed 's/O2/O0/'`"
export SUSE_ASNEEDED=0

./configure --disable-static --prefix=%{_prefix}
make %{?_smp_mflags} libdir=%{_libdir} pkgdatadir=%{_datadir}/ooRexx

cat > rpmmacros.rexx << EOF
%_ooRexx        $(echo %{version} | cut -d. -f1)
%_rexxclassdir  %{_datadir}/ooRexx
%_rexxlibdir    %{_libdir}
EOF

cat > %{name}.pc << EOF
prefix=%{_prefix}
exec_prefix=%{_prefix}
libdir=%{_libdir}
includedir=%{_includedir}

%{name}_binary_version=%{version}
%{name}_major=$(echo %{version} | cut -d. -f1)
%{name}_minor=$(echo %{version} | cut -d. -f2)

Name: %{name}
Description: Open Object Rexx
Version: %{version}
Libs: -L\${libdir}/ooRexx -lrexx -lrexxapi
Cflags: -I\${includedir}
EOF

#******************************************************************************
%install
#******************************************************************************
make DESTDIR=${RPM_BUILD_ROOT} libdir=%{_libdir} mandir=%{_datadir}/ooRexx pkgdatadir=%{_datadir}/ooRexx install

# REXX system-wide RPM macros
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/rpm
install -m 644 rpmmacros.rexx $RPM_BUILD_ROOT/%{_sysconfdir}/rpm/macros.rexx

# PKGconfig file
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
install -m 644 %{name}.pc $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/%{name}.pc

# Add links for some ooRexx scripts
cd $RPM_BUILD_ROOT/%{_bindir}
ln -sf %{_datadir}/ooRexx/rexxtry.rex .

# Sort out systemd vs init depending on system version
mkdir $RPM_BUILD_ROOT/sbin
%if 0%{?suse_version} > 1230
mkdir -p %{buildroot}%{_unitdir}
install -D -m 444 %{buildroot}%{_datadir}/ooRexx/rxapid.service %{buildroot}%{_unitdir}/%{name}.service
rm -f %{buildroot}%{_datadir}/ooRexx/rxapid.service
ln -s /sbin/service $RPM_BUILD_ROOT/sbin/rc%{name}
%else
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/init.d
ln -s %{_bindir}/rxapid $RPM_BUILD_ROOT/%{_sysconfdir}/init.d/rxapid
ln -s /%{_sysconfdir}/init.d/rxapid $RPM_BUILD_ROOT/sbin/rcrxapid
rm -f %{buildroot}%{_datadir}/ooRexx/rxapid.service
%endif

# fix wrong permissions from the original package
chmod 644 %{buildroot}%{_datadir}/ooRexx/readme
chmod 644 %{buildroot}%{_datadir}/ooRexx/*cls

# adding update-alternatives support (boo#1083875)
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
BINARIES="rexx rexxc rxqueue"
for f in ${BINARIES}; do
		mv %{buildroot}/%{_bindir}/$f %{buildroot}/%{_bindir}/$f.oorexx
done

# strangely, SLE11 requires a dummy file for the ghost-marked files(?)
%if 0%{?suse_version} < 1230
touch %{buildroot}%{_sysconfdir}/alternatives/{rexx,rexxc,rxqueue,rexx.1,rexxc.1,rxqueue.1,rxsubcom.1,oorexx-config.1}
%endif

#******************************************************************************
%clean
#******************************************************************************
# kill leftover "rexximage" process left by the compilation process
killall rexximage && /bin/true
rm -rf $RPM_BUILD_ROOT

#******************************************************************************
%files
#******************************************************************************
%defattr(-,root,root,-)
%doc
%dir %{_datadir}/ooRexx
%config %{_sysconfdir}/rpm/macros.rexx
%{_bindir}/rexx.oorexx
%{_bindir}/rexxc.oorexx
%{_bindir}/rxqueue.oorexx
%{_bindir}/rxapi
%{_bindir}/rxapid
%{_bindir}/rxsubcom
%{_bindir}/rexximage
%{_bindir}/rexx.img
%{_bindir}/rexx.cat
%{_bindir}/rexxtry.rex
%{_datadir}/ooRexx/rxregexp.cls
%{_datadir}/ooRexx/rxftp.cls
%{_datadir}/ooRexx/csvStream.cls
%{_datadir}/ooRexx/socket.cls
%{_datadir}/ooRexx/streamsocket.cls
%{_datadir}/ooRexx/mime.cls
%{_datadir}/ooRexx/smtp.cls

%ghost %{_sysconfdir}/alternatives/rexx
%ghost %{_sysconfdir}/alternatives/rexxc
%ghost %{_sysconfdir}/alternatives/rxqueue
%ghost %{_sysconfdir}/alternatives/rexx.1
%ghost %{_sysconfdir}/alternatives/rexxc.1
%ghost %{_sysconfdir}/alternatives/rxqueue.1
%ghost %{_sysconfdir}/alternatives/rxsubcom.1

%{_libdir}/librexx.so
%{_libdir}/librexx.so.4
%{_libdir}/librexx.so.%{orx_libversion}
%{_libdir}/librexxapi.so
%{_libdir}/librexxapi.so.4
%{_libdir}/librexxapi.so.%{orx_libversion}
%{_libdir}/librxsock.so
%{_libdir}/librxsock.so.4
%{_libdir}/librxsock.so.%{orx_libversion}
%{_libdir}/librxmath.so
%{_libdir}/librxmath.so.4
%{_libdir}/librxmath.so.%{orx_libversion}
%{_libdir}/librxregexp.so
%{_libdir}/librxregexp.so.4
%{_libdir}/librxregexp.so.%{orx_libversion}
%{_libdir}/librexxutil.so
%{_libdir}/librexxutil.so.4
%{_libdir}/librexxutil.so.%{orx_libversion}
%{_libdir}/libhostemu.so
%{_libdir}/libhostemu.so.4
%{_libdir}/libhostemu.so.%{orx_libversion}
%{_libdir}/librxunixsys.so
%{_libdir}/librxunixsys.so.4
%{_libdir}/librxunixsys.so.%{orx_libversion}

%dir %{_datadir}/ooRexx/man1
%{_datadir}/ooRexx/man1/rexx.1
%{_datadir}/ooRexx/man1/rexxc.1
%{_datadir}/ooRexx/man1/rxsubcom.1
%{_datadir}/ooRexx/man1/rxqueue.1
%{_datadir}/ooRexx/rexx.sh
%{_datadir}/ooRexx/rexx.csh
%{_datadir}/ooRexx/*.rex
%{_datadir}/ooRexx/readme

%if 0%{?suse_version} > 1230
%{_unitdir}/%{name}.service
/sbin/rcooRexx
%else
%{_sysconfdir}/init.d/rxapid
/sbin/rcrxapid
%endif

#******************************************************************************

%files devel
%defattr(-,root,root,-)
%{_bindir}/oorexx-config
%{_datadir}/ooRexx/man1/oorexx-config.1
%ghost %{_sysconfdir}/alternatives/oorexx-config.1
%{_includedir}/rexx.h
%{_includedir}/rexxapidefs.h
%{_includedir}/rexxapitypes.h
%{_includedir}/rexxplatformapis.h
%{_includedir}/rexxplatformdefs.h
%{_includedir}/oorexxapi.h
%{_includedir}/oorexxerrors.h
%{_libdir}/librexx.la
%{_libdir}/librexxapi.la
%{_libdir}/librxsock.la
%{_libdir}/librxmath.la
%{_libdir}/librxregexp.la
%{_libdir}/librexxutil.la
%{_libdir}/libhostemu.la
%{_libdir}/librxunixsys.la
%{_libdir}/pkgconfig/%{name}.pc

%pre
%if 0%{?suse_version} > 1230
%service_add_pre ooRexx.service
%endif

%post
# Add the rxapi service
%if 0%{?suse_version} > 1230
%service_add_post ooRexx.service
echo "Please enable the ooRexx rxapid service manually."
echo "To do this, run:"
echo "systemctl enable ooRexx.service"
echo "systemctl start ooRexx.service"
%else
%fillup_and_insserv rxapid
%endif

/sbin/ldconfig
BINARIES="rexx rexxc rxqueue"
for f in ${BINARIES}; do
	update-alternatives --install \
   		%{_bindir}/$f $f %{_bindir}/$f.oorexx 10
done

for f in $(find %{_datadir}/ooRexx/man1 -type f); do
		NAME=$(basename $f)
   		update-alternatives --install \
        %{_mandir}/man1/${NAME} ${NAME} %{_datadir}/ooRexx/man1/${NAME} 10
done   

%post devel
update-alternatives --install \
        %{_mandir}/man1/oorexx-config.1 oorexx-config.1 %{_datadir}/ooRexx/man1/oorexx-config.1 10

#******************************************************************************
%preun
%if 0%{?suse_version} > 1230
%service_del_preun ooRexx.service
%endif
BINARIES="rexx rexxc rxqueue"
for f in ${BINARIES}; do
	if [ ! -f %{_bindir}/$f ] ; then
   		update-alternatives --remove $f %{_bindir}/$f
	fi
done

for f in $(find %{_datadir}/ooRexx/man1 -type f); do
		NAME=$(basename $f)
   		update-alternatives --remove ${NAME} %{_mandir}/man1/${NAME}
done

#******************************************************************************
%postun
#******************************************************************************
%if 0%{?suse_version} > 1230
%service_del_postun ooRexx.service
%else
%restart_on_update rxapid
%insserv_cleanup
%endif

/sbin/ldconfig

%preun devel
update-alternatives --remove oorexx-config.1 %{_mandir}/man1/oorexx-config.1

#******************************************************************************

%changelog
