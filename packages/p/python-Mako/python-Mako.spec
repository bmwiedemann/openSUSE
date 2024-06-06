#
# spec file for package python-Mako
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

%{?sle15_python_module_pythons}
Name:           python-Mako
Version:        1.3.5
Release:        0
Summary:        A Python templating language
License:        MIT
URL:            https://www.makotemplates.org/
Source:         https://files.pythonhosted.org/packages/source/M/Mako/Mako-%{version}.tar.gz
BuildRequires:  %{python_module MarkupSafe >= 0.9.2}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros >= 20210929
Requires:       python-MarkupSafe >= 0.9.2
Requires:       python-setuptools
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
BuildArch:      noarch
Recommends:     python-Beaker >= 1.1
Provides:       python-mako = %{version}
Obsoletes:      python-mako < %{version}
%python_subpackages

%description
Mako is a template library written in Python. It provides a non-XML
syntax which compiles into Python modules for performance. Mako's
syntax and API borrows from Django templates, Cheetah, Myghty, and
Genshi. Conceptually, Mako is an embedded Python (i.e. Python Server
Page) language, which refines the ideas of componentized layout and
inheritance, while maintaining close ties to Python calling and
scoping semantics.

%prep
%setup -q -n Mako-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/mako-render
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative mako-render

%post
%python_install_alternative mako-render

%postun
%python_uninstall_alternative mako-render

%files %{python_files}
%license LICENSE
%doc CHANGES README.rst
%doc examples
%python_alternative %{_bindir}/mako-render
%{python_sitelib}/mako/
%{python_sitelib}/Mako-%{version}-py*.egg-info

%changelog
