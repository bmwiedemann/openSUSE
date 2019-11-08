#
# spec file for package scim-canna
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


Name:           scim-canna
Version:        1.0.1
Release:        0
Summary:        Canna Input Method Engine for SCIM
License:        GPL-2.0-or-later
Group:          System/I18n/Japanese
Url:            http://sourceforge.jp/projects/scim-imengine/
Source:         http://iij.dl.sourceforge.jp/scim-imengine/29155/%{name}-%{version}.tar.gz
#PATCH-FIX-UPSTREAM migration old gtk functions: gtktooltips
Patch1:         gtk-2.12+-gtktooltips-migration.patch
#PATCH-FIX-UPSTREAM convert old gtk_combo to new gtk_combobox
Patch2:         gtk-2.4+-combobox-migration.patch
BuildRequires:  canna-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  scim-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Canna Input Method Engine for SCIM

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
autoreconf -fiv
CXXFLAGS="%{optflags}"
%configure \
    --disable-static \
    --enable-debug
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -name "*.la" -delete -print
%find_lang %{name}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README ChangeLog
%{_scim_enginedir}/canna.so
%if 0%{?suse_version} >= 1140
%{_scim_uidir}/canna-imengine-setup.so
%endif
%{_scim_icondir}/%{name}.png

%changelog
