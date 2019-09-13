#
# spec file for package scim-skk
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


Name:           scim-skk
Version:        0.5.2
Release:        0
Summary:        SKK Input Method Engine for SCIM
License:        GPL-2.0+
Group:          System/I18n/Japanese
Url:            http://sourceforge.jp/projects/scim-imengine/
Source0:        http://osdn.dl.sourceforge.jp/scim-imengine/15351/scim-skk-0.5.2.tar.bz2
Patch0:         commit-when-focus-out.patch
Patch2:         missing-includes.patch
Patch3:         scim-skk-iter-remove-fix.diff
Patch4:         scim-skk-fix-returns.diff
#PATCH-FOR-UPSTREAM fix builds against latest gtk.
Patch5:         gtk-2.24+-replace-functions.patch
BuildRequires:  anthy-devel
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  scim-devel
BuildRequires:  update-desktop-files
Requires:       skkdic
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SKK Input Method Engine for SCIM

%prep
%setup -q
%patch0 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
CXXFLAGS="%{optflags}" \
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
%doc AUTHORS COPYING NEWS README* ChangeLog TODO
%{_scim_enginedir}/skk.so
%if 0%{?suse_version} >= 1140
%{_scim_uidir}/skk-imengine-setup.so
%endif
%{_scim_icondir}/scim-skk.png

%changelog
