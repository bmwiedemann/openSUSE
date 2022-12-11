#
# spec file
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2018-2022 Dr. Axel Braun
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
Version:        2.6
Release:        0
Summary:        Self-hosting Tor Onion Service based file sharing
License:        GPL-3.0-or-later
Group:          Productivity/Networking/File-Sharing
URL:            https://github.com/onionshare/onionshare
Source0:        https://github.com/onionshare/onionshare/archive/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE skip test_large_download in gui tests
Patch0:         0001-adjust_tests.diff
# PATCH-FIX-UPSTREAM fix-test-cli-web.patch -- https://github.com/onionshare/onionshare/issues/1534
Patch1:         fix-test-cli-web.patch
# PATCH-FIX-OPENSUSE relax-async-mode.patch -- Do not rely on gevent
Patch2:         relax-async-mode.patch
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Flask >= 1.4.1
BuildRequires:  python3-Flask-SocketIO >= 5.0.1
BuildRequires:  python3-PyNaCl
BuildRequires:  python3-PySocks
BuildRequires:  python3-Unidecode
BuildRequires:  python3-cepa >= 1.8.3
BuildRequires:  python3-colorama
BuildRequires:  python3-eventlet
BuildRequires:  python3-poetry
BuildRequires:  python3-psutil
BuildRequires:  python3-pyside2 >= 5.15.2
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-qt
BuildRequires:  python3-pytest-xvfb
BuildRequires:  python3-qrcode
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python3-urllib3
BuildRequires:  tor
BuildRequires:  update-desktop-files
Requires:       python3-Flask >= 1.4.1
Requires:       python3-Flask-SocketIO >= 5.0.1
Requires:       python3-PyNaCl
Requires:       python3-PySocks
Requires:       python3-Unidecode
Requires:       python3-cepa >= 1.8.3
Requires:       python3-colorama
Requires:       python3-eventlet
Requires:       python3-psutil
Requires:       python3-pyside2 >= 5.15.2
Requires:       python3-qrcode
Requires:       python3-requests
Requires:       python3-urllib3
Requires:       tor
Provides:       %{name}-%{version}
Obsoletes:      %{name}-data < %{version}
Obsoletes:      python310-onionshare < %{version}
Obsoletes:      python36-onionshare < %{version}
Obsoletes:      python38-onionshare < %{version}
Obsoletes:      python39-onionshare < %{version}
BuildArch:      noarch

%description
OnionShare lets the user share files securely and anonymously. It
works by starting a web server, making it accessible as a Tor Onion
Service, and generating an unguessable URL to access and download the
files. It does not require setting up a separate server or using a
third party file-sharing service. Files are hosted on the machine the
program is run on. The receiving user just needs to open the URL in
Tor Browser to download the file.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
pushd cli
%python3_build
popd
pushd desktop
%python3_build

%install
pushd cli
%python3_install
popd
pushd desktop
%python3_install

install -Dm 0644 org.onionshare.OnionShare.appdata.xml \
  %{buildroot}%{_datadir}/metainfo/org.onionshare.OnionShare.metainfo.xml
install -Dm 0644 org.onionshare.OnionShare.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/org.onionshare.OnionShare.svg
%suse_update_desktop_file -i org.onionshare.OnionShare

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

#Desktop tests disabled. The 'server' tests seem to fail
# pushd desktop
# the gui test files need to be called separately upstream's way for application setup and teardown in between
# this script calls pytest from the PATH defined above.
# ./tests/run.sh
# popd

%files
%{_bindir}/%{modname}
%{_bindir}/%{modname}-cli
%license LICENSE
%doc README.md
%{_datadir}/applications/org.onionshare.OnionShare.desktop
%{_datadir}/metainfo/org.onionshare.OnionShare.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/org.onionshare.OnionShare.svg
%{python3_sitelib}/onionshare
%{python3_sitelib}/onionshare-%{version}*-info
%{python3_sitelib}/onionshare_cli
%{python3_sitelib}/onionshare_cli-%{version}*-info

%changelog
