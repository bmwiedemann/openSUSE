#
# spec file for package h5utils
#
# Copyright (c) 2023 SUSE LLC
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


Name:           h5utils
Version:        1.13.2
Release:        0
Summary:        Utilities for Data Conversions from hdf5
License:        GPL-2.0-or-later AND MIT
Group:          Productivity/Scientific/Electronics
URL:            https://github.com/stevengj/h5utils
Source0:        https://github.com/stevengj/h5utils/releases/download/%{version}/h5utils-%{version}.tar.gz
BuildRequires:  hdf5-devel
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig(gsl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)
Requires:       meep

%description
h5utils is a set of utilities for visualization and conversion of
scientific data in the HDF5 format.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog
%{_bindir}/h5fromtxt
%{_bindir}/h5topng
%{_bindir}/h5totxt
%{_bindir}/h5tovtk
%{_mandir}/man1/h5fromtxt.1%{ext_man}
%{_mandir}/man1/h5topng.1%{ext_man}
%{_mandir}/man1/h5totxt.1%{ext_man}
%{_mandir}/man1/h5tovtk.1%{ext_man}
%{_datadir}/h5utils/

%changelog
