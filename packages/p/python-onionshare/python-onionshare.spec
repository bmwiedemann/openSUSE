#
# spec file for package python-onionshare
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2018-2024 Dr. Axel Braun
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


# Always only build one flavor
%if 0%{?suse_version} >= 1550
%define pythons python3
%else
%{?sle15_python_module_pythons}
%endif
%global mypython %pythons
%global mysitelib %{expand:%%{%{mypython}_sitelib}}
%define plainpython python

Name:           python-onionshare
Version:        2.6.2
Release:        0
Summary:        Self-hosting Tor Onion Service based file sharing
License:        GPL-3.0-or-later
Group:          Productivity/Networking/File-Sharing
URL:            https://github.com/onionshare/onionshare
Source0:        https://github.com/onionshare/onionshare/archive/v%{version}.tar.gz#/onionshare-%{version}.tar.gz
Source99:       python-onionshare.rpmlintrc
# PATCH-FIX-OPENSUSE skip test_large_download in gui tests
Patch0:         0001-adjust_tests.diff
# PATCH-FIX-OPENSUSE relax-async-mode.patch -- Do not rely on gevent
Patch1:         relax-async-mode.patch
BuildRequires:  %{mypython}-devel >= 3.8
BuildRequires:  %{mypython}-pip
BuildRequires:  %{mypython}-setuptools
BuildRequires:  %{mypython}-wheel
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros

BuildRequires:  %{mypython}-poetry-core
BuildRequires:  update-desktop-files
# SECTION test
BuildRequires:  %{mypython}-pytest
BuildRequires:  %{mypython}-pytest-qt
BuildRequires:  %{mypython}-pytest-xvfb
# /SECTION
# SECTION runtime test
BuildRequires:  %{mypython}-Cython >= 3.0.2
BuildRequires:  %{mypython}-Flask >= 2.3.2
BuildRequires:  %{mypython}-Flask-Compress >= 1.13
BuildRequires:  %{mypython}-Flask-SocketIO >= 5.3.4
BuildRequires:  %{mypython}-PyNaCl
BuildRequires:  %{mypython}-PySocks
BuildRequires:  %{mypython}-Unidecode
BuildRequires:  %{mypython}-Werkzeug >= 2.3.4
BuildRequires:  %{mypython}-cepa
BuildRequires:  %{mypython}-click
BuildRequires:  %{mypython}-colorama
BuildRequires:  %{mypython}-eventlet
BuildRequires:  %{mypython}-gevent >= 23.9.1
BuildRequires:  %{mypython}-gevent-websocket
BuildRequires:  %{mypython}-packaging >= 23.1
BuildRequires:  %{mypython}-psutil
BuildRequires:  %{mypython}-pyside6 >= 6.5.2
BuildRequires:  %{mypython}-python-gnupg
BuildRequires:  %{mypython}-qrcode
BuildRequires:  %{mypython}-requests
BuildRequires:  %{mypython}-urllib3
BuildRequires:  %{mypython}-waitress >= 2.1.2
BuildRequires:  tor
# /SECTION
Requires:       python-Cython >= 3.0.2
Requires:       python-Flask >= 2.3.2
Requires:       python-Flask-Compress >= 1.13
Requires:       python-Flask-SocketIO >= 5.3.4
Requires:       python-PyNaCl
Requires:       python-PySocks
Requires:       python-Unidecode
Requires:       python-Werkzeug >= 2.3.4
Requires:       python-cepa >= 1.8.1
Requires:       python-click
Requires:       python-colorama
Requires:       python-eventlet
Requires:       python-gevent >= 23.9.1
Requires:       python-gevent-websocket
Requires:       python-packaging >= 23.1
Requires:       python-psutil
Requires:       python-pyside6 >= 6.5.2
Requires:       python-python-gnupg
Requires:       python-qrcode
Requires:       python-requests
Requires:       python-setuptools
Requires:       python-urllib3
Requires:       python-waitress >= 2.1.2
Requires:       python-wheel >= 0.41.2
Requires:       tor
Provides:       python-onionshare = %{version}-%{release}
Provides:       python-onionshare_cli = %{version}-%{release}
# Obsolete old multiflavor packages
Obsoletes:      %{plainpython}-onionshare-data < 2.3.1
Obsoletes:      python310-onionshare < 2.3.1
Obsoletes:      python36-onionshare < 2.3.1
Obsoletes:      python38-onionshare < 2.3.1
Obsoletes:      python39-onionshare < 2.3.1
%if %{suse_version} >= 1500
# incorrect package name was used until 2024-01-24
Obsoletes:      %{plainpython}-onionshare <= 2.6
%endif
%if 0%{?sle_version} >= 150600 && "%pythons" != "python3"
# obsolete python 3.6 package
Obsoletes:      python3-onionshare <= 2.6
%endif
BuildArch:      noarch
%python_subpackages

%description
OnionShare lets the user share files securely and anonymously. It
works by starting a web server, making it accessible as a Tor Onion
Service, and generating an unguessable URL to access and download the
files. It does not require setting up a separate server or using a
third party file-sharing service. Files are hosted on the machine the
program is run on. The receiving user just needs to open the URL in
Tor Browser to download the file.

%prep
%autosetup -p1 -n onionshare-%{version}

%build
pushd cli
%pyproject_wheel
popd
pushd desktop
%pyproject_wheel

%install
pushd cli
%pyproject_install
popd
pushd desktop
%pyproject_install

install -Dm 0644 org.onionshare.OnionShare.appdata.xml \
  %{buildroot}%{_datadir}/metainfo/org.onionshare.OnionShare.metainfo.xml
install -Dm 0644 org.onionshare.OnionShare.svg \
  %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/org.onionshare.OnionShare.svg
%suse_update_desktop_file -i org.onionshare.OnionShare

%fdupes %{buildroot}%{mysitelib}

%check
export PYTHONPATH=%{buildroot}%{mysitelib}
# we don't trust the update-alternatives priority: pytest could point to the wrong python3 flavor.
# (https://github.com/openSUSE/python-rpm-macros/issues/109)
mkdir testbin
ln -s %{_bindir}/pytest-%{%{mypython}_bin_suffix} testbin/pytest
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

%files %python_files
%{_bindir}/onionshare
%{_bindir}/onionshare-cli
%license LICENSE.txt
%doc README.md
%{_datadir}/applications/org.onionshare.OnionShare.desktop
%{_datadir}/metainfo/org.onionshare.OnionShare.metainfo.xml
%{_datadir}/icons/hicolor/scalable/apps/org.onionshare.OnionShare.svg
%{mysitelib}/onionshare
%{mysitelib}/onionshare-%{version}*-info
%{mysitelib}/onionshare_cli
%{mysitelib}/onionshare_cli-%{version}*-info

%changelog
