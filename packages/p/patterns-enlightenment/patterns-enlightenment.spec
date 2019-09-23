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

Name:           patterns-enlightenment
Version:        20170319
Release:        0
Summary:        Patterns for Installation (Enlightenment patterns)
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

This particular package contains the Enlightenment pattern.

################################################################################

%package enlightenment
%pattern_graphicalenvironments
Summary:        Enlightenment
Group:          Metapackages
Provides:       pattern() = enlightenment
Provides:       pattern-icon() = pattern-enlightenment
Provides:       pattern-order() = 1500
Provides:       pattern-visible()
Obsoletes:      %{name}-e17
Requires:       pattern() = x11
Recommends:     pattern() = multimedia
Recommends:     pattern() = imaging
Requires:       enlightenment
Requires:       lightdm
Recommends:     terminology
Recommends:     desktop-branding

Recommends:     google-droid-fonts
Recommends:     MozillaFirefox
Recommends:     desktop-data-openSUSE
# bnc#508120
Recommends:     xdg-user-dirs
# from data/COMMON-DESKTOP-OPT
# packages a GTK application
Recommends:     gutenprint
# MAYBE later lsb-graphics
Recommends:     icedtea-web
# give net shares
Recommends:     samba
# needs python-qt4, see#649280#14
Suggests:       hplip
# Add some Common useful programs that don't require another DE
Recommends:     clementine
Recommends:     vlc
Recommends:     leafpad
Recommends:     mupdf

%description enlightenment
Enlightenment Window Manager and applications

%files enlightenment
%dir /usr/share/doc/packages/patterns
/usr/share/doc/packages/patterns/enlightenment.txt

################################################################################

%prep

%build

%install
mkdir -p %{buildroot}/usr/share/doc/packages/patterns/
echo 'This file marks the pattern enlightenment to be installed.' >%{buildroot}/usr/share/doc/packages/patterns/enlightenment.txt
