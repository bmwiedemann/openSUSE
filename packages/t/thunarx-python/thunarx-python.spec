#
# spec file for package thunarx-python
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           thunarx-python
Version:        0.5.1
Release:        0
Summary:        Python Bindings for the Thunar Extension Framework
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
Url:            http://goodies.xfce.org/projects/bindings/thunarx-python
Source:         http://archive.xfce.org/src/bindings/%{name}/0.5/%{name}-%{version}.tar.bz2
Patch0:         reproducible.patch
BuildRequires:  fdupes
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig
BuildRequires:  python-devel
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.20.0
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.20.0
BuildRequires:  pkgconfig(thunarx-3)
Requires:       python-gtk
Requires:       thunar
Recommends:     %{name}-doc = %{version}

%description
This package provides the Python bindings for the Thunar Extension framework
which allow one to create Python plugins for Thunar.

%package doc
Summary:        Documentation for thunarx-python
Group:          Documentation/HTML

%description doc
This package provides the documentation files for python thunarx.

%prep
%setup -q
%patch0 -p1

%build
%configure \
    --enable-gtk-doc \
    --docdir=%{_defaultdocdir}/%{name}
make %{?_smp_mflags}

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
