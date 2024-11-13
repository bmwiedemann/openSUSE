#
# spec file for package libjodycode
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


%define c_lib   libjodycode3
Name:           libjodycode
Version:        3.1
Release:        0
Summary:        Shared code used by several utilities written by Jody Bruchon
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://codeberg.org/jbruchon/libjodycode
Source0:        https://codeberg.org/jbruchon/libjodycode/archive/v%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make

%description
libjodycode is a software code library containing code shared among several of the programs written by Jody Bruchon such as imagepile, jdupes, winregfs, and zeromerge. These shared pieces of code were copied between each program as they were updated. As the number of programs increased and keeping these pieces of code synced became more annoying, the decision was made to combine all of them into a single reusable shared library.

%package -n libjodycode-devel
Summary:        Development files for libjodycode
Group:          Development/Libraries/C and C++
Requires:       %{c_lib} = %{version}

%description -n libjodycode-devel
Development files and headers for libjodycode

%package -n %{c_lib}
Summary:        Shared code used by several utilities written by Jody Bruchon
Group:          System/Libraries

%description -n %{c_lib}
libjodycode is a software code library containing code shared among several of the programs written by Jody Bruchon such as imagepile, jdupes, winregfs, and zeromerge. These shared pieces of code were copied between each program as they were updated. As the number of programs increased and keeping these pieces of code synced became more annoying, the decision was made to combine all of them into a single reusable shared library.

%prep
%setup -q -n %name

%build
%make_build

%install
%make_install PREFIX="%{_prefix}" LIB_DIR="%{_libdir}"
rm %{buildroot}%{_libdir}/libjodycode.a

%post -n %{c_lib} -p /sbin/ldconfig
%postun -n %{c_lib} -p /sbin/ldconfig

%files -n %{c_lib}
%license LICENSE.txt
%{_libdir}/libjodycode.so.3
%{_libdir}/libjodycode.so.3.1

%files -n libjodycode-devel
%doc CHANGES.txt README.md
%{_includedir}/libjodycode.h
%{_libdir}/libjodycode.so
%{_mandir}/man7/libjodycode.7%{?ext_man}

%changelog
