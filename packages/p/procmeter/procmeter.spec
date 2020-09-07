#
# spec file for package procmeter
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


Name:           procmeter
Version:        3.6+svn409
Release:        0
Summary:        Utility to display current system parameters
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://gedanken.org.uk/software/procmeter3
Source:         procmeter3-%{version}.tar.xz
Source1:        procmeter3.desktop
# PATCH-FIX-UPSTREAM procmeter3-loff_t.patch
Patch0:         procmeter3-loff_t.patch
BuildRequires:  libsensors4-devel
BuildRequires:  update-desktop-files
Provides:       procmtr
Obsoletes:      procmtr
%if 0%{?favor_gtk2}
BuildRequires:  gtk2-devel
%else
BuildRequires:  gtk3-devel
%endif
BuildRequires:  libX11-devel
BuildRequires:  libXaw-devel
BuildRequires:  libXt-devel

%description
With procmeter, one can display various system parameters, e.g.
processor load, network load, etc.

%package devel
Summary:        Development files for the procmeter system parameter display program
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
With procmeter, one can display various system parameters, e.g.
processor load, network load, etc.

This package provides files needed to build modules for procmeter.

%prep
%setup -q -n procmeter3-%{version}
%patch0 -p1

%build
make %{?_smp_mflags} INSTDIR=%{_prefix} CFLAGS="%{optflags}"

%install
%make_install INSTDIR=%{_prefix}
%suse_update_desktop_file -i procmeter3 System Monitor

%if 0%{?suse_version} < 1500
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%license COPYING
%doc NEWS README
%{_datadir}/applications/*.desktop
%{_bindir}/*
%{_prefix}/lib/ProcMeter3/
%{_mandir}/man?/*
%exclude %{_prefix}/lib/ProcMeter3/example/

%files devel
%{_includedir}/ProcMeter3/
%{_prefix}/lib/ProcMeter3/example/

%changelog
