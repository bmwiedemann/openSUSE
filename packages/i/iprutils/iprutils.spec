#
# spec file for package iprutils
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define revision 1
Name:           iprutils
# NOTE: package's changelog is hidden in % changelog section
# in file iprutils/spec/iprutils.spec
Version:        2.4.18
Release:        0
Summary:        Utilities for the IBM Power Linux RAID Adapters
License:        CPL-1.0
Group:          Hardware/Other
Url:            https://sourceforge.net/projects/iprdd
Source0:        https://sourceforge.net/projects/iprdd/files/iprutils%%20for%%202.6%%20kernels/%{version}/%{name}-%{version}.%{revision}.tar.gz
Patch0:         iprutils.fix_ncurses_cflags_var.patch
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(glib-2.0)
ExclusiveArch:  ppc ppc64 ppc64le
%systemd_requires
%if 0%{?suse_version} > 1320
BuildRequires:  pkgconfig(form)
BuildRequires:  pkgconfig(ncurses)
%else
BuildRequires:  ncurses-devel
%endif

%description
Provides a suite of utilities to manage and configure SCSI devices
supported by the ipr SCSI storage device driver.

%prep
%setup -q -n %{name}-%{version}.%{revision}
%patch0 -p1

%build
export CPPFLAGS="$(pkg-config ncurses form --cflags)"
export LIBS="$(pkg-config ncurses form --libs)"
aclocal
automake --add-missing
autoreconf
%configure --sbindir=%{_sbindir} --libdir=%{_libdir} --disable-static
make %{?_smp_mflags}

%install
%make_install
ln -s service %{buildroot}%{_sbindir}/rciprdump
ln -s service %{buildroot}%{_sbindir}/rciprinit
ln -s service %{buildroot}%{_sbindir}/rciprupdate

%pre
%service_add_pre iprdump.service
%service_add_pre iprinit.service
%service_add_pre iprupdate.service

%post
%service_add_post iprdump.service
%service_add_post iprinit.service
%service_add_post iprupdate.service

%preun
%service_del_preun iprdump.service
%service_del_preun iprinit.service
%service_del_preun iprupdate.service

%postun
%service_del_postun iprdump.service
%service_del_postun iprinit.service
%service_del_postun iprupdate.service

%files
%license LICENSE
%doc README
%{_sbindir}/iprconfig
%{_sbindir}/iprdump
%{_sbindir}/iprupdate
%{_sbindir}/iprinit
%{_sbindir}/iprdbg
%{_sbindir}/iprsos
%{_mandir}/man8/*
%{_sysconfdir}/ha.d
%{_sysconfdir}/ha.d/resource.d
%{_sysconfdir}/ha.d/resource.d/iprha
%{_sysconfdir}/bash_completion.d/*
%{_unitdir}/*
%{_sbindir}/rciprdump
%{_sbindir}/rciprinit
%{_sbindir}/rciprupdate
%{_udevrulesdir}/*

%changelog
