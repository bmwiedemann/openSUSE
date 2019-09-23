#
# spec file for package bootchart
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define real_version 0.14.8
Name:           bootchart
Version:        2.%{real_version}
Release:        0
Summary:        Boot Process Charting Application
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            https://github.com/mmeeks/bootchart
Source:         https://github.com/xrmx/bootchart/releases/download/%{real_version}/bootchart2-%{real_version}.tar.bz2
Patch0:         bootchart-let-RMP-strip-manpages.patch
# PATCH-FIX-UPSTREAM
Patch1:         include-sys-sysmacros-h.patch
BuildRequires:  fdupes
BuildRequires:  python-devel
BuildRequires:  systemd-rpm-macros
Requires:       lsb-release
Requires:       python-cairo
Requires:       python-gtk
%{?systemd_requires}

%description
bootchart2 instruments your boot process and provides a tool to render
a graph of what was happening during the boot process later.

%prep
%setup -q -n bootchart2-%{real_version}
%patch0 -p1
%patch1 -p1

%build
export EARLY_PREFIX=%{_prefix}
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
export PY_LIBDIR=%{py_libdir}
export PY_SITEDIR=%{py_sitedir}
export EARLY_PREFIX=%{_prefix}
export DOCDIR=%{_docdir}/%{name}
%make_install
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcbootchart2
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcbootchart2-done
%fdupes -s %{buildroot}%{python_sitelib}

%pre
%service_add_pre bootchart2.service bootchart2-done.service bootchart2-done.timer

%post
%service_add_post bootchart2.service bootchart2-done.service bootchart2-done.timer

%preun
%service_del_preun bootchart2.service bootchart2-done.service bootchart2-done.timer

%postun
%service_del_postun bootchart2.service bootchart2-done.service bootchart2-done.timer

%files
%license COPYING
%dir %{_libexecdir}/bootchart
%{_docdir}/*
%{_bindir}/pybootchartgui
%{_libexecdir}/bootchart/tmpfs
%{_libexecdir}/bootchart/bootchart-collector
%{_mandir}/man1/bootchart2.1%{?ext_man}
%{_mandir}/man1/bootchartd.1%{?ext_man}
%{_mandir}/man1/pybootchartgui.1%{?ext_man}
%{_mandir}/man1/%{name}*
%{_sbindir}/bootchartd
%{_sbindir}/rcbootchart2
%{_sbindir}/rcbootchart2-done
%{_unitdir}/bootchart2*.service
%{_unitdir}/bootchart2-done.timer
%config(noreplace) %{_sysconfdir}/bootchartd.conf
%{py_sitedir}/pybootchartgui

%changelog
