#
# spec file for package python-hawkauthlib
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define pyname hawkauthlib
Name:           python-hawkauthlib
Version:        2.0.0
Release:        0
Summary:        Hawk Access Authentication protocol
License:        MPL-2.0
Group:          Development/Languages/Python
URL:            https://github.com/mozilla-services/hawkauthlib
Source0:        https://github.com/mozilla-services/hawkauthlib/archive/v%{version}.tar.gz
# Add MPL-2.0 License text directly from MPL upstream, since it is not included in package tarball
Source1:        https://www.mozilla.org/media/MPL/2.0/index.txt
BuildRequires:  %{python_module WebOb}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-WebOb
Suggests:       python-requests
BuildArch:      noarch
%python_subpackages

%description
hawkauthlib is a low-level library for implementing Hawk Access Authentication, a
simple HTTP request-signing scheme described in:https://npmjs.org/package/hawk

%prep
%setup -q -n hawkauthlib-%{version}

%build
%python_build
cp %{S:1} LICENSE

%install
%python_install

%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc CHANGES.txt README.rst
%{python_sitelib}/%{pyname}
%{python_sitelib}/%{pyname}-%{version}-py%{py_ver}.egg-info/

%changelog
