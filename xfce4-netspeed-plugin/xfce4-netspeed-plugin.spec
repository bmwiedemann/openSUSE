#
# spec file for package xfce4-netspeed-plugin
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


%define plugin netspeed
Name:           xfce4-%{plugin}-plugin
Version:        0.3.1
Release:        100
Summary:        Xfce4 Netspeed Plugin
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://code.google.com/p/xfce4-netspeed-plugin/
Source0:        https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/xfce4-netspeed-plugin/%{name}-%{version}.tar.gz
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libgtop-2.0)
BuildRequires:  pkgconfig(libxfce4panel-1.0)
BuildRequires:  pkgconfig(libxfce4ui-1)
# package was renamed in 2019 after Leap 15.1
Provides:       xfce4-panel-plugin-%{plugin} = %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin} < %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin}-debuginfo

%description
An Xfce4 panel plugin that shows the network download/upload speed.

%prep
%setup -qn %{name}

%build
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_libexecdir}/xfce4/panel-plugins/xfce4-netspeed-plugin
%{_datadir}/xfce4/panel-plugins/xfce4-netspeed-plugin.desktop
%{_datadir}/icons/hicolor/*/*/xfce4-netspeed-plugin.*

%changelog
