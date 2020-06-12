#
# spec file for package tvheadend
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2016 Packman Team <packman@links2linux.de>
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


%define htsgroup video
%define htsuser hts
%define homedir %{_localstatedir}/lib/tvheadend
Name:           tvheadend
Version:        4.2.8
Release:        0
Summary:        A TV Streaming Server
# parsers are from FFMpeg project under LGPL-2.1
# FFdecsa and extra/capmt_ca.c is GPL-2.0+ which is compatibile with GPL-3.0+
# rest of code seems to be GPL-3.0+
License:        GPL-3.0-or-later AND LGPL-2.1-only
Group:          Productivity/Multimedia/Other
URL:            https://tvheadend.org/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source2:        %{name}-rpmlintrc
Source3:        %{name}_super
# From https://github.com/tvheadend/dtv-scan-tables.git as build system fails to retrieve them
Source4:        dvb-scan-git20190112.tar.gz
# PATCH-FIX-OPENSUSE tvheadend-fix-service-dependency.patch -- do not wait for or require syslog
Patch2:         %{name}-fix-service-dependency.patch
# PATCH-FIX-UPSTREAM -- fix unsufficient configure checks when using LTO (check optimized away)
Patch3:         fix_configure_checks_with_LTO.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  pkgconfig(avahi-client)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavresample)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(liburiparser)
BuildRequires:  pkgconfig(zlib)
Requires(pre):  group(%{htsgroup})
%{?systemd_ordering}

%description
A TV streaming server supporting DVB-S, DVB-S2, DVB-C, DVB-T, ATSC, IPTV,
and Analog video (V4L) as input sources.

It also comes with a web interface both used for configuration and
day-to-day operations, such as searching the electronic program guide
(EPG) and for scheduling recordings.

%prep
%setup -q
%patch2 -p1
%patch3 -p1

sed -e "s/-u \([^ ]*\) -g \([^ ]*\)/-u %{htsuser} -g %{htsgroup}/" -i rpm/%{name}.sysconfig
sed -e '/^TVH_ARGS/cTVH_ARGS="-C"' -i debian/%{name}.default
sed -e '/cmake/d' -i configure
# Disable failing attempt to download from within the build host which has no internet connectivity
sed -e 's@"${ROOTDIR}/support/getmuxlist"@true@g' -i configure
echo %{version} > rpm/version

%build
export CFLAGS_NO_WERROR="yes"
export CFLAGS="%{optflags} -fcommon"
%configure \
  --python=%{_bindir}/python3 \
  --disable-ffmpeg_static \
  --disable-hdhomerun_static
mkdir -p data/dvb-scan
tar -C data/dvb-scan -xvf %{SOURCE4}
touch data/dvb-scan/.stamp
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_fillupdir}/
mkdir -p %{buildroot}%{_sbindir}
install -D -m 644 rpm/%{name}.service %{buildroot}/%{_unitdir}/%{name}.service
sed -i 's@/home/tvheadend@%{homedir}@' rpm/%{name}.sysconfig
install -m 644 rpm/%{name}.sysconfig %{buildroot}/%{_fillupdir}/sysconfig.%{name}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
# Install superuser helper script
sed -i 's@/home/tvheadend@%{homedir}@' %{SOURCE3}
install -Dm0755 %{SOURCE3} %{buildroot}%{_sbindir}/%{name}_super
%fdupes -s %{buildroot}%{_datadir}
chmod -x %{buildroot}%{_mandir}/man1/tvheadend.1

%post
%fillup_only %{name}
%service_add_post %{name}.service
cat << 'EOM'
  ==> IMPORTANT: Post configuration tasks;
  ==> 1. Start the tvheadend service (to create home directory).
  ==> 2. Run tvheadend_super to set default username and password.
  ==> 3. Restart tvheadend service.
  ==>
  ==>
  ==> All further configuration is maintained through the web interface:
  ==>
  ==> http://localhost:9981/
  ==>
EOM

%pre
%service_add_pre %{name}.service
getent passwd %{htsuser} >/dev/null || %{_sbindir}/useradd -g %{htsgroup} -m -d %{homedir} -r -s /bin/false %{htsuser} -c "Tvheadend TV server"

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc CONTRIBUTING.md
%license LICENSE.md
%{_bindir}/tvheadend
%{_datadir}/tvheadend
%{_mandir}/man1/tvheadend.1%{?ext_man}
%{_unitdir}/%{name}.service
%{_fillupdir}/sysconfig.%{name}
%{_sbindir}/%{name}_super
%{_sbindir}/rc%{name}

%changelog
