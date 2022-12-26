#
# spec file for package erlang
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


%{!?make_build:%{expand: %%global make_build %{make} %%{?_smp_mflags}}}
%define epmd_home %{_var}/lib/epmd
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           erlang
Version:        25.2
Release:        0
Summary:        General-purpose programming language and runtime environment
License:        Apache-2.0
URL:            https://www.erlang.org
Source0:        https://github.com/erlang/otp/archive/OTP-%{version}.tar.gz
Source3:        %{name}-rpmlintrc
Source5:        erlang.sysconfig
Source6:        macros.erlang
Source7:        epmd.service
Source8:        epmd.socket
Source9:        README.SUSE
Source10:       epmd-user.conf
# PATCH-MISSING-TAG -- See http://en.opensuse.org/openSUSE:Packaging_Patches_guidelines
Patch0:         otp-R16B-rpath.patch
# PATCH-FIX-OPENSUSE erlang-not-install-misc.patch - matwey.kornilov@gmail.com -- patch from Fedora, this removes unneeded magic
Patch4:         erlang-not-install-misc.patch
BuildRequires:  Mesa-devel
BuildRequires:  autoconf
BuildRequires:  dejavu-fonts
BuildRequires:  fdupes
BuildRequires:  fop
BuildRequires:  gcc-c++
BuildRequires:  java-devel
BuildRequires:  openssh
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  sysuser-tools
BuildRequires:  update-alternatives
BuildRequires:  wxWidgets-devel >= 3.1
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(odbc)
BuildRequires:  pkgconfig(tcl)
BuildRequires:  pkgconfig(tk)
# not set up to be built with position independend executable support
#!BuildIgnore:  gcc-PIE
Requires:       erlang-epmd
%if 0%{?rhel} >= 7
%undefine _missing_build_ids_terminate_build
%endif

%description
Erlang is a general-purpose programming language and runtime
environment. Erlang has built-in support for concurrency, distribution
and fault tolerance. Erlang is used in several large telecommunication
systems from Ericsson.

%package debugger
Summary:        A debugger for debugging and testing of Erlang programs
Requires:       %{name} = %{version}
Requires:       %{name}-wx = %{version}

%description debugger
A debugger for debugging and testing of Erlang programs.

%package dialyzer
Summary:        A DIscrepany AnaLYZer for ERlang programs
Requires:       %{name} = %{version}
Requires:       %{name}-wx = %{version}
Requires:       graphviz

%description dialyzer
A DIscrepany AnaLYZer for ERlang programs.

%package diameter
Summary:        Main API of the Diameter application
Requires:       %{name} = %{version}

%description diameter
This module provides the interface with which a user can implement a Diameter
node that sends and receives messages using the Diameter protocol as defined in
RFC 6733.

%package doc
Summary:        Erlang documentation
Requires:       %{name} = %{version}

%description doc
Documentation for Erlang.

%package epmd
Summary:        Erlang Port Mapper daemon
Requires:       %{name} = %{version}
Requires(post): %fillup_prereq
%{sysusers_requires}
%{?systemd_requires}

%description epmd
The Erlang Port Mapper daemon acts as a name server on all hosts involved in distributed Erlang computations.

%package et
Summary:        An event tracer for Erlang programs
Requires:       %{name} = %{version}
Requires:       %{name}-wx = %{version}

%description et
An event tracer for Erlang programs.

%package jinterface
Summary:        Erlang Java Interface
Requires:       %{name} = %{version}
Requires:       java >= 1.6.0

%description jinterface
JInterface module for accessing erlang from Java

%package reltool
Summary:        A release management tool
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
Requires:       %{name} = %{version}
Requires:       %{name}-wx = %{version}

%description observer
The observer is gui frontend containing various tools to inspect a system.
It displays system information, application structures, process information,
ets or mnesia tables and a frontend for tracing with ttb.

%package src
Summary:        Erlang/OTP applications sources
Requires:       %{name} = %{version}

%description src
Erlang sources for all the applications in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package debugger-src
Summary:        Erlang/OTP debugger application sources
Requires:       %{name}-debugger = %{version}

%description debugger-src
Erlang sources for the debugger application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package dialyzer-src
Summary:        Erlang/OTP dialyzer application sources
Requires:       %{name}-dialyzer = %{version}

%description dialyzer-src
Erlang sources for the dialyzer application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package diameter-src
Summary:        Erlang/OTP Diameter application sources
Requires:       %{name}-diameter = %{version}

%description diameter-src
Erlang sources for the Diameter application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package et-src
Summary:        Erlang/OTP et application sources
Requires:       %{name}-et = %{version}

%description et-src
Erlang sources for the et application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package jinterface-src
Summary:        Erlang/OTP jinterface application sources
Requires:       %{name}-jinterface = %{version}

