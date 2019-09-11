#
# spec file for package unclutter
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Url:            http://www.ibiblio.org/pub/X11/contrib/utilities/

Name:           unclutter
BuildRequires:  imake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Version:        8
Release:        0
Provides:       unclutt = %{version}
Obsoletes:      unclutt < %{version}
Summary:        Remove the idle cursor image from the screen
License:        SUSE-Public-Domain
Group:          System/X11/Utilities
Source:         %{name}-%{version}.tar.bz2
Patch:          %{name}-%{version}-return.diff
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Unclutterer removes the cursor image from the screen so that it does
not obstruct the area you are looking at after it has not moved for a
given period of time.



Authors:
--------
    Mark M Martin <mmm@cetia.fr>
    Andreas Stolcke <stolcke@ICSI.Berkeley.EDU>

%prep
%setup -q
%patch

%build
xmkmf
make

%install
make install DESTDIR=${RPM_BUILD_ROOT}
make install.man DESTDIR=${RPM_BUILD_ROOT}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc README
%{_bindir}/*
%doc %{_mandir}/*/*

%changelog
