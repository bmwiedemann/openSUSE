#
# spec file for package jp2a
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


%{!?license: %global license %doc}
Name:           jp2a
Version:        1.0.6
Release:        0
Summary:        Converts JPEG images to ASCII
License:        GPL-2.0-only
Group:          Amusements/Toys/Graphics
Url:            https://github.com/cslarsen/jp2a
Source:         https://github.com/cslarsen/jp2a/archive/a72958075f3fb414a5a55d0a02da6789cb972f7b.zip#/%{name}-%{version}.zip
#Source:         https://github.com/cslarsen/jp2a/archive/v%%{version}.tar.gz#/%%{name}-%%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg8-devel
BuildRequires:  unzip

%description
jp2a is a JPEG to ASCII converter.

%prep
%setup -q -n %{name}-a72958075f3fb414a5a55d0a02da6789cb972f7b

%build
autoreconf -vi
%configure --enable-curl
make %{?_smp_mflags}

%install
%make_install

%check
pushd tests
make %{?_smp_mflags} check
popd

%files
%doc ChangeLog README NEWS
%license COPYING
%{_bindir}/jp2a
%{_mandir}/man1/jp2a.1%{?ext_man}

%changelog
