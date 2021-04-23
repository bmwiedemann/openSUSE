#
# spec file for package scim-tomoe
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           scim-tomoe
Version:        0.6.0
Release:        0
Summary:        Tomoe Input Method Engine for SCIM
License:        GPL-2.0+
Group:          System/I18n/Japanese
Url:            http://sourceforge.net/projects/tomoe/
Source:         http://jaist.dl.sourceforge.net/project/tomoe/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz 
Patch3:         missing-includes.patch
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  gucharmap-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  scim-devel
BuildRequires:  tomoe-devel
BuildRequires:  tomoe-gtk-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Tomoe Input Method Engine for SCIM

%prep
%setup -q
%patch3 -p1

%build
autoreconf -fiv
CXXFLAGS="%{optflags}"
%configure \
    --disable-static \
    --enable-debug
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -name "*.la" -delete -print
%find_lang %{name}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README TODO ChangeLog
%{_bindir}/scim-tomoe
%{_scim_helperdir}/tomoe*
%{_scim_icondir}/scim-tomoe.png

%changelog
