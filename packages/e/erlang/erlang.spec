#
# spec file for package erlang
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

%if 0%{?rhel} >= 7
%undefine _missing_build_ids_terminate_build
%endif

%{!?make_build:%{expand: %%global make_build %%{__make} %%{?_smp_mflags}}}

Name:           erlang
Version:        22.1
Release:        0
# not set up to be built with position independend executable support
#!BuildIgnore:	gcc-PIE
Summary:        General-purpose programming language and runtime environment
License:        Apache-2.0
Group:          Development/Languages/Other
Url:            http://www.erlang.org
Source0:        https://github.com/erlang/otp/archive/OTP-%{version}.tar.gz
Source3:        %{name}-rpmlintrc
Source4:        epmd.init
Source5:        erlang.sysconfig
Source6:        macros.erlang
Source7:        epmd.service
Source8:        epmd.socket
Source9:        README.SUSE
# PATCH-MISSING-TAG -- See http://en.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         otp-R16B-rpath.patch
# PATCH-FIX-OPENSUSE erlang-not-install-misc.patch - matwey.kornilov@gmail.com -- patch from Fedora, this removes unneeded magic
Patch4:         erlang-not-install-misc.patch
BuildRequires:  autoconf
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRequires:  openssh
BuildRequires:  openssl-devel
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRequires:  unixODBC-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %fillup_prereq
BuildRequires:  %insserv_prereq
BuildRequires:  Mesa-devel
BuildRequires:  fdupes
BuildRequires:  fop
BuildRequires:  dejavu-fonts
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  krb5-devel
BuildRequires:  update-alternatives
%if 0%{?suse_version} >= 1220
BuildRequires:  xsltproc
%else
BuildRequires:  libxslt
%endif
Requires:       erlang-epmd

%if 0%{?suse_version} >= 1320
BuildRequires:  wxWidgets-devel >= 3
%else
%if 0%{?suse_version} >= 1315
BuildRequires:  wxWidgets-devel >= 2.8
%define wx_requires_generator 1
%else
BuildRequires:  wxWidgets >= 2.8
BuildRequires:  wxWidgets-wxcontainer-devel >= 2.8
%define wx_requires_generator 1
%endif
%endif

%if 0%{?wx_requires_generator}
%define _use_internal_dependency_generator 0
%define __find_requires %wx_requires
%endif

%if 0%{?suse_version} >=1230
BuildRequires:  systemd-devel
BuildRequires:  pkgconfig(systemd)
%define have_systemd 1
%endif

%define epmd_home %{_var}/lib/epmd

%description
Erlang is a general-purpose programming language and runtime
environment. Erlang has built-in support for concurrency, distribution
and fault tolerance. Erlang is used in several large telecommunication
systems from Ericsson.

%package debugger
Summary:        A debugger for debugging and testing of Erlang programs
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-wx = %{version}

%description debugger
A debugger for debugging and testing of Erlang programs.

%package dialyzer
Summary:        A DIscrepany AnaLYZer for ERlang programs
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-wx = %{version}
Requires:       graphviz

%description dialyzer
A DIscrepany AnaLYZer for ERlang programs.

%package diameter
Summary:        Main API of the Diameter application
Group:          Development/Languages/Other
Requires:       %{name} = %{version}

%description diameter
This module provides the interface with which a user can implement a Diameter
node that sends and receives messages using the Diameter protocol as defined in
RFC 6733.

%package doc
Summary:        Erlang documentation
Group:          Development/Languages/Other
%if 0%{?suse_version}
Recommends:     %{name} = %{version}
%endif

%description doc
Documentation for Erlang.

%package epmd
Summary:        Erlang Port Mapper daemon
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires(postun): %insserv_prereq
Requires(post): %fillup_prereq
%if 0%{?have_systemd}
%{?systemd_requires}
%endif

%description epmd
The Erlang Port Mapper daemon acts as a name server on all hosts involved in distributed Erlang computations.

%package et
Summary:        An event tracer for Erlang programs
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-wx = %{version}

