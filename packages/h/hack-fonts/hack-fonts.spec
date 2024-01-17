#
# spec file for package hack-fonts
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2015 Alexander Evseev
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


%define realname Hack
%define extraver -ttf
%define srcext   zip
# Common info
Name:           hack-fonts
Version:        3.003
Release:        0
Summary:        A typeface designed for source code
License:        Bitstream-Vera AND MIT
# rpmlint has not been updated yet to reflect the new license names already present on
# format specfile https://github.com/rpm-software-management/rpmlint/pull/982
Group:          System/X11/Fonts
URL:            http://sourcefoundry.org/hack/
Source:         https://github.com/source-foundry/Hack/releases/download/v%{version}/%{realname}-v%{version}%{?extraver}.%{srcext}
Source1:        README.md
Source2:        LICENSE.md
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
Provides:       %{realname} = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
A typeface designed for source code

Hack includes monospaced regular, bold, oblique, and bold oblique sets to cover
all of your syntax highlighting needs.

Over 1500 glyphs that include lovingly tuned expanded Latin, modern Greek, and
Cyrillic character sets.

Powerline glyphs are included in the regular set. Patching is not necessary.
Install and go.

%prep
%setup -q -n %{realname}-%{version}%{?extraver} -c

%build

%install
mkdir -p %{buildroot}%{_ttfontsdir}
install -m644 ttf/*.ttf %{buildroot}%{_ttfontsdir}
install -d %{buildroot}%{_docdir}/%{name}
install -m644 %{S:1} %{S:2} %{buildroot}%{_docdir}/%{name}

%reconfigure_fonts_scriptlets

%files
%defattr(-,root,root)
%doc %{_docdir}/%{name}
%{_ttfontsdir}

%changelog
