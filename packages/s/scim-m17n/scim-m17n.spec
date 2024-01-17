#
# spec file for package scim-m17n
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


Name:           scim-m17n
Version:        0.2.3
Release:        0
Summary:        M17N Input Method Engine for SCIM
License:        GPL-2.0+
Group:          System/I18n/Chinese
Url:            http://sourceforge.net/projects/scim
Source:         http://hivelocity.dl.sourceforge.net/project/scim/scim-m17n/0.2.3/scim-m17n-0.2.3.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libotf-devel
BuildRequires:  libtool
BuildRequires:  m17n-lib-devel
BuildRequires:  pkg-config
BuildRequires:  scim-devel
BuildRequires:  wordcut-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
M17N Input Method Engine for SCIM

Supports all input methods offered by m17n-lib and m17n-db.

Currently the following languages are supported:

Amharic, Arabic, Armenian, Assamese, Bengali, Chinese, Croatian,
Devanagari, Dhivehi, Farsi, Georgian Greek, Gujarati, Hebrew, Japanese,
Kannada, Kazakh, Khmer, Korean, Lao, Malayalam, Myanmar, Oriya,
Punjabi, Russian, Serbian, Sinhala, Slovak, Syriac, Tamil, Telugu,
Thai, Tibetan, Vietnamese

Several generic input methods for languages based on the Latin alphabet
are also included.

%prep
%setup -q

%build
libtoolize --force
autoreconf --force --install --verbose
CXXFLAGS="%{optflags}" \
%configure  --enable-debug \
            --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -name "*.la" -delete -print

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING README
%{_scim_enginedir}/m17n.so
%{_scim_icondir}/scim-m17n.png

%changelog
