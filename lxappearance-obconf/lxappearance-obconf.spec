#
# spec file for package lxappearance-obconf
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           lxappearance-obconf
Version:        0.2.3
Release:        0
Summary:        Lxappearance Plugin to Configure Openbox
License:        GPL-2.0
Group:          System/GUI/LXDE
Url:            http://www.lxde.org/
Source:         %{name}-%{version}.tar.xz
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(lxappearance)
BuildRequires:  pkgconfig(obrender-3.5)
BuildRequires:  pkgconfig(obt-3.5)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(sm)
Requires:       lxappearance
Requires:       openbox
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%lang_package

%description
ObConf is a program used to configure OpenBox window manager developed
by Dana Jansens, Tim Riley, and Javeed Shaikh. LXAppearance is a tool
used to configure look and feels of the desktop written by Hong Jen Yee
for LXDE project. This plugin is derived from ObConf as an attempt to
integrate obconf with LXAppearance to provide a better user experience.
Most of the source code are taken from ObConf written by its authors
with some modifications added by LXAppearance developers to make it a
plugin.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} V=1

%install
%make_install
rm %{buildroot}/%{_libdir}/lxappearance/plugins/*.{a,la}
%find_lang %{name}

%files
%defattr(-,root,root)
%doc AUTHORS CHANGELOG COPYING README
%{_libdir}/lxappearance/plugins
%dir %{_datadir}/lxappearance/obconf
%{_datadir}/lxappearance/obconf/obconf.glade

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
