#
# spec file for package gputils
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define ver 1.5.0
%define version %{ver}
%define src_ver %{ver}-1

Name:           gputils
Version:        %{version}
Release:        0
Summary:        Development utilities for Microchip PIC microcontrollers
License:        GPL-2.0+
Group:          Development/Tools/Other
Url:            http://gputils.sourceforge.net
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{src_ver}.tar.bz2
# PATCH-FIX-OPENSUSE gputils-no-build-time.patch -- fix W: file-contains-current-date
Patch1:         gputils-no-build-time.patch
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
%setup -q
%patch1 -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%fdupes %{buildroot}

# documentation
install -d %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/doc/%{name}-%{ver}/html %{buildroot}%{_docdir}/%{name}
rm -r %{buildroot}%{_datadir}/doc/%{name}-%{ver}
install -Dm 644 doc/gputils.pdf %{buildroot}%{_docdir}/%{name}

%files
%defattr(-,root,root)
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
%doc AUTHORS COPYING ChangeLog NEWS README
%exclude %{_docdir}/%{name}/html/
%exclude %{_docdir}/%{name}/gputils.pdf

%if 0%{?suse_version} >= 1200
%files doc
%defattr(-,root,root)
%{_docdir}/%{name}/html/
%{_docdir}/%{name}/gputils.pdf
%endif

%changelog
