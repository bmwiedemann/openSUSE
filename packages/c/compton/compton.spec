#
# spec file for package compton
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


%define rev 316eac0613bf342ff91cc645a6c3c80e6b9083fb
Name:           compton
Version:        0.1.0
Release:        0
Summary:        A compositor for X11
License:        MIT
Group:          System/X11/Utilities
URL:            https://github.com/chjj/compton
Source:         https://github.com/chjj/compton/archive/%{rev}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  asciidoc
BuildRequires:  gcc-c++
BuildRequires:  git
# For the /usr/share/icons/hicolor/** directories.
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxslt-tools
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
Requires:       hicolor-icon-theme
Requires(post): desktop-file-utils
Requires(pre):  desktop-file-utils
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif

%description
Compton was forked from Dana Jansens' fork of xcompmgr and refactored.

%prep
%setup -q -n %{name}-%{rev}

%build
# Export the COMPTON_VERSION variable (you may also pass it to make directly)
export COMPTON_VERSION=%{version}-%{release}
export CFLAGS="%{optflags}"
make %{?_smp_mflags}
make %{?_smp_mflags} docs

%install
%make_install
%if 0%{?suse_version}
%suse_update_desktop_file %{name} Utility DesktopUtility
%endif

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-trans
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_mandir}/man1/%{name}-trans.1%{?ext_man}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
