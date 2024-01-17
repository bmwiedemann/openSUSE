#
# spec file for package cldr-emoji-annotation
#
# Copyright (c) 2020 SUSE LLC
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


Name:           cldr-emoji-annotation
Version:        36.12.120191002_0
Release:        0
Summary:        Emoji annotation files in CLDR
License:        LGPL-2.0-or-later AND Unicode
Group:          System/I18n/Chinese
URL:            https://github.com/fujiwarat/cldr-emoji-annotation
Source:         https://github.com/fujiwarat/cldr-emoji-annotation/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains the pkg-config files for development when building
programs that use cldr-annotations.

%package devel
Summary:        Files for development using cldr-annotations
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
This package contains the pkg-config files for development
when building programs that use cldr-annotations.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure

make %{?_smp_mflags}

%install
%make_install

%fdupes %{buildroot}

%files
%doc AUTHORS README unicode-license.txt
%{_datadir}/unicode/

%files devel
%{_datadir}/pkgconfig/%{name}.pc

%changelog
