#
# spec file for package a2ps-h
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           a2ps-h
Requires:       python
Version:        20010113
Release:        0
Summary:        a2ps Support for Korean PostScript Filter (Python Version)
License:        GPL-2.0-or-later
Source0:        a2ps-h.py
Source1:        a2ps-h-font.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
a2ps support for Korean PostScript filter (Python version).

%prep

%build

%install
mkdir -p %{buildroot}%{_prefix}/bin
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
install -m 755 %{SOURCE0} %{buildroot}%{_prefix}/bin/a2ps-h.py
head -n 18 %{SOURCE0} > %{buildroot}%{_defaultdocdir}/%{name}/Copyright
find %{buildroot}%{_prefix}/bin -name a2ps-h.py -exec patch {} %{SOURCE1} \;

%files
%dir %{_defaultdocdir}/%{name}
%{_defaultdocdir}/%{name}/Copyright
%attr(555, root, root) %{_prefix}/bin/a2ps-h.py

%changelog
