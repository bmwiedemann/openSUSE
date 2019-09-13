#
# spec file for package python-mygpoclient
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2010 Pascal Bleser <pascal.bleser@opensuse.org>
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
Name:           python-mygpoclient
Version:        1.8
Release:        0
Summary:        Python gpodder.net API Client Library
License:        GPL-3.0-or-later
Group:          Development/Libraries/Python
URL:            http://gpodder.org/mygpoclient
Source:         https://files.pythonhosted.org/packages/source/m/mygpoclient/mygpoclient-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-simplejson
BuildArch:      noarch
%python_subpackages

%description
The mygpoclient library allows developers to utilize a Pythonic interface to
the my.gpodder.org web services.

%prep
%setup -q -n "mygpoclient-%{version}"

%build
%python_build

%install
%python_install
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc AUTHORS
%license COPYING
%python3_only %{_bindir}/mygpo-bpsync
%python3_only %{_bindir}/mygpo-list-devices
%python3_only %{_bindir}/mygpo-simple-client
%python3_only %{_mandir}/man1/mygpo-bpsync.1%{ext_man}
%{python_sitelib}/*

%changelog
