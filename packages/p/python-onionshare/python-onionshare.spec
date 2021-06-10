#
# spec file
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2018-2021 Dr. Axel Braun
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


%define modname onionshare
Name:           python-%{modname}
Version:        2.3.2
Release:        0
Summary:        Self-hosting Tor Onion Service based file sharing
License:        GPL-3.0-or-later
Group:          Productivity/Networking/File-Sharing
URL:            https://github.com/micahflee/onionshare
Source0:        https://github.com/micahflee/onionshare/archive/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
Source1:        %{modname}.desktop
Patch0:         0001-adjust_tests.diff
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Flask
BuildRequires:  python3-Flask-HTTPAuth
BuildRequires:  python3-Flask-SocketIO
BuildRequires:  python3-PySocks
BuildRequires:  python3-Unidecode
BuildRequires:  python3-colorama
BuildRequires:  python3-nautilus
BuildRequires:  python3-psutil
BuildRequires:  python3-pycrypto
BuildRequires:  python3-pyside2
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-qt
BuildRequires:  python3-pytest-xvfb
BuildRequires:  python3-qrcode
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python3-stem
BuildRequires:  tor
BuildRequires:  update-desktop-files
Requires:       python3-Flask
Requires:       python3-Flask-HTTPAuth
Requires:       python3-Flask-SocketIO
Requires:       python3-Unidecode
Requires:       python3-colorama
Requires:       python3-psutil
Requires:       python3-pycrypto
Requires:       python3-pyside2
Requires:       python3-qrcode
Requires:       python3-requests
Requires:       python3-stem
Requires:       tor
BuildArch:      noarch

Provides:       %{name}-%{version}
Obsoletes:      %{name}-data < %{version}
Obsoletes:      python36-onionshare < %{version}
Obsoletes:      python38-onionshare < %{version}
Obsoletes:      python39-onionshare < %{version}

%description
OnionShare lets the user share files securely and anonymously. It
works by starting a web server, making it accessible as a Tor Onion
Service, and generating an unguessable URL to access and download the
files. It does not require setting up a separate server or using a
third party file-sharing service. Files are hosted on the machine the
program is run on. The receiving user just needs to open the URL in
Tor Browser to download the file.

%prep
%setup -q -n %{modname}-%{version}
%autopatch -p1
cp %{SOURCE1} .

sed -i 's/sys.platform != "Linux"/sys.platform != "linux"/' cli/tests/test_cli_settings.py cli/tests/test_cli_common.py

%build
cd cli
%python3_build
cd ../desktop/src
%python3_build

%install
cd cli
%python3_install

cd ../desktop/src
%python3_install

mkdir -p %{buildroot}%{_datadir}/pixmaps
cp org.onionshare.OnionShare.svg %{buildroot}%{_datadir}/pixmaps/.

pwd

desktop-file-install --dir %{buildroot}%{_datadir}/applications/ org.onionshare.OnionShare.desktop
%suse_update_desktop_file org.onionshare.OnionShare

%fdupes %{buildroot}%{python3_sitelib}

%check
export PYTHONPATH=%{buildroot}%{python3_sitelib}
# we don't trust the update-alternatives priority: pytest could point to the wrong python3 flavor.
# (https://github.com/openSUSE/python-rpm-macros/issues/109)
mkdir testbin
ln -s %{_bindir}/pytest-%{python3_bin_suffix} testbin/pytest
export PATH=$PWD/testbin:$PATH

pushd cli
pytest -v -k 'not test_large_download' -rs tests
popd

pushd desktop
# the gui test files need to be called separately upstream's way for application setup and teardown in between
# this script calls pytest from the PATH defined above.
./tests/run.sh
popd

%files
%{_bindir}/%{modname}
%{_bindir}/%{modname}-cli
%license LICENSE
%doc README.md
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{python3_sitelib}/onionshare
%{python3_sitelib}/onionshare-%{version}*-info
%{python3_sitelib}/onionshare_cli
%{python3_sitelib}/onionshare_cli-%{version}*-info

%changelog
