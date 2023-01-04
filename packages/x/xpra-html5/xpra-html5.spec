#
# spec file for package xpra-html5
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


%define uglifyjs_version 3.17.4
%define minifier uglifyjs
%define python python3

Name:           xpra-html5
Release:        0
Version:        7.0+git20221227.017148e
Summary:        HTML5 client for Xpra
License:        GPL-2.0+ AND BSD-3-Clause AND LGPL-3.0+ AND MIT
URL:            https://xpra.org/
Source0:        xpra-html5-%{version}.tar.gz
### To update UglifyJS using npm release:
###   npm pack uglify-js
### To update UglifyJS using github release:
###   osc service runall download_files
#Source1:        https://registry.npmjs.org/uglify-js/-/uglify-js-%%{uglifyjs_ver}.tgz#/uglify-js-%%{uglifyjs_version}.tgz
Source1:        https://github.com/mishoo/UglifyJS/archive/refs/tags/v%{uglifyjs_version}.tar.gz#/uglify-js-%{uglifyjs_version}.tar.gz
#####
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  nodejs-common
BuildRequires:  python3
Requires:       cups-client
Requires:       dejavu-fonts
Requires:       qrencode
Requires:       xpra
Requires:       python3-avahi
Requires:       python3-netifaces
Requires:       python3-paramiko
Requires:       python3-pyinotify
Requires:       python3-pyxdg
Requires:       python3-websockify
Requires:       python3-zeroconf
Provides:       bundled(js-aurora)
Provides:       bundled(js-bencode)
Provides:       bundled(js-broadway)
Provides:       bundled(js-forge)
Provides:       bundled(js-jquery) = 3.1.1
Provides:       bundled(js-jquery-ui) = 1.12.1
Provides:       bundled(js-lz4)
Provides:       bundled(js-zlib)
BuildArch:      noarch
ExcludeArch:    %ix86

%description
This is the HTML5 client for Xpra,
which can be made available for browsers by the xpra server
or by any other web server.

%prep
%setup -q -a 1

%build
### intentionally left empty.

%install

### Debug info for proper uglifyjs setup
echo -e "\nUGLIFYJS -check1 :: $(which uglifyjs)\n"
echo -e "\nPATH: '$PATH'\n"
echo -e "\nPWD: '$(pwd)'\n"
echo -e "%{name} :: %{version}"
find . -iname uglifyjs -exec ls -ld {} \;
### Using npm download
#export PATH=$PATH:$(pwd)/package/bin
#chmod -v 755 %%{_builddir}/%%{name}-%%{version}/package/bin/uglifyjs
#ls -l %%{_builddir}/%%{name}-%%{version}/package/bin
#####
export PATH=$PATH:$(pwd)/UglifyJS-%{uglifyjs_version}/bin
chmod -v 755 %{_builddir}/%{name}-%{version}/UglifyJS-%{uglifyjs_version}/bin/uglifyjs
ls -l %{_builddir}/%{name}-%{version}/UglifyJS-%{uglifyjs_version}/bin
find . -iname uglifyjs -exec ls -ld {} \;
echo -e "\nUGLIFYJS -check2 :: $(which uglifyjs)\n"
#####

mkdir -p %{buildroot}%{_datadir}/xpra/www/js/lib
mkdir -p %{buildroot}%{_sysconfdir}/xpra/html5-client
%{python} ./setup.py install %{buildroot} %{_datadir}/xpra/www/ %{_sysconfdir}/xpra/html5-client %{minifier}
# Ensure there are no executable files:
find %{buildroot}%{_datadir}/xpra/www/ -type f -exec chmod 0644 {} \;
mkdir -p %{buildroot}/usr/share/doc/xpra-html5/

%fdupes -s %{buildroot}

%files
%dir %{_sysconfdir}/xpra
%{_sysconfdir}/xpra/html5-client
%config %{_sysconfdir}/xpra/html5-client/default-settings.txt
%{_datadir}/xpra
%{_datadir}/xpra/www

%changelog

