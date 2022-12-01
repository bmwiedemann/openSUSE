#
# spec file for package patterns-server
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


%bcond_with betatest
Name:           patterns-server
Version:        20210330
Release:        0
Summary:        Patterns for Installation (server patterns)
License:        MIT
Group:          Metapackages
URL:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
Source1:        pattern-definition-32bit.txt
Source2:        create_32bit-patterns_file.pl
Source3:        pre_checkin.sh
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains all the server related patterns

################################################################################
%package dhcp_dns_server
%pattern_serverfunctions
Summary:        DHCP and DNS Server
Group:          Metapackages
Provides:       pattern() = dhcp_dns_server
Provides:       pattern-icon() = pattern-server
Provides:       pattern-order() = 3040
Provides:       pattern-visible()
Requires:       bind
Requires:       dhcp-server
Requires:       pattern() = basesystem
Recommends:     bind-chrootenv
Recommends:     bind-doc
Recommends:     dhcp
Recommends:     dhcp-relay
Recommends:     yast2-dhcp-server
Recommends:     yast2-dns-server
%if 0%{?is_opensuse}
Provides:       patterns-openSUSE-dhcp_dns_server = %{version}
Obsoletes:      patterns-openSUSE-dhcp_dns_server < %{version}
%else
Provides:       patterns-sles-dhcp_dns_server = %{version}
Obsoletes:      patterns-sles-dhcp_dns_server < %{version}
%endif

%description dhcp_dns_server
Software to set up a server for the Dynamic Host Configuration Protocol (DHCP) and the Domain Name System (DNS) services. DHCP provides configuration parameters to client computers to integrate them into a network, whereas DNS delivers information associated with domain names, in particular, the IP address.

%files dhcp_dns_server
%dir %{_docdir}/patterns
%{_docdir}/patterns/dhcp_dns_server.txt

################################################################################

%package directory_server
%pattern_serverfunctions
Summary:        Directory Server (LDAP)
Group:          Metapackages
Provides:       pattern() = directory_server
Provides:       pattern-icon() = pattern-server
Provides:       pattern-order() = 3060
Provides:       pattern-visible()
Requires:       pattern() = basesystem
# bsc#1084789
Recommends:     389-ds
Recommends:     nss_ldap
Recommends:     pam_ldap
Recommends:     yast2-ldap-server
%if 0%{?is_opensuse}
Provides:       patterns-openSUSE-directory_server = %{version}
Obsoletes:      patterns-openSUSE-directory_server < %{version}
%else
Provides:       patterns-sles-directory_server = %{version}
Obsoletes:      patterns-sles-directory_server < %{version}
%endif

%description directory_server
Software to set up a directory server with OpenLDAP. The Lightweight Directory Access Protocol (LDAP) is used to access online directory services.

%files directory_server
%dir %{_docdir}/patterns
%{_docdir}/patterns/directory_server.txt

################################################################################

%package file_server
%pattern_serverfunctions
Summary:        File Server
Group:          Metapackages
Provides:       pattern() = file_server
Provides:       pattern-icon() = pattern-server
Provides:       pattern-order() = 2900
Provides:       pattern-visible()
Requires:       nfs-kernel-server
Requires:       pattern() = basesystem
Recommends:     nfsidmap
Recommends:     samba
Recommends:     samba-client
Recommends:     samba-winbind
Recommends:     tftp
Recommends:     vsftpd
%if 0%{?is_opensuse}
Provides:       patterns-openSUSE-file_server = %{version}
Obsoletes:      patterns-openSUSE-file_server < %{version}
%else
Provides:       patterns-sles-file_server = %{version}
Obsoletes:      patterns-sles-file_server < %{version}
%endif
%if 0%{?is_opensuse}
Recommends:     yast2-ftp-server
Recommends:     yast2-nfs-server
Recommends:     yast2-samba-server
Recommends:     yast2-tftp-server
Suggests:       atftp
%endif

