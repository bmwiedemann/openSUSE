#
# spec file for package python-glad2
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


%define pythons python3
Name:           python-glad2
Version:        2.0.8
Release:        0
Summary:        Command line utility to load/generate multi-language GL/GLES/EGL/GLX/WGL code
License:        MIT
URL:            https://github.com/Dav1dde/glad
Source0:        https://files.pythonhosted.org/packages/source/g/glad2/glad2-%{version}.tar.gz
Source1:        python-glad2-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools > 61.0
BuildRequires:  python3-wheel
Requires:       python3-Jinja2
Provides:       glad
Obsoletes:      python311-glad2 < %{version}
Obsoletes:      python312-glad2 < %{version}
Obsoletes:      python313-glad2 < %{version}
BuildArch:      noarch
%python_subpackages

%description
Glad is a command line utility to generate GL/GLES/EGL/GLX/WGL loader code
based on the official specifications for using as bundled source code with
apps.

%prep
%autosetup -n glad2-%{version}
sed -Ei "1{\@%{_bindir}/env python@d}" glad/__main__.py

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{python3_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{_bindir}/glad
%{python3_sitelib}/glad/
%{python3_sitelib}/glad2-%{version}*.*-info

%changelog
