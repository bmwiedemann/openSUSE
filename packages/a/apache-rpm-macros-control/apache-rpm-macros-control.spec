#
# spec file for package apache-rpm-macros-control
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%if 0%{?suse_version} > 1230
%define macros_dir            %{_libexecdir}/rpm/macros.d
%else
%define macros_dir            %{_sysconfdir}/rpm
%endif
Name:           apache-rpm-macros-control
Version:        20151110
Release:        0
Summary:        Apache RPM Macros
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
Url:            http://httpd.apache.org/
Source1:        macros.apache-control
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Macros intended for Apache restarts in rpm scriptlets.

%prep

%build

%install
mkdir -p %{buildroot}%{macros_dir}
install -m 644 %{SOURCE1} %{buildroot}%{macros_dir}

%files
%defattr(-,root,root)
%dir %{macros_dir}
%{macros_dir}/macros.apache*

%changelog