%description et
An event tracer for Erlang programs.

%package jinterface
Summary:        Erlang Java Interface
Group:          Development/Libraries/Java
Requires:       %{name} = %{version}
Requires:       java >= 1.6.0

%description jinterface
JInterface module for accessing erlang from Java

%package reltool
Summary:        A release management tool
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-wx = %{version}

%description reltool
Reltool is a release management tool. It analyses a given
Erlang/OTP installation and determines various dependencies
between applications. The graphical frontend depicts the
dependencies and enables interactive customization of a
target system. The backend provides a batch interface
for generation of customized target systems.

%package observer
Summary:        A GUI tool for observing an erlang system
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       %{name}-wx = %{version}

%description observer
The observer is gui frontend containing various tools to inspect a system.
It displays system information, application structures, process information,
ets or mnesia tables and a frontend for tracing with ttb.

%package src
Summary:        Erlang/OTP applications sources
Group:          Development/Languages/Other
Requires:       %{name} = %{version}

%description src
Erlang sources for all the applications in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package debugger-src
Summary:        Erlang/OTP debugger application sources
Group:          Development/Languages/Other
Requires:       %{name}-debugger = %{version}

%description debugger-src
Erlang sources for the debugger application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package dialyzer-src
Summary:        Erlang/OTP dialyzer application sources
Group:          Development/Languages/Other
Requires:       %{name}-dialyzer = %{version}

%description dialyzer-src
Erlang sources for the dialyzer application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package diameter-src
Summary:        Erlang/OTP Diameter application sources
Group:          Development/Languages/Other
Requires:       %{name}-diameter = %{version}

%description diameter-src
Erlang sources for the Diameter application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package et-src
Summary:        Erlang/OTP et application sources
Group:          Development/Languages/Other
Requires:       %{name}-et = %{version}

%description et-src
Erlang sources for the et application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package jinterface-src
Summary:        Erlang/OTP jinterface application sources
Group:          Development/Languages/Other
Requires:       %{name}-jinterface = %{version}

%description jinterface-src
Erlang sources for the jinterface application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package reltool-src
Summary:        Erlang/OTP reltool application sources
Group:          Development/Languages/Other
Requires:       %{name}-reltool = %{version}

%description reltool-src
Erlang sources for the reltool application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package observer-src
Summary:        Erlang/OTP observer application sources
Group:          Development/Languages/Other
Requires:       %{name}-observer = %{version}

%description observer-src
Erlang sources for the observer application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating embedded systems.

%package wx-src
Summary:        Erlang/OTP wx application sources
Group:          Development/Languages/Other
Requires:       %{name}-wx = %{version}

%description wx-src
Erlang sources for the wx application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package wx
Summary:        A library for wxWidgets support in Erlang
Group:          Development/Languages/Other
Requires:       %{name} = %{version}
Requires:       wxWidgets >= 2.8

%description wx
A Graphics System used to write platform independent user interfaces.

%prep
%setup -q -n otp-OTP-%{version}
%patch0 -p1 -b .rpath
%patch4 -p1
cp %{S:9} .

./otp_build autoconf
# enable dynamic linking for ssl
sed -i 's|SSL_DYNAMIC_ONLY=no|SSL_DYNAMIC_ONLY=yes|' erts/configure
# Remove shipped zlib sources
#rm -f erts/emulator/zlib/*.[ch]

# fix for arch linux bug #17001 (wx not working)
sed -i 's|WX_LIBS=`$WX_CONFIG_WITH_ARGS --libs`|WX_LIBS="`$WX_CONFIG_WITH_ARGS --libs` -lGLU"|' lib/wx/configure || return 1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
# we need build only 1.6 target for java
# for SLE only
%if 0%{?sles_version} >= 10 || 0%{?suse_version} >= 1110
	export JAVAC="javac -source 1.6 -target 1.6"
%endif
%if 0%{?suse_version} == 1100 || 0%{?fedora_version} == 9
export CFLAGS="-fno-strict-aliasing"
%else
export CFLAGS="%{optflags} -fno-strict-aliasing"
%endif
export CXXFLAGS=$CFLAGS

