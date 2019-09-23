#
# spec file for package scim-anthy
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           scim-anthy
Version:        1.3.2
Release:        0
Summary:        Anthy Input Method Engine for SCIM
License:        LGPL-2.1+
Group:          System/I18n/Japanese
Url:            https://github.com/scim-im/scim-anthy
Source:         https://github.com/scim-im/scim-anthy/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  anthy-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  scim-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Anthy Input Method Engine for SCIM

%prep
%setup -q

%build
libtoolize --force
autoreconf --force --install --verbose
%configure \
    --disable-static \
    --enable-debug
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README ChangeLog
%{_scim_enginedir}/anthy.so
%if 0%{?suse_version} >= 1140
%{_scim_uidir}/anthy-imengine-setup.so
%{_scim_helperdir}/anthy-imengine-helper.so
%endif
%{_scim_datadir}/Anthy/
%{_scim_icondir}/*.png

%changelog
