#
# spec file for package diff-pdf
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


Name:           diff-pdf
Version:        0.2
Release:        0
Summary:        Simple PDF comparison tool
License:        GPL-2.0 and LGPL-2.0
Group:          Productivity/Publishing/PDF
Url:            https://github.com/vslavik/diff-pdf
Source0:        https://github.com/vslavik/diff-pdf/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  wxWidgets-3_0-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-pdf)
BuildRequires:  pkgconfig(poppler)
BuildRequires:  pkgconfig(poppler-cairo)
BuildRequires:  pkgconfig(poppler-glib)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
diff-pdf is a simple tool for comparing two PDF files.

%prep
%setup -q

%build
export CXXFLAGS="%{optflags} -fpermissive"
export LDFLAGS='-Wl,--as-needed -Wl,--no-undefined -Wl,-z,now'
./bootstrap
%configure
make %{?_smp_mflags} V=1

%install
%make_install

%files
%defattr(-,root,root,-)
%doc AUTHORS COPYING COPYING.icons README
%{_bindir}/diff-pdf

%changelog
