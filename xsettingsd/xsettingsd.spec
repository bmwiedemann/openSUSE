#
# spec file for package xsettingsd
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


Name:           xsettingsd
Version:        0.0+git20171105
Release:        0
Summary:        Provides settings to X11 applications
License:        BSD-3-Clause
Group:          System/X11/Utilities
Url:            https://github.com/derat/xsettingsd
Source:         %{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  scons
BuildRequires:  xz
BuildRequires:  pkgconfig(x11)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
xsettingsd is a daemon that implements the XSETTINGS specification.
It is intended to be small, fast, and minimally dependent on other
libraries. It can serve as an alternative to mate-settings-daemon for users
who are not using the MATE desktop environment but who still run GTK+
applications and want to configure things such as themes, font
antialiasing/hinting, and UI sound effects.

%prep
%setup -q
%if 0%{?suse_version} < 1210
# -Wno-narrowing makes the build to fail.
sed -i 's/ -Wno-narrowing//' SConstruct
%endif

%build
CFLAGS="%{optflags}" CXXFLAGS="%{optflags}" scons %{?_smp_mflags}

%install
for file in %{name} dump_xsettings; do
    install -Dpm 0755 $file %{buildroot}%{_bindir}/$file
    install -Dpm 0644 $file.1 %{buildroot}%{_mandir}/man1/$file.1
done

%files
%defattr (-,root,root)
%doc COPYING README
%{_bindir}/%{name}
%{_bindir}/dump_xsettings
%{_mandir}/man?/%{name}.?%{?ext_man}
%{_mandir}/man?/dump_xsettings.?%{?ext_man}

%changelog
