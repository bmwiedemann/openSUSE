#
# spec file for package xfce4-icon-theme
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


Name:           xfce4-icon-theme
Version:        4.4.3
Release:        0
Summary:        Default Icon Theme for the Xfce Desktop Environment
License:        GPL-2.0+
Group:          System/GUI/XFCE
Url:            http://www.xfce.org/
Source:         http://archive.xfce.org/src/art/xfce4-icon-theme/4.4/%{name}-%{version}.tar.bz2
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains the default icon theme for Xfce desktop environment.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

# remove /usr/lib/pkgconfig/xfce4-icon-theme-1.0.pc
rm -rf %{buildroot}%{_libdir}

%icon_theme_cache_create_ghost Rodent

%fdupes %{buildroot}%{_datadir}/icons/Rodent

%clean
rm -rf %{buildroot}

%post
%icon_theme_cache_post Rodent

%files
%defattr(-,root,root)
%doc README ChangeLog INSTALL COPYING AUTHORS
%ghost %{_datadir}/icons/Rodent/icon-theme.cache
%{_datadir}/icons/Rodent
%dir %{_datadir}/xfce4
%dir %{_datadir}/xfce4/mime
%{_datadir}/xfce4/mime/Rodent.mime.xml

%changelog
