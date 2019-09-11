#
# spec file for package nodejs-emojione
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _name emojione
%define include_android 0
%define include_ios 0

Name:           nodejs-%{_name}
Version:        3.1.2
Release:        0
Summary:        A set of emojis designed for the web
# Artwork included is in CC-BY-SA license
# Non-Artwork files are under MIT license
License:        MIT AND CC-BY-4.0
Group:          Development/Languages/NodeJS
URL:            https://github.com/Ranks/emojione
Source0:        https://github.com/Ranks/emojione/archive/%{version}/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  nodejs-packaging
%if 0%{?suse_version} >= 1316
BuildRequires:  nodejs-devel
%else
BuildRequires:  nodejs6-devel
BuildRequires:  npm
%endif
BuildRequires:  fdupes
BuildRequires:  python3
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
EmojiOne is a set of emojis designed for the web. It includes
libraries to convert Unicode characters to shortnames (like ":smile:")
and shortnames to our custom emoji images. PNG and SVG formats provided
for the emoji images.

%package demo
Summary:        EmojiOne Demos
Group:          Development/Languages/NodeJS
Requires:       %{name} = %{version}

%description demo
The following demos are provided to show how to use EmojiOne.

%if %{include_android}
%package android
Summary:        EmojiOne utility for Android
Group:          Development/Languages/NodeJS
Requires:       %{name} = %{version}
%if 0%{suse_version} > 1316
Requires:       npm6
%endif

%description android
This utility provides a method to convert from shortname to Unicode characters.
%endif

%package awesome
Summary:        Emojione templates
Group:          Development/Languages/NodeJS
Requires:       %{name} = %{version}

%description awesome
EmojiOne Awesome is for front-end developers who want to drop an emoji onto a
page without using any sorts of scripts. 


%package meteor
Summary:        EmojiOne utility for Meteor
Group:          Development/Languages/NodeJS
Requires:       %{name} = %{version}

%description meteor
This utility provides a method to convert from shortname to Unicode characters.

%package swift
Summary:        EmojiOne utility for swift
Group:          Development/Languages/NodeJS
Requires:       %{name} = %{version}

%description swift
This utility provides a method to convert from shortname to Unicode characters.

%if %{include_ios}
%package ios
Summary:        EmojiOne utility for iOS
Group:          Development/Languages/NodeJS
Requires:       %{name} = %{version}
%if 0%{suse_version} > 1316
Requires:       npm6
%endif

%description ios
EmojiOne utility is for iOS.

%package ios-devel
Summary:        Development tools for nodejs-emojione-ios
Group:          Development/Languages/NodeJS
Requires:       %{name} = %{version}

%description ios-devel
The nodejs-emojione-ios-devel package contains the header files and developer
docs for nodejs-emojione-ios.
%endif

%package python
Summary:        EmojiOne utility for Python
Group:          Development/Languages/NodeJS
Requires:       %{name} = %{version}
Requires:       python3

%description python
EmojiOne utility is for Python.

%prep
%setup -q -n %{_name}-%{version}
chmod a+x lib/python/emojipy/*.py
find . -name "*.js" -exec chmod 0644 {} +
find . -name "*.svg" -exec chmod 0644 {} +
find . -name "*.py" -exec sed -i 's|#!/usr/bin/env python|#!/usr/bin/python|g' {} \;
sed -i '1i\#!/usr/bin/python3' lib/python/emojipy/emojipy.py lib/python/emojipy/__init__.py

%build

%install
# Use cp instead of macro, It would run a wrong installing.
mkdir -p %{buildroot}%{nodejs_sitelib}/%{_name}
cp -R * %{buildroot}%{nodejs_sitelib}/%{_name}

find %{buildroot}%{nodejs_sitelib} -name "*.md" -exec rm -rf {} +
find %{buildroot}%{nodejs_sitelib} -name ".gitignore" -exec rm -rf {} +

%if !0%{include_android}
rm -rf %{buildroot}%{nodejs_sitelib}/%{_name}/lib/android
%endif

%if !0%{include_ios}
rm -rf %{buildroot}%{nodejs_sitelib}/%{_name}/lib/ios
%endif

# https://github.com/Ranks/emojione/issues/295
rm -rf %{buildroot}%{nodejs_sitelib}/%{_name}/assets/fonts

%fdupes %{buildroot}/%{nodejs_sitelib}

%files
%defattr(-,root,root,-)
%license LICENSE.md
%doc CONTRIBUTING.md README.md INSTALLATION.md UPGRADE.md USAGE.md
%dir %{nodejs_sitelib}
%dir %{nodejs_sitelib}/%{_name}/
%dir %{nodejs_sitelib}/%{_name}/lib
%dir %{nodejs_sitelib}/%{_name}/lib/php
%dir %{nodejs_sitelib}/%{_name}/lib/php/src
%dir %{nodejs_sitelib}/%{_name}/lib/php/test
%{nodejs_sitelib}/%{_name}/*.json
%{nodejs_sitelib}/%{_name}/*.js
%{nodejs_sitelib}/%{_name}/extras
%{nodejs_sitelib}/%{_name}/lib/js
%{nodejs_sitelib}/%{_name}/lib/php/phpunit.xml.dist
%{nodejs_sitelib}/%{_name}/lib/php/autoload.php
%{nodejs_sitelib}/%{_name}/lib/php/src/*.php
%{nodejs_sitelib}/%{_name}/lib/php/test/*.php

%files demo
%defattr(-,root,root,-)
%{nodejs_sitelib}/%{_name}/examples

%if %{include_android}
%files android
%defattr(-,root,root,-)
%doc lib/android/README.md
%{nodejs_sitelib}/%{_name}/lib/android
%endif

%files awesome
%defattr(-,root,root,-)
%doc lib/emojione-awesome/README.md
%{nodejs_sitelib}/%{_name}/lib/emojione-awesome

%files meteor
%defattr(-,root,root,-)
%{nodejs_sitelib}/%{_name}/lib/meteor

%files swift
%defattr(-,root,root,-)
%doc lib/swift/README.md
%{nodejs_sitelib}/%{_name}/lib/swift

%if %{include_ios}
%files ios
%defattr(-,root,root,-)
%doc lib/ios/README.md
%{nodejs_sitelib}/%{_name}/lib/ios
%exclude %{nodejs_sitelib}/%{_name}/lib/ios/src

%files ios-devel
%defattr(-,root,root,-)
%{nodejs_sitelib}/%{_name}/lib/ios/src
%endif

%files python
%defattr(-,root,root,-)
%doc lib/python/README.md
%{nodejs_sitelib}/%{_name}/lib/python

%changelog
