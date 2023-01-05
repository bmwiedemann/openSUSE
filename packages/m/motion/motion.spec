#
# spec file for package motion
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


%define spooldir /var/spool/motion

Name:           motion
Version:        4.5.1
Release:        0
Summary:        A motion detection system
License:        GPL-2.0-or-later
Group:          Hardware/Camera
URL:            https://motion-project.github.io/
Source0:        https://github.com/Motion-Project/motion/archive/release-%{version}.tar.gz
Source1:        motion-service
Source2:        motion-sysconfig
Patch0:         harden_motion.service.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libmicrohttpd)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(sqlite3)
%{?systemd_requires}
BuildRequires:  group(video)
Requires(pre):  group(video)
Requires(pre):  pwdutils
Requires(pre):  %fillup_prereq

%description
Motion is a software motion detector. It grabs images from video4linux devices
and/or from webcams (such as the axis network cameras). Motion is the perfect
tool for keeping an eye on your property keeping only those images that are
interesting. Motion is strictly command line driven and can run as a daemon
with a rather small footprint. This version is built with ffmpeg support but
without MySQL and PostgreSQL support.

%prep
%setup -q -n motion-release-%version
%patch0 -p1

%build
autoreconf -i -f
%configure \
  --without-optimizecpu \
  --without-mariadb \
  --without-mysql \
  --without-pgsql
%make_build

%install
%make_install

# We keep the main configuration file
mv %{buildroot}%{_sysconfdir}/%{name}/motion-dist.conf %{buildroot}%{_sysconfdir}/%{name}/motion.conf
rm %{buildroot}%{_sysconfdir}/%{name}/camera*-dist.conf

install -m 0644 -D -t %{buildroot}%{_datadir}/%{name}/examples data/*.{conf,service}

#We change the PID file path to match the one in the startup script
sed -i 's|/var/run/motion/motion.pid|/var/run/motion.pid|g' %{buildroot}%{_sysconfdir}/%{name}/motion.conf
#We remove SQL directives in the configuration file, as we don't use them
sed -i 's|sql_log_image|; sql_log_image|g' %{buildroot}%{_sysconfdir}/%{name}/motion.conf
sed -i 's|sql_log_snapshot|; sql_log_snapshot|g' %{buildroot}%{_sysconfdir}/%{name}/motion.conf
sed -i 's|sql_log_mpeg|; sql_log_mpeg|g' %{buildroot}%{_sysconfdir}/%{name}/motion.conf
sed -i 's|sql_log_timelapse|; sql_log_timelapse|g' %{buildroot}%{_sysconfdir}/%{name}/motion.conf
sed -i 's|sql_query|; sql_query|g' %{buildroot}%{_sysconfdir}/%{name}/motion.conf
sed -i 's|target_dir /usr/local/apache2/htdocs/cam1|target_dir %{spooldir}|g' %{buildroot}%{_sysconfdir}/%{name}/motion.conf

mkdir -p %{buildroot}%{_unitdir}
install -c -m 0644 %{SOURCE1}  %{buildroot}%{_unitdir}/motion.service
mkdir -p %{buildroot}%{_fillupdir}
cp %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.%{name}

mkdir -p %{buildroot}%{_sbindir}
ln -s service %{buildroot}%{_sbindir}/rcmotion

mkdir -p %{buildroot}/%{spooldir}

rm -rf %{buildroot}/usr/share/doc/motion/

rm -rf %{buildroot}/usr/share/locale

%post
%service_add_post motion.service
%fillup_only

%postun
%service_del_postun motion.service

%pre
getent group motion || groupadd --system motion
getent passwd motion || useradd -g motion -G video -c "Motion capture daemon" -d %{spooldir} --system motion
%service_add_pre motion.service

%preun
%service_del_preun motion.service

%files
%doc doc/CHANGELOG doc/CREDITS README.md doc/*.png doc/*.html doc/*.jpg
%license LICENSE
%dir %{_sysconfdir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/examples
%attr(0770,root,motion) %dir %{spooldir}
%attr(0644,root,root) %{_datadir}/%{name}/examples/motion-dist.conf
%attr(0644,root,root) %{_datadir}/%{name}/examples/motion.service
%attr(0644,root,root) %{_datadir}/%{name}/examples/camera*-dist.conf
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/motion.conf
%attr(0755,root,root) %{_bindir}/motion
%attr(0644,root,root) %{_mandir}/man1/motion.1*
%config %{_unitdir}/motion.service
%{_fillupdir}/sysconfig.%{name}
%{_sbindir}/rcmotion

%changelog
