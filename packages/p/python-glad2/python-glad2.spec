#
# spec file for package python-glad2
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


%{?sle15_python_module_pythons}
Name:           python-glad2
Version:        2.0.6
Release:        0
Summary:        Multi-Language GL/GLES/EGL/GLX/WGL Loader-Generator
License:        MIT
URL:            https://github.com/Dav1dde/glad
Source:         https://files.pythonhosted.org/packages/source/g/glad2/glad2-%{version}.tar.gz
Source1:        python-glad2-rpmlintrc
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Jinja2}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Jinja2
Requires:       python-setuptools
BuildArch:      noarch
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
%python_subpackages

%description
Multi-Language GL/GLES/EGL/GLX/WGL Loader-Generator based on the official specifications.

%prep
%setup -q -n glad2-%{version}

%build
%python_build

%install
find %(buildroot) -name 'glsc2.*' -delete # empty files
%python_install
%python_clone -a %{buildroot}%{_bindir}/glad
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative glad

%postun
%python_uninstall_alternative glad

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/glad
%{python_sitelib}/*

%changelog
