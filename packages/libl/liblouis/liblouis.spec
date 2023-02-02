#
# spec file for package liblouis
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


%define sover 20
Name:           liblouis
Version:        3.24.0
Release:        0
Summary:        Two-way braille translator
License:        LGPL-3.0-or-later
Group:          Productivity/Other
URL:            http://liblouis.org/
Source0:        https://github.com/liblouis/liblouis/releases/download/v%{version}/liblouis-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  libyaml-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3
Requires:       liblouis%{sover} = %{version}

%description
liblouis is a translator from and to braille. It features support for
computer and literary braille, supports contracted and uncontracted
translation for many languages and has support for hyphenation. New
languages can be added through tables that support a rule- or
dictionary-based approach. Math braille (Nemeth and Marburg) is
supported.

Included are also tools for testing and debugging tables.

%package -n liblouis%{sover}
Summary:        Two-way braille translator
# We used to have a package named liblouis, until 2.4.1.
License:        LGPL-3.0-or-later
Group:          System/Libraries
Requires:       %{name}-data >= %{version}
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n liblouis%{sover}
liblouis is a translator from and to braille. It features support for
computer and literary braille, supports contracted and uncontracted
translation for many languages and has support for hyphenation. New
languages can be added through tables that support a rule- or
dictionary-based approach. Math braille (Nemeth and Marburg) is
supported.

%package data
Summary:        Data files for the liblouis two-way braille translator
License:        LGPL-3.0-or-later
Group:          System/Libraries
Conflicts:      liblouis2 < 3.3.0
BuildArch:      noarch

%description data
liblouis is a translator from and to braille. It features support for
computer and literary braille, supports contracted and uncontracted
translation for many languages and has support for hyphenation.

This package contains data required by main package.

%package tools
Summary:        Tools from the liblouis braille translator package
License:        GPL-3.0-or-later
Group:          Productivity/Other

%description tools
liblouis is a translator from and to braille. It features support for
computer and literary braille, supports contracted and uncontracted
translation for many languages and has support for hyphenation.

%package doc
Summary:        Documentation for the liblouis braille translator
License:        LGPL-3.0-or-later
Group:          Documentation/Other

%description doc
liblouis is a translator from and to braille. It features support for
computer and literary braille, supports contracted and uncontracted
translation for many languages and has support for hyphenation.

%package devel
Summary:        Development files for the liblouis braille translator
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       liblouis%{sover} = %{version}

%description devel
liblouis is a translator from and to braille. It features support for
computer and literary braille, supports contracted and uncontracted
translation for many languages and has support for hyphenation. New
languages can be added through tables that support a rule- or
dictionary-based approach. Math braille (Nemeth and Marburg) is
supported.

%package -n python3-louis
Summary:        Python3 bindings for the liblouis braille translator
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
Requires:       liblouis%{sover} = %{version}

%description -n python3-louis
liblouis is a translator from and to braille. It features support for
computer and literary braille, supports contracted and uncontracted
translation for many languages and has support for hyphenation.

This subpackage contains the Python3 bindings.

%prep
%autosetup -p1

%build
%configure --disable-static --enable-ucs4
%make_build

# build python binding
pushd python
%python3_build
popd

%install
%make_install
# doc is only auto-installed when makeinfo is present
%make_install -C doc
find %{buildroot} -type f -name "*.la" -delete -print
# We'll package them as rpm docs
rm -f %{buildroot}%{_datadir}/doc/liblouis/liblouis.{html,txt}
%fdupes %{buildroot}%{_datadir}
%fdupes %{buildroot}%{_libdir}

# install python binding
pushd python
%python3_install
popd

%post -n liblouis%{sover} -p /sbin/ldconfig
%postun -n liblouis%{sover} -p /sbin/ldconfig

%check
make check %{_smp_mflags}

%files -n liblouis%{sover}
%license COPYING.LESSER
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/*.so.*

%files data
%{_datadir}/liblouis/

%files tools
%license COPYING

%{_bindir}/lou_*

%files doc
%doc doc/liblouis.html doc/liblouis.txt
%{_infodir}/%{name}.info%{?ext_info}

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/liblouis

%files -n python3-louis
%{python3_sitelib}/louis*.egg-info
%{python3_sitelib}/louis

%changelog
