#
# spec file for package irda
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define _udevrulesdir %(pkg-config --variable=udevdir udev)/rules.d
Name:           irda
Version:        0.9.18
Release:        0
Summary:        Necessary Tools for Using the Infrared Port
License:        GPL-2.0+
Group:          Hardware/Other
Url:            http://irda.sourceforge.net
Source:         http://sourceforge.net/projects/irda/files/irda-utils/%{version}/irda-utils-%{version}.tar.gz
Source1:        52-irda.rules
Source2:        irattach.service
Source3:        irda-0.9.18.sysconfig
Source4:        irda-rpmlintrc
Patch1:         irda-0.9.18-psion-no-strict-aliasing.diff
Patch2:         irda-0.9.18-irnetd-install.diff
Patch3:         irda-0.9.18-findchip-ppc.diff
Patch4:         irda-0.9.18-irdadump-flush-stdout.diff
Patch5:         irda-utils-0.9.18-fix-irkbd-makefile.diff
Patch6:         irda-utils-0.9.16-fix-off-by-one.diff
Patch7:         irda-libpci_with_libz.diff
Patch8:         irda-0.9.18-buildroot.diff
Patch9:         irda-0.9.18-no-findchip-smc.diff
Patch10:        irda-optflags.diff
Patch11:        irda-fix_link_command.diff
Patch12:        irda-exit_on_error.diff
Patch13:        irda-irdaping_no_strict_aliasing.diff
Patch14:        irda-no_std_paths.diff
Patch15:        irda-parseoldasssysconfig.patch
BuildRequires:  glib2-devel
BuildRequires:  linux-kernel-headers
BuildRequires:  pciutils-devel
BuildRequires:  pkgconfig(libHX)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
Requires(pre):  %fillup_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}

%description
This package contains all necessary scripts and programs for setting up
and using the infrared port for printing or communicating. The start
and stop scripts are prepared to access the UART emulation ('SIR' mode)
with 115 kbit/s data transfer rate. This is supported by most laptops
with an infrared interface.

After starting the infrared protocol manager 'irmanger' with the
command 'rcirda start', you can send data to your printer using the
device file /dev/irlpt0. If you like to talk to other computers with
infrared interface or to a mobile phone, you can use the serial
emulation provided by the device file /dev/ircomm0.

Take a look at the README file located in
%{_docdir}/irda/README and the IRDA HOWTO in
%{_datadir}/doc/howto/en/IR-HOWTO.gz. If the infrared port on your
laptop is located on an IO or IRQ address other than IO address 0x2f8
(/dev/ttyS1) or interrupt 3, you should use YaST to change the
variables IRDA_PORT and IRDA_IRQ in the configuration file
%{_sysconfdir}/rc.config.

%prep
%setup -q -n irda-utils-%{version}
%patch1
%patch2
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8
%patch9
%patch10
%patch11
%patch12
%patch13
%patch14
%patch15

%build
make %{?_smp_mflags} V=1 RPM_OPT_FLAGS="%{optflags} -fgnu89-inline -D_GNU_SOURCE -D_FILE_OFFSET_BITS=64" INITD=%{_sysconfdir}/init.d ROOT=%{buildroot} all

%install
install -d -m 755 %{buildroot}%{_prefix}/sbin
install -d -m 755 %{buildroot}%{_prefix}/bin
install -d -m 755 %{buildroot}%{_docdir}/irda
install -d -m 755 %{buildroot}%{_fillupdir}
make INITD=%{_sysconfdir}/init.d \
             DOCDIR=%{_defaultdocdir}/irda \
             ROOT=%{buildroot} \
	MANDIR=%{_mandir} \
	install
rm %{buildroot}%{_sysconfdir}/sysconfig/irda %{buildroot}%{_sysconfdir}/sysconfig/network-scripts/ifcfg-irlan0
rmdir %{buildroot}%{_sysconfdir}/sysconfig/network-scripts
#documentation, READMEs
install -m 644 README %{buildroot}%{_docdir}/irda/
install -m 644 ethereal/README %{buildroot}%{_docdir}/irda/README.ethereal
install -m 644 irattach/README %{buildroot}%{_docdir}/irda/README.irattach
install -m 644 irdadump/README %{buildroot}%{_docdir}/irda/README.irdadump
install -m 644 ethereal/README %{buildroot}%{_docdir}/irda/README.ethereal
install -m 644 irdaping/README %{buildroot}%{_docdir}/irda/README.irdaping
install -m 644 ethereal/README %{buildroot}%{_docdir}/irda/README.ethereal
install -m 644 irsockets/README %{buildroot}%{_docdir}/irda/README.irsockets
install -m 644 tekram/README %{buildroot}%{_docdir}/irda/README.tekram
# udev stuff
install -D -m 644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/52-irda.rules
# sysconfig template
install -m 644 %{SOURCE3} %{buildroot}%{_fillupdir}/sysconfig.irda
install -D -m 0644 %{SOURCE2} %{buildroot}%{_unitdir}/irattach.service
ln -sv %{_sbindir}/service %{buildroot}%{_sbindir}/rcirattach

%pre
%service_add_pre irattach.service

%post
%{fillup_only -n irda}
%service_add_post irattach.service
%udev_rules_update

%preun
%service_del_preun irattach.service

%postun
%service_del_postun irattach.service

%files
%defattr(-,root,root)
%doc %{_docdir}/irda
%{_sbindir}/*
%{_bindir}/*
%doc %{_mandir}/man4/*
%doc %{_mandir}/man7/*
%doc %{_mandir}/man8/*
%{_fillupdir}/sysconfig.irda
%{_udevrulesdir}/52-irda.rules
%{_unitdir}/irattach.service

%changelog
