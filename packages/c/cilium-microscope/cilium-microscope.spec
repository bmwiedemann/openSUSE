#
# spec file for package cilium-microscope
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           cilium-microscope
Version:        1.0.1
Release:        0
Summary:        Program to gather monitor data from CCilium nodes in a cluster
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            https://github.com/cilium/microscope
Source:         https://github.com/cilium/microscope/archive/%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-pip
BuildRequires:  python-setuptools
Requires:       python-PyYAML
Requires:       python-cachetools
Requires:       python-chardet
Requires:       python-google-auth
Requires:       python-idna
Requires:       python-kubernetes
Requires:       python-oauthlib
Requires:       python-pyasn1
Requires:       python-pyasn1-modules
Requires:       python-python-dateutil
Requires:       python-requests
Requires:       python-requests-oauthlib
Requires:       python-rsa
Requires:       python-urllib3
Requires:       python-urwid
Requires:       python-websocket-client
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Provides:       python-cilium-microscope = %{version}
Obsoletes:      python-cilium-microscope < %{version}
BuildArch:      noarch

%description
Cilium microscope allows you to see cilium monitor output from all
your cilium nodes. This allows you to have one simple to use command
to interact with your cilium nodes within k8s cluster.

%prep
%setup -q -n microscope-%{version}

%build
python setup.py build
python setup.py install --skip-build --prefix=%{_prefix} --root=%{buildroot} --install-data=/
cp LICENSE %{buildroot}/%{python_sitelib}/microscope/

%files
%{python_sitelib}/*
%{_bindir}/microscope
%license %{python_sitelib}/microscope/LICENSE

%changelog
