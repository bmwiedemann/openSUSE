#
# spec file for package courier-prime-fonts
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


Name:           courier-prime-fonts
Version:        1.203
Release:        0
Summary:        Monospace font similar to Courier
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            http://quoteunquoteapps.com/courierprime/
Source0:        courier-prime.zip
Source1:        courier-sans.zip
Source2:        courier-code.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Courier Prime is a Courier-like monospace fonts for screenplay (and other use cases).
It is optimized for 12 point size and matches the metrics of Courier.

%prep
%setup -c
%setup -T -D -a 1
%setup -T -D -a 2

mv Courier\ Prime/*.ttf ./
mv Courier\ Prime/LICENSE/OFL.txt LICENSE
mv Courier\ Prime/Read\ me.txt README
mv CourierPrimeSans-master/ttf/*.ttf ./
mv ttf/*.ttf ./

# Replace spaces in filenames
for file in *.ttf; do mv "$file" "$(echo "$file" | tr ' ' '_')"; done

# Fix DOS line endings
sed -i 's/\r//g' LICENSE README

%build
# -- nop --

%install
mkdir -p  %{buildroot}%{_ttfontsdir}/
install -c -m 644 *.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%defattr(-, root,root)
%doc LICENSE README
%{_ttfontsdir}

%changelog
