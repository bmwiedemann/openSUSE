#
# spec file for package bodr
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           bodr
Version:        10
Release:        0
Summary:        Blue Obelisk Data Repository
License:        CC0-1.0
Group:          System/Libraries
Url:            https://blueobelisk.github.io/datarepository.html
Source0:        https://github.com/BlueObelisk/bodr/archive/BODR-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildArch:      noarch

%description
The Blue Obelisk Data Repository lists many important chemoinformatics data
such as element and isotope properties, atomic radii, etc. including
references to original literature. Developers can use this repository to make
their software interoperable.


%prep
%setup -q -n bodr-BODR-%{version}/bodr

%build
autoreconf -iv
%configure
%make_build

%install
%make_install docdir=%{_defaultdocdir}/bodr
rm %{buildroot}/%{_defaultdocdir}/bodr/COPYING

%files
%license COPYING
%doc %{_defaultdocdir}/%{name}
%{_datadir}/bodr
%{_datadir}/pkgconfig/bodr.pc

%changelog

