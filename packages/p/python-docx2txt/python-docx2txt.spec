#
# spec file for package python-docx2txt
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-docx2txt
Version:        0.9
Release:        0
Summary:        A pure python-based utility to extract text and images from docx files
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ankushshah89/python-docx2txt
Source:         https://files.pythonhosted.org/packages/source/d/docx2txt/docx2txt-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
A pure python-based utility to extract text and images from docx files. It can however also extract text from header, footer and hyperlinks.

%prep
%autosetup -p1 -n docx2txt-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/docx2txt
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre
%python_reset_alternative docx2txt

%post
%python_install_alternative docx2txt

%postun
%python_uninstall_alternative docx2txt

%files %{python_files}
%license LICENSE.txt
%python_alternative %{_bindir}/docx2txt
%{python_sitelib}/docx2txt
%{python_sitelib}/docx2txt-%{version}.dist-info

%changelog
