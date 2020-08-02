#
# spec file for package patterns-openSUSE
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


%bcond_with betatest

Name:           patterns-devel-tcl
Version:        20170319
Release:        0
Summary:        Patterns for Installation (Tcl devel)
License:        MIT
Group:          Metapackages
Url:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  patterns-rpm-macros


%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the Tcl development pattern.

################################################################################

%package devel_tcl
%pattern_development
Summary:        Tcl/Tk Development
Group:          Metapackages
Provides:       pattern() = devel_tcl
Provides:       pattern-icon() = pattern-tcltk-devel
Provides:       pattern-order() = 3480
Provides:       pattern-visible()

Recommends:     tcl
Recommends:     tcl-devel
Recommends:     tk
Recommends:     tk-devel
Recommends:     bwidget
Recommends:     expect
Recommends:     frink
Recommends:     iwidgets
Recommends:     snack
Recommends:     tcllib
Recommends:     tcludp
Recommends:     tclx
Recommends:     tdom
Recommends:     tix
Recommends:     tkimg
Recommends:     tktable
Recommends:     tls
# #387771
Recommends:     itk
Recommends:     expect-devel
# #387771
Recommends:     tclplug
Suggests:       PgTcl
Suggests:       scotty
Suggests:       sqlite3-tcl
Suggests:       vtcl

%description devel_tcl
Tools and libraries for development using Tcl and Tk.

%files devel_tcl
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/devel_tcl.txt

################################################################################

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/packages/patterns/
echo 'This file marks the pattern devel_tcl to be installed.' > $RPM_BUILD_ROOT/usr/share/doc/packages/patterns/devel_tcl.txt
