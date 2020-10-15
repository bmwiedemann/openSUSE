#
# spec file for package foliate
#
# Copyright (c) 2020 SUSE LLC
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


%global __requires_exclude typelib\\(Handy\\) = 1
%define oname com.github.johnfactotum.Foliate
Name:           foliate
Version:        2.5.0
Release:        0
Summary:        A GTK eBook reader
License:        GPL-3.0-only
Group:          Productivity/Office/Other
URL:            https://johnfactotum.github.io/foliate/
Source:         %{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(glib-2.0)
Requires:       typelib(WebKit2)
BuildArch:      noarch

%description
A GTK eBook viewer, built with GJS and Epub.js.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

chmod a-x README.md COPYING
find %{buildroot}/%{_datadir} -type f -executable -exec chmod -x "{}" +

chmod a-x %{buildroot}/%{_datadir}/com.github.johnfactotum.Foliate/assets/KindleUnpack/*

pushd %{buildroot}%{_datadir}/com.github.johnfactotum.Foliate/assets/KindleUnpack/
sed -i -e '/^#!/, 1d' *.py
popd
%fdupes %{buildroot}/%{_datadir}/%{oname}

%find_lang %{oname} --with-gnome

ln -sr %{buildroot}/%{_bindir}/%{oname} %{buildroot}/%{_bindir}/%{name}

%files
%license COPYING
%doc README.md
%{_bindir}/%{oname}
%{_bindir}/%{name}
%{_datadir}/applications/
%{_datadir}/com.github.johnfactotum.Foliate
%{_datadir}/glib-2.0/schemas/
%{_datadir}/metainfo/
%{_datadir}/icons/hicolor/

%files lang -f %{oname}.lang

%changelog
