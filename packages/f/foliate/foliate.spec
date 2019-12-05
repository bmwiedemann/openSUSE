#
# spec file for package foliate
#
# Copyright (c) 2019 SUSE LLC
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


%define oname com.github.johnfactotum.Foliate
Name:           foliate
Version:        1.5.3
Release:        0
Summary:        A simple and modern GTK eBook reader
License:        GPL-3.0-only
Group:          Productivity/Office/Other
URL:            https://johnfactotum.github.io/foliate/
Source:         %{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildArch:      noarch

%description
A simple and modern GTK eBook viewer, built with GJS and Epub.js.

%lang_package

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
find {README.md,COPYING} -type f -perm /111 -exec chmod 644 {} \;
find %{buildroot}/%{_datadir}/. -type f -executable -exec chmod -x "{}" \;
for file in %{buildroot}%{_datadir}/%{oname}/assets/KindleUnpack/*; do
   chmod a-x $file
done
pushd %{buildroot}%{_datadir}/%{oname}/assets/KindleUnpack/
sed -i -e '/^#!\//, 1d' *.py
popd
%find_lang %{oname} --with-gnome

%files
%license COPYING
%doc README.md
%{_bindir}/%{oname}
%{_datadir}/applications/
%{_datadir}/%{oname}/
%{_datadir}/glib-2.0/schemas/
%{_datadir}/metainfo/
%{_datadir}/icons/hicolor/

%files lang -f %{oname}.lang

%changelog
