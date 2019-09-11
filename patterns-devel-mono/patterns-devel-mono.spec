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

Name:           patterns-devel-mono
Version:        20170319
Release:        0
Summary:        Patterns for Installation (Mono devel)
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

This particular package contains the pattern for Mono Development

################################################################################

%package devel_mono
%pattern_development
Summary:        .NET Development
Group:          Metapackages
Provides:       pattern() = devel_mono
Provides:       pattern-icon() = pattern-mono
Provides:       pattern-order() = 3220
Provides:       pattern-visible()

Recommends:     mono-core
Recommends:     mono-devel
Recommends:     monodevelop
Recommends:     apache2-mod_mono
Recommends:     boo
Recommends:     dbus-1-mono
Recommends:     gsf-sharp
Recommends:     gtk-sharp2-complete
Recommends:     gtk-sharp2-doc
Recommends:     gtk-sharp2-gapi
Recommends:     gtksourceview2-sharp
Recommends:     ikvm
Recommends:     mono-basic
Recommends:     mono-data
Recommends:     mono-data-oracle
Recommends:     mono-data-postgresql
Recommends:     mono-data-sqlite
Recommends:     monodoc-core
Recommends:     mono-extras
Recommends:     mono-locale-extras
Recommends:     mono-nunit
Recommends:     mono-tools
Recommends:     mono-web
Recommends:     mono-winforms
Suggests:       mono-debugger
Suggests:       rsvg2-sharp
Suggests:       vte016-sharp

%description devel_mono
Tools and libraries for .NET development using Mono.

%files devel_mono
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/devel_mono.txt

################################################################################

%prep

%build

%install
mkdir -p %{buildroot}/%{_defaultdocdir}/patterns/
echo 'This file marks the pattern devel_mono to be installed.' >%{buildroot}/%{_defaultdocdir}/patterns/devel_mono.txt
