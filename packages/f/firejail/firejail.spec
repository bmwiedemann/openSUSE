#
# spec file for package firejail
#
# Copyright (c) 2020 SUSE LLC
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


Name:           firejail
Version:        0.9.62
Release:        0
Summary:        Linux namepaces sandbox program
License:        GPL-2.0-only
Group:          Productivity/Security
URL:            https://firejail.wordpress.com/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
Source1:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz.asc
# PATCH-FIX-OPENSUSE firejail-0.9.62-fix-usr-etc.patch -- https://github.com/netblue30/firejail/issues/3145 two patches combined, source see file
Patch0:         firejail-0.9.62-fix-usr-etc.patch
# PATHCH-FIX-UPSTREAM fix-CVE-2020-17367 -- fixes boo#1174986
Patch1:         https://github.com/netblue30/firejail/commit/2c734d6350ad321fccbefc5ef0382199ac331b37.patch#/fix-CVE-2020-17367.patch
# PATHCH-FIX-UPSTREAM fix-CVE-2020-17368 -- fixes boo#1174986
Patch2:         https://github.com/netblue30/firejail/commit/34193604fed04cad2b7b6b0f1a3a0428afd9ed5b.patch#/fix-CVE-2020-17368.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libapparmor-devel
Requires(pre):  shadow
PreReq:         permissions

%description
Firejail is a SUID sandbox program that reduces the risk of security
breaches by restricting the running environment of untrusted applications
using Linux namespaces and seccomp-bpf. It includes sandbox profiles for
many existing applications like Iceweasel/Mozilla Firefox and Chromium.

Firejail also expands the restricted shell facility found in bash by adding
Linux namespace support. It supports sandboxing specific users upon login.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
sed -i '1s/^#!\/usr\/bin\/env /#!\/usr\/bin\//' contrib/fj-mkdeb.py contrib/fjclip.py contrib/fjdisplay.py contrib/fjresize.py contrib/sort.py

%build
%configure --docdir=%{_docdir}/%{name} \
	   --enable-apparmor
make %{?_smp_mflags} VERBOSE=1

%pre
getent group firejail >/dev/null || groupadd -r firejail
exit 0

%install
%make_install
%fdupes -s %{buildroot}

%post
%set_permissions %{_bindir}/firejail

%verifyscript
%verify_permissions -e %{_bindir}/firejail

%files
%attr(4750,root,firejail) %verify(not user group mode) %{_bindir}/firejail
%{_bindir}/firecfg
%{_bindir}/firemon
%{_datadir}/bash-completion
%{_libdir}/%{name}
%doc %{_docdir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man5/*
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/*
%config %{_sysconfdir}/apparmor.d/firejail-default
%config %{_sysconfdir}/apparmor.d/local/firejail-local
%dir %{_sysconfdir}/apparmor.d
%dir %{_sysconfdir}/apparmor.d/local

%changelog
