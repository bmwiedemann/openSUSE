#
# spec file for package davfs2
#
# Copyright (c) 2023 SUSE LLC
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


Name:           davfs2
Version:        1.7.0
Release:        0
Summary:        FUSE-Filesystem to access WebDAV servers
License:        GPL-3.0-only
Group:          System/Filesystems
URL:            https://savannah.nongnu.org/projects/%{name}
Source0:        https://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1:        https://download.savannah.nongnu.org/releases/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        %{name}-rpmlintrc
# Taken from https://savannah.nongnu.org/project/release-gpgkeys.php?group=davfs2&download=1
Source3:        davfs2.keyring
BuildRequires:  automake >= 1.16
BuildRequires:  fuse-devel >= 2.2
BuildRequires:  neon-devel
BuildRequires:  pwdutils
Requires:       fuse >= 2.2
Requires(pre):  %{_sbindir}/groupadd
Requires(pre):  %{_sbindir}/useradd
Obsoletes:      fuse-%{name} < %{version}
Provides:       fuse-%{name} = %{version}

%description
davfs2 is a FUSE file system driver that allows mounting a WebDAV server
as a local file system, like a disk drive. This way, applications can access
resources on a Web server without knowing anything about HTTP or WebDAV.

davfs2 runs as a daemon in userspace. It uses the kernel file system "coda", or
FUSE. To connect to the WebDAV server, it makes use of the neon library,
supporting TLS/SSL and access via proxy servers.

%prep
%setup -q
cd src

%build
dav_user="%{name}" \
dav_group="%{name}" \
%configure \
%if 0%{?suse_version} >= 1550
    ssbindir="%{_sbindir}" \
%endif
    --disable-static
%if 0%{?suse_version} >= 1000
PIE="-fPIE"
pie="-pie"
%endif
%make_build AM_CFLAGS="-Wall %{optflags} $PIE" AM_LDFLAGS="$pie"

%install
%make_install
rm -rf "%{buildroot}%{_datadir}/doc"
install -d "%{buildroot}%{_localstatedir}/cache/%{name}"
%find_lang %{name}
rm -rf "%{buildroot}/%{_docdir}"

%pre
%{_bindir}/getent group %{name} >/dev/null || %{_sbindir}/groupadd -r %{name}
%{_bindir}/getent passwd %{name} >/dev/null || %{_sbindir}/useradd -r -g %{name} -d %{_localstatedir}/cache/%{name} %{name}

%post
%if 0%{?set_permissions:1} > 0
    %set_permissions "%{_sbindir}/mount.davfs"
%else
%if 0%{?run_permissions:1} > 0
    %run_permissions
%endif
%endif

%if 0%{?suse_version} >= 1120
%verifyscript
%verify_permissions -e %{_sbindir}/mount.davfs
%endif

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%license COPYING
%doc AUTHORS BUGS FAQ NEWS README* THANKS TODO etc/%{name}.conf etc/secrets
%{_mandir}/man5/%{name}.conf.5%{?ext_man}
%{_mandir}/man8/mount.davfs.8%{?ext_man}
%{_mandir}/man8/umount.davfs.8%{?ext_man}
%{_mandir}/*/man5/%{name}.conf.5%{?ext_man}
%{_mandir}/*/man8/mount.davfs.8%{?ext_man}
%{_mandir}/*/man8/umount.davfs.8%{?ext_man}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%config %{_sysconfdir}/%{name}/secrets
%config %{_sysconfdir}/%{name}/certs/
%verify(not user group mode) %attr(0755,root,root) %{_sbindir}/mount.davfs
%{_sbindir}/umount.davfs
%{_datadir}/%{name}
%attr(0750, %{name}, %{name}) %{_localstatedir}/cache/%{name}
%if 0%{?suse_version} < 1550
/sbin/mount.davfs
/sbin/umount.davfs
%endif

%changelog
