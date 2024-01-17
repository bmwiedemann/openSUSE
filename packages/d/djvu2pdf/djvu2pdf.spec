#
# spec file for package djvu2pdf

# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           djvu2pdf 
Version:        0.9.2
Release:        1
License:        GPL-2.0+ or LGPL-2.0+
Summary:        Converting Djvu Files to PDF Files
Url:            http://0x2a.at/s/projects/djvu2pdf
Group:          Productivity/Graphics/Other
Source:         http://0x2a.at/site/projects/djvu2pdf/%{name}-%{version}.tar.gz

Requires:       djvulibre
Requires:       ghostscript-library

BuildArch:	noarch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A small tool to convert Djvu files to PDF files. Works on Linux, BSD and MacOS.

%prep
%setup -q

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install %{name} $RPM_BUILD_ROOT%{_bindir}
install -m 0644 %{name}.1.gz $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc changelog copyright
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.gz

%changelog

