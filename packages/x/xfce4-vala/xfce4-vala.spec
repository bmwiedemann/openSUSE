#
# spec file for package xfce4-vala
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_with git
Name:           xfce4-vala
Version:        4.10.3
Release:        0
Summary:        Vala Bindings to Xfce Libraries
License:        LGPL-2.1+
Group:          Development/Libraries/Other
Url:            https://wiki.xfce.org/vala-bindings
Source:         https://archive.xfce.org/src/bindings/xfce4-vala/4.10/%{name}-%{version}.tar.bz2
Source100:      %{name}-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  libvala-devel
BuildRequires:  vala
BuildRequires:  pkgconfig(exo-2)
BuildRequires:  pkgconfig(libxfce4panel-2.0)
BuildRequires:  pkgconfig(libxfce4ui-2)
BuildRequires:  pkgconfig(libxfce4util-1.0)
BuildRequires:  pkgconfig(libxfconf-0)
BuildRequires:  pkgconfig(garcon-1)

%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
Requires:       vala
BuildArch:      noarch

%description
This package provides Vala bindings to Xfce Libraries.

%prep
%setup -q

%build
%global vala_version %{?libvala_version}%{!?libvala_version:%(rpm -q --provides $(rpm -q --whatprovides libvala-devel) | grep -o "pkgconfig(libvala-.*)" | sed -e "s|pkgconfig(libvala-||" -e "s|)||g")}
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-maintainer-mode \
    --with-vala-api=%{vala_version}
%else
%configure \
    --with-vala-api=%{vala_version}
%endif
%make_build

%install
%make_install

%fdupes %{buildroot}/usr/share/vala-%{vala_version}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_datadir}/pkgconfig/xfce4-vala.pc
%dir %{_datadir}/vala-%{vala_version}
%dir %{_datadir}/vala-%{vala_version}/vapi
%{_datadir}/vala-%{vala_version}/vapi/*.deps
%{_datadir}/vala-%{vala_version}/vapi/*.vapi

%changelog
