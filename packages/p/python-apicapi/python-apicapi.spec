#
# spec file for package python-apicapi
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%global  sname  apicapi
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
# package does not support python3 at all (uses iteritems/etc)
%define  skip_python3 1
Name:           python-apicapi
Version:        1.6.0
Release:        0
Summary:        Python interface to the APIC REST API
License:        Apache-2.0
URL:            https://github.com/noironetworks/apicapi/
Source:         https://github.com/noironetworks/apicapi/archive/%{version}.tar.gz
# https://github.com/noironetworks/apicapi/pull/85
Source99:       http://www.apache.org/licenses/LICENSE-2.0.txt
Patch1:         python-apicapi-disableparseconfigtest.patch
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module WebOb}
BuildRequires:  %{python_module click >= 5.1}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module oslo.config >= 1.4.0}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testtools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-SQLAlchemy
Requires:       python-click >= 5.1
Requires:       python-oslo.config >= 1.4.0
Requires:       python-pyOpenSSL
Requires:       python-requests
BuildArch:      noarch
%python_subpackages

%description
This library provides an interface for the APIC REST API, for use by
the other Cisco APIC Python packages.

%prep
%setup -q -n %{sname}-%{version}
%patch1 -p1
cp %{SOURCE99} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Install other supporting files (like bash_completions)
install -p -D -m 644 etc/apic.bash_completion \
    %{buildroot}%{_datadir}/bash-completion/completions/apic

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m unittest discover -s apicapi/tests/unit

%files %{python_files}
%license LICENSE-2.0.txt
%doc AUTHORS README.rst
%{python_sitelib}/%{sname}
%{python_sitelib}/%{sname}-%{version}*.egg-info
%{_bindir}/apic
%{_bindir}/apic-bond-watch
%{_datadir}/bash-completion/completions/apic

%changelog
