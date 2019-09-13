#
# spec file for package patterns-office
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           patterns-office
Version:        20170506
Release:        0
Summary:        Patterns for Installation (Office)
License:        MIT
Group:          Metapackages
Url:            https://github.com/openSUSE/patterns
Source0:        %{name}-rpmlintrc
BuildRequires:  patterns-rpm-macros

%description
This is an internal package that is used to create the patterns as part
of the installation source setup.  Installation of this package does
not make sense.

This particular package contains the office patterns.

%package office
%pattern_desktopfunctions
Summary:        Office Software
Group:          Metapackages
Provides:       pattern() = office
Provides:       pattern-icon() = pattern-office
Provides:       pattern-order() = 1640
Provides:       pattern-visible()
Recommends:     libreoffice
Recommends:     libreoffice-calc
Recommends:     libreoffice-draw
Recommends:     libreoffice-impress
Recommends:     libreoffice-math
Recommends:     libreoffice-writer

%description office
Office software for your desktop environment including LibreOffice.

%files office
%dir %{_defaultdocdir}/patterns
%{_defaultdocdir}/patterns/office.txt

%prep
:

%build
:

%install
mkdir -p %{buildroot}/%{_defaultdocdir}/patterns
echo "This file marks the pattern office to be installed." \
	> %{buildroot}/%{_defaultdocdir}/patterns/office.txt

%changelog
