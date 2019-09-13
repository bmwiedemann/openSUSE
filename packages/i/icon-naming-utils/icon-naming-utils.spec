#
# spec file for package icon-naming-utils
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


Name:           icon-naming-utils
Version:        0.8.90
Release:        0
Summary:        Icon Name Specification Mapping Script
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            http://tango-project.org/Standard_Icon_Naming_Specification
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  perl-XML-Simple
Requires:       perl-XML-Simple
Provides:       %{name}-devel = %{version}-%{release}
BuildArch:      noarch

%description
A script for creating a symlink mapping for deprecated icon names to
the new icon naming specification names for desktop icon themes.

%prep
%setup -q

%build
%configure\
	--libexecdir=%{_prefix}/lib/icon-naming-utils
make %{?_smp_mflags}

%install
%make_install

%files
%doc AUTHORS ChangeLog NEWS README
%{_prefix}/lib/icon-naming-utils
%{_datadir}/dtds
%{_datadir}/icon-naming-utils
%{_datadir}/pkgconfig/*.pc

%changelog
