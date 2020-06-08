#
# spec file for package webalizer
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


%define apache_serverroot %(/usr/sbin/apxs2 -q datadir 2>/dev/null || apxs -q PREFIX)
%define editlvl 08

Name:           webalizer
Summary:        A Web Server Log File Analysis Program
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Utilities
Version:        2.23
Release:        0
URL:            http://www.mrunix.net/webalizer/
Source0:        ftp://ftp.mrunix.net/pub/webalizer/%{name}-%{version}-%{editlvl}-src.tar.bz2
Source1:        flags.tar.bz2
Source2:        flags.license.html
# PATCH-MISSING-TAG -- See http://en.opensuse.org/Packaging/Patches
Patch0:         %{name}-2.21-02.diff
# PATCH-MISSING-TAG -- See http://en.opensuse.org/Packaging/Patches
Patch1:         %{name}-2.21-02-ia64.diff
# PATCH-MISSING-TAG -- See http://en.opensuse.org/Packaging/Patches
Patch3:         %{name}-2.21-02-maxagent.diff
# PATCH-MISSING-TAG -- See http://en.opensuse.org/Packaging/Patches
Patch4:         %{name}-2.23-04-conf.patch
# PATCH-MISSING-TAG -- See http://en.opensuse.org/Packaging/Patches
Patch5:         %{name}-2.21-02-fclose.diff
# FIX-DATADIR - fix for datadir and mandir
Patch6:         %{name}-2.23-04-Makefile.patch
Patch7:         webalizer-overlinking.patch
# static variables
Patch8:         webalizer-static.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  apache2-devel
BuildRequires:  autoconf
BuildRequires:  db-devel
BuildRequires:  gd-devel
BuildRequires:  libapr-util1-devel
BuildRequires:  libbz2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  pcre-devel
Requires:       %{name}-flags

%description
Webalizer is a web server log file analysis program which produces
usage statistics in HTML format for viewing with a browser.  The
results are presented in both columnar and graphical formats, which
facilitates interpretation.  Yearly, monthly, daily, and hourly usage
statistics are presented, along with the ability to display usage by
site, URL, referrer, user agent (browser) and country (user agent and
referrer are only available if your web server produces Combined log
format files).

Webalizer supports CLF (common log format) log files, as well as
Combined log formats as defined by NCSA and others, and variations of
these which it attempts to handle intelligently.

%package flags
Summary:        Flags of the World
License:        CC-BY-SA-3.0
Group:          Productivity/Networking/Web/Utilities
URL:            http://flags.blogpotato.de/
BuildArch:      noarch

%description flags
Images for those who want to visualize the data returned by an
IP-to-Country database (e.g. the one provided by Directi) with
corresponding flags. Flags provided are based on the iso3166
countrycode, that means there are currently 243 flags offered in the
world set.

%prep
%setup -q -n %{name}-%{version}-%{editlvl} -a 1
%patch0
%patch1
%patch3
%patch4
%patch5
%patch6
%patch7
%patch8 -p1
%{__cp} -a %{S:2} .

%build
autoconf
CFLAGS="%{optflags} -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64" ./configure \
  --prefix=%{_prefix} \
  --mandir=%{_mandir} \
  --sysconfdir=%{_sysconfdir} \
  --enable-bz2 \
  --enable-geoip \
  --with-gdlib=%{_libdir} \
  --with-gd=/usr/include/gd \
  %{_target_cpu}-suse-linux
make LIBNAME=%{_lib}

%install
install -d -m 755 %{buildroot}%{_prefix}/bin
install -d -m 755 %{buildroot}/etc
install -d -m 755 %{buildroot}/%{_mandir}/man1
make "DESTDIR=%{buildroot}" install
install -d -m 755 %{buildroot}%{apache_serverroot}/htdocs/%{name}
install -d -m 755 %{buildroot}%{_localstatedir}/lib/%{name}
mv %{buildroot}/%{_sysconfdir}/%{name}.conf.sample %{buildroot}/%{_sysconfdir}/%{name}.conf

#install flags
%{__cp} -a flags %{buildroot}%{apache_serverroot}/htdocs/%{name}/

%preun
#rm -f var/lib/%{name}/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES COPYING Copyright README README.FIRST country-codes.txt
%doc %{_mandir}/man?/*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%dir %{apache_serverroot}/htdocs/%{name}
%exclude %{apache_serverroot}/htdocs/%{name}/flags
%{_bindir}/*
%{_localstatedir}/lib/%{name}

%files flags
%defattr(-,root,root)
%doc flags.license.html
%dir %{apache_serverroot}/htdocs/%{name}/flags
%{apache_serverroot}/htdocs/%{name}/flags/*

%changelog
