#
# spec file for package python-certstream
#
# Copyright (c) 2025 SUSE LLC
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


%bcond_without libalternatives
Name:           python-certstream
Version:        1.12
Release:        0
Summary:        Python library for receiving certificate transparency list updates
License:        MIT
URL:            https://github.com/CaliDog/certstream-python/
Source0:        https://files.pythonhosted.org/packages/source/c/certstream/certstream-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 18.0.1}
BuildRequires:  %{python_module wheel}
#SECTION tests
BuildRequires:  %{python_module termcolor}
BuildRequires:  %{python_module websocket-client >= 0.58.0}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
# /SECTION
Requires:       python3-termcolor
Requires:       python3-websocket-client >= 0.48.0
BuildArch:      noarch

%python_subpackages

%description
Certstream is a library to connect to the certstream network (certstream.calidog.io).

It supports automatic reconnection when networks issues occur, and should be stable for long-running jobs.

%prep
%autosetup -p1 -n certstream-%{version}
# do not hardcode dependencies
sed -i -e 's:==:>=:g' requirements.txt

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/certstream
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# there are no tests

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative certstream

# post and postun macro call is not needed with only libalternatives

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/certstream/
%{python_sitelib}/certstream-%{version}*-info
%python_alternative %{_bindir}/certstream

%changelog
