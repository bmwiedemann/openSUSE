#
# spec file for package python-certstream
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-certstream
Version:        1.11
Release:        0
Summary:        Python library for receiving certificate transparency list updates
License:        MIT
URL:            https://github.com/CaliDog/certstream-python/
Source0:        https://files.pythonhosted.org/packages/source/c/certstream/certstream-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 18.0.1}
#SECTION tests
BuildRequires:  %{python_module termcolor}
BuildRequires:  %{python_module websocket-client >= 0.48.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
# /SECTION
Requires:       python3-termcolor
Requires:       python3-websocket-client >= 0.48.0
BuildArch:      noarch

%python_subpackages

%description
Certstream is a library to connect to the certstream network (certstream.calidog.io).

It supports automatic reconnection when networks issues occur, and should be stable for long-running jobs.

%prep
%setup -q -n certstream-%{version}
# do not hardcode dependencies
sed -i -e 's:==:>=:g' requirements.txt

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/certstream
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# there are no tests

%post
%python_install_alternative certstream

%postun
%python_uninstall_alternative certstream

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/certstream/
%{python_sitelib}/certstream-%{version}-py*.egg-info
%python_alternative %{_bindir}/certstream

%changelog