%configure \
%if 0%{?have_systemd}
    --enable-systemd \
%endif
    --with-ssl=%{_prefix} \
    --enable-threads \
    --enable-smp-support \
    --enable-kernel-poll \
%ifnarch s390 s390x
    --enable-hipe \
%endif
    --enable-shared-zlib
# clean stalled files before rebuild them
%make_build clean
%make_build
# to build the docs, just compiled erlang is required
PATH=$PWD/bin:$PATH %make_build docs

%install
%if 0%{?sles_version} >= 10
    make DESTDIR=%{buildroot} install
    make DESTDIR=%{buildroot} install-docs
%else
    %make_install install-docs
%endif

export TOOLS_VERSION=`ls %{buildroot}%{_libdir}/erlang/lib/ |grep ^tools- | sed "s|tools-||"`

# clean up
find %{buildroot}%{_libdir}/erlang -perm 0775 | xargs chmod -v 0755
find %{buildroot}%{_libdir}/erlang -name Makefile | xargs chmod -v 0644
find %{buildroot}%{_libdir}/erlang -name \*.bat | xargs rm -fv
find %{buildroot}%{_libdir}/erlang -name index.txt.old | xargs rm -fv
find %{buildroot}%{_libdir}/erlang -type d -path '*/priv/obj' -print | xargs rm -rfv

# doc
mv README.md README
mkdir -p erlang_doc
find %{buildroot}%{_libdir}/erlang -maxdepth 3 -type d -name doc -or -name info | while read S;do D=`echo $S | sed -e 's|%{buildroot}%{_libdir}/erlang|erlang_doc|'`; B=`dirname $D`; mkdir -p $B; mv $S $D; done
# compress man pages ...
find %{buildroot}%{_libdir}/erlang/man -type f -exec gzip {} +

#make link to OtpErlang-*.jar in %%{_javadir}
mkdir -p %{buildroot}%{_javadir}
cd %{buildroot}%{_javadir}
export JINTERFACE_VERSION=`ls %{buildroot}%{_libdir}/erlang/lib/ |grep ^jinterface- | sed "s|jinterface-||"`
ln -sf ../../%{_lib}/erlang/lib/jinterface-$JINTERFACE_VERSION/priv/OtpErlang.jar OtpErlang-$JINTERFACE_VERSION.jar
cd -

# The man-pages for binaries are safe to move to %{_mandir}, others may conflict with other packages
mkdir -p %{buildroot}%{_mandir}/man1
for link in $(ls %{buildroot}%{_libdir}/erlang/man/man1/); do
    ln -s %{_libdir}/erlang/man/man1/$link %{buildroot}%{_mandir}/man1/$link
done

