#
# spec file for package transifex-client
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           transifex-client
Version:        0.12.4
Release:        0
Summary:        Transifex Command-line Client
License:        GPL-2.0
Group:          Productivity/Text/Utilities
Url:            https://github.com/transifex/transifex-client
Source:         https://github.com/transifex/transifex-client/archive/%{version}.tar.gz
BuildRequires:  python3-mock
BuildRequires:  python3-setuptools
BuildRequires:  python3-urllib3
Requires:       python3-setuptools
Requires:       python3-urllib3
BuildArch:      noarch

%description
The Transifex Command-line Client is a command line tool that enables you
to easily manage your translations within a project without the need of
an elaborate UI system.

You can use the command-line client to easily create new resources, map
locale files to translations and synchronize your Transifex project with
your local repository and vice verca. Translators and localization
managers can also use it to handle large volumes of translation files
easily and without much hassle.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
# remove pem file
rm %{buildroot}/%{python3_sitelib}/txclib/cacert.pem

%check
python3 setup.py test

%files
%defattr(-,root,root)
%doc README.md LICENSE
%{_bindir}/tx
%{python3_sitelib}/*

%changelog
