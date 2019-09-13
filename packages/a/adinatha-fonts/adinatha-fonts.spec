#
# spec file for package adinatha-fonts
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


Name:           adinatha-fonts
Version:        1.0
Release:        0
Summary:        Tamil-Brahmi font
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://www.virtualvinodh.com/
Source0:        http://www.virtualvinodh.com/download/Adinatha-Tamil-Brahmi.zip
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Adinatha is a  working Unicode Tamil Brahmi font.

%prep
%setup -q -c -T -a0

%build
dos2unix *.xml

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.otf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc *.pdf *.xml
%{_ttfontsdir}

%changelog
