#
# spec file for package typescript
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


Name:           typescript
Version:        5.5.3
Release:        0
Summary:        A language for application scale JavaScript development
License:        Apache-2.0
Group:          Development/Libraries/Other
URL:            http://typescriptlang.org/
Source0:        https://github.com/microsoft/TypeScript/releases/download/v%{version}/%{name}-%{version}.tgz
BuildRequires:  fdupes
BuildRequires:  nodejs-packaging
BuildArch:      noarch
%{?nodejs_requires}

%description
TypeScript is a language for application-scale JavaScript. TypeScript adds
optional types, classes, and modules to JavaScript. TypeScript supports tools
for large-scale JavaScript applications for any browser, for any host, on any
OS. TypeScript compiles to readable, standards-based JavaScript.

%prep
%autosetup -n package

sed -i 's/\r$//' ThirdPartyNoticeText.txt
sed -i 's/\r$//' README.md
sed -i 's/\r$//' LICENSE.txt

%build

%install
%nodejs_install

# Fix shebang lines
for file in %{buildroot}%{_bindir}/ts* ; do
    sed -i -e "s|#!%{_bindir}/env node|#!%{_bindir}/node|" $(readlink -f $file)
done

%fdupes %{buildroot}

%files
%license LICENSE.txt ThirdPartyNoticeText.txt
%doc README.md
%dir %{nodejs_sitelib}
%{nodejs_sitelib}/%{name}
%{_bindir}/tsc
%{_bindir}/tsserver

%changelog