%description jinterface-src
Erlang sources for the jinterface application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package reltool-src
Summary:        Erlang/OTP reltool application sources
Requires:       %{name}-reltool = %{version}

%description reltool-src
Erlang sources for the reltool application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package observer-src
Summary:        Erlang/OTP observer application sources
Requires:       %{name}-observer = %{version}

%description observer-src
Erlang sources for the observer application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating embedded systems.

%package wx-src
Summary:        Erlang/OTP wx application sources
Requires:       %{name}-wx = %{version}

%description wx-src
Erlang sources for the wx application in the Erlang/OTP system.
They are useful for educational purpose and as a base for creating
embedded systems.

%package wx
Summary:        A library for wxWidgets support in Erlang
Requires:       %{name} = %{version}
Requires:       wxWidgets >= 2.8

%description wx
A Graphics System used to write platform independent user interfaces.

%prep
%setup -q -n otp-OTP-%{version}
%patch0 -p1 -b .rpath
%patch4 -p1
cp %{SOURCE9} .

./otp_build autoconf
# enable dynamic linking for ssl
sed -i 's|SSL_DYNAMIC_ONLY=no|SSL_DYNAMIC_ONLY=yes|' erts/configure
# Remove shipped zlib sources
#rm -f erts/emulator/zlib/*.[ch]

# fix for arch linux bug #17001 (wx not working)
sed -i 's|WX_LIBS=`$WX_CONFIG_WITH_ARGS --libs`|WX_LIBS="`$WX_CONFIG_WITH_ARGS --libs` -lGLU"|' lib/wx/configure || return 1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CFLAGS="%{optflags} -fno-strict-aliasing"
export CXXFLAGS=$CFLAGS
export LANG="en_US.UTF-8"

%configure \
    --enable-systemd \
    --with-ssl=%{_prefix} \
    --enable-threads \
    --enable-smp-support \
    --enable-kernel-poll \
    --enable-shared-zlib
# clean stalled files before rebuild them
%make_build clean
%make_build
# to build the docs, just compiled erlang is required
PATH=$PWD/bin:$PATH %make_build docs

%sysusers_generate_pre %{SOURCE10} epmd epmd-user.conf

%install
%make_install install-docs

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
mv %{buildroot}%{_libdir}/erlang/doc ./erlang_doc
find %{buildroot}%{_libdir}/erlang -maxdepth 4 -name info -or -type d -and -path '%{buildroot}%{_libdir}/**/doc/*' -and -not -name chunks -prune | while read S;do D=`echo $S | sed -e 's|%{buildroot}%{_libdir}/erlang|erlang_doc|'`; B=`dirname $D`; mkdir -p $B; mv $S $D; done
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

install -d -m 0750 %{buildroot}%{epmd_home}
install -d -m 0755 %{buildroot}%{_sbindir}
install -D -m 0644 %{SOURCE7} %{buildroot}%{_unitdir}/epmd.service
install -D -m 0644 %{SOURCE8} %{buildroot}%{_unitdir}/epmd.socket
ln -s service %{buildroot}%{_sbindir}/rcepmd
install -D -m 0644 %{SOURCE6} %{buildroot}%{_rpmmacrodir}/macros.erlang
mkdir -p %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE10} %{buildroot}%{_sysusersdir}

%pre epmd -f epmd.pre
%service_add_pre epmd.service epmd.socket

%post epmd
%fillup_only erlang
%service_add_post epmd.service epmd.socket

%preun epmd
%service_del_preun epmd.service epmd.socket

%postun epmd
%service_del_postun epmd.service epmd.socket

