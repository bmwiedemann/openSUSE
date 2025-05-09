#
# spec file for package blog
#
# Copyright (c) 2025 SUSE LLC
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


Name:           blog
Version:        2.35
%define sonum   2
Release:        0
Summary:        Boot logging
License:        GPL-2.0-or-later
Group:          System/Base
URL:            https://github.com/bitstreamout/showconsole
Source:         https://github.com/bitstreamout/showconsole/archive/v%{version}.tar.gz#/showconsole-%{version}.tar.gz
Source1:        blog-rpmlintrc
BuildRequires:  bash
%if 0%{suse_version} >= 1550
# regenerate_initrd_post moved to rpm-config-SUSE:initrd.macros
BuildRequires:  rpm-config-SUSE >= 0.g11
%{regenerate_initrd_requires}
%else
Requires(post): /usr/bin/mkdir
Recommends:     suse-module-tools
%endif
Requires(post): coreutils
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       sysvinit-tools:/sbin/blogd
Suggests:       blog-plymouth = %{version}

%description
The blogd daemon determines the real underlying character device of
/dev/console. Blogd spawns a pty/tty pair to reconnect the current
/dev/console with the slave of the pty/tty pair. During writing
information from this slave to the real character device a ring
buffer is used to hold the information for writing it to an existing
logging file.

%package -n libblogger%{sonum}
Summary:        FIFO interface used by startproc
Group:          System/Libraries
%if %sonum == 2
Provides:       %{name}:%{_libdir}/libblogger.so.2
%endif

%description -n libblogger%{sonum}
The libaray for the FIFO interface used by the LSB startproc command.

%package	plymouth
Summary:        Replaces plymouth by blogd
Group:          System/Base
Requires:       blog = %{version}
Requires:       systemd
Conflicts:      plymouth
Conflicts:      plymouth-dracut

%description	plymouth
The Blogd daemon can be used as a replacement for Plymouth in situations where
a splash screen and/or usage of a frame buffer is unwanted.  The Blogd is also
a Plymouth agent. That means, it can handle requests for a password prompt by
the system password service of systemd.
The blogd daemon writes out boot log messages to every terminal device used by
/dev/console and to the log file /var/log/boot.log.  When halting or rebooting
the system, it moves the log file to /var/log/boot.old and appends all log
messages upto to point at which the file systems becomes unavailable.

%package	devel
Summary:        Provides library and header for boot logging
Group:          Development/Libraries/C and C++
Requires:       libblogger%{sonum} = %{version}

%description	devel
The libaray and the header file for the FIFO interface used to build
the LSB startproc command.

%prep
%setup -q -n showconsole-%version
for l in rt util pthread
do
    ln -sf %{_libdir}/lib${l}.so.[0-9] lib${l}.so
done

%build
make V=1 %{?_smp_mflags} CC="%__cc" \
    LIBDIR=%{_libdir} \
    INCDIR=%{_includedir} \
    SYSDUNITS=%{_unitdir} \
    BOOT_LOGFILE=%{_localstatedir}/log/boot.log \
    BOOT_OLDLOGFILE=%{_localstatedir}/log/boot.old

%install
%make_install \
    MANPATH=%{_mandir} \
    INSTBINFLAGS="-m 0744" \
%if 0%{?suse_version} >= 1550
    SBINDIR=%{_sbindir} \
%endif
    LIBDIR=%{_libdir} \
    INCDIR=%{_includedir} \
    SYSDUNITS=%{_unitdir} \
    BOOT_LOGFILE=%{_localstatedir}/log/boot.log \
    BOOT_OLDLOGFILE=%{_localstatedir}/log/boot.old

rm %{buildroot}%{_unitdir}/systemd-ask-password-blog.service.wants/systemd-vconsole-setup.service

%post   -n libblogger%{sonum} -p /sbin/ldconfig
%postun -n libblogger%{sonum} -p /sbin/ldconfig

%post   plymouth
ln -sf ../systemd-vconsole-setup.service %{_unitdir}/systemd-ask-password-blog.service.wants/
test -x /bin/systemctl && /bin/systemctl daemon-reload >/dev/null 2>&1 || :
%if 0%{suse_version} >= 1550
%{regenerate_initrd_post}
%else
! command -v mkdir >/dev/null || mkdir -p /run/regenerate-initrd/
test ! -d /run/regenerate-initrd || > /run/regenerate-initrd/all
%endif

