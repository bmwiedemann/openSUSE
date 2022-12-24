#
# spec file for package nodejs-underscore
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


%define _name underscore
%if 0%{?suse_version} == 1315
%define nodejs_modulesdir /usr/lib/node_modules
%endif

Name:           nodejs-underscore
Version:        1.13.6
Release:        0
Summary:        A utility belt library for JavaScript
License:        MIT
Group:          Development/Languages/NodeJS
URL:            https://github.com/jashkenas/underscore
Source0:        https://github.com/jashkenas/underscore/archive/%{version}/%{_name}-%{version}.tar.gz
BuildArch:      noarch
%if 0%{?suse_version} < 1315 || 0%{?suse_version} > 1315
BuildRequires:  nodejs-packaging
%endif
BuildRequires:  fdupes
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?nodejs_requires}

%description
Underscore.js is a utility belt library for JavaScript that provides support
for the usual functional suspects (each, map, reduce, filter...) without
extending any core JavaScript objects.

%prep
%setup -q -n %{_name}-%{version}

%build

%install
mkdir -p %{buildroot}%{nodejs_modulesdir}/%{_name}
cp -R * %{buildroot}%{nodejs_modulesdir}/%{_name}

rm -rf %{buildroot}%{nodejs_modulesdir}/underscore/test/.eslintrc

%fdupes %{buildroot}/%{nodejs_modulesdir}

%files
%defattr(-,root,root,-)
%doc CONTRIBUTING.md README.md
%license LICENSE
%dir %{nodejs_modulesdir}
%{nodejs_modulesdir}/%{_name}

%changelog
