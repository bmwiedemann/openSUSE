#
# spec file for package arptables
#
# Copyright (c) 2019 SUSE LLC
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


Name:           arptables
Version:        0.0.5
Release:        0
Summary:        User Space Tool to Set Up and Maintain ARP Filtering Tables
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            http://ebtables.sourceforge.net/

#Git-Clone:	git://git.netfilter.org/arptables
Source:         http://ftp.netfilter.org/pub/arptables/arptables-%version.tar.gz
Source2:        http://ftp.netfilter.org/pub/arptables/arptables-%version.tar.gz.sig
Source3:        %name.keyring
BuildRequires:  coreutils
BuildRequires:  perl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description
arptables is a user space tool used to set up and maintain the tables
of ARP rules in the Linux kernel. These rules inspect the ARP frames.
arptables is similar to the iptables userspace tool, but less
complicated.

%prep
%autosetup -p1

%build
make %{?_smp_mflags} all PREFIX="%_prefix" COPT_FLAGS="%optflags -W -Wall"

%install
%make_install PREFIX="%_prefix" MANDIR="%_mandir"
# This is a RH-specific init script
rm -Rf "%buildroot/etc/rc.d"

b="%buildroot"
mv "$b/%_sbindir/arptables-restore" "$b/%_sbindir/arptables-legacy-restore"
mv "$b/%_sbindir/arptables-save" "$b/%_sbindir/arptables-legacy-save"
for i in arptables arptables-restore arptables-save; do
	ln -fs "/etc/alternatives/$i" "$b/%_sbindir/$i"
done

%post
update-alternatives --force \
	--install "%_sbindir/arptables" arptables "%_sbindir/arptables-legacy" 1 \
	--slave "%_sbindir/arptables-restore" arptables-restore "%_sbindir/arptables-legacy-restore" \
	--slave "%_sbindir/arptables-save" arptables-save "%_sbindir/arptables-legacy-save"

%postun
if test "$1" = 0; then
	update-alternatives --remove arptables "%_sbindir/arptables-legacy"
fi

%files
%defattr(-,root,root)
%ghost %_sysconfdir/alternatives/arptables
%ghost %_sysconfdir/alternatives/arptables-restore
%ghost %_sysconfdir/alternatives/arptables-save
%_sbindir/arptables*
%_mandir/*/arptables*
%doc COPYING

%changelog
