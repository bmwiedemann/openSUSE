#
# spec file for package idep
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


Name:           idep
Version:        0.5
Release:        0
Summary:        Track the Dependencies in your C or C++ Code
License:        GPL-2.0-or-later
Group:          Development/Languages/C and C++
URL:            https://www.stolk.org
Source:         %{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}-configure.diff
Patch1:         idep-C_headers.patch
Patch2:         idep-foreign_package.patch
Patch3:         idep-constify_args.patch
Patch4:         idep-call_LT_INIT.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool

%description
Idep can be used for checking the dependencies of C++ include files. It
offers these features:

- Prints out hierarchy of include files

- Lists the class definitions that are found in each header file

- Detects cyclic dependencies in your include files

- Detects inclusions that could be pruned

%prep
%autosetup -p0

%build
autoreconf -fiv
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog README
%{_bindir}/idep

%changelog
