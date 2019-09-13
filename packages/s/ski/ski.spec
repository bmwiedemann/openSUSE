#
# spec file for package ski
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ski
Version:        6.11
Release:        0
Summary:        Skiing simulation with curses interface in python
License:        BSD-3-Clause
Group:          Amusements/Games/Action/Race
Url:            http://catb.org/~esr/ski/
Source0:        http://www.catb.org/~esr/%{name}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM - ski-ski.desktop.patch -- Adjust to Desktop Menu Specification
Patch0:         %{name}-%{name}.desktop.patch
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
Requires:       python3
Requires:       python3-curses
Requires:       python3-pygame
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Imagine you are skiing down an infinite slope, facing such hazards as
trees, ice, bare ground, and the man-eating Yeti! Unfortunately,
you have put your jet-powered skis on backwards, so you can't see
ahead where you are going; only behind where you have been. However,
you can turn to either side, jump or hop through the air, teleport
through hyperspace, launch nuclear ICBMs, and cast spells to call the
Fire Demon.  And since the hazards occur in patches, you can skillfully
outmaneuver them. A fun and very silly game that proves you don't need
fancy graphical user interfaces to have a good time.

%prep
%setup -q
%patch0

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
%make_install

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
%endif

%files
%defattr(-,root,root,-)
%doc COPYING NEWS README
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6%{ext_man}
%{_datadir}/appdata/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
