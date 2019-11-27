#
# spec file for package product-builder-plugin-openSUSE
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


Name:           product-builder-plugin-openSUSE
Summary:        openSUSE - KIWI Image System
License:        GPL-2.0-or-later
Group:          System/Management
Version:        1.2.2
Release:        0
Source:         product-builder-plugins-%version.tar.xz
Provides:       product-builder-plugin = %version-%release
Provides:       product-builder-plugin-Tumbleweed = 1.2.1
Obsoletes:      product-builder-plugin-Tumbleweed <= 1.2.1
Requires:       createrepo_c
Requires:       instsource-susedata
Requires:       mkdosfs
Requires:       mtools
Requires:       openSUSE-appstream-process
Requires:       package-EULAs
Requires:       package-translations
Requires:       product-builder
Supplements:    product-builder
BuildArch:      noarch

%description
openSUSE - Product Builder Image System InstSource plugins provides information
and plugin code to create meta information for a SUSE
installation source.

%prep
%setup -n product-builder-plugins-%version

%build
# empty because of rpmlint warning rpm-buildroot-usage

%install
# build
test -e /.buildenv && . /.buildenv
make buildroot="%{buildroot}" version="openSUSE" install

%files
%license LICENSE
%dir %{_datadir}/kiwi
%dir %{_datadir}/kiwi/modules
%dir %{_datadir}/kiwi/modules/plugins
%dir %{_datadir}/kiwi/modules/plugins/openSUSE
%{_datadir}/kiwi/modules/plugins/openSUSE/*.pm
%config(noreplace) %{_datadir}/kiwi/modules/plugins/openSUSE/*.ini

%changelog
