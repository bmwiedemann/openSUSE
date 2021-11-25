#
# spec file for package icinga-php-common
#
# Copyright (c) 2021 SUSE LLC
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


%global revision 1
%global basedir %{_datadir}/icinga-php
Name:           icinga-php-common
Version:        1.0.0
Release:        %{revision}%{?dist}
Summary:        Icinga PHP Common for Icinga Web 2
License:        SUSE-Public-Domain
Group:          System/Monitoring
URL:            https://icinga.com
BuildArch:      noarch

%description
This package manages the directory %{_datadir}/icinga-php.

%install
mkdir -vp %{buildroot}%{basedir}

%files
%{basedir}

%changelog
