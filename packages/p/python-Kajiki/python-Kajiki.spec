#
# spec file for package python-Kajiki
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


Name:           python-Kajiki
Version:        0.9.2
Release:        0
Summary:        Compiler for Genshi syntax outputting Python bytecode
License:        MIT
URL:            https://github.com/nandoflorestan/kajiki
Source:         https://github.com/jackrosenthal/kajiki/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}-gh.tar.gz
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module linetable}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires:       python-linetable
BuildArch:      noarch
%python_subpackages

%description
Kajiki compiles Genshi-like syntax to Python bytecode.

(Genshi is a Python library parsing, generating, and processing HTML, XML or
other textual content for output generation on the web.)

%prep
%setup -q -n kajiki-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/kajiki
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative kajiki

%postun
%python_uninstall_alternative kajiki

%check
# tests fail on 32-bit platform as they expect 64-bit int
%ifnarch %arm32 %ix86 s390 ppc
%pytest
%endif

%files %{python_files}
%python_alternative %{_bindir}/kajiki
%license LICENSE.rst
%doc README.rst
%{python_sitelib}/kajiki
%{python_sitelib}/kajiki-%{version}.dist-info

%changelog