# emacs: automatically load support for erlang
# http://lists.mandriva.com//bugs/2007-08/msg00930.php
mkdir -p %{buildroot}%{_datadir}/emacs/site-lisp
cat > %{buildroot}%{_datadir}/emacs/site-lisp/erlang.el << EOF
(setq load-path (cons "%{_libdir}/erlang/lib/tools-$TOOLS_VERSION/emacs" load-path))
(add-to-list 'load-path "%{_datadir}/emacs/site-lisp/ess")
(load-library "erlang-start")
EOF

# hardlink duplicates:
find . -name "start_erl*" | xargs chmod 755
%fdupes %{buildroot}/%{_libdir}/erlang
# %%doc macro copies the files to the package doc dir, hardlinks thus don't work
%fdupes -s erlang_doc

install -d -m 0750        %{buildroot}%{epmd_home}
install -d -m 0755        %{buildroot}%{_sbindir}
%if 0%{?have_systemd}
install -D -m 0644 %{S:7} %{buildroot}%{_unitdir}/epmd.service
install -D -m 0644 %{S:8} %{buildroot}%{_unitdir}/epmd.socket
ln -s   /sbin/service     %{buildroot}%{_sbindir}/rcepmd
%else
ln -s   /etc/init.d/epmd  %{buildroot}%{_sbindir}/rcepmd
install -D -m 0755 %{S:4} %{buildroot}/etc/init.d/epmd
install -D -m 0644 %{S:5} %{buildroot}%{_fillupdir}/sysconfig.erlang
%endif
install -D -m 0644 %{S:6} %{buildroot}%{_sysconfdir}/rpm/macros.erlang

%pre epmd
getent group epmd || /usr/sbin/groupadd -r epmd || :
getent passwd epmd || /usr/sbin/useradd -g epmd -s /bin/false -r -c "Erlang Port Mapper Daemon" -d %{epmd_home} epmd || :
%if 0%{?have_systemd}
%service_add_pre epmd.service epmd.socket
%endif

%post epmd
%fillup_only erlang
%if 0%{?have_systemd}
%service_add_post epmd.service epmd.socket
%endif

%preun epmd
%if 0%{?have_systemd}
%service_del_preun epmd.service epmd.socket
%endif
%stop_on_removal epmd

%postun epmd
%if 0%{?have_systemd}
%service_del_postun epmd.service epmd.socket
%endif
%restart_on_update epmd
%{insserv_cleanup}

%files
%license LICENSE.txt
%doc AUTHORS README
%if 0%{?have_systemd}
%doc README.SUSE
%endif
%doc %{_libdir}/erlang/PR.template
%doc %{_libdir}/erlang/README.md
%doc %{_libdir}/erlang/COPYRIGHT
%{_bindir}/*
%exclude %{_bindir}/dialyzer
%exclude %{_bindir}/epmd
%dir %{_libdir}/erlang
%dir %{_libdir}/erlang/lib/
%exclude %{_libdir}/erlang/lib/*/src
%exclude %{_libdir}/erlang/lib/*/c_src
%exclude %{_libdir}/erlang/lib/*/java_src
%{_libdir}/erlang/bin/
%exclude %{_libdir}/erlang/bin/dialyzer
%exclude %{_libdir}/erlang/bin/epmd
%{_libdir}/erlang/erts-*/
%exclude %{_libdir}/erlang/erts-*/bin/dialyzer
%exclude %{_libdir}/erlang/erts-*/bin/epmd
%{_libdir}/erlang/lib/asn1-*/
%{_libdir}/erlang/lib/common_test-*/
%{_libdir}/erlang/lib/compiler-*/
%{_libdir}/erlang/lib/crypto-*/
%{_libdir}/erlang/lib/edoc-*/
%{_libdir}/erlang/lib/eldap-*/
%{_libdir}/erlang/lib/erl_docgen-*/
%{_libdir}/erlang/lib/erl_interface-*/
%{_libdir}/erlang/lib/erts-*/
%{_libdir}/erlang/lib/eunit-*/
%{_libdir}/erlang/lib/hipe-*/
%{_libdir}/erlang/lib/ftp-*/
%{_libdir}/erlang/lib/inets-*/
%{_libdir}/erlang/lib/kernel-*/
%{_libdir}/erlang/lib/megaco-*/
%{_libdir}/erlang/lib/mnesia-*/
%{_libdir}/erlang/lib/odbc-*/
%{_libdir}/erlang/lib/tftp-*/
%{_libdir}/erlang/lib/os_mon-*/
%{_libdir}/erlang/lib/parsetools-*/
%{_libdir}/erlang/lib/public_key-*/
%{_libdir}/erlang/lib/runtime_tools-*/
%{_libdir}/erlang/lib/sasl-*/
%{_libdir}/erlang/lib/snmp-*/
%{_libdir}/erlang/lib/ssh-*/
%{_libdir}/erlang/lib/ssl-*/
%{_libdir}/erlang/lib/stdlib-*/
%{_libdir}/erlang/lib/syntax_tools-*/
%{_libdir}/erlang/lib/tools-*/
%{_libdir}/erlang/lib/xmerl-*/
%{_libdir}/erlang/man/
%{_mandir}/man1/*.1.gz
%{_libdir}/erlang/releases/
%{_libdir}/erlang/usr/
%{_libdir}/erlang/Install
%{_datadir}/emacs/site-lisp/erlang.el
%config %{_sysconfdir}/rpm/macros.erlang

%files debugger
%defattr(-,root,root)
%{_libdir}/erlang/lib/debugger-*/
%exclude %{_libdir}/erlang/lib/debugger-*/src

%files dialyzer
%defattr(-,root,root)
%{_libdir}/erlang/lib/dialyzer-*/
%exclude %{_libdir}/erlang/lib/dialyzer-*/src
%{_bindir}/dialyzer
%{_libdir}/erlang/bin/dialyzer
%{_libdir}/erlang/erts-*/bin/dialyzer

%files diameter
%defattr(-,root,root)
%{_libdir}/erlang/lib/diameter-*/
%exclude %{_libdir}/erlang/lib/diameter-*/src

%files doc
%defattr(0644,root,root,0755)
%doc erlang_doc/*

%files et
%defattr(-,root,root)
%{_libdir}/erlang/lib/et-*/
%exclude %{_libdir}/erlang/lib/et-*/src

%files epmd
%defattr(-,root,root)
%{_bindir}/epmd
%{_libdir}/erlang/bin/epmd
%{_libdir}/erlang/erts-*/bin/epmd
%dir %attr(-,epmd,epmd) %{epmd_home}
%if 0%{?have_systemd}
%{_unitdir}/epmd.service
%{_unitdir}/epmd.socket
%else
/etc/init.d/epmd
%{_fillupdir}/sysconfig.erlang
%endif
%{_sbindir}/rcepmd

%files jinterface
%defattr(-,root,root,-)
%{_libdir}/erlang/lib/jinterface-*/
%exclude %{_libdir}/erlang/lib/jinterface-*/java_src
%{_javadir}/*

%files reltool
%defattr(-,root,root)
%{_libdir}/erlang/lib/reltool-*/
%exclude %{_libdir}/erlang/lib/reltool-*/src

%files observer
%defattr(-,root,root)
%{_libdir}/erlang/lib/observer-*/
%exclude %{_libdir}/erlang/lib/observer-*/src

%files wx
%defattr(-,root,root)
%{_libdir}/erlang/lib/wx-*/
%exclude %{_libdir}/erlang/lib/wx-*/src

%files src
%defattr(-,root,root)
%exclude %{_libdir}/erlang/lib/erl_interface-*/src/INSTALL
%{_libdir}/erlang/lib/*/src
%{_libdir}/erlang/lib/*/c_src
%{_libdir}/erlang/lib/*/java_src
%exclude %{_libdir}/erlang/lib/debugger-*/src
%exclude %{_libdir}/erlang/lib/dialyzer-*/src
%exclude %{_libdir}/erlang/lib/diameter-*/src
%exclude %{_libdir}/erlang/lib/et-*/src
%exclude %{_libdir}/erlang/lib/jinterface-*/java_src
%exclude %{_libdir}/erlang/lib/reltool-*/src
%exclude %{_libdir}/erlang/lib/observer-*/src
%exclude %{_libdir}/erlang/lib/wx-*/src

%files debugger-src
%defattr(-,root,root)
%{_libdir}/erlang/lib/debugger-*/src

%files dialyzer-src
%defattr(-,root,root)
%{_libdir}/erlang/lib/dialyzer-*/src

%files diameter-src
%defattr(-,root,root)
%{_libdir}/erlang/lib/diameter-*/src

%files et-src
%defattr(-,root,root)
%{_libdir}/erlang/lib/et-*/src

%files jinterface-src
%defattr(-,root,root)
%{_libdir}/erlang/lib/jinterface-*/java_src

%files reltool-src
%defattr(-,root,root)
%{_libdir}/erlang/lib/reltool-*/src

%files observer-src
%defattr(-,root,root)
%{_libdir}/erlang/lib/observer-*/src

%files wx-src
%defattr(-,root,root)
%{_libdir}/erlang/lib/wx-*/src

%changelog
