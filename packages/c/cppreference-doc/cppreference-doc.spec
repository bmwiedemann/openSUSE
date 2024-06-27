#
# spec file for package cppreference-doc
#
# Copyright (c) 2024 SUSE LLC
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


Name:           cppreference-doc
Version:        20240610
Release:        0
Summary:        Cppreference documentation for offline reading
License:        CC-BY-SA-3.0
Group:          Documentation/HTML
URL:            http://en.cppreference.com/w/
Source0:        https://github.com/PeterFeicht/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM cppreference-doc-premailer-3.9-compat.patch badshah400@gmail.com -- Fix building against premailer >= 3.9
Patch0:         cppreference-doc-premailer-3.9-compat.patch
BuildRequires:  devhelp
BuildRequires:  fdupes
BuildRequires:  libqt5-qttools
%if 0%{?suse_version} < 1550
BuildRequires:  python3-cssutils
%else
# At least version 2.0.0 of cssutils is required for building on oS 1550
BuildRequires:  python3-cssutils >= 2.0.0
%endif
BuildRequires:  python3-lxml
BuildRequires:  python3-premailer
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Cppreference is a complete online reference for the C and C++ languages and standard libraries, i.e. a more convenient version of the C and C++ standards. This package provides an offline mirror of the reference.

%package devhelp
Summary:        Cppreference documentation for offline reading - devhelp version
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description devhelp
Cppreference is a complete online reference for the C and C++ languages and standard libraries, i.e. a more convenient version of the C and C++ standards. This package provides an offline mirror of the reference in the devhelp format.

This package provides the documentation in the devhelp format.

%package qhelp
Summary:        Cppreference documentation for offline reading - qhelp version
Group:          Documentation/Other
Requires:       %{name} = %{version}

%description qhelp
Cppreference is a complete online reference for the C and C++ languages and standard libraries, i.e. a more convenient version of the C and C++ standards. This package provides an offline mirror of the reference in the devhelp format.

This package provides the documentation in the qhelp format.

%prep
%autosetup -p1

%build
make %{?_smp_mflags} qhelpgenerator=qhelpgenerator-qt5

%install
%make_install

rm %{buildroot}%{_datadir}/devhelp/books/cppreference-doxygen*.xml

%fdupes %{buildroot}%{_datadir}/cppreference/

%files
%doc README.md
%dir %{_datadir}/cppreference
%dir %{_datadir}/cppreference/doc
%{_datadir}/cppreference/doc/html/

%files devhelp
%{_datadir}/devhelp/books/cppreference-doc-en-c/
%{_datadir}/devhelp/books/cppreference-doc-en-cpp/

%files qhelp
%dir %{_datadir}/cppreference/doc/qch
%{_datadir}/cppreference/doc/qch/

%changelog
