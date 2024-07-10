#
# spec file for package gputils
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


Name:           gputils
Version:        1.5.2
Release:        0
Summary:        Development utilities for Microchip PIC microcontrollers
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            http://gputils.sourceforge.net
Source:         https://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE gputils-no-build-time.patch -- fix W: file-contains-current-date
Patch1:         gputils-no-build-time.patch
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make

%description
This is a collection of development tools for Microchip PIC
microcontrollers.

Gputils implements a subset of features available with Microchip's tools.
See the documentation for an up-to-date list of what gputils can do.

%package        doc
Summary:        Documentation files for PIC MCUs
Group:          Documentation/Other
Requires:       %{name} = %{version}
%if 0%{?suse_version} >= 1140
BuildArch:      noarch
%endif

%description doc
Documentation for gputils and supported PIC MCUs.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%fdupes %{buildroot}

# documentation
install -d %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/%{name}-%{version}/html %{buildroot}%{_docdir}/%{name}
rm -r %{buildroot}%{_datadir}/doc/%{name}-%{version}
install -Dm 644 doc/gputils.pdf %{buildroot}%{_docdir}/%{name}

%files
%{_bindir}/gpasm
%{_bindir}/gpdasm
%{_bindir}/gplib
%{_bindir}/gplink
%{_bindir}/gpstrip
%{_bindir}/gpvc
%{_bindir}/gpvo
%{_mandir}/man1/*
%{_mandir}/fr/man1/*
%{_datadir}/gputils
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%exclude %{_docdir}/%{name}/html/
%exclude %{_docdir}/%{name}/gputils.pdf

%if 0%{?suse_version} >= 1200
%files doc
%{_docdir}/%{name}/html/
%{_docdir}/%{name}/gputils.pdf
%endif

%changelog
