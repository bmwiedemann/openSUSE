#
# spec file for package mozilla-fira-sans-fonts
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


Name:           mozilla-fira-fonts
Version:        4.202
Release:        0
Summary:        Mozilla’s Fira Type Family
License:        OFL-1.1
Group:          System/X11/Fonts
Url:            https://github.com/mozilla/Fira
Source0:        https://github.com/mozilla/Fira/archive/refs/tags/%{version}.zip#/Fira-%{version}.zip
BuildRequires:  fontpackages-devel
BuildRequires:  unzip
%reconfigure_fonts_prereq
BuildArch:      noarch
Provides:       mozilla-fira-sans-fonts  < %version-%release
Provides:       mozilla-feura-sans-fonts < %version-%release

%description
Fira Sans (née Feura Sans) is a friendly free sans-serif font designed
for Firefox OS. It looks very similar to FF Meta, but has a larger
x-height to improve on-screen appearance. (Available in 16 weights, each
with accompanying italics.)
This package also contains Fira Sans Condensed, 16% more compact, and
Fira Mono, a monospaced semi-serif font with a matching design.
(Available in three weights, without italics.)

Designers: Ralph du Carrois & Erik Spiekermann.

%prep
%autosetup -n Fira-%{version}
chmod -x LICENSE

%build

%install
install -d %{buildroot}%{_ttfontsdir}
# by default install command uses 755 umask
install -D -v -m 644 otf/*.otf %{buildroot}%{_ttfontsdir}

%reconfigure_fonts_scriptlets

%files
%license LICENSE
%dir %{_ttfontsdir}
%{_ttfontsdir}/*.otf

%changelog
