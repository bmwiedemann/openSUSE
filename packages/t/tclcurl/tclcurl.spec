#
# spec file for package tclcurl
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2012 Guido Berhoerster.
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


Name:           tclcurl
Version:        7.22.0
Release:        0
Summary:        Tcl Binding to libcurl
License:        TCL
Group:          Development/Languages/Tcl
URL:            https://github.com/flightaware/tclcurl-fa
Source:         https://github.com/flightaware/tclcurl-fa/archive/refs/tags/v%{version}.tar.gz#/%{name}-fa-%{version}.tar.gz
Patch0:         tclcurl-types.patch
BuildRequires:  bc
BuildRequires:  libcurl-devel >= 7.54.0
BuildRequires:  tcl-devel
Requires:       tcl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
TclCurl provides TCL bindings to the libcurl client-side URL transfer library.

%prep
%autosetup -p0 -n %{name}-fa-%{version}

chmod 644 *.txt doc/*.txt doc/*.html

%build
%configure
make %{?_smp_mflags}

%install
%make_install pkglibdir=%{tcl_archdir}/TclCurl%{version}

mkdir html
cp -p doc/*.html html

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog.txt Changes.txt README.md
%{tcl_archdir}/TclCurl%{version}
%doc %{_mandir}/mann/*.n*

%changelog
