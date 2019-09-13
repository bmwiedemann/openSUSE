#
# spec file for package postsrsd
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           postsrsd
Version:        1.2.g9
Release:        0
Summary:        Sender Rewriting Support for postfix
License:        GPL-2.0
Group:          Productivity/Networking/Email/Servers
Url:            https://github.com/roehling/postsrsd

#Git-Clone:	git://github.com/roehling/postsrsd
#Snapshot:	1.2-9-gb161cb4 ; no regular release tarballs available
Source:         %name-%version.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz

%description
PostSRSd provides the Sender Rewriting Scheme (SRS) via TCP-based 
lookup tables for Postfix. SRS is needed if your mail server acts
as forwarder.

%prep
%setup -qn %name

%build
%cmake -DGENERATE_SRS_SECRET=0 -DCHROOT_DIR=/var/lib/empty \
	-DUSE_APPARMOR=1 -DINIT_FLAVOR=systemd
%make_jobs

%install
%cmake_install
b="%buildroot"
mkdir -p "$b/%_prefix/lib/systemd/system" "$b/%_defaultdocdir"
mv "$b/%_sysconfdir/systemd/system"/* "$b/%_prefix/lib/systemd/system/"
mv "$b/%_datadir/doc/%name" "$b/%_defaultdocdir/"
cp README.md "$b/%_defaultdocdir/%name/"
ln -s service "$b/%_sbindir/rcpostsrsd"

%pre
%service_add_pre postsrsd.service

%post
s="%_sysconfdir/postsrsd.secret"
if [ ! -e "$s" ]; then
	echo "No postsrsd secret found in $s, generating one."
	dd if=/dev/urandom of="$s" bs=64 count=1
fi
%service_add_post postsrsd.service

%preun
%service_del_preun postsrsd.service

%postun
%service_del_postun postsrsd.service

%files
%defattr(-,root,root)
%dir %_sysconfdir/apparmor.d
%config %_sysconfdir/apparmor.d/*
%config(noreplace) %_sysconfdir/default/postsrsd
%ghost %_sysconfdir/postsrsd.secret
%_sbindir/postsrsd
%_sbindir/rcpostsrsd
%_prefix/lib/systemd/system/*.service
%_docdir/%name/
%doc LICENSE

%changelog
