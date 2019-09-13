#
# spec file for package scim-chewing
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


Name:           scim-chewing
Version:        0.3.6+git20150821.5df4075
Release:        0
Summary:        Chewing IM engine for SCIM platform
License:        GPL-2.0+
Group:          System/I18n/Chinese
Url:            https://github.com/chewing/scim-chewing
Source:         %{name}-%{version}.tar.xz
Patch:          %{name}-0.3.6-autogen.patch
BuildRequires:  gcc-c++
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libchewing-devel
BuildRequires:  libtool
BuildRequires:  scim-devel
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Chewing IM engine for SCIM platform.

%prep
%setup -q
%patch -p1
NOCONFIGURE=1 ./autogen.sh

%build
CXXFLAGS="%{optflags}" \
%configure \
    --disable-static \
    --enable-debug
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README
%{_scim_enginedir}/chewing.so
%{_scim_uidir}/chewing-imengine-setup.so
%{_scim_icondir}/%{name}.png
%{_scim_icondir}/%{name}-swap-colors.png

%changelog
