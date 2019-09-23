#
# spec file for package mgopen-fonts
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           mgopen-fonts
Version:        0.20050518
Release:        0
Summary:        Free High-Quality Greek Fonts
License:        SUSE-MgOpen
Group:          System/X11/Fonts
Url:            http://www.ellak.gr/fonts/mgopen/index.en
Source0:        http://www.ellak.gr/fonts/mgopen/files/MgOpen.tar.bz2
# The file README contains the license and was created with
# w3m -dump http://www.ellak.gr/fonts/mgopen/index.en > README
Source1:        README
BuildRequires:  fontpackages-devel
%reconfigure_fonts_prereq
Provides:       scalable-font-el
Provides:       locale(el)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Free high-quality Greek fonts created by Magenta Ltd.

%prep
%setup -c %{name} -n %{name}
cp $RPM_SOURCE_DIR/README .

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}/

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc README
%{_ttfontsdir}

%changelog
