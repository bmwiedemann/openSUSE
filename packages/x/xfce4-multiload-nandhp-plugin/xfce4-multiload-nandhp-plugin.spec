#
# spec file for package xfce4-multiload-nandhp-plugin
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


%define git_version 0-3
%define plugin multiload-nandhp
Name:           xfce4-%{plugin}-plugin
Version:        0.3
Release:        0
Summary:        System Load Monitor for the Xfce Panel
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
Url:            https://github.com/nandhp/multiload-nandhp
Source0:        https://github.com/nandhp/multiload-nandhp/archive/version-%{git_version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
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
A system load monitor that graphs processor, memory, and swap space use,
plus network and disk activity.

It is a port of the GNOME multiload applet to the Xfce panel.

%prep
%setup -q -n multiload-nandhp-version-%{git_version}

%build
./autogen.sh
%configure
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/xfce4/panel/plugins/libmultiload.la

%find_lang multiload-nandhp %{?no_lang_C}

%files -f multiload-nandhp.lang
%doc AUTHORS README.md
%license COPYING
%{_libdir}/xfce4/panel/plugins/libmultiload.so
%{_datadir}/xfce4/panel/plugins/multiload.desktop

%changelog
