#
# spec file for package shared-desktop-ontologies
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           shared-desktop-ontologies
Version:        0.11.0
Release:        0
Summary:        Shared Desktop Ontologies
License:        (CC-BY-SA-3.0 or BSD-3-Clause) and CC-BY-3.0 and W3C
Group:          System/X11/Utilities
Url:            http://oscaf.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/oscaf/%{name}/%{version}/%{name}-%{version}.tar.bz2
BuildRequires:  cmake
BuildRequires:  kde4-filesystem
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Open Semantic Collaboration Architecture Foundation (OSCAF) ontologies
and reference code development. This project is used by maintainers from
open source projects to maintain standards for the interoperability of
desktop and web applications.

%package devel
Summary:        Shared Desktop Ontologies
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Open Semantic Collaboration Architecture Foundation (OSCAF) ontologies
and reference code development. This project is used by maintainers from
open source projects to maintain standards for the interoperability of
desktop and web applications.

%prep
%setup -q

%build
%cmake_kde4 -d build

%install
%kde4_makeinstall -C build

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog LICENSE.* README
%{_datadir}/ontology/

%files devel
%defattr(-,root,root,-)
%{_datadir}/cmake/SharedDesktopOntologies/
%{_datadir}/pkgconfig/shared-desktop-ontologies.pc

%changelog
