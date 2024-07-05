#
# spec file for package playwright
#
# Copyright (c) 2023 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           playwright
Version:        1.32.1
Release:        0
Summary:        Playwright enables reliable end-to-end testing for modern web apps
License:        Apache-2.0
Group:          Development/Languages/NodeJS
Url:            https://playwright.dev/
Source0:        %{name}.json
Source1:	https://registry.npmjs.org/playwright-core/-/playwright-core-1.32.1.tgz
Source2:	https://registry.npmjs.org/playwright/-/playwright-1.32.1.tgz
Source3:        https://registry.npmjs.org/@playwright/test/-/test-1.32.1.tgz
Source10:       playwright.sh
BuildRequires:	fdupes
BuildRequires:  nodejs-packaging
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%{nodejs_find_provides_and_requires}

%description
Playwright was created specifically to accommodate the needs of end-to-end
testing. Playwright supports all modern rendering engines including Chromium,
WebKit, and Firefox. Test on Windows, Linux, and macOS, locally or on CI,
headless or headed with native mobile emulation of Google Chrome for Android
and Mobile Safari.

%prep
%nodejs_prep

%build
# nothing to do

%install
echo %{_sourcedir}
# set UTF-8 environment to avoid "invalid byte sequence in US-ASCII" errors
export LC_ALL=C.UTF-8
%nodejs_mkdir
%nodejs_copy

# install the @playwright/test manually
mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}/node_modules/@playwright/test
cp -aR %{_sourcedir}/test-%{version}/* %{buildroot}%{nodejs_sitelib}/%{name}/node_modules/@playwright/test

%nodejs_build
%nodejs_clean
%nodejs_filelist

%nodejs_fixdep --drop playwright-core --drop @types/node
%nodejs_fixdep --drop @types/node

mkdir -p %{buildroot}%{_bindir}
cp %{SOURCE10} %{buildroot}%{_bindir}/playwright
chmod +x %{buildroot}%{_bindir}/playwright
#ln -sf %{nodejs_sitelib}/%{name}/cli.js %{buildroot}%{_bindir}/playwright
#chmod +x %{buildroot}%{nodejs_sitelib}/%{name}/cli.js

%fdupes %{buildroot}

%files -f %{_sourcedir}/files.lst
%defattr(-,root,root,-)
%dir /usr/lib/node_modules
%{_bindir}/playwright

%changelog
