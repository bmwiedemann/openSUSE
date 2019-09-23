#
# spec file for package urlwatch
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           urlwatch
Version:        2.17
Release:        0
Summary:        A tool for monitoring webpages for updates
License:        BSD-3-Clause
Group:          Productivity/Networking/Web/Utilities
Url:            https://thp.io/2008/urlwatch/
Source0:        https://github.com/thp/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  python-futures
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python-keyring
Requires:       python3-PyYAML
Requires:       python3-appdirs
Requires:       python3-lxml
Requires:       python3-minidb
Requires:       python3-requests
BuildArch:      noarch
Requires:       python-futures

%description
urlwatch is intended to help you watch changes in webpages and get
notified (via email, in your terminal or with a custom-written
reporter class) of any changes. The change notification will include
the URL that has changed and a unified diff of what has changed.


A default config is ~/.urlwatch/urlwatch.yaml.
use "urlwatch --edit-config" to customize it.

You need to create ~/.urlwatch/urls.yaml in order to use urlwatch.
Use "urlwatch --edit" to open the file with your editor.

Please look in

 /usr/share/doc/packages/urlwatch/README.md

 TIPS AND TRICKS what to use in urls.yaml.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGELOG* README*
%license COPYING*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{py3_ver}.egg-info
%{_datadir}/%{name}

%changelog