%description file_server
File services to host files so that they may be accessed or retrieved by other computers on the same network. This includes the FTP, SMB, and NFS protocols.

%files file_server
%dir %{_docdir}/patterns
%{_docdir}/patterns/file_server.txt

################################################################################

%package gateway_server
%pattern_serverfunctions
Summary:        Internet Gateway
Group:          Metapackages
Provides:       pattern() = gateway_server
Provides:       pattern-icon() = pattern-server
Provides:       pattern-order() = 3020
Provides:       pattern-visible()
Requires:       pattern() = basesystem
Recommends:     arptables
Recommends:     calamaris
Recommends:     ddclient
Recommends:     fetchmail
Recommends:     fetchmailconf
Recommends:     ipsec-tools
Recommends:     quagga
Recommends:     radvd
Recommends:     rarpd
Recommends:     squid
Recommends:     whois
Recommends:     wireshark
Recommends:     wondershaper
%if 0%{?is_opensuse}
Provides:       patterns-openSUSE-gateway_server = %{version}
Obsoletes:      patterns-openSUSE-gateway_server < %{version}
%else
Provides:       patterns-sles-gateway_server = %{version}
Obsoletes:      patterns-sles-gateway_server < %{version}
%endif

%description gateway_server
Software to set up a proxy, firewall, and gateway server, including a virtual private network (VPN) gateway.

%files gateway_server
%dir %{_docdir}/patterns
%{_docdir}/patterns/gateway_server.txt

################################################################################

%package kvm_server
%pattern_serverfunctions
Summary:        KVM Host Server
Group:          Metapackages
Provides:       pattern() = kvm_server
Provides:       pattern-icon() = pattern-server
Provides:       pattern-order() = 3099
Provides:       pattern-visible()
Requires:       tftp
Requires:       pattern() = basesystem
Recommends:     libvirt-daemon-qemu
Recommends:     tigervnc
Recommends:     virt-install
Recommends:     vm-install
%if 0%{?is_opensuse}
Provides:       patterns-openSUSE-kvm_server = %{version}
Obsoletes:      patterns-openSUSE-kvm_server < %{version}
%else
Provides:       patterns-sles-kvm_server = %{version}
Obsoletes:      patterns-sles-kvm_server < %{version}
%endif
# fix issue because qemu-kvm is not present on all arch and
# we would like to deprecate it for the futur (will be only
# updated if already installed on the system)
%ifarch %ix86 x86_64
Requires:       qemu-x86
%endif
%ifarch ppc ppc64 ppc64le
Requires:       qemu-ppc
%endif
%ifarch s390x
Requires:       qemu-s390x
%endif
%ifarch %arm %arm64
Requires:       qemu-arm
Requires:       qemu-ipxe
%endif

%description kvm_server
Software to set up a server for configuring, managing, and monitoring virtual machines on a single physical machine.

%files kvm_server
%dir %{_docdir}/patterns
%{_docdir}/patterns/kvm_server.txt

################################################################################

%package kvm_tools
%pattern_basetechnologies
Summary:        KVM Virtualization Host and tools
Group:          Metapackages
Provides:       pattern() = kvm_tools
Provides:       pattern-icon() = pattern-server
Provides:       pattern-order() = 1090
Provides:       pattern-visible()
Requires:       libvirt-client
Requires:       libvirt-daemon-config-network
Requires:       libvirt-daemon-qemu
Requires:       tigervnc
Requires:       pattern() = basesystem
Requires:       pattern() = kvm_server
# bnc#868542
Requires:       virt-manager
Requires:       vm-install
Recommends:     openssh
# BSC#1078908
Recommends:     vim
Recommends:     virt-install
Recommends:     virt-v2v
Recommends:     virt-viewer
Recommends:     xorg-x11-xauth
Recommends:     yast2-control-center
Recommends:     yast2-ncurses
Recommends:     yast2-ncurses-pkg
Recommends:     yast2-vm
%if !0%{?is_opensuse}
Provides:       patterns-sles-kvm_tools = %{version}
Obsoletes:      patterns-sles-kvm_tools < %{version}
%endif

