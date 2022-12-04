#
# spec file for package python-plaster-pastedeploy
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-plaster-pastedeploy
Version:        1.0.1
Release:        0
Summary:        A loader implementing the PasteDeploy syntax to be used by plaster
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Pylons/plaster_pastedeploy
Source0:        https://files.pythonhosted.org/packages/source/p/plaster_pastedeploy/plaster_pastedeploy-%{version}.tar.gz
BuildRequires:  %{python_module PasteDeploy >= 2.0}
BuildRequires:  %{python_module plaster >= 0.5}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PasteDeploy >= 2.0
Requires:       python-plaster >= 0.5
Provides:       python-plaster_pastedeploy = %{version}
BuildArch:      noarch
%python_subpackages

%description
plaster_pastedeploy is a plaster plugin that provides a plaster.Loader
that can parse ini files according to the standard set by PasteDeploy.
It supports the wsgi plaster protocol, implementing the
plaster.protocols.IWSGIProtocol interface.

%prep
%setup -q -n plaster_pastedeploy-%{version}
rm -rf src/plaster_pastedeploy.egg-info

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
