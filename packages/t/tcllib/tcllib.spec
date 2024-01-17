#
# spec file for package tcllib
#
# Copyright (c) 2022 SUSE LLC
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


Name:           tcllib
Version:        1.21
Release:        0
Summary:        Tcl Standard Library
License:        TCL
Group:          Development/Libraries/Tcl
URL:            http://tcllib.sf.net
Source0:        http://core.tcl.tk/tcllib/uv/tcllib-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  sed
BuildRequires:  tcl
Requires:       /bin/sh
BuildArch:      noarch

%description
This package is intended to be a collection of Tcl packages that
provide utility functions useful to a large collection of Tcl
programmers.

%prep
%setup -q
# upstream typo
chmod 644 examples/mapproj/ncar780.txt

# fix DOS lineendings
sed -i 's/\r$//' examples/httpd/htdocs/*.md examples/tepam/run_tepam_demo.bat

# remove shebang from module
sed -i '1{ /^#!/d }' modules/pki/pki.tcl modules/oauth/oauth.tcl modules/defer/defer.tcl modules/lazyset/lazyset.tcl

# do not use /usr/bin/env in shebang
for script in $(find apps examples -type f -executable -print); do
    sed -i 's:%{_bindir}/env tclsh:%{_bindir}/tclsh:' $script
done

%build

%install
tclsh ./installer.tcl -no-examples -no-html \
 -app-path   %{buildroot}/%{_bindir} \
 -pkg-path   %{buildroot}/%{_datadir}/tcl/%{name}%{version} \
 -nroff-path %{buildroot}%{_mandir}/mann \
 -no-wait -no-gui

%files
%license license.terms
%doc README.md ChangeLog
%doc support/releases/history/README-*
%{_datadir}/tcl
%{_bindir}/*
%doc examples
%{_mandir}/mann/*

%changelog
