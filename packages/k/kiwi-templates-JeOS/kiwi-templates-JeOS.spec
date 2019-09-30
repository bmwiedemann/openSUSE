#
# spec file for package kiwi-templates-JeOS
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


%define dest %_datadir/kiwi/image/openSUSE-Tumbleweed-JeOS

%if "@BUILD_FLAVOR@" != ""
ExclusiveArch:  do_not_build
%endif

Name:           kiwi-templates-JeOS
Version:        84.87
Release:        0
BuildArch:      noarch
Summary:        KIWI - openSUSE Tumbleweed JeOS image templates
License:        MIT
Group:          System/Management
Url:            https://www.opensuse.org/
Source01:       config.sh
Source02:       JeOS.kiwi
Source03:       editbootinstall_rpi.sh
#
Source99:       LICENSE
Requires:       python3-kiwi
Supplements:    kiwi-templates

%description
This package contains system image templates to easily build
a openSUSE Tumbleweed based operating system image with
kiwi.

%prep
%setup -cT
cp "%SOURCE99" .

%build

%install
dst="%buildroot%dest"
mkdir -p $dst
for i in %{SOURCE1} %{SOURCE2} %{SOURCE3}; do
	install -m 644 $i "$dst"
done

%files
%license LICENSE
%dest
%_datadir/kiwi/

%changelog