%files
%license LICENSE.txt
%doc AUTHORS README
%doc README.SUSE
%doc %{_libdir}/erlang/PR.template
%doc %{_libdir}/erlang/README.md
%doc %{_libdir}/erlang/COPYRIGHT
%{_bindir}/*
%exclude %{_bindir}/dialyzer
%exclude %{_bindir}/epmd
%dir %{_libdir}/erlang
%dir %{_libdir}/erlang/lib/
%exclude %{_libdir}/erlang/lib/*/doc/chunks
%exclude %{_libdir}/erlang/lib/*/src
%exclude %{_libdir}/erlang/lib/*/c_src
%exclude %{_libdir}/erlang/lib/*/java_src
%dir %{_libdir}/erlang/bin/
%{_libdir}/erlang/bin/*
%exclude %{_libdir}/erlang/bin/dialyzer
%exclude %{_libdir}/erlang/bin/epmd
%dir %{_libdir}/erlang/erts-*/
%dir %{_libdir}/erlang/erts-*/bin/
%{_libdir}/erlang/erts-*/*
%exclude %{_libdir}/erlang/erts-*/bin/dialyzer
%exclude %{_libdir}/erlang/erts-*/bin/epmd
%dir %{_libdir}/erlang/lib/asn1-*/
%{_libdir}/erlang/lib/asn1-*/*
%dir %{_libdir}/erlang/lib/common_test-*/
%{_libdir}/erlang/lib/common_test-*/*
%dir %{_libdir}/erlang/lib/compiler-*/
%{_libdir}/erlang/lib/compiler-*/*
%dir %{_libdir}/erlang/lib/crypto-*/
%{_libdir}/erlang/lib/crypto-*/*
%dir %{_libdir}/erlang/lib/edoc-*/
%{_libdir}/erlang/lib/edoc-*/*
%dir %{_libdir}/erlang/lib/eldap-*/
%{_libdir}/erlang/lib/eldap-*/*
%dir %{_libdir}/erlang/lib/erl_docgen-*/
%{_libdir}/erlang/lib/erl_docgen-*/*
%dir %{_libdir}/erlang/lib/erl_interface-*/
%{_libdir}/erlang/lib/erl_interface-*/*
%dir %{_libdir}/erlang/lib/erts-*/
%{_libdir}/erlang/lib/erts-*/*
%dir %{_libdir}/erlang/lib/eunit-*/
%{_libdir}/erlang/lib/eunit-*/*
%dir %{_libdir}/erlang/lib/ftp-*/
%{_libdir}/erlang/lib/ftp-*/*
%dir %{_libdir}/erlang/lib/inets-*/
%{_libdir}/erlang/lib/inets-*/*
%dir %{_libdir}/erlang/lib/kernel-*/
%{_libdir}/erlang/lib/kernel-*/*
%dir %{_libdir}/erlang/lib/megaco-*/
%{_libdir}/erlang/lib/megaco-*/*
%dir %{_libdir}/erlang/lib/mnesia-*/
%{_libdir}/erlang/lib/mnesia-*/*
%dir %{_libdir}/erlang/lib/odbc-*/
%{_libdir}/erlang/lib/odbc-*/*
%dir %{_libdir}/erlang/lib/tftp-*/
%{_libdir}/erlang/lib/tftp-*/*
%dir %{_libdir}/erlang/lib/os_mon-*/
%{_libdir}/erlang/lib/os_mon-*/*
%dir %{_libdir}/erlang/lib/parsetools-*/
%{_libdir}/erlang/lib/parsetools-*/*
%dir %{_libdir}/erlang/lib/public_key-*/
%{_libdir}/erlang/lib/public_key-*/*
%dir %{_libdir}/erlang/lib/runtime_tools-*/
%{_libdir}/erlang/lib/runtime_tools-*/*
%dir %{_libdir}/erlang/lib/sasl-*/
%{_libdir}/erlang/lib/sasl-*/*
%dir %{_libdir}/erlang/lib/snmp-*/
%{_libdir}/erlang/lib/snmp-*/*
%dir %{_libdir}/erlang/lib/ssh-*/
%{_libdir}/erlang/lib/ssh-*/*
%dir %{_libdir}/erlang/lib/ssl-*/
%{_libdir}/erlang/lib/ssl-*/*
%dir %{_libdir}/erlang/lib/stdlib-*/
%{_libdir}/erlang/lib/stdlib-*/*
%dir %{_libdir}/erlang/lib/syntax_tools-*/
%{_libdir}/erlang/lib/syntax_tools-*/*
%dir %{_libdir}/erlang/lib/tools-*/
%{_libdir}/erlang/lib/tools-*/*
%dir %{_libdir}/erlang/lib/xmerl-*/
%{_libdir}/erlang/lib/xmerl-*/*
%{_libdir}/erlang/man/
%{_mandir}/man1/*.1%{?ext_man}
%{_libdir}/erlang/releases/
%dir %{_libdir}/erlang/usr/
%dir %{_libdir}/erlang/usr/include
%{_libdir}/erlang/usr/include/*.h
%dir %{_libdir}/erlang/usr/lib
%{_libdir}/erlang/usr/lib/*.a
%{_libdir}/erlang/Install
%{_datadir}/emacs/site-lisp/erlang.el
%{_rpmmacrodir}/macros.erlang

%files debugger
%{_libdir}/erlang/lib/debugger-*/
%exclude %{_libdir}/erlang/lib/debugger-*/src

%files dialyzer
%{_bindir}/dialyzer
%{_libdir}/erlang/bin/dialyzer
%{_libdir}/erlang/erts-*/bin/dialyzer
%dir %{_libdir}/erlang/lib/dialyzer-*/
%{_libdir}/erlang/lib/dialyzer-*/*
%exclude %{_libdir}/erlang/lib/dialyzer-*/src

