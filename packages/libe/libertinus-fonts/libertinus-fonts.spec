#
# spec file for package libertinus-fonts
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define fontname Libertinus
Name:           libertinus-fonts
Version:        6.10
Release:        0
Summary:        Libertinus font family
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/alif-type/libertinus
Source0:        https://github.com/alif-type/libertinus/releases/download/v%{version}/%{fontname}-%{version}.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Libertinus font family: serif, sans and mono. It is a fork of the Linux Libertine font family.

%prep
%setup -q -n %{fontname}-%{version}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -m 0644 *.otf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%doc FONTLOG.txt OFL.txt README.txt
%dir %{_ttfontsdir}
%{_ttfontsdir}/*

%changelog
