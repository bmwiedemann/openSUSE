#
# spec file for package poppler-data
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


Name:           poppler-data
Version:        0.4.12
Release:        0
Summary:        Encoding Files for use with libpoppler
License:        BSD-3-Clause AND GPL-2.0-only AND GPL-3.0-only
Group:          System/Libraries
URL:            https://poppler.freedesktop.org/
Source:         https://poppler.freedesktop.org/%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
This package consists of encoding files for use with poppler. The
encoding files are optional and poppler will automatically read them if
they are present. When installed, the encoding files enables poppler
to correctly render CJK and Cyrrilic properly.

%package        devel
Summary:        Developer files for %{name}
BuildRequires:  pkgconfig
Requires:       %{name} = %{version}-%{release}

%description    devel
This package contains the pkgconfig file for %{name}.

%prep
%setup -q

%build

%install
%make_install prefix=%{_prefix}

%files
%license COPYING*
%doc README
%{_datadir}/poppler

%files devel
%{_datadir}/pkgconfig/poppler-data.pc

%changelog
