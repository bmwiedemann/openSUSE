#
# spec file for package ddccontrol-db
#
# Copyright (c) 2022 SUSE LLC
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


Name:           ddccontrol-db
URL:            https://github.com/ddccontrol/ddccontrol-db
Version:        20220903
Release:        0
Summary:        Monitor database for ddccontrol
License:        GPL-2.0-or-later
Group:          Hardware/Other
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExcludeArch:    s390 s390x
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-tools
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  m4
Recommends:     %{name}-lang = %version

%description
Database of well-known monitors and their DDC/CI controls
used by ddccontrol.


%lang_package

%prep
%setup -q
./autogen.sh

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT prefix=/usr
%find_lang %{name}

%files
%defattr(-,root,root)
%dir %{_datadir}/ddccontrol-db
%dir %{_datadir}/ddccontrol-db/monitor
%{_datadir}/ddccontrol-db/monitor/*
%{_datadir}/ddccontrol-db/options.xml
%doc AUTHORS ChangeLog NEWS README.md
%license COPYING

%files lang -f ddccontrol-db.lang
%defattr(-,root,root)

%changelog
