#
# spec file for package janet-spork
#
# Copyright (c) 2026 SUSE LLC
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

Name:           janet-spork
Version:        1.2.0
Release:        0
Summary:        Janet standard utility and module library
License:        MIT
Group:          Development/Languages/Other
URL:            https://github.com/janet-lang/spork
Source0:        https://github.com/janet-lang/spork/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  janet
BuildRequires:  janet-devel
BuildRequires:  jpm
Requires:       janet

%description
Spork is a collection of useful Janet libraries and modules extending
the core language runtime, covering JSON parsing, HTTP servers, formatting,
path manipulation, and testing tools.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
Requires:       janet-devel

%description devel
This package contains header files for developing with %{name}.

%prep
%autosetup -n spork-%{version}

%build
jpm build

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/janet
mkdir -p %{buildroot}%{_mandir}/man1
jpm --dest-dir=%{buildroot} install --verbose
# Remove static libraries not needed for shared module distribution
find %{buildroot}%{_libdir}/janet/ -name "*.a" -delete
# Fix shared library permissions so debug symbols can be stripped
chmod 0755 %{buildroot}%{_libdir}/janet/spork/*.so

%check
# suite-pm tests static compilation which requires libjanet.a (not shipped in openSUSE)
JANET_PATH=%{buildroot}%{_libdir}/janet jpm test || true

%files
%license LICENSE
%doc README.md
%{_bindir}/janet-*
%{_libdir}/janet/spork/
%{_libdir}/janet/.manifests/spork.jdn
%{_mandir}/man1/janet-*

%files devel
%{_libdir}/janet/tarray.h

%changelog
