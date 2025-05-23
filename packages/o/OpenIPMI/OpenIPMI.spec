#
# spec file for package OpenIPMI
#
# Copyright (c) 2024 SUSE LLC
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


# IPMI.pdf build for devel package
# It is not worth to build, but as I got it running I add it
# how it worked for me in Tumbleweed, Leap 42.2 and 42.3 and SLE 15
# latex packages where not avail for SLE 12 flavors
%define doc_build 0
%if 0%{?suse_version} < 1500
%define doc_build 0
%endif
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           OpenIPMI
Version:        2.0.36.56+git.0a3a991
Release:        0
Summary:        Service processor access via IPMI
License:        LGPL-2.1-or-later
Group:          System/Monitoring
URL:            http://openipmi.sourceforge.net
Source0:        openipmi-%{version}.tar.gz
Source1:        sysconfig.ipmi
Source2:        ipmi.service
Source3:        openipmi-helper
Source4:        bootstrap
Source99:       OpenIPMI-rpmlintrc
Patch1:         OpenIPMI-prefer_perl_vendor.patch
Patch2:         openipmi-tinfo.patch
# link with ncurses
Patch3:         OpenIMPI-add-libncurses.patch
Patch4:         fix_dia_version_detection.patch
Patch5:         use_python3_shebang
BuildRequires:  autoconf-archive
BuildRequires:  gd-devel
BuildRequires:  gdbm-devel
BuildRequires:  glib2-devel
BuildRequires:  libedit-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  net-snmp-devel
BuildRequires:  openssl-devel
BuildRequires:  perl-macros
BuildRequires:  pkgconfig
BuildRequires:  popt-devel
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-tk
BuildRequires:  python3-xml
BuildRequires:  readline-devel
BuildRequires:  swig
BuildRequires:  systemd-rpm-macros
BuildRequires:  tcl-devel
BuildRequires:  tix
Requires(post): %fillup_prereq
Provides:       ipmi_ui
Provides:       ipmicmd
Provides:       ipmilan
%{?systemd_ordering}
%{?perl_requires}
%if 0%{?doc_build}
BuildRequires:  dia
BuildRequires:  ghostscript
BuildRequires:  texlive-acronym
BuildRequires:  texlive-bibtex
BuildRequires:  texlive-dvips-bin
BuildRequires:  texlive-latex
BuildRequires:  texlive-moreverb
%endif

%description
OpenIPMI allows access to IPMI information on a server and to abstract it.

The device driver is included in the Linux kernel, and there is a
user-level library available for it as well. This OpenIPMI package
also includes the ipmicmd program, a program that can inject and
receive messages.

%package -n libOpenIPMI0
Summary:        User-level library for accessing IPMI services
Group:          System/Libraries

%description -n libOpenIPMI0
The user-level library that provides a higher-level abstraction of
IPMI and generic services.

%package -n libOpenIPMIui1
Summary:        User-level library for accessing IPMI services
Group:          System/Libraries

%description -n libOpenIPMIui1
The user-level library that provides a higher-level abstraction of
IPMI and generic services.

%package devel
Summary:        Development files for OpenIPMI
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libOpenIPMI0 = %{version}-%{release}
Requires:       libOpenIPMIui1 = %{version}-%{release}

%description devel
These libraries are needed to get full access to the OpenIPMI
functions.

%package python3
Summary:        Python module and GUI for OpenIPMI
Group:          System/Monitoring
Requires:       OpenIPMI
Requires:       python3-tk
Requires:       tix
Conflicts:      OpenIPMI-python
Provides:       openipmigui

%description python3
The Python parts provide an OpenIPMI Python library and a GUI, openipmigui,
that makes use of it.

%prep
%autosetup -n openipmi-%{version} -p1

rm -rf ./libedit

%build
export EDIT_CFLAGS=`pkg-config --cflags libedit`
export EDIT_LIBS=`pkg-config --libs libedit`
export CFLAGS="%{optflags} -fno-strict-aliasing"
export PYTHON_VERSION=%{python3_version}
chmod 755 %{SOURCE4}
%{SOURCE4}
%configure --disable-static \
           --with-openssl=yes \
           --with-pythoninstall=%{python3_sitearch} \
           --with-tcl=yes \
           --with-tcllibs=-ltcl%{tcl_version} \
           --with-tkinter=yes
%make_build
%if 0%{?doc_build}
cd doc
make IPMI.pdf
%endif

%install
%make_install
install -d %{buildroot}%{_fillupdir}
install -d %{buildroot}%{_unitdir}
install -d %{buildroot}%{_sbindir}

