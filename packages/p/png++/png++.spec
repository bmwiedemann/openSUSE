#
# spec file for package png++
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           png++
Version:        0.2.9
Release:        0
Summary:        C++ wrapper for the libpng library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://www.nongnu.org/pngpp/
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
PNG++ provides a C++ interface to libpng, the PNG reference implementation library.

%package -n %{name}-devel
Summary:        C++ wrapper for libpng library
Group:          Development/Libraries/C and C++
Requires:       pkgconfig(libpng)

%description -n %{name}-devel
PNG++ provides a C++ interface to libpng, the PNG reference implementation library.

%prep
%setup -q

%build

%install
install -d -m 0755 %{buildroot}%{_includedir}/%{name}
install -m 0644 *.hpp %{buildroot}%{_includedir}/%{name}

%files -n %{name}-devel
%defattr(-,root,root)
%{_includedir}/%{name}

%changelog
