#
# spec file for package asar
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           asar
Version:        3.2.17
Release:        0
Summary:        Creating atom-shell (electron) app packages
License:        MIT and ISC
Group:          Development/Languages/NodeJS
Url:            https://github.com/electron/asar
Source0:        https://github.com/electron/asar/archive/refs/tags/v%{version}.tar.gz
# Created by prepare-vendor.sh
Source1:        vendor.tar.zst
Source2:        prepare_vendor.sh

BuildArch:      noarch

BuildRequires:  fdupes
BuildRequires:  jq
BuildRequires:  nodejs-packaging
%if 0%{?fedora} >= 37
BuildRequires:  nodejs-npm
%else
BuildRequires:  npm
%endif
BuildRequires:  typescript
BuildRequires:  zstd

%global __requires_exclude ^npm(.*)$
Provides: nodejs-asar = %{version}
%description
Asar is a simple extensive archive format, it works like tar
that concatenates all files together without compression, while
having random access support.


%prep
%autosetup -p1 -a 1
# Use system typescript for building
rm -rf node_modules/typescript
rm -v node_modules/.bin/ts{c,server}

%build
export ELECTRON_SKIP_BINARY_DOWNLOAD=1
npm rebuild --verbose --foreground-scripts
# tsc may return a non-zero exit code due to type warnings despite actually succesfully compiling the code.
# If it fails to compile, it will be catched anyway in #check.
tsc --removeComments --sourceMap false || true

%install
mkdir -pv %{buildroot}%{nodejs_sitelib}/@electron
mkdir -pv %{buildroot}%{_bindir}
cp -lr . %{buildroot}%{nodejs_sitelib}/@electron/asar
ln -srv %{buildroot}%{nodejs_sitelib}/@electron/asar/bin/asar.js %{buildroot}%{_bindir}/asar
# symlink old package name
ln -srv %{buildroot}%{nodejs_sitelib}/{@electron/,}asar
#fix shebang
sed -i '1s/env //' %{buildroot}%{nodejs_sitelib}/@electron/asar/bin/asar.js
cd %{buildroot}%{nodejs_sitelib}/asar

# Correct bogus version in package.json
jq -cj '.version="%{version}"' package.json > new

#remove devdependencies
jq -cj 'del(.devDependencies)' package.json > tmp
mv -v tmp package.json
npm prune --omit=dev --verbose --ignore-scripts

mv -v new package.json


#Remove development garbage
find -name example -print0 |xargs -r0 -- rm -rvf
find -name test -print0 |xargs -r0 -- rm -rvf
find -name typings -print0 |xargs -r0 -- rm -rvf
find -name @types -print0 |xargs -r0 -- rm -rvf
find -name .github -print0 |xargs -r0 -- rm -rvf
find -name .circleci -print0 |xargs -r0 -- rm -rvf
find -name '*.md' -type f -print -delete
find -name '*.markdown' -type f -print -delete
find -name '*.ts' -type f -print -delete
find -name '.*.yml' -type f -print -delete
find -name '.*ignore' -type f -print -delete
find -name 'snapcraft*' -type f -print -delete
find -name '.git*' -type f -print -delete
find -name yarn.lock -type f -print -delete
find -name '.yarn*' -type f -print -delete
find -name '*package-lock.json' -type f -print -delete
find -name '.prettierrc*' -type f -print -delete
find -name '.releaserc*' -type f -print -delete
find -name tsconfig.json -type f -print -delete

# Remove empty directories
find . -type d -empty -print -delete

%fdupes %{buildroot}

%check
pushd %{buildroot}%{nodejs_sitelib}/asar
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Node.js/#_build_testing_in_check
%{__nodejs} -e 'require("./")'

#check that the executable starts
./bin/asar.js -h
popd

#the actual test suite 
npx mocha -- --reporter spec --timeout 10000

%files
%defattr(-,root,root)
%doc CHANGELOG.md README.md
%license LICENSE.md
%{_bindir}/asar
%{nodejs_sitelib}

%changelog