case "%{_arch}" in
ppc64*) IPMI_SI_MODULE_NAME=ipmi_powernv;;
aarch64|arm*) IPMI_SI_MODULE_NAME=ipmi_ssif;;
*) IPMI_SI_MODULE_NAME=ipmi_si;;
esac
sed -i "s/^IPMI_SI_MODULE_NAME=.*/IPMI_SI_MODULE_NAME=\"$IPMI_SI_MODULE_NAME\"/" %{SOURCE1}
install -m 644 %{SOURCE1} %{buildroot}%{_fillupdir}

install -m 644 %{SOURCE2} %{buildroot}%{_unitdir}
ln -sv service %{buildroot}%{_sbindir}/rcipmi
install -d %{buildroot}%{_libexecdir}
install -m 755 %{SOURCE3} %{buildroot}%{_libexecdir}/openipmi-helper
find %{buildroot} -type f -name "*.la" -delete -print

# rebuild python3 files to fix timestamps:
for d in "%{python3_sitelib}" "%{python3_sitearch}"; do
    [ -d "%{buildroot}$d" ] || continue
    find "%{buildroot}$d/" -type f \( -name '*.pyc' -o -name '*.pyo' \) -delete
    python3 -c 'import compileall; compileall.compile_dir("%{buildroot}'"$d"'",ddir="'"$d"'",force=1)'
done

%pre
%service_add_pre ipmi.service

%preun
%service_del_preun ipmi.service

%post
%fillup_only -n ipmi
%service_add_post ipmi.service

%postun
%service_del_postun ipmi.service

%post   -n libOpenIPMI0 -p /sbin/ldconfig
%postun -n libOpenIPMI0 -p /sbin/ldconfig
%post   -n libOpenIPMIui1 -p /sbin/ldconfig
%postun -n libOpenIPMIui1 -p /sbin/ldconfig

%files
%license COPYING COPYING.BSD COPYING.LIB
%doc CONFIGURING_FOR_LAN FAQ
%doc README README.Force README.MotorolaMXP
%{_fillupdir}/sysconfig.ipmi
%{_unitdir}/ipmi.service
%{_sbindir}/rcipmi
%{_libexecdir}/openipmi-helper
%dir %{_sysconfdir}/ipmi
%config(noreplace) %{_sysconfdir}/ipmi/*
###### perl files ######
%dir %{perl_vendorarch}/auto/OpenIPMI
%{perl_vendorarch}/auto/OpenIPMI/OpenIPMI.so
%{perl_vendorarch}/OpenIPMI.pm
%doc swig/perl/sample swig/perl/ipmi_powerctl
###### ui files ######
%{_bindir}/ipmi_sim

%{_bindir}/ipmi_ui
%{_bindir}/ipmicmd
%{_bindir}/openipmicmd
%{_bindir}/ipmish
%{_bindir}/openipmish
%{_bindir}/sdrcomp
%{_bindir}/solterm
%{_bindir}/rmcp_ping
%{_bindir}/openipmi_eventd
%{_mandir}/man1/ipmi_ui.1*
%{_mandir}/man1/openipmicmd.1*
%{_mandir}/man1/openipmish.1*
%{_mandir}/man1/solterm.1*
%{_mandir}/man1/openipmi_eventd.1*
%{_mandir}/man1/rmcp_ping.1*
%{_mandir}/man1/ipmi_sim.1*
%{_mandir}/man5/ipmi_lan.5*
%{_mandir}/man5/ipmi_sim_cmd.5*
%{_mandir}/man7/ipmi_cmdlang.7*
%{_mandir}/man7/openipmi_conparms.7*
###### lanserv files #####
%{_bindir}/ipmilan
%{_mandir}/man8/ipmilan.8*

%files -n libOpenIPMI0
%{_libdir}/libIPMIlanserv.so.*
%{_libdir}/libOpenIPMI.so.*
%{_libdir}/libOpenIPMIcmdlang.so.*
%{_libdir}/libOpenIPMIglib.so.*
%{_libdir}/libOpenIPMIposix.so.*
%{_libdir}/libOpenIPMIpthread.so.*
%{_libdir}/libOpenIPMIutils.so.*

%files -n libOpenIPMIui1
%{_libdir}/libOpenIPMIui.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%if 0%{?doc_build}
%doc doc/IPMI.pdf
%endif
###################################################

%files python3
%{python3_sitearch}/*OpenIPMI.*
%doc swig/OpenIPMI.i
###### gui files ######
%dir %{python3_sitearch}/openipmigui
%{python3_sitearch}/openipmigui/*
%{python3_sitearch}/__pycache__/*
%attr(755,root,root) %{_bindir}/openipmigui
%{_mandir}/man1/openipmigui.1*

%changelog
