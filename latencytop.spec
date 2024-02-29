#
# spec file for package latencytop
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           latencytop
Version:        0.5
Release:        0
Summary:        Kernel latency measuring tool
License:        GPL-2.0
Group:          System/Monitoring
Url:            http://www.latencytop.org/
Source:         latencytop-%{version}.tar.bz2
Patch0:         latencytop-warning-fixes.diff
Patch1:         latencytop-incremental-output.patch
Patch2:         latencytop-incremental-man.patch
BuildRequires:  gtk2-devel
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig

%description
LatencyTOP is a Linux* tool for software developers (both kernel and
userspace), aimed at identifying where in the system latency is
happening, and what kind of operation/action is causing the latency to
happen so that the code can be changed to avoid the worst latency
hiccups. A version with graphic interface is available as xlatencytop.

%package -n xlatencytop
Summary:        Kernel latency measuring tool
Group:          System/Monitoring
Requires:       %{name} = %{version}
Conflicts:      %{name} < %{version}-%{release}

%description -n xlatencytop
LatencyTOP is a Linux* tool for software developers (both kernel and
userspace), aimed at identifying where in the system latency is
happening, and what kind of operation/action is causing the latency to
happen so that the code can be changed to avoid the worst latency
hiccups. This package contains version with graphic interface.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p2
%patch -P 2 -p1

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags}
mv latencytop xlatencytop
make %{?_smp_mflags} clean
sed -i 's|HAS_GTK_GUI = 1|#HAS_GTK_GUI = 1|' Makefile
make %{?_smp_mflags}

%install
install -d %{buildroot}%{_sbindir}
%make_install
install -Dpm 0755 xlatencytop \
  %{buildroot}%{_sbindir}/xlatencytop
install -Dpm 0644 latencytop.8 \
  %{buildroot}%{_mandir}/man8/latencytop.8

%files
%{_sbindir}/latencytop
%{_datadir}/latencytop
%{_mandir}/man8/latencytop.8%{ext_man}
%{_datadir}/latencytop

%files -n xlatencytop
%{_sbindir}/xlatencytop

%changelog