%files diameter
%dir %{_libdir}/erlang/lib/diameter-*/
%{_libdir}/erlang/lib/diameter-*/*
%exclude %{_libdir}/erlang/lib/diameter-*/src

%files doc
%defattr(0644,root,root,0755)
%doc erlang_doc/*
%{_libdir}/erlang/lib/*/doc/chunks
%exclude %{_libdir}/erlang/lib/debugger-*/doc/chunks
%exclude %{_libdir}/erlang/lib/dialyzer-*/doc/chunks
%exclude %{_libdir}/erlang/lib/diameter-*/doc/chunks
%exclude %{_libdir}/erlang/lib/et-*/doc/chunks
%exclude %{_libdir}/erlang/lib/reltool-*/doc/chunks
%exclude %{_libdir}/erlang/lib/observer-*/doc/chunks
%exclude %{_libdir}/erlang/lib/wx-*/doc/chunks

%files et
%dir %{_libdir}/erlang/lib/et-*/
%{_libdir}/erlang/lib/et-*/*
%exclude %{_libdir}/erlang/lib/et-*/src

%files epmd
%{_bindir}/epmd
%dir %{_libdir}/erlang/
%dir %{_libdir}/erlang/bin/
%{_libdir}/erlang/bin/epmd
%dir %{_libdir}/erlang/erts-*/
%dir %{_libdir}/erlang/erts-*/bin/
%{_libdir}/erlang/erts-*/bin/epmd
%dir %attr(-,epmd,epmd) %{epmd_home}
%{_unitdir}/epmd.service
%{_unitdir}/epmd.socket
%{_sbindir}/rcepmd
%{_sysusersdir}/epmd-user.conf

%files jinterface
%dir %{_libdir}/erlang/lib/jinterface-*/
%{_libdir}/erlang/lib/jinterface-*/*
%exclude %{_libdir}/erlang/lib/jinterface-*/java_src
%{_javadir}/*

%files reltool
%dir %{_libdir}/erlang/lib/reltool-*/
%{_libdir}/erlang/lib/reltool-*/*
%exclude %{_libdir}/erlang/lib/reltool-*/src

%files observer
%dir %{_libdir}/erlang/lib/observer-*/
%{_libdir}/erlang/lib/observer-*/*
%exclude %{_libdir}/erlang/lib/observer-*/src

%files wx
%dir %{_libdir}/erlang/lib/wx-*/
%{_libdir}/erlang/lib/wx-*/*
%exclude %{_libdir}/erlang/lib/wx-*/src

%files src
%exclude %{_libdir}/erlang/lib/erl_interface-*/src/INSTALL
%dir %{_libdir}/erlang/lib/*/src
%{_libdir}/erlang/lib/*/src/*
%dir %{_libdir}/erlang/lib/*/c_src
%{_libdir}/erlang/lib/*/c_src/*
%dir %{_libdir}/erlang/lib/*/java_src
%{_libdir}/erlang/lib/*/java_src/*
%exclude %{_libdir}/erlang/lib/debugger-*/src
%exclude %{_libdir}/erlang/lib/dialyzer-*/src
%exclude %{_libdir}/erlang/lib/diameter-*/src
%exclude %{_libdir}/erlang/lib/et-*/src
%exclude %{_libdir}/erlang/lib/jinterface-*/java_src
%exclude %{_libdir}/erlang/lib/reltool-*/src
%exclude %{_libdir}/erlang/lib/observer-*/src
%exclude %{_libdir}/erlang/lib/wx-*/src

%files debugger-src
%dir %{_libdir}/erlang/lib/debugger-*/src
%{_libdir}/erlang/lib/debugger-*/src/*

%files dialyzer-src
%dir %{_libdir}/erlang/lib/dialyzer-*/src
%{_libdir}/erlang/lib/dialyzer-*/src/*

%files diameter-src
%dir %{_libdir}/erlang/lib/diameter-*/src
%{_libdir}/erlang/lib/diameter-*/src/*

%files et-src
%dir %{_libdir}/erlang/lib/et-*/src
%{_libdir}/erlang/lib/et-*/src/*

%files jinterface-src
%dir %{_libdir}/erlang/lib/jinterface-*/java_src
%{_libdir}/erlang/lib/jinterface-*/java_src/*

%files reltool-src
%dir %{_libdir}/erlang/lib/reltool-*/src
%{_libdir}/erlang/lib/reltool-*/src/*

%files observer-src
%dir %{_libdir}/erlang/lib/observer-*/src
%{_libdir}/erlang/lib/observer-*/src/*

%files wx-src
%dir %{_libdir}/erlang/lib/wx-*/src
%{_libdir}/erlang/lib/wx-*/src/*

%changelog
