#
# spec file for package transifex-client
#
# Copyright (c) 2020 SUSE LLC
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


Name:           transifex-client
Version:        0.13.9
Release:        0
Summary:        Transifex Command-line Client
License:        GPL-2.0-only
Group:          Productivity/Text/Utilities
URL:            https://github.com/transifex/transifex-client
Source:         https://github.com/transifex/transifex-client/archive/%{version}.tar.gz
BuildRequires:  python3-mock
BuildRequires:  python3-mock >= 3.0.5
BuildRequires:  python3-python-slugify
BuildRequires:  python3-requests >= 2.19.1
BuildRequires:  python3-setuptools
BuildRequires:  python3-urllib3 >= 1.24.2
Requires:       python3-python-slugify
Requires:       python3-requests >= 2.19.1
Requires:       python3-setuptools
Requires:       python3-urllib3 >= 1.24.2
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
sed -i -e "s/slugify<.*/slugify/" requirements.txt
sed -i -e "s/mock>=3.0.5,<4.0/mock>=3.0.5/" setup.py
sed -i -e '1{\,^#!/usr/bin/env python,d}' txclib/cmdline.py

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
# remove pem file
rm %{buildroot}/%{python3_sitelib}/txclib/cacert.pem

mv %{buildroot}%{_bindir}/tx %{buildroot}%{_bindir}/transifex-tx
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
ln -s -f %{_sysconfdir}/alternatives/tx %{buildroot}%{_bindir}/tx

%check
python3 setup.py test

%post
%{_sbindir}/update-alternatives --install %{_bindir}/tx tx %{_bindir}/transifex-tx 20

%postun
if [ ! -e %{_bindir}/transifex-tx ] ; then
  %{_sbindir}/update-alternatives --remove tx %{_bindir}/transifex-tx
fi

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%ghost %{_sysconfdir}/alternatives/tx
%{_bindir}/transifex-tx
%{_bindir}/tx
%{python3_sitelib}/*

%changelog
