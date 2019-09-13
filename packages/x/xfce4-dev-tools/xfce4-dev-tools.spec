#
# spec file for package xfce4-dev-tools
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


%bcond_with git
Name:           xfce4-dev-tools
Version:        4.14.0
Release:        0
Summary:        Xfce Development Tools
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://www.xfce.org/
Source0:        https://archive.xfce.org/src/xfce/xfce4-dev-tools/4.14/%{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig(glib-2.0)
Requires:       autoconf
Requires:       automake
Requires:       intltool
Requires:       libtool
Requires:       make

%description
The Xfce development tools are a collection of tools and macros for
Xfce developers and people that want to build unreleased development
versions of Xfce.

%prep
%autosetup

%build
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-maintainer-mode
%else
%configure
%endif
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog HACKING NEWS README
%license COPYING
%{_bindir}/xdt-autogen
%{_bindir}/xdt-csource
%dir %{_datadir}/xfce4
%dir %{_datadir}/xfce4/dev-tools
%dir %{_datadir}/xfce4/dev-tools/m4macros
%{_datadir}/xfce4/dev-tools/m4macros/*.m4

%changelog
