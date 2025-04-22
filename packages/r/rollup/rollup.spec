#
# spec file for package rollup
#
# Copyright (c) 2025 SUSE LLC
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


Name:           rollup
Version:        3.29.4
Release:        0
Summary:        Module bundler for JavaScript
License:        BSD-2-Clause
URL:            https://github.com/rollup/rollup
Source:         https://registry.npmjs.org/rollup/-/rollup-3.29.4.tgz
Provides:       nodejs-rollup
BuildRequires:  nodejs
BuildRequires:  nodejs-packaging
BuildArch:      noarch

%description
Rollup is a module bundler for JavaScript which compiles small pieces of code into
something larger and more complex, such as a library or application.
It uses the standardized ES module format for code, instead of previous idiosyncratic
solutions such as CommonJS and AMD. ES modules let you freely and seamlessly combine
the most useful individual functions from your favorite libraries.
Rollup can optimize ES modules for faster native loading in modern browsers,
or output a legacy module format allowing ES module workflows today.

%prep
%autosetup -n package


%install
mkdir -pv %{buildroot}%{nodejs_sitelib}/rollup
cp -alr . %{buildroot}%{nodejs_sitelib}/rollup
install -D -d -m 0755              %{buildroot}%{_datadir}/yarn/ %{buildroot}%{_bindir}
#fix shebang
sed -i '1s/env //' %{buildroot}%{nodejs_sitelib}/rollup/dist/bin/rollup
ln -srv %{buildroot}%{nodejs_sitelib}/rollup/dist/bin/rollup %{buildroot}%{_bindir}/rollup


%files
%dir %{nodejs_sitelib}
%{nodejs_sitelib}/rollup
%{_bindir}/rollup

%changelog
