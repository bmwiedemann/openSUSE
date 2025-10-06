#
# spec file for package python-knowit
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-knowit
Version:        0.5.11
Release:        0
Summary:        Extract information from video files
License:        MIT
URL:            https://github.com/ratoaq2/knowit
Source0:        https://files.pythonhosted.org/packages/source/k/knowit/knowit-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires:       python-Pint >= 0.20.1
Requires:       python-PyYAML >= 6.0
Requires:       python-babelfish >= 0.6.1
Requires:       python-enzyme >= 0.5.2
Requires:       python-pymediainfo >= 6.0.1
Requires:       python-trakit >= 0.2.2

BuildArch:      noarch
%python_subpackages

%description
To extract information from video files.

%prep
%autosetup -n knowit-%{version}
chmod -x knowit/provider.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/knowit
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative knowit

%postun
%python_uninstall_alternative knowit

%files %{python_files}
%license LICENSE
%doc README.md
%python_alternative %{_bindir}/knowit
%{python_sitelib}/knowit
%{python_sitelib}/knowit-%{version}.dist-info

%changelog
