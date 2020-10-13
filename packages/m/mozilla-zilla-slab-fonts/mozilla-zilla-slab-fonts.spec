#
# spec file for package mozilla-zilla-slab-fonts
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

%global short_name zilla-slab
Name:           mozilla-%{short_name}-fonts
Version:        1.002
Release:        0
Summary:        A Slab Typeface from Mozilla
License:        OFL-1.1
Group:          System/X11/Fonts
URL:            https://github.com/mozilla/%{short_name}
Source:         %{URL}/releases/download/v%{version}/Zilla-Slab-Fonts-v%{version}.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
BuildArch:      noarch
%reconfigure_fonts_prereq

%description
%{summary}.

Designers: Typotheque

%prep
%autosetup -n %{short_name}

%build
# nop

%install
install -d %{buildroot}%{_ttfontsdir}
# by default install command uses 755 umask
install -m 644 ttf/*.ttf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%attr(0644,-,-) %license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.ttf

%changelog
