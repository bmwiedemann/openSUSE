#
# spec file for package nvdock
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


Name:           nvdock
Version:        1.02
Release:        0
Summary:        Tray icon for launching NVIDIA Settings
License:        BSD-3-Clause
Group:          System/X11/Utilities
URL:            https://www.opsat.net/development/nvdock/
Source0:        http://bobmajdakjr.googlecode.com/files/%{name}-%{version}.tar.bz2
# The provided Makefile sucks, so I did this one. -- adam@mizerski.pl
Source1:        Makefile
Source2:        %{name}.desktop
# PATCH-FEATURE-OPENSUSE nvdock-1.02-datadir.patch.in adam@mizerski.pl - allow custom datadir
Source3:        %{name}-1.02-datadir.patch.in
# PATCH-FIX-UPSTREAM nvdock-1.02-argptr.patch adam@mizerski.pl - Get rid of "warning: cast to pointer from integer of different size"
Patch0:         %{name}-1.02-argptr.patch
Patch1:         %{name}-fix-gcc10-build.patch
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gtk+-2.0)

%description
Little NVIDIA tray icon.
Hover over it and it will tell you your GPU temperature if your card is into that kind of thing.
A double click will launch the NVIDIA settings control panel, and right click will bring up a nifty menu with a few options.
Also on the menu it will show the NVIDIA driver version, which is surely to come in handy at least one time in your life.

%prep
%setup -q
sed -e "s|@DATADIR@|%{_datadir}|g" < %{SOURCE3} | patch -p1
%autopatch -p1

%build
make -C src -f %{SOURCE1} %{?_smp_mflags}

%install
install -m 755 -D src/nvdock %{buildroot}%{_bindir}/nvdock
install -m 644 -D data/nvdock.png %{buildroot}%{_datadir}/pixmaps/nvdock.png
install -m 644 -D %{SOURCE2} %{buildroot}%{_datadir}/applications/nvdock.desktop
%suse_update_desktop_file nvdock

# Compatibility cruft
# there is no %%license prior to SLE12
%if %{undefined _defaultlicensedir}
%define license %doc
%else
# filesystem before SLE12 SP3 lacks /usr/share/licenses
%if 0%(test ! -d %{_defaultlicensedir} && echo 1)
%define _defaultlicensedir %{_defaultdocdir}
%endif
%endif
# End of compatibility cruft

%files
%{_bindir}/nvdock
%{_datadir}/pixmaps/nvdock.png
%{_datadir}/applications/nvdock.desktop
%license COPYING
%doc ChangeLog README TODO

%changelog
