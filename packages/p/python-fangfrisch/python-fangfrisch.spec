#
# spec file for package python-fangfrisch
#
# Copyright (c) 2024 SUSE LLC
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


%define skip_python2 1
Name:           python-fangfrisch
Version:        1.9.0
Release:        0
Summary:        Update and verify unofficial Clam Anti-Virus signatures
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/rseichter/fangfrisch
Source:         https://github.com/rseichter/fangfrisch/archive/refs/tags/%{version}.tar.gz
BuildRequires:  %{python_module SQLAlchemy}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-SQLAlchemy
Requires:       python-requests
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Fangfrisch (German for "freshly caught") is a sibling of the Clam
Anti-Virus freshclam utility. It allows downloading virus definition
files that are not official ClamAV canon, e.g. from Sanesecurity and
URLhaus. Fangfrisch was designed with security in mind, to be run by an
unprivileged user only.

%prep
%autosetup -p1 -n fangfrisch-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests
%python_clone -a %{buildroot}%{_bindir}/fangfrisch

%post
%python_install_alternative fangfrisch

%postun
%python_uninstall_alternative fangfrisch

%check
# make check wants to do network... cant do this in OBS
#python_expand script -eqc "pytest-%%{$python_version} -vv -s" /dev/null

%files %{python_files}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{_bindir}/fangfrisch
%{python_sitelib}/fangfrisch
%{python_sitelib}/fangfrisch-%{version}*-info
%python_alternative %{_bindir}/fangfrisch

%changelog
