#
# spec file for package tagbanwa-fonts
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

%define src_name tagbanwa

Name:           tagbanwa-fonts
Version:        1.001
Release:        0
Summary:        Tagbanwa Fonts
License:        CC-BY-2.5
Group:          System/X11/Fonts
Url:            http://youpibouh.thefreecat.org/download/tagbanwa.htm
Source0:        http://youpibouh.thefreecat.org/download/%{src_name}.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Font for the Tagbanwa script.

%prep
%setup -q -n %{src_name}

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc *.txt CC-2.5
%{_ttfontsdir}

%changelog
