#
# spec file for package velum-branding
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%if 0%{?is_opensuse} && 0%{?suse_version} > 1500
  %define _dist kubic
%else
  %define _dist caasp
%endif

Name:           velum-branding
Version:        0.0.0+git_r22_fe3c5d0
Release:        0
Summary:        Branding for velum
License:        Apache-2.0
Group:          Applications/Internet
Url:            https://github.com/kubic-project/velum-branding
Source:         master.tar.gz
Provides:       velum-branding = %{version}

%description
%{_dist} branding themes for velum

%prep
%setup -q -n velum-branding-master

%build
%install
# Install the web content
install -d -m 0755 %{buildroot}/%{_datadir}/velum
install -d -m 0755 %{buildroot}/%{_datadir}/velum/images
install -d -m 0755 %{buildroot}/%{_datadir}/velum/static-pages
# set the product name
cp %{_dist}-%{name}/PRODUCT %{buildroot}/%{_datadir}/velum
# add different logos
cp -R %{_dist}-%{name}/app/assets/images/* %{buildroot}/%{_datadir}/velum/images
# add static pages
cp -R %{_dist}-%{name}/static-pages/* %{buildroot}/%{_datadir}/velum/static-pages

%files
%defattr(-,root,root)
%dir %{_datadir}/velum
%{_datadir}/velum/PRODUCT
%dir %{_datadir}/velum/images
%{_datadir}/velum/images/*
%dir %{_datadir}/velum/static-pages
%{_datadir}/velum/static-pages/*

%if 0%{?suse_version} < 1500
%doc LICENSE
%else
%license LICENSE
%endif

%changelog
