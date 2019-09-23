#
# spec file for package fwbuilder
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           fwbuilder
Version:        5.3.7
Release:        0
Summary:        Firewall Builder
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
Url:            http://www.fwbuilder.org/
Source:         https://github.com/fwbuilder/fwbuilder/archive/v%{version}.tar.gz
Patch0:         fwbuilder-qmake-without-flags.patch
Patch1:         fix-bsc1124647-segfault.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  hicolor-icon-theme
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  net-snmp-devel
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
Requires:       hicolor-icon-theme
Requires:       rcs
%if 0%{?suse_version}
BuildRequires:  fdupes
Requires(post): update-desktop-files
Requires(postun): update-desktop-files
%endif

%description
Firewall Builder consists of a GUI and set of policy compilers for
various firewall platforms. It helps users maintain a database of
objects and allows policy editing using simple drag-and-drop
operations. The GUI generates a firewall description in the form of an XML
file, which compilers then interpret and generate platform-specific
code. Several algorithms are provided for automated network object
discovery and bulk import of data. The GUI and policy compilers are
independent of another.

%prep
%autosetup -p1
#%%patch1 -p1

%build
NOCONFIGURE=1 ./autogen.sh "--with-qmake=qmake-qt5"
%configure \
    --with-qmake=qmake-qt5 \
    --with-docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install
%if 0%{?suse_version}
%suse_update_desktop_file -r %{name} System Security
%fdupes -s %{buildroot}
%endif

%if 0%{?suse_version} > 1310
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_docdir}/%{name}
%{_datadir}/%{name}-%{version}
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/fwb*

%changelog