%postun plymouth
test -x /bin/systemctl && /bin/systemctl daemon-reload >/dev/null 2>&1 || :

%posttrans plymouth
%if 0%{suse_version} >= 1550
%{regenerate_initrd_posttrans}
%else
if test -x /usr/lib/module-init-tools/regenerate-initrd-posttrans
then
    /usr/lib/module-init-tools/regenerate-initrd-posttrans
fi
%endif

%files
%defattr(-,root,root)
%license COPYING
%doc README
%if 0%{?suse_version} < 1550
/sbin/blogctl
/sbin/blogd
/sbin/blogger
/sbin/isserial
/sbin/setconsole
/sbin/showconsole
%else
%{_sbindir}/blogctl
%{_sbindir}/blogd
%{_sbindir}/blogger
%{_sbindir}/isserial
%{_sbindir}/setconsole
%{_sbindir}/showconsole
%endif
%doc %{_mandir}/man8/blogctl.8.gz
%doc %{_mandir}/man8/blogd.8.gz
%doc %{_mandir}/man8/blogger.8.gz
%doc %{_mandir}/man8/isserial.8.gz
%doc %{_mandir}/man8/setconsole.8.gz
%doc %{_mandir}/man8/showconsole.8.gz

%files -n libblogger%{sonum}
%{_libdir}/libblogger.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/libblogger.h
%{_libdir}/libblogger.so

%files plymouth
%defattr(-,root,root)
%dir %{_prefix}/lib/dracut/
%dir %{_prefix}/lib/dracut/modules.d/
%dir %{_prefix}/lib/dracut/modules.d/99blog/
%dir %{_unitdir}/default.target.wants/
%dir %{_unitdir}/emergency.target.wants/
%dir %{_unitdir}/initrd-switch-root.target.wants/
%dir %{_unitdir}/rescue.target.wants/
%dir %{_unitdir}/sysinit.target.wants/
%dir %{_unitdir}/halt.target.wants/
%dir %{_unitdir}/reboot.target.wants/
%dir %{_unitdir}/poweroff.target.wants/
%dir %{_unitdir}/kexec.target.wants/
%dir %{_unitdir}/local-fs-pre.target.wants/
%dir %{_unitdir}/systemd-ask-password-blog.service.wants/
%{_prefix}/lib/dracut/modules.d/99blog/module-setup.sh
%{_unitdir}/blog-halt.service
%{_unitdir}/blog-kexec.service
%{_unitdir}/blog-poweroff.service
%{_unitdir}/blog-quit.service
%{_unitdir}/blog-reboot.service
%{_unitdir}/blog-store-messages.service
%{_unitdir}/blog-switch-initramfs.service
%{_unitdir}/blog-switch-root.service
%{_unitdir}/blog-umount.service
%{_unitdir}/blog.service
%{_unitdir}/systemd-ask-password-blog.path
%{_unitdir}/systemd-ask-password-blog.service
%{_unitdir}/default.target.wants/blog-quit.service
%{_unitdir}/emergency.target.wants/blog-quit.service
%{_unitdir}/halt.target.wants/blog-halt.service
%{_unitdir}/halt.target.wants/blog-switch-initramfs.service
%{_unitdir}/initrd-switch-root.target.wants/blog-switch-root.service
%{_unitdir}/initrd-switch-root.target.wants/blog.service
%{_unitdir}/kexec.target.wants/blog-kexec.service
%{_unitdir}/kexec.target.wants/blog-switch-initramfs.service
%{_unitdir}/local-fs-pre.target.wants/blog-umount.service
%{_unitdir}/poweroff.target.wants/blog-poweroff.service
%{_unitdir}/poweroff.target.wants/blog-switch-initramfs.service
%{_unitdir}/reboot.target.wants/blog-reboot.service
%{_unitdir}/reboot.target.wants/blog-switch-initramfs.service
%{_unitdir}/rescue.target.wants/blog-quit.service
%{_unitdir}/sysinit.target.wants/blog-store-messages.service
%{_unitdir}/sysinit.target.wants/blog.service
%ghost %attr(0644,root,root) %{_unitdir}/systemd-ask-password-blog.service.wants/systemd-vconsole-setup.service

%changelog
