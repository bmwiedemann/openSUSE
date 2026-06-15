#
# spec file for package guile-arguments
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


Name:           guile-arguments
Version:        0.1.1
Release:        0
Summary:        Parser for breaking down command line arguments into structured objects
License:        GPL-3.0-or-later
Group:          Development/Libraries/Other
URL:            https://codeberg.org/fishinthecalculator/arguments
Source0:        https://codeberg.org/fishinthecalculator/arguments/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  guile-devel >= 3.0
BuildRequires:  make
BuildRequires:  pkg-config
BuildRequires:  texinfo
Requires:       guile >= 3.0
Requires(post): %{install_info_prereq}
Requires(preun):%{install_info_prereq}

%description
guile-arguments is a Guile Scheme library to parse command line
arguments into structured objects, much like (ice-9 getopt-long).
Its API allows declaring arguments through a small DSL, then call
a procedure to parse the command line into a structured object.

%prep
%autosetup -p1 -n arguments

%build
autoreconf -vif
%configure
%make_build

%check
%make_build check

%install
%make_install

%post
%install_info --info-dir=%{_infodir} %{_infodir}/arguments.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/arguments.info.gz

%files
%license COPYING
%doc README.md
%{_datadir}/guile
%{_libdir}/guile
%{_infodir}/arguments.info%{?ext_info}

%changelog
