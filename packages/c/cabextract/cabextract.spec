#
# spec file for package cabextract
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


Name:           cabextract
Version:        1.10
Release:        0
Summary:        A Program to Extract Microsoft Cabinet Files
License:        GPL-3.0-or-later
Group:          System/Console
URL:            https://www.cabextract.org.uk/
Source:         https://www.cabextract.org.uk/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libmspack) >= 0.8

%description
Cabinet (.CAB) files are a form of archive, which Microsoft uses to
distribute their software and things like Windows Font Packs.
cabextract can be used to unpack these files.

%prep
%autosetup

%build
%configure \
  --with-external-libmspack
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc AUTHORS README
%{_bindir}/cabextract
%{_mandir}/man1/cabextract.1%{?ext_man}

%changelog
