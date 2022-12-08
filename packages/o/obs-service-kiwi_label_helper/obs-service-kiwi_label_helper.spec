#
# spec file for package obs-service-kiwi_label_helper
#
# Copyright (c) 2022 SUSE LLC
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


Name:           obs-service-kiwi_label_helper
Version:        0.0
Release:        0
Summary:        Service to duplicate labels with a custom prefix
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://build.opensuse.org
Source0:        kiwi_label_helper.service
Source1:        kiwi_label_helper
Source2:        README
Source3:        label_helper.xsl
Requires:       libxslt-tools
BuildArch:      noarch

%description
This service can be used during buildtime to implement the
suse_label_helper:add_prefix element useful for building containers.

%prep
%setup -q -D -T -c
cp %{SOURCE2} .

%build

%install

mkdir -p %{buildroot}%{_prefix}/lib/obs/service %{buildroot}%{_prefix}/lib/kiwi_label_helper
install -m 0644 %{SOURCE0} %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 %{SOURCE1} %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 %{SOURCE3} %{buildroot}%{_prefix}/lib/kiwi_label_helper

%files
%doc README
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service
%dir %{_prefix}/lib/kiwi_label_helper
%{_prefix}/lib/kiwi_label_helper/label_helper.xsl

%changelog
