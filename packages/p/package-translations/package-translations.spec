#
# spec file for package package-translations
#
# Copyright (c) 2023 SUSE LLC
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


Name:           package-translations
Version:        89.87.20230128.cd224a6
Release:        0
Summary:        Summary and Descriptions Translations
License:        BSD-3-Clause
Group:          System/GUI/Other
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch
URL:            https://github.com/openSUSE/packages-i18n/

%define build_languages cs de es fr hu it ja lt nl nn ru uk zh_CN

%description
This package provides translations for our packages. You don't want to install this
package on your system, it's only useful when you create openSUSE media.

%prep
%setup -q

%build

%install
target_dir=$RPM_BUILD_ROOT/usr/share/locale/en_US/LC_MESSAGES
mkdir -p $target_dir
for lang in %build_languages; do
  msgcat --use-first $lang/po/*.po | msgfmt -o $target_dir/package-translations-$lang.mo -
done

%files
%defattr(-,root,root)
%lang(en) /usr/share/locale/en_US/LC_MESSAGES/*

%changelog
