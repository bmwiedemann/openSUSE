#
# spec file for package tcllib
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Url:            http://tcllib.sf.net
BuildRequires:  tcl
Version:        1.19
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Tcl Standard Library
License:        TCL
Group:          Development/Libraries/Tcl
BuildRequires:  sed
Requires:       /bin/sh
BuildArch:      noarch
Source0:        http://core.tcl.tk/tcllib/uv/tcllib-%version.tar.xz
Source1:        %name-rpmlintrc

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
sed -i '1d' modules/pki/pki.tcl modules/oauth/oauth.tcl modules/defer/defer.tcl

# do not use /usr/bin/env in shebang
for script in $(find apps examples -type f -executable -print); do
    sed -i 's:/usr/bin/env tclsh:/usr/bin/tclsh:' $script
done

%build

%install
tclsh ./installer.tcl -no-examples -no-html \
 -app-path   %buildroot/%_bindir \
 -pkg-path   %buildroot/%_datadir/tcl/%name%version \
 -nroff-path %buildroot%_mandir/mann \
 -no-wait -no-gui

%files
%defattr(-,root,root)
%doc license.terms README ChangeLog
%doc support/releases/history/README-*
%_datadir/tcl
%_bindir/*
%doc examples
%doc %_mandir/mann/*

%changelog
