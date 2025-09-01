#
# spec file for package sil-andika-six-fonts
#
# Copyright (c) 2025 SUSE LLC
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


Name:           sil-andika-six-fonts
License:        OFL-1.1
Group:          System/X11/Fonts
Summary:        Sans serif, Unicode-compliant Font For Literacy Use
Version:        6.210
Release:        0
URL:            https://software.sil.org/andika/
Source0:        https://software.sil.org/downloads/r/andika/AndikaSix-%{version}.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Andika Six is renamed version of Andika v6.200 with no other
changes. Andika version 7 includes metrics changes that
could cause lines, paragraphs, and pages to reflow. Because
of this we wanted to provide a font that reproduced the
exact metrics and behavior of Andika v6.200 and could be
installed at the same time as the newest Andika (v7 and beyond).
Andika v7 is still the best font for most people to use.
But if you have documents prepared with Andika v6.200 and
need to preserve the spacing, you can install Andika Six,
change the doc to use it instead of Andika, and avoid any
issues with reflow. Then you can use Andika v7 for new
documents and benefit from the many improvements in this and
future versions.

%prep
%autosetup -c
find -type f -exec chmod -x {} +
find -name '*.txt' -exec dos2unix {} +

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 AndikaSix-%{version}/*.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%doc AndikaSix-%{version}/*.txt AndikaSix-%{version}/documentation/pdf/*.pdf
%{_ttfontsdir}

%changelog
