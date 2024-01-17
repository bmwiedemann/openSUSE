#
# spec file for package product-builder-plugin-Tumbleweed
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


Name:           product-builder-plugin-Tumbleweed
Summary:        openSUSE - KIWI Image System
License:        GPL-2.0-or-later
Group:          System/Management
Version:        1.8.3
Release:        0
Source:         product-builder-plugins-%version.tar.xz
Provides:       product-builder-plugin = %version-%release
Requires:       createrepo_c
Requires:       dnf
Requires:       mtools
Requires:       product-builder
Requires:       perl(YAML::XS)
Supplements:    product-builder
Requires:       build >= 20230215
%if 0%{?suse_version}
Requires:       instsource-susedata
Requires:       mkdosfs
Requires:       openSUSE-appstream-process
Requires:       package-EULAs
Requires:       package-translations
%endif
BuildArch:      noarch

%description
openSUSE - Product Builder Image System InstSource plugins provides information
and plugin code to create meta information for a SUSE
installation source. This particular package contains the metadata
plugins specific for the openSUSE Tumblweed media.

%prep
%setup -n product-builder-plugins-%version

%build
# empty because of rpmlint warning rpm-buildroot-usage

%install
# build
test -e /.buildenv && . /.buildenv
make buildroot="%{buildroot}" version="tumbleweed" install

%files
%license LICENSE
%dir %{_datadir}/kiwi
%dir %{_datadir}/kiwi/modules
%dir %{_datadir}/kiwi/modules/plugins
%dir %{_datadir}/kiwi/modules/plugins/tumbleweed
%{_datadir}/kiwi/modules/plugins/tumbleweed/*.pm
%config(noreplace) %{_datadir}/kiwi/modules/plugins/tumbleweed/*.ini

%changelog
