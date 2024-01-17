#
# spec file for package pdf2svg
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           pdf2svg
Url:            http://www.cityinthesky.co.uk/opensource/pdf2svg/
Summary:        PDF to SVG Converter
License:        GPL-2.0+
Group:          Productivity/Graphics/Convertors
Version:        0.2.3
Release:        0
Source0:        https://github.com/db9052/pdf2svg/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  cairo-devel
BuildRequires:  gtk2-devel
BuildRequires:  libpoppler-glib-devel

%description
A small tool to convert PDF files into SVG using poppler and cairo.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root,-)
%doc README COPYING AUTHORS ChangeLog LICENSE
%{_bindir}/%{name}

%changelog
