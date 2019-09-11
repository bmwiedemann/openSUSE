#
# spec file for package terminology-theme-openSUSE-oliveleaf
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


Name:           terminology-theme-openSUSE-oliveleaf
Version:        20160314
Release:        0
Summary:        openSUSE theme for Terminology
License:        BSD-2-Clause and LGPL-2.1 and CC-BY-SA-3.0
Group:          System/X11/Terminals
Url:            https://en.opensuse.org/Portal:Enlightenment
Source:         %{name}-%{version}.tar.xz
BuildRequires:  ImageMagick
BuildRequires:  edje
Requires:       terminology
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Provides:       terminology-theme

%description
openSUSE theme for Terminology

%prep
%setup -q

%build
./build-darkmod.sh --termpkg
cp terminology/openSUSE-oliveleaf.edj .

cp licenses-authors/* .

%install
install -m 0755 -d %{buildroot}%{_datadir}/terminology/themes
install -m 0644 -t %{buildroot}%{_datadir}/terminology/themes openSUSE-oliveleaf.edj

%files
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_datadir}/terminology

%changelog
