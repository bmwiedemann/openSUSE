#
# spec file for package meslo-lg-fonts
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


Name:           meslo-lg-fonts
Version:        1.2.1
Release:        0
Summary:        Meslo LG Font Family
License:        Apache-2.0
Group:          System/X11/Fonts
Url:            https://github.com/andreberg/Meslo-Font
# Extract sources 0 and 1 from
# https://github.com/andreberg/Meslo-Font/archive/v1.2.1.tar.gz
# which is large and includes previous versions.
Source0:        Meslo_LG_v%{version}.zip
Source1:        README.textile
Source2:        COPYING
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
Meslo LG is a customized version of Apple's Menlo-Regular font (which is
a customized Bitstream Vera Sans Mono).

%prep
%setup -qn "Meslo LG v%{version}"
cp %{SOURCE1} .
cp %{SOURCE2} .
# %%doc doesn't work with spaces. Let's rename the file.
mv -f "About Meslo LG v%{version}.pdf" About_Meslo_LG_v%{version}.pdf

%build

%install
for f in *.ttf ; do
    install -Dm 644 "${f}" %{buildroot}%{_ttfontsdir}/"${f}"
done

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root,-)
%doc About_Meslo_LG_v%{version}.pdf COPYING README.textile
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.ttf

%changelog