%description kvm_tools
This will provide all minimal system to get a running KVM Hypervisor
and be able to configure, manage, and monitor virtual machines on a
single physical machine.

%files kvm_tools
%dir %{_docdir}/patterns
%{_docdir}/patterns/kvm_tools.txt

################################################################################

%package lamp_server
%pattern_serverfunctions
Summary:        Web and LAMP Server
Group:          Metapackages
Provides:       pattern() = lamp_server
Provides:       pattern-icon() = pattern-web-devel
Provides:       pattern-order() = 3000
Provides:       pattern-visible()
Requires:       apache2
Requires:       pattern() = basesystem
Recommends:     apache2-doc
Recommends:     apache2-example-pages
Recommends:     apache2-mod_php8
Recommends:     apache2-mod_python
Recommends:     apache2-prefork
Recommends:     libapr-util1
Recommends:     libapr1
Recommends:     mariadb
Recommends:     perl
Recommends:     yast2-http-server
%if 0%{?is_opensuse}
Provides:       patterns-openSUSE-lamp_server = %{version}
Obsoletes:      patterns-openSUSE-lamp_server < %{version}
%else
Provides:       patterns-sles-lamp_server = %{version}
Obsoletes:      patterns-sles-lamp_server < %{version}
%endif

%description lamp_server
Software to set up a Web server that is able to serve static, dynamic, and interactive content (like a Web shop). This includes Apache HTTP Server, the database management system MySQL, and scripting languages such as PHP, Python, Ruby on Rails, or Perl.

%files lamp_server
%dir %{_docdir}/patterns
%{_docdir}/patterns/lamp_server.txt

################################################################################

%package mail_server
%pattern_serverfunctions
Summary:        Mail and News Server
Group:          Metapackages
Provides:       pattern() = mail_server
Provides:       pattern-icon() = pattern-server
Provides:       pattern-order() = 2980
Provides:       pattern-visible()
Requires:       vacation
Requires:       pattern() = basesystem
Recommends:     amavisd-new
Recommends:     clamav
Recommends:     cyrus-imapd
Recommends:     inn
Recommends:     mailman
Recommends:     spamassassin
%if 0%{?is_opensuse}
Provides:       patterns-openSUSE-mail_server = %{version}
Obsoletes:      patterns-openSUSE-mail_server < %{version}
%else
Provides:       patterns-sles-mail_server = %{version}
Obsoletes:      patterns-sles-mail_server < %{version}
%endif

%description mail_server
Software to set up electronic mail and message services to handle email, mailing, and news lists, including a virus scanner to scan messages at the server level.

%files mail_server
%dir %{_docdir}/patterns
%{_docdir}/patterns/mail_server.txt

################################################################################

%package printing
%pattern_serverfunctions
Summary:        Print Server
Group:          Metapackages
Provides:       pattern() = print_server
Provides:       pattern-icon() = pattern-server
Provides:       pattern-order() = 2960
Provides:       pattern-visible()
Requires:       cups
Requires:       pattern() = basesystem
Recommends:     OpenPrintingPPDs-ghostscript
Recommends:     OpenPrintingPPDs-hpijs
Recommends:     OpenPrintingPPDs-postscript
Recommends:     cups-backends
Recommends:     cups-filters
Recommends:     cups-filters-cups-browsed
Recommends:     cups-filters-foomatic-rip
Recommends:     cups-filters-ghostscript
Recommends:     epson-inkjet-printer-escpr
Recommends:     gutenprint
Recommends:     hplip-hpijs
Recommends:     manufacturer-PPDs
Recommends:     samba
Recommends:     splix
%if 0%{?is_opensuse}
Provides:       patterns-openSUSE-print_server = %{version}
Obsoletes:      patterns-openSUSE-print_server < %{version}
%else
Provides:       patterns-sles-printing = %{version}
Obsoletes:      patterns-sles-printing < %{version}
%endif

