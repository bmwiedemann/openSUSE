#
# spec file for package thunarx-python
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


Name:           thunarx-python
Version:        0.5.1
Release:        0
Summary:        Python Bindings for the Thunar Extension Framework
License:        GPL-2.0-or-later
URL:            https://goodies.xfce.org/projects/bindings/thunarx-python
Source:         http://archive.xfce.org/src/bindings/%{name}/0.5/%{name}-%{version}.tar.bz2
Patch0:         reproducible.patch
Patch1:         thunarx-python-py3.8.diff
BuildRequires:  fdupes
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.20.0
BuildRequires:  pkgconfig(thunarx-3)
Requires:       thunar
Recommends:     %{name}-doc = %{version}

%description
This package provides the Python bindings for the Thunar Extension framework
which allow one to create Python plugins for Thunar.

%package doc
Summary:        Documentation for thunarx-python

%description doc
This package provides the documentation files for python thunarx.

%prep
%autosetup -p1

%build
# gcc10 workaround
export CFLAGS="%{optflags} -fcommon"
%configure \
    --enable-gtk-doc \
    --docdir=%{_defaultdocdir}/%{name}
%make_build

%install
%make_install
mv %{buildroot}%{_defaultdocdir}/%{name}/README \
    %{buildroot}%{_defaultdocdir}/%{name}/README.examples
rm -f %{buildroot}%{_libdir}/thunarx-python/thunarx.la \
    %{buildroot}%{_libdir}/thunarx-3/thunarx-python.la

%files
%dir %{_libdir}/thunarx-3/
%{_libdir}/thunarx-3/thunarx-python.so

%files doc
%doc %{_defaultdocdir}/%{name}
%doc %{_datadir}/gtk-doc/html/thunarx-python/

%changelog
