#
# spec file for package scim-hangul
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


Name:           scim-hangul
Version:        0.4.0+git20140408.ee1d084
Release:        0
Summary:        Hangul Input Method Engine for SCIM
License:        GPL-2.0+
Group:          System/I18n/Korean
Url:            https://github.com/choehwanjin/scim-hangul
Source:         %{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  libhangul-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libtool
BuildRequires:  scim-devel
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Hangul Input Method Engine for SCIM

%prep
%setup -q -n %{name}-%{version}

%build
touch ChangeLog
autoreconf -fiv
export CXXFLAGS="%{optflags}"
%configure  --disable-static \
            --enable-debug
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -name "*.la" -delete -print
%find_lang %{name}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README
%{_scim_enginedir}/hangul.so
%if 0%{?suse_version} >= 1140
%{_scim_uidir}/hangul-imengine-setup.so
%endif
%{_scim_icondir}/scim-hangul.png
%{_scim_icondir}/scim-hangul-off.png
%{_scim_icondir}/scim-hangul-on.png
%dir %{_scim_datadir}/hangul/
%{_scim_datadir}/hangul/symbol.txt

%changelog
