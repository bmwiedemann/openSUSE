#
# spec file for package manchu-fonts
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           manchu-fonts
Version:        2.007+svn77
Release:        0
Summary:        Manchu Unicode Fonts
License:        OFL-1.1 and GFDL-1.2+
Group:          System/X11/Fonts
Url:            http://sourceforge.net/projects/manchufont/
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  dos2unix
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Font for the Manchu script

%prep
%setup -q

%build

%install
dos2unix *.txt
mkdir -p %{buildroot}%{_ttfontsdir}
install -m 0644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc *.txt *.odt *.pdf
%{_ttfontsdir}

%changelog
