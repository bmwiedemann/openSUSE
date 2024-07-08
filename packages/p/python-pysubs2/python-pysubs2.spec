#
# spec file for package python-pysubs2
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
Name:           python-pysubs2
Version:        1.7.2
Release:        0
Summary:        Python library for editing subtitle files
License:        MIT
Group:          Development/Languages/Python
URL:            https://pysubs2.readthedocs.io
Source0:        https://files.pythonhosted.org/packages/source/p/pysubs2/pysubs2-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
pysubs2 is a Python library for editing subtitle files. It’s based on
SubStation Alpha, the native format of Aegisub; it also supports SubRip (SRT),
MicroDVD, MPL2, TMP and WebVTT formats and OpenAI Whisper captions.

There is a small CLI tool for batch conversion and retiming.

%prep
%autosetup -p1 -n pysubs2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pysubs2
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pysubs2

%postun
%python_uninstall_alternative pysubs2

%check
# online tests only

%files %{python_files}
%license LICENSE.txt
%doc README.md
%python_alternative %{_bindir}/pysubs2
%{python_sitelib}/pysubs2
%{python_sitelib}/pysubs2-%{version}.dist-info

%changelog