%description printing
This pattern provides all packages necessary for printing. It provides all
needed packages for printing to a locally connected printer, printing using a
remote print server and for setting up a print server.

%files printing
%dir %{_docdir}/patterns
%{_docdir}/patterns/printing.txt

################################################################################

# BSC#1088175
%ifarch x86_64
%package xen_server
%pattern_serverfunctions
Summary:        Xen Virtual Machine Host Server
Group:          Metapackages
Provides:       pattern() = xen_server
Provides:       pattern-icon() = pattern-server
Provides:       pattern-order() = 3080
Provides:       pattern-visible()
Requires:       kernel-xen
Requires:       tftp
Requires:       xen
Requires:       xen-libs
Requires:       xen-tools
Requires:       pattern() = basesystem
Recommends:     libvirt-daemon-xen
Recommends:     tigervnc
# #382423
Recommends:     virt-install
Recommends:     vm-install
%if 0%{?is_opensuse}
Provides:       patterns-openSUSE-xen_server = %{version}
Obsoletes:      patterns-openSUSE-xen_server < %{version}
%else
Provides:       patterns-sles-xen_server = %{version}
Obsoletes:      patterns-sles-xen_server < %{version}
%endif

%description xen_server
Software to set up a server for configuring, managing, and monitoring virtual machines on a single physical machine.

%files xen_server
%dir %{_docdir}/patterns
%{_docdir}/patterns/xen_server.txt
%endif

################################################################################
# BSC#1088175
%ifarch x86_64
%package xen_tools
%pattern_basetechnologies
Summary:        XEN Virtualization Host and tools
Group:          Metapackages
Provides:       pattern() = xen_tools
Provides:       pattern-icon() = pattern-server
Provides:       pattern-order() = 1080
Provides:       pattern-visible()
Requires:       libvirt-client
Requires:       libvirt-daemon-config-network
Requires:       libvirt-daemon-xen
Requires:       tigervnc
Requires:       pattern() = basesystem
Requires:       pattern() = xen_server
# bnc#868542
Requires:       virt-manager
Requires:       vm-install
Recommends:     openssh
# BSC#1078908
Recommends:     vim
Recommends:     virt-install
Recommends:     virt-viewer
#Recommends:     sles-xen_en-pdf
Recommends:     xen-doc-html
Recommends:     xorg-x11-xauth
Recommends:     yast2-control-center
Recommends:     yast2-ncurses
Recommends:     yast2-ncurses-pkg
Recommends:     yast2-vm
%if !0%{?is_opensuse}
Provides:       patterns-sles-xen_tools = %{version}
Obsoletes:      patterns-sles-xen_tools < %{version}
%endif

%description xen_tools
This will provide all minimal system to get a running XEN Hypervisor
and be able to configure, manage, and monitor virtual machines on a
single physical machine.

%files xen_tools
%dir %{_docdir}/patterns
%{_docdir}/patterns/xen_tools.txt
%endif

################################################################################

%prep

%build

%install
mkdir -p "%{buildroot}%{_docdir}/patterns"
for i in dhcp_dns_server directory_server file_server gateway_server \
    lamp_server mail_server printing
    do
	echo "This file marks the pattern $i to be installed." \
		>"%{buildroot}%{_docdir}/patterns/$i.txt"
    echo "This file marks the pattern $i-32bit to be installed." \
        >"%{buildroot}%{_docdir}/patterns/$i-32bit.txt"
done
# NO 32bits pattern for KVM or XEN
for i in kvm_tools kvm_server
    do
    echo "This file marks the pattern $i to be installed." \
        > "%{buildroot}%{_docdir}/patterns/$i.txt"
done
# XEN is only available on x86_64
%ifarch x86_64
    for i in xen_server xen_tools; do
    echo "This file marks the pattern $i to be installed." \
        >"%{buildroot}%{_docdir}/patterns/$i.txt"
done
%endif

#
# This file is created at check-in time. Sorry for the inconsistent workflow :(
#
%include %{SOURCE1}

%changelog
