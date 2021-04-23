#
# spec file for package tv-fonts
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           tv-fonts
Version:        1.1
Release:        0
Summary:        Fonts for TV Applications
License:        MIT
Group:          System/X11/Fonts
BuildRequires:  fontpackages-devel
BuildRequires:  freetype2
%if 0%{?suse_version} >= 1220
BuildRequires:  bdftopcf
BuildRequires:  mkfontdir
%else
BuildRequires:  xorg-x11
BuildRequires:  xorg-x11-devel
%endif
%reconfigure_fonts_prereq
Source:         %{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM
Patch0:         reproducible.patch
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package includes some X Window System bitmap fonts for TV
applications:  large fonts frequently used in on-screen displays,
teletext font, and more.

%prep
%setup -q
%patch0 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS"

%install
mkdir -p	%{buildroot}%{_miscfontsdir}
cp -v *.pcf.gz 	%{buildroot}%{_miscfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%{_miscfontsdir}/

%changelog
