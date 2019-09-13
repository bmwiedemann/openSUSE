#
# spec file for package poppler-data
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


Name:           poppler-data
Version:        0.4.9
Release:        0
Summary:        Encoding Files for use with libpoppler
License:        BSD-3-Clause AND GPL-2.0-only
Group:          System/Libraries
Url:            https://poppler.freedesktop.org/
Source:         https://poppler.freedesktop.org/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildArch:      noarch

%description
This package consists of encoding files for use with poppler. The
encoding files are optional and poppler will automatically read them if
they are present. When installed, the encoding files enables poppler
to correctly render CJK and Cyrrilic properly.

%prep
%setup -q

%build
make %{?_smp_mflags} prefix=%{_prefix}

%install
%make_install prefix=%{_prefix}

%files
%license COPYING COPYING.adobe COPYING.gpl2
%doc README
%{_datadir}/poppler
%{_datadir}/pkgconfig/poppler-data.pc

%changelog
