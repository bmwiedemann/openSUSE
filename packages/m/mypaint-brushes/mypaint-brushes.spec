#
# spec file for package mypaint-brushes
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


Name:           mypaint-brushes
Version:        2.0.2 
Release:        0
Summary:        Brushes to be used with the MyPaint library
# According to Licenses.dep5 the files used for building/installing are GPLv2+
# but the shipped brush files are CC0-1.0
License:        CC0-1.0
Group:          Productivity/Graphics/Bitmap Editors
URL:            https://github.com/mypaint
Source0:        https://github.com/mypaint/mypaint-brushes/releases/download/v%{version}/%{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildArch:      noarch

%description
This package contains brush files for use with MyPaint and other programs.

%package devel
Summary:        Files for developing with mypaint-brushes
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
This package contains a pkgconfig file which makes it easier to develop
programs using these brush files.

%prep
%autosetup

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc AUTHORS NEWS README
%dir %{_datadir}/mypaint-data
%dir %{_datadir}/mypaint-data/2.0
%{_datadir}/mypaint-data/2.0/brushes

%files devel
%license COPYING
%{_datadir}/pkgconfig/mypaint-brushes-2.0.pc

%changelog
