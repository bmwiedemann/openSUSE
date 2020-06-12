#
# spec file for package python-onionshare
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2018-2020 Dr. Axel Braun
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%define modname onionshare
%define oldpython python
Name:           python-%{modname}
Version:        2.2
Release:        0
Summary:        Self-hosting Tor Onion Service based file sharing
License:        GPL-3.0-or-later
URL:            https://github.com/micahflee/onionshare
Source0:        https://github.com/micahflee/onionshare/archive/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
Source1:        %{modname}.desktop
BuildRequires:  %{python_module Flask-HTTPAuth}
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module PySocks}
BuildRequires:  %{python_module nautilus}
BuildRequires:  %{python_module pycrypto}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module stem}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  update-desktop-files
Requires:       %{oldpython}-%{modname}-data
Requires:       python-Flask
Requires:       python-Flask-HTTPAuth
Requires:       python-pycrypto
Requires:       python-pytest
Requires:       python-qt5
Requires:       python-stem
Requires:       tor
Requires(post): update-alternatives
Requires(postun): update-alternatives
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

%package -n python-onionshare-data
Summary:        Self-hosting Tor Onion Service based file sharing

%description -n python-onionshare-data
OnionShare lets the user share files securely and anonymously. It
works by starting a web server, making it accessible as a Tor Onion
Service, and generating an unguessable URL to access and download the
files. It does not require setting up a separate server or using a
third party file-sharing service. Files are hosted on the machine the
program is run on. The receiving user just needs to open the URL in
Tor Browser to download the file.

%prep
%setup -q -n %{modname}-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/%{modname}
%python_clone -a %{buildroot}%{_bindir}/%{modname}-gui

mkdir -p %{buildroot}%{_datadir}/pixmaps
cp install/%{modname}80.xpm %{buildroot}%{_datadir}/pixmaps/%{modname}80.xpm

desktop-file-install --dir %{buildroot}%{_datadir}/applications/ %{modname}.desktop
%suse_update_desktop_file %{modname}

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests

%post
%python_install_alternative %{modname} %{modname}-gui

%postun
%python_uninstall_alternative %{modname}

%files %{python_files}
%python_alternative %{_bindir}/%{modname}
%python_alternative %{_bindir}/%{modname}-gui
%license LICENSE
%doc README.md
%{python_sitelib}/*

%files -n python-onionshare-data
%{_datadir}/%{modname}*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_datadir}/icons/*
%{_datadir}/metainfo/*
%{_datadir}/nautilus-python/*

%changelog
