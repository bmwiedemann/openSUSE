#
# spec file for package obs-service-replace_using_package_version
#
# Copyright (c) 2024 SUSE LLC
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


%define service replace_using_package_version

Name:           obs-service-%{service}
Version:        0.0.9
Release:        0
Summary:        An OBS service: Replaces a regex  with the version value of a package
License:        GPL-3.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/obs-service-%{service}
Source0:        %{service}.py
Source1:        %{service}.service
Source2:        LICENSE
BuildRequires:  sed
# for the __python3 macro
BuildRequires:  python-rpm-macros
Requires:       python3-docopt
Requires:       python3-rpm
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This service replaces a given regex with the version value of
a given package. Can be used to align the version of you package or image
to the version of another package.

%prep
cp %{S:0} .
cp %{S:1} .
cp %{S:2} .

%build
sed -i "s|#!/usr/bin/env python3|#!/usr/bin/python3|g" %{service}.py

%install

install -D -m 755 %{service}.py %{buildroot}%{_prefix}/lib/obs/service/%{service}
install -D -m 644 %{service}.service %{buildroot}%{_prefix}/lib/obs/service/%{service}.service
# Doing %%python3_fix_shebang_path old fashioned way for the backward compatibility
sed -i "1s@#\\!.*python\S*@#\\!$(realpath %__python3)@" \
    %{buildroot}%{_prefix}/lib/obs/service/%{service}

%files
%defattr(-,root,root)
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service
%license LICENSE

%changelog
