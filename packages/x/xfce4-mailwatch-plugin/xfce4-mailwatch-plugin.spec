#
# spec file for package xfce4-mailwatch-plugin
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


%define panel_version 4.12.0
%define plugin mailwatch
%bcond_with git
Name:           xfce4-%{plugin}-plugin
Version:        1.2.0
Release:        100
Summary:        Versatile Mail Checking Plugin for the Xfce Panel
License:        GPL-2.0
Group:          System/GUI/XFCE
URL:            https://goodies.xfce.org/projects/panel-plugins/xfce4-mailwatch-plugin
Source0:        https://archive.xfce.org/src/panel-plugins/xfce4-mailwatch-plugin/1.2/%{name}-%{version}.tar.bz2
BuildRequires:  ed
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  libgcrypt-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(exo-1)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libxfce4panel-1.0)
BuildRequires:  pkgconfig(libxfce4ui-1)
BuildRequires:  pkgconfig(libxfce4util-1.0)
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
Recommends:     %{name}-lang = %{version}
Requires:       xfce4-panel >= %{panel_version}
# package was renamed in 2019 after Leap 15.1
Provides:       xfce4-panel-plugin-%{plugin} = %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin} < %{version}-%{release}
Obsoletes:      xfce4-panel-plugin-%{plugin}-debuginfo

%description
The Mailwatch plugin is a multi-protocol, multi-mailbox mail checking tool
which supports a variety of protocols and local mailbox formats. It can check
multiple locations and execute custom actions when it finds new mail.

%package lang
Summary:        Translations for package %{name}
Group:          System/Localization
Requires:       %{name} = %{version}
Supplements:    %{name}
Provides:       %{name}-lang-all = %{version}
# package was renamed in 2019 after Leap 15.1
Obsoletes:      xfce4-panel-plugin-%{plugin}-lang < %{version}-%{release}
Provides:       xfce4-panel-plugin-%{plugin}-lang = %{version}-%{release}
BuildArch:      noarch

%description lang
Provides translations for the "%{name}" package.

%prep
%autosetup
# fix up missing icon
ed -s panel-plugin/mailwatch.desktop.in 2>/dev/null <<'EOF'
,s/^Icon=xfce-mail/Icon=mail-unread/
w
EOF

%build
%configure --disable-static
make %{_smp_mflags} V=1

%install
%make_install

rm %{buildroot}%{_libdir}/xfce4/panel/plugins/libmailwatch.la

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name} %{name}.lang %{?no_lang_C}

%files
%doc AUTHORS NEWS README TODO
%license COPYING
%{_libdir}/xfce4/panel/plugins/libmailwatch.so
%{_datadir}/xfce4/panel/plugins/mailwatch.desktop
%{_datadir}/icons/hicolor/*/apps/*

%files lang -f %{name}.lang

%changelog
